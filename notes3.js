/* ============================ Highlights and notes in the reader (Kindle-style) ============================
   S.hl["bookId|section"] = [{ id, p, w:"ar"|"en", q, k, c, note, at }]
   q: the selected text with harakat removed; k: which occurrence of q in that paragraph. Matching ignores harakat,
   so highlights survive switching harakat on and off. Saved on the device with the rest of the user's data. */
const HL_COLORS = [["y","Yellow"],["g","Green"],["b","Blue"],["p","Pink"]];
const hlNorm = s => s.replace(/[ً-ٰٟـۖ-ۭ‌-‏]/g, "").replace(/\s+/g, " ");
function hlMap(text){ let n = "", map = [], sp = false;
  for (let i = 0; i < text.length; i++) { const ch = text[i];
    if (/[ً-ٰٟـۖ-ۭ‌-‏]/.test(ch)) continue;
    if (/\s/.test(ch)) { if (sp) continue; sp = true; n += " "; map.push(i); continue; }
    sp = false; n += ch; map.push(i); }
  return { n, map }; }
function hlRange(el, s, e){ const r = document.createRange(), w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let pos = 0, node, set = false;
  while ((node = w.nextNode())) { const L = node.textContent.length;
    if (!set && s < pos + L) { r.setStart(node, s - pos); set = true; }
    if (set && e <= pos + L) { r.setEnd(node, e - pos); return r; } pos += L; }
  return null; }
function hlList(key){ S.hl = S.hl || {}; return S.hl[key] || (S.hl[key] = []); }
function hlApply(bid, i){
  const key = `${bid}|${i}`, list = (S.hl||{})[key] || [];
  list.forEach(h => { const para = document.querySelector(`.para[data-pj="${h.p}"] .${h.w === "en" ? "en-read" : "ar-read"}`); if (!para) return;
    const { n, map } = hlMap(para.textContent); let at = -1, from = 0;
    for (let c = 0; c <= h.k; c++) { at = n.indexOf(h.q, from); if (at < 0) break; from = at + 1; }
    if (at < 0) return; const s = map[at], e = map[at + h.q.length - 1] + 1;
    // extend the end over any harakat that follow the last letter
    let end = e; const t = para.textContent; while (end < t.length && /[ً-ٰٟۖ-ۭ]/.test(t[end])) end++;
    const r = hlRange(para, s, end); if (!r) return;
    try { const m = document.createElement("mark"); m.className = `hl hl-${h.c}${h.note ? " has-note" : ""}`; m.dataset.hl = h.id; m.tabIndex = 0;
      m.setAttribute("aria-label", h.note ? "Highlight with a note" : "Highlight"); m.appendChild(r.extractContents()); r.insertNode(m); } catch(e){} });
}
let HLBAR = null;
function hlHideBar(){ if (HLBAR) { HLBAR.remove(); HLBAR = null; } }
function hlFromSelection(bid, i){
  const sel = getSelection(); if (!sel || sel.isCollapsed || !sel.rangeCount) return null;
  const r = sel.getRangeAt(0), el = (r.commonAncestorContainer.nodeType === 3 ? r.commonAncestorContainer.parentElement : r.commonAncestorContainer).closest(".ar-read,.en-read");
  if (!el || !el.closest(".reader")) return null;
  const para = el.closest(".para"); if (!para) return null;
  const pre = document.createRange(); pre.selectNodeContents(el); pre.setEnd(r.startContainer, r.startOffset);
  const before = hlNorm(pre.toString()), q = hlNorm(r.toString()).trim(); if (q.length < 2) return null;
  const full = hlMap(el.textContent).n; let k = 0, from = 0, at;
  const startN = before.replace(/^\s+/, "").length + (before.length - before.replace(/^\s+/, "").length);
  while ((at = full.indexOf(q, from)) >= 0 && at < startN - 1) { k++; from = at + 1; }
  return { p: +para.dataset.pj, w: el.classList.contains("en-read") ? "en" : "ar", q, k, rect: r.getBoundingClientRect() };
}
function hlSave(bid, i, sel, c, note){
  const list = hlList(`${bid}|${i}`), h = { id: Date.now().toString(36) + Math.random().toString(36).slice(2, 5), p: sel.p, w: sel.w, q: sel.q, k: sel.k, c, note: note || "", at: Date.now() };
  list.push(h); save(); return h; }
function hlShowBar(b, i, sel){
  hlHideBar(); const bar = HLBAR = document.createElement("div"); bar.className = "hlbar"; bar.setAttribute("role", "toolbar"); bar.setAttribute("aria-label", "Highlight");
  bar.innerHTML = HL_COLORS.map(([c, t]) => `<button class="hlc hl-${c}" data-c="${c}" aria-label="Highlight ${t}"></button>`).join("") +
    `<span class="hlsep"></span><button class="hlbtn" data-act="note">Note</button><button class="hlbtn" data-act="copy">Copy</button>`;
  document.body.appendChild(bar);
  const top = sel.rect.bottom + 10 + bar.offsetHeight > innerHeight - 90 ? sel.rect.top - bar.offsetHeight - 10 : sel.rect.bottom + 10;
  bar.style.top = Math.max(8, top) + "px"; bar.style.left = Math.min(innerWidth - bar.offsetWidth - 8, Math.max(8, sel.rect.left + sel.rect.width / 2 - bar.offsetWidth / 2)) + "px";
  bar.onmousedown = e => e.preventDefault();
  bar.querySelectorAll("[data-c]").forEach(x => x.onclick = () => { hlSave(b.id, i, sel, x.dataset.c); getSelection().removeAllRanges(); hlHideBar(); hlRedraw(b, i); });
  bar.querySelector('[data-act="copy"]').onclick = () => { const t = String(getSelection()); (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(() => toast("Copied"), () => {}); hlHideBar(); };
  bar.querySelector('[data-act="note"]').onclick = () => { getSelection().removeAllRanges(); hlHideBar(); const h = hlSave(b.id, i, sel, "y"); hlRedraw(b, i); hlEdit(b, i, h.id, true); };
}
function hlRedraw(b, i){ const y = document.querySelector(".pbody") ? document.querySelector(".pbody").scrollTop : 0; $("#app").innerHTML = readView(b, i); bindRead(b, i); const pb = document.querySelector(".pbody"); if (pb) pb.scrollTop = y; }
function hlEdit(b, i, id, fresh){
  const list = hlList(`${b.id}|${i}`), h = list.find(x => x.id === id); if (!h) return;
  modal(`<h2 style="margin:0 0 8px">${fresh ? "Add a note" : "Highlight"}</h2>
    <blockquote class="hlq ${h.w === "ar" ? "ar" : ""}" ${h.w === "ar" ? 'dir="rtl" lang="ar"' : ""}>${esc(h.q)}</blockquote>
    <div class="spread"><label class="small" for="hlnote" style="font-weight:700">Your note</label>${micBtn()}</div><textarea id="hlnote" rows="4" placeholder="Write a note, or tap the mic and speak…">${esc(h.note)}</textarea>
    <div class="hlcols" role="group" aria-label="Colour">${HL_COLORS.map(([c, t]) => `<button class="hlc hl-${c} ${h.c === c ? "on" : ""}" data-c="${c}" aria-label="${t}" aria-pressed="${h.c === c}"></button>`).join("")}</div>
    <div class="btnrow"><button class="btn ghost" id="hldel">Delete</button><button class="btn" id="hlok">Save</button></div>`, (el, close) => {
      let c = h.c; el.querySelectorAll("[data-c]").forEach(x => x.onclick = () => { c = x.dataset.c; el.querySelectorAll("[data-c]").forEach(y => { y.classList.toggle("on", y === x); y.setAttribute("aria-pressed", y === x); }); });
      const ta = el.querySelector("#hlnote"); setTimeout(() => ta.focus(), 50); bindMic(el, ta);
      el.querySelector("#hlok").onclick = () => { h.note = ta.value.trim(); h.c = c; save(); close(); hlRedraw(b, i); if (h.note) toast("Note saved"); };
      el.querySelector("#hldel").onclick = () => { list.splice(list.indexOf(h), 1); save(); close(); hlRedraw(b, i); toast("Highlight removed"); };
      el.onclick = e => { if (e.target === el) close(); }; });
}
function hlBind(b, i){
  hlApply(b.id, i);
  document.querySelectorAll("mark.hl").forEach(m => { const open = e => { e.stopPropagation(); hlEdit(b, i, m.dataset.hl); }; m.onclick = open; m.onkeydown = e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(e); } }; });
  let t; document.onselectionchange = () => { clearTimeout(t); t = setTimeout(() => { if (!document.querySelector(".reader")) { hlHideBar(); document.onselectionchange = null; return; }
    const s = hlFromSelection(b.id, i); if (s) hlShowBar(b, i, s); else hlHideBar(); }, 250); };
}
// all highlights and notes for one book, or every book
function hlEntries(bid){ const out = [];
  for (const [k, list] of Object.entries(S.sticky || {})) { const [id, i] = k.split("|"); if (bid && id !== bid) continue; list.forEach(n => out.push({ id:n.id, q:"Sticky note", note:n.t, c:n.c, w:"en", at:n.at, bid:id, i:+i, sticky:true })); } for (const [k, list] of Object.entries(S.hl || {})) { const [id, i] = k.split("|"); if (bid && id !== bid) continue; list.forEach(h => out.push({ ...h, bid:id, i:+i })); }
  return out.sort((a, b) => a.bid === b.bid ? (a.i - b.i || a.p - b.p) : 0); }
function hlListHtml(entries, showBook){
  return entries.length ? `<div class="stack">${entries.map(h => { const bk = bookById(h.bid); return `<button class="item hlitem" data-read="${h.bid}|${h.i}"><span class="hlsw hl-${h.c}" aria-hidden="true"></span>
    <span style="min-width:0;flex:1">${showBook && bk ? `<span class="s" style="display:block">${esc(bk.title)} · section ${h.i + 1}</span>` : `<span class="s" style="display:block">Section ${h.i + 1}</span>`}
      <span class="t ${h.w === "ar" ? "ar" : ""}" style="display:block">${esc(snip(h.q, 120))}</span>${h.note ? `<span class="hlnote-s">${esc(h.note)}</span>` : ""}</span></button>`; }).join("")}</div>`
    : `<p class="muted">Select any words in a book to highlight them or add a note.</p>`; }
function notesView(){ const all = hlEntries(); return shell(`<button class="back" data-go="library">${ICON.back} Library</button><h1>Your notes</h1>
  <p class="muted" style="margin:0 0 14px">${all.length ? `${all.length} highlight${all.length > 1 ? "s" : ""}, ${all.filter(h => h.note).length} with notes. Tap one to open it in the book.` : "Highlights and notes you make in any book appear here."}</p>${hlListHtml(all, true)}`); }

/* ---- Voice notes: speech-to-text where the phone supports it ---- */
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const micBtn = () => SR ? `<button type="button" class="micbtn" id="mic" aria-label="Speak your note"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/></svg><span>Speak</span></button>` : "";
function bindMic(el, ta){
  const b = el.querySelector("#mic"); if (!b || !SR) return; let rec = null;
  b.onclick = () => { if (rec) { rec.stop(); return; }
    rec = new SR(); rec.lang = S.micLang || "en-GB"; rec.interimResults = true; rec.continuous = true; const base = ta.value ? ta.value.trimEnd() + " " : "";
    rec.onresult = e => { let t = ""; for (const r of e.results) t += r[0].transcript; ta.value = base + t; };
    rec.onend = () => { rec = null; b.classList.remove("on"); b.querySelector("span").textContent = "Speak"; };
    rec.onerror = e => { if (e.error === "not-allowed") toast("Allow the microphone for this app to speak notes."); };
    try { rec.start(); b.classList.add("on"); b.querySelector("span").textContent = "Stop"; } catch(e){ rec = null; } };
}
/* ---- Sticky notes: a note pinned to a page of a book, no highlight needed ---- */
function stickyList(bid, i){ S.sticky = S.sticky || {}; return S.sticky[`${bid}|${i}`] || (S.sticky[`${bid}|${i}`] = []); }
function stickyHtml(bid, i){ const L = (S.sticky||{})[`${bid}|${i}`] || [];
  return `<div class="stickies">${L.map(n => `<button class="sticky st-${n.c||"y"}" data-sticky="${n.id}"><span class="st-pin" aria-hidden="true"></span>${esc(snip(n.t, 140))}</button>`).join("")}
    <button class="sticky-add" id="sticky-add">+ Sticky note</button></div>`; }
function stickyEdit(b, i, id){
  const L = stickyList(b.id, i), n = id ? L.find(x => x.id === id) : { id:"s" + Date.now().toString(36), t:"", c:"y", at:Date.now() };
  modal(`<h2 style="margin:0 0 8px">${id ? "Sticky note" : "New sticky note"}</h2><p class="small muted" style="margin:0 0 8px">Pinned to this page of ${esc(b.title)}.</p>
    <div class="spread"><label class="small" for="stnote" style="font-weight:700">Note</label>${micBtn()}</div><textarea id="stnote" rows="5" placeholder="Write, or tap the mic and speak…">${esc(n.t)}</textarea>
    <div class="hlcols" role="group" aria-label="Colour">${HL_COLORS.map(([c, t]) => `<button class="hlc hl-${c} ${n.c === c ? "on" : ""}" data-c="${c}" aria-label="${t}" aria-pressed="${n.c === c}"></button>`).join("")}</div>
    <div class="btnrow">${id ? `<button class="btn ghost" id="stdel">Delete</button>` : `<button class="btn ghost" id="stx">Cancel</button>`}<button class="btn" id="stok">Save</button></div>`, (el, close) => {
      let c = n.c; el.querySelectorAll("[data-c]").forEach(x => x.onclick = () => { c = x.dataset.c; el.querySelectorAll("[data-c]").forEach(y => { y.classList.toggle("on", y === x); y.setAttribute("aria-pressed", y === x); }); });
      const ta = el.querySelector("#stnote"); setTimeout(() => ta.focus(), 50); bindMic(el, ta);
      el.querySelector("#stok").onclick = () => { n.t = ta.value.trim(); n.c = c; if (!n.t) return close(); if (!id) L.push(n); save(); close(); hlRedraw(b, i); toast("Sticky note saved"); };
      const d = el.querySelector("#stdel"); if (d) d.onclick = () => { L.splice(L.indexOf(n), 1); save(); close(); hlRedraw(b, i); };
      const x = el.querySelector("#stx"); if (x) x.onclick = close; el.onclick = e => { if (e.target === el) close(); }; });
}
function stickyBind(b, i){
  const a = $("#sticky-add"); if (a) a.onclick = () => stickyEdit(b, i);
  document.querySelectorAll("[data-sticky]").forEach(x => x.onclick = () => stickyEdit(b, i, x.dataset.sticky));
}
