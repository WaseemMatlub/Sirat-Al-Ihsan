"""The five Ihya us-Sunnah editions (used with permission): vowelled, so each paragraph is kept with harakat (v)
and without (p) for the Harakat on/off switch."""
import json, re, sys
sys.path.insert(0, "tools")

def parse(raw):                                        # headings "### |" (level by bars); paragraphs are blocks split by blank lines
    body = raw.split("#META#Header#End#", 1)[-1]
    body = re.sub(r"[ \t]*PageV\d+P\d+[ \t]*\n?", "", body)
    secs, cur = [], None
    for block in re.split(r"\n\s*\n", body):
        lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
        for l in lines:
            m = re.match(r"^#{1,3} (\|+)\s*(.*)$", l)
            if m: cur = {"h": m.group(2).strip(), "lvl": len(m.group(1)), "p": []}; secs.append(cur); continue
            if cur is None: cur = {"h": "مقدمة", "lvl": 1, "p": []}; secs.append(cur)
            if cur.get("_open"): cur["p"][-1] += " " + l
            else: cur["p"].append(l); cur["_open"] = True
        if cur: cur["_open"] = False
    for x in secs: x.pop("_open", None)
    return secs
from build_lib_common import write, paginate
HAR = re.compile(r"[ً-ْٰ]")
BOOKS = {"hikam":"al-hikam", "nahwmir":"nahw-mir", "miatamil":"sharh-miat-amil", "hidayatnahw":"hidayat-al-nahw", "azhari":"sharh-khalid-al-azhari-ala-al-ajurrumiyya"}
for b, f in BOOKS.items():
    secs = parse(open(f"sources/ihya/{f}.txt", encoding="utf-8").read())
    for x in secs:
        x["h"] = re.sub(r"^\[\s*|\s*\]$", "", x["h"]).strip()
        x["p"] = [q.strip() for q in x["p"] if q.strip()]
    secs = [x for x in secs if x["p"]]
    if b == "hikam":                                    # the aphorisms 20 to a page; the letters and the munajat as they are
        items = [q for q in secs[0]["p"] if q != "بسم الله الرحمن الرحيم"]
        secs = [{"h": f"الحكم {k+1} إلى {min(k+20,len(items))}", "lvl": 1, "parent": "الحكم العطائية", "p": items[k:k+20]} for k in range(0, len(items), 20)] + secs[1:]
        last = None
        for x in secs:
            if x["lvl"] == 1 and not x.get("parent"): last = x["h"]
            elif x["lvl"] > 1: x["parent"] = "المكاتبات"
    secs = paginate(secs)
    for x in secs: x["v"] = x["p"]; x["p"] = [HAR.sub("", q) for q in x["p"]]
    write(b, secs, {"src": "Ihya us Sunnah edition", "narrate_ar": True})
