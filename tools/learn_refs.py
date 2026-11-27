"""Attach a 'ref' to every lesson card and question: the exact section (and paragraph where the text
has English) of the book in the app's Library that the source line names, so students can tap it."""
import json, math, os, re, collections

TX = os.path.join(os.path.dirname(__file__), "..", "app", "data", "texts")

# source name (start of src) -> (library id, text file)
BOOKS = [
 ("nur al-idah", "t_nur", "nur_idah"), ("maraqi al-falah", "t_nur", "nur_idah"),
 ("mukhtasar al-quduri", "t_quduri", "quduri"),
 ("al-'aqidah al-tahawiyyah", "t_tahawiyya", "tahawiyya_full"),
 ("umm al-barahin", "t_umm", "umm"), ("al-fiqh al-akbar", "t_fiqhakbar", "fiqh_akbar"),
 ("jawharat al-tawhid", "t_jawhara", "jawhara"),
 ("sahih al-bukhari", "t_bukhari", "bukhari"), ("al-bukhari", "t_bukhari", "bukhari"),
 ("sahih muslim", "t_muslim", "muslim"), ("muslim", "t_muslim", "muslim"),
 ("al-fusul", "t_fusul", "fusul"), ("tarikh al-khulafa'", "t_tarikh_khulafa", "tarikh_khulafa"),
 ("bidayat al-hidayah", "t_bidaya", "bidaya"), ("al-risalah al-qushayriyyah", "t_risala", "risala"),
 ("al-munqidh", "t_munqidh", "munqidh"), ("ihya'", "t_ihya", "ihya"), ("al-tibyan", "t_tibyan", "tibyan"),
 ("ayyuha al-walad", "t_ayyuha", "ayyuha"), ("al-shama'il", "t_shamail", "shamail"),
 ("usul al-shashi", "t_shashi", "usul_shashi"), ("al-adhkar", "t_adhkar", "adhkar"),
 ("riyad al-salihin", "t_riyad", "riyad"), ("sunan al-tirmidhi", "t_tirmidhi", "tirmidhi"), ("al-tirmidhi", "t_tirmidhi", "tirmidhi"),
 ("sunan abi dawud", "t_abudawud", "abudawud"), ("sunan ibn majah", "t_ibnmajah", "ibnmajah"),
 ("sunan al-nasa'i", "t_nasai", "nasai"), ("al-nawawi's forty", "t_arbain", "arbain"),
 ("qur'an", "t_jalalayn", "jalalayn"), ("al-muqaddimah al-jazariyyah", "t_jazariyya", "jazariyya"),
]
# Arabic chapter to open, per lesson and book, for texts without English to match against
KEY = {
 "quduri": {"f_how2": "صفة الصلاة", "f_texts": "صفة الصلاة", "f_sahw": "السهو", "f_jamaah": "صفة الصلاة", "f_rakahs": "صفة الصلاة", "f_travel": "صلاة المسافر",
   "f_jumuah": "صلاة الجمعة", "f_sawm0": "كتاب الصوم", "fasting1": "كتاب الصوم", "fasting3": "كتاب الصوم", "zakat1": "كتاب الزكاة",
   "zakat2": "زكاة العروض", "zakat3": "دفع الصدقة", "f_fitr": "صدقة الفطر", "f_udhiyah": "الاضحيه", "hj1": "كتاب الحج", "hj2": "كتاب الحج",
   "hj3": "كتاب الحج", "hj4": "القران", "hj9": "التمتع", "hj5": "كتاب الحج", "hj6": "كتاب الحج", "hj7": "كتاب الحج", "hj8": "كتاب الحج",
   "hh3": "الذبائح", "hh4": "الكراهيه", "hh5": "الكراهيه", "hh6": "الربا", "sh_bayt": "دفع الصدقة", "f_money": "الربا", "f_death": "الجنائز",
   "f_nikah": "كتاب النكاح", "f_death": "الفرائض", "f_madhur": "الحيض", "zakat1b": "كتاب الزكاة"},
 "fusul": {"sr1": "نسبه", "sr1b": "ولادته", "sr3": "المعذبين", "sr_sorrow": "خروج النبي", "sr_aqabah": "العقبه", "sr4": "الاسراء",
   "sr_madinah": "المواخاه", "sr5": "بدر الكبرى", "sr_hudaybiyah": "الحديبيه", "sr6": "فتح مكه", "sr_passing": "وفاته", "sr_family": "اولاده",
   "sh_mothers": "ازواجه", "sr2": "مبعثه"},
 "tarikh_khulafa": {"sh_abubakr": "ابو بكر", "sh_umar": "عمر بن الخطاب", "sh_uthman": "عثمان بن", "sh_ali": "علي بن ابي", "sh_love": "علي بن ابي", "sh_bayt": "الحسن بن علي"},
 "bidaya": {"heart1": "توطئه", "heart3": "الغيبه", "heart4": "الحسد", "heart5": "اداب العالم", "ad_wake": "الاستيقاظ", "ad_eat": "البطن",
   "ad_home": "دخول المسجد", "ad_sleep": "النوم", "ad_limbs": "اداب العين", "ad_teach": "اداب العالم", "ad_salam": "العلاقه بالعوام"},
 "risala": {"tz_path": "باب الادب", "heart2": "التوبه", "tz_dhikr": "الذكر", "tz_tawakkul": "التوكل", "tz_sabr": "الصبر"},
 "munqidh": {"dd6": "اقسام علومهم", "dd2": "السفسطه", "dd3": "طرق الصوفيه", "dd4": "حقيقه النبوه", "dd5": "طرق الصوفيه"},
 "tibyan": {"qr0": "الباب الاول", "qr5": "الباب السادس"},
 "ayyuha": {"heart5": "ايها الولد"},
 "shamail": {"sr7": "خلق رسول"},
 "ihya": {"hh1": "الحلال", "hh2": "الورع", "hh6": "منكرات", "hh7": "منكرات", "hh_kabair": "الكبائر", "aq_shirk": "الرياء", "heart1": "العلم", "heart3": "الغيبه"},
 "usul_shashi": {"fiqh0": "الواجب بحكم"},
 "riyad": {"heart2": "التوبه", "ad_salam": "السلام"},
 "adhkar": {"ad_wake": "استيقظ", "ad_adhkar": "الصباح", "ad_dress": "لبس", "ad_sleep": "النوم"},
}
SURAH = {"al-fatihah": "الفاتحه", "al-baqarah": "البقره", "al 'imran": "ال عمران", "al-nisa'": "النساء", "al-ma'idah": "المائده", "al-tawbah": "التوبه",
  "al-ra'd": "الرعد", "al-hijr": "الحجر", "al-nahl": "النحل", "al-isra'": "الاسراء", "al-ahzab": "الاحزاب", "al-shura": "الشوري", "al-fath": "الفتح",
  "al-talaq": "الطلاق", "al-qiyamah": "القيامه", "al-'alaq": "العلق", "al-hujurat": "الحجرات", "al-nur": "النور", "luqman": "لقمان", "al-an'am": "الانعام"}

def norm(s):
    s = re.sub(r"[ً-ْٰـ]", "", s or "")
    return s.translate(str.maketrans("أإآٱةى", "ااااهي"))

_cache = {}
def load(f):
    if f in _cache: return _cache[f]
    d = json.load(open(os.path.join(TX, f + ".json")))
    secs = d["sections"]
    if d.get("split"):
        k = 0
        while os.path.exists(os.path.join(TX, f, f"{k}.json")):
            for j, s in enumerate(json.load(open(os.path.join(TX, f, f"{k}.json")))): secs[k * d["split"] + j].update(s)
            k += 1
    paras = [(i, j, t) for i, s in enumerate(secs) for j, t in enumerate(s.get("en") or [])]
    STOP = set("that this with from have they them their there which what when were will would your about been into only also because than then over just like each more most some such them these those does done must shall upon said says".split())
    toks = lambda t: {w for w in re.findall(r"[a-z]{4,}", t.lower().replace("'", "")) if w not in STOP}
    pt = [toks(t) for _, _, t in paras]
    df = collections.Counter(w for s in pt for w in s); N = max(1, len(pt))
    _cache[f] = (secs, paras, pt, {w: math.log(N / c) for w, c in df.items()}, toks)
    return _cache[f]

def by_heading(f, key):
    secs = load(f)[0]; k = norm(key)
    for i, s in enumerate(secs):
        if k in norm(s.get("h", "")) or k in norm(s.get("parent", "") or ""): return i
    return None

HADITH = {"bukhari", "muslim"}
def by_english(f, text, chapter=None, near=None, head="", allow=None):
    secs, paras, pt, idf, toks = load(f)
    if not paras: return None
    q = toks(text); hq = toks(head); best = (0, None)
    for (i, j, _), s in zip(paras, pt):
        if chapter and chapter.lower() not in (secs[i].get("parent") or "").lower(): continue
        if allow is not None:
            if i not in allow: continue
        elif near is not None and abs(i - near) > 8: continue
        ov = q & s
        hs = toks(f"{secs[i].get('he') or ''} {secs[i].get('h') or ''}")
        hb = sum(idf.get(w, 2) for w in (hq | q) & hs) / math.sqrt(len(hs) + 2) if hs else 0
        if len(ov) < 3 and hb < 1.5: continue
        sc = sum(idf.get(w, 0) for w in ov) / math.sqrt(len(s) + 4) + 1.5 * hb
        if sc > best[0]: best = (sc, (i, j))
    need = (2.8 if not chapter else 1.6) if f in HADITH else (0.3 if allow else 1.4)
    if best[0] > need: return best[1]
    if allow: return (allow[0], 0)
    return None

ANCHOR = {}
KEYC = {("tz_path", "A false guide"): "مقدمه", ("f_nikah", "Divorce"): "كتاب الطلاق", ("f_nikah", "Rights"): "النفقات",("sr5", "Uhud"): "احد", ("sr5", "The Trench"): "الخندق", ("heart4", "Showing off"): "الرياء", ("heart4", "Self-admiration"): "العجب",
  ("sr6", "The opening of Makkah"): "فتح مكه", ("sr6", "The farewell"): "حجه الوداع", ("sr4", "The Hijrah"): "هجره رسول", ("sr4", "The pledges of 'Aqabah"): "العقبه",
  ("sr3", "Abyssinia"): "المعذبين", ("sr3", "The boycott and Ta'if"): "مقاطعه", ("sr1b", "In the desert"): "ولادته", ("heart3", "Backbiting"): "الغيبه",
  ("ad_limbs", "Eyes and ears"): "اداب العين", ("ad_limbs", "The tongue"): "الكذب", ("ad_limbs", "Stomach, hands, feet"): "اداب البطن"}
TITLE = {}
R = lambda a, b: list(range(a, b + 1))
NUR = {"fiqh0": [], "f_istinja": R(11, 16), "purity1": R(1, 3), "purity2": [17], "purity3": R(22, 24), "purity4": [26, 27],
  "purity5": R(28, 33) + [62, 63], "f_najasa": R(66, 68), "purity6": R(34, 43), "fiqh_khuff": R(44, 51), "fiqh_hayd": R(52, 65),
  "f_times": R(74, 78), "f_adhan": R(79, 85), "prayer1": R(86, 95), "prayer2": [86, 87], "prayer3": [96, 161, 162], "f_how1": R(97, 100),
  "f_how2": R(99, 100), "f_rakahs": [99], "f_sunan": [97, 98, 113, 116], "f_sahw": R(161, 168), "prayer4": [111, 112, 157],
  "prayer5": R(119, 122), "f_sunnahs": R(123, 125) + [135, 136], "f_jamaah": R(101, 109) + [159], "f_travel": R(138, 144),
  "f_qada": [145, 154, 155], "f_jumuah": R(179, 183), "f_janazah": R(199, 216), "f_eid": R(184, 190), "f_sawm0": R(224, 236),
  "fasting1": [237], "fasting2": R(238, 247), "fasting3": R(247, 256), "qr5": [62, 63], "hh_kabair": [118], "zakat1": [], "f_death": R(199, 220),
  "f_madhur": [50, 64, 65, 53], "f_texts": [99, 120]}
def resolve(src, text, lid):
    s = src.replace("Hadith, ", "").strip(); low = s.lower()
    for name, lib, f in BOOKS:
        if not low.startswith(name): continue
        if f == "jalalayn":
            import learn_ayat as A
            m = re.match(r"qur'an,\s*(.+?)\s+(\d+)(?::(\d+))?", low)
            if not m: return None
            num = {v.lower(): k for k, v in A.NAME.items()}.get(m.group(1))
            if not num: return None
            if m.group(3): return jal_ref(num, int(m.group(3)))
            return jal_ref(num, int(m.group(2)))
        if f == "jazariyya":
            JZ = {"points of articulation": 1, "qualities": 2, "tajweed": 3, "ra's": 5, "lams": 6, "doubled nun": 10, "nun sakinah": 11,
                  "lengthening": 12, "stopping": 13, "conclusion": 18}
            ch = next((v for k, v in JZ.items() if k in low), None)
            if ch is None: return None
            hit = by_english(f, text, None, None, "", [ch])
            return {"b": lib, "i": ch, "j": hit[1] if hit and hit[0] == ch else 0}
        secs, paras = load(f)[:2]
        num = re.search(r"\((\d+)\)", s)
        if f in HADITH and num:
            pre = ("Bukhari " if f == "bukhari" else "Muslim ") + num.group(1) + "."
            for i, j, t in paras:
                if t.startswith(pre) or t.startswith(pre.replace(".", " ")): return {"b": lib, "i": i, "j": j}
        if paras:
            chap = None
            m = re.search(r"book of ([a-z' ]+)", low)
            if m and f in ("bukhari", "muslim"): chap = m.group(1).strip().split(" ")[-1]
            allow = NUR.get(lid) if f == "nur_idah" else None
            if allow == []: return None
            near = ANCHOR.get((lid, f)) if f not in HADITH else None
            head = ", ".join(s.split(",")[1:]) + " " + text.split(" ")[0]
            hit = by_english(f, text, chap, near, head, allow) or (by_english(f, text, None, near, head, allow) if chap else None)
            if hit: return {"b": lib, "i": hit[0], "j": hit[1]}
        key = KEYC.get((lid, TITLE.get("t"))) or KEY.get(f, {}).get(lid)
        if key:
            i = by_heading(f, key)
            if i is not None: return {"b": lib, "i": i}
        return None
    return None

def _anchors(courses):
    ANCHOR.clear()
    for c in courses:
        for l in c["lessons"]:
            by = collections.defaultdict(list)
            for x in l["cards"] + l["checks"]:
                low = x["src"].replace("Hadith, ", "").lower()
                for name, lib, f in BOOKS:
                    if low.startswith(name):
                        if f not in HADITH and load(f)[1]: by[f].append(f"{x.get('t','')} {x.get('x','')} {x.get('q','')} {x.get('a','')} {x.get('why','')}")
                        break
            for f, texts in by.items():
                hits = [by_english(f, t) for t in texts]; idx = [h[0] for h in hits if h]
                if idx: ANCHOR[(l["id"], f)] = sorted(idx)[len(idx) // 2]   # median section of the lesson's matches

def jal_ref(s, a):
    secs = load("jalalayn")[0]
    tag = f"[{s}.{a}]"
    for i, sec in enumerate(secs):
        for j, t in enumerate(sec.get("p") or []):
            if t.startswith(tag): return {"b": "t_jalalayn", "i": i, "j": j}
    return None

def add_refs(courses):
    _anchors(courses)
    stats = collections.Counter()
    for c in courses:
        for l in c["lessons"]:
            for x in l["cards"]:
                if x.get("ar") and x.get("ref"): stats[True] += 1; continue
                TITLE["t"] = x["t"]; r = resolve(x["src"], f"{x['t']} {x['x']}", l["id"]); stats[bool(r)] += 1
                if r: x["ref"] = r
                else: x.pop("ref", None)
            for x in l["checks"]:
                TITLE["t"] = None; r = resolve(x["src"], f"{x['q']} {x['a']} {x['why']}", l["id"]); stats[bool(r)] += 1
                if r: x["ref"] = r
                else: x.pop("ref", None)
    print("refs", dict(stats))
    return courses
