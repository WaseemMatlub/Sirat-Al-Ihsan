"""Audio for single words in word lessons (Qur'an words and verbs), with the free Piper voice.
Writes audio/words/<card id>.mp3 and data/wordaudio.json (the ids that have audio)."""
import json, os, re, subprocess, wave
from piper import PiperVoice
voice = PiperVoice.load(os.environ.get("MODEL", "ar_JO-kareem-medium.onnx"))
DECKS = {1: ["quran"], 2: ["verbs1"], 3: ["verbs2"]}
have = set(json.load(open("data/wordaudio.json"))) if os.path.exists("data/wordaudio.json") else set()
os.makedirs("audio/words", exist_ok=True); made = 0
for y, decks in DECKS.items():
    d = json.load(open(f"data/year{y}.json", encoding="utf-8"))
    for dk in decks:
        for c in d["decks"].get(dk, []):
            w = c["f"].strip(); out = f"audio/words/{c['id']}.mp3"
            if c["id"] in have and os.path.exists(out): continue
            if len(re.sub(r"[^ء-ي]", "", w)) < 2: continue          # single letters (و، ل، ب) are not read on their own
            wav = out[:-4] + ".wav"
            with wave.open(wav, "wb") as wf:
                (voice.synthesize_wav if hasattr(voice, "synthesize_wav") else voice.synthesize)(w, wf)
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-ac", "1", "-b:a", "40k", out], check=True); os.remove(wav)
            have.add(c["id"]); made += 1
json.dump(sorted(have), open("data/wordaudio.json", "w"))
print("word clips made:", made, "total:", len(have))
