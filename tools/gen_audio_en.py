"""Generate natural English narration for every book paragraph that has an English translation.
Runs on GitHub Actions (see .github/workflows/audio.yml). Uses Kokoro (open-source, Apache-2.0).
Writes audio/en/<book>/<section>_<para>.mp3 and records the paths in data/texts/<book>.json as "aud_en"."""
import glob, json, os, re, subprocess, sys
import numpy as np, soundfile as sf
from kokoro import KPipeline

VOICE = os.environ.get("VOICE", "bm_george")       # British male narrator
pipe = KPipeline(lang_code="b")                     # British English

HONORIFICS = [("ﷺ", ", peace and blessings be upon him,"), ("عليه السلام", ", peace be upon him,"), ("عليهم السلام", ", peace be upon them,"),
              ("عليها السلام", ", peace be upon her,"), ("رضي الله عنهما", ", may Allah be pleased with them,"), ("رضي الله عنهم", ", may Allah be pleased with them,"),
              ("رضي الله عنها", ", may Allah be pleased with her,"), ("رضي الله عنه", ", may Allah be pleased with him,"), ("رحمه الله", ", may Allah have mercy on him,")]
def speakable(t):
    for a, b in HONORIFICS: t = t.replace(a, b)
    t = re.sub(r"[؀-ۿﷰ-﷿⁨⁩]+", " ", t)    # any leftover Arabic script
    t = re.sub(r"\s+,", ",", re.sub(r",\s*,", ",", t))
    return re.sub(r"\s{2,}", " ", t).strip(" ,")

def synth(text, mp3):
    chunks = []
    for r in pipe(text, voice=VOICE, speed=1.0):
        a = r.audio if hasattr(r, "audio") else r[2]
        if a is None: continue
        chunks.append(a.detach().cpu().numpy() if hasattr(a, "detach") else np.asarray(a))
    if not chunks: return False
    wav = mp3[:-4] + ".wav"; sf.write(wav, np.concatenate(chunks), 24000)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-ac", "1", "-b:a", "48k", mp3], check=True); os.remove(wav)
    return True

made = 0
for path in sorted(glob.glob("data/texts/*.json")):
    d = json.load(open(path, encoding="utf-8")); book = os.path.basename(path)[:-5]; changed = False
    if not d.get("narrate"): continue          # only books marked for narration (keeps huge collections out)
    for i, s in enumerate(d["sections"]):
        if not s.get("en"): continue
        aud = s.get("aud_en") or [None] * len(s["en"])
        for j, t in enumerate(s["en"]):
            out = f"audio/en/{book}/{i}_{j}.mp3"
            if aud[j] == out and os.path.exists(out): continue
            text = speakable(t)
            if not text: continue
            os.makedirs(os.path.dirname(out), exist_ok=True)
            if synth(text, out): aud[j] = out; made += 1; changed = True
        s["aud_en"] = aud
    if changed:
        json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
        print(f"{book}: audio updated", flush=True)
print(f"made {made} clips")
