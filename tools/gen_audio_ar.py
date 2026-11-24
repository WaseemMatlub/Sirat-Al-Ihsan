"""Arabic narration with Piper (open-source, MIT) and its ar_JO 'kareem' voice.
Runs on GitHub Actions (.github/workflows/audio_ar.yml). Narrates the vowelled text (s.v) of books marked "narrate_ar": true.
Writes audio/ar/<book>/<section>_<para>.mp3 and records the paths in data/texts/<book>.json as "audio"."""
import glob, json, os, re, subprocess, sys, wave
from piper import PiperVoice

MODEL = os.environ.get("MODEL", "ar_JO-kareem-medium.onnx")
ONLY = os.environ.get("BOOK", "").strip()
voice = PiperVoice.load(MODEL)

def clean(t):
    t = re.sub(r"[«»{}\[\]()\"“”]", " ", t)
    t = t.replace("...", "، ").replace("…", "، ")
    return re.sub(r"\s{2,}", " ", t).strip()

def synth(text, mp3):
    wav = mp3[:-4] + ".wav"
    with wave.open(wav, "wb") as wf:
        if hasattr(voice, "synthesize_wav"): voice.synthesize_wav(text, wf)       # piper-tts >= 1.3
        else: voice.synthesize(text, wf)                                           # older versions
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-ac", "1", "-b:a", "48k", mp3], check=True); os.remove(wav)

made = 0
for path in sorted(glob.glob("data/texts/*.json")):
    book = os.path.basename(path)[:-5]
    d = json.load(open(path, encoding="utf-8"))
    if ONLY and book != ONLY: continue
    if not ONLY and not d.get("narrate_ar"): continue
    changed = False
    for i, s in enumerate(d["sections"]):
        src = s.get("v") or s.get("p")
        if not src: continue
        aud = s.get("audio") or [None] * len(src)
        for j, t in enumerate(src):
            out = f"audio/ar/{book}/{i}_{j}.mp3"
            if aud[j] == out and os.path.exists(out): continue
            os.makedirs(os.path.dirname(out), exist_ok=True)
            synth(clean(t), out); aud[j] = out; made += 1; changed = True
        s["audio"] = aud
    if changed:
        d["narrate_ar"] = True
        json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
        print(book, "narrated")
print("clips made:", made)
