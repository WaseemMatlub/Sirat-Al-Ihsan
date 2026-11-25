-- Ihsan leaderboard. Run once in Supabase: SQL Editor -> New query -> paste -> Run.
-- No accounts: each device makes a random id and a secret code. Only the id, nickname and points can be read;
-- points change only through submit_score, which checks the code and limits how fast points can grow.

drop function if exists public.submit_score(text, integer, integer, integer);
drop function if exists public.leave_leaderboard();
drop table if exists public.leaderboard;

create table public.leaderboard (
  id          uuid primary key,
  secret_hash text not null,
  name        text not null check (char_length(name) between 2 and 20 and name !~ '[<>]'),
  xp          integer not null default 0,
  week_xp     integer not null default 0,
  week_start  date not null default (date_trunc('week', now()))::date,
  streak      integer not null default 0,
  updated_at  timestamptz not null default now()
);
alter table public.leaderboard enable row level security;
create policy "anyone can read the leaderboard" on public.leaderboard for select using (true);
revoke all on public.leaderboard from anon, authenticated;
grant select (id, name, xp, week_xp, week_start, streak) on public.leaderboard to anon, authenticated;   -- never the secret
create index leaderboard_week on public.leaderboard (week_start, week_xp desc);
create index leaderboard_all on public.leaderboard (xp desc);

create or replace function public.submit_score(p_id uuid, p_secret text, p_name text, p_total integer, p_gain integer, p_streak integer)
returns void language plpgsql security definer set search_path = public as $$
declare r public.leaderboard; wk date := (date_trunc('week', now()))::date; g integer := least(greatest(coalesce(p_gain,0), 0), 400);
        h text := encode(sha256(convert_to(coalesce(p_secret,''), 'UTF8')), 'hex');
begin
  if char_length(coalesce(p_secret,'')) < 20 then raise exception 'bad code'; end if;
  select * into r from public.leaderboard where id = p_id;
  if not found then
    insert into public.leaderboard (id, secret_hash, name, xp, week_xp, week_start, streak)
    values (p_id, h, p_name, least(greatest(coalesce(p_total,0), 0), 5000), g, wk, least(greatest(coalesce(p_streak,0), 0), 365));
    return;
  end if;
  if r.secret_hash <> h then raise exception 'bad code'; end if;
  if r.updated_at > now() - interval '30 seconds' then g := 0; end if;      -- at most one gain every 30 seconds
  update public.leaderboard set
    name       = p_name,
    xp         = r.xp + g,
    week_xp    = case when r.week_start = wk then r.week_xp + g else g end,
    week_start = wk,
    streak     = least(greatest(coalesce(p_streak,0), 0), r.streak + 1),
    updated_at = case when g > 0 then now() else r.updated_at end
  where id = p_id;
end $$;

create or replace function public.leave_leaderboard(p_id uuid, p_secret text)
returns void language sql security definer set search_path = public as $$
  delete from public.leaderboard where id = p_id and secret_hash = encode(sha256(convert_to(coalesce(p_secret,''), 'UTF8')), 'hex');
$$;

revoke all on function public.submit_score(uuid, text, text, integer, integer, integer) from public;
revoke all on function public.leave_leaderboard(uuid, text) from public;
grant execute on function public.submit_score(uuid, text, text, integer, integer, integer) to anon, authenticated;
grant execute on function public.leave_leaderboard(uuid, text) to anon, authenticated;
