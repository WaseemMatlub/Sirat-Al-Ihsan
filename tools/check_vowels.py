"""Compare vowelled text against the source: same letters once harakat are removed (allowing small typo fixes)."""
import json, re, sys, difflib, importlib
H = re.compile(r"[ً-ْٰـ]")
N = lambda s: re.sub(r"\s+", " ", H.sub("", s).replace("أ","ا").replace("إ","ا").replace("آ","ا").replace("ٱ","ا").replace("ى","ي").replace("ئ","ي").replace("ؤ","و").replace("ء","").replace("ة","ه")).strip()
def check(src_json, mod, attr="A"):
    T = json.load(open(src_json)); A = getattr(importlib.import_module(mod), attr); bad = 0
    for i, rows in A.items():
        P = T["sections"][i]["p"]
        if len(rows) != len(P): print("COUNT", i, len(rows), len(P)); bad += 1; continue
        for j, (v, en) in enumerate(rows):
            r = difflib.SequenceMatcher(None, N(v), N(P[j])).ratio()
            if r < .97: print(f"[{i}.{j}] {r:.3f}\n  src: {P[j][:150]}\n  new: {H.sub('', v)[:150]}"); bad += 1
    print("checked", sum(len(r) for r in A.values()), "paragraphs,", bad, "to look at")
if __name__ == "__main__": sys.path.insert(0, "tools"); check(sys.argv[1], sys.argv[2])
