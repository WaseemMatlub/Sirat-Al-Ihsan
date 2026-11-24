"""Dictionary for tap-to-look-up: Lane's Lexicon (public domain) and a classical Arabic-Arabic dictionary,
bucketed by the first two letters of the (unvowelled, hamza-normalised) headword."""
import json, os, re, collections
STRIP = lambda s: re.sub(r"[ً-ٰٟـ]", "", s)
NORM = lambda s: STRIP(s).replace("أ","ا").replace("إ","ا").replace("آ","ا").replace("ٱ","ا").replace("ى","ي").strip()
def bucket(k): return "_".join(f"{ord(c):04x}" for c in k[:2])
def build(src, field, name, cap):
    rows = json.load(open(f"json/{src}.json")); B = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in rows:
        k = NORM(r.get("Arabic", "")); v = (r.get(field) or "").strip()
        if not re.fullmatch(r"[ء-ي]+", k or "") or not v or v == r.get("Arabic"): continue
        B[bucket(k)][k].append(v[:cap])
    out = f"app/data/dict/{name}"; os.makedirs(out, exist_ok=True)
    for f in os.listdir(out): os.remove(f"{out}/{f}")
    for b, d in B.items(): json.dump(d, open(f"{out}/{b}.json", "w"), ensure_ascii=False, separators=(",", ":"))
    sizes = [os.path.getsize(f"{out}/{f}") for f in os.listdir(out)]
    print(name, len(B), "files, largest", max(sizes)//1024, "KB, total", sum(sizes)//1024, "KB")
build("Lanes_Lexicon", "English", "lane", 6000)
build("Arabic_Arabic_Dictionary", "Definition", "ar", 4000)
