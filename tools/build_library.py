"""Build the new full books for the Library.
- OpenITI texts: parsed, long sections cut into readable pages.
- Books we already have line by line (with English): Tahawiyya, Umm al-Barahin, Jawhara, Burda, Bukhari, Muslim.
- Anything over ~1 MB is written split: an index (headings only) plus parts fetched as the student reads."""
import json, os, re, sys
sys.path.insert(0, "tools")
from oiti_parse import parse
from honorifics import honor
from fixjoin import fixjoin
OUT = "app/data/texts"; RAW = "/home/claude/texts_raw"
HAR = re.compile(r"[ً-ْٰ]")
PAGE = 6000

def paginate(secs):
    out = []
    for s in secs:
        if sum(len(p) for p in s["p"]) <= PAGE * 1.4: out.append(s); continue
        pages, cur, n = [], [], 0
        for p in s["p"]:
            if cur and n + len(p) > PAGE: pages.append(cur); cur, n = [], 0
            cur.append(p); n += len(p)
        if cur: pages.append(cur)
        for k, pg in enumerate(pages):
            t = {**s, "p": pg, "h": f"{s['h']} ({k+1}/{len(pages)})", "parent": s.get("parent") or s["h"]}
            out.append(t)
    return out

def write(book, secs, extra=None):
    d = {"id": book, "sections": secs, **(extra or {})}
    raw = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
    for f in os.listdir(OUT):                                    # clear old parts
        if f == book and os.path.isdir(f"{OUT}/{f}"):
            for x in os.listdir(f"{OUT}/{f}"): os.remove(f"{OUT}/{f}/{x}")
    if len(raw.encode()) < 1_000_000:
        open(f"{OUT}/{book}.json", "w").write(raw); print(book, len(secs), "sections", len(raw)//1024, "KB"); return
    os.makedirs(f"{OUT}/{book}", exist_ok=True)
    size = sum(len(json.dumps(s, ensure_ascii=False)) for s in secs) / len(secs); ch = max(5, int(350_000 / size))
    for k in range(0, len(secs), ch):
        json.dump(secs[k:k+ch], open(f"{OUT}/{book}/{k//ch}.json", "w"), ensure_ascii=False, separators=(",", ":"))
    idx = [{k: v for k, v in s.items() if k in ("h", "he", "parent", "lvl")} | {"n": len(s["p"])} for s in secs]
    json.dump({**d, "sections": idx, "split": ch}, open(f"{OUT}/{book}.json", "w"), ensure_ascii=False, separators=(",", ":"))
    print(book, len(secs), "sections, split into", -(-len(secs)//ch), "parts of", ch)

# 1. OpenITI
META_P = re.compile(r"^(المؤلف|الناشر|الطبعة|عدد الأجزاء|المحقق|حققه|راجعه|«المحققون»|\[ترقيم|\[الكتاب مرقم)")
for b in ["majalla", "kanz", "jalalayn", "qatr", "alfiyya", "mughni", "iqtisad", "hidaya",
          "risala", "kafiya", "maqamat", "manar", "shifa", "tadhkira", "baydawi", "mukhtasar_maani", "milal", "ihya", "tawdih",
          "muwatta", "abudawud", "tirmidhi", "nasai", "ibnmajah", "sharh_maani"]:
    raw = open(f"{RAW}/{b}.txt", encoding="utf-8").read()
    raw = re.sub(r"### \| \[حكم الألباني\] :\n# [^\n]*\n(~~[^\n]*\n)*", "", raw)     # modern gradings added by an editor
    secs = parse(raw)
    for x in secs:                                   # edition footnote markers and Shamela catalogue lines
        x["p"] = [re.sub(r"\s*«\d+»", "", q) for q in x["p"] if not META_P.match(q) and "الناشر:" not in q]
        x["h"] = re.sub(r"^CHECK\s*", "", x["h"]); x["h"] = re.sub(r"^\d+\s*-\s*", "", x["h"])
    secs = [x for x in secs if x["p"]]
    merged = []                                      # page-number headings ("[ص: 12]") are not chapters
    for x in secs:
        if merged and re.fullmatch(r"\[?\s*ص\s*:\s*\d+\s*\]?\s*:?", x["h"]): merged[-1]["p"] += x["p"]
        else: merged.append(x)
    secs = merged
    last = None                                      # babs inherit the kitab above them
    for x in secs:
        if x.get("parent"): last = x["parent"]
        elif last and x["lvl"] > 1: x["parent"] = last
    for x in secs:
        for k in ("h", "parent"):
            if k in x: x[k] = re.sub(r"^\[\s*(\d+\s*-\s*)?|\s*\]$", "", x[k]).strip()
    write(b, paginate(secs))

# 2. Books we have line by line, with English
Y = {n: json.load(open(f"app/data/year{n}.json")) for n in (1, 2)}
def from_lines(book, rows, per, head, skip=0):
    rows = rows[skip:]; secs = []
    for k in range(0, len(rows), per):
        ch = rows[k:k+per]
        secs.append({"h": f"{head} {k+1}–{k+len(ch)}", "lvl": 1, "v": [r["ar"] for r in ch], "p": [HAR.sub("", r["ar"]) for r in ch], "en": [r["en"] for r in ch]})
    write(book, secs, {"ai": False, "bilingual": True})
write_lines = [("tahawiyya_full", Y[1]["books"]["tahawiyya"], 10, "Points", 1), ("umm", Y[1]["books"]["umm"], 10, "Lines", 0),
               ("jawhara", Y[2]["books"]["jawhara"], 12, "Verses", 0)]
for book, rows, per, head, skip in write_lines: from_lines(book, rows, per, head, skip)
burda = Y[2]["decks"]["burda"]
verses = [{"ar": burda[i]["f"] + "  ...  " + burda[i+1]["f"], "en": burda[i]["b"] + " / " + burda[i+1]["b"]} for i in range(0, len(burda) - 1, 2)]
from_lines("burda", verses, 10, "Verses", 0)

# 3. Sahih al-Bukhari and Sahih Muslim, 10 hadith per section, by kitab
def hadith(src, book, label, per=10):
    rows = [r for r in json.load(open(f"json/{src}.json")) if r.get("Chapter") and r["Chapter"] != "Chapter_English" and r.get("Arabic", "").strip()]
    secs, chap, buf = [], None, []
    def flush():
        if not buf: return
        num = lambda x: str(int(float(x))) if str(x).replace(".", "").isdigit() else str(x)
        a, b = num(buf[0]["Hadithnumber"]), num(buf[-1]["Hadithnumber"])
        secs.append({"h": f"Hadith {a}–{b}" if a != b else f"Hadith {a}", "parent": chap, "lvl": 2,
                     "v": [r["Arabic"].strip() for r in buf], "p": [HAR.sub("", r["Arabic"].strip()) for r in buf],
                     "en": [f"{label} {num(r['Hadithnumber'])}. " + honor(fixjoin(r["English"].strip())) for r in buf]})
    for r in rows:
        if r["Chapter"] != chap or len(buf) == per: flush(); buf = []; chap = r["Chapter"]
        buf.append(r)
    flush(); write(book, secs, {"bilingual": True})
hadith("Hadith__Sahih_Bukhari", "bukhari", "Bukhari")
hadith("Hadith__Sahih_Muslim", "muslim", "Muslim")
