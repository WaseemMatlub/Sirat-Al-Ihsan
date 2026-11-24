"""Convert OpenITI mARkdown texts into chaptered JSON for the Ihsan reader.
Usage: python3 oiti_parse.py <raw.txt> <out.json> <id> <title>"""
import json, re, sys

def parse(raw):
    body = raw.split("#META#Header#End#", 1)[-1]
    body = re.sub(r"[ \t]*PageV\d+P\d+[ \t]*", " ", body)      # page markers (keep line breaks)
    body = re.sub(r"[ \t]*\bms\d+\b[ \t]*", " ", body)           # milestone markers
    body = re.sub(r"\n[ \t]*~~", " ", body)                      # continuation lines
    body = re.sub(r"\s*@QB@\s*", " ﴿", body); body = re.sub(r"\s*@QE@\s*", "﴾ ", body)   # Qur'an quotation markers
    secs, cur = [], None
    def new(h, lvl):
        nonlocal cur
        cur = {"h": h, "lvl": lvl, "p": []}; secs.append(cur)
    for line in body.split("\n"):
        line = line.rstrip()
        m = re.match(r"^#{1,3} (\|+)\s*(.*)$", line)           # '### | Kitab', '### || Bab', JK style '# | ...'
        if m:
            h = re.sub(r"^AUTO\s*", "", m.group(2)).strip()
            h = re.sub(r"^\d+\s*-\s*", "", h).strip(" .:")
            h = re.sub(r"^[-*\s]+", "", h)                          # edition bullets "- *"
            h = re.sub(r"^\(\s*\d+\s*\)\s*", "", h)                 # "( 12 )" bab numbers
            h = re.sub(r"\[?\s*وفيه\s*\(?\s*\d+\s*\)?\s*(حديثا|حديث|أحاديث|احاديث)?\s*\]?", "", h)  # "[ وفيه 15 حديثا ]"
            h = re.sub(r"\(\s*\d+\s*\)", "", h)                       # footnote markers
            h = re.sub(r"\s{2,}", " ", h).strip(" .:-*")
            if h: new(h, len(m.group(1)))
            continue
        m = re.match(r"^# (.*)$", line)
        if m:
            t = re.sub(r"\s{2,}", " ", m.group(1)).strip()
            if not t or t in ("...", "…") or re.fullmatch(r"[-*\s]+", t): continue
            if cur is None: new("مقدمة", 1)
            cur["p"].append(t)
    # headings that are only hadith numbers ("1/1-") belong inside the previous bab
    merged = []
    for s in secs:
        if merged and not re.search(r"[\u0621-\u064A]", s["h"]):
            merged[-1]["p"].extend((f"{s['h'].strip(' -')} " + p) if i == 0 else p for i, p in enumerate(s["p"]))
        else: merged.append(s)
    secs = merged
    # merge empty headings into the next section's title path
    out, pending = [], []
    for s in secs:
        if not s["p"]: pending.append(s); continue
        if pending:
            top = [p for p in pending if p["lvl"] < s["lvl"]]
            if top: s["parent"] = top[-1]["h"]
            pending = []
        out.append(s)
    # carry kitab title down to its babs
    parent = None
    for s in out:
        if s["lvl"] == 1: parent = s["h"]
        elif parent and "parent" not in s: s["parent"] = parent
    return out

if __name__ == "__main__":
    raw, dst, bid, title = sys.argv[1:5]
    secs = parse(open(raw, encoding="utf-8").read())
    json.dump({"id": bid, "title": title, "sections": secs}, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    n = sum(len(s["p"]) for s in secs)
    print(f"{bid}: {len(secs)} sections, {n} paragraphs, {sum(len(p) for s in secs for p in s['p'])//1000}k chars")
