// Supabase Edge Function "remind": runs every hour. At each learner's chosen hour (8pm by default), if they studied
// yesterday but not yet today, it sends "N hours left to keep your streak". The notification keys are made once and
// kept in the private push_keys table, so no secret ever leaves the project. GET ?key=1 returns the public key.
import webpush from "npm:web-push@3.6.7";
import { createClient } from "npm:@supabase/supabase-js@2";

const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS", "Content-Type": "application/json" };

async function keys() {
  const { data } = await db.from("push_keys").select("public_key, private_key").eq("id", 1).maybeSingle();
  if (data) return data;
  const k = webpush.generateVAPIDKeys();
  await db.from("push_keys").insert({ id: 1, public_key: k.publicKey, private_key: k.privateKey });
  return { public_key: k.publicKey, private_key: k.privateKey };
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const k = await keys();
  if (new URL(req.url).searchParams.get("key")) return new Response(JSON.stringify({ key: k.public_key }), { headers: CORS });
  webpush.setVapidDetails("mailto:noreply@waseemmatlub.github.io", k.public_key, k.private_key);
  const now = Date.now();
  const { data: subs } = await db.from("push_subs").select("*");
  let sent = 0;
  for (const s of subs ?? []) {
    const local = now - s.tz_offset * 60000;                       // tz_offset is the browser's getTimezoneOffset()
    const day = Math.floor(local / 864e5), hour = new Date(local).getUTCHours();
    if (hour !== s.remind_hour || s.last_reminded === day) continue;
    if (!(s.streak > 0 && s.last_study_day === day - 1)) continue;  // only when a streak is about to be lost
    const left = 24 - hour;
    try {
      await webpush.sendNotification({ endpoint: s.endpoint, keys: { p256dh: s.p256dh, auth: s.auth } },
        JSON.stringify({ title: "Keep your streak going", body: `${left} hour${left > 1 ? "s" : ""} left today to keep your ${s.streak}-day streak.` }));
      sent++;
      await db.from("push_subs").update({ last_reminded: day }).eq("id", s.id);
    } catch (e) {
      const code = (e as { statusCode?: number }).statusCode;
      if (code === 404 || code === 410) await db.from("push_subs").delete().eq("id", s.id);   // the device unsubscribed
    }
  }
  return new Response(JSON.stringify({ sent }), { headers: CORS });
});
