-- Live classes. Run once in Supabase: SQL Editor -> New query -> paste -> Run.
-- Teachers get a private teacher code from the madrasa (see "Add a teacher" at the bottom). Students need no account.
-- Anyone can see the timetable and recordings; only a teacher with a valid code can start, schedule or end a class.

create extension if not exists pgcrypto;

create table if not exists public.teachers (
  id        uuid primary key default gen_random_uuid(),
  name      text not null check (char_length(name) between 2 and 60),
  code_hash text not null unique,
  active    boolean not null default true
);
alter table public.teachers enable row level security;
revoke all on public.teachers from anon, authenticated;

create table if not exists public.classes (
  id          uuid primary key default gen_random_uuid(),
  teacher_id  uuid not null references public.teachers(id),
  teacher     text not null,
  book_id     text,
  book_title  text not null check (char_length(book_title) between 2 and 120),
  topic       text check (char_length(topic) <= 200),
  starts_at   timestamptz not null default now(),
  status      text not null default 'scheduled' check (status in ('scheduled','live','ended')),
  room        text not null,
  recording   text,          -- link to the refined recording, added after the class
  transcript  text,          -- link to the transcript and chapters
  created_at  timestamptz not null default now()
);
alter table public.classes enable row level security;
create policy "anyone can see classes" on public.classes for select using (true);
revoke all on public.classes from anon, authenticated;
grant select on public.classes to anon, authenticated;
create index if not exists classes_when on public.classes (starts_at desc);

create or replace function public.teacher_from_code(p_code text) returns public.teachers
language sql security definer set search_path = public as $$
  select * from public.teachers where code_hash = encode(digest(coalesce(p_code,''), 'sha256'), 'hex') and active limit 1 $$;

-- Check a teacher code: returns the teacher's name, or raises an error
create or replace function public.teacher_login(p_code text) returns text
language plpgsql security definer set search_path = public as $$
declare t public.teachers := public.teacher_from_code(p_code);
begin if t.id is null then raise exception 'unknown teacher code'; end if; return t.name; end $$;

-- Start a class now, or schedule one for later. Returns the class id.
create or replace function public.class_create(p_code text, p_book_id text, p_book_title text, p_topic text, p_starts_at timestamptz, p_live boolean)
returns uuid language plpgsql security definer set search_path = public as $$
declare t public.teachers := public.teacher_from_code(p_code); new_id uuid := gen_random_uuid();
begin
  if t.id is null then raise exception 'unknown teacher code'; end if;
  insert into public.classes (id, teacher_id, teacher, book_id, book_title, topic, starts_at, status, room)
  values (new_id, t.id, t.name, p_book_id, p_book_title, p_topic, coalesce(p_starts_at, now()),
          case when p_live then 'live' else 'scheduled' end,
          'DarAsSiddiq-' || replace(new_id::text, '-', ''));
  return new_id;
end $$;

-- Go live, end, or delete one of your own classes
create or replace function public.class_set(p_code text, p_id uuid, p_status text) returns void
language plpgsql security definer set search_path = public as $$
declare t public.teachers := public.teacher_from_code(p_code);
begin
  if t.id is null then raise exception 'unknown teacher code'; end if;
  if p_status = 'deleted' then delete from public.classes where id = p_id and teacher_id = t.id and status <> 'ended'; return; end if;
  if p_status not in ('live','ended') then raise exception 'bad status'; end if;
  update public.classes set status = p_status, starts_at = case when p_status = 'live' then now() else starts_at end
  where id = p_id and teacher_id = t.id;
end $$;

grant execute on function public.teacher_login(text), public.class_create(text, text, text, text, timestamptz, boolean), public.class_set(text, uuid, text) to anon, authenticated;
revoke execute on function public.teacher_from_code(text) from anon, authenticated, public;

-- Add a teacher (run this yourself, once per teacher; give them the code privately):
--   insert into public.teachers (name, code_hash) values ('Sufi Rahim', encode(digest('choose-a-long-secret-code', 'sha256'), 'hex'));
-- Add a refined recording after a class:
--   update public.classes set recording = 'https://...', transcript = 'https://...' where id = '...';
