"""Step-by-step guides (Hanafi): wudu, ghusl, salah, 'umrah and Hajj.
Rulings from Mukhtasar al-Quduri and Nur al-Idah (al-Shurunbulali); du'as from the hadith collections, with sources.
Qur'an text is taken verbatim from Tanzil (tanzil.net, CC BY 3.0). Writes app/data/guides.json"""
import json, os
Q = json.load(open("/home/claude/ext/quran-json/data/tanzil/simple.json"))
def V(s, a): return next(v["text"] for v in Q[str(s)] if v["verse"] == a)

QD = "Mukhtasar al-Quduri"; NI = "Nur al-Idah"
HJ = f"{QD}, Book of Hajj"

def say(label, ar, tr, en, src): return {"label": label, "ar": ar, "tr": tr, "en": en, "src": src}
def S(t, do, src, rule=None, says=(), note=None, more=None):
    d = {"t": t, "do": do, "src": src}
    if rule: d["rule"] = rule
    if says: d["says"] = list(says)
    if note: d["note"] = note
    if more: d["more"] = more
    return d

# ------------------------------------------------------------------ shared recitations
TALBIYAH = say("The talbiyah", "لَبَّيْكَ اللَّهُمَّ لَبَّيْكَ، لَبَّيْكَ لَا شَرِيكَ لَكَ لَبَّيْكَ، إِنَّ الْحَمْدَ وَالنِّعْمَةَ لَكَ وَالْمُلْكَ، لَا شَرِيكَ لَكَ",
    "Labbayk Allahumma labbayk, labbayk la sharika laka labbayk, inna al-hamda wa al-ni'mata laka wa al-mulk, la sharika lak.",
    "Here I am, O Allah, here I am. Here I am, You have no partner, here I am. All praise and blessings are Yours, and the dominion. You have no partner.",
    f"Sahih al-Bukhari (1549) and Muslim (1184); {HJ}")
MASJID_IN = say("Entering the masjid (right foot first)", "بِسْمِ اللَّهِ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى رَسُولِ اللَّهِ، اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ",
    "Bismillah, wa al-salatu wa al-salamu 'ala rasulillah. Allahumma iftah li abwaba rahmatik.",
    "In the name of Allah, and blessings and peace on the Messenger of Allah. O Allah, open for me the doors of Your mercy.",
    "Sahih Muslim (713); the salam on the Prophet ﷺ in Abu Dawud (465); al-Nawawi, al-Adhkar")
ISTILAM = say("At the Black Stone, raising the hands", "بِسْمِ اللَّهِ، وَاللَّهُ أَكْبَرُ", "Bismillah, wallahu akbar.", "In the name of Allah, and Allah is the Greatest.",
    f"Takbir at the Stone: Sahih al-Bukhari (1613); raising the hands: {NI}, when to raise the hands")
YAMANI = say("Between the Yemeni corner and the Black Stone", V(2, 201).split("يَقُولُ ")[1],
    "Rabbana atina fi al-dunya hasanatan wa fi al-akhirati hasanatan wa qina 'adhab al-nar.",
    "Our Lord, give us good in this world and good in the Hereafter, and protect us from the punishment of the Fire.",
    "Qur'an 2:201; Sunan Abi Dawud (1892), from 'Abdullah ibn al-Sa'ib رضي الله عنه")
MAQAM = say("Walking to the Station of Ibrahim", "وَاتَّخِذُوا مِن مَّقَامِ إِبْرَاهِيمَ مُصَلًّى", "Wattakhidhu min maqami Ibrahima musalla.",
    "And take the Station of Ibrahim as a place of prayer.", "Qur'an 2:125; Sahih Muslim (1218), the hadith of Jabir رضي الله عنه")
SAFA_AYAH = say("Climbing al-Safa (the first time)", "إِنَّ الصَّفَا وَالْمَرْوَةَ مِن شَعَائِرِ اللَّهِ — أَبْدَأُ بِمَا بَدَأَ اللَّهُ بِهِ",
    "Inna al-Safa wa al-Marwata min sha'a'irillah. Abda'u bima bada'a Allahu bih.",
    "Al-Safa and al-Marwah are among the signs of Allah. I begin with what Allah began with.",
    "Qur'an 2:158; Sahih Muslim (1218), the hadith of Jabir رضي الله عنه")
SAFA_DHIKR = say("On al-Safa and al-Marwah, facing the Ka'bah (three times, with du'a in between)",
    "اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ، اللَّهُ أَكْبَرُ، لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ، وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ، لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ، أَنْجَزَ وَعْدَهُ، وَنَصَرَ عَبْدَهُ، وَهَزَمَ الْأَحْزَابَ وَحْدَهُ",
    "Allahu akbar (3). La ilaha illa Allahu wahdahu la sharika lah, lahu al-mulku wa lahu al-hamd, wa huwa 'ala kulli shay'in qadir. La ilaha illa Allahu wahdah, anjaza wa'dah, wa nasara 'abdah, wa hazama al-ahzaba wahdah.",
    "Allah is the Greatest (3). There is no god but Allah alone, with no partner; His is the dominion and His the praise, and He has power over all things. There is no god but Allah alone; He fulfilled His promise, helped His servant, and alone defeated the confederates.",
    "Sahih Muslim (1218), the hadith of Jabir رضي الله عنه")
GREEN = say("Between the green markers (men walk briskly)", "رَبِّ اغْفِرْ وَارْحَمْ، إِنَّكَ أَنْتَ الْأَعَزُّ الْأَكْرَمُ",
    "Rabbi ighfir warham, innaka anta al-a'azzu al-akram.", "My Lord, forgive and have mercy; You are the Most Mighty, the Most Generous.",
    "Reported from Ibn Mas'ud and Ibn 'Umar رضي الله عنهم in their sa'y (Musannaf Ibn Abi Shaybah)")
ZAMZAM = say("Drinking Zamzam", "بِسْمِ اللَّهِ", "Bismillah.", "Drink facing the qiblah, in three breaths, and ask Allah for what you need: the Prophet ﷺ said, 'The water of Zamzam is for whatever it is drunk for.'",
    "Sunan Ibn Majah (3062), from Jabir رضي الله عنه")
ARAFAH = say("The best du'a of 'Arafah", "لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ، وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ",
    "La ilaha illa Allahu wahdahu la sharika lah, lahu al-mulku wa lahu al-hamd, wa huwa 'ala kulli shay'in qadir.",
    "There is no god but Allah alone, with no partner; His is the dominion and His the praise, and He has power over all things.",
    "Jami' al-Tirmidhi (3585): 'The best du'a is the du'a of the day of 'Arafah, and the best that I and the prophets before me have said is…'")
RAMI = say("With each pebble", "بِسْمِ اللَّهِ، اللَّهُ أَكْبَرُ", "Bismillah, Allahu akbar.", "In the name of Allah. Allah is the Greatest.",
    f"Takbir with every pebble: Sahih Muslim (1218), the hadith of Jabir رضي الله عنه; {HJ}")
INTENT_UMRAH = say("Intention for 'umrah", "اللَّهُمَّ إِنِّي أُرِيدُ الْعُمْرَةَ فَيَسِّرْهَا لِي وَتَقَبَّلْهَا مِنِّي",
    "Allahumma inni uridu al-'umrata fa-yassirha li wa taqabbalha minni.", "O Allah, I intend 'umrah, so make it easy for me and accept it from me.",
    f"{HJ} (the same wording it gives for Hajj, said for 'umrah)")
INTENT_HAJJ = say("Intention for Hajj", "اللَّهُمَّ إِنِّي أُرِيدُ الْحَجَّ فَيَسِّرْهُ لِي وَتَقَبَّلْهُ مِنِّي",
    "Allahumma inni uridu al-hajja fa-yassirhu li wa taqabbalhu minni.", "O Allah, I intend Hajj, so make it easy for me and accept it from me.", HJ)

# ------------------------------------------------------------------ 'Umrah
UMRAH = [
 S("Before the miqat", ["Cut your nails and remove unwanted hair.", "Make ghusl (wudu is enough, ghusl is better).",
   "Men: put on two clean, unstitched white sheets, one round the waist (izar) and one over the shoulders (rida'). Women: ordinary modest clothes; the face stays uncovered.",
   "Put perfume on the body (not the ihram sheets) before the intention.", "Pray two rak'ahs, if it is not a disliked time."], HJ, "Sunnah",
   more="The miqat is the boundary where ihram begins. Coming from the UK by air you usually pass it in the plane, so many people put on ihram at home or at the airport and make the intention just before the miqat."),
 S("Intention and talbiyah", ["Just before the miqat, make the intention.", "Then say the talbiyah. With the intention and the talbiyah together you are in ihram.",
   "Keep saying the talbiyah often: after prayers, going up or down, meeting people, waking."], HJ, "Condition (shart)",
   says=[INTENT_UMRAH, TALBIYAH], note="Men say the talbiyah aloud; women quietly."),
 S("While in ihram", ["Men: no stitched clothing, and do not cover the head or face.", "Everyone: no perfume, no cutting hair or nails, no intimacy, no arguing or bad speech, no hunting.",
   "Bathing, an umbrella or shade, a belt for money and a watch are all fine."], HJ, "Wajib to avoid",
   note="Breaking a rule of ihram brings a penalty (a sacrifice or charity). Ask a scholar if this happens."),
 S("Entering al-Masjid al-Haram", ["Enter with the right foot.", "When you first see the Ka'bah, raise your hands, say 'Allahu akbar' and 'La ilaha illa Allah', and make du'a: it is a time when du'a is answered.",
   "Go straight to the Black Stone to begin the tawaf."], f"{HJ}; {NI}, when to raise the hands", "Sunnah", says=[MASJID_IN]),
 S("Tawaf: seven circuits round the Ka'bah", ["Have wudu. Men uncover the right shoulder (idtiba').", "Stand facing the Black Stone, make the intention for tawaf, raise your hands to your ears and say the takbir.",
   "Kiss or touch the Stone if you can without pushing anyone; otherwise point to it with your palms and kiss them.",
   "Walk round with the Ka'bah on your left, outside the semicircular wall (Hatim).", "Men walk briskly with short steps (raml) in the first three circuits only.",
   "Each time you pass the Stone, point to it and say 'Bismillah, Allahu akbar'. After the seventh circuit you finish at the Stone."], HJ, "Pillar (rukn) of 'umrah",
   says=[ISTILAM, YAMANI], note="There is no fixed du'a for each circuit. Make du'a, dhikr and send salawat in your own words, in any language.",
   more="If the prayer is called during tawaf, pray with the congregation and continue from where you stopped. If you lose count, go by what you are sure of (the lower number)."),
 S("Two rak'ahs after tawaf", ["Cover the right shoulder again.", "Pray two rak'ahs behind the Station of Ibrahim if you can, otherwise anywhere in the masjid.",
   "The Prophet ﷺ recited al-Kafirun in the first and al-Ikhlas in the second.", "Then drink Zamzam."], f"{HJ}; Sahih Muslim (1218)", "Wajib",
   says=[MAQAM, ZAMZAM]),
 S("Sa'y: seven lengths between al-Safa and al-Marwah", ["Go to al-Safa. Climb it until you can see the Ka'bah, face it, raise your hands and say the takbir and tahlil, send salawat on the Prophet ﷺ and make du'a.",
   "Walk towards al-Marwah. Men walk briskly between the green lights.", "At al-Marwah do the same as at al-Safa. That is one length.",
   "Al-Marwah back to al-Safa is the second. Finish the seventh at al-Marwah."], HJ, "Wajib",
   says=[SAFA_AYAH, SAFA_DHIKR, GREEN], note="Wudu is not a condition for sa'y, but it is better to have it."),
 S("Shave or trim", ["Men: shaving the whole head is better; trimming at least a fingertip's length from a quarter of the head is allowed.", "Women: trim a fingertip's length from the ends of the hair.",
   "Your 'umrah is complete and you leave ihram. Alhamdulillah."], HJ, "Wajib",
   note="The Prophet ﷺ made du'a three times for those who shave and once for those who trim (Sahih al-Bukhari 1728)."),
]

# ------------------------------------------------------------------ Hajj (tamattu')
HAJJ = [
 S("Know the three ways", ["Tamattu': 'umrah in the months of Hajj, leave ihram, then Hajj from Makkah. Most pilgrims from far away do this, and this guide follows it.",
   "Qiran: 'umrah and Hajj in one ihram. The best in the Hanafi school.", "Ifrad: Hajj alone."], f"{QD}, chapters on Qiran and Tamattu'",
   note="The pillars of Hajj are ihram, standing at 'Arafah and tawaf al-ziyarah. Missing the standing at 'Arafah means missing the Hajj."),
 S("Your 'umrah", ["Perform 'umrah as in the 'Umrah guide: ihram at the miqat, tawaf, sa'y, then shave or trim.", "Stay in Makkah out of ihram until the 8th of Dhu al-Hijjah."], f"{QD}, chapter on Tamattu'", "Part of tamattu'"),
 S("8th Dhu al-Hijjah: ihram again, then Mina", ["Make ghusl and put on ihram in Makkah. Make the intention for Hajj and say the talbiyah.", "Go to Mina and pray Zuhr, 'Asr, Maghrib, 'Isha' and the next Fajr there, each in its time."],
   f"{QD}, chapter on Tamattu'; {HJ}", "Pillar: the ihram", says=[INTENT_HAJJ, TALBIYAH]),
 S("9th: the day of 'Arafah", ["After sunrise go to 'Arafah, saying the talbiyah.", "Pray Zuhr and 'Asr. (In the Hanafi school they are joined only behind the imam of the masjid there; otherwise pray each in its time.)",
   "Be anywhere within 'Arafah, except the valley of 'Uranah, at any moment from midday until dawn of the 10th: this is the pillar of Hajj.",
   "Spend the afternoon facing the qiblah with raised hands, in du'a, dhikr, talbiyah, salawat and tears, until sunset."], HJ, "Pillar (rukn)",
   says=[ARAFAH, TALBIYAH], note="Whoever misses the standing at 'Arafah has missed the Hajj. Do not leave before sunset."),
 S("Night of the 10th: Muzdalifah", ["After sunset leave calmly for Muzdalifah. Do not pray Maghrib on the way.", "At Muzdalifah pray Maghrib and 'Isha' together in the time of 'Isha', with one adhan and one iqamah.",
   "Spend the night there. Pick up 49 or 70 small pebbles, the size of a chickpea.", "Pray Fajr early, then stand at the Mash'ar al-Haram (or anywhere in Muzdalifah) in du'a and dhikr until it is light, and leave for Mina before sunrise."],
   HJ, "Wajib (the standing after Fajr)", says=[say("Remembering Allah at Muzdalifah", "فَاذْكُرُوا اللَّهَ عِندَ الْمَشْعَرِ الْحَرَامِ", "Fadhkuru Allaha 'inda al-mash'ari al-haram.",
     "Remember Allah at the Sacred Monument.", "Qur'an 2:198")] + [TALBIYAH]),
 S("10th: stoning, sacrifice, shaving", ["At Jamrat al-'Aqabah (the large pillar) throw seven pebbles, one at a time, saying the takbir with each. Stop the talbiyah with the first pebble.",
   "Then offer the sacrifice of tamattu' (or have it done through an agent).", "Then shave or trim. Now everything is lawful again except intimacy."], HJ, "Wajib",
   says=[RAMI], note="In tamattu' and qiran keep this order: stoning, then sacrifice, then shaving. Changing it requires a penalty sacrifice according to Abu Hanifah."),
 S("Tawaf al-ziyarah and sa'y", ["Go to Makkah on the 10th, 11th or 12th and perform tawaf al-ziyarah: seven circuits. This is the fard tawaf of Hajj.",
   "Pray two rak'ahs and drink Zamzam, then do the sa'y between al-Safa and al-Marwah for your Hajj.", "After this, intimacy is lawful as well."], HJ, "Pillar (rukn)",
   says=[ISTILAM, YAMANI, SAFA_DHIKR], note="Delaying it past the 12th requires a sacrifice, according to Abu Hanifah. A woman in her period waits until she is pure."),
 S("11th, 12th (and 13th): the three jamarat", ["Stay the nights in Mina. Each day after midday stone all three, seven pebbles each: first the small one (near Masjid al-Khayf), then the middle one, then Jamrat al-'Aqabah.",
   "After the first and the second, move aside, face the qiblah, raise your hands and make a long du'a. Do not stop after the last one.",
   "You may leave Mina on the 12th before sunset. If you are still in Mina at dawn on the 13th, you must stone that day too."], HJ, "Wajib",
   says=[RAMI]),
 S("The farewell tawaf", ["Before leaving Makkah, perform tawaf al-wada': seven circuits without raml or idtiba', then two rak'ahs and Zamzam.",
   "It is wajib on those who do not live in Makkah. A woman in her period (after tawaf al-ziyarah) is excused from it.", "Leave with your heart attached to the House. May Allah accept your Hajj."], HJ, "Wajib",
   more="Many then travel to Madinah to visit the Prophet ﷺ and pray in his masjid. That visit is among the greatest acts of nearness, but it is not part of the Hajj."),
]

# ------------------------------------------------------------------ Wudu
WUDU = [
 S("Before you begin", ["Make the intention in your heart: to purify yourself for prayer.", "Sit somewhere raised, facing the qiblah if you can.", "Say 'Bismillah'.", "Use the miswak (or your finger) on your teeth."],
   f"{NI}, sunnahs and manners of wudu", "Sunnah", says=[say("At the start", "بِسْمِ اللَّهِ", "Bismillah.", "In the name of Allah.", f"{NI}, sunnahs of wudu")]),
 S("Hands", ["Wash both hands up to the wrists, three times.", "Pass water between your fingers. Move a ring so water reaches under it."], f"{NI}, sunnahs of wudu", "Sunnah"),
 S("Mouth", ["Take water in the right hand and rinse the mouth, three times, with fresh water each time.", "Rinse thoroughly, unless you are fasting."], f"{NI}, sunnahs of wudu", "Sunnah"),
 S("Nose", ["With the right hand, draw water into the nose, three times, fresh water each time.", "Blow it out with the left hand."], f"{NI}, sunnahs and manners of wudu", "Sunnah"),
 S("Face", ["Wash the whole face three times: from the hairline to under the chin, and from one earlobe to the other.", "Run wet fingers through a thick beard from below."],
   f"{NI}, the obligations of wudu; {QD}, Book of Purity", "Fard (once)", note="Washing once is the obligation; three times is the sunnah. Not one hair's breadth may be left dry."),
 S("Arms", ["Wash the right arm from the fingertips up to and including the elbow, three times.", "Then the left arm the same way."],
   f"{NI}, the obligations of wudu", "Fard (once)", note="The elbows are included. Remove anything that stops water reaching the skin, such as nail varnish."),
 S("Head", ["With wet hands, wipe over the whole head once, from front to back.", "Wiping a quarter of the head is the obligation; the whole head is the sunnah."],
   f"{NI}, the obligations and sunnahs of wudu", "Fard (a quarter)"),
 S("Ears and neck", ["With the same wet hands, wipe inside the ears with the index fingers and behind them with the thumbs.", "Wipe the back of the neck with the backs of the fingers (not the throat)."],
   f"{NI}, sunnahs of wudu", "Sunnah"),
 S("Feet", ["Wash the right foot up to and including the ankles, three times, passing the little finger of the left hand between the toes.", "Then the left foot the same way."],
   f"{NI}, the obligations of wudu", "Fard (once)", note="The ankles are included. Wiping over leather socks (khuffs) is allowed under its own conditions."),
 S("When you finish", ["Look up and say the shahadah and the du'a.", "Keep the order and do it without long pauses: both are sunnah."],
   f"{NI}, manners of wudu", "Adab", says=[say("After wudu", "أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ، اللَّهُمَّ اجْعَلْنِي مِنَ التَّوَّابِينَ، وَاجْعَلْنِي مِنَ الْمُتَطَهِّرِينَ",
     "Ashhadu an la ilaha illa Allahu wahdahu la sharika lah, wa ashhadu anna Muhammadan 'abduhu wa rasuluh. Allahumma ij'alni min al-tawwabin, waj'alni min al-mutatahhirin.",
     "I bear witness that there is no god but Allah alone, with no partner, and that Muhammad is His servant and Messenger. O Allah, make me of those who repent and of those who purify themselves.",
     "Sahih Muslim (234), with the last line in al-Tirmidhi (55); Nur al-Idah, manners of wudu")],
   more="Imam al-Ghazali's short du'a for each limb is under Home › Du'as › Imam al-Ghazali's du'as."),
]

# ------------------------------------------------------------------ Ghusl
GHUSL = [
 S("When ghusl is fard", ["After janabah: sexual intercourse (even without emission), or the release of fluid with desire, awake or asleep.", "For a woman, when her period or post-natal bleeding (nifas) ends."],
   f"{QD}, Book of Purity; {NI}, what makes ghusl necessary", "Know this first",
   note="The fard of ghusl is only three things: rinsing the whole mouth, rinsing the nose up to the soft bone, and washing the whole body once. Everything else below is the sunnah way."),
 S("Intention and bismillah", ["Make the intention in your heart to lift the state of major impurity.", "Say 'Bismillah' before entering the bathroom or before uncovering."], f"{NI}, sunnahs of ghusl", "Sunnah"),
 S("Hands, private parts, any impurity", ["Wash both hands up to the wrists.", "Wash the private parts.", "Wash off any impurity on the body."], f"{QD}, Book of Purity", "Sunnah"),
 S("Wudu", ["Make a full wudu as for prayer.", "If you stand where the water collects, leave the feet until the end."], f"{QD}, Book of Purity", "Sunnah"),
 S("Mouth and nose, thoroughly", ["Rinse the whole mouth so water reaches everywhere (gargle, unless fasting).", "Draw water up the nose to the soft bone."], f"{NI}, what is fard in ghusl", "Fard",
   note="If you did these well in your wudu, they count."),
 S("Pour water over the whole body", ["Pour water over the head three times, then over the right shoulder three times, then the left three times.", "Rub the body with your hands.",
   "Make sure water reaches every part: the navel, behind the ears, under the arms, between the toes, the roots of the hair, and the skin under the beard."],
   f"{QD}, Book of Purity; {NI}, what is fard and sunnah in ghusl", "Fard (whole body once)",
   note="A woman need not undo her braids if water reaches the roots of her hair. A man must wet all his hair."),
 S("Finish", ["Move away from where the water collected and wash your feet.", "Do not face the qiblah while uncovered, and do not talk unnecessarily."], f"{QD}, Book of Purity; {NI}, manners of ghusl", "Sunnah",
   more="This ghusl also counts as wudu, so you may pray straight after it unless something breaks your wudu."),
]

# ------------------------------------------------------------------ Salah
FAT = "\n".join(V(1, a) for a in range(1, 8))
IKH = "\n".join(V(112, a) for a in range(1, 5)).replace("بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ", "")
SALAH = [
 S("Before you pray", ["Wudu (or ghusl if needed).", "Clean body, clothes and place.", "Cover the 'awrah: for a man from the navel to below the knees; for a woman everything except the face, hands and feet.",
   "Face the qiblah, and make sure the time has come in.", "Make the intention in your heart: which prayer, e.g. 'the fard of Fajr'."],
   f"{NI}, conditions of the prayer", "Conditions (fard)",
   more="Rak'ahs of each prayer (Hanafi): Fajr 2 sunnah, 2 fard. Zuhr 4 sunnah, 4 fard, 2 sunnah. 'Asr 4 fard. Maghrib 3 fard, 2 sunnah. 'Isha' 4 fard, 2 sunnah, then witr 3 (wajib). This guide walks through two rak'ahs, then shows what changes for three or four."),
 S("Opening takbir", ["Stand straight, feet about four fingers apart.", "Raise the hands: men to the earlobes (thumbs touching them), women to the shoulders.", "Say 'Allahu akbar'. You are now in the prayer."],
   f"{QD}, how to pray; {NI}, sunnahs of the prayer", "Fard", says=[say("Takbir", "اللَّهُ أَكْبَرُ", "Allahu akbar.", "Allah is the Greatest.", f"{QD}, how to pray")]),
 S("Hands folded, opening praise", ["Men: right hand over the left, below the navel, holding the left wrist with thumb and little finger. Women: hands on the chest.", "Look at the place of prostration.", "Say the opening praise (thana') quietly."],
   f"{QD}, how to pray; {NI}, sunnahs of the prayer", "Sunnah",
   says=[say("Thana'", "سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، وَتَبَارَكَ اسْمُكَ، وَتَعَالَى جَدُّكَ، وَلَا إِلَهَ غَيْرُكَ", "Subhanaka Allahumma wa bihamdika, wa tabaraka ismuka, wa ta'ala jadduka, wa la ilaha ghayruk.",
     "Glory be to You, O Allah, and praise. Blessed is Your name, exalted is Your majesty, and there is no god besides You.", f"{QD}, how to pray")]),
 S("Seeking refuge and bismillah", ["Quietly say the ta'awwudh, then the basmalah."], f"{QD}, how to pray", "Sunnah",
   says=[say("Ta'awwudh and basmalah", "أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ، بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ", "A'udhu billahi min al-shaytan al-rajim. Bismillahi al-Rahmani al-Rahim.",
     "I seek refuge in Allah from the accursed devil. In the name of Allah, the Most Merciful, the Most Kind.", f"{QD}, how to pray")],
   note="Following an imam, you say only the thana' and then stay silent: the follower does not recite."),
 S("Al-Fatihah and a surah", ["Recite al-Fatihah, then say 'Amin' quietly.", "Then recite a surah, or at least three short verses (e.g. al-Ikhlas)."],
   f"{QD}, how to pray; {NI}, the wajibs of the prayer", "Fard to recite; al-Fatihah and the surah are wajib",
   says=[say("Al-Fatihah", FAT, "Bismillahi al-Rahmani al-Rahim. Al-hamdu lillahi rabbi al-'alamin. Al-Rahmani al-Rahim. Maliki yawmi al-din. Iyyaka na'budu wa iyyaka nasta'in. Ihdina al-sirata al-mustaqim. Sirata alladhina an'amta 'alayhim, ghayri al-maghdubi 'alayhim wa la al-dallin.",
     "In the name of Allah, the Most Merciful, the Most Kind. Praise be to Allah, Lord of the worlds, the Most Merciful, the Most Kind, Master of the Day of Judgement. You alone we worship and You alone we ask for help. Guide us on the straight path, the path of those You have blessed, not of those who earned anger, nor of those who went astray.", "Qur'an, al-Fatihah 1:1–7"),
     say("For example, al-Ikhlas", IKH, "Qul huwa Allahu ahad. Allahu al-samad. Lam yalid wa lam yulad. Wa lam yakun lahu kufuwan ahad.",
     "Say: He is Allah, One. Allah, the Everlasting Refuge. He does not beget, nor was He begotten, and there is none equal to Him.", "Qur'an, al-Ikhlas 112:1–4")]),
 S("Ruku' (bowing)", ["Say 'Allahu akbar' and bow.", "Men: hold the knees with fingers spread, back flat, head level with the back. Women bow a little less.", "Stay still and say the tasbih three times."],
   f"{QD}, how to pray; {NI}, how to pray", "Fard (stillness wajib)",
   says=[say("In ruku' (3 times)", "سُبْحَانَ رَبِّيَ الْعَظِيمِ", "Subhana rabbiya al-'azim.", "Glory be to my Lord, the Magnificent.", f"{QD}, how to pray")]),
 S("Standing up from ruku'", ["Rise saying 'Sami'a Allahu liman hamidah'.", "Standing straight and still, say 'Rabbana laka al-hamd'. (Behind an imam, say only 'Rabbana laka al-hamd'.)"],
   f"{NI}, how to pray", "Wajib (to stand still)",
   says=[say("Rising and standing", "سَمِعَ اللَّهُ لِمَنْ حَمِدَهُ — رَبَّنَا لَكَ الْحَمْدُ", "Sami'a Allahu liman hamidah. Rabbana laka al-hamd.", "Allah hears the one who praises Him. Our Lord, to You is all praise.", f"{NI}, how to pray")]),
 S("Sujud (prostration)", ["Say 'Allahu akbar' and go down: knees first, then hands, then the face between the hands.", "Forehead and nose on the ground, fingers and toes towards the qiblah.",
   "Men: arms away from the sides and the belly away from the thighs. Women: keep close and low.", "Stay still and say the tasbih three times."],
   f"{QD}, how to pray; {NI}, how to pray", "Fard",
   says=[say("In sujud (3 times)", "سُبْحَانَ رَبِّيَ الْأَعْلَى", "Subhana rabbiya al-a'la.", "Glory be to my Lord, the Most High.", f"{QD}, how to pray")]),
 S("Sitting, then the second sujud", ["Rise saying 'Allahu akbar' and sit upright, hands on the thighs, until you are still.", "Say 'Allahu akbar' and make the second sujud exactly like the first."],
   f"{QD}, how to pray", "Second sujud fard; sitting still wajib"),
 S("Stand for the second rak'ah", ["Say 'Allahu akbar' and stand up on the balls of the feet, without pushing on the ground or sitting first.",
   "Pray the second rak'ah like the first, but without the thana' and the ta'awwudh. Say 'Bismillah' before al-Fatihah."], f"{QD}, how to pray", "Sunnah way"),
 S("Sitting and the tashahhud", ["After the second sujud of the second rak'ah, sit: men on the left foot with the right foot upright, toes to the qiblah; women sit with both feet out to the right.",
   "Hands on the thighs. Recite the tashahhud of Ibn Mas'ud رضي الله عنه.", "Raise the right index finger at 'la ilaha' and lower it at 'illa Allah'."],
   f"{QD}, how to pray; {NI}, how to pray", "Wajib (the last sitting itself is fard)",
   says=[say("Tashahhud", "التَّحِيَّاتُ لِلَّهِ وَالصَّلَوَاتُ وَالطَّيِّبَاتُ، السَّلَامُ عَلَيْكَ أَيُّهَا النَّبِيُّ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ، السَّلَامُ عَلَيْنَا وَعَلَى عِبَادِ اللَّهِ الصَّالِحِينَ، أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللَّهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ",
     "Al-tahiyyatu lillahi wa al-salawatu wa al-tayyibat. Al-salamu 'alayka ayyuha al-nabiyyu wa rahmatullahi wa barakatuh. Al-salamu 'alayna wa 'ala 'ibadillahi al-salihin. Ashhadu an la ilaha illa Allah, wa ashhadu anna Muhammadan 'abduhu wa rasuluh.",
     "All greetings, prayers and good things are for Allah. Peace be on you, O Prophet, and the mercy of Allah and His blessings. Peace be on us and on the righteous servants of Allah. I bear witness that there is no god but Allah, and I bear witness that Muhammad is His servant and Messenger.",
     f"{QD}, how to pray; Sahih al-Bukhari (831) and Muslim (402), from Ibn Mas'ud رضي الله عنه")]),
 S("In a prayer of three or four rak'ahs", ["In the first sitting recite only the tashahhud, then stand straight up for the third rak'ah, saying 'Allahu akbar'.",
   "In the third and fourth rak'ahs of a fard prayer recite al-Fatihah only.", "Sit again after the last rak'ah and continue with the next step."],
   f"{QD}, how to pray; {NI}, the wajibs of the prayer", "Wajib",
   more="In witr (three rak'ahs), recite al-Fatihah and a surah in all three. In the third, before ruku', say 'Allahu akbar' raising the hands, then the qunut."),
 S("Salawat and a du'a", ["In the last sitting, after the tashahhud, send salawat on the Prophet ﷺ (the salawat of Ibrahim).",
   "Then make a du'a in words like those of the Qur'an and Sunnah."], f"{QD}, how to pray; {NI}, sunnahs of the prayer", "Sunnah",
   says=[say("Salawat Ibrahimiyyah", "اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ، اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ",
     "Allahumma salli 'ala Muhammadin wa 'ala ali Muhammad, kama sallayta 'ala Ibrahima wa 'ala ali Ibrahim, innaka hamidun majid. Allahumma barik 'ala Muhammadin wa 'ala ali Muhammad, kama barakta 'ala Ibrahima wa 'ala ali Ibrahim, innaka hamidun majid.",
     "O Allah, send blessings on Muhammad and the family of Muhammad, as You sent blessings on Ibrahim and the family of Ibrahim; You are Praiseworthy, Glorious. O Allah, bless Muhammad and the family of Muhammad, as You blessed Ibrahim and the family of Ibrahim; You are Praiseworthy, Glorious.",
     "Sahih al-Bukhari (3370), from Ka'b ibn 'Ujrah رضي الله عنه"),
     say("The du'a taught to Abu Bakr al-Siddiq رضي الله عنه", "اللَّهُمَّ إِنِّي ظَلَمْتُ نَفْسِي ظُلْمًا كَثِيرًا، وَلَا يَغْفِرُ الذُّنُوبَ إِلَّا أَنْتَ، فَاغْفِرْ لِي مَغْفِرَةً مِنْ عِنْدِكَ، وَارْحَمْنِي، إِنَّكَ أَنْتَ الْغَفُورُ الرَّحِيمُ",
     "Allahumma inni zalamtu nafsi zulman kathira, wa la yaghfiru al-dhunuba illa ant, faghfir li maghfiratan min 'indik, warhamni, innaka anta al-Ghafuru al-Rahim.",
     "O Allah, I have wronged myself greatly, and none forgives sins but You. So forgive me with forgiveness from You, and have mercy on me; You are the Forgiving, the Merciful.",
     "Sahih al-Bukhari (834) and Muslim (2705): Abu Bakr رضي الله عنه asked for a du'a to say in his prayer")]),
 S("Salam", ["Turn the head to the right and say the salam, then to the left and say it again.", "With the first salam the prayer ends."],
   f"{QD}, how to pray; {NI}, the wajibs of the prayer", "Wajib",
   says=[say("Right, then left", "السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ", "Al-salamu 'alaykum wa rahmatullah.", "Peace be on you, and the mercy of Allah.", f"{QD}, how to pray")]),
 S("After the prayer", ["Say 'Astaghfirullah' three times.", "Recite Ayat al-Kursi and the three Quls.", "Say 'Subhan Allah' 33 times, 'Al-hamdu lillah' 33 times and 'Allahu akbar' 33 times, then the tahlil once.",
   "Raise your hands and make du'a for yourself and the Muslims."], f"{NI}, the dhikr after the fard", "Sunnah",
   says=[say("Then once", "لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ، وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ",
     "La ilaha illa Allahu wahdahu la sharika lah, lahu al-mulku wa lahu al-hamd, wa huwa 'ala kulli shay'in qadir.",
     "There is no god but Allah alone, with no partner; His is the dominion and His the praise, and He has power over all things.", f"{NI}, the dhikr after the fard")],
   note="If a sunnah prayer follows the fard (Zuhr, Maghrib, 'Isha'), it is sunnah to stand for it soon, and to keep the longer dhikr until after it."),
 S("Witr: the qunut", ["In the third rak'ah of witr, after al-Fatihah and a surah, say 'Allahu akbar' raising your hands, fold them again, and recite the qunut. Then go into ruku'."],
   f"{QD}, how to pray; {NI}, the qunut", "Wajib",
   says=[say("Du'a al-qunut", "اللَّهُمَّ إِنَّا نَسْتَعِينُكَ، وَنَسْتَهْدِيكَ، وَنَسْتَغْفِرُكَ، وَنَتُوبُ إِلَيْكَ، وَنُؤْمِنُ بِكَ، وَنَتَوَكَّلُ عَلَيْكَ، وَنُثْنِي عَلَيْكَ الْخَيْرَ كُلَّهُ، نَشْكُرُكَ وَلَا نَكْفُرُكَ، وَنَخْلَعُ وَنَتْرُكُ مَنْ يَفْجُرُكَ، اللَّهُمَّ إِيَّاكَ نَعْبُدُ، وَلَكَ نُصَلِّي وَنَسْجُدُ، وَإِلَيْكَ نَسْعَى وَنَحْفِدُ، نَرْجُو رَحْمَتَكَ، وَنَخْشَى عَذَابَكَ، إِنَّ عَذَابَكَ الْجِدَّ بِالْكُفَّارِ مُلْحِقٌ",
     "Allahumma inna nasta'inuka, wa nastahdika, wa nastaghfiruka, wa natubu ilayk, wa nu'minu bik, wa natawakkalu 'alayk, wa nuthni 'alayka al-khayra kullah, nashkuruka wa la nakfuruk, wa nakhla'u wa natruku man yafjuruk. Allahumma iyyaka na'bud, wa laka nusalli wa nasjud, wa ilayka nas'a wa nahfid, narju rahmatak, wa nakhsha 'adhabak, inna 'adhabaka al-jidda bil-kuffari mulhiq.",
     "O Allah, we ask You for help and guidance and forgiveness, we turn to You, believe in You and rely on You, and we praise You with all good. We thank You and are not ungrateful, and we cast off and leave whoever disobeys You. O Allah, You alone we worship, to You we pray and prostrate, to You we hasten and serve. We hope for Your mercy and fear Your punishment; Your true punishment overtakes the disbelievers.",
     f"{NI}, the wording of the qunut")],
   note="If you do not know it yet, say 'Rabbana atina fi al-dunya hasanah…' or 'Allahumma ighfir li' three times until you learn it (Nur al-Idah)."),
]

# ------------------------------------------------------------------ Making up missed prayers, the short way
RA = "Ibn 'Abidin, Radd al-Muhtar, chapter on making up missed prayers"
FR = "Imam Ahmad Rida Khan, al-Fatawa al-Ridawiyyah, on making up many missed prayers"
QADA = [
 S("What must be made up", ["Every missed fard prayer, and witr (wajib in the Hanafi school).", "Sunnah prayers are not made up. (The sunnah of Fajr is prayed with the Fajr if both are made up before midday the same day.)",
   "Fasts of Ramadan that were missed are also owed."], f"{NI}, making up missed prayers; {QD}, chapter on missed prayers", "Fard",
   note="Use the Qada' tool (Tools › Qada' prayers) to work out how many you owe and to tick them off."),
 S("When you can pray them", ["At any time of day or night, except the three times when no prayer is valid: while the sun is rising, when it is at its height, and while it is setting.",
   "Unlike nafl, you may make them up after Fajr and after 'Asr."], f"{NI}, the disliked times", "Know this"),
 S("Order: when it matters", ["If you owe fewer than six prayers, make them up in order, before the prayer of the time (unless its time is running out).",
   "Once you owe six or more (not counting witr), the order no longer applies. Pray them in any order, alongside the prayers of the day."],
   f"{QD}, chapter on missed prayers; {NI}, what drops the order", "Fard (for fewer than six)"),
 S("The intention made easy", ["When you owe many, you do not need to know the exact date of each one.", "Intend, for example: 'the first Fajr I owe' (or 'the last Fajr I owe'). Each time you pray it, the next one becomes 'the first'."],
   f"{NI}, making up missed prayers: 'to make it easy, he intends the first Zuhr he owes, or the last'", "Sunnah way",
   says=[say("Intention (in the heart; saying it is fine)", "نَوَيْتُ أَنْ أُصَلِّيَ أَوَّلَ فَجْرٍ فَاتَنِي", "Nawaytu an usalliya awwala fajrin fatani.", "I intend to pray the first Fajr that I missed.", f"{NI}, making up missed prayers")]),
 S("The quickest way to pray each one", ["Keep every fard and wajib: the opening takbir, standing, al-Fatihah and a surah in the first two rak'ahs, ruku', both sujuds, sitting, the tashahhud and the salam.",
   "In ruku' and sujud you may say the tasbih once instead of three times.",
   "In the third and fourth rak'ahs of a fard prayer, instead of al-Fatihah you may say 'Subhan Allah' three times: al-Fatihah there is sunnah, not wajib.",
   "In the last sitting, after the tashahhud, you may shorten the salawat to 'Allahumma salli 'ala sayyidina Muhammadin wa alih', then give the salam.",
   "In witr, instead of the full qunut you may say 'Rabbi ighfir li' once."],
   f"al-Ikhtiyar li-Ta'lil al-Mukhtar (the last two rak'ahs); {NI}, the qunut; {FR}", "Allowed for qada'",
   says=[say("In the third and fourth rak'ahs (3 times)", "سُبْحَانَ اللَّهِ", "Subhan Allah.", "Glory be to Allah.", "al-Ikhtiyar: 'and if he wishes he says tasbih, for it [al-Fatihah] is not wajib'"),
         say("Short salawat in the last sitting", "اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدٍ وَآلِهِ", "Allahumma salli 'ala sayyidina Muhammadin wa alih.", "O Allah, send blessings on our master Muhammad and his family.", FR),
         say("In witr, in place of the qunut", "رَبِّ اغْفِرْ لِي", "Rabbi ighfir li.", "My Lord, forgive me.", f"{NI}: whoever cannot do the qunut says 'Allahumma ighfir li'; {FR}")],
   note="This is a concession for clearing a large debt of prayers quickly. It does not apply to the prayers of the day, which you should pray in full with their sunnahs.",
   more="Some scholars of later times also said the three tasbihs of ruku' and sujud are better kept. If you have time, praying them in full is better; the short way is for when the debt is large."),
 S("Make a plan you can keep", ["Pray one day's worth (Fajr, Zuhr, 'Asr, Maghrib, 'Isha', witr) with each prayer of the day, or each morning. That is about 10–15 minutes the short way.",
   "Spend time you would give to extra nafl on qada' instead, while keeping the regular sunnah prayers.", "Keep count in the Qada' tool so you always know what is left."],
   f"{RA}: busying oneself with missed prayers is more important than nafl, except the known sunnahs", "Advice"),
 S("If you die before finishing", ["Make a will (wasiyyah) that fidyah be paid from a third of your estate for what remains: for each prayer, including witr, half a sa' of wheat or its value.",
   "Keep going and ask Allah to accept. Sincere repentance with steady making up is what is asked of you."], f"{NI}, how the fidyah is paid (kayfiyyat al-isqat)", "Know this"),
]

GUIDES = [
 {"id": "wudu", "group": "purity", "title": "How to make wudu", "sub": "Step by step, with what is fard and what is sunnah", "src": f"{NI} and {QD}", "steps": WUDU},
 {"id": "ghusl", "group": "purity", "title": "How to make ghusl", "sub": "The full bath, and its three obligations", "src": f"{QD} and {NI}", "steps": GHUSL},
 {"id": "salah", "group": "prayer", "title": "How to pray", "sub": "Every position and what to say, the Hanafi way", "src": f"{QD} and {NI}", "steps": SALAH},
 {"id": "qada", "group": "prayer", "title": "Making up missed prayers, the quickest way", "sub": "The order, the easy intention and the short way to pray each one", "src": f"{NI}, {QD} and later Hanafi fatwas", "steps": QADA},
 {"id": "umrah", "group": "pilgrimage", "title": "How to perform 'Umrah", "sub": "Step by step, with the du'as", "src": HJ, "steps": UMRAH},
 {"id": "hajj", "group": "pilgrimage", "title": "How to perform Hajj", "sub": "Tamattu', from the 'umrah to the farewell tawaf", "src": HJ, "steps": HAJJ},
]
if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(__import__("harakat_cache").apply(GUIDES), open(os.path.join(here, "..", "app", "data", "guides.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print("guides", [(g["id"], len(g["steps"]), sum(len(s.get("says", [])) for s in g["steps"])) for g in GUIDES])
