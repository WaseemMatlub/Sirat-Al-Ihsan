"""Add harakat to the library texts that have none, using the CATT model (Character-based Arabic Tashkeel Transformer,
Abjad AI, Apache-2.0). Every word is checked: the model may only add marks, never change letters; if it does, the original
word is kept. Books processed are marked "ai": true, so the app shows that the harakat await a teacher's check.
Usage: python harakat.py TEXTS_DIR SHARD SHARDS [CATT_DIR]"""
import sys, os, re, json, glob, hashlib, time
TEXTS, SHARD, SHARDS = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
CATT = sys.argv[4] if len(sys.argv) > 4 else "/home/claude/abjadai/catt"
sys.path.insert(0, CATT)
import torch
from eo_pl import TashkeelModel
from tashkeel_tokenizer import TashkeelTokenizer
torch.set_num_threads(os.cpu_count() or 2)
tok = TashkeelTokenizer()
model = TashkeelModel(tok, max_seq_len=1024, n_layers=6, learnable_pos_emb=False)
model.load_state_dict(torch.load(os.path.join(CATT, "models/best_eo_mlm_ns_epoch_193.pt"), map_location="cpu")); model.eval()

H = re.compile("[ً-ْٰ]")
AR = re.compile("[ء-يٱ]+[ء-يٱً-ْٰ]*")
def bare(w): return H.sub("", w)
def needs(paras):
    t = " ".join(paras[:30]); L = len(re.findall("[ء-ي]", t))
    return L > 0 and len(H.findall(t)) / L < 0.25

def vowel_batch(paras):
    """Return the paragraphs with harakat added to every Arabic word."""
    jobs, slots = [], []          # each job: a chunk of bare Arabic words; slots: (para, [match spans])
    for pi, p in enumerate(paras):
        ms = list(AR.finditer(p)); words = [bare(m.group()) for m in ms]
        chunk, start = [], 0
        for k, w in enumerate(words):
            if chunk and len(" ".join(chunk)) + len(w) > 400:
                jobs.append(" ".join(chunk)); slots.append((pi, ms[start:k])); chunk, start = [], k
            chunk.append(w)
        if chunk: jobs.append(" ".join(chunk)); slots.append((pi, ms[start:]))
    outs = model.do_tashkeel_batch(jobs, 32, False) if jobs else []
    res = list(paras); edits = {i: [] for i in range(len(paras))}
    for (pi, ms), src, out in zip(slots, jobs, outs):
        ow = out.split()
        if len(ow) != len(ms):
            continue
        for m, w in zip(ms, ow):
            if bare(w) == bare(m.group()): edits[pi].append((m.start(), m.end(), w))
    for pi, ed in edits.items():
        p = paras[pi]
        for s, e, w in sorted(ed, reverse=True): p = p[:s] + w + p[e:]
        res[pi] = p
    return res

def files():
    fs = [f for f in glob.glob(os.path.join(TEXTS, "*.json")) + glob.glob(os.path.join(TEXTS, "*", "*.json")) if not f.endswith("index.json")]
    return sorted(f for f in fs if int(hashlib.md5(os.path.relpath(f, TEXTS).encode()).hexdigest(), 16) % SHARDS == SHARD)

t0 = time.time(); nw = 0
for f in files():
    try: d = json.load(open(f))
    except Exception: continue
    secs = d.get("sections") if isinstance(d, dict) else None
    if not secs or d.get("ai_harakat"): continue
    if any("v" in s for s in secs) or not needs([x for s in secs[:20] for x in s.get("p", [])]): continue
    for s in secs:
        if s.get("p"): s["p"] = vowel_batch(s["p"]); nw += sum(len(x.split()) for x in s["p"])
        if s.get("h") and not re.search("[a-zA-Z]", s["h"]): s["h"] = vowel_batch([s["h"]])[0]
    d["ai_harakat"] = True
    json.dump(d, open(f, "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"{os.path.relpath(f, TEXTS)}: {nw} words, {time.time()-t0:.0f}s", flush=True)
print("done", nw, "words", f"{time.time()-t0:.0f}s")
