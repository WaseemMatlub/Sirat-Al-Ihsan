"""Sayings of the Awliya' for the daily card: Arabic taken from our checked texts, English written carefully for the app."""
import json, re
H = "Imam Ibn 'Ata' Allah al-Iskandari رحمه الله"
HIKAM = {  # number in al-Hikam: English
 1: "One sign of relying on your own deeds is losing hope when you slip.",
 3: "Even the strongest resolve cannot break through the walls of destiny.",
 4: "Rest yourself from planning. What Another has taken care of for you, do not take on yourself.",
 5: "Striving for what is already guaranteed to you, while falling short in what is asked of you, is a sign that your inner sight has dimmed.",
 6: "Do not let a delay in the gift, despite your persistence in du'a, make you despair. He has guaranteed you an answer in what He chooses for you, not in what you choose for yourself, and at the time He wills, not the time you wish.",
 10: "Deeds are lifeless forms; their spirit is the secret of sincerity within them.",
 11: "Bury your existence in the earth of obscurity, for what sprouts from what was not buried does not flourish.",
 12: "Nothing benefits the heart like a retreat in which it enters the field of reflection.",
 22: "With every breath you take, a decree of His is being carried out in you.",
 25: "No request you seek through your Lord is held back, and no request you seek through yourself is made easy.",
 32: "Looking into the faults hidden within you is better than looking into the unseen that is veiled from you.",
 45: "No deed is small that comes from a heart free of the world, and no deed is great that comes from a heart greedy for it.",
 50: "No sin is small when His justice faces you, and no sin is great when His grace meets you.",
 58: "Do not rejoice in an act of obedience because it came from you. Rejoice in it because it came from Allah to you.",
 64: "Whoever is not grateful for blessings exposes them to loss. Whoever is grateful has tied them down with their cord.",
 86: "If you want honour that never perishes, do not seek honour in what perishes.",
 90: "It is reward enough for your obedience that He was pleased to make you worthy of it.",
 98: "He blessed you first by bringing you into being, and then by sending you provision without pause.",
 105: "Let the pain of trials be lightened by knowing that He is the One testing you. The One who faces you with these decrees is the One who has always chosen well for you.",
}
items = [q for s in json.load(open("app/data/texts/hikam.json"))["sections"] for q in s["v"]]
out = []
for n, en in HIKAM.items():
    ar = re.sub(r"^\d+\s*-\s*", "", items[n-1]).strip()
    assert items[n-1].startswith(f"{n} -"), n
    out.append({"ar": ar, "en": en, "by": H, "src": f"al-Hikam {n}"})
out += [
 {"ar": "وأوقاتك عمرك، وعمرك رأس مالك", "en": "Your moments are your life, and your life is your capital.", "by": "Imam Abu Hamid al-Ghazali رحمه الله", "src": "Bidayat al-Hidayah"},
 {"ar": "العلم بلا عمل جنون، والعمل بغير علم لا يكون", "en": "Knowledge without action is madness, and action without knowledge does not happen.", "by": "Imam Abu Hamid al-Ghazali رحمه الله", "src": "Ayyuha al-Walad"},
]
json.dump(__import__("harakat_cache").apply(out), open("app/data/quotes.json", "w"), ensure_ascii=False, separators=(",", ":")); print("quotes", len(out))
