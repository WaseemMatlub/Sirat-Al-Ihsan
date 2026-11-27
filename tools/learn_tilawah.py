"""Reading the Qur'an: the letters, the vowel signs and the basic rules of tajweed, after al-Muqaddimah al-Jazariyyah."""
J = "al-Muqaddimah al-Jazariyyah"

def C(t, x, src, ar=None):
    d = {"t": t, "x": x, "src": src}
    if ar: d["ar"] = ar
    return d
def Q(q, a, w, why, src): return {"q": q, "a": a, "w": w, "why": why, "src": src}

LESSONS = [
 {"id": "tl_letters1", "title": "The Arabic letters (1)", "about": "Reading right to left, and the first fourteen letters.", "cards": [
   C("Right to left", "Arabic is written and read from right to left. There are 28 letters, plus the hamzah (ء). Most letters join to the letter after them, and their shape changes a little at the start, middle or end of a word.", f"{J}, the points of articulation"),
   C("Alif, ba', ta', tha'", "Alif is a straight line. Ba' has one dot below; ta' two dots above; tha' three dots above (said like 'th' in 'think').", f"{J}, the points of articulation", "ا   ب   ت   ث"),
   C("Jim, ha', kha'", "Jim has a dot inside. Ha' (ح) has no dot: a breathy 'h' from the middle of the throat. Kha' (خ) has a dot above: a rough sound from the top of the throat, like 'ch' in Scottish 'loch'.", f"{J}, the points of articulation", "ج   ح   خ"),
   C("Dal, dhal, ra', zay", "Dal is a 'd'; dhal has a dot and is said like 'th' in 'this'. Ra' is a rolled 'r'; zay has a dot and is a 'z'. These four never join to the letter after them.", f"{J}, the points of articulation", "د   ذ   ر   ز"),
   C("Sin, shin, sad, dad", "Sin is 's' and shin (three dots) is 'sh'. Sad (ص) is a heavy 's' with the tongue raised; dad (ض) is a heavy letter from the side of the tongue, found only in Arabic.", f"{J}, the points of articulation", "س   ش   ص   ض"),
  ], "checks": [
   Q("Which way is Arabic read?", "Right to left", ["Left to right", "Top to bottom", "Either way"], "The first letter of a word is on the right.", f"{J}, the points of articulation"),
   Q("Which letter has one dot below?", "ب (ba')", ["ت (ta')", "ث (tha')", "ن (nun)"], "Ba' has one dot below; ta' two above; tha' three above.", f"{J}, the points of articulation"),
   Q("Which letter is the rough sound from the top of the throat, with a dot above?", "خ (kha')", ["ح (ha')", "ج (jim)", "ه (ha')"], "Kha' has a dot above; ha' (ح) has none.", f"{J}, the points of articulation"),
   Q("Which of these letters never joins to the letter after it?", "د (dal)", ["ب (ba')", "س (sin)", "ج (jim)"], "Alif, dal, dhal, ra', zay and waw never join forward.", f"{J}, the points of articulation"),
  ]},
 {"id": "tl_letters2", "title": "The Arabic letters (2)", "about": "The second fourteen letters, and the hamzah.", "cards": [
   C("Ta', za', 'ayn, ghayn", "Ta' (ط) is a heavy 't' and za' (ظ) a heavy 'th' as in 'this'. 'Ayn (ع) is a deep sound from the middle of the throat, with no English equal; ghayn (غ), with a dot, is a gargled sound from the top of the throat.", f"{J}, the points of articulation", "ط   ظ   ع   غ"),
   C("Fa', qaf, kaf, lam", "Fa' has one dot above; qaf (ق) has two dots and is a deep 'q' from the back of the tongue; kaf (ك) is an ordinary 'k'. Lam is 'l'.", f"{J}, the points of articulation", "ف   ق   ك   ل"),
   C("Mim, nun, ha', waw, ya'", "Mim is 'm' and nun 'n'. This ha' (ه) is a light 'h' from the deepest part of the throat. Waw is 'w' and ya' is 'y'.", f"{J}, the points of articulation", "م   ن   ه   و   ي"),
   C("The hamzah", "The hamzah (ء) is a short catch in the throat, like the break in 'uh-oh'. It often sits on an alif, waw or ya'.", f"{J}, the points of articulation", "ء   أ   ؤ   ئ"),
   C("Shapes in a word", "Each letter changes a little depending on where it is. Ba' at the start, middle and end of a word:", f"{J}, the points of articulation", "بـ   ـبـ   ـب"),
  ], "checks": [
   Q("Which letter is the deep throat sound with no English equal?", "ع ('ayn)", ["ء (hamzah)", "ه (ha')", "غ (ghayn)"], "'Ayn comes from the middle of the throat; mixing it with the hamzah changes words.", f"{J}, the points of articulation"),
   Q("Which is the deep 'q' from the back of the tongue?", "ق (qaf)", ["ك (kaf)", "ف (fa')", "غ (ghayn)"], "Qaf is heavy and deep; kaf is light.", f"{J}, the points of articulation"),
   Q("Which is the light 'h' from the deepest part of the throat?", "ه", ["ح", "خ", "ع"], "ه is light and airy; ح is breathier, from the middle of the throat.", f"{J}, the points of articulation"),
   Q("How many letters are in the Arabic alphabet?", "28, with the hamzah besides", ["26", "30", "22"], "Twenty-eight letters, and the hamzah.", f"{J}, the points of articulation"),
  ]},
 {"id": "tl_harakat", "title": "Vowels and signs", "about": "The short vowels, sukun, shaddah, tanween and the long vowels.", "cards": [
   C("Three short vowels", "Fathah (a line above) is a short 'a'; kasrah (a line below) a short 'i'; dammah (a small waw above) a short 'u'.", f"{J}, the points of articulation", "بَ   بِ   بُ"),
   C("Sukun", "A small circle above means the letter has no vowel: it closes the syllable. أَبْ is read 'ab'.", f"{J}, the points of articulation", "أَبْ"),
   C("Shaddah", "A shaddah (like a small 'w') doubles the letter: it is read once closed and once open. رَبِّ is 'rab-bi'. Missing a shaddah can change the meaning.", f"{J}, the points of articulation", "رَبِّ"),
   C("Tanween", "A doubled vowel at the end of a word adds an 'n' sound: -an, -in, -un.", f"{J}, rulings of nun sakinah and tanween", "بًا   بٍ   بٌ"),
   C("The long vowels", "Alif after a fathah, ya' after a kasrah and waw after a dammah lengthen the vowel for two counts: baa, bii, buu. These are the letters of madd.", f"{J}, lengthening and shortening", "بَا   بِي   بُو"),
  ], "checks": [
   Q("A small circle above a letter (sukun) means…", "The letter has no vowel", ["Say it twice", "Make it long", "Say it heavily"], "Sukun closes the syllable, as in أَبْ (ab).", f"{J}, the points of articulation"),
   Q("What does a shaddah do?", "Doubles the letter", ["Makes it silent", "Adds an 'n'", "Makes it long"], "رَبِّ is read rab-bi.", f"{J}, the points of articulation"),
   Q("How is بُو read?", "buu, held for two counts", ["bu, short", "bi", "ba"], "Waw after a dammah lengthens the 'u'.", f"{J}, lengthening and shortening"),
   Q("Tanween adds which sound at the end of a word?", "An 'n' sound", ["An 'm' sound", "A long 'a'", "Nothing"], "-an, -in, -un.", f"{J}, rulings of nun sakinah and tanween"),
  ]},
 {"id": "tl_makharij", "title": "Where the letters come from", "about": "The points of articulation, the heavy letters, and the mistakes that change meaning.", "cards": [
   C("Seventeen points", "Ibn al-Jazari counts seventeen points of articulation, in five areas: the empty space of the mouth and throat (the long vowels), the throat, the tongue, the lips, and the nose (for ghunnah).", f"{J}, the points of articulation"),
   C("The throat", "Hamzah and ha' (ه) from the deepest part; 'ayn and ha' (ح) from the middle; ghayn and kha' from the top.", f"{J}, the points of articulation", "ء ه   ع ح   غ خ"),
   C("The lips", "Fa' from the inside of the lower lip with the upper teeth; ba', mim and waw from the two lips.", f"{J}, the points of articulation", "ف   ب م و"),
   C("The heavy letters", "Seven letters are always said heavy, with the back of the tongue raised. They are gathered in the phrase khuss daghtin qiz. All other letters are light, except ra' and the lam of 'Allah' at times.", f"{J}, the qualities of the letters", "خُصَّ ضَغْطٍ قِظْ"),
   C("Mistakes that change meaning", "Mixing ح and ه, ع and ء, ق and ك, or س and ص changes the word. قَلْبٌ is 'heart' but كَلْبٌ is 'dog'. Practise these pairs with a teacher.", f"{J}, the qualities of the letters", "قَلْبٌ   كَلْبٌ"),
  ], "checks": [
   Q("How many points of articulation does Ibn al-Jazari count?", "Seventeen", ["Five", "Twenty-eight", "Seven"], "Seventeen points, in five areas.", f"{J}, the points of articulation"),
   Q("Which letters come from the middle of the throat?", "ع and ح", ["ء and ه", "غ and خ", "ق and ك"], "Deepest: ء ه; middle: ع ح; top: غ خ.", f"{J}, the points of articulation"),
   Q("Which phrase gathers the seven always-heavy letters?", "خُصَّ ضَغْطٍ قِظْ (khuss daghtin qiz)", ["يَرْمَلُونَ (yarmalun)", "قُطْبُ جَدٍّ (qutbu jadd)", "بَمَو (bamaw)"], "Kha', sad, dad, ghayn, ta', qaf, za'.", f"{J}, the qualities of the letters"),
   Q("Saying كَلْب instead of قَلْب changes 'heart' to…", "'dog'", ["'heart' still", "'mind'", "Nothing changes"], "The point of articulation matters for meaning.", f"{J}, the qualities of the letters"),
  ]},
 {"id": "tl_nun", "title": "Nun sakinah and tanween", "about": "The four rules for a nun with sukun, or tanween.", "cards": [
   C("Clear (izhar)", "Before the six throat letters (ء ه ع ح غ خ) the nun is said clearly, with no ghunnah.", f"{J}, rulings of nun sakinah and tanween", "مَنْ آمَنَ"),
   C("Merging (idgham)", "Before the letters of yarmalun (ي ر م ل و ن) the nun merges into the next letter: with ghunnah into ي ن م و, and without it into ل and ر. It only happens across two words.", f"{J}, rulings of nun sakinah and tanween", "مِنْ رَبِّهِمْ   مَنْ يَقُولُ"),
   C("Changing (iqlab)", "Before ba' the nun turns into a hidden mim, with ghunnah: مِنْ بَعْدِ is read 'mim ba'di'.", f"{J}, rulings of nun sakinah and tanween", "مِنْ بَعْدِ"),
   C("Hiding (ikhfa')", "Before the other fifteen letters the nun is hidden: said lightly through the nose with ghunnah, the tongue not touching its point.", f"{J}, rulings of nun sakinah and tanween", "أَنْتُمْ   مِنْ قَبْلِ"),
   C("The ghunnah", "Ghunnah is the sound from the nose, held for about two counts. It is also always there in a nun or mim with shaddah: إِنَّ, ثُمَّ.", f"{J}, the doubled nun and mim", "إِنَّ   ثُمَّ"),
  ], "checks": [
   Q("A nun sakinah comes before ع. Which rule applies?", "Izhar: say it clearly", ["Idgham", "Iqlab", "Ikhfa'"], "Before the six throat letters the nun is clear.", f"{J}, rulings of nun sakinah and tanween"),
   Q("How is مِنْ بَعْدِ read?", "Mim ba'di: the nun turns into a hidden mim", ["Min ba'di, clearly", "Mib-ba'di, merged", "Mi ba'di, no nun"], "This is iqlab, before ba'.", f"{J}, rulings of nun sakinah and tanween"),
   Q("Into which letters does the nun merge without ghunnah?", "ل and ر", ["ي and و", "م and ن", "ب and ف"], "With ghunnah: ي ن م و; without: ل ر.", f"{J}, rulings of nun sakinah and tanween"),
   Q("How long is a ghunnah held?", "About two counts", ["Six counts", "No time at all", "As long as one breath"], "Two counts, as in إِنَّ and ثُمَّ.", f"{J}, the doubled nun and mim"),
  ]},
 {"id": "tl_meem", "title": "Mim sakinah", "about": "The three rules for a mim with sukun.", "cards": [
   C("Hidden before ba'", "A mim sakinah before ba' is hidden with ghunnah, the lips closing lightly (ikhfa' shafawi).", f"{J}, the doubled nun and mim", "تَرْمِيهِمْ بِحِجَارَةٍ"),
   C("Merged before mim", "A mim sakinah before another mim merges into it with ghunnah.", f"{J}, the doubled nun and mim", "لَهُمْ مَا"),
   C("Clear before the rest", "Before every other letter the mim is said clearly, taking special care before fa' and waw.", f"{J}, the doubled nun and mim", "أَنْعَمْتَ"),
  ], "checks": [
   Q("A mim sakinah before ba' is…", "Hidden with ghunnah", ["Said clearly", "Dropped", "Turned into nun"], "This is ikhfa' shafawi.", f"{J}, the doubled nun and mim"),
   Q("In أَنْعَمْتَ the mim is…", "Said clearly", ["Hidden", "Merged", "Silent"], "Before any letter but ب and م, the mim is clear.", f"{J}, the doubled nun and mim"),
   Q("A mim sakinah before another mim…", "Merges into it with ghunnah", ["Is said clearly", "Is hidden", "Becomes a nun"], "As in لَهُمْ مَا.", f"{J}, the doubled nun and mim"),
  ]},
 {"id": "tl_madd", "title": "Lengthening (madd)", "about": "How long to hold the long vowels.", "cards": [
   C("Natural madd", "A long vowel with no hamzah or sukun after it is held two counts. This is the base of all madd.", f"{J}, lengthening and shortening", "قَالَ"),
   C("Joined madd", "When a hamzah follows the long vowel in the same word, lengthening is obligatory: four or five counts.", f"{J}, lengthening and shortening", "جَاءَ   السَّمَاءِ"),
   C("Separated madd", "When the hamzah begins the next word, lengthen four or five counts in the reading of Hafs from 'Asim (the most common).", f"{J}, lengthening and shortening", "إِنَّا أَعْطَيْنَاكَ"),
   C("Necessary madd", "When a shaddah or fixed sukun follows the long vowel, hold it six counts.", f"{J}, lengthening and shortening", "الضَّالِّينَ"),
   C("Stopping", "When you stop on a word after a long vowel, you may hold it two, four or six counts.", f"{J}, stopping and starting", "الرَّحِيمْ"),
  ], "checks": [
   Q("How long is a natural madd?", "Two counts", ["Six counts", "Four counts", "One count"], "Two counts is the base.", f"{J}, lengthening and shortening"),
   Q("How long is the madd in الضَّالِّينَ?", "Six counts", ["Two counts", "Four counts", "None"], "A shaddah follows the long vowel: necessary madd, six counts.", f"{J}, lengthening and shortening"),
   Q("In جَاءَ the hamzah follows the long vowel in the same word. The madd is…", "Obligatory, four or five counts", ["Two counts only", "Not lengthened", "Six counts only"], "This is the joined madd.", f"{J}, lengthening and shortening"),
  ]},
 {"id": "tl_more", "title": "Qalqalah, ra' and the lam of Allah", "about": "The echo letters, and when ra' and lam are heavy.", "cards": [
   C("Qalqalah", "The five letters of qutbu jadd (ق ط ب ج د) are given a slight bounce when they have a sukun, strongest when you stop on them.", f"{J}, the qualities of the letters", "أَحَدْ   يَخْلُقْ"),
   C("The lam of 'Allah'", "The lam in the name 'Allah' is heavy after a fathah or dammah, and light after a kasrah.", f"{J}, the lams", "قَالَ اللَّهُ   بِسْمِ اللَّهِ"),
   C("Ra'", "Ra' is heavy with a fathah or dammah, and light with a kasrah.", f"{J}, the ra's", "رَبِّ   رِزْقًا"),
   C("Where to stop", "Stop where the meaning is complete, at the end of a verse if you can, and stop with a sukun on the last letter. Do not start again from a place that changes the meaning.", f"{J}, stopping and starting"),
  ], "checks": [
   Q("Which letters have qalqalah?", "ق ط ب ج د (qutbu jadd)", ["ي ر م ل و ن", "ء ه ع ح غ خ", "خ ص ض غ ط ق ظ"], "They bounce when they have a sukun.", f"{J}, the qualities of the letters"),
   Q("In بِسْمِ اللَّهِ the lam of 'Allah' is…", "Light, after a kasrah", ["Heavy", "Silent", "Doubled twice"], "Heavy after a fathah or dammah; light after a kasrah.", f"{J}, the lams"),
   Q("Ra' with a kasrah is…", "Light", ["Heavy", "Silent", "Bounced"], "Ra' is light with a kasrah, heavy with a fathah or dammah.", f"{J}, the ra's"),
  ]},
 {"id": "tl_fatihah", "title": "Reciting al-Fatihah correctly", "about": "Putting it all together for the surah you recite in every rak'ah.", "cards": [
   C("Tajweed is a duty", "Ibn al-Jazari says applying tajweed is an obligation: whoever does not recite the Qur'an correctly is sinful. At the least, every Muslim must avoid clear mistakes that change letters, vowels or meaning, especially in al-Fatihah.", f"{J}, tajweed"),
   C("Watch the letters", "Say ح in al-hamdu (not ه), ع in al-'alamin (not ء), ص in al-sirat, and ض in al-dallin with its six-count madd.", f"{J}, the qualities of the letters", "الْحَمْدُ   الْعَالَمِينَ   الصِّرَاطَ   الضَّالِّينَ"),
   C("Keep the shaddahs", "Al-Fatihah with the basmalah has fourteen shaddahs. In إِيَّاكَ, dropping the shaddah changes the meaning entirely, so press on it.", f"{J}, tajweed", "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"),
   C("Learn by listening", "Tajweed is taken from a teacher by ear. Recite al-Fatihah to someone who knows, ask them to correct you, and listen to a sound reciter daily.", f"{J}, conclusion"),
  ], "checks": [
   Q("According to Ibn al-Jazari, applying tajweed is…", "An obligation", ["Only for imams", "Only recommended", "Only for Arabs"], "He calls it a binding obligation.", f"{J}, tajweed"),
   Q("Which letter begins al-hamdu in al-Fatihah?", "ح, the breathy throat letter", ["ه, the light h", "خ", "ع"], "ح and ه are different letters.", f"{J}, the qualities of the letters"),
   Q("How many shaddahs are in al-Fatihah with the basmalah?", "Fourteen", ["Four", "Seven", "Twenty"], "Leaving one out is a clear mistake.", f"{J}, tajweed"),
   Q("What is the best way to learn tajweed?", "Reciting to a teacher who corrects you", ["Reading about it only", "Guessing from the writing", "Reciting fast"], "Tajweed is taken by hearing.", f"{J}, conclusion"),
  ]},
]
COURSE = {"id": "tilawah", "title": "Reading the Qur'an: letters and tajweed", "ar": "التِّلَاوَةُ وَالتَّجْوِيدُ",
  "sub": "The Arabic letters, vowel signs and the basic rules of tajweed", "book": "al-Muqaddimah al-Jazariyyah of Ibn al-Jazari", "color": "#2D6A6A", "lessons": LESSONS}
