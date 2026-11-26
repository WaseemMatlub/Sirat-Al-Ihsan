"""Salawat on the Prophet ﷺ, with where each comes from. Writes app/data/salawat.json.
Rule: say exactly where a text and its virtue come from. Hadith virtues are graded; virtues reported by the awliya'
in devotional manuals are labelled as such, not presented as hadith."""
import json, os
D = {
 "intro": "Allah and His angels send blessings on the Prophet. O you who believe, send blessings on him and greet him with peace. (al-Ahzab 56) The Prophet ﷺ said: whoever sends one blessing on me, Allah sends ten on him.",
 "introSrc": "Qur'an, al-Ahzab 56; Hadith, Sahih Muslim, Book of Prayer.",
 "items": [
  {"id": "ibrahimi", "name": "Durood Ibrahimi", "by": "Taught by the Prophet ﷺ himself",
   "ar": "اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ. اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ",
   "en": "O Allah, send blessings on Muhammad and the family of Muhammad, as You sent blessings on Ibrahim and the family of Ibrahim; You are Praiseworthy, Glorious. O Allah, bless Muhammad and the family of Muhammad, as You blessed Ibrahim and the family of Ibrahim; You are Praiseworthy, Glorious.",
   "src": "Sahih al-Bukhari (Book of the Prophets; Book of Invocations) and Sahih Muslim (Book of Prayer), from Ka'b ibn 'Ujrah رضي الله عنه, when the Companions asked how to send blessings on him.",
   "virtue": "It is the salawat recited in the final sitting of every prayer, and the form the Prophet ﷺ taught.",
   "grade": "Authentic (sahih)."},
  {"id": "ummi", "name": "Salat al-Ummi (Friday)", "by": "Recited eighty times on Friday after 'Asr",
   "ar": "اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ النَّبِيِّ الْأُمِّيِّ وَعَلَى آلِهِ وَسَلِّمْ تَسْلِيمًا",
   "en": "O Allah, send blessings on Muhammad, the unlettered Prophet, and on his family, and grant them abundant peace.",
   "src": "Reported in al-Sakhawi's al-Qawl al-Badi' fi al-Salat 'ala al-Habib al-Shafi', chapter on blessings on Friday.",
   "virtue": "It is reported that whoever says it eighty times on Friday before rising from his place after 'Asr has eighty years of sins forgiven.",
   "grade": "The chain of this report is weak; the scholars allowed acting on weak reports for virtues of good deeds."},
  {"id": "tunjina", "name": "Durood Tunjina (Salat al-Munjiyah)", "by": "The blessing that rescues",
   "ar": "اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدٍ صَلَاةً تُنْجِينَا بِهَا مِنْ جَمِيعِ الْأَهْوَالِ وَالْآفَاتِ، وَتَقْضِي لَنَا بِهَا جَمِيعَ الْحَاجَاتِ، وَتُطَهِّرُنَا بِهَا مِنْ جَمِيعِ السَّيِّئَاتِ، وَتَرْفَعُنَا بِهَا عِنْدَكَ أَعْلَى الدَّرَجَاتِ، وَتُبَلِّغُنَا بِهَا أَقْصَى الْغَايَاتِ مِنْ جَمِيعِ الْخَيْرَاتِ فِي الْحَيَاةِ وَبَعْدَ الْمَمَاتِ",
   "en": "O Allah, send blessings on our master Muhammad, a blessing by which You rescue us from all terrors and afflictions, fulfil all our needs, purify us of all wrongs, raise us to the highest ranks with You, and bring us to the utmost of every good in life and after death.",
   "src": "Related by Imam al-Fakihani رحمه الله (d. 734 AH) in al-Fajr al-Munir, from Shaykh Musa al-Darir رحمه الله, who was taught it in a dream of the Prophet ﷺ when his ship was caught in a storm; he and the passengers recited it and the storm passed. Al-Sakhawi also mentions it.",
   "virtue": "The awliya' recite it, often a thousand times, in times of fear and hardship.",
   "grade": "From the practice and experience of the righteous, not a hadith."},
  {"id": "nariyya", "name": "Salat al-Nariyya (al-Tafrijiyya)", "by": "The blessing of relief",
   "ar": "اللَّهُمَّ صَلِّ صَلَاةً كَامِلَةً وَسَلِّمْ سَلَامًا تَامًّا عَلَى سَيِّدِنَا مُحَمَّدٍ الَّذِي تَنْحَلُّ بِهِ الْعُقَدُ، وَتَنْفَرِجُ بِهِ الْكُرَبُ، وَتُقْضَى بِهِ الْحَوَائِجُ، وَتُنَالُ بِهِ الرَّغَائِبُ وَحُسْنُ الْخَوَاتِيمِ، وَيُسْتَسْقَى الْغَمَامُ بِوَجْهِهِ الْكَرِيمِ، وَعَلَى آلِهِ وَصَحْبِهِ فِي كُلِّ لَمْحَةٍ وَنَفَسٍ بِعَدَدِ كُلِّ مَعْلُومٍ لَكَ",
   "en": "O Allah, send complete blessings and perfect peace on our master Muhammad, through whom knots are untied, distress is lifted, needs are met, hopes and good endings are attained, and rain is sought by his noble face; and on his family and Companions, in every glance and breath, as many times as all that You know.",
   "src": "Attributed to Shaykh Ibrahim al-Tazi رحمه الله (d. 866 AH) of the Maghrib.",
   "virtue": "The righteous recite it 4,444 times, gathered together, when seeking relief from a hardship.",
   "grade": "From the practice of the righteous, not a hadith. Note: 'through whom' means through his rank with Allah, by Allah's leave."},
  {"id": "fatih", "name": "Salat al-Fatih", "by": "The blessing of the Opener",
   "ar": "اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدٍ الْفَاتِحِ لِمَا أُغْلِقَ، وَالْخَاتِمِ لِمَا سَبَقَ، نَاصِرِ الْحَقِّ بِالْحَقِّ، وَالْهَادِي إِلَى صِرَاطِكَ الْمُسْتَقِيمِ، وَعَلَى آلِهِ حَقَّ قَدْرِهِ وَمِقْدَارِهِ الْعَظِيمِ",
   "en": "O Allah, send blessings on our master Muhammad, the opener of what was closed, the seal of what came before, the helper of truth by the truth, the guide to Your straight path; and on his family, as befits his immense rank and worth.",
   "src": "Composed by Shaykh Muhammad ibn Abi al-Hasan al-Bakri رحمه الله (d. 952 AH) of Egypt; recited widely, especially in the Tijani path.",
   "virtue": "Its great virtues are reported by the masters of the Tijani path.",
   "grade": "From the awliya', not a hadith."},
  {"id": "taj", "name": "Durood Taj", "by": "The blessing of the Crown",
   "ar": "اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا وَمَوْلَانَا مُحَمَّدٍ صَاحِبِ التَّاجِ وَالْمِعْرَاجِ وَالْبُرَاقِ وَالْعَلَمِ، دَافِعِ الْبَلَاءِ وَالْوَبَاءِ وَالْقَحْطِ وَالْمَرَضِ وَالْأَلَمِ، اسْمُهُ مَكْتُوبٌ مَرْفُوعٌ مَشْفُوعٌ مَنْقُوشٌ فِي اللَّوْحِ وَالْقَلَمِ، سَيِّدِ الْعَرَبِ وَالْعَجَمِ، جِسْمُهُ مُقَدَّسٌ مُعَطَّرٌ مُطَهَّرٌ مُنَوَّرٌ فِي الْبَيْتِ وَالْحَرَمِ، شَمْسِ الضُّحَى بَدْرِ الدُّجَى صَدْرِ الْعُلَى نُورِ الْهُدَى كَهْفِ الْوَرَى مِصْبَاحِ الظُّلَمِ، جَمِيلِ الشِّيَمِ شَفِيعِ الْأُمَمِ صَاحِبِ الْجُودِ وَالْكَرَمِ، وَاللَّهُ عَاصِمُهُ وَجِبْرِيلُ خَادِمُهُ وَالْبُرَاقُ مَرْكَبُهُ وَالْمِعْرَاجُ سَفَرُهُ وَسِدْرَةُ الْمُنْتَهَى مَقَامُهُ وَقَابَ قَوْسَيْنِ مَطْلُوبُهُ وَالْمَطْلُوبُ مَقْصُودُهُ وَالْمَقْصُودُ مَوْجُودُهُ، سَيِّدِ الْمُرْسَلِينَ خَاتَمِ النَّبِيِّينَ شَفِيعِ الْمُذْنِبِينَ أَنِيسِ الْغَرِيبِينَ رَحْمَةٍ لِلْعَالَمِينَ رَاحَةِ الْعَاشِقِينَ مُرَادِ الْمُشْتَاقِينَ شَمْسِ الْعَارِفِينَ سِرَاجِ السَّالِكِينَ مِصْبَاحِ الْمُقَرَّبِينَ مُحِبِّ الْفُقَرَاءِ وَالْغُرَبَاءِ وَالْمَسَاكِينِ سَيِّدِ الثَّقَلَيْنِ نَبِيِّ الْحَرَمَيْنِ إِمَامِ الْقِبْلَتَيْنِ وَسِيلَتِنَا فِي الدَّارَيْنِ صَاحِبِ قَابَ قَوْسَيْنِ مَحْبُوبِ رَبِّ الْمَشْرِقَيْنِ وَالْمَغْرِبَيْنِ جَدِّ الْحَسَنِ وَالْحُسَيْنِ مَوْلَانَا وَمَوْلَى الثَّقَلَيْنِ أَبِي الْقَاسِمِ مُحَمَّدِ بْنِ عَبْدِ اللَّهِ نُورٍ مِنْ نُورِ اللَّهِ، يَا أَيُّهَا الْمُشْتَاقُونَ بِنُورِ جَمَالِهِ صَلُّوا عَلَيْهِ وَآلِهِ وَأَصْحَابِهِ وَسَلِّمُوا تَسْلِيمًا",
   "en": "O Allah, send blessings on our master and protector Muhammad, possessor of the crown, the ascension, the Buraq and the banner; the averter of affliction, plague, drought, illness and pain; whose name is written, raised, accepted in intercession and inscribed on the Tablet and by the Pen; master of the Arabs and non-Arabs; whose body is sanctified, fragrant, pure and radiant in the House and the Sanctuary; the morning sun, the full moon in darkness, the foremost in loftiness, the light of guidance, the refuge of creation, the lamp in darkness; beautiful in character, intercessor for the nations, possessor of generosity and nobility. Allah is his protector, Jibril his servant, the Buraq his mount, the ascension his journey, the Lote Tree of the Boundary his station, two bow-lengths his goal, the Sought his aim, and his aim attained. Master of the Messengers, Seal of the Prophets, intercessor for sinners, companion of strangers, mercy to the worlds, comfort of the lovers, desire of the yearning, sun of the knowers, lamp of the travellers, light of those brought near, lover of the poor, strangers and needy; master of men and jinn, Prophet of the two Sanctuaries, imam of the two qiblahs, our means in both worlds, possessor of 'two bow-lengths', beloved of the Lord of the two easts and two wests, grandfather of al-Hasan and al-Husayn, our master and the master of men and jinn, Abu al-Qasim Muhammad son of 'Abdullah, a light from the light of Allah. O you who yearn for the light of his beauty, send blessings and abundant peace on him, his family and his Companions.",
   "src": "Attributed to Shaykh Abu Bakr ibn Salim al-'Alawi رحمه الله (d. 992 AH) of Hadramawt, and widely recited in the Indian subcontinent.",
   "virtue": "Devotional manuals of the awliya' report many benefits for reciting it, such as protection and relief.",
   "grade": "From the awliya', not a hadith. Printed copies differ in a few words; this follows the most common printing. 'Averter of affliction' and 'a light from the light of Allah' are understood by the scholars of the path as by Allah's leave, and as a light created by Allah."},
  {"id": "khizri", "name": "Durood Khizri", "by": "Short and easy to repeat",
   "ar": "صَلَّى اللَّهُ عَلَى حَبِيبِهِ مُحَمَّدٍ وَآلِهِ وَسَلَّمَ",
   "en": "May Allah send blessings and peace on His beloved Muhammad and his family.",
   "src": "Attributed in devotional books to Sayyiduna al-Khidr عليه السلام; no chain is known for this.",
   "virtue": "Beloved for its shortness, so it can be said many times through the day.",
   "grade": "Its attribution has no known chain; the words themselves are sound and may be said at any time."},
 ],
 "pending": "Durood Lakhi (said in devotional manuals to equal 100,000 salawat — a virtue not found in the hadith collections) and Dala'il al-Khayrat of Imam al-Jazuli رحمه الله will be added once we have a verified printed text to copy from, so that not a letter is wrong.",
}
if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(__import__("harakat_cache").apply(D), open(os.path.join(here, "..", "app", "data", "salawat.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print("salawat", len(D["items"]))
