/* ============================ TOOLS: Qibla, Qada', Zakat, Inheritance, Hajj guides, Salawat ============================
   All work offline. Inheritance follows Mukhtasar al-Quduri, Book of Inheritance (Hanafi). */
let GUIDES = null, SALAWAT = null;
const loadGuides = async () => GUIDES || (GUIDES = await fetch("data/guides.json").then(r => r.json()).catch(() => []));
const loadSalawat = async () => SALAWAT || (SALAWAT = await fetch("data/salawat.json").then(r => r.json()).catch(() => null));
const TOOL_ICON = {
  qibla:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/></svg>',
  qada:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="4" y="5" width="16" height="15" rx="2"/><path d="M8 3v4M16 3v4M4 10h16M9 15l2 2 4-4"/></svg>',
  zakat:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><ellipse cx="12" cy="7" rx="7" ry="3"/><path d="M5 7v5c0 1.7 3.1 3 7 3s7-1.3 7-3V7M5 12v5c0 1.7 3.1 3 7 3s7-1.3 7-3v-5"/></svg>',
  inherit:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="18" r="2.5"/><circle cx="12" cy="18" r="2.5"/><circle cx="19" cy="18" r="2.5"/><path d="M12 7.5V15.5M12 11H5v4.5M12 11h7v4.5"/></svg>',
  kaaba:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M4 7l8-3 8 3v11l-8 3-8-3z"/><path d="M4 7l8 3 8-3M12 10v11M4 11l8 3 8-3"/></svg>',
  salawat:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
};
function toolsView(){
  const row = (go, ico, t, s) => `<button class="item tool" ${go}><span class="sr-ico">${TOOL_ICON[ico]}</span><span style="min-width:0"><span class="t">${t}</span><br><span class="s">${s}</span></span><span aria-hidden="true">›</span></button>`;
  return shell(`<h1>Tools</h1><p class="muted" style="margin:0 0 14px">They all work without internet.</p>
    <p class="label">Prayer</p><div class="stack">
      ${row('data-go="qibla"', "qibla", "Qibla finder", "Point your phone to the Ka'bah")}
      ${row('data-go="qada"', "qada", "Qada' prayers", "Work out missed prayers and track making them up")}</div>
    <p class="label">Wealth</p><div class="stack">
      ${row('data-go="zakat"', "zakat", "Zakat calculator", "Hanafi nisab, gold, silver, cash and trade goods")}
      ${row('data-go="inherit"', "inherit", "Inheritance calculator", "Shares by the Hanafi school, from al-Quduri")}</div>
    <p class="label">Pilgrimage</p><div class="stack">
      ${row('data-guide="umrah"', "kaaba", "How to perform 'Umrah", "Step by step, tick off as you go")}
      ${row('data-guide="hajj"', "kaaba", "How to perform Hajj", "Tamattu', from the 'umrah to the farewell tawaf")}</div>
    <p class="label">Remembrance</p><div class="stack">
      ${row('data-go="salawat"', "salawat", "Salawat on the Prophet ﷺ", "Durood Ibrahimi, Taj, Tunjina, Khizri and more, with sources")}</div>`);
}

/* ---------------- Guides ---------------- */
function guideView(id){
  if (!GUIDES) { loadGuides().then(render); return shell(`<p class="muted">Loading…</p>`); }
  const g = GUIDES.find(x => x.id === id); if (!g) return shell(`<p class="muted">Not found.</p>`);
  const done = (S.guides||{})[id] || [], n = g.steps.length, d = done.length;
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1 style="margin-bottom:2px">${esc(g.title)}</h1>
    <p class="muted" style="margin:0 0 10px">${esc(g.sub)}. From ${esc(g.src)}.</p>
    <div class="topic-p" style="margin-bottom:14px"><span class="bar" style="flex:1;height:6px"><i style="width:${Math.max(2, d/n*100)}%;background:var(--brand)"></i></span><span class="small muted">${d} of ${n}</span></div>
    <ol class="gsteps">${g.steps.map((s, i) => { const on = done.includes(i);
      return `<li class="gstep ${on ? "on" : ""}"><div class="gs-h"><span class="gs-n">${on ? ICON.check.replace("<svg",'<svg width="14" height="14"') : i+1}</span><h3>${esc(s.t)}</h3></div>
        <ul>${s.do.map(x => `<li>${esc(x)}</li>`).join("")}</ul>
        ${s.say ? `<div class="gs-say"><p class="ar" lang="ar" dir="rtl">${esc(s.say.ar)}</p><p class="small"><i>${esc(s.say.tr)}</i></p><p class="small">${esc(s.say.en)}</p></div>` : ""}
        ${s.note ? `<p class="gs-note">${esc(s.note)}</p>` : ""}
        <div class="gs-f"><span class="small muted">${esc(s.src)}</span><button class="btn small-btn ${on ? "ghost" : ""}" data-gstep="${i}" aria-pressed="${on}">${on ? "Done" : "Mark as done"}</button></div></li>`; }).join("")}</ol>
    ${d ? `<button class="linkbtn" id="greset">Start again</button>` : ""}`);
}

/* ---------------- Qibla ---------------- */
const KAABA = [21.422487, 39.826206];
function qiblaBearing(lat, lon){ const r = x => x * Math.PI / 180, [kl, ko] = KAABA.map(r), p = r(lat), dl = ko - r(lon);
  return (Math.atan2(Math.sin(dl), Math.cos(p) * Math.tan(kl) - Math.sin(p) * Math.cos(dl)) * 180 / Math.PI + 360) % 360; }
function kaabaKm(lat, lon){ const r = x => x * Math.PI / 180, [a, b] = KAABA;
  const h = Math.sin(r(a-lat)/2)**2 + Math.cos(r(lat))*Math.cos(r(a))*Math.sin(r(b-lon)/2)**2; return 6371 * 2 * Math.asin(Math.sqrt(h)); }
let QB = null;
function qiblaView(){
  const q = S.qibla;
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1>Qibla finder</h1>
    ${q ? `<div class="compass-wrap"><div class="compass" id="compass" role="img" aria-label="Qibla is ${Math.round(q.b)} degrees from north">
        <div class="dial" id="dial"><span class="n">N</span><span class="e">E</span><span class="s">S</span><span class="w">W</span>
        <div class="needle" style="transform:rotate(${q.b}deg)"><span class="kb">${TOOL_ICON.kaaba}</span></div></div><span class="mark" aria-hidden="true"></span></div></div>
      <p class="qb-big">${Math.round(q.b)}° <span class="muted small">from north</span></p>
      <p class="small muted" style="text-align:center" id="qstat">${"DeviceOrientationEvent" in window ? "Hold your phone flat. The Ka'bah symbol points to the qiblah." : "Use a compass: face " + Math.round(q.b) + "° from north."}</p>
      <p class="small muted" style="text-align:center">About ${Math.round(kaabaKm(q.lat, q.lon)).toLocaleString()} km to the Ka'bah</p>
      <div class="btnrow"><button class="btn ghost" id="qcomp">Use compass</button><button class="btn ghost" id="qloc">Update location</button></div>`
    : `<p>Allow location once and the qiblah is worked out on your phone. Your location is not sent anywhere.</p><button class="btn" id="qloc">Find the qiblah</button>`}
    <details class="manual" style="margin-top:16px"><summary>Enter a location by hand</summary>
      <div class="frow"><label>Latitude<input id="qlat" inputmode="decimal" value="${q ? q.lat.toFixed(4) : ""}" placeholder="53.8008"></label><label>Longitude<input id="qlon" inputmode="decimal" value="${q ? q.lon.toFixed(4) : ""}" placeholder="-1.5491"></label></div>
      <button class="btn ghost" id="qset">Use these</button></details>
    <p class="small muted" style="margin-top:14px">Phone compasses can be thrown off by metal and magnets. Calibrate by moving the phone in a figure of eight. For the prayer, the direction of the Ka'bah is what counts; a small difference is excused.</p>`);
}
function bindQibla(){
  const set = (lat, lon) => { S.qibla = { lat, lon, b: qiblaBearing(lat, lon) }; save(); render(); };
  const ql = $("#qloc"); if (ql) ql.onclick = () => { if (!navigator.geolocation) return toast("Location isn't available on this device");
    ql.disabled = true; ql.textContent = "Finding you…";
    navigator.geolocation.getCurrentPosition(p => set(p.coords.latitude, p.coords.longitude), () => { toast("Location was not allowed. You can enter it by hand below."); render(); }, { enableHighAccuracy:false, timeout:15000, maximumAge:3600000 }); };
  const qs = $("#qset"); if (qs) qs.onclick = () => { const a = parseFloat($("#qlat").value), b = parseFloat($("#qlon").value);
    if (!(a >= -90 && a <= 90 && b >= -180 && b <= 180)) return toast("Enter a latitude (−90 to 90) and longitude (−180 to 180)"); set(a, b); };
  const qc = $("#qcomp"); if (qc) qc.onclick = async () => {
    try { if (typeof DeviceOrientationEvent !== "undefined" && DeviceOrientationEvent.requestPermission) { const r = await DeviceOrientationEvent.requestPermission(); if (r !== "granted") return toast("Compass permission was not given"); } } catch(e){}
    if (QB) window.removeEventListener("deviceorientationabsolute", QB), window.removeEventListener("deviceorientation", QB);
    QB = e => { const dial = $("#dial"); if (!dial) return window.removeEventListener("deviceorientation", QB);
      let h = e.webkitCompassHeading; if (h == null && e.absolute && e.alpha != null) h = 360 - e.alpha; if (h == null) return;
      dial.style.transform = `rotate(${-h}deg)`; const off = ((S.qibla.b - h) % 360 + 540) % 360 - 180;
      const st = $("#qstat"); if (st) st.textContent = Math.abs(off) < 4 ? "You are facing the qiblah" : `Turn ${off > 0 ? "right" : "left"} ${Math.round(Math.abs(off))}°`; };
    window.addEventListener("ondeviceorientationabsolute" in window ? "deviceorientationabsolute" : "deviceorientation", QB); qc.textContent = "Compass on"; };
}

/* ---------------- Qada' ---------------- */
const QP = [["fajr","Fajr"],["zuhr","Zuhr"],["asr","'Asr"],["maghrib","Maghrib"],["isha","'Isha'"],["witr","Witr"]];
function qadaCount(from, to, female, hayd, nifas){
  const d0 = Date.parse(from), d1 = Date.parse(to); if (!(d1 > d0)) return null;
  let days = Math.round((d1 - d0) / 864e5);
  if (female) { const months = days / 29.53; days = Math.max(0, Math.round(days - months * Math.min(10, Math.max(0, hayd||0)) - (nifas||0))); }
  return days;
}
function qadaView(){
  const Q = S.qada || { left:{}, fasts:0 }, c = S.qadaCalc || {}, total = QP.reduce((a,[k]) => a + (Q.left[k]||0), 0);
  const days = c.from && c.to ? qadaCount(c.from, c.to, c.female, c.hayd, c.nifas) : null;
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1>Qada' prayers</h1>
    <p class="muted" style="margin:0 0 12px">Every missed fard prayer, and witr (wajib in the Hanafi school), stays owed until it is made up. <span class="small">Nur al-Idah, making up missed prayers.</span></p>
    <section class="card pad"><h2 style="margin-top:0">Work it out</h2>
      <div class="frow"><label>From (when you reached puberty)<input type="date" id="qf" value="${esc(c.from||"")}"></label><label>To (when you began praying regularly)<input type="date" id="qt" value="${esc(c.to||"")}"></label></div>
      <label class="chk"><input type="checkbox" id="qfem" ${c.female ? "checked" : ""}> I am a woman (days of menstruation and nifas are not made up)</label>
      <div class="frow ${c.female ? "" : "hide"}" id="qfemrow"><label>Usual days of period each month<input type="number" id="qh" min="3" max="10" value="${c.hayd ?? 6}"></label><label>Total days of nifas (all births)<input type="number" id="qn" min="0" value="${c.nifas ?? 0}"></label></div>
      ${days != null ? `<p class="qa-res"><b>${days.toLocaleString()} days</b> to make up: ${days.toLocaleString()} of each of the five prayers and witr — ${(days*6).toLocaleString()} prayers in all.</p>
        <button class="btn" id="qadd">Add these to my tracker</button>` : `<p class="small muted">Enter both dates. If you are unsure, take the earlier date: it is safer to make up more.</p>`}
      <p class="small muted">Puberty in the Hanafi school comes with its signs; with no signs, at fifteen lunar years.</p></section>
    <section class="card pad"><h2 style="margin-top:0">My tracker</h2>
      ${total ? `<p class="muted" style="margin-top:0">${total.toLocaleString()} prayers left${c.perDay ? `, about ${Math.ceil(total / (c.perDay*6)).toLocaleString()} days at ${c.perDay} day${c.perDay>1?"s'":"'s"} worth a day` : ""}.</p>` : `<p class="muted" style="margin-top:0">Nothing to make up yet. Add numbers from the calculator, or set them yourself.</p>`}
      <div class="qtrack">${QP.map(([k, t]) => `<div class="qrow"><span class="qn">${t}</span><button class="qbtn" data-qminus="${k}" aria-label="Made up one ${t}" ${Q.left[k] ? "" : "disabled"}>−</button>
        <input class="qv" data-qset="${k}" type="number" min="0" value="${Q.left[k]||0}" aria-label="${t} left"><button class="qbtn" data-qplus="${k}" aria-label="Add one ${t}">+</button></div>`).join("")}
        <div class="qrow"><span class="qn">Fasts</span><button class="qbtn" data-qminus="fasts" aria-label="Made up one fast" ${Q.fasts ? "" : "disabled"}>−</button><input class="qv" data-qset="fasts" type="number" min="0" value="${Q.fasts||0}" aria-label="Fasts left"><button class="qbtn" data-qplus="fasts" aria-label="Add one fast">+</button></div></div>
      <button class="btn ghost" id="qday" ${total ? "" : "disabled"}>I made up one full day (all six)</button>
      <label class="small" style="display:block;margin-top:10px">Plan: make up <select id="qper">${[1,2,3,5].map(n => `<option ${c.perDay===n?"selected":""}>${n}</option>`).join("")}</select> day(s) of prayers each day</label></section>`);
}
function bindQada(){
  const c = S.qadaCalc = S.qadaCalc || {}; const Q = S.qada = S.qada || { left:{}, fasts:0 };
  const upd = () => { c.from = $("#qf").value; c.to = $("#qt").value; c.female = $("#qfem").checked; c.hayd = +($("#qh")||{}).value || 6; c.nifas = +($("#qn")||{}).value || 0; save(); render(); };
  ["#qf","#qt","#qfem","#qh","#qn"].forEach(s => { const el = $(s); if (el) el.onchange = upd; });
  const qa = $("#qadd"); if (qa) qa.onclick = () => { const d = qadaCount(c.from, c.to, c.female, c.hayd, c.nifas); confirmBox(`Add ${d} days (${d*6} prayers) to your tracker?`, () => { QP.forEach(([k]) => Q.left[k] = (Q.left[k]||0) + d); save(); toast("Added to your tracker"); render(); }); };
  const bump = (k, n) => { if (k === "fasts") Q.fasts = Math.max(0, (Q.fasts||0) + n); else Q.left[k] = Math.max(0, (Q.left[k]||0) + n); save(); render(); };
  document.querySelectorAll("[data-qminus]").forEach(b => b.onclick = () => bump(b.dataset.qminus, -1));
  document.querySelectorAll("[data-qplus]").forEach(b => b.onclick = () => bump(b.dataset.qplus, 1));
  document.querySelectorAll("[data-qset]").forEach(i => i.onchange = () => { const k = i.dataset.qset, v = Math.max(0, parseInt(i.value)||0); if (k === "fasts") Q.fasts = v; else Q.left[k] = v; save(); render(); });
  const qd = $("#qday"); if (qd) qd.onclick = () => { QP.forEach(([k]) => Q.left[k] = Math.max(0, (Q.left[k]||0) - 1)); save(); toast("May Allah accept it"); render(); };
  const qp = $("#qper"); if (qp) qp.onchange = () => { c.perDay = +qp.value; save(); render(); };
}

/* ---------------- Zakat ---------------- */
const NISAB_G = { silver: 612.36, gold: 87.48 };   // 200 dirhams of silver, 20 mithqals of gold (common modern equivalents)
function zakatCalc(z){
  const n = k => Math.max(0, parseFloat(z[k]) || 0);
  const goldVal = n("goldG") * n("goldP"), silverVal = n("silverG") * n("silverP");
  const assets = n("cash") + n("owed") + n("goods") + goldVal + silverVal + n("other"), net = Math.max(0, assets - n("debts"));
  const nisabS = NISAB_G.silver * n("silverP"), nisabG = NISAB_G.gold * n("goldP");
  const nisab = nisabS && nisabG ? Math.min(nisabS, nisabG) : (nisabS || nisabG);   // al-Quduri: value by what benefits the poor most
  return { goldVal, silverVal, assets, net, nisab, nisabS, nisabG, due: nisab ? net >= nisab : null, zakat: net * 0.025 };
}
function zakatView(){
  const z = S.zakat || {}, r = zakatCalc(z), cur = z.cur || "£", m = v => cur + (Math.round(v*100)/100).toLocaleString(undefined, { minimumFractionDigits:2, maximumFractionDigits:2 });
  const f = (k, t, hint) => `<label>${t}${hint ? ` <span class="small muted">${hint}</span>` : ""}<input type="number" inputmode="decimal" min="0" step="any" data-z="${k}" value="${esc(z[k] ?? "")}"></label>`;
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1>Zakat calculator</h1>
    <p class="muted" style="margin:0 0 12px">Zakat is 2.5% of what you own above the nisab, once a full lunar year has passed on it. <span class="small">Mukhtasar al-Quduri, Book of Zakat.</span></p>
    <section class="card pad"><h2 style="margin-top:0">Today's prices</h2><p class="small muted" style="margin-top:0">Check today's price per gram, then enter it here. It is saved on your phone.</p>
      <div class="frow">${f("goldP", "Gold, per gram")}${f("silverP", "Silver, per gram")}<label>Currency<input data-z="cur" value="${esc(cur)}" maxlength="3"></label></div></section>
    <section class="card pad"><h2 style="margin-top:0">What you own</h2>
      <div class="frow">${f("cash", "Cash and bank balances")}${f("owed", "Money owed to you", "that you expect back")}</div>
      <div class="frow">${f("goldG", "Gold, in grams", "including jewellery")}${f("silverG", "Silver, in grams", "including jewellery")}</div>
      <div class="frow">${f("goods", "Trade goods", "stock bought to sell, at its value")}${f("other", "Other zakatable wealth", "e.g. shares bought to trade")}</div>
      <h2>What you owe</h2><div class="frow">${f("debts", "Debts due now")}</div></section>
    <section class="card pad zres" role="status" aria-live="polite">
      ${r.nisab ? `<p class="spread"><span>Total, after debts</span><b>${m(r.net)}</b></p><p class="spread"><span>Nisab (silver: 612.36 g)</span><b>${m(r.nisabS || r.nisab)}</b></p>
        ${r.due ? `<p class="zbig">Zakat due: <b>${m(r.zakat)}</b></p><p class="small muted">If a full lunar year has passed with you holding at least the nisab.</p>`
                : `<p class="zbig">No zakat due</p><p class="small muted">What you own is below the nisab.</p>`}`
        : `<p class="muted" style="margin:0">Enter the price of silver (and gold) to see the nisab and your zakat.</p>`}
      <details class="small" style="margin-top:10px"><summary>How this is worked out</summary>
        <p>The nisab is 200 dirhams of silver (about 612.36 g) or 20 mithqals of gold (about 87.48 g). In the Hanafi school gold, silver, cash and trade goods are added together by value, and valued by whichever is more beneficial to the poor, which today is silver. Jewellery of gold and silver is included. Your home, car, clothes and furniture are not counted. <i>Mukhtasar al-Quduri: chapters on zakat of silver, gold and trade goods.</i></p>
        <p>The rate is a fortieth (2.5%) of the whole. Imam Abu Hanifah held that nothing is due on an amount above the nisab until it reaches a further fifth of the nisab; this calculator uses 2.5% of the whole amount, as most people pay today.</p></details></section>`);
}
function bindZakat(){ S.zakat = S.zakat || {};
  document.querySelectorAll("[data-z]").forEach(i => i.oninput = () => { S.zakat[i.dataset.z] = i.value; save();
    const pos = i.selectionStart, k = i.dataset.z; render(); const n = document.querySelector(`[data-z="${k}"]`); if (n) { n.focus(); try { n.setSelectionRange(pos, pos); } catch(e){} } }); }

/* ---------------- Inheritance (Hanafi, al-Quduri) ---------------- */
const gcd = (a, b) => b ? gcd(b, a % b) : Math.abs(a);
const Fr = (n, d = 1) => { if (d < 0) { n = -n; d = -d; } const g = gcd(n, d) || 1; return [n/g, d/g]; };
const fadd = (a, b) => Fr(a[0]*b[1] + b[0]*a[1], a[1]*b[1]), fsub = (a, b) => fadd(a, [-b[0], b[1]]);
const fmul = (a, b) => Fr(a[0]*b[0], a[1]*b[1]), fdiv = (a, b) => Fr(a[0]*b[1], a[1]*b[0]);
const fcmp = (a, b) => a[0]*b[1] - b[0]*a[1], fstr = a => a[0] === 0 ? "0" : a[1] === 1 ? String(a[0]) : `${a[0]}/${a[1]}`;
const HEIRS = [
  ["husband","Husband",1], ["wives","Wife / wives",4], ["father","Father",1], ["mother","Mother",1],
  ["pgf","Father's father",1], ["mgm","Mother's mother",1], ["pgm","Father's mother",1],
  ["sons","Sons",20], ["daughters","Daughters",20], ["sonsons","Sons' sons",20], ["sondaughters","Sons' daughters",20],
  ["fbro","Full brothers",20], ["fsis","Full sisters",20], ["cbro","Paternal half-brothers",20], ["csis","Paternal half-sisters",20],
  ["ubro","Maternal half-brothers",20], ["usis","Maternal half-sisters",20],
  ["fnephew","Full brothers' sons",20], ["cnephew","Paternal half-brothers' sons",20],
  ["funcle","Full paternal uncles",20], ["cuncle","Father's paternal half-brothers",20], ["fcousin","Full uncles' sons",20], ["ccousin","Half-uncles' sons",20]];
function inheritCalc(h){
  const c = k => Math.max(0, h[k]|0), notes = [], fixed = {}, excl = {};
  const descM = c("sons") + c("sonsons") > 0, descF = c("daughters") + c("sondaughters") > 0, desc = descM || descF;
  const sib = c("fbro") + c("fsis") + c("cbro") + c("csis") + c("ubro") + c("usis");
  const father = c("father") > 0, gf = !father && c("pgf") > 0, maleAsc = father || gf;
  const spouse = c("husband") ? "husband" : c("wives") ? "wives" : null;
  if (c("husband")) fixed.husband = desc ? Fr(1,4) : Fr(1,2);
  if (c("wives")) fixed.wives = desc ? Fr(1,8) : Fr(1,4);
  let umariyya = false;
  if (c("mother")) { if (desc || sib >= 2) fixed.mother = Fr(1,6); else if (spouse && father) umariyya = true; else fixed.mother = Fr(1,3);
    if (c("mgm")) excl.mgm = "the mother"; if (c("pgm")) excl.pgm = "the mother"; }
  else { const gms = []; if (c("mgm")) gms.push("mgm"); if (c("pgm")) { if (father) excl.pgm = "the father"; else gms.push("pgm"); } gms.forEach(k => fixed[k] = Fr(1, 6 * gms.length)); }
  if (father && c("pgf")) excl.pgf = "the father";
  const asc = father ? "father" : gf ? "pgf" : null; if (asc && desc) fixed[asc] = Fr(1,6);
  if (c("daughters") && !c("sons")) fixed.daughters = c("daughters") === 1 ? Fr(1,2) : Fr(2,3);
  if (c("sons")) { if (c("sonsons")) excl.sonsons = "a son"; if (c("sondaughters")) excl.sondaughters = "a son"; }
  else if (c("sondaughters") && !c("sonsons")) { if (!c("daughters")) fixed.sondaughters = c("sondaughters") === 1 ? Fr(1,2) : Fr(2,3);
    else if (c("daughters") === 1) fixed.sondaughters = Fr(1,6); else excl.sondaughters = "two or more daughters"; }
  const u = c("ubro") + c("usis");
  if (u) { if (desc || maleAsc) { const by = desc ? "the deceased's children" : father ? "the father" : "the grandfather"; ["ubro","usis"].forEach(k => { if (c(k)) excl[k] = by; }); }
    else { const sh = u === 1 ? Fr(1,6) : Fr(1,3); ["ubro","usis"].forEach(k => { if (c(k)) fixed[k] = fmul(sh, Fr(c(k), u)); }); } }
  const sibBlock = descM ? "a son or son's son" : father ? "the father" : gf ? "the grandfather (as Abu Hanifah held)" : null;
  let fsisG = false, csisG = false;
  if (c("fsis")) { if (sibBlock) excl.fsis = sibBlock; else if (!c("fbro")) { if (descF) fsisG = true; else fixed.fsis = c("fsis") === 1 ? Fr(1,2) : Fr(2,3); } }
  if (c("csis")) { if (sibBlock) excl.csis = sibBlock; else if (c("fbro")) excl.csis = "a full brother"; else if (fsisG) excl.csis = "a full sister inheriting with the daughters";
    else if (!c("cbro")) { if (c("fsis") >= 2) excl.csis = "two or more full sisters"; else if (c("fsis") === 1) fixed.csis = Fr(1,6); else if (descF) csisG = true; else fixed.csis = c("csis") === 1 ? Fr(1,2) : Fr(2,3); } }
  // nearest residuaries first (al-Quduri): [male, female] groups share 2:1
  const R = [["sons","daughters"],["sonsons","sondaughters"],["father"],["pgf"],["fbro","fsis"],["fsis*"],["cbro","csis"],["csis*"],["fnephew"],["cnephew"],["funcle"],["cuncle"],["fcousin"],["ccousin"]];
  const has = g => g[0] === "fsis*" ? fsisG : g[0] === "csis*" ? csisG : g[0] === "father" ? father : g[0] === "pgf" ? gf : c(g[0]) > 0 && !excl[g[0]];
  const ri = R.findIndex(has), resid = ri >= 0 ? R[ri] : null;
  if (ri >= 0) R.slice(ri + 1).forEach(g => g.forEach(k => { if (k.endsWith("*")) return; if (c(k) && !fixed[k] && !excl[k] && !(k === "pgf" && father)) excl[k] = "a nearer residuary heir"; }));
  let sumF = Object.values(fixed).reduce(fadd, Fr(0));
  if (umariyya) { fixed.mother = fmul(fsub(Fr(1), fixed[spouse]), Fr(1,3)); sumF = fadd(sumF, fixed.mother);
    notes.push("One of the two 'Umariyyah cases: the mother takes a third of what remains after the spouse's share (al-Quduri)."); }
  const share = { ...fixed }, awl = () => { notes.push("The fixed shares add up to more than the whole, so each is reduced in proportion ('awl)."); for (const k in share) share[k] = fdiv(share[k], sumF); };
  if (resid) { const rem = fsub(Fr(1), sumF);
    if (fcmp(rem, Fr(0)) < 0) awl();
    const members = resid[0].endsWith("*") ? [resid[0].slice(0, -1)] : resid;
    if (rem[0] > 0) { const w = k => (members.length === 2 && k === members[1] ? 1 : 2) * c(k), units = members.reduce((a, k) => a + w(k), 0);
      members.forEach(k => { if (c(k)) share[k] = fadd(share[k] || Fr(0), fmul(rem, Fr(w(k), units))); }); }
    else members.forEach(k => { if (c(k) && !share[k]) excl[k] = "the fixed shares, which used up the whole estate"; }); }
  else if (Object.keys(share).length) {
    if (fcmp(sumF, Fr(1)) > 0) awl();
    else if (fcmp(sumF, Fr(1)) < 0) { const others = Object.keys(share).filter(k => k !== "husband" && k !== "wives");
      if (others.length) { const rest = fsub(Fr(1), spouse ? share[spouse] : Fr(0)), tot = others.map(k => share[k]).reduce(fadd, Fr(0));
        others.forEach(k => share[k] = fmul(fdiv(share[k], tot), rest)); notes.push("There is no residuary heir, so what is left returns to the heirs in proportion to their shares, but not to the spouse (radd, al-Quduri)."); }
      else notes.push(`What is left after the spouse's share (${fstr(fsub(Fr(1), sumF))}) goes to more distant relatives (dhawu al-arham). Ask a scholar how to divide it.`); } }
  else if (HEIRS.some(([k]) => c(k))) notes.push("No heir with a share is present. Ask a scholar.");
  const out = {}; HEIRS.forEach(([k, t]) => { if (!c(k)) return; out[k] = { t, n: c(k), share: share[k] || Fr(0), why: excl[k] || "" }; });
  return { out, notes };
}
function inheritView(){
  const h = S.inherit || {}, est = h.est || {}, r = inheritCalc(h.h || {}), cur = est.cur || "£";
  const n = k => Math.max(0, parseFloat(est[k]) || 0), gross = n("total"), afterDebts = Math.max(0, gross - n("funeral") - n("debts"));
  const will = Math.min(n("will"), afterDebts / 3), net = afterDebts - will, m = v => cur + (Math.round(v*100)/100).toLocaleString(undefined, { minimumFractionDigits:2, maximumFractionDigits:2 });
  const dead = h.dead || "m";
  const rows = HEIRS.filter(([k]) => !((dead === "m" && k === "husband") || (dead === "f" && k === "wives")));
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1>Inheritance calculator</h1>
    <p class="muted" style="margin:0 0 12px">By the Hanafi school, following <i>Mukhtasar al-Quduri, Book of Inheritance</i>. For a real estate, have a scholar confirm the result.</p>
    <section class="card pad"><h2 style="margin-top:0">The deceased</h2>
      <div class="seg mini" role="group" aria-label="The deceased was"><button data-dead="m" aria-pressed="${dead==="m"}" class="${dead==="m"?"on":""}">A man</button><button data-dead="f" aria-pressed="${dead==="f"}" class="${dead==="f"?"on":""}">A woman</button></div>
      <div class="frow" style="margin-top:12px">${[["total","Whole estate"],["funeral","Funeral costs"],["debts","Debts"],["will","Bequest (wasiyyah)"]].map(([k,t]) => `<label>${t}<input type="number" inputmode="decimal" min="0" step="any" data-est="${k}" value="${esc(est[k] ?? "")}"></label>`).join("")}</div>
      <p class="small muted">Funeral costs and debts come first, then a bequest of up to a third of what is left, then the shares below.</p></section>
    <section class="card pad"><h2 style="margin-top:0">Living relatives</h2><div class="heirs">${rows.map(([k, t, mx]) => `<label class="hrow"><span>${t}</span>
      ${mx === 1 ? `<input type="checkbox" data-heir="${k}" ${(h.h||{})[k] ? "checked" : ""}>` : `<input type="number" min="0" max="${mx}" data-heir="${k}" value="${(h.h||{})[k] || 0}">`}</label>`).join("")}</div></section>
    <section class="card pad" role="status" aria-live="polite"><h2 style="margin-top:0">Shares</h2>
      ${Object.keys(r.out).length ? `<table class="itable"><thead><tr><th>Heir</th><th>Share</th>${gross ? "<th>Amount</th>" : ""}</tr></thead><tbody>
        ${Object.entries(r.out).map(([k, o]) => { const each = o.n > 1 && o.share[0] ? fdiv(o.share, Fr(o.n)) : null;
          return `<tr class="${o.share[0] ? "" : "ex"}"><td>${esc(o.t)}${o.n > 1 ? ` ×${o.n}` : ""}${o.why && !o.share[0] ? `<br><span class="small muted">Excluded by ${esc(o.why)}</span>` : ""}</td>
            <td>${fstr(o.share)}${each ? `<br><span class="small muted">${fstr(each)} each</span>` : ""}</td>${gross ? `<td>${m(net * o.share[0] / o.share[1])}${each ? `<br><span class="small muted">${m(net * each[0] / each[1])} each</span>` : ""}</td>` : ""}</tr>`; }).join("")}</tbody></table>
        ${gross ? `<p class="small muted">Shared estate: ${m(net)} (after ${m(n("funeral") + n("debts"))} costs and debts${will ? `, and a bequest of ${m(will)}` : ""}).</p>` : ""}`
      : `<p class="muted" style="margin:0">Tick the relatives who are alive.</p>`}
      ${r.notes.map(x => `<p class="small notebox">${esc(x)}</p>`).join("")}
      <details class="small"><summary>Rules used</summary><p>Fixed shares (½, ¼, ⅛, ⅔, ⅓, ⅙), the residuaries in order — sons, then their sons, then the father, the grandfather, brothers, then uncles — exclusion (hajb), proportional reduction ('awl) and return (radd, never to the spouse). As Abu Hanifah held, the grandfather excludes brothers and sisters. In al-Mushtarakah the full brothers receive nothing. Killers, slaves and those of another religion do not inherit. <i>Mukhtasar al-Quduri, Book of Inheritance.</i></p></details></section>`);
}
function bindInherit(){ S.inherit = S.inherit || { h:{}, est:{} }; const I = S.inherit; I.h = I.h || {}; I.est = I.est || {};
  document.querySelectorAll("[data-dead]").forEach(b => b.onclick = () => { I.dead = b.dataset.dead; if (I.dead === "m") delete I.h.husband; else delete I.h.wives; save(); render(); });
  document.querySelectorAll("[data-heir]").forEach(i => i.onchange = () => { const k = i.dataset.heir; I.h[k] = i.type === "checkbox" ? (i.checked ? 1 : 0) : Math.min(+i.max, Math.max(0, parseInt(i.value)||0)); save(); render(); });
  document.querySelectorAll("[data-est]").forEach(i => i.onchange = () => { I.est[i.dataset.est] = i.value; save(); render(); });
}

/* ---------------- Salawat ---------------- */
function salawatView(){
  if (!SALAWAT) { loadSalawat().then(render); return shell(`<p class="muted">Loading…</p>`); }
  const cnt = S.salCount || {};
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1>Salawat on the Prophet ﷺ</h1>
    <p class="muted" style="margin:0 0 6px">${esc(SALAWAT.intro)}</p><p class="small muted" style="margin:0 0 14px">${esc(SALAWAT.introSrc)}</p>
    ${SALAWAT.items.map(x => `<section class="card pad sal" id="sal-${x.id}"><h2 style="margin:0 0 2px">${esc(x.name)}</h2><p class="small muted" style="margin:0 0 10px">${esc(x.by)}</p>
      <p class="ar sal-ar" lang="ar" dir="rtl">${esc(x.ar)}</p>${x.en ? `<p class="sal-en">${esc(x.en)}</p>` : ""}
      <div class="sal-src"><p><b>Source:</b> ${esc(x.src)}</p>${x.virtue ? `<p><b>Virtue:</b> ${esc(x.virtue)}</p>` : ""}${x.grade ? `<p class="small muted">${esc(x.grade)}</p>` : ""}</div>
      <div class="sal-c"><button class="btn small-btn" data-sal="${x.id}">Count one</button><span class="small muted">${(cnt[x.id]||0).toLocaleString()} recited</span></div></section>`).join("")}
    ${SALAWAT.pending ? `<p class="small muted">${esc(SALAWAT.pending)}</p>` : ""}`);
}
function bindSalawat(){ document.querySelectorAll("[data-sal]").forEach(b => b.onclick = () => { S.salCount = S.salCount || {}; S.salCount[b.dataset.sal] = (S.salCount[b.dataset.sal]||0) + 1; save();
  const s = b.nextElementSibling; if (s) s.textContent = S.salCount[b.dataset.sal].toLocaleString() + " recited"; if (navigator.vibrate) navigator.vibrate(8); }); }

function toolsRender(app){
  if (view.name === "tools") app.innerHTML = toolsView();
  else if (view.name === "guide") app.innerHTML = guideView(view.id);
  else if (view.name === "qibla") app.innerHTML = qiblaView();
  else if (view.name === "qada") app.innerHTML = qadaView();
  else if (view.name === "zakat") app.innerHTML = zakatView();
  else if (view.name === "inherit") app.innerHTML = inheritView();
  else if (view.name === "salawat") app.innerHTML = salawatView();
  else return false;
  return true;
}
function toolsBind(app){
  app.querySelectorAll("[data-guide]").forEach(b => b.onclick = () => go({ name:"guide", id:b.dataset.guide }));
  app.querySelectorAll("[data-gstep]").forEach(b => b.onclick = () => { S.guides = S.guides || {}; const d = S.guides[view.id] = S.guides[view.id] || [], i = +b.dataset.gstep;
    const k = d.indexOf(i); if (k >= 0) d.splice(k, 1); else d.push(i); save(); const y = window.scrollY; render(); window.scrollTo(0, y); });
  const gr = $("#greset"); if (gr) gr.onclick = () => confirmBox("Clear all ticks for this guide?", () => { S.guides[view.id] = []; save(); render(); });
  if (view.name === "qibla") bindQibla(); if (view.name === "qada") bindQada(); if (view.name === "zakat") bindZakat();
  if (view.name === "inherit") bindInherit(); if (view.name === "salawat") bindSalawat();
}
