import json, os
OUT = "app/data/texts"
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

