-- Ihsan leaderboard. Run once in Supabase: SQL Editor -> New query -> paste -> Run.
-- Learners join with an anonymous account (no email). Anyone can read the board; scores change only through submit_score,
-- which limits how fast points can grow so it can't simply be overwritten.

create table if not exists public.leaderboard (
  user_id    uuid primary key references auth.users(id) on delete cascade,
  name       text not null check (char_length(name) between 2 and 20 and name !~ '[<>]'),
  xp         integer not null default 0,
  week_xp    integer not null default 0,
  week_start date not null default (date_trunc('week', now()))::date,
  streak     integer not null default 0,
  updated_at timestamptz not null default now()
);
alter table public.leaderboard enable row level security;
drop policy if exists "anyone can read the leaderboard" on public.leaderboard;
create policy "anyone can read the leaderboard" on public.leaderboard for select using (true);
create index if not exists leaderboard_week on public.leaderboard (week_start, week_xp desc);
create index if not exists leaderboard_all on public.leaderboard (xp desc);

create or replace function public.submit_score(p_name text, p_total integer, p_gain integer, p_streak integer)
returns void language plpgsql security definer set search_path = public as $$
declare r public.leaderboard; wk date := (date_trunc('week', now()))::date; g integer := least(greatest(coalesce(p_gain,0), 0), 400);
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  select * into r from public.leaderboard where user_id = auth.uid();
  if not found then
    insert into public.leaderboard (user_id, name, xp, week_xp, week_start, streak)
    values (auth.uid(), p_name, least(greatest(coalesce(p_total,0), 0), 5000), g, wk, least(greatest(coalesce(p_streak,0), 0), 365));
    return;
  end if;
  if r.updated_at > now() - interval '30 seconds' then g := 0; end if;      -- at most one gain every 30 seconds
  update public.leaderboard set
    name       = p_name,
    xp         = r.xp + g,
    week_xp    = case when r.week_start = wk then r.week_xp + g else g end,
    week_start = wk,
    streak     = least(greatest(coalesce(p_streak,0), 0), r.streak + 1),
    updated_at = case when g > 0 then now() else r.updated_at end
  where user_id = auth.uid();
end $$;

create or replace function public.leave_leaderboard()
returns void language sql security definer set search_path = public as $$
  delete from public.leaderboard where user_id = auth.uid();
$$;

revoke all on function public.submit_score(text, integer, integer, integer) from public, anon;
revoke all on function public.leave_leaderboard() from public, anon;
grant execute on function public.submit_score(text, integer, integer, integer) to authenticated;
grant execute on function public.leave_leaderboard() to authenticated;
