"""The sections of Dala'il al-Khayrat that come before Part 1, with our own English.
Arabic transcribed from the printed Arabic-English edition (Lahore, 2010), book pages 26-94; Qur'an from Tanzil.
English is our own, translated from the Arabic (it does not copy any published translation)."""
import json
Q = json.load(open("/home/claude/ext/quran-json/data/tanzil/simple.json"))
def sura(s):   # Tanzil puts the basmalah on verse 1; keep it once
    return " ".join(v["text"] for v in Q[str(s)])
D = "/home/claude/dalail/front/"
lines = lambda f: [l.strip() for l in open(D + f) if l.strip()]
B = "بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ"
SAW = "صَلَّى اللَّهُ عَلَيْهِ وَآلِهِ وَسَلَّمَ"

def P(ar, en, n=None): d = {"ar": ar, "en": en}; d.update({"n": n} if n else {}); return d

OPENING = [
 P("أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ", "I seek the forgiveness of Allah, the Magnificent.", 3),
 P("سُبْحَانَ اللَّهِ وَالْحَمْدُ لِلَّهِ", "Glory be to Allah, and all praise is for Allah.", 3),
 P("حَسْبِيَ اللَّهُ وَنِعْمَ الْوَكِيلُ", "Allah is enough for me, and He is the best Trustee.", 3),
 P("أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ", "I seek refuge in Allah from the accursed devil."),
 P(B, "In the name of Allah, the Most Merciful, the Most Compassionate."),
 P(sura(112), "Surat al-Ikhlas: Say, He is Allah, One; Allah, the Eternal Refuge; He neither begets nor was begotten, and there is none equal to Him.", 3),
 P(sura(113), "Surat al-Falaq: Say, I seek refuge in the Lord of daybreak from the evil of what He created, from the evil of darkness when it settles, from the evil of those who blow on knots, and from the evil of an envier when he envies."),
 P(sura(114), "Surat al-Nas: Say, I seek refuge in the Lord of mankind, the King of mankind, the God of mankind, from the evil of the whisperer who withdraws, who whispers in the hearts of mankind, from among jinn and mankind."),
 P(" ".join(v["text"] for v in Q["1"]), "Surat al-Fatihah: In the name of Allah, the Most Merciful, the Most Compassionate. All praise is for Allah, Lord of the worlds, the Most Merciful, the Most Compassionate, Master of the Day of Judgement. You alone we worship and You alone we ask for help. Guide us on the straight path, the path of those You have blessed, not of those who earned anger, nor of those who went astray."),
]

ASMA = [P("أَسْمَاءُ اللَّهِ الْحُسْنَى ۔ " + B, "The Most Beautiful Names of Allah. In the name of Allah, the Most Merciful, the Most Compassionate.")] + \
  [P(f"{a} جَلَّ جَلَالُهُ", f"{e}, exalted is His majesty.") for a, e in zip(lines("allah.txt"), lines("allah_en.txt"))]

IFTITAH = [
 P(B, "In the name of Allah, the Most Merciful, the Most Compassionate."),
 P("إِلَهِي بِجَاهِ نَبِيِّكَ سَيِّدِنَا مُحَمَّدٍ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ عِنْدَكَ وَمَكَانَتِهِ لَدَيْكَ وَمَحَبَّتِكَ لَهُ وَمَحَبَّتِهِ لَكَ",
   "My God, by the rank of Your Prophet, our master Muhammad ﷺ, with You, his standing in Your presence, Your love for him and his love for You,"),
 P("وَبِالسِّرِّ الَّذِي بَيْنَكَ وَبَيْنَهُ", "and by the secret that is between You and him,"),
 P("أَسْأَلُكَ أَنْ تُصَلِّيَ وَتُسَلِّمَ عَلَيْهِ وَعَلَى آلِهِ وَصَحْبِهِ وَضَاعِفِ اللَّهُمَّ مَحَبَّتِي فِيهِ وَعَرِّفْنِي بِحَقِّهِ وَرُتَبِهِ وَوَفِّقْنِي لِاتِّبَاعِهِ وَالْقِيَامِ بِأَدَبِهِ وَسُنَّتِهِ وَاجْمَعْنِي عَلَيْهِ وَمَتِّعْنِي بِرُؤْيَتِهِ وَأَسْعِدْنِي بِمُكَالَمَتِهِ وَارْفَعْ عَنِّي الْعَوَائِقَ وَالْعَلَائِقَ وَالْوَسَائِطَ وَالْحِجَابَ وَشَنِّفْ سَمْعِي مَعَهُ بِلَذِيذِ الْخِطَابِ",
   "I ask You to send blessings and peace on him, his family and his Companions. O Allah, multiply my love for him, make me know his due and his ranks, grant me success in following him and keeping to his manners and his Sunnah. Gather me to him, delight me with seeing him, gladden me with speaking to him, lift from me every obstacle, attachment, intermediary and veil, and grace my hearing with the sweetness of his words."),
 P("وَهَيِّئْنِي لِلتَّلَقِّي مِنْهُ وَأَهِّلْنِي لِخِدْمَتِهِ", "Make me ready to receive from him, and make me worthy to serve him."),
 P("وَاجْعَلْ صَلَاتِي عَلَيْهِ نُورًا نَيِّرًا كَامِلًا مُكَمَّلًا طَاهِرًا مُطَهَّرًا مَاحِيًا كُلَّ ظُلْمٍ وَظُلْمَةٍ وَشَكٍّ وَشِرْكٍ وَكُفْرٍ وَزُورٍ وَوِزْرٍ وَاجْعَلْهَا سَبَبًا لِلتَّمْحِيصِ وَمَرْقًى لِأَنَالَ بِهَا أَعْلَى مَقَامِ الْإِخْلَاصِ وَالتَّخْصِيصِ حَتَّى لَا يَبْقَى فِيَّ رَبَّانِيَّةٌ لِغَيْرِكَ وَحَتَّى أَصْلُحَ لِحَضْرَتِكَ وَأَكُونَ مِنْ أَهْلِ خُصُوصِيَّتِكَ مُسْتَمْسِكًا بِأَدَبِهِ وَسُنَّتِهِ صَلَّى اللَّهُ عَلَيْهِ وَآلِهِ وَأَصْحَابِهِ وَأَهْلِ بَيْتِهِ أَجْمَعِينَ فِي كُلِّ وَقْتٍ وَحِينٍ",
   "Make my blessings on him a shining light, complete and perfecting, pure and purifying, erasing every wrong and darkness, doubt and association, disbelief, falsehood and sin. Make them a means of purification and a ladder by which I reach the highest station of sincerity and being singled out, until nothing in me answers to any lord but You, until I am fit for Your presence and among Your chosen people, holding fast to his manners and his Sunnah. Allah's blessings be on him, his family, his Companions and all his household, at every moment and time."),
 P("يَا اللَّهُ يَا نُورُ يَا حَقُّ يَا مُبِينُ", "O Allah, O Light, O Truth, O Manifest.", 3),
]

NABI = [P("ذِكْرُ أَسْمَاءِ سَيِّدِنَا وَنَبِيِّنَا وَمَوْلَانَا مُحَمَّدٍ " + SAW + " وَهِيَ مِائَتَانِ وَوَاحِدٌ وَهِيَ هَذِهِ",
          "The names of our master, our Prophet and our patron Muhammad ﷺ. They are two hundred and one, and these are they.")]
for k, (a, e) in enumerate(zip(lines("nabi.txt"), lines("nabi_en.txt"))):
    pre = "اللَّهُمَّ صَلِّ وَسَلِّمْ وَبَارِكْ عَلَى مَنِ اسْمُهُ " if k < 4 else ""
    NABI.append(P(f"{pre}سَيِّدُنَا {a} {SAW}", ("O Allah, send blessings, peace and grace on the one whose name is: " if k < 4 else "") + f"our master {e} ﷺ"))
NABI.append(P("اللَّهُمَّ يَا رَبِّ بِجَاهِ نَبِيِّكَ الْمُصْطَفَى وَرَسُولِكَ الْمُرْتَضَى طَهِّرْ قُلُوبَنَا مِنْ كُلِّ وَصْفٍ يُبَاعِدُنَا عَنْ مُشَاهَدَتِكَ وَمَحَبَّتِكَ وَأَمِتْنَا عَلَى السُّنَّةِ وَالْجَمَاعَةِ وَالشَّوْقِ إِلَى لِقَائِكَ يَا ذَا الْجَلَالِ وَالْإِكْرَامِ",
   "O Allah, my Lord, by the rank of Your chosen Prophet and Your well-pleasing Messenger, purify our hearts of every trait that keeps us far from witnessing You and loving You, and let us die upon the Sunnah and the Community, longing to meet You, O Possessor of Majesty and Honour."))
NABI.append(P("وَصَلَّى اللَّهُ عَلَى سَيِّدِنَا وَمَوْلَانَا مُحَمَّدٍ وَعَلَى آلِهِ وَصَحْبِهِ وَسَلَّمَ تَسْلِيمًا وَالْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
   "Allah's blessings be on our master and patron Muhammad, his family and Companions, and abundant peace. All praise is for Allah, Lord of the worlds."))

NIYYAH = [
 P("هَذَا الدُّعَاءُ يُقْرَأُ بَعْدَ الْأَسْمَاءِ الشَّرِيفَةِ", "This du'a is read after the noble Names."),
 P(B, "In the name of Allah, the Most Merciful, the Most Compassionate."),
 P("الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ", "All praise is for Allah, Lord of the worlds."),
 P("حَسْبِيَ اللَّهُ وَنِعْمَ الْوَكِيلُ وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ الْعَلِيِّ الْعَظِيمِ", "Allah is enough for me and He is the best Trustee. There is no power and no strength except by Allah, the High, the Magnificent."),
 P("اللَّهُمَّ إِنِّي أَبْرَأُ مِنْ حَوْلِي وَقُوَّتِي إِلَى حَوْلِكَ وَقُوَّتِكَ", "O Allah, I let go of my own power and strength and turn to Your power and strength."),
 P("اللَّهُمَّ إِنِّي نَوَيْتُ بِصَلَاتِي عَلَى النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ امْتِثَالًا لِأَمْرِكَ وَتَصْدِيقًا لِنَبِيِّكَ سَيِّدِنَا مُحَمَّدٍ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ وَمَحَبَّةً فِيهِ وَشَوْقًا إِلَيْهِ وَتَعْظِيمًا لِقَدْرِهِ وَلِكَوْنِهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ أَهْلًا لِذَلِكَ فَتَقَبَّلْهَا مِنِّي بِفَضْلِكَ وَإِحْسَانِكَ وَأَزِلْ حِجَابَ الْغَفْلَةِ عَنْ قَلْبِي وَاجْعَلْنِي مِنْ عِبَادِكَ الصَّالِحِينَ",
   "O Allah, in sending blessings on the Prophet ﷺ I intend to obey Your command, to affirm the truth of Your Prophet, our master Muhammad ﷺ, out of love for him and longing for him, to honour his rank, and because he ﷺ is worthy of it. So accept it from me by Your grace and kindness, lift the veil of heedlessness from my heart, and make me one of Your righteous servants."),
 P("اللَّهُمَّ زِدْهُ شَرَفًا عَلَى شَرَفِهِ الَّذِي أَوْلَيْتَهُ وَعِزًّا عَلَى عِزِّهِ الَّذِي أَعْطَيْتَهُ وَنُورًا عَلَى نُورِهِ الَّذِي مِنْهُ خَلَقْتَهُ وَأَعْلِ مَقَامَهُ فِي مَقَامَاتِ الْمُرْسَلِينَ وَدَرَجَتَهُ فِي دَرَجَاتِ النَّبِيِّينَ وَأَسْأَلُكَ رِضَاكَ وَرِضَاهُ يَا رَبَّ الْعَالَمِينَ مَعَ الْعَافِيَةِ الدَّائِمَةِ وَالْمَوْتِ عَلَى الْكِتَابِ وَالسُّنَّةِ وَالْجَمَاعَةِ وَكَلِمَةِ الشَّهَادَةِ عَلَى تَحْقِيقِهَا مِنْ غَيْرِ تَبْدِيلٍ وَلَا تَغْيِيرٍ وَاغْفِرْ لِي مَا ارْتَكَبْتُهُ بِفَضْلِكَ وَجُودِكَ وَكَرَمِكَ يَا أَرْحَمَ الرَّاحِمِينَ",
   "O Allah, increase him in honour upon the honour You gave him, in might upon the might You granted him, and in light upon the light from which You created him. Raise his station among the stations of the messengers and his rank among the ranks of the prophets. I ask You for Your pleasure and his, O Lord of the worlds, with lasting well-being, and to die upon the Book, the Sunnah and the Community, and upon the testimony of faith truly held, without change or alteration. Forgive me what I have done, by Your grace, generosity and kindness, O Most Merciful of the merciful."),
 P("وَصَلَّى اللَّهُ عَلَى سَيِّدِنَا مُحَمَّدٍ وَعَلَى آلِهِ وَصَحْبِهِ وَسَلَّمَ تَسْلِيمًا وَالْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ", "Allah's blessings be on our master Muhammad, his family and Companions, and abundant peace. All praise is for Allah, Lord of the worlds."),
 P("اللَّهُمَّ جَدِّدْ وَجَرِّدْ فِي هَذَا الْوَقْتِ وَفِي هَذِهِ السَّاعَةِ مِنْ صَلَوَاتِكَ التَّامَّاتِ وَتَحِيَّاتِكَ الزَّاكِيَاتِ وَرِضْوَانِكَ الْأَكْبَرِ الْأَتَمِّ الْأَدْوَمِ عَلَى أَكْمَلِ عَبْدٍ لَكَ فِي هَذَا الْعَالَمِ مِنْ بَنِي آدَمَ الَّذِي أَقَمْتَهُ لَكَ ظِلًّا وَجَعَلْتَهُ لِحَوَائِجِ خَلْقِكَ قِبْلَةً وَمَحَلًّا وَاصْطَفَيْتَهُ لِنَفْسِكَ وَأَقَمْتَهُ بِحُجَّتِكَ وَأَظْهَرْتَهُ بِصُورَتِكَ وَاخْتَرْتَهُ مُسْتَوًى لِتَجَلِّيكَ وَمَنْزِلًا لِتَنْفِيذِ أَوَامِرِكَ وَنَوَاهِيكَ فِي أَرْضِكَ وَسَمَاوَاتِكَ وَوَاسِطَةً بَيْنَكَ وَبَيْنَ مُكَوَّنَاتِكَ",
   "O Allah, renew and send down, at this time and in this hour, Your perfect blessings, Your pure greetings and Your greatest, fullest and most lasting good pleasure on the most perfect of Your servants in this world from the children of Adam: whom You set up as a shade for You, made a qiblah and resting place for the needs of Your creation, chose for Yourself, established with Your proof, made manifest with the form You gave him, chose as a place where Your self-disclosure appears and a station for carrying out Your commands and prohibitions in Your earth and heavens, and an intermediary between You and Your creation."),
 P("اللَّهُمَّ اجْعَلْنِي فِي قَلْبِ الْإِنْسَانِ الْكَامِلِ وَحَبِّبْهُ فِيَّ", "O Allah, place me in the heart of the Perfect Man, and make him love me."),
 P("وَصَلَّى اللَّهُ عَلَى سَيِّدِنَا وَمَوْلَانَا مُحَمَّدٍ وَعَلَى آلِهِ وَصَحْبِهِ بِعَدَدِ ذَرَّاتِ الْوُجُودِ وَبِعَدَدِ مَعْلُومَاتِ اللَّهِ", "Allah's blessings be on our master and patron Muhammad, his family and Companions, as many as the atoms of existence and as many as all that Allah knows."),
 P("اللَّهُمَّ وَفِّقْنِي لِقِرَاءَتِهَا عَلَى الدَّوَامِ آمِينَ يَا رَبَّ الْعَالَمِينَ", "O Allah, grant me success in reading it always. Amin, O Lord of the worlds."),
]

RAWDAH = [
 P("هَذِهِ صِفَةُ الرَّوْضَةِ الَّتِي دُفِنَ فِيهَا رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ وَصَاحِبَاهُ أَبُو بَكْرٍ وَعُمَرُ رَضِيَ اللَّهُ عَنْهُمَا",
   "This is the description of the blessed garden in which the Messenger of Allah ﷺ is buried, with his two companions Abu Bakr and 'Umar رضي الله عنهما."),
 P("هَكَذَا ذَكَرَهُ عُرْوَةُ ابْنُ الزُّبَيْرِ رَضِيَ اللَّهُ تَعَالَى عَنْهُ قَالَ دُفِنَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ فِي السَّهْوَةِ وَدُفِنَ أَبُو بَكْرٍ رَضِيَ اللَّهُ عَنْهُ خَلْفَ رَسُولِ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ وَدُفِنَ عُمَرُ بْنُ الْخَطَّابِ رَضِيَ اللَّهُ عَنْهُ عِنْدَ رِجْلَيْ أَبِي بَكْرٍ وَبَقِيَتِ السَّهْوَةُ الشَّرْقِيَّةُ فَارِغَةً فِيهَا مَوْضِعُ قَبْرٍ يُقَالُ وَاللَّهُ أَعْلَمُ إِنَّ عِيسَى ابْنَ مَرْيَمَ عَلَيْهِ السَّلَامُ يُدْفَنُ فِيهِ وَكَذَلِكَ جَاءَ فِي الْخَبَرِ عَنْ رَسُولِ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ",
   "So it was described by 'Urwah ibn al-Zubayr رضي الله عنه. He said: The Messenger of Allah ﷺ was buried in the alcove, Abu Bakr رضي الله عنه was buried behind him, and 'Umar ibn al-Khattab رضي الله عنه at the feet of Abu Bakr. The eastern part of the alcove remained empty, with room for a grave. It is said, and Allah knows best, that 'Isa son of Maryam عليه السلام will be buried there, and so it has come in a report from the Messenger of Allah ﷺ."),
 P("وَقَالَتْ عَائِشَةُ رَضِيَ اللَّهُ عَنْهَا رَأَيْتُ ثَلَاثَةَ أَقْمَارٍ سُقُوطًا فِي حُجْرَتِي فَقَصَصْتُ رُؤْيَايَ عَلَى أَبِي بَكْرٍ فَقَالَ لِي يَا عَائِشَةُ لَيُدْفَنَنَّ فِي بَيْتِكِ ثَلَاثَةٌ هُمْ خَيْرُ أَهْلِ الْأَرْضِ فَلَمَّا تُوُفِّيَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ وَدُفِنَ فِي بَيْتِي قَالَ لِي أَبُو بَكْرٍ هَذَا وَاحِدٌ مِنْ أَقْمَارِكِ وَهُوَ خَيْرُهُمْ صَلَّى اللَّهُ عَلَيْهِ وَعَلَى آلِهِ وَسَلَّمَ كَثِيرًا",
   "'A'ishah رضي الله عنها said: I saw three moons fall into my room, and told my dream to Abu Bakr. He said: 'A'ishah, three people will be buried in your house who are the best of the people of the earth. When the Messenger of Allah ﷺ passed away and was buried in my house, Abu Bakr said to me: This is one of your moons, and he is the best of them. Allah's abundant blessings and peace be on him and his family."),
]

FRONT = {
 "opening": {"title": "Opening Du'a", "about": "Read before you begin: seeking forgiveness, praise and the last three surahs with al-Fatihah.", "pages": "26–28", "items": OPENING},
 "asma": {"title": "Names of Allah", "about": "The ninety-nine Most Beautiful Names, each followed by 'exalted is His majesty'.", "pages": "30–36", "items": ASMA},
 "iftitah": {"title": "Du'a al-Iftitah", "about": "The opening supplication, read after the Names of Allah.", "pages": "38–40", "items": IFTITAH},
 "nabi": {"title": "Names of the Prophet ﷺ", "about": "Al-Jazuli's list of 201 names of the Prophet ﷺ, each with a blessing.", "pages": "62–88", "items": NABI},
 "niyyah": {"title": "Du'a of Intention", "about": "Read after the noble Names, to make your intention before the day's part.", "pages": "90–92", "items": NIYYAH},
 "rawdah": {"title": "The Blessed Rawdah", "about": "A description of the resting place of the Prophet ﷺ and his two companions.", "pages": "94", "items": RAWDAH},
}
if __name__ == "__main__":
    print({k: len(v["items"]) for k, v in FRONT.items()})
