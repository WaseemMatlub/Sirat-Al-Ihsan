"""Fully voweled Arabic for the daily and al-Ghazali du'as, and the step-by-step layout of the longer ones.
Wording is the same as in duas.py (al-Adhkar and Bidayat al-Hidayah); only the harakat are added."""

# Same order as DAILY in duas.py
DAILY_AR = [
 "الْحَمْدُ لِلَّهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ",
 "بِاسْمِكَ اللَّهُمَّ أَحْيَا وَأَمُوتُ",
 "بِاسْمِكَ رَبِّي وَضَعْتُ جَنْبِي، وَبِكَ أَرْفَعُهُ، إِنْ أَمْسَكْتَ نَفْسِي فَارْحَمْهَا، وَإِنْ أَرْسَلْتَهَا فَاحْفَظْهَا بِمَا تَحْفَظُ بِهِ عِبَادَكَ الصَّالِحِينَ",
 "بِسْمِ اللَّهِ، اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْخُبُثِ وَالْخَبَائِثِ",
 "غُفْرَانَكَ، الْحَمْدُ لِلَّهِ الَّذِي أَذْهَبَ عَنِّي الْأَذَى وَعَافَانِي",
 "أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ، اللَّهُمَّ اجْعَلْنِي مِنَ التَّوَّابِينَ، وَاجْعَلْنِي مِنَ الْمُتَطَهِّرِينَ",
 "الْحَمْدُ لِلَّهِ الَّذِي كَسَانِي هَذَا وَرَزَقَنِيهِ مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ",
 "بِسْمِ اللَّهِ، تَوَكَّلْتُ عَلَى اللَّهِ، لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ",
 "اللَّهُمَّ إِنِّي أَسْأَلُكَ خَيْرَ الْمَوْلَجِ، وَخَيْرَ الْمَخْرَجِ، بِاسْمِ اللَّهِ وَلَجْنَا، وَبِاسْمِ اللَّهِ خَرَجْنَا، وَعَلَى اللَّهِ رَبِّنَا تَوَكَّلْنَا",
 "بِسْمِ اللَّهِ",
 "الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنِي هَذَا وَرَزَقَنِيهِ مِنْ غَيْرِ حَوْلٍ مِنِّي وَلَا قُوَّةٍ",
 "اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ",
 "اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ",
 "قُلْ هُوَ اللَّهُ أَحَدٌ، وَالْمُعَوِّذَتَيْنِ، ثَلَاثَ مَرَّاتٍ",
 "اللَّهُمَّ أَنْتَ رَبِّي، لَا إِلَهَ إِلَّا أَنْتَ، خَلَقْتَنِي وَأَنَا عَبْدُكَ، وَأَنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، أَبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ، وَأَبُوءُ لَكَ بِذَنْبِي، فَاغْفِرْ لِي، فَإِنَّهُ لَا يَغْفِرُ الذُّنُوبَ إِلَّا أَنْتَ، أَعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ",
 "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ وَإِنَّا إِلَى رَبِّنَا لَمُنْقَلِبُونَ، اللَّهُمَّ إِنَّا نَسْأَلُكَ فِي سَفَرِنَا هَذَا الْبِرَّ وَالتَّقْوَى، وَمِنَ الْعَمَلِ مَا تَرْضَى، اللَّهُمَّ هَوِّنْ عَلَيْنَا سَفَرَنَا هَذَا، وَاطْوِ عَنَّا بُعْدَهُ، اللَّهُمَّ أَنْتَ الصَّاحِبُ فِي السَّفَرِ، وَالْخَلِيفَةُ فِي الْأَهْلِ، اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ وَعْثَاءِ السَّفَرِ، وَكَآبَةِ الْمَنْظَرِ، وَسُوءِ الْمُنْقَلَبِ فِي الْمَالِ وَالْأَهْلِ",
 "لَا إِلَهَ إِلَّا اللَّهُ الْعَظِيمُ الْحَلِيمُ، لَا إِلَهَ إِلَّا اللَّهُ رَبُّ الْعَرْشِ الْعَظِيمِ، لَا إِلَهَ إِلَّا اللَّهُ رَبُّ السَّمَاوَاتِ وَرَبُّ الْأَرْضِ رَبُّ الْعَرْشِ الْكَرِيمِ",
 "اللَّهُمَّ أَنَا عَبْدُكَ، وَابْنُ عَبْدِكَ، وَابْنُ أَمَتِكَ، فِي قَبْضَتِكَ، نَاصِيَتِي بِيَدِكَ، مَاضٍ فِيَّ حُكْمُكَ، عَدْلٌ فِيَّ قَضَاؤُكَ، أَسْأَلُكَ بِكُلِّ اسْمٍ هُوَ لَكَ سَمَّيْتَ بِهِ نَفْسَكَ، أَوْ أَنْزَلْتَهُ فِي كِتَابِكَ، أَوْ عَلَّمْتَهُ أَحَدًا مِنْ خَلْقِكَ، أَوِ اسْتَأْثَرْتَ بِهِ فِي عِلْمِ الْغَيْبِ عِنْدَكَ، أَنْ تَجْعَلَ الْقُرْآنَ الْعَظِيمَ نُورَ صَدْرِي، وَرَبِيعَ قَلْبِي، وَجَلَاءَ حُزْنِي، وَذَهَابَ هَمِّي",
 "اللَّهُمَّ رَبَّ النَّاسِ أَذْهِبِ الْبَأْسَ، اشْفِ أَنْتَ الشَّافِي، لَا شِفَاءَ إِلَّا شِفَاؤُكَ، شِفَاءً لَا يُغَادِرُ سَقَمًا",
 None,   # 'When in pain' is given in parts below
 "اللَّهُمَّ صَيِّبًا نَافِعًا",
 "اللَّهُمَّ أَهِلَّهُ عَلَيْنَا بِالْيُمْنِ وَالْإِيمَانِ، وَالسَّلَامَةِ وَالْإِسْلَامِ، رَبِّي وَرَبُّكَ اللَّهُ",
 "الْحَمْدُ لِلَّهِ، اللَّهُمَّ كَمَا حَسَّنْتَ خَلْقِي فَحَسِّنْ خُلُقِي",
 "لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ، وَلَهُ الْحَمْدُ، يُحْيِي وَيُمِيتُ، وَهُوَ حَيٌّ لَا يَمُوتُ، بِيَدِهِ الْخَيْرُ، وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ",
 "يَرْحَمُكَ اللَّهُ",
]
# Arabic inside the notes, voweled
NOTE_AR = {
 "بسم الله أوله وآخره": "بِسْمِ اللَّهِ أَوَّلَهُ وَآخِرَهُ",
 "آيبون تائبون عابدون لربنا حامدون": "آيِبُونَ تَائِبُونَ عَابِدُونَ لِرَبِّنَا حَامِدُونَ",
}
# Du'as shown step by step: title -> [(step, what to do, arabic, english)]
DAILY_PARTS = {
 "When in pain": [
  ("First", "Put your hand where it hurts and say three times:", "بِسْمِ اللَّهِ", "In the name of Allah."),
  ("Then", "Say seven times:", "أَعُوذُ بِعِزَّةِ اللَّهِ وَقُدْرَتِهِ مِنْ شَرِّ مَا أَجِدُ وَأُحَاذِرُ", "I seek refuge in the might and power of Allah from the evil of what I feel and what I fear."),
 ],
}

B = "Imam al-Ghazali, Bidayat al-Hidayah"
GHAZALI = [
 {"t": "On waking", "when": "The first words of the day", "src": f"{B}, the manners of waking",
  "note": "Al-Ghazali: try to wake before dawn, and let the first thing on your heart and tongue be the remembrance of Allah.",
  "parts": [
   ("Praise", "As soon as you wake:", "الْحَمْدُ لِلَّهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ",
    "Praise be to Allah who gave us life after He caused us to die, and to Him is the return."),
   ("The morning", "Then:", "أَصْبَحْنَا وَأَصْبَحَ الْمُلْكُ لِلَّهِ، وَالْعَظَمَةُ وَالسُّلْطَانُ لِلَّهِ، وَالْعِزَّةُ وَالْقُدْرَةُ لِلَّهِ رَبِّ الْعَالَمِينَ، أَصْبَحْنَا عَلَى فِطْرَةِ الْإِسْلَامِ، وَعَلَى كَلِمَةِ الْإِخْلَاصِ، وَعَلَى دِينِ نَبِيِّنَا مُحَمَّدٍ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ، وَعَلَى مِلَّةِ أَبِينَا إِبْرَاهِيمَ حَنِيفًا مُسْلِمًا وَمَا كَانَ مِنَ الْمُشْرِكِينَ",
    "We have entered the morning and the dominion belongs to Allah; greatness and authority, might and power belong to Allah, Lord of the worlds. We have entered the morning upon the natural way of Islam, the word of sincerity, the religion of our Prophet Muhammad ﷺ, and the way of our father Ibrahim عليه السلام, upright and submitting, who was not of the idolaters."),
   ("Asking for the day", "Then:", "اللَّهُمَّ بِكَ أَصْبَحْنَا، وَبِكَ أَمْسَيْنَا، وَبِكَ نَحْيَا، وَبِكَ نَمُوتُ، وَإِلَيْكَ النُّشُورُ، اللَّهُمَّ إِنَّا نَسْأَلُكَ أَنْ تَبْعَثَنَا فِي هَذَا الْيَوْمِ إِلَى كُلِّ خَيْرٍ، وَنَعُوذُ بِكَ أَنْ نَجْتَرِحَ فِيهِ سُوءًا أَوْ نَجُرَّهُ إِلَى مُسْلِمٍ، أَوْ يَجُرَّهُ أَحَدٌ إِلَيْنَا، نَسْأَلُكَ خَيْرَ هَذَا الْيَوْمِ وَخَيْرَ مَا فِيهِ، وَنَعُوذُ بِكَ مِنْ شَرِّ هَذَا الْيَوْمِ وَشَرِّ مَا فِيهِ",
    "O Allah, by You we enter the morning and the evening, by You we live and die, and to You is the return. O Allah, we ask You to send us forth today to every good, and we seek refuge in You from committing evil today, or bringing it on a Muslim, or anyone bringing it on us. We ask You for the good of this day and what is in it, and seek refuge in You from its evil and the evil of what is in it."),
  ]},
 {"t": "After istinja'", "when": "After cleaning yourself in the toilet", "src": f"{B}, the manners of the toilet",
  "ar": "اللَّهُمَّ طَهِّرْ قَلْبِي مِنَ النِّفَاقِ، وَحَصِّنْ فَرْجِي مِنَ الْفَوَاحِشِ",
  "en": "O Allah, purify my heart of hypocrisy and guard my chastity from indecency."},
 {"t": "The du'as of wudu", "when": "One short du'a for each part of wudu, in order", "src": f"{B}, the manners of wudu",
  "note": "Al-Ghazali recommends these. Imam al-Nawawi رحمه الله notes in al-Adhkar that the limb-by-limb du'as are not reported from the Prophet ﷺ; they are good words of du'a, said without believing them to be a sunnah. Your wudu is complete without them.",
  "parts": [
   ("Before you begin", "Sit facing the qiblah and say:", "بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ، رَبِّ أَعُوذُ بِكَ مِنْ هَمَزَاتِ الشَّيَاطِينِ، وَأَعُوذُ بِكَ رَبِّ أَنْ يَحْضُرُونِ",
    "In the name of Allah, the Most Merciful, the Most Kind. My Lord, I seek refuge in You from the promptings of the devils, and I seek refuge in You, my Lord, from their coming near me."),
   ("Hands", "Wash both hands three times, then make your intention:", "اللَّهُمَّ إِنِّي أَسْأَلُكَ الْيُمْنَ وَالْبَرَكَةَ، وَأَعُوذُ بِكَ مِنَ الشُّؤْمِ وَالْهَلَكَةِ",
    "O Allah, I ask You for good fortune and blessing, and I seek refuge in You from ill fortune and ruin."),
   ("Mouth", "Rinse your mouth three times:", "اللَّهُمَّ أَعِنِّي عَلَى تِلَاوَةِ كِتَابِكَ وَكَثْرَةِ الذِّكْرِ لَكَ، وَثَبِّتْنِي بِالْقَوْلِ الثَّابِتِ فِي الْحَيَاةِ الدُّنْيَا وَفِي الْآخِرَةِ",
    "O Allah, help me to recite Your Book and remember You much, and make me firm with the firm word in this life and the next."),
   ("Nose, drawing water in", "Draw water into your nose three times:", "اللَّهُمَّ أَرِحْنِي رَائِحَةَ الْجَنَّةِ وَأَنْتَ عَنِّي رَاضٍ",
    "O Allah, let me smell the scent of Paradise while You are pleased with me."),
   ("Nose, blowing out", "Blow the water out:", "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ رَوَائِحِ النَّارِ وَسُوءِ الدَّارِ",
    "O Allah, I seek refuge in You from the smells of the Fire and an evil abode."),
   ("Face", "Wash your face, from the hairline to the chin and from ear to ear:", "اللَّهُمَّ بَيِّضْ وَجْهِي بِنُورِكَ يَوْمَ تَبْيَضُّ وُجُوهُ أَوْلِيَائِكَ، وَلَا تُسَوِّدْ وَجْهِي بِظُلُمَاتِكَ يَوْمَ تَسْوَدُّ وُجُوهُ أَعْدَائِكَ",
    "O Allah, brighten my face with Your light on the Day the faces of Your friends are brightened, and do not darken my face with Your darkness on the Day the faces of Your enemies are darkened."),
   ("Right arm", "Wash your right arm up to and including the elbow:", "اللَّهُمَّ أَعْطِنِي كِتَابِي بِيَمِينِي، وَحَاسِبْنِي حِسَابًا يَسِيرًا",
    "O Allah, give me my book in my right hand and make my reckoning easy."),
   ("Left arm", "Wash your left arm the same way:", "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ أَنْ تُعْطِيَنِي كِتَابِي بِشِمَالِي أَوْ مِنْ وَرَاءِ ظَهْرِي",
    "O Allah, I seek refuge in You from being given my book in my left hand or from behind my back."),
   ("Head", "Wipe your head with wet hands, front to back and back again:", "اللَّهُمَّ غَشِّنِي بِرَحْمَتِكَ، وَأَنْزِلْ عَلَيَّ مِنْ بَرَكَاتِكَ، وَأَظِلَّنِي تَحْتَ ظِلِّ عَرْشِكَ يَوْمَ لَا ظِلَّ إِلَّا ظِلُّكَ، اللَّهُمَّ حَرِّمْ شَعْرِي وَبَشَرِي عَلَى النَّارِ",
    "O Allah, cover me with Your mercy, send down Your blessings on me, and shade me under Your Throne on the Day there is no shade but Yours. O Allah, forbid my hair and skin to the Fire."),
   ("Ears", "Wipe your ears, inside and out:", "اللَّهُمَّ اجْعَلْنِي مِنَ الَّذِينَ يَسْتَمِعُونَ الْقَوْلَ فَيَتَّبِعُونَ أَحْسَنَهُ، اللَّهُمَّ أَسْمِعْنِي مُنَادِيَ الْجَنَّةِ فِي الْجَنَّةِ مَعَ الْأَبْرَارِ",
    "O Allah, make me of those who listen to the word and follow the best of it. O Allah, let me hear the caller of Paradise, in Paradise, with the righteous."),
   ("Neck", "Wipe the back of your neck:", "اللَّهُمَّ فُكَّ رَقَبَتِي مِنَ النَّارِ، وَأَعُوذُ بِكَ مِنَ السَّلَاسِلِ وَالْأَغْلَالِ",
    "O Allah, free my neck from the Fire. I seek refuge in You from the chains and the shackles."),
   ("Right foot", "Wash your right foot up to and including the ankle, and between the toes:", "اللَّهُمَّ ثَبِّتْ قَدَمِي عَلَى الصِّرَاطِ الْمُسْتَقِيمِ مَعَ أَقْدَامِ عِبَادِكَ الصَّالِحِينَ",
    "O Allah, make my foot firm on the straight Bridge with the feet of Your righteous servants."),
   ("Left foot", "Wash your left foot the same way:", "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ أَنْ تَزِلَّ قَدَمِي عَلَى الصِّرَاطِ فِي النَّارِ يَوْمَ تَزِلُّ أَقْدَامُ الْمُنَافِقِينَ وَالْمُشْرِكِينَ",
    "O Allah, I seek refuge in You from my foot slipping off the Bridge into the Fire, on the Day the feet of the hypocrites and idolaters slip."),
   ("When you finish", "Look up to the sky and say:", "أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ، سُبْحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، أَشْهَدُ أَنْ لَا إِلَهَ إِلَّا أَنْتَ، أَنْتَ التَّوَّابُ الرَّحِيمُ، اللَّهُمَّ اجْعَلْنِي مِنَ التَّوَّابِينَ، وَاجْعَلْنِي مِنَ الْمُتَطَهِّرِينَ، وَاجْعَلْنِي مِنْ عِبَادِكَ الصَّالِحِينَ، وَاجْعَلْنِي صَبُورًا شَكُورًا، وَاجْعَلْنِي أَذْكُرُكَ ذِكْرًا كَثِيرًا، وَأُسَبِّحُكَ بُكْرَةً وَأَصِيلًا",
    "I bear witness that there is no god but Allah alone, with no partner, and that Muhammad is His servant and Messenger. Glory and praise be to You, O Allah; I bear witness that there is no god but You; You are the Relenting, the Merciful. O Allah, make me of those who repent, of those who purify themselves, and of Your righteous servants. Make me patient and grateful, and let me remember You much and glorify You morning and evening."),
  ]},
 {"t": "The adhan and after it", "when": "When you hear the call to prayer", "src": f"{B}, the manners of entering the masjid",
  "parts": [
   ("During the adhan", "Repeat each phrase after the mu'adhdhin. At 'hayya 'ala al-salah' and 'hayya 'ala al-falah' say instead:", "لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ الْعَلِيِّ الْعَظِيمِ",
    "There is no power and no strength except by Allah, the High, the Mighty."),
   ("In the Fajr adhan", "At 'al-salatu khayrun min al-nawm' say:", "صَدَقْتَ وَبَرَرْتَ", "You have spoken truly and well."),
   ("In the iqamah", "At 'qad qamat al-salah' say:", "أَقَامَهَا اللَّهُ وَأَدَامَهَا", "May Allah establish it and keep it."),
   ("After the adhan", "When it ends, say:", "اللَّهُمَّ إِنِّي أَسْأَلُكَ عِنْدَ حُضُورِ صَلَاتِكَ، وَأَصْوَاتِ دُعَاتِكَ، وَإِدْبَارِ لَيْلِكَ، وَإِقْبَالِ نَهَارِكَ، أَنْ تُؤْتِيَ مُحَمَّدًا الْوَسِيلَةَ وَالْفَضِيلَةَ وَالدَّرَجَةَ الرَّفِيعَةَ، وَابْعَثْهُ الْمَقَامَ الْمَحْمُودَ الَّذِي وَعَدْتَهُ، إِنَّكَ لَا تُخْلِفُ الْمِيعَادَ",
    "O Allah, I ask You, at the coming of Your prayer, the voices of Your callers, the passing of Your night and the coming of Your day, to give Muhammad ﷺ the Wasilah, the excellence and the lofty rank, and raise him to the praised station You promised him. You do not break Your promise."),
  ]},
 {"t": "After the fard prayer", "when": "As soon as you finish the obligatory prayer", "src": f"{B}, the manners of entering the masjid",
  "note": "This is how al-Ghazali begins; he continues with tasbih and tahlil and then the comprehensive du'as.",
  "ar": "اللَّهُمَّ أَنْتَ السَّلَامُ، وَمِنْكَ السَّلَامُ، وَإِلَيْكَ يَعُودُ السَّلَامُ، فَحَيِّنَا رَبَّنَا بِالسَّلَامِ، وَأَدْخِلْنَا الْجَنَّةَ دَارَ السَّلَامِ، تَبَارَكْتَ يَا ذَا الْجَلَالِ وَالْإِكْرَامِ",
  "en": "O Allah, You are Peace and from You is peace, and to You peace returns. Greet us, our Lord, with peace, and admit us to Paradise, the abode of peace. Blessed are You, Possessor of Majesty and Honour."},
 {"t": "A du'a for light", "when": "After the sunnah of Fajr", "src": f"{B}, the manners of entering the masjid",
  "ar": "اللَّهُمَّ اجْعَلْ لِي نُورًا فِي قَلْبِي، وَنُورًا فِي قَبْرِي، وَنُورًا فِي سَمْعِي، وَنُورًا فِي بَصَرِي، وَنُورًا فِي شَعْرِي، وَنُورًا فِي بَشَرِي، وَنُورًا فِي لَحْمِي، وَنُورًا فِي دَمِي، وَنُورًا فِي عِظَامِي، وَنُورًا مِنْ بَيْنِ يَدَيَّ، وَنُورًا مِنْ خَلْفِي، وَنُورًا عَنْ يَمِينِي، وَنُورًا عَنْ شِمَالِي، وَنُورًا مِنْ فَوْقِي، وَنُورًا مِنْ تَحْتِي، اللَّهُمَّ زِدْنِي نُورًا، وَأَعْطِنِي نُورًا أَعْظَمَ نُورٍ، وَاجْعَلْ لِي نُورًا بِرَحْمَتِكَ يَا أَرْحَمَ الرَّاحِمِينَ",
  "en": "O Allah, place light in my heart, light in my grave, light in my hearing, light in my sight, in my hair, my skin, my flesh, my blood and my bones; light before me and behind me, on my right and my left, above me and below me. O Allah, increase me in light, give me the greatest light, and make light for me, by Your mercy, O Most Merciful of the merciful."},
 {"t": "Before sleep", "when": "Lying on your right side, facing the qiblah", "src": f"{B}, the manners of sleep",
  "note": "Then recite Ayat al-Kursi, the end of al-Baqarah, al-Ikhlas, al-Falaq, al-Nas and Tabarak (al-Mulk), and sleep in wudu.",
  "parts": [
   ("Lying down", "As you lie down:", "بِاسْمِكَ رَبِّي وَضَعْتُ جَنْبِي وَبِاسْمِكَ أَرْفَعُهُ، فَاغْفِرْ لِي ذَنْبِي، اللَّهُمَّ قِنِي عَذَابَكَ يَوْمَ تَبْعَثُ عِبَادَكَ، اللَّهُمَّ بِاسْمِكَ أَحْيَا وَأَمُوتُ",
    "In Your name, my Lord, I lay down my side and in Your name I raise it, so forgive me my sin. O Allah, protect me from Your punishment on the Day You raise Your servants. O Allah, in Your name I live and die."),
   ("Seeking protection", "Then:", "أَعُوذُ بِكَ اللَّهُمَّ مِنْ شَرِّ كُلِّ ذِي شَرٍّ، وَمِنْ شَرِّ كُلِّ دَابَّةٍ أَنْتَ آخِذٌ بِنَاصِيَتِهَا، إِنَّ رَبِّي عَلَى صِرَاطٍ مُسْتَقِيمٍ، اللَّهُمَّ أَنْتَ الْأَوَّلُ فَلَيْسَ قَبْلَكَ شَيْءٌ، وَأَنْتَ الْآخِرُ فَلَيْسَ بَعْدَكَ شَيْءٌ، وَأَنْتَ الظَّاهِرُ فَلَيْسَ فَوْقَكَ شَيْءٌ، وَأَنْتَ الْبَاطِنُ فَلَيْسَ دُونَكَ شَيْءٌ، اقْضِ عَنِّي الدَّيْنَ، وَأَغْنِنِي مِنَ الْفَقْرِ",
    "I seek refuge in You, O Allah, from the evil of every evil thing and every creature whose forelock You hold; my Lord is on a straight path. O Allah, You are the First, nothing is before You; the Last, nothing is after You; the Manifest, nothing is above You; the Hidden, nothing is beneath You. Settle my debt and free me from poverty."),
   ("Your soul", "Then:", "اللَّهُمَّ أَنْتَ خَلَقْتَ نَفْسِي وَأَنْتَ تَتَوَفَّاهَا، لَكَ مَمَاتُهَا وَمَحْيَاهَا، إِنْ أَمَتَّهَا فَاغْفِرْ لَهَا، وَإِنْ أَحْيَيْتَهَا فَاحْفَظْهَا بِمَا تَحْفَظُ بِهِ عِبَادَكَ الصَّالِحِينَ، اللَّهُمَّ إِنِّي أَسْأَلُكَ الْعَفْوَ وَالْعَافِيَةَ فِي الدِّينِ وَالدُّنْيَا وَالْآخِرَةِ",
    "O Allah, You created my soul and You take it; its death and its life are Yours. If You take it, forgive it; if You let it live, protect it as You protect Your righteous servants. O Allah, I ask You for pardon and well-being in my religion, my world and the Hereafter."),
   ("Waking for worship", "Then:", "اللَّهُمَّ أَيْقِظْنِي فِي أَحَبِّ السَّاعَاتِ إِلَيْكَ، وَاسْتَعْمِلْنِي بِأَحَبِّ الْأَعْمَالِ إِلَيْكَ، لِتُقَرِّبَنِي إِلَيْكَ زُلْفَى، وَتُبْعِدَنِي عَنْ سَخَطِكَ بُعْدًا، أَسْأَلُكَ فَتُعْطِينِي، وَأَسْتَغْفِرُكَ فَتَغْفِرُ لِي، وَأَدْعُوكَ فَتَسْتَجِيبُ لِي",
    "O Allah, wake me at the hour most beloved to You and use me in the deeds most beloved to You, to bring me near to You and far from Your displeasure. I ask and You give me; I seek forgiveness and You forgive me; I call on You and You answer me."),
  ]},
]

ABOUT = {
 "daily": {"title": "Daily du'as", "short": "Waking, sleeping, eating, wudu, leaving home",
   "about": "Short du'as the Prophet ﷺ taught for everyday moments. Imam al-Nawawi رحمه الله (d. 676 AH), the great hadith scholar, gathered them with their sources in his book al-Adhkar. Learn one at a time and say it each time that moment comes."},
 "rabbana": {"title": "The 40 Rabbana", "short": "Du'as from the Qur'an that begin 'Our Lord'",
   "about": "Forty du'as from the Qur'an that begin رَبَّنَا, 'Our Lord'. They are the words of the prophets عليهم السلام and the believers, which Allah kept in His Book. Many people read all forty after a prayer, or one a day."},
 "ghazali": {"title": "Imam al-Ghazali's du'as", "short": "A day of worship, from waking to sleep",
   "about": "Imam Abu Hamid al-Ghazali رحمه الله (d. 505 AH) is called Hujjat al-Islam, 'the Proof of Islam'. He was a Shafi'i jurist, an Ash'ari theologian and a Sufi master. In his short book Bidayat al-Hidayah ('The Beginning of Guidance') he walks a beginner through one day of worship. These are the du'as he teaches for each part of that day, in his own words."},
}
