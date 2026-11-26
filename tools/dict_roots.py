"""Root dictionary in the familiar root-by-root layout: each root, then its verb forms (I to X) and its nouns with plurals.
Glosses from the Buckwalter Arabic Morphological Analyzer lexicon (Tim Buckwalter, (c) 2002 QAMUS LLC and the
Trustees of the University of Pennsylvania, GNU GPL v2). The layout is our own; no text is taken from Hans Wehr.
Writes app/data/dict/roots/<first letter>.json and an index of roots."""
import json, os, re, collections
SRC = "/home/claude/ext/pya/pyaramorph-0.2/pyaramorph/dictStems"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app", "data", "dict", "roots")
BW = {"'":"ء","|":"آ",">":"أ","&":"ؤ","<":"إ","}":"ئ","A":"ا","b":"ب","p":"ة","t":"ت","v":"ث","j":"ج","H":"ح","x":"خ","d":"د","*":"ذ","r":"ر","z":"ز",
      "s":"س","$":"ش","S":"ص","D":"ض","T":"ط","Z":"ظ","E":"ع","g":"غ","_":"ـ","f":"ف","q":"ق","k":"ك","l":"ل","m":"م","n":"ن","h":"ه","w":"و","Y":"ى","y":"ي",
      "F":"ً","N":"ٌ","K":"ٍ","a":"َ","u":"ُ","i":"ِ","~":"ّ","o":"ْ","`":"ٰ","{":"ٱ"}
def ar(s):
    s = re.sub(r"(?<=[^aiuo~FNK{A|<>])A", "aA", s)   # fatha before a long alif, as in a fully voweled text
    s = re.sub(r"~A", "~aA", s)
    return "".join(BW.get(c, "") for c in s).replace("ٱ", "ا")
def clean(g):
    g = re.sub(r"<pos>.*?</pos>", "", g).strip()
    parts = [p.strip() for p in g.split(";") if p.strip()]
    seen = []; [seen.append(p) for p in parts if p not in seen]
    return "; ".join(seen[:4])

# Which verb form, from the perfect stem pattern of a three-letter root
def form_of(pv, root):
    r = [c for c in root]
    if len(r) != 3: return None
    s = pv.replace("{", "A")
    a, b, c = [re.escape(x) for x in r]
    pats = [("X", f"Aisota{a}o{b}a{c}"), ("X", f"Aisota{a}a{c}"), ("VIII", f"Ai{a}ota{b}a{c}"), ("VII", f"Ainoa{a}a{b}a{c}"), ("VII", f"Aino{a}a{b}a{c}"),
            ("IX", f"Ai{a}o{b}a{c}~"), ("VI", f"ta{a}A{b}a{c}"), ("V", f"ta{a}a{b}~a{c}"), ("IV", f">a{a}o{b}a{c}"), ("IV", f">a{a}a{c}"), ("IV", f">a{a}A{c}"),
            ("III", f"{a}A{b}a{c}"), ("II", f"{a}a{b}~a{c}")]
    for f, p in pats:
        if s == p: return f
    if re.fullmatch(f"{a}a{b}[aiu]{c}", s) or re.fullmatch(f"{a}a{b}~", s) or re.fullmatch(f"{a}A{c}", s) or re.fullmatch(f"{a}a{b}[aAY]", s): return "I"
    if s.startswith("Aisota") or s.startswith("Ast"): return "X"
    if s.startswith("Ain"): return "VII"
    if s.startswith("Ai") and "t" in s[2:5]: return "VIII"
    if s.startswith("ta") and "~" in s: return "V"
    if s.startswith("ta") and "A" in s[2:5]: return "VI"
    if s.startswith(">a"): return "IV"
    if "~" in s and not s.endswith("~"): return "II"
    if len(s) >= 2 and s[1] == "A": return "III"
    return "I"
ORDER = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "Q"]

roots = collections.OrderedDict(); root = None; lemma = None
for line in open(SRC, encoding="utf-8", errors="ignore"):
    line = line.rstrip("\n")
    if line.startswith(";--- "):
        root = line[5:].split()[0]; roots.setdefault(root, collections.OrderedDict()); lemma = None; continue
    if line.startswith(";; "): lemma = line[3:].strip(); continue
    if not line or line.startswith(";") or root is None or lemma is None: continue
    f = line.split("\t")
    if len(f) < 4: continue
    roots[root].setdefault(lemma, []).append((f[1], f[2], f[3]))

out = collections.defaultdict(dict); index = []
for r, lems in roots.items():
    rk = ar(r.replace(">", "A").replace("<", "A").replace("|", "A"))
    if not rk or len(rk) < 2: continue
    verbs, nouns = {}, []
    for lem, stems in lems.items():
        cats = [c for _, c, _ in stems]; gl = clean(stems[0][2])
        if not gl: continue
        pv = next((v for v, c, _ in stems if c.startswith("PV") and "Pass" not in c), None)
        iv = next((v for v, c, _ in stems if c.startswith("IV") and "Pass" not in c), None)
        if pv:
            fm = form_of(pv, r) if len(r) == 3 else "Q"
            e = verbs.setdefault(fm or "I", {"pf": ar(pv) + ("" if pv.endswith(("A", "Y")) else "َ"), "ipf": "", "gl": []})
            if iv and not e["ipf"]:
                pre = "يُ" if any(c.startswith("IV_yu") for _, c, _ in stems) else "يَ"
                e["ipf"] = pre + ar(iv) + ("" if iv.endswith(("A", "Y", "w", "y")) else "ُ")
            for g in gl.split("; "):
                if g not in e["gl"] and len(e["gl"]) < 5: e["gl"].append(g)
        elif any(c.startswith("N") or c.startswith("Nap") for c in cats) and not any(c == "Nprop" for c in cats):
            forms = []
            for v, c, g in stems:
                w = ar(v)
                if w not in forms: forms.append(w)
            sing = forms[0]; pl = [w for w in forms[1:] if w != sing][:2]
            prev = next((x for x in nouns if x["w"] == sing), None)
            if prev: prev["gl"] = "; ".join(dict.fromkeys((prev["gl"] + "; " + gl).split("; "))); prev["pl"] = prev["pl"] or pl
            else: nouns.append({"w": sing, "pl": pl, "gl": gl})
    if not verbs and not nouns: continue
    entry = {"r": rk, "v": [dict(f=k, **verbs[k]) | {"gl": "; ".join(verbs[k]["gl"])} for k in ORDER if k in verbs], "n": nouns[:40]}
    out[rk[0]][rk] = entry; index.append(rk)

os.makedirs(OUT, exist_ok=True)
# English search index: word -> roots whose meanings use it
STOP = set("a an the of to in on for and or be with by as at from into one's oneself something someone sth s.o. o.s. etc".split())
en = collections.defaultdict(list)
for d in out.values():
    for rk, e in d.items():
        words = set()
        for x in e["v"] + e["n"]:
            for w in re.findall(r"[a-z]+", x["gl"].lower()):
                if len(w) > 2 and w not in STOP: words.add(w)
        for w in words:
            if len(en[w]) < 40: en[w].append(rk)
json.dump(en, open(os.path.join(OUT, "en.json"), "w"), ensure_ascii=False, separators=(",", ":"))
for k, v in out.items():
    json.dump(v, open(os.path.join(OUT, f"{ord(k):04x}.json"), "w"), ensure_ascii=False, separators=(",", ":"))
json.dump(sorted(set(index)), open(os.path.join(OUT, "index.json"), "w"), ensure_ascii=False, separators=(",", ":"))
print(len(index), "roots;", sum(len(e["v"]) for d in out.values() for e in d.values()), "verb forms;", sum(len(e["n"]) for d in out.values() for e in d.values()), "nouns")
print(json.dumps(out["ك"].get("كتب"), ensure_ascii=False)[:1400])
