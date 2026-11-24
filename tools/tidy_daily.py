"""Tidy the English of the hadith of the day: explain untranslated words once, use ʿ for the letter ʿayn,
and drop the transliterated chapter names in brackets."""
import json, re
GLOSS = {"Badana":"sacrificial camel", "Sadaqa":"charity", "Umra":"lesser pilgrimage", "Ruqya":"healing recitation", "Khutba":"sermon",
  "Musalla":"place of prayer", "Jumua":"Friday prayer", "Tiyara":"taking bad omens", "Araya":"selling fresh dates on the palm for dried ones",
  "Ghazwat":"expedition of", "Kuniya":"honorific name", "Haya":"modesty", "Tashahhud":"the testimony said in prayer", "Ihram":"the pilgrim's state",
  "Tawaf":"circling the Kaʿba", "Iqama":"the second call to prayer", "Witr":"the odd-numbered night prayer", "Hadi":"sacrificial animal",
  "Ansar":"the Helpers of Medina", "Muhajirin":"the Emigrants", "Zuhr":"midday prayer", "Asr":"afternoon prayer", "Isha":"night prayer", "Fajr":"dawn prayer", "Maghrib":"sunset prayer"}
for m in range(12):
    p = f"app/data/daily/{m}.json"; H = json.load(open(p, encoding="utf-8"))
    for h in H:
        e = h["e"].replace("`", "ʿ")
        for w, g in GLOSS.items():
            if f"({g})" in e: continue
            e = re.sub(rf"\b({w}[sh]?)\b(?!\s*\()", rf"\1 ({g})", e, count=1)
        h["e"] = re.sub(r"\s+", " ", e).strip()
        h["c"] = re.sub(r"\s*\([^)]*\)\s*$", "", h["c"].replace("`", "ʿ"))
    json.dump(H, open(p, "w", encoding="utf-8"), ensure_ascii=False)
print("tidied")
