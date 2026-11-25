"""Step-by-step guides (Hanafi), from Mukhtasar al-Quduri, Book of Hajj. Writes app/data/guides.json"""
import json, os
HJ = "Mukhtasar al-Quduri, Book of Hajj"
TALBIYAH = ("لَبَّيْكَ اللَّهُمَّ لَبَّيْكَ، لَبَّيْكَ لَا شَرِيكَ لَكَ لَبَّيْكَ، إِنَّ الْحَمْدَ وَالنِّعْمَةَ لَكَ وَالْمُلْكَ، لَا شَرِيكَ لَكَ",
            "Labbayk Allahumma labbayk, labbayk la sharika laka labbayk, inna al-hamda wa al-ni'mata laka wa al-mulk, la sharika lak.",
            "Here I am, O Allah, here I am. Here I am, You have no partner, here I am. All praise and blessings are Yours, and the dominion. You have no partner.")
def S(t, do, src, say=None, note=None): return {"t": t, "do": do, "src": src, **({"say": {"ar": say[0], "tr": say[1], "en": say[2]}} if say else {}), **({"note": note} if note else {})}

UMRAH = [
 S("Before the miqat", ["Cut nails and remove unwanted hair while you can.", "Make ghusl (wudu is allowed, ghusl is better).", "Men: put on two clean unstitched sheets, a lower (izar) and an upper (rida'). Women: normal modest clothes, face uncovered.", "Apply perfume to the body if you have it, before the intention.", "Pray two rak'ahs if it is not a disliked time."], HJ),
 S("Intention and talbiyah", ["Before passing the miqat, make the intention for 'umrah: 'O Allah, I intend 'umrah, make it easy for me and accept it from me.'", "Say the talbiyah. With it you are in ihram.", "Keep saying it often: after prayers, when going up or down, when meeting people."], HJ, TALBIYAH,
   "Men say it aloud; women quietly."),
 S("In ihram", ["Men: no stitched clothes, no covering the head or face.", "No perfume, no cutting hair or nails, no intimacy, no arguing, no hunting.", "Bathing, shade and a money belt are fine."], HJ),
 S("Entering al-Masjid al-Haram", ["Stop the talbiyah when you begin the tawaf.", "On seeing the Ka'bah say 'Allahu akbar' and 'La ilaha illa Allah', and make du'a."], "Mukhtasar al-Quduri, Book of Hajj; chapter on Tamattu'"),
 S("Tawaf: seven circuits", ["Men: uncover the right shoulder (idtiba').", "Start at the Black Stone: face it, say 'Bismillah, Allahu akbar', raise the hands and touch or kiss it if you can without pushing anyone; otherwise point to it.", "Walk round with the Ka'bah on your left, outside the Hatim.", "Men jog lightly (raml) in the first three circuits.", "Touch or point to the Stone each time you pass it, and end at it after the seventh circuit."], HJ),
 S("Two rak'ahs of tawaf", ["Cover the shoulder again.", "Pray two rak'ahs behind the Station of Ibrahim, or anywhere easy in the masjid.", "Drink Zamzam."], HJ),
 S("Sa'y: seven circuits", ["Go to al-Safa, face the Ka'bah, say takbir and tahlil, send blessings on the Prophet ﷺ and make du'a.", "Walk to al-Marwah. Men run between the two green markers.", "At al-Marwah do the same as at al-Safa. That is one circuit.", "Complete seven, ending at al-Marwah."], HJ),
 S("Shave or trim", ["Men: shaving the head is better; trimming is allowed.", "Women: trim a fingertip's length from the hair.", "Your 'umrah is complete and you leave ihram. Alhamdulillah."], "Mukhtasar al-Quduri, Book of Hajj; chapter on missing Hajj"),
]

HAJJ = [
 S("Choose your way", ["Most pilgrims from far away do tamattu': 'umrah first, then Hajj from Makkah. This guide follows tamattu'.", "Qiran (both together) is the best in the Hanafi school; ifrad is Hajj alone."], "Mukhtasar al-Quduri, chapters on Qiran and Tamattu'"),
 S("Do your 'umrah", ["Follow the 'Umrah guide: ihram at the miqat, tawaf, sa'y, then shave or trim.", "Stay in Makkah out of ihram until the 8th."], "Mukhtasar al-Quduri, chapter on Tamattu'"),
 S("8th Dhu al-Hijjah: ihram and Mina", ["Make ghusl, put on ihram in Makkah, make the intention for Hajj and say the talbiyah.", "Go to Mina and pray Zuhr, 'Asr, Maghrib, 'Isha' and the next Fajr there."], "Mukhtasar al-Quduri, chapter on Tamattu'; Book of Hajj", TALBIYAH),
 S("9th: the day of 'Arafah", ["After sunrise go to 'Arafah.", "Be within 'Arafah (not Batn 'Uranah) at some time between midday and dawn of the 10th: this is the pillar of Hajj.", "Spend the day in du'a, dhikr, talbiyah and tears. Ghusl beforehand is recommended."], HJ,
   note="Whoever misses the standing at 'Arafah has missed the Hajj."),
 S("Night of the 10th: Muzdalifah", ["After sunset leave calmly for Muzdalifah. Do not pray Maghrib on the way.", "At Muzdalifah pray Maghrib and 'Isha' together with one adhan and iqamah.", "Pick up pebbles for the stoning.", "Pray Fajr early, stand in du'a, then leave for Mina before sunrise."], HJ),
 S("10th: stoning, sacrifice, shaving", ["Stone Jamrat al-'Aqabah with seven pebbles, saying 'Allahu akbar' with each. Stop the talbiyah with the first pebble.", "Then the sacrifice (dam al-tamattu') — keep this order in tamattu'.", "Then shave or trim. Now all is lawful except intimacy."], HJ,
   note="Keep the order stoning, sacrifice, then shaving."),
 S("Tawaf al-Ziyarah", ["Go to Makkah on the 10th, 11th or 12th and perform tawaf al-ziyarah: seven circuits. This is the fard tawaf of Hajj.", "Then sa'y between al-Safa and al-Marwah (a mutamatti' has not yet done sa'y for Hajj).", "After this, intimacy also becomes lawful."], HJ,
   note="Delaying it past the 12th requires a sacrifice, according to Abu Hanifah."),
 S("11th and 12th: the three jamarat", ["Stay in Mina. After midday stone all three: first the small one (nearest Masjid al-Khayf), then the middle, then Jamrat al-'Aqabah, seven pebbles each.", "After the first and second, stand facing the qiblah and make du'a. Do not stand after the last.", "You may leave Mina on the 12th before sunset, or stay and stone on the 13th."], HJ),
 S("Farewell tawaf", ["Before leaving Makkah, perform tawaf al-wada': seven circuits without raml.", "It is wajib for those not from Makkah. A woman in her period after tawaf al-ziyarah is excused from it.", "May Allah accept your Hajj."], HJ),
]

GUIDES = [
 {"id": "umrah", "title": "How to perform 'Umrah", "sub": "Step by step, in the Hanafi school", "src": HJ, "steps": UMRAH},
 {"id": "hajj", "title": "How to perform Hajj (tamattu')", "sub": "From the 'umrah to the farewell tawaf", "src": HJ, "steps": HAJJ},
]
if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(GUIDES, open(os.path.join(here, "..", "app", "data", "guides.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print("guides", len(GUIDES), [len(g["steps"]) for g in GUIDES])
