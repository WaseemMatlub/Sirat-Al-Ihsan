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
  drop:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/></svg>',
  pray:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18M7 20v-4l5-3 5 3v4M12 13V9M12 9a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/></svg>',
  beads:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="4" r="2"/><circle cx="6.5" cy="7" r="2"/><circle cx="17.5" cy="7" r="2"/><circle cx="5" cy="13" r="2"/><circle cx="19" cy="13" r="2"/><circle cx="8" cy="18.5" r="2"/><circle cx="16" cy="18.5" r="2"/><path d="M12 20.5v1.5"/></svg>',
  salawat:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
};
function toolsView(){
  const row = (go, ico, t, s) => `<button class="item tool" ${go}><span class="sr-ico">${TOOL_ICON[ico]}</span><span style="min-width:0"><span class="t">${t}</span><br><span class="s">${s}</span></span><span aria-hidden="true">›</span></button>`;
  return shell(`<h1>Tools</h1><p class="muted" style="margin:0 0 14px">Guides and calculators. They all work without internet.</p>
    <p class="label">Step-by-step guides</p><div class="stack">
      ${row('data-guide="wudu"', "drop", "How to make wudu", "What is fard and what is sunnah, in order")}
      ${row('data-guide="ghusl"', "drop", "How to make ghusl", "The full bath and its three obligations")}
      ${row('data-guide="salah"', "pray", "How to pray", "Every position and what to say")}</div>
    <p class="label">Dhikr</p><div class="stack">
      ${row('data-go="tasbih"', "beads", "Tasbih counter", "Tap to count your dhikr, with a target and a gentle buzz")}</div>
    <p class="label">Prayer</p><div class="stack">
      ${row('data-go="qibla"', "qibla", "Qibla finder", "Point your phone to the Ka'bah")}
      ${row('data-go="qada"', "qada", "Qada' prayers", "Work out missed prayers and track making them up")}</div>
    <p class="label">Wealth</p><div class="stack">
      ${row('data-go="zakat"', "zakat", "Zakat calculator", "Hanafi nisab, gold, silver, cash and trade goods")}
      ${row('data-go="inherit"', "inherit", "Inheritance calculator", "Shares by the Hanafi school, from al-Quduri")}</div>
    <p class="label">Pilgrimage</p><div class="stack">
      ${row('data-guide="umrah"', "kaaba", "How to perform 'Umrah", "Step by step, with the du'a for each part")}
      ${row('data-guide="hajj"', "kaaba", "How to perform Hajj", "Tamattu', day by day, with the du'as")}</div>
`);
}

/* ---------------- Guides ---------------- */
function guideView(id){
  if (!GUIDES) { loadGuides().then(render); return shell(`<p class="muted">Loading…</p>`); }
  const g = GUIDES.find(x => x.id === id); if (!g) return shell(`<p class="muted">Not found.</p>`);
  const done = (S.guides||{})[id] || [], n = g.steps.length, d = done.length;
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1 style="margin-bottom:2px">${esc(g.title)}</h1>
    <p class="muted" style="margin:0 0 10px">${esc(g.sub)}. From ${esc(g.src)}.</p>
    <div class="topic-p" style="margin-bottom:14px"><span class="bar" style="flex:1;height:6px"><i style="width:${Math.max(2, d/n*100)}%;background:var(--brand)"></i></span><span class="small muted">${d} of ${n}</span></div>
    ${g.steps.some(x => x.rule) ? `<details class="exbox"><summary><b>What do Fard, Wajib and Sunnah mean?</b></summary><ul class="small" style="margin:8px 0 0;padding-left:18px;line-height:1.55">
      <li><b>Fard</b> (or pillar, condition): without it the act is not valid and must be done again.</li>
      <li><b>Wajib</b>: required. Leaving it out is a sin; in the prayer, missing one by mistake is made up with the prostration of forgetfulness (sajdat al-sahw).</li>
      <li><b>Sunnah</b>: the way of the Prophet ﷺ. Keep to it for its reward and its light; the act is still valid without it.</li>
      <li><b>Adab</b>: a good manner, recommended.</li></ul><p class="small muted" style="margin:6px 0 0">Nur al-Idah and Mukhtasar al-Quduri.</p></details>` : ""}
    <ol class="gsteps">${g.steps.map((s, i) => { const on = done.includes(i);
      return `<li class="gstep ${on ? "on" : ""}"><div class="gs-h"><span class="gs-n">${on ? ICON.check.replace("<svg",'<svg width="14" height="14"') : i+1}</span><h3>${esc(s.t)}</h3></div>
        ${s.rule ? `<p class="gs-rule ${/^Fard|Pillar|Condition/.test(s.rule) ? "fard" : /^Wajib/.test(s.rule) ? "wajib" : ""}">${esc(s.rule)}</p>` : ""}
        <ul>${s.do.map(x => `<li>${esc(x)}</li>`).join("")}</ul>
        ${(s.says || []).map(x => `<div class="gs-say"><p class="gs-sl">${esc(x.label)}</p><p class="ar" lang="ar" dir="rtl">${esc(x.ar).replace(/\n/g, "<br>")}</p><p class="small gs-tr"><i>${esc(x.tr)}</i></p><p class="small">${esc(x.en)}</p><p class="small muted gs-ss">${esc(x.src)}</p></div>`).join("")}
        ${s.note ? `<p class="gs-note">${esc(s.note)}</p>` : ""}
        ${s.more ? `<details class="gs-more"><summary>More detail</summary><p>${esc(s.more)}</p></details>` : ""}
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
const QIBLA_EX = [["London", 51.5074, -0.1278], ["Leeds", 53.8008, -1.5491], ["Birmingham", 52.4862, -1.8904], ["Istanbul", 41.0082, 28.9784], ["Cairo", 30.0444, 31.2357], ["Karachi", 24.8607, 67.0011], ["Kuala Lumpur", 3.139, 101.6869], ["New York", 40.7128, -74.006], ["Cape Town", -33.9249, 18.4241], ["Madinah", 24.4672, 39.6111]];
const compassWord = b => ["N","NE","E","SE","S","SW","W","NW"][Math.round(b / 45) % 8];
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
    <details class="exbox" style="margin-top:14px"><summary><b>Examples</b><span class="small muted"> · the qiblah from some cities</span></summary>
      <table class="itable" style="margin-top:8px"><thead><tr><th>City</th><th>Qiblah</th><th>Distance</th></tr></thead><tbody>
      ${QIBLA_EX.map(([n, a, b]) => `<tr><td>${n}</td><td>${Math.round(qiblaBearing(a, b))}° ${compassWord(qiblaBearing(a, b))}</td><td>${Math.round(kaabaKm(a, b)).toLocaleString()} km</td></tr>`).join("")}</tbody></table>
      <p class="small muted">Degrees are measured clockwise from true north, along the shortest path over the globe. That is why from New York the qiblah is north-east, not south-east.</p></details>
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
const QADA_EX = [
  { t:"A man who reached puberty on 1 January 2010 and began praying regularly on 1 January 2012.", r:"730 days: 730 of each of the five prayers and witr, 4,380 prayers in all.", v:{ from:"2010-01-01", to:"2012-01-01" } },
  { t:"A woman who missed prayers from 1 March 2015 to 1 March 2018, with a usual period of 6 days and 40 days of nifas.", r:"1,096 days, less about 223 days of her periods and 40 days of nifas, leaves 833 days to make up.", v:{ from:"2015-03-01", to:"2018-03-01", female:true, hayd:6, nifas:40 } },
];
function qadaView(){
  const Q = S.qada || { left:{}, fasts:0 }, c = S.qadaCalc || {}, total = QP.reduce((a,[k]) => a + (Q.left[k]||0), 0);
  const days = c.from && c.to ? qadaCount(c.from, c.to, c.female, c.hayd, c.nifas) : null;
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1>Qada' prayers</h1>
    <p class="muted" style="margin:0 0 12px">Every missed fard prayer, and witr (wajib in the Hanafi school), stays owed until it is made up. <span class="small">Nur al-Idah, making up missed prayers.</span></p>
    ${exBox(QADA_EX, "qad")}
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
  bindExamples();
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
const ZAK_EX = [
  { t:"£5,000 in the bank, 20 g of gold jewellery, £500 of bills due. Gold £95/g, silver £0.75/g.", r:"Total £6,900, less £500 debts = £6,400. That is above the silver nisab (612.36 g × £0.75 = £459.27), so zakat is 2.5%: £160.",
    v:{ cur:"£", goldP:"95", silverP:"0.75", cash:"5000", goldG:"20", debts:"500" } },
  { t:"A shopkeeper: £2,000 cash, £8,000 of stock to sell, £1,500 owed to him, £3,000 owed to a supplier.", r:"Cash + stock + money owed to him = £11,500, less £3,000 debts = £8,500. Zakat: £212.50.",
    v:{ cur:"£", goldP:"95", silverP:"0.75", cash:"2000", goods:"8000", owed:"1500", debts:"3000" } },
  { t:"£300 in savings, nothing else.", r:"£300 is below the nisab (£459.27 at these prices), so no zakat is due.",
    v:{ cur:"£", goldP:"95", silverP:"0.75", cash:"300" } },
];
function zakatView(){
  const z = S.zakat || {}, r = zakatCalc(z), cur = z.cur || "£", m = v => cur + (Math.round(v*100)/100).toLocaleString(undefined, { minimumFractionDigits:2, maximumFractionDigits:2 });
  const f = (k, t, hint) => `<label>${t}${hint ? ` <span class="small muted">${hint}</span>` : ""}<input type="number" inputmode="decimal" min="0" step="any" data-z="${k}" value="${esc(z[k] ?? "")}"></label>`;
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1>Zakat calculator</h1>
    <p class="muted" style="margin:0 0 12px">Zakat is 2.5% of what you own above the nisab, once a full lunar year has passed on it. <span class="small">Mukhtasar al-Quduri, Book of Zakat.</span></p>
    ${exBox(ZAK_EX, "zak")}<p class="small muted" style="margin:0 0 12px">The examples use sample prices. Enter today's prices for your own zakat.</p>
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
    const pos = i.selectionStart, k = i.dataset.z; render(); const n = document.querySelector(`[data-z="${k}"]`); if (n) { n.focus(); try { n.setSelectionRange(pos, pos); } catch(e){} } });
  bindExamples(); }

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
  const c = k => Math.max(0, h[k]|0), notes = [], fixed = {}, excl = {}, why = {};
  const descM = c("sons") + c("sonsons") > 0, descF = c("daughters") + c("sondaughters") > 0, desc = descM || descF;
  const sib = c("fbro") + c("fsis") + c("cbro") + c("csis") + c("ubro") + c("usis");
  const father = c("father") > 0, gf = !father && c("pgf") > 0, maleAsc = father || gf;
  const spouse = c("husband") ? "husband" : c("wives") ? "wives" : null;
  if (c("husband")) { fixed.husband = desc ? Fr(1,4) : Fr(1,2); why.husband = desc ? "A quarter, because the deceased left children" : "A half, because the deceased left no children"; }
  if (c("wives")) { fixed.wives = desc ? Fr(1,8) : Fr(1,4); why.wives = (desc ? "An eighth, because the deceased left children" : "A quarter, because the deceased left no children") + (c("wives") > 1 ? ", shared equally between the wives" : ""); }
  let umariyya = false;
  if (c("mother")) { if (desc || sib >= 2) { fixed.mother = Fr(1,6); why.mother = desc ? "A sixth, because the deceased left children" : "A sixth, because the deceased left two or more brothers or sisters"; } else if (spouse && father) { umariyya = true; why.mother = "A third of what is left after the spouse (the 'Umariyyah case)"; } else { fixed.mother = Fr(1,3); why.mother = "A third, because there are no children and fewer than two siblings"; }
    if (c("mgm")) excl.mgm = "the mother"; if (c("pgm")) excl.pgm = "the mother"; }
  else { const gms = []; if (c("mgm")) gms.push("mgm"); if (c("pgm")) { if (father) excl.pgm = "the father"; else gms.push("pgm"); } gms.forEach(k => { fixed[k] = Fr(1, 6 * gms.length); why[k] = gms.length > 1 ? "The grandmothers share a sixth" : "A sixth, as there is no mother"; }); }
  if (father && c("pgf")) excl.pgf = "the father";
  const asc = father ? "father" : gf ? "pgf" : null; if (asc && desc) { fixed[asc] = Fr(1,6); why[asc] = "A sixth, because the deceased left children" + (descM ? "" : ", plus anything left over"); }
  if (c("daughters") && !c("sons")) { fixed.daughters = c("daughters") === 1 ? Fr(1,2) : Fr(2,3); why.daughters = c("daughters") === 1 ? "A half, for one daughter with no son" : "Two thirds, shared by two or more daughters with no son"; }
  if (c("sons")) { if (c("sonsons")) excl.sonsons = "a son"; if (c("sondaughters")) excl.sondaughters = "a son"; }
  else if (c("sondaughters") && !c("sonsons")) { if (!c("daughters")) { fixed.sondaughters = c("sondaughters") === 1 ? Fr(1,2) : Fr(2,3); why.sondaughters = "Like daughters, as there are no children"; }
    else if (c("daughters") === 1) { fixed.sondaughters = Fr(1,6); why.sondaughters = "A sixth, completing two thirds with the daughter"; } else excl.sondaughters = "two or more daughters"; }
  const u = c("ubro") + c("usis");
  if (u) { if (desc || maleAsc) { const by = desc ? "the deceased's children" : father ? "the father" : "the grandfather"; ["ubro","usis"].forEach(k => { if (c(k)) excl[k] = by; }); }
    else { const sh = u === 1 ? Fr(1,6) : Fr(1,3); ["ubro","usis"].forEach(k => { if (c(k)) { fixed[k] = fmul(sh, Fr(c(k), u)); why[k] = u === 1 ? "A sixth, as there are no children, father or grandfather" : "A third shared equally, male and female, as there are no children, father or grandfather"; } }); } }
  const sibBlock = descM ? "a son or son's son" : father ? "the father" : gf ? "the grandfather (as Abu Hanifah held)" : null;
  let fsisG = false, csisG = false;
  if (c("fsis")) { if (sibBlock) excl.fsis = sibBlock; else if (!c("fbro")) { if (descF) fsisG = true; else { fixed.fsis = c("fsis") === 1 ? Fr(1,2) : Fr(2,3); why.fsis = c("fsis") === 1 ? "A half, as there are no children, father or brothers" : "Two thirds shared, as there are no children, father or brothers"; } } }
  if (c("csis")) { if (sibBlock) excl.csis = sibBlock; else if (c("fbro")) excl.csis = "a full brother"; else if (fsisG) excl.csis = "a full sister inheriting with the daughters";
    else if (!c("cbro")) { if (c("fsis") >= 2) excl.csis = "two or more full sisters"; else if (c("fsis") === 1) { fixed.csis = Fr(1,6); why.csis = "A sixth, completing two thirds with the full sister"; } else if (descF) csisG = true; else { fixed.csis = c("csis") === 1 ? Fr(1,2) : Fr(2,3); why.csis = "Like full sisters, as there are none"; } } }
  // nearest residuaries first (al-Quduri): [male, female] groups share 2:1
  const R = [["sons","daughters"],["sonsons","sondaughters"],["father"],["pgf"],["fbro","fsis"],["fsis*"],["cbro","csis"],["csis*"],["fnephew"],["cnephew"],["funcle"],["cuncle"],["fcousin"],["ccousin"]];
  const has = g => g[0] === "fsis*" ? fsisG : g[0] === "csis*" ? csisG : g[0] === "father" ? father : g[0] === "pgf" ? gf : c(g[0]) > 0 && !excl[g[0]];
  const ri = R.findIndex(has), resid = ri >= 0 ? R[ri] : null;
  if (ri >= 0) R.slice(ri + 1).forEach(g => g.forEach(k => { if (k.endsWith("*")) return; if (c(k) && !fixed[k] && !excl[k] && !(k === "pgf" && father)) excl[k] = sibBlock && ["fbro","cbro","fnephew","cnephew","funcle","cuncle","fcousin","ccousin"].includes(k) ? sibBlock : "a nearer residuary heir"; }));
  let sumF = Object.values(fixed).reduce(fadd, Fr(0));
  if (umariyya) { fixed.mother = fmul(fsub(Fr(1), fixed[spouse]), Fr(1,3)); sumF = fadd(sumF, fixed.mother);
    notes.push("One of the two 'Umariyyah cases: the mother takes a third of what remains after the spouse's share (al-Quduri)."); }
  const share = { ...fixed }, awl = () => { notes.push("The fixed shares add up to more than the whole, so each is reduced in proportion ('awl)."); for (const k in share) share[k] = fdiv(share[k], sumF); };
  if (resid) { const rem = fsub(Fr(1), sumF);
    if (fcmp(rem, Fr(0)) < 0) awl();
    const members = resid[0].endsWith("*") ? [resid[0].slice(0, -1)] : resid;
    if (rem[0] > 0) { const w = k => (members.length === 2 && k === members[1] ? 1 : 2) * c(k), units = members.reduce((a, k) => a + w(k), 0);
      members.forEach(k => { if (c(k)) { share[k] = fadd(share[k] || Fr(0), fmul(rem, Fr(w(k), units))); why[k] = why[k] ? why[k] : members.length === 2 ? "What is left, a male taking twice a female's share" : (fsisG && k === "fsis") || (csisG && k === "csis") ? "What is left: sisters inherit the remainder alongside daughters" : "What is left, as the nearest male relative"; } }); }
    else members.forEach(k => { if (c(k) && !share[k]) excl[k] = "the fixed shares, which used up the whole estate"; }); }
  else if (Object.keys(share).length) {
    if (fcmp(sumF, Fr(1)) > 0) awl();
    else if (fcmp(sumF, Fr(1)) < 0) { const others = Object.keys(share).filter(k => k !== "husband" && k !== "wives");
      if (others.length) { const rest = fsub(Fr(1), spouse ? share[spouse] : Fr(0)), tot = others.map(k => share[k]).reduce(fadd, Fr(0));
        others.forEach(k => share[k] = fmul(fdiv(share[k], tot), rest)); notes.push("There is no residuary heir, so what is left returns to the heirs in proportion to their shares, but not to the spouse (radd, al-Quduri)."); }
      else notes.push(`What is left after the spouse's share (${fstr(fsub(Fr(1), sumF))}) goes to more distant relatives (dhawu al-arham). Ask a scholar how to divide it.`); } }
  else if (HEIRS.some(([k]) => c(k))) notes.push("No heir with a share is present. Ask a scholar.");
  const out = {}; HEIRS.forEach(([k, t]) => { if (!c(k)) return; out[k] = { t, n: c(k), share: share[k] || Fr(0), why: excl[k] || "", reason: why[k] || "" }; });
  return { out, notes };
}
const INH_EX = [
  { t:"A man leaves his wife, his mother, one son and two daughters. Estate £120,000; funeral £2,000; debts £3,000.", r:"Wife ⅛ and mother ⅙ come first; the son and daughters share what is left, a son taking twice a daughter's share.",
    v:{ dead:"m", h:{ wives:1, mother:1, sons:1, daughters:2 }, est:{ total:"120000", funeral:"2000", debts:"3000" } } },
  { t:"A woman leaves her husband, her mother and her father. Estate £60,000.", r:"One of the two 'Umariyyah cases: husband ½, then the mother takes a third of what is left (⅙) and the father the rest (⅓).",
    v:{ dead:"f", h:{ husband:1, mother:1, father:1 }, est:{ total:"60000" } } },
  { t:"A woman leaves her husband and two full sisters. Estate £70,000.", r:"The shares add up to more than the whole (½ + ⅔), so they are reduced in proportion ('awl): husband 3/7, sisters 4/7.",
    v:{ dead:"f", h:{ husband:1, fsis:2 }, est:{ total:"70000" } } },
  { t:"A man leaves his father's father and a full brother.", r:"As Imam Abu Hanifah held, the grandfather takes the place of the father and excludes the brother.",
    v:{ dead:"m", h:{ pgf:1, fbro:1 }, est:{} } },
];
// Worked examples a user can load with one tap
function exBox(list, key){
  return `<details class="exbox"><summary><b>Try an example</b><span class="small muted"> · see how it works before entering your own</span></summary>
    <div class="stack" style="margin-top:10px">${list.map((x, i) => `<button class="item exbtn" data-ex="${key}|${i}"><span style="flex:1;min-width:0"><span class="t" style="font-weight:600">${esc(x.t)}</span><br><span class="s">${esc(x.r)}</span></span><span class="pill">Load</span></button>`).join("")}</div>
    <button class="linkbtn" data-exclear="${key}" style="margin-top:10px">Clear everything and start again</button></details>`;
}
function bindExamples(){
  const st = { inh:["inherit", INH_EX], zak:["zakat", ZAK_EX], qad:["qadaCalc", QADA_EX] };
  document.querySelectorAll("[data-ex]").forEach(b => b.onclick = () => { const [k, i] = b.dataset.ex.split("|"), [key, list] = st[k];
    S[key] = JSON.parse(JSON.stringify(list[+i].v)); save(); render(); toast("Example loaded. Scroll down to see the result."); });
  document.querySelectorAll("[data-exclear]").forEach(b => b.onclick = () => { const [key] = st[b.dataset.exclear]; confirmBox("Clear everything you have entered here?", () => { S[key] = key === "inherit" ? { h:{}, est:{} } : {}; save(); render(); }); });
}
function inheritView(){
  const h = S.inherit || {}, est = h.est || {}, r = inheritCalc(h.h || {}), cur = est.cur || "£";
  const n = k => Math.max(0, parseFloat(est[k]) || 0), gross = n("total"), afterDebts = Math.max(0, gross - n("funeral") - n("debts"));
  const will = Math.min(n("will"), afterDebts / 3), net = afterDebts - will, m = v => cur + (Math.round(v*100)/100).toLocaleString(undefined, { minimumFractionDigits:2, maximumFractionDigits:2 });
  const dead = h.dead || "m";
  const rows = HEIRS.filter(([k]) => !((dead === "m" && k === "husband") || (dead === "f" && k === "wives")));
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1>Inheritance calculator</h1>
    <p class="muted" style="margin:0 0 12px">By the Hanafi school, following <i>Mukhtasar al-Quduri, Book of Inheritance</i>. For a real estate, have a scholar confirm the result.</p>
    ${exBox(INH_EX, "inh")}
    <section class="card pad"><h2 style="margin-top:0">The deceased</h2>
      <div class="seg mini" role="group" aria-label="The deceased was"><button data-dead="m" aria-pressed="${dead==="m"}" class="${dead==="m"?"on":""}">A man</button><button data-dead="f" aria-pressed="${dead==="f"}" class="${dead==="f"?"on":""}">A woman</button></div>
      <div class="frow" style="margin-top:12px">${[["total","Whole estate"],["funeral","Funeral costs"],["debts","Debts"],["will","Bequest (wasiyyah)"]].map(([k,t]) => `<label>${t}<input type="number" inputmode="decimal" min="0" step="any" data-est="${k}" value="${esc(est[k] ?? "")}"></label>`).join("")}</div>
      <p class="small muted">Funeral costs and debts come first, then a bequest of up to a third of what is left, then the shares below.</p></section>
    <section class="card pad"><h2 style="margin-top:0">Living relatives</h2><div class="heirs">${rows.map(([k, t, mx]) => `<label class="hrow"><span>${t}</span>
      ${mx === 1 ? `<input type="checkbox" data-heir="${k}" ${(h.h||{})[k] ? "checked" : ""}>` : `<span class="stp"><button type="button" data-hstep="${k}|-1" aria-label="One fewer: ${t}" ${(h.h||{})[k] ? "" : "disabled"}>−</button><span class="stp-n" aria-live="polite">${(h.h||{})[k] || 0}</span><button type="button" data-hstep="${k}|1" aria-label="One more: ${t}" ${((h.h||{})[k]||0) >= mx ? "disabled" : ""}>+</button></span>`}</label>`).join("")}</div></section>
    <section class="card pad" role="status" aria-live="polite"><h2 style="margin-top:0">Shares</h2>
      ${Object.keys(r.out).length ? `<table class="itable"><thead><tr><th>Heir</th><th>Share</th>${gross ? "<th>Amount</th>" : ""}</tr></thead><tbody>
        ${Object.entries(r.out).map(([k, o]) => { const each = o.n > 1 && o.share[0] ? fdiv(o.share, Fr(o.n)) : null;
          return `<tr class="${o.share[0] ? "" : "ex"}"><td>${esc(o.t)}${o.n > 1 ? ` ×${o.n}` : ""}${o.why && !o.share[0] ? `<br><span class="small muted">Excluded by ${esc(o.why)}</span>` : o.reason ? `<br><span class="small muted">${esc(o.reason)}</span>` : ""}</td>
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
  document.querySelectorAll("[data-hstep]").forEach(b => b.onclick = () => { const [k, d] = b.dataset.hstep.split("|"), mx = (HEIRS.find(x => x[0] === k) || [0,0,20])[2];
    I.h[k] = Math.min(mx, Math.max(0, (I.h[k]||0) + +d)); save(); const y = window.scrollY; render(); window.scrollTo(0, y); });
  bindExamples();
}

/* ---------------- Salawat ---------------- */
// First-page card: one salawat to recite (changes daily), with a counter
function salawatCard(){
  if (!SALAWAT) { loadSalawat().then(() => { if (view.name === "home" && SALAWAT) render(); }); return ""; }
  const short = SALAWAT.items.filter(x => x.id !== "taj"), x = short[today() % short.length], n = (S.salCount||{})[x.id] || 0;
  return `<section class="card salcard" aria-labelledby="salh"><p class="sal-k" id="salh">Today's salawat · ${esc(x.name)}</p>
    <p class="ar sal-ar" lang="ar" dir="rtl">${esc(x.ar)}</p>
    <button class="salbtn" data-sal="${x.id}"><span class="sb-plus" aria-hidden="true">+1</span><span class="sb-t">Tap each time you recite it</span><span class="sb-n" data-salc="${x.id}">${n.toLocaleString()}</span></button></section>
    <div class="glist">${grow("salawat", "", "ص", "All salawat", "Seven salawat with their sources and virtues")}${grow("dalail", "", "د", "Dala'il al-Khayrat", "Imam al-Jazuli's book of salawat, one part a day")}</div>`;
}
const GICO = {
  daily: `<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>`,
  rabbana: `<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M2 4h6a4 4 0 0 1 4 4v12a3 3 0 0 0-3-3H2zM22 4h-6a4 4 0 0 0-4 4v12a3 3 0 0 1 3-3h7z"/></svg>`,
  ghazali: `<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.2 3.8a5.5 5.5 0 0 0-7.8 0L5 11.2V19h7.8l7.4-7.4a5.5 5.5 0 0 0 0-7.8zM16 8 2 22M17.5 15H9"/></svg>`,
};
const CHEV = `<svg class="g-ch" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>`;
// One tappable row in a grouped list: icon, title, one line saying what is inside, chevron
function grow(goName, dua, icoAr, t, sub, svg){
  return `<button class="grow" ${dua ? `data-dua="${dua}"` : `data-go="${goName}"`}><span class="g-ico ${svg ? "" : "ar"}" aria-hidden="true">${svg || icoAr}</span>
    <span class="g-m"><span class="g-t">${esc(t)}</span><span class="g-s">${esc(sub)}</span></span>${CHEV}</button>`;
}
function duaRows(){
  return `<div class="glist">${grow("", "daily", "", "Daily du'as", "Waking, sleeping, eating, the toilet, leaving home", GICO.daily)}
    ${grow("", "rabbana", "", "The 40 Rabbana", "Du'as from the Qur'an that begin 'Our Lord'", GICO.rabbana)}
    ${grow("", "ghazali", "", "Imam al-Ghazali's du'as", "A day of worship from his Beginning of Guidance, with wudu step by step", GICO.ghazali)}</div>`;
}
function salawatView(){
  if (!SALAWAT) { loadSalawat().then(render); return shell(`<p class="muted">Loading…</p>`); }
  const cnt = S.salCount || {};
  return shell(`<button class="back" data-go="home">${ICON.back} Home</button><h1>Salawat on the Prophet ﷺ</h1>
    <p class="muted" style="margin:0 0 6px">${esc(SALAWAT.intro)}</p><p class="small muted" style="margin:0 0 14px">${esc(SALAWAT.introSrc)}</p>
    <button class="item dl-entry" data-go="dalail"><span class="dl-ico ar" aria-hidden="true">د</span><span style="flex:1;min-width:0"><span class="t">Dala'il al-Khayrat</span><br><span class="s">Imam al-Jazuli's salawat, one hizb a day</span></span><span aria-hidden="true">›</span></button>
    ${SALAWAT.items.map(x => `<section class="card pad sal" id="sal-${x.id}"><h2 style="margin:0 0 2px">${esc(x.name)}</h2><p class="small muted" style="margin:0 0 10px">${esc(x.by)}</p>
      <p class="ar sal-ar" lang="ar" dir="rtl">${esc(x.ar)}</p>${x.en ? `<p class="sal-en">${esc(x.en)}</p>` : ""}
      <div class="sal-src"><p><b>Source:</b> ${esc(x.src)}</p>${x.virtue ? `<p><b>Virtue:</b> ${esc(x.virtue)}</p>` : ""}${x.grade ? `<p class="small muted">${esc(x.grade)}</p>` : ""}</div>
      <div class="sal-c"><button class="btn small-btn" data-sal="${x.id}">Count one</button><span class="small muted">${(cnt[x.id]||0).toLocaleString()} recited</span></div></section>`).join("")}
    ${SALAWAT.pending ? `<p class="small muted">${esc(SALAWAT.pending.replace(/ and Dala'il al-Khayrat of Imam al-Jazuli رحمه الله/, ""))}</p>` : ""}`);
}
function bindSalawat(){ document.querySelectorAll("[data-sal]").forEach(b => b.onclick = () => { S.salCount = S.salCount || {}; S.salCount[b.dataset.sal] = (S.salCount[b.dataset.sal]||0) + 1; save();
  const s = b.nextElementSibling; if (s) s.textContent = S.salCount[b.dataset.sal].toLocaleString() + " recited"; if (navigator.vibrate) navigator.vibrate(8); }); }
function bindSalCard(){ document.querySelectorAll(".salcard [data-sal]").forEach(b => b.onclick = () => { S.salCount = S.salCount || {}; const k = b.dataset.sal; S.salCount[k] = (S.salCount[k]||0) + 1; save();
  const c = document.querySelector(`[data-salc="${k}"]`); if (c) c.textContent = S.salCount[k].toLocaleString(); if (navigator.vibrate) navigator.vibrate(8); }); }

let DUAS = null;
const loadDuas = async () => DUAS || (DUAS = await fetch("data/duas.json").then(r => r.json()).catch(() => null));
function duaBody(x){
  if (x.parts) return `<ol class="dsteps">${x.parts.map(p => `<li><p class="ds-h">${esc(p.step)}</p><p class="ds-do">${esc(p.do)}</p>
      <p class="ar dua-ar" lang="ar" dir="rtl">${esc(p.ar)}</p><p class="dua-en">${esc(p.en)}</p></li>`).join("")}</ol>`;
  return `<p class="ar dua-ar" lang="ar" dir="rtl">${esc(x.ar)}</p><p class="dua-en">${esc(x.en)}</p>`;
}
function duasView(sec){
  if (!DUAS) { loadDuas().then(render); return shell(`<p class="muted">Loading…</p>`); }
  const cur = DUAS.sections.find(x => x.id === sec) || DUAS.sections[0];
  return shell(`<button class="back" data-go="home">${ICON.back} Home</button><h1 style="margin-bottom:10px">Du'as</h1>
    <div class="dseg" role="tablist" aria-label="Du'a collections">${DUAS.sections.map(x => `<button role="tab" aria-selected="${x.id === cur.id}" class="${x.id === cur.id ? "on" : ""}" data-dua="${x.id}">${esc(x.title)}</button>`).join("")}</div>
    <section class="about-box"><p class="ab-h">About this collection</p><p>${esc(cur.about || cur.sub)}</p><p class="small muted" style="margin:6px 0 0">Tap a du'a to open it. ${cur.items.length} in this collection.</p></section>
    <div class="dlist">${cur.items.map((x, i) => { const t = x.t.replace(/^\d+\.\s*/, "") || "Rabbana";
      return `<details class="dua"><summary><span class="dua-n">${i+1}</span><span class="g-m"><span class="g-t">${esc(t)}</span>${x.when || x.parts ? `<span class="g-s">${esc(x.when || x.parts.length + " short steps, in order")}</span>` : ""}</span>${CHEV}</summary>
        <div class="dua-b">${duaBody(x)}${x.note ? `<p class="small notebox">${esc(x.note)}</p>` : ""}<p class="small muted dua-src">Source: ${esc(x.src)}</p></div></details>`; }).join("")}</div>
    ${cur.credit ? `<p class="small muted" style="margin-top:14px">${esc(cur.credit)}</p>` : ""}`);
}
let DALAIL = null;
const loadDalail = async () => DALAIL || (DALAIL = await fetch("data/dalail.json").then(r => r.json()).catch(() => null));
const dalailToday = () => [7, 1, 2, 3, 4, 5, 6][new Date().getDay()];   // Sunday = 7th hizb, Monday = 1st
const DL_TILES = [["opening","Opening Du'a",""],["asma","Names of Allah","ﷻ"],["nabi","Names of the Prophet","ﷺ"],["niyyah","Du'a of Intention",""]];
// Short phrases flow on one line with a stop mark between them; a new paragraph starts at each "Allahumma"
function dlFlow(paras){
  const out = []; let cur = [];
  const flush = () => { if (cur.length) out.push(`<p>${cur.map(x => `${esc(x)} <span class="dl-stop" aria-hidden="true"></span>`).join(" ")}</p>`); cur = []; };
  paras.forEach(p => { if (/^فَصْلٌ/.test(p)) { flush(); out.push(`<p class="dl-h">${esc(p)}</p>`); return; }
    if (/^(اللَّهُمَّ|الْحَمْدُ|بِسْمِ)/.test(p) && cur.length) flush(); cur.push(p); });
  flush(); return out.join("");
}
function dalailMenu(){
  const t = dalailToday(), readToday = (S.dalail || {})[new Date().toDateString()], ex = DALAIL.extra || {};
  const tile = (attr, label, sub, cls, ok) => `<button class="dl-tile ${cls || ""}" ${attr} ${ok ? "" : 'aria-disabled="true"'}><span class="dl-tl">${label}</span>${sub ? `<span class="dl-ts">${sub}</span>` : ""}</button>`;
  const pre = DL_TILES.map(([k, l, h]) => tile(`data-dlx="${k}"`, `${esc(l)}${h ? ` <span class="ar">${h}</span>` : ""}`, ex[k] ? "" : "Coming soon", (k === "opening" || k === "niyyah" ? "wide" : "") + (ex[k] ? "" : " off"), !!ex[k]));
  const parts = DALAIL.ahzab.map(h => tile(`data-hizb="${h.n}"`, `Part ${h.n}`, `${esc(h.day.replace(" (second)", ", second"))}${h.n === t ? " · today" : ""}${readToday === h.n ? " · read ✓" : ""}${h.paras ? "" : " · coming soon"}`,
    (h.n === t ? "today" : "") + (h.paras ? "" : " off"), !!h.paras));
  return shell(`<button class="back" data-go="salawat">${ICON.back} Salawat</button>
    <h1 style="margin-bottom:2px">Dala'il al-Khayrat</h1><p class="ar" lang="ar" style="font-size:1.3rem;margin:0">دَلَائِلُ الْخَيْرَاتِ</p>
    <p class="muted" style="margin:6px 0 14px">${esc(DALAIL.by)}. Read one part a day, starting on Monday, and finish the whole book each week. Today is Part ${t}.</p>
    <div class="dl-grid">${pre.join("")}${parts.join("")}${tile(`data-dlx="khatm"`, "Du'a of Completion", ex.khatm ? "" : "Coming soon", "wide" + (ex.khatm ? "" : " off"), !!ex.khatm)}</div>
    <p class="small muted" style="margin-top:14px">${esc(DALAIL.note)}</p>`);
}
function dalailView(n, x){
  if (!DALAIL) { loadDalail().then(render); return shell(`<p class="muted">Loading…</p>`); }
  if (x) { const e = (DALAIL.extra || {})[x]; const title = x === "khatm" ? "Du'a of Completion" : (DL_TILES.find(d => d[0] === x) || [0, ""])[1];
    return shell(`<button class="back" data-dlmenu>${ICON.back} Dala'il al-Khayrat</button><h1>${esc(title)}</h1>
      ${e ? `<section class="card pad dl-card"><div class="dl-text" lang="ar" dir="rtl">${e.paras.map(p => `<p>${esc(p)} <span class="dl-stop" aria-hidden="true"></span></p>`).join("")}</div></section>` : `<p class="muted">This section is being typed in from the printed edition.</p>`}`); }
  if (!n) return dalailMenu();
  const t = dalailToday(), cur = DALAIL.ahzab.find(h => h.n === n) || DALAIL.ahzab[0], read = (S.dalail || {})[new Date().toDateString()] === cur.n;
  const prev = DALAIL.ahzab.find(h => h.n === cur.n - 1), next = DALAIL.ahzab.find(h => h.n === cur.n + 1);
  return shell(`<button class="back" data-dlmenu>${ICON.back} Dala'il al-Khayrat</button>
    <div class="spread" style="align-items:baseline"><h1 style="margin-bottom:2px">Part ${cur.n}</h1><span class="ar muted" lang="ar" style="font-size:1.1rem">${esc(cur.ar)}</span></div>
    <p class="muted" style="margin:0 0 12px">${esc(cur.day)}${cur.n === t ? " · today's part" : ""}. Book pages ${esc(cur.pages)}.</p>
    <section class="card pad dl-card">
      ${cur.paras ? `<div class="dl-text" lang="ar" dir="rtl">${dlFlow(cur.paras)}</div>
        <button class="btn ${read ? "ghost" : ""}" id="dlread" style="margin-top:12px" ${read ? "disabled" : ""}>${read ? "Read today, alhamdulillah" : "I've read this part today"}</button>`
      : `<p class="muted">This part is being typed in, letter by letter, from the printed edition.</p>`}</section>
    <div class="btnrow">${prev ? `<button class="btn ghost" data-hizb="${prev.n}">‹ Part ${prev.n}</button>` : "<span></span>"}${next ? `<button class="btn ghost" data-hizb="${next.n}">Part ${next.n} ›</button>` : `<button class="btn ghost" data-dlx="khatm">Du'a of Completion ›</button>`}</div>`);
}
/* ---------------- Tasbih ---------------- */
const DHIKR = [
  ["subhan", "سُبْحَانَ اللَّهِ", "Subhan Allah", "Glory be to Allah"],
  ["hamd", "الْحَمْدُ لِلَّهِ", "Al-hamdu lillah", "All praise is for Allah"],
  ["akbar", "اللَّهُ أَكْبَرُ", "Allahu akbar", "Allah is the Greatest"],
  ["tahlil", "لَا إِلَهَ إِلَّا اللَّهُ", "La ilaha illa Allah", "There is no god but Allah"],
  ["istighfar", "أَسْتَغْفِرُ اللَّهَ", "Astaghfirullah", "I ask Allah's forgiveness"],
  ["salawat", "اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدٍ", "Allahumma salli 'ala sayyidina Muhammad", "O Allah, send blessings on our master Muhammad ﷺ"],
  ["hawqala", "لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ", "La hawla wa la quwwata illa billah", "There is no power and no strength except by Allah"],
  ["free", "", "Any dhikr", "Count anything you like"],
];
function tasbihView(){
  const T = S.tasbih = S.tasbih || { d:"subhan", n:0, target:33, tot:{} }, d = DHIKR.find(x => x[0] === T.d) || DHIKR[0];
  const inRound = T.target ? (T.n % T.target || (T.n ? T.target : 0)) : 0, pct = T.target ? inRound / T.target * 100 : 0, rounds = T.target ? Math.floor((T.n - 1) / T.target) : 0;
  return shell(`<button class="back" data-go="tools">${ICON.back} Tools</button><h1 style="margin-bottom:8px">Tasbih counter</h1>
    <div class="tb-chips" role="group" aria-label="Choose a dhikr">${DHIKR.map(x => `<button class="dchip ${x[0] === T.d ? "on" : ""}" data-tbd="${x[0]}" aria-pressed="${x[0] === T.d}">${esc(x[2])}</button>`).join("")}</div>
    <button class="tb-pad" id="tbtap" aria-label="Count one. ${T.n} so far">
      ${d[1] ? `<span class="ar tb-ar" lang="ar">${esc(d[1])}</span>` : ""}<span class="tb-en">${esc(d[3])}</span>
      <span class="tb-n" aria-live="polite">${T.n}</span>
      ${T.target ? `<span class="tb-ring" style="--p:${pct}%"></span><span class="tb-of">${inRound} of ${T.target}${rounds > 0 ? ` · ${rounds} round${rounds > 1 ? "s" : ""} done` : ""}</span>` : `<span class="tb-of">no target</span>`}
      <span class="tb-hint">Tap anywhere here</span></button>
    <div class="tb-row"><label class="small">Target <select id="tbt">${[33, 34, 99, 100, 1000, 0].map(n => `<option value="${n}" ${T.target === n ? "selected" : ""}>${n || "None"}</option>`).join("")}</select></label>
      <button class="btn ghost small-btn" id="tbundo" ${T.n ? "" : "disabled"}>Undo</button><button class="btn ghost small-btn" id="tbreset" ${T.n ? "" : "disabled"}>Reset</button></div>
    <p class="small muted">All time: ${DHIKR.filter(x => (T.tot||{})[x[0]]).map(x => `${esc(x[2])} ${T.tot[x[0]].toLocaleString()}`).join(" · ") || "nothing yet"}.</p>
    <details class="exbox"><summary><b>After each prayer</b></summary><p class="small" style="margin:8px 0 0">Subhan Allah 33, al-hamdu lillah 33, Allahu akbar 33 (or 34), then the tahlil once: "Whoever does this after every prayer, his sins are forgiven even if they are like the foam of the sea." Sahih Muslim (597), from Abu Hurayrah رضي الله عنه.</p></details>`);
}
function bindTasbih(){
  const T = S.tasbih; const tap = $("#tbtap"); const on = document.querySelector(".tb-chips .on"); if (on) on.parentNode.scrollLeft = on.offsetLeft - 16;
  if (tap) tap.onclick = () => { T.n++; T.tot = T.tot || {}; T.tot[T.d] = (T.tot[T.d] || 0) + 1; save();
    const hit = T.target && T.n % T.target === 0; if (navigator.vibrate) navigator.vibrate(hit ? [60, 60, 60] : 8);
    if (hit) toast(`${T.target} done. Alhamdulillah`); render(); };
  document.querySelectorAll("[data-tbd]").forEach(b => b.onclick = () => { T.d = b.dataset.tbd; T.n = 0; save(); render(); });
  const t = $("#tbt"); if (t) t.onchange = () => { T.target = +t.value; save(); render(); };
  const u = $("#tbundo"); if (u) u.onclick = () => { if (T.n) { T.n--; T.tot[T.d] = Math.max(0, (T.tot[T.d]||1) - 1); save(); render(); } };
  const r = $("#tbreset"); if (r) r.onclick = () => { T.n = 0; save(); render(); };
}
function toolsRender(app){
  if (view.name === "dalail") { app.innerHTML = dalailView(view.n, view.x); return true; }
  if (view.name === "duas") { app.innerHTML = duasView(view.sec); return true; }
  if (view.name === "tools") app.innerHTML = toolsView();
  else if (view.name === "guide") app.innerHTML = guideView(view.id);
  else if (view.name === "qibla") app.innerHTML = qiblaView();
  else if (view.name === "qada") app.innerHTML = qadaView();
  else if (view.name === "zakat") app.innerHTML = zakatView();
  else if (view.name === "inherit") app.innerHTML = inheritView();
  else if (view.name === "salawat") app.innerHTML = salawatView();
  else if (view.name === "tasbih") app.innerHTML = tasbihView();
  else return false;
  return true;
}
function toolsBind(app){
  app.querySelectorAll("[data-dua]").forEach(b => b.onclick = () => { go({ name:"duas", sec:b.dataset.dua }); });
  app.querySelectorAll("[data-hizb]").forEach(b => b.onclick = () => { if (b.getAttribute("aria-disabled")) return toast("This part is being typed in. Coming soon."); go({ name:"dalail", n:+b.dataset.hizb }); window.scrollTo(0,0); });
  app.querySelectorAll("[data-dlx]").forEach(b => b.onclick = () => { if (b.getAttribute("aria-disabled")) return toast("This section is being typed in from a printed edition. Coming soon."); go({ name:"dalail", x:b.dataset.dlx }); });
  app.querySelectorAll("[data-dlmenu]").forEach(b => b.onclick = () => go({ name:"dalail" }));
  const dr = app.querySelector("#dlread"); if (dr) dr.onclick = () => { S.dalail = S.dalail || {}; S.dalail[new Date().toDateString()] = view.n; save(); toast("May Allah accept it"); render(); };
  app.querySelectorAll("[data-guide]").forEach(b => b.onclick = () => go({ name:"guide", id:b.dataset.guide }));
  app.querySelectorAll("[data-gstep]").forEach(b => b.onclick = () => { S.guides = S.guides || {}; const d = S.guides[view.id] = S.guides[view.id] || [], i = +b.dataset.gstep;
    const k = d.indexOf(i); if (k >= 0) d.splice(k, 1); else d.push(i); save(); const y = window.scrollY; render(); window.scrollTo(0, y); });
  const gr = $("#greset"); if (gr) gr.onclick = () => confirmBox("Clear all ticks for this guide?", () => { S.guides[view.id] = []; save(); render(); });
  if (view.name === "qibla") bindQibla(); if (view.name === "qada") bindQada(); if (view.name === "zakat") bindZakat();
  if (view.name === "inherit") bindInherit(); if (view.name === "salawat") bindSalawat(); if (view.name === "tasbih") bindTasbih(); if (view.name === "home") bindSalCard();
}
