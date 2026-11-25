"""Every flashcard set and lesson book in its own file, so the course plan (YEARS in app3.js) can move them between years freely.
data/decks/<id>.json : cards      data/lines/<id>.json : lesson lines"""
import json, os
D = "app/data"; os.makedirs(f"{D}/lines", exist_ok=True)
for n in range(1, 6):
    p = f"{D}/year{n}.json"
    if not os.path.exists(p): continue
    y = json.load(open(p))
    for k, v in y["decks"].items():
        if not os.path.exists(f"{D}/decks/{k}.json"): json.dump(v, open(f"{D}/decks/{k}.json", "w"), ensure_ascii=False, separators=(",", ":"))
    for k, v in y["books"].items(): json.dump(v, open(f"{D}/lines/{k}.json", "w"), ensure_ascii=False, separators=(",", ":"))
# Year 5: Tafsir al-Jalalayn, Juz' 'Amma only (surahs 78-114)
import re
j = json.load(open(f"{D}/decks/jalalayn.json"))
amma = [c for c in j if (m := re.search(r"\[(\d+):\d+\]", c["f"])) and int(m.group(1)) >= 78]
json.dump(amma, open(f"{D}/decks/jalalayn_amma.json", "w"), ensure_ascii=False, separators=(",", ":"))
# Year 3: the Forty Hadith as lessons, from the vowelled bilingual text
a = json.load(open(f"{D}/texts/arbain.json")); rows = []
for i, s in enumerate(a["sections"][1:], 1):
    for k, (v, e) in enumerate(zip(s.get("v") or s["p"], s.get("en") or [])):
        rows.append({"id": f"ar{i}_{k}", "ar": v, "en": e, "note": s.get("he") or s["h"]})
json.dump(rows, open(f"{D}/lines/arbain.json", "w"), ensure_ascii=False, separators=(",", ":"))
print("decks", len(os.listdir(f"{D}/decks")), "lines", sorted(f[:-5] for f in os.listdir(f"{D}/lines")), "amma", len(amma), "arbain rows", len(rows))
