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

LOW = 0.5   # a string with fewer marks than this per letter is voweled again from scratch
def low(x):
    L = len(re.findall("[ء-ي]", x)); return L >= 2 and len(H.findall(x)) / L < LOW

def files():
    fs = [f for f in glob.glob(os.path.join(TEXTS, "**", "*.json"), recursive=True)
          if "/dict/" not in f and "wordaudio" not in f and "/audio" not in f and not f.endswith("index.json")]
    return sorted(f for f in fs if int(hashlib.md5(os.path.relpath(f, TEXTS).encode()).hexdigest(), 16) % SHARDS == SHARD)

def collect(x, out, path=()):
    """Every string in the file that is Arabic with too few harakat, with where it lives."""
    if isinstance(x, str):
        if low(x): out.append(path)
    elif isinstance(x, dict):
        for k, v in x.items(): collect(v, out, path + (k,))
    elif isinstance(x, list):
        for k, v in enumerate(x): collect(v, out, path + (k,))

def get(d, p):
    for k in p: d = d[k]
    return d
def put(d, p, v):
    for k in p[:-1]: d = d[k]
    d[p[-1]] = v

total = 0; t0 = time.time()
for f in files():
    try: d = json.load(open(f, encoding="utf-8"))
    except Exception: continue
    paths = []; collect(d, paths)
    if not paths: continue
    texts = [get(d, p) for p in paths]
    out = []
    for i in range(0, len(texts), 200): out += vowel_batch(texts[i:i+200])
    changed = 0
    for p, a, b in zip(paths, texts, out):
        if a != b: put(d, p, b); changed += 1
    if not changed: continue
    if isinstance(d, dict): d["ai_harakat"] = True
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    n = sum(len(x.split()) for x in texts); total += n
    print(f"{os.path.relpath(f, TEXTS)}: {changed} strings, {n} words, {time.time()-t0:.0f}s", flush=True)
print("done", total, "words")
