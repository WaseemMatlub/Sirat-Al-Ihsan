// ---- tappable words: any glossary term in lessons, questions, explanations and notes opens its meaning
const GLOSS_MORE = [
 ["Makruh tahriman", "Prohibitively disliked (makruh tahrimi): close to haram. Doing it is a sin and deserves punishment, though less than haram, and whoever does it should repent. Its proof is not definitive, like wajib's. Examples: delaying 'Asr until the sun turns yellow, or praying while badly needing the toilet."],
 ["Makruh tanzihan", "Mildly disliked (makruh tanzihi): better to leave. There is no sin in doing it, but leaving it is rewarded. Examples: yawning in prayer without covering the mouth, or praying bareheaded out of laziness."],
 ["Fard kifayah", "A communal obligation: if some Muslims do it, the rest are free of it; if nobody does it, everyone who could have is sinful. Example: the funeral prayer."],
 ["Sunnah mu'akkadah", "A stressed sunnah: one the Prophet ﷺ did regularly. Leaving it now and then is not a sin, but making a habit of leaving it is blameworthy."],
 ["Ja'iz", "Permissible: no sin in doing it or leaving it."],
 ["Niyyah", "Intention: the purpose in the heart behind an act. Saying it with the tongue is not required."],
 ["Mukallaf", "A person who is accountable: Muslim, sane and having reached puberty."],
 ["Baligh", "Having reached puberty, after which the religious duties become binding."],
 ["Najis", "Impure: something that must be washed off the body, clothes or place of prayer before praying."],
 ["Tahir", "Pure: clean in the sense of the Shari'ah."],
 ["Ghalizah", "Heavy impurity, such as urine, stools, flowing blood and wine. Only a small amount (a dirham) is excused."],
 ["Khafifah", "Light impurity, such as the urine of animals that are eaten. Less than a quarter of a garment or limb is excused."],
 ["Mithqal", "A weight of about 4.25 g (20 qirats), used for gold, a dirham's weight of solid impurity, and a man's silver ring."],
 ["Masah", "Wiping with a wet hand rather than washing, as over the head or over khuffs."],
 ["Takbirat al-ihram", "The opening 'Allahu akbar' that begins the prayer. After it, talking, eating and so on are forbidden until the salam."],
 ["Qa'dah", "The sitting in the prayer, for the tashahhud."],
 ["Khushu'", "Humility and presence of heart in the prayer."],
 ["Tasbih", "Saying 'Subhan Allah' (Glory be to Allah); also the prayer beads used to count dhikr."],
 ["Nafl", "A voluntary act of worship beyond what is required."],
 ["Tarawih", "The sunnah night prayer of Ramadan, prayed after 'Isha'."],
 ["Tahajjud", "Voluntary prayer at night after waking from sleep."],
 ["Musafir", "A traveller in the Shari'ah sense: someone who sets out intending a journey of about 78 km (48 miles) or more."],
 ["Muqim", "A resident: someone at home, or who intends to stay fifteen days or more in one place."],
 ["Khutbah", "The sermon given by the imam, as on Friday and Eid."],
 ["Masjid", "A mosque: a place set aside for the prayer."],
 ["Imam", "The one who leads the prayer; also a title for a great scholar, such as Imam Abu Hanifah رَحِمَهُ اللَّهُ."],
 ["Mu'adhdhin", "The person who calls the adhan."],
 ["Ka'bah", "The House of Allah in Makkah, which Muslims face in prayer."],
 ["Talbiyah", "The words said in ihram: 'Labbayk Allahumma labbayk…' (Here I am, O Allah, here I am…)."],
 ["Muhrim", "A person who has entered ihram."],
 ["Raml", "Walking briskly with short steps and moving shoulders in the first three circuits of tawaf, for men."],
 ["Jamrah", "One of the three stone pillars at Mina that pilgrims throw pebbles at (plural jamarat)."],
 ["Tashriq", "The days of tashriq: the 11th, 12th and 13th of Dhu al-Hijjah."],
 ["Qiran", "Doing Hajj and 'umrah together in one ihram. The best form of Hajj in the Hanafi school."],
 ["Tamattu'", "Doing 'umrah in the months of Hajj, leaving ihram, then entering ihram again for Hajj in the same year."],
 ["Ifrad", "Doing Hajj alone, without 'umrah."],
 ["Dam", "A penalty sacrifice of a sheep or goat, owed for certain mistakes in Hajj, slaughtered in the Haram."],
 ["Udhiyah", "The Eid al-Adha sacrifice (qurbani): wajib in the Hanafi school on everyone who owns the nisab."],
 ["Sadaqah", "Charity given for Allah's sake, beyond what is required."],
 ["Riba", "Interest or usury: an unlawful increase in a loan or in exchanging certain goods. A major sin."],
 ["Ahl al-Kitab", "The People of the Book: Jews and Christians."],
 ["Mahram", "A close relative a person can never marry, such as a parent, child or sibling. A woman travels with a mahram."],
 ["Wara'", "Scrupulousness: staying away from what is doubtful out of fear of falling into the haram."],
 ["Ghibah", "Backbiting: saying something true about someone behind their back that they would dislike. A major sin."],
 ["Namimah", "Tale-carrying: passing on what people say to stir up trouble between them."],
 ["Kabirah", "A major sin (plural kaba'ir): one with a specific threat of punishment, a curse or a legal penalty."],
 ["Taqwa", "God-consciousness: guarding yourself from Allah's displeasure by obeying Him and avoiding sin."],
 ["Sabr", "Patience: holding yourself to obedience, away from sin, and steady in hardship."],
 ["Shukr", "Gratitude to Allah, with the heart, the tongue and the limbs."],
 ["Tawakkul", "Trust in Allah while still taking the means."],
 ["Zuhd", "Detachment: not letting the world take hold of the heart, even while using it."],
 ["Nafs", "The self or ego, which inclines to desires and must be disciplined."],
 ["Adab", "Good manners and proper conduct, with Allah and with people."],
 ["Adhkar", "Words of remembrance said at set times, such as morning, evening and after prayer (singular dhikr)."],
 ["Bismillah", "'In the name of Allah': said before eating, entering, starting any good act."],
 ["Shahadah", "The testimony of faith: 'There is no god but Allah, and Muhammad is the Messenger of Allah.'"],
 ["Akhirah", "The Hereafter: life after death, the Day of Judgement, Paradise and the Fire."],
 ["Barzakh", "The life of the grave, between death and the Resurrection."],
 ["Qiyamah", "The Day of Resurrection, when all are raised and judged."],
 ["Shafa'ah", "Intercession: asking for good for others on the Day of Judgement, first of all by the Prophet ﷺ."],
 ["Jinn", "Beings created from smokeless fire, accountable like humans, some believers and some not."],
 ["Wahy", "Revelation from Allah to His prophets."],
 ["Surah", "A chapter of the Qur'an. There are 114."],
 ["Ayah", "A verse of the Qur'an; also a sign of Allah."],
 ["Mushaf", "A written copy of the Qur'an. Wudu is needed to touch it."],
 ["Hijrah", "The migration of the Prophet ﷺ from Makkah to Madinah, which begins the Islamic calendar."],
 ["Ansar", "'The Helpers': the Muslims of Madinah who took in the Prophet ﷺ and the emigrants."],
 ["Muhajirun", "'The Emigrants': the Muslims who left Makkah for Allah's sake and moved to Madinah."],
 ["Ahl al-Bayt", "The family of the Prophet ﷺ: his wives, his children and their descendants, and his relatives from Banu Hashim."],
 ["Khalifah", "Caliph: the leader of the Muslims after the Prophet ﷺ. The first four are Abu Bakr, 'Umar, 'Uthman and 'Ali رَضِيَ اللَّهُ عَنْهُمْ."],
 ["Ijma'", "Consensus of the qualified scholars of the Ummah on a ruling."],
 ["Qiyas", "Analogy: applying a ruling from the Qur'an or Sunnah to a new case with the same reason."],
 ["Taqlid", "Following a qualified scholar or school without knowing every proof yourself, as most people must."],
 ["Mujtahid", "A scholar able to derive rulings directly from the sources."],
 ["Fatwa", "A ruling given by a qualified scholar (mufti) in answer to a question."],
 ["Bid'ah", "An innovation in the religion with no basis in the Shari'ah."],
 ["Shari'ah", "The sacred law: what Allah has commanded and forbidden."],
 ["Mawlid", "The birth of the Prophet ﷺ, and gatherings that remember it."],
 ["Murshid", "A spiritual guide in the path of tazkiyah."],
 ["Tariqah", "A Sufi path of purifying the heart under a guide, such as the Naqshbandi path."],
 ["Kaffarah", "An expiation owed for certain sins, such as breaking a Ramadan fast on purpose or breaking an oath."],
 ["Suhur", "The pre-dawn meal before a fast."],
 ["I'tikaf", "Staying in the masjid with the intention of worship, especially the last ten nights of Ramadan."],
 ["Laylat al-Qadr", "The Night of Power in the last ten nights of Ramadan, better than a thousand months."],
 ["Fathah", "The short vowel 'a', a small line above the letter."],
 ["Kasrah", "The short vowel 'i', a small line below the letter."],
 ["Dammah", "The short vowel 'u', a small waw above the letter."],
 ["Sukun", "A small circle above a letter: it has no vowel."],
 ["Shaddah", "A sign above a letter that doubles it."],
 ["Tanween", "A doubled vowel sign at the end of a word, adding an 'n' sound: -an, -in, -un."],
 ["Ghunnah", "The nasal sound from the nose, held about two counts, in nun and mim."],
 ["Madd", "Lengthening a long vowel: two counts naturally, up to six in some cases."],
 ["Qalqalah", "A slight bounce on the letters ق ط ب ج د when they have a sukun."],
 ["Makhraj", "The point in the mouth or throat a letter comes from (plural makharij)."],
 ["Izhar", "Saying the nun or mim clearly, without hiding or merging it."],
 ["Idgham", "Merging one letter into the next."],
 ["Iqlab", "Turning a nun sakinah or tanween into a hidden mim before ba'."],
 ["Ikhfa'", "Hiding a letter: saying it lightly through the nose, between clear and merged."],
 ["Hafs", "The narration of the Qur'an from Imam 'Asim through Hafs, the one most Muslims recite today."],
 ["Nafaqah", "Maintenance: the food, clothing and housing a husband owes his wife, and a father his children."],
 ["Mahr", "The marriage gift the husband owes the wife. It is her property alone."],
 ["Walimah", "The wedding meal held by the husband after the marriage: a sunnah."],
 ["Khitbah", "An engagement: a promise to marry. It does not make the couple lawful to each other."],
 ["Kafa'ah", "Suitability: the husband being a fitting match for the wife, mainly in religion and character."],
 ["Khul'", "A separation the wife asks for, giving back the mahr or something else for her release."],
 ["Talaq", "Divorce pronounced by the husband."],
 ["Raj'i", "A revocable divorce: after one or two talaqs the husband may take his wife back during the 'iddah."],
 ["'Iddah", "The waiting period after divorce or death before a woman may remarry."],
 ["Hadanah", "Custody: the right to raise young children, which goes first to the mother."],
 ["Rada'ah", "Nursing: a child nursed by a woman within the first two years becomes like her own child for marriage purposes."],
 ["Silat al-rahim", "Keeping ties with relatives: a duty, and cutting them is a major sin."],
 ["'Aqiqah", "The sacrifice for a newborn, on the seventh day."],
 ["Istikharah", "The prayer and du'a for asking Allah to choose what is best in a decision."],
 ["Halalah", "A marriage arranged only to make a thrice-divorced woman lawful again to her first husband. The Prophet ﷺ cursed it."],
 ["Ruqyah", "Healing by reciting the Qur'an and prophetic du'as over someone."],
];
const GLOSS_ALIAS = { "Makruh tahriman":["makruh tahrimi","makrooh tahrimi","tahrimi","tahriman"], "Makruh tanzihan":["makruh tanzihi","makruh tanzeehi","makrooh tanzihi","tanzihi","tanzeehi","tanzihan"], "Istinja'":["istinja"], "Istibra'":["istibra"], "Rak'ah":["rak'ahs","rakah","rakat"], "Wudu":["wudu'","ablution"], "Sujud":["sajdah","prostration"],
  "Qada'":["qada","making up"], "Qasr":["shortening the prayer"], "Hayd":["menstruation"], "Najasah":["impurity","najasa"], "Khuffs":["khuff","leather socks"],
  "Dirham (as a measure)":["dirham"], "'Umrah":["umrah"], "Sahabah":["sahabi","Companion","Companions"], "Wali (plural awliya')":["wali","awliya'","awliya"],
  "Fard al-'Ayn":["fard al-ayn","fard 'ayn"], "Sajdat al-sahw":["sajdat al-sahw","prostration of forgetfulness"], "Zakat al-Fitr":["zakat al-fitr","sadaqat al-fitr"],
  "Karamah":["karamat"], "Mu'jizah":["mu'jizat","miracle"], "Du'a":["du'as","dua"], "Salawat":["salat 'ala al-nabi"], "Kabirah":["kaba'ir","major sin","major sins"],
  "Jamrah":["jamarat"], "Udhiyah":["qurbani"], "Mu'adhdhin":["muezzin"], "Ahl al-Kitab":["Kitabi"], "Ghalizah":[], "Adhkar":["adhkar"], "Ayah":["ayat"], "Surah":["surahs"],
  "Taqwa":[], "Niyyah":["intention"], "Musafir":["traveller"], "Imam":[], "Masjid":["masjids"], "Nafl":["nawafil"], "Mahram":[] };
const GLOSS_SKIP = new Set(["Allah", "ﷺ", "رَضِيَ اللَّهُ عَنْهُ", "رَحِمَهُ اللَّهُ", "عَلَيْهِ السَّلَامُ"]);
let _glMap = null, _glRe = null;
function glossAll(){ return GLOSSARY.concat(GLOSS_MORE); }
function glBuild(){
  if (_glRe) return; _glMap = new Map(); const keys = [];
  for (const [t, d] of glossAll()) { if (GLOSS_SKIP.has(t)) continue;
    const base = t.replace(/\s*\(.*\)$/, ""), names = [base, ...(GLOSS_ALIAS[t] || [])];
    for (const n of names) { const k = n.toLowerCase(); if (!_glMap.has(k)) { _glMap.set(k, [t, d]); keys.push(n); } } }
  keys.sort((a, b) => b.length - a.length);
  const rx = s => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&").replace(/'/g, "['’]?");
  _glRe = new RegExp(`(?<![A-Za-z'’\\-])(${keys.map(rx).join("|")})(?:s)?(?![A-Za-z\\-])`, "gi");
}
function glLookup(w){ glBuild(); const k = w.toLowerCase().replace(/’/g, "'"); return _glMap.get(k) || _glMap.get(k.replace(/s$/, "")) || _glMap.get(k.replace(/'/g, "")) ||
  [..._glMap.entries()].find(([n]) => n.replace(/'/g, "") === k.replace(/'/g, ""))?.[1]; }
const GL_SEL = ".sw-card h2, .sw-card > p:not(.src), p.q, .explain-box p:not(.eb-h):not(.eb-src), .rc-x, .nsec p, .bp-why";
function glDecorate(root){
  if (!root || S.gloss === false) return; glBuild();
  root.querySelectorAll(GL_SEL).forEach(el => {
    if (el.dataset.gl || el.closest("button, summary, a, .gloss")) return; el.dataset.gl = "1";
    const seen = new Set(), walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const tn of nodes) {
      if (tn.parentElement.closest("button, .gl-w, [lang=ar]")) continue;
      const s = tn.nodeValue; _glRe.lastIndex = 0; let m, last = 0, frag = null;
      while ((m = _glRe.exec(s))) {
        if (/^(say|says|said|sad|din|amin|man)$/i.test(m[0])) continue;   // ordinary English words that look like terms without the apostrophe
        const hit = glLookup(m[1]); if (!hit || seen.has(hit[0])) continue; seen.add(hit[0]);
        frag = frag || document.createDocumentFragment();
        frag.append(s.slice(last, m.index));
        const b = document.createElement("button"); b.type = "button"; b.className = "gl-w"; b.dataset.term = hit[0]; b.textContent = m[0];
        b.setAttribute("aria-label", `${m[0]}: tap for meaning`); frag.append(b); last = m.index + m[0].length;
      }
      if (frag) { frag.append(s.slice(last)); tn.replaceWith(frag); }
    }
  });
}
function glShow(term){
  const hit = glossAll().find(([t]) => t === term); if (!hit) return;
  document.querySelector(".gl-sheet")?.remove();
  const d = document.createElement("div"); d.className = "gl-sheet"; d.setAttribute("role", "dialog"); d.setAttribute("aria-modal", "true"); d.setAttribute("aria-label", hit[0]);
  d.innerHTML = `<div class="gl-in"><div class="gl-top"><h2>${esc(hit[0])}</h2><button class="x" aria-label="Close">${ICON.x}</button></div><p>${esc(hit[1])}</p>
    <button class="linkbtn small" data-allwords>See all words to know</button></div>`;
  const prev = document.activeElement, close = () => { d.remove(); prev && prev.focus && prev.focus(); };
  d.addEventListener("click", e => { if (e.target === d || e.target.closest(".x")) close(); if (e.target.closest("[data-allwords]")) { close(); go({ name:"glossary" }); } });
  d.addEventListener("keydown", e => { if (e.key === "Escape") close(); });
  document.body.append(d); d.querySelector(".x").focus();
}
document.addEventListener("click", e => { const b = e.target.closest(".gl-w"); if (b) { e.preventDefault(); e.stopPropagation(); glShow(b.dataset.term); } }, true);
(() => { let q = 0; const app = document.getElementById("app"); if (!app || typeof MutationObserver === "undefined") return;
  new MutationObserver(() => { if (q) return; q = requestAnimationFrame(() => { q = 0; glDecorate(app); }); }).observe(app, { childList:true, subtree:true }); })();
