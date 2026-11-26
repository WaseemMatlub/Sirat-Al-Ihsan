"""Dala'il al-Khayrat of Imam Muhammad ibn Sulayman al-Jazuli (d. 870 AH). Arabic transcribed by reading each page of a
printed Indian-subcontinent edition (eight ahzab, beginning on Monday), page by page, and checked against the page images.
Only the Arabic text is taken. Writes app/data/dalail.json. Ahzab not yet transcribed are marked as coming."""
import json, os, glob, re
HERE = os.path.dirname(os.path.abspath(__file__)); TX = "/home/claude/dalail/tx"
AHZAB = [(1,"Monday",1,27),(2,"Tuesday",28,54),(3,"Wednesday",55,81),(4,"Thursday",82,109),(5,"Friday",110,142),(6,"Saturday",143,173),(7,"Sunday",174,201),(8,"Monday (second)",202,216)]
AR_NUM = ["الأول","الثاني","الثالث","الرابع","الخامس","السادس","السابع","الثامن"]
K = "\u0650"  # kasra
def standard(t):
    """Indo-Pak orthography -> standard (Arab-print) orthography. Letters and vowels are unchanged; only how they are written."""
    t = t.replace("اَللّٰهُمَّ", "اللَّهُمَّ").replace("لّٰه", "لَّه")
    t = t.replace("\u0627\u0670", "\u0622")                      # اٰ -> آ
    t = t.replace("لٰوة", "لَاة")                                   # salah written with alif
    t = re.sub("\u0670\u0649", "\u064e\u0649", t)                   # ـٰى -> ـَى (عَلٰى -> عَلَى)
    t = t.replace("\u0651\u0670\u0649", "\u0651\u064e\u0649")      # حَتّٰى -> حَتَّى
    t = t.replace("\u0651\u0670", "\u0651\u064e\u0627")            # الرّٰحِمِيْنَ -> الرَّاحِمِينَ, الصّٰلِحِيْنَ -> الصَّالِحِينَ
    t = t.replace("ه\u0656", "هِ").replace("ه\u0657", "هُ")          # هٖ هٗ
    t = re.sub(r"([\u064b-\u064d]) (\S)([\u064e-\u0650]?)\u0651", r"\1 \2\3", t)     # no shadda after tanween (idgham marking)
    t = re.sub(r"(\u0646\u0652) (\S)([\u064e-\u0650]?)\u0651", r"\1 \2\3", t)   # no shadda after nun sakinah (مِمَّنْ لَّزِمَ)
    t = re.sub("\u0650\u064a\u0652", "\u0650\u064a", t)             # ِيْ -> ِي
    t = re.sub("\u064f\u0648\u0652", "\u064f\u0648", t)             # ُوْ -> ُو
    # hamzat wasl after al- in verbal nouns of forms VII, VIII, X: الْاِسْتِ..., الْاِنْ.ِ, الْاِ.ْتِ
    t = re.sub("الْاِ(?=(سْتِ|نْ.\u0650|.ْتِ))", "الِا", t)
    t = re.sub("ا\u0650", "إ\u0650", t)                              # اِ -> إِ (remaining are hamzat qat')
    t = re.sub("ا\u064e", "أ\u064e", t).replace("ا\u064f", "أ\u064f").replace("ا\u0652", "أ\u0652")
    t = t.replace("الِإِ", "الِا")
    t = re.sub(r"الله(?=[\u064f\u0650\u064e])", "اللَّه", t)                                  # اللهُ -> اللَّهُ
    t = re.sub(r"([\u0650\u0651]{2})\u064a\u0652", "\\1\u064a", t)                         # ِّيْ -> ِّي
    t = re.sub(r"([\u064f\u0651]{2})\u0648\u0652", "\\1\u0648", t)                         # ُّوْ -> ُّو
    t = re.sub(r"([\u064b-\u064d][\u0627\u0649]?) (\S)([\u064e-\u0650]?)\u0651", r"\1 \2\3", t)   # no shadda after tanween + alif
    t = re.sub(r"(^| )وَ\u0651? (?=\S)", r"\1وَ", t)
    for k, v in (("ذٰلِ","ذَلِ"),("هٰذ","هَذ"),("هٰؤُ","هَؤُ"),("رَحْمٰن","رَحْمَن"),("إِلٰه","إِلَه"),("اِلٰه","إِلَه"),("لٰكِن","لَكِن"),("أُولٰئِ","أُولَئِ"),("اُولٰئِ","أُولَئِ")): t = t.replace(k, v)   # words written without alif in standard print
    t = re.sub("\u0670(?=[\u0621-\u064A])", "\u064e\u0627", t)          # mid-word dagger alif -> fatha + alif (إِبْرَاهِيمَ, الْعَالَمِينَ)
    t = t.replace("يَا\u064eأَ", "يَا أَ").replace("ي\u064e\u0627أَ", "يَا أَ")
    t = re.sub("\u0670$|\u0670(?= )", "\u064e\u0627", t)
    t = t.replace("\u0656", "\u0650").replace("\u0657", "\u064f")                                          # rejoin a و split at a page end
    return t
def pages(a, b):
    out = []
    for p in range(a, b + 1):
        f = f"{TX}/{p:03d}.txt"
        if not os.path.exists(f): return None
        out.append(open(f).read().strip())
    return out
out = {"title": "Dala'il al-Khayrat", "ar": "دلائل الخيرات", "by": "Imam Muhammad ibn Sulayman al-Jazuli رحمه الله (d. 870 AH)",
       "note": "The Arabic is typed letter by letter from two printed editions and checked against the page images: the eight parts and the closing du'a from an Indo-Pak Arabic-Urdu edition, and the opening sections from the Arabic-English edition (Lahore, 2010). The English is our own translation from the Arabic, made for this app.",
       "ahzab": []}
for n, day, a, b in AHZAB:
    ps = pages(a, b); h = {"n": n, "day": day, "ar": "الحزب " + AR_NUM[n-1], "pages": f"{a}–{b}"}
    if ps:
        lines = [l for l in "\n".join(ps).split("\n") if not l.startswith("## ")]
        text = " ".join(lines)
        text = re.sub(r"\s+", " ", text)
        parts = [standard(p.strip()) for p in text.split("۝") if p.strip()]
        h["paras"] = parts
    out["ahzab"].append(h)
ps = pages(217, 223)
if ps:
    text = re.sub(r"\s+", " ", " ".join(l for l in "\n".join(ps).split("\n") if not l.startswith("## ")))
    out["extra"] = {"khatm": {"paras": [standard(p.strip()) for p in text.split("۝") if p.strip()], "pages": "217–223"}}
from dalail_front import FRONT
for k, v in FRONT.items():
    out["extra"][k] = {"title": v["title"], "about": v["about"], "pages": v["pages"], "paras": [x["ar"] for x in v["items"]], "en": [x["en"] for x in v["items"]], "times": [x.get("n", 0) for x in v["items"]]}
try:
    from dalail_en import EN
    for k, v in EN.items():
        tgt = out["extra"]["khatm"] if k == "khatm" else next(h for h in out["ahzab"] if h["n"] == k)
        if len(v) == len(tgt["paras"]): tgt["en"] = v
        else: print("EN count mismatch", k, len(v), len(tgt["paras"]))
except ImportError: pass
json.dump(out, open(os.path.join(HERE, "..", "app", "data", "dalail.json"), "w"), ensure_ascii=False, separators=(",", ":"))
print([(h["n"], len(h.get("paras", []))) for h in out["ahzab"]])
