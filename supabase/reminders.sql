-- Streak reminders. Run once in Supabase SQL Editor after deploying the "remind" Edge Function.
create table if not exists public.push_keys (id int primary key, public_key text not null, private_key text not null);
alter table public.push_keys enable row level security;
revoke all on public.push_keys from anon, authenticated;

create table if not exists public.push_subs (
  id uuid primary key, secret_hash text not null,
  endpoint text not null, p256dh text not null, auth text not null,
  tz_offset int not null default 0, remind_hour int not null default 20 check (remind_hour between 0 and 23),
  streak int not null default 0, last_study_day int not null default 0, last_reminded int not null default 0,
  updated_at timestamptz not null default now());
alter table public.push_subs enable row level security;
revoke all on public.push_subs from anon, authenticated;

create or replace function public.save_push(p_id uuid, p_secret text, p_endpoint text, p_p256dh text, p_auth text, p_tz int, p_hour int, p_streak int, p_day int)
returns void language plpgsql security definer set search_path = public as $$
declare h text := encode(sha256(convert_to(coalesce(p_secret,''), 'UTF8')), 'hex'); old text;
begin
  if char_length(coalesce(p_secret,'')) < 20 or char_length(coalesce(p_endpoint,'')) > 1000 or p_endpoint !~ '^https://' then raise exception 'bad request'; end if;
  select secret_hash into old from public.push_subs where id = p_id;
  if found and old <> h then raise exception 'bad code'; end if;
  insert into public.push_subs (id, secret_hash, endpoint, p256dh, auth, tz_offset, remind_hour, streak, last_study_day)
  values (p_id, h, p_endpoint, p_p256dh, p_auth, least(greatest(p_tz,-840),840), least(greatest(p_hour,0),23), greatest(p_streak,0), p_day)
  on conflict (id) do update set endpoint = excluded.endpoint, p256dh = excluded.p256dh, auth = excluded.auth, tz_offset = excluded.tz_offset,
    remind_hour = excluded.remind_hour, streak = excluded.streak, last_study_day = excluded.last_study_day, updated_at = now();
end $$;

create or replace function public.push_progress(p_id uuid, p_secret text, p_streak int, p_day int)
returns void language sql security definer set search_path = public as $$
  update public.push_subs set streak = greatest(p_streak,0), last_study_day = p_day, updated_at = now()
  where id = p_id and secret_hash = encode(sha256(convert_to(coalesce(p_secret,''), 'UTF8')), 'hex');
$$;

create or replace function public.remove_push(p_id uuid, p_secret text)
returns void language sql security definer set search_path = public as $$
  delete from public.push_subs where id = p_id and secret_hash = encode(sha256(convert_to(coalesce(p_secret,''), 'UTF8')), 'hex');
$$;

revoke all on function public.save_push(uuid,text,text,text,text,int,int,int,int), public.push_progress(uuid,text,int,int), public.remove_push(uuid,text) from public;
grant execute on function public.save_push(uuid,text,text,text,text,int,int,int,int), public.push_progress(uuid,text,int,int), public.remove_push(uuid,text) to anon, authenticated;

-- run the reminder check at the top of every hour
create extension if not exists pg_cron;
create extension if not exists pg_net;
select cron.unschedule('streak-reminders') where exists (select 1 from cron.job where jobname = 'streak-reminders');
select cron.schedule('streak-reminders', '0 * * * *',
  $$ select net.http_post(url := 'https://xzjwitslughozgywmcvi.supabase.co/functions/v1/remind', headers := '{"Content-Type":"application/json","Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh6andpdHNsdWdob3pneXdtY3ZpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTU2MDIyNjIsImV4cCI6MjExMTE3ODI2Mn0.vD1x56sRkHBRk2Yg203Tkqyy1Pto5Kk8iF_PoIR-MBI"}'::jsonb, body := '{}'::jsonb) $$);
