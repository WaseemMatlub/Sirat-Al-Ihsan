"""Third pass on the basics: so that a student who finishes them knows their Fard al-'Ayn, can hold their own,
and can pass it on. Adds the Companions and Ahl al-Bayt, the adab of daily life, and more of the Seerah.
Each lesson: (id, title, about, [cards (title, text, source)], [questions (q, answer, [3 wrong], why, source)])."""
FU = "al-Fusul fi Sirat al-Rasul"
TK = "Tarikh al-Khulafa'"
TH = "al-'Aqidah al-Tahawiyyah"
BH = "Bidayat al-Hidayah"
AD = "al-Adhkar"
RS = "Riyad al-Salihin"

SEERAH_MORE = [  # (insert after, lesson)
 ("sr3", ("sr_sorrow", "The Year of Sorrow and Ta'if", "Losing Khadijah and Abu Talib, and the journey to Ta'if.", [
   ("The Year of Sorrow", "In the tenth year of prophethood, Khadijah رَضِيَ اللَّهُ عَنْهَا and his uncle Abu Talib died within a short time of each other. Quraysh's harm grew, and that year was called the Year of Sorrow.", f"{FU}, the death of Abu Talib and Khadijah"),
   ("Ta'if", "He ﷺ went to Ta'if to call its people to Islam. They rejected him and set their children and slaves on him, throwing stones until his feet bled.", f"{FU}, the journey to Ta'if"),
   ("His mercy", "The angel of the mountains offered to crush the town between two mountains. He ﷺ said: rather, I hope Allah will bring from their descendants people who worship Allah alone.", "Sahih al-Bukhari, Book of the Beginning of Creation"),
  ], [
   ("Why is the tenth year of prophethood called the Year of Sorrow?", "Khadijah and Abu Talib both died that year", ["The Muslims were driven from Makkah", "The Battle of Uhud was lost", "Revelation stopped for a year"], "He ﷺ lost his wife and his protector within a short time.", FU),
   ("How did the people of Ta'if receive the Prophet ﷺ?", "They rejected him and stoned him until his feet bled", ["They accepted Islam at once", "They gave him shelter for a year", "They ignored him politely"], "Yet he ﷺ did not curse them.", FU),
   ("When offered to have Ta'if destroyed, what did he ﷺ say?", "He hoped their descendants would worship Allah", ["Yes, destroy them", "Wait one more year", "Destroy only their leaders"], "A lesson in mercy and patience in calling to Allah.", "Sahih al-Bukhari"),
  ])),
 ("sr_sorrow", ("sr_aqabah", "The pledges of 'Aqabah", "How Madinah opened its doors to Islam.", [
   ("The first pledge", "At Hajj, twelve men from Yathrib (Madinah) met him ﷺ at 'Aqabah and pledged to worship Allah alone, not steal, not commit zina and not kill their children. He sent Mus'ab ibn 'Umayr رَضِيَ اللَّهُ عَنْهُ with them to teach.", f"{FU}, the first 'Aqabah"),
   ("The second pledge", "The next year, seventy-three men and two women pledged to protect him ﷺ as they protected their own families. This opened the way to the Hijrah.", f"{FU}, the second 'Aqabah"),
  ], [
   ("Who did the Prophet ﷺ send to Madinah to teach after the first pledge?", "Mus'ab ibn 'Umayr رَضِيَ اللَّهُ عَنْهُ", ["Abu Bakr رَضِيَ اللَّهُ عَنْهُ", "Bilal رَضِيَ اللَّهُ عَنْهُ", "'Ali رَضِيَ اللَّهُ عَنْهُ"], "He was the first teacher sent out in Islam.", FU),
   ("What did the people of Madinah pledge at the second 'Aqabah?", "To protect him ﷺ as they protected their own families", ["To fight Quraysh at once", "To move to Makkah", "To pay him a yearly tax"], "This pledge opened the way to the Hijrah.", FU),
   ("Where did the pledges of 'Aqabah take place?", "At 'Aqabah near Mina, during the Hajj season", ["In Madinah", "In Ta'if", "In the Cave of Hira'"], "The Prophet ﷺ met the tribes when they came for Hajj.", FU),
  ])),
 ("sr_aqabah", None),  # placeholder kept for ordering clarity
 ("sr4", None),
 ("sr4", ("sr_madinah", "Building Madinah", "The masjid, the brotherhood, and a new community.", [
   ("The masjid", "On arriving in Madinah he ﷺ built his masjid, working with his own hands, carrying bricks with the Companions. It was the centre of worship, learning and community.", f"{FU}, building the masjid"),
   ("The brotherhood", "He ﷺ joined each Muhajir (emigrant from Makkah) with an Ansari (helper from Madinah) as brothers. The Ansar shared their homes and wealth with them.", f"{FU}, the brotherhood"),
   ("The adhan", "The adhan was given its words after 'Abdullah ibn Zayd رَضِيَ اللَّهُ عَنْهُ saw it in a dream, and Bilal رَضِيَ اللَّهُ عَنْهُ, with his beautiful voice, became the first mu'adhdhin.", "Sunan Abi Dawud, Book of Prayer"),
  ], [
   ("What was the first thing the Prophet ﷺ built in Madinah?", "His masjid", ["A fort", "A market", "His own house"], "He ﷺ carried bricks with the Companions himself.", FU),
   ("Who were the Ansar?", "The Muslims of Madinah who helped the emigrants", ["The emigrants from Makkah", "The Prophet's family", "The people of Ta'if"], "Ansar means helpers; the Muhajirun were the emigrants.", FU),
   ("Who was the first mu'adhdhin?", "Bilal رَضِيَ اللَّهُ عَنْهُ", ["Abu Bakr رَضِيَ اللَّهُ عَنْهُ", "'Abdullah ibn Zayd رَضِيَ اللَّهُ عَنْهُ", "'Umar رَضِيَ اللَّهُ عَنْهُ"], "'Abdullah ibn Zayd saw the words in a dream; Bilal called it.", "Sunan Abi Dawud"),
  ])),
 ("sr5", ("sr_hudaybiyah", "Hudaybiyah and Khaybar", "A treaty that looked like a loss, and was a clear victory.", [
   ("The treaty", "In 6 AH the Prophet ﷺ set out for 'umrah with about 1,400 Companions. Quraysh blocked him at al-Hudaybiyah, and a ten-year peace treaty was made. Its terms seemed hard on the Muslims.", f"{FU}, al-Hudaybiyah"),
   ("The pledge under the tree", "When it was rumoured that 'Uthman رَضِيَ اللَّهُ عَنْهُ had been killed, the Companions pledged to stand firm. Allah said He was pleased with them: the Pledge of Ridwan.", "Qur'an, al-Fath 18"),
   ("A clear victory", "Allah called the treaty 'a clear victory'. In the peace, Islam spread faster than ever, and Khaybar was taken soon after.", "Qur'an, al-Fath 1"),
  ], [
   ("What did Allah call the Treaty of Hudaybiyah?", "A clear victory", ["A defeat", "A mistake", "A test only"], "'Indeed, We have given you a clear victory.' (al-Fath 1)", "Qur'an"),
   ("Why did the Companions make the Pledge of Ridwan?", "It was rumoured that 'Uthman رَضِيَ اللَّهُ عَنْهُ had been killed", ["To elect a caliph", "To begin the conquest of Makkah", "To leave for Abyssinia"], "Allah said He was pleased with those who pledged under the tree.", "Qur'an, al-Fath 18"),
   ("Why had the Prophet ﷺ set out for Makkah that year?", "To perform 'umrah", ["To fight Quraysh", "To perform Hajj", "To trade"], "He went in ihram with the sacrificial animals, intending peace.", FU),
  ])),
 ("sr6", ("sr_farewell", "The Farewell Hajj", "His only Hajj ﷺ, and his last sermon.", [
   ("His Hajj", "In 10 AH the Prophet ﷺ performed Hajj with over a hundred thousand Companions. It was his only Hajj, and he taught them its rites, saying: take your rites from me.", "Sahih Muslim, Book of Hajj"),
   ("The sermon at 'Arafah", "He ﷺ said your blood, wealth and honour are sacred to one another, ended the feuds and riba of the Days of Ignorance, urged kindness to women, and left them the Book of Allah.", "Sahih Muslim, Book of Hajj"),
   ("The religion completed", "At 'Arafah the verse came down: 'Today I have perfected your religion for you, completed My favour upon you, and chosen Islam as your religion.'", "Qur'an, al-Ma'idah 3"),
  ], [
   ("How many times did the Prophet ﷺ perform Hajj after the Hijrah?", "Once, in 10 AH", ["Every year", "Twice", "Never"], "It is called the Farewell Hajj.", "Sahih Muslim"),
   ("What did he ﷺ declare sacred in the Farewell Sermon?", "People's blood, wealth and honour", ["Only the Ka'bah", "Only the month of Ramadan", "Only Makkah and Madinah"], "Sacred as that day, that month and that land.", "Sahih Muslim"),
   ("Which verse came down at 'Arafah during the Farewell Hajj?", "'Today I have perfected your religion for you'", ["'Read in the name of your Lord'", "'Say: He is Allah, One'", "'And establish the prayer'"], "Al-Ma'idah 3.", "Qur'an"),
  ])),
 ("sr_farewell", ("sr_passing", "His passing ﷺ", "The last days, and how the Companions held firm.", [
   ("His illness", "In Rabi' al-Awwal 11 AH he ﷺ fell ill. He asked to be nursed in the room of 'A'ishah رَضِيَ اللَّهُ عَنْهَا and told Abu Bakr رَضِيَ اللَّهُ عَنْهُ to lead the people in prayer.", f"{FU}, his illness"),
   ("His last words", "His last advice included the prayer and kindness to those under your care. He ﷺ passed away on a Monday, aged sixty-three, saying: 'With the highest companion.'", "Sahih al-Bukhari, Book of Military Expeditions"),
   ("Abu Bakr's words", "When some could not believe it, Abu Bakr رَضِيَ اللَّهُ عَنْهُ said: whoever worshipped Muhammad, Muhammad has died; whoever worships Allah, Allah is Ever-Living and never dies. Then he recited Al 'Imran 144.", "Sahih al-Bukhari, Book of Military Expeditions"),
  ], [
   ("How old was the Prophet ﷺ when he passed away?", "Sixty-three", ["Forty", "Seventy", "Fifty-three"], "He ﷺ received revelation at forty and lived twenty-three years after.", FU),
   ("Whom did he ﷺ tell to lead the prayer during his final illness?", "Abu Bakr رَضِيَ اللَّهُ عَنْهُ", ["'Umar رَضِيَ اللَّهُ عَنْهُ", "'Ali رَضِيَ اللَّهُ عَنْهُ", "Bilal رَضِيَ اللَّهُ عَنْهُ"], "The Companions saw this as a sign of Abu Bakr's precedence.", FU),
   ("What did Abu Bakr رَضِيَ اللَّهُ عَنْهُ remind the people when the Prophet ﷺ passed away?", "Allah is Ever-Living and never dies", ["The Prophet ﷺ would return", "They should leave Madinah", "Nothing; he stayed silent"], "Whoever worships Allah, Allah is Ever-Living and never dies.", "Sahih al-Bukhari"),
  ])),
]
SEERAH_MORE = [x for x in SEERAH_MORE if x[1]]

SAHABAH = {"id":"sahabah", "title":"The Companions and Ahl al-Bayt", "ar":"الصَّحَابَةُ وَآلُ الْبَيْتِ",
 "sub":"The four caliphs, the ten, the Mothers of the Believers and the Prophet's family ﷺ",
 "book":"Tarikh al-Khulafa' and al-'Aqidah al-Tahawiyyah", "color":"#6B4E2E", "lessons":[
 ("sh_who", "Who the Companions are", "Their rank, and why we love them.", [
   ("Who they are", "A Companion (sahabi) is someone who met the Prophet ﷺ as a believer and died as a Muslim. They carried the Qur'an and the Sunnah to us.", f"{TH}, the Companions"),
   ("Their rank", "The Prophet ﷺ said: the best of people are my generation, then those after them, then those after them. Allah said He is pleased with the foremost Muhajirun and Ansar, and those who follow them in excellence.", "Qur'an, al-Tawbah 100"),
   ("Our way with them", "We love them all, go to excess about none of them, disown none, speak of them only with good, and keep silent about the disputes between them. Loving them is religion and faith; hating them is disbelief, hypocrisy and transgression.", f"{TH}, the Companions"),
  ], [
   ("Who counts as a Companion (sahabi)?", "One who met the Prophet ﷺ as a believer and died Muslim", ["Anyone who lived in his time", "Only those who fought at Badr", "Only his family"], "Even a brief meeting as a believer is enough.", TH),
   ("Which generation did the Prophet ﷺ call the best of people?", "His own generation", ["The last generation", "The generation of 'Isa عَلَيْهِ السَّلَامُ", "Every generation equally"], "Then those after them, then those after them.", "Sahih al-Bukhari"),
   ("How does Imam al-Tahawi say we speak about the disputes between the Companions?", "We keep silent and speak of them only with good", ["We take sides", "We judge who was right", "We avoid mentioning any Companion"], "They were people of excellence; Allah will judge between them.", TH),
   ("Loving the Companions is, according to al-Tahawi…", "Part of religion and faith", ["Optional", "Only for scholars", "A cultural custom"], "And hating them is disbelief, hypocrisy and transgression.", TH),
 ]),
 ("sh_abubakr", "Abu Bakr al-Siddiq رَضِيَ اللَّهُ عَنْهُ", "The first caliph, and the best of the Ummah after its Prophet ﷺ.", [
   ("The truthful", "'Abdullah ibn Abi Quhafah, the first free man to believe. He was called al-Siddiq (the truthful) for affirming the Night Journey at once: 'If he said it, then it is true.'", f"{TK}, Abu Bakr"),
   ("Companion of the Cave", "He accompanied the Prophet ﷺ on the Hijrah and hid with him in the Cave of Thawr. Allah mentions him: 'the second of two, when they were in the cave.'", "Qur'an, al-Tawbah 40"),
   ("His caliphate", "He was caliph for about two years. He stood firm against those who refused zakat and against the false prophets, and began the gathering of the Qur'an into one volume.", f"{TK}, Abu Bakr"),
  ], [
   ("Why was Abu Bakr رَضِيَ اللَّهُ عَنْهُ called al-Siddiq?", "For affirming the Prophet ﷺ at once, as with the Night Journey", ["For his wealth", "For his bravery in battle", "For his age"], "'If he said it, then it is true.'", TK),
   ("Who was with the Prophet ﷺ in the Cave of Thawr?", "Abu Bakr رَضِيَ اللَّهُ عَنْهُ", ["'Umar رَضِيَ اللَّهُ عَنْهُ", "'Ali رَضِيَ اللَّهُ عَنْهُ", "Bilal رَضِيَ اللَّهُ عَنْهُ"], "'The second of two, when they were in the cave.' (al-Tawbah 40)", "Qur'an"),
   ("What did Abu Bakr رَضِيَ اللَّهُ عَنْهُ begin during his caliphate?", "Gathering the Qur'an into one volume", ["Building the Dome of the Rock", "Conquering Spain", "Writing the hadith books"], "Zayd ibn Thabit رَضِيَ اللَّهُ عَنْهُ gathered it at his command.", TK),
   ("Who is the best of this Ummah after the Prophet ﷺ, according to Ahl al-Sunnah?", "Abu Bakr, then 'Umar, then 'Uthman, then 'Ali", ["'Ali, then Abu Bakr", "All four equally", "'Umar, then Abu Bakr"], "The order of their caliphate is the order of their excellence.", TH),
 ]),
 ("sh_umar", "'Umar ibn al-Khattab رَضِيَ اللَّهُ عَنْهُ", "Al-Faruq, the second caliph.", [
   ("His Islam", "His acceptance of Islam was a great strength for the Muslims; after it they prayed openly at the Ka'bah. He was named al-Faruq, the one who separates truth from falsehood.", f"{TK}, 'Umar"),
   ("His justice", "Caliph for ten years, he was known for justice and fearing Allah. Under him Syria, Iraq, Persia and Egypt opened, and Jerusalem was received peacefully.", f"{TK}, 'Umar"),
   ("What he began", "He began the Hijri calendar, gathered the people for tarawih behind one imam, and set up the public treasury and offices. He was martyred while leading the Fajr prayer.", f"{TK}, 'Umar"),
  ], [
   ("What title was 'Umar رَضِيَ اللَّهُ عَنْهُ given?", "Al-Faruq", ["Al-Siddiq", "Dhu al-Nurayn", "Asad Allah"], "The one who separates truth from falsehood.", TK),
   ("Which calendar did 'Umar رَضِيَ اللَّهُ عَنْهُ begin?", "The Hijri calendar", ["The solar calendar", "The Roman calendar", "No calendar"], "Counting from the Hijrah of the Prophet ﷺ.", TK),
   ("How was 'Umar رَضِيَ اللَّهُ عَنْهُ martyred?", "Stabbed while leading the Fajr prayer", ["In the Battle of Yarmuk", "By poison", "He died of old age"], "He was stabbed by Abu Lu'lu'ah in the masjid.", TK),
   ("Which city was received peacefully in 'Umar's caliphate?", "Jerusalem", ["Makkah", "Baghdad", "Cordoba"], "'Umar رَضِيَ اللَّهُ عَنْهُ travelled to receive it himself.", TK),
 ]),
 ("sh_uthman", "'Uthman ibn 'Affan رَضِيَ اللَّهُ عَنْهُ", "Dhu al-Nurayn, the third caliph.", [
   ("Possessor of two lights", "He married two daughters of the Prophet ﷺ, Ruqayyah and then Umm Kulthum رَضِيَ اللَّهُ عَنْهُمَا, and was called Dhu al-Nurayn, the possessor of two lights. He was known for his modesty; even the angels were shy of him.", f"{TK}, 'Uthman"),
   ("His generosity", "He bought the well of Rumah for the Muslims and equipped the army of Tabuk from his own wealth.", f"{TK}, 'Uthman"),
   ("The one copy", "As caliph for twelve years, he had the Qur'an copied in one standard text from Abu Bakr's volume and sent to the cities. He was martyred in his house while reading the Qur'an.", f"{TK}, 'Uthman"),
  ], [
   ("Why was 'Uthman رَضِيَ اللَّهُ عَنْهُ called Dhu al-Nurayn?", "He married two daughters of the Prophet ﷺ", ["He had a shining face", "He memorised two scriptures", "He was born at dawn"], "Ruqayyah, then after her death Umm Kulthum رَضِيَ اللَّهُ عَنْهُمَا.", TK),
   ("What did 'Uthman رَضِيَ اللَّهُ عَنْهُ do with the Qur'an?", "Had standard copies made and sent to the cities", ["First gathered it into one volume", "Added vowel marks", "Translated it"], "Abu Bakr gathered it; 'Uthman made the standard copies.", TK),
   ("Which quality was 'Uthman رَضِيَ اللَّهُ عَنْهُ especially known for?", "Modesty (haya')", ["Anger", "Poetry", "Wrestling"], "The Prophet ﷺ said: shall I not be shy of a man of whom the angels are shy?", "Sahih Muslim"),
 ]),
 ("sh_ali", "'Ali ibn Abi Talib رَضِيَ اللَّهُ عَنْهُ", "The fourth caliph, the Prophet's cousin and son-in-law.", [
   ("Close to the Prophet ﷺ", "He was raised in the Prophet's home and was the first child to accept Islam. He slept in the Prophet's bed on the night of the Hijrah, and married Fatimah رَضِيَ اللَّهُ عَنْهَا.", f"{TK}, 'Ali"),
   ("His knowledge and courage", "The Prophet ﷺ said to him: you are to me as Harun was to Musa, except there is no prophet after me. At Khaybar he was given the banner and the fort was opened at his hands.", "Sahih al-Bukhari, Virtues of the Companions"),
   ("His caliphate", "He was caliph for about five years in a time of trials, and was martyred in Kufah on his way to Fajr. Many chains of the Sufis and scholars go back through him.", f"{TK}, 'Ali"),
  ], [
   ("Who slept in the Prophet's bed on the night of the Hijrah?", "'Ali رَضِيَ اللَّهُ عَنْهُ", ["Abu Bakr رَضِيَ اللَّهُ عَنْهُ", "Zayd ibn Harithah رَضِيَ اللَّهُ عَنْهُ", "'Umar رَضِيَ اللَّهُ عَنْهُ"], "He risked his life so the Prophet ﷺ could leave safely.", TK),
   ("The Prophet ﷺ told 'Ali: you are to me as … was to Musa.", "Harun", ["Yusha'", "al-Khadir", "Shu'ayb"], "Except that there is no prophet after me.", "Sahih al-Bukhari"),
   ("Which daughter of the Prophet ﷺ did 'Ali رَضِيَ اللَّهُ عَنْهُ marry?", "Fatimah رَضِيَ اللَّهُ عَنْهَا", ["Zaynab رَضِيَ اللَّهُ عَنْهَا", "Ruqayyah رَضِيَ اللَّهُ عَنْهَا", "Umm Kulthum رَضِيَ اللَّهُ عَنْهَا"], "Their sons were al-Hasan and al-Husayn رَضِيَ اللَّهُ عَنْهُمَا.", TK),
   ("Where was 'Ali رَضِيَ اللَّهُ عَنْهُ martyred?", "In Kufah, on his way to Fajr", ["In Madinah", "At Karbala", "In Damascus"], "Karbala is where his son al-Husayn was martyred.", TK),
 ]),
 ("sh_ten", "The ten promised Paradise", "The Companions named together in one hadith.", [
   ("The hadith", "The Prophet ﷺ named ten Companions in one sitting as people of Paradise: Abu Bakr, 'Umar, 'Uthman, 'Ali, Talhah, al-Zubayr, 'Abd al-Rahman ibn 'Awf, Sa'd ibn Abi Waqqas, Sa'id ibn Zayd and Abu 'Ubaydah ibn al-Jarrah رَضِيَ اللَّهُ عَنْهُمْ.", "Sunan al-Tirmidhi, Book of Virtues"),
   ("Others too", "The ten are not the only ones promised Paradise. Others were given glad tidings too, such as Khadijah, Fatimah, al-Hasan, al-Husayn, Bilal and the people of Badr.", f"{TH}, the Companions"),
  ], [
   ("Which of these is one of the ten promised Paradise?", "Abu 'Ubaydah ibn al-Jarrah رَضِيَ اللَّهُ عَنْهُ", ["Abu Sufyan", "Khalid ibn al-Walid رَضِيَ اللَّهُ عَنْهُ", "Mu'adh ibn Jabal رَضِيَ اللَّهُ عَنْهُ"], "Named with Abu Bakr, 'Umar, 'Uthman, 'Ali, Talhah, al-Zubayr, 'Abd al-Rahman, Sa'd and Sa'id.", "Sunan al-Tirmidhi"),
   ("Are the ten the only people promised Paradise?", "No, others were given glad tidings too", ["Yes, only these ten", "Only the ten and the Prophets", "No one is promised Paradise"], "Such as Khadijah, Fatimah, al-Hasan, al-Husayn and the people of Badr.", TH),
   ("Which of these is NOT among the ten?", "Bilal ibn Rabah رَضِيَ اللَّهُ عَنْهُ", ["Sa'd ibn Abi Waqqas رَضِيَ اللَّهُ عَنْهُ", "Talhah ibn 'Ubaydullah رَضِيَ اللَّهُ عَنْهُ", "al-Zubayr ibn al-'Awwam رَضِيَ اللَّهُ عَنْهُ"], "Bilal was also given glad tidings of Paradise, in another hadith.", "Sunan al-Tirmidhi"),
 ]),
 ("sh_mothers", "The Mothers of the Believers", "The wives of the Prophet ﷺ.", [
   ("Our mothers", "Allah called the Prophet's wives the Mothers of the Believers. We honour them as our mothers.", "Qur'an, al-Ahzab 6"),
   ("Khadijah and 'A'ishah", "Khadijah bint Khuwaylid was his first wife, the first to believe, and the mother of his children except Ibrahim. 'A'ishah bint Abi Bakr was among the most learned of the Companions; many of the Sunnah's rulings come through her.", f"{FU}, his wives"),
   ("The others", "Sawdah, Hafsah, Zaynab bint Khuzaymah, Umm Salamah, Zaynab bint Jahsh, Juwayriyah, Umm Habibah, Safiyyah and Maymunah رَضِيَ اللَّهُ عَنْهُنَّ.", f"{FU}, his wives"),
  ], [
   ("What did Allah call the wives of the Prophet ﷺ?", "The Mothers of the Believers", ["The Companions of the Cave", "The Helpers", "The Emigrants"], "'And his wives are their mothers.' (al-Ahzab 6)", "Qur'an"),
   ("Who was the first wife of the Prophet ﷺ and the first to believe?", "Khadijah رَضِيَ اللَّهُ عَنْهَا", ["'A'ishah رَضِيَ اللَّهُ عَنْهَا", "Sawdah رَضِيَ اللَّهُ عَنْهَا", "Hafsah رَضِيَ اللَّهُ عَنْهَا"], "She supported him with her wealth and her heart.", FU),
   ("Which Mother of the Believers was among the most learned of the Companions?", "'A'ishah رَضِيَ اللَّهُ عَنْهَا", ["Juwayriyah رَضِيَ اللَّهُ عَنْهَا", "Maymunah رَضِيَ اللَّهُ عَنْهَا", "Safiyyah رَضِيَ اللَّهُ عَنْهَا"], "Senior Companions came to her with their questions.", FU),
   ("Hafsah رَضِيَ اللَّهُ عَنْهَا was the daughter of…", "'Umar ibn al-Khattab رَضِيَ اللَّهُ عَنْهُ", ["Abu Bakr رَضِيَ اللَّهُ عَنْهُ", "Abu Sufyan", "'Ali رَضِيَ اللَّهُ عَنْهُ"], "'A'ishah was the daughter of Abu Bakr.", FU),
 ]),
 ("sh_bayt", "The Ahl al-Bayt", "The family of the Prophet ﷺ, and loving them.", [
   ("Who they are", "The Ahl al-Bayt are the family of the Prophet ﷺ: his wives, Fatimah, 'Ali, al-Hasan, al-Husayn and their descendants, and the believers of Banu Hashim. Zakat may not be given to them, out of honour.", "Qur'an, al-Ahzab 33"),
   ("Fatimah al-Zahra'", "His youngest daughter. He ﷺ said: Fatimah is a part of me; whoever angers her angers me. She is the leader of the women of Paradise.", "Sahih al-Bukhari, Virtues of the Companions"),
   ("Al-Hasan and al-Husayn", "He ﷺ called them his two sweet basils of this world, and said they are the leaders of the youth of Paradise. Al-Husayn رَضِيَ اللَّهُ عَنْهُ was martyred at Karbala in 61 AH, a great tragedy for the Ummah.", "Sunan al-Tirmidhi, Book of Virtues"),
   ("I remind you of Allah", "He ﷺ said: I leave among you two weighty things: the Book of Allah, and the people of my house. I remind you of Allah regarding the people of my house. Loving them is part of loving him.", "Sahih Muslim, Virtues of the Companions"),
  ], [
   ("Who did the Prophet ﷺ call the leaders of the youth of Paradise?", "Al-Hasan and al-Husayn رَضِيَ اللَّهُ عَنْهُمَا", ["Abu Bakr and 'Umar رَضِيَ اللَّهُ عَنْهُمَا", "Zayd and Usamah رَضِيَ اللَّهُ عَنْهُمَا", "'Ali and Ja'far رَضِيَ اللَّهُ عَنْهُمَا"], "Narrated by al-Tirmidhi.", "Sunan al-Tirmidhi"),
   ("Where was al-Husayn رَضِيَ اللَّهُ عَنْهُ martyred?", "Karbala", ["Kufah", "Madinah", "Damascus"], "In 61 AH, on the day of 'Ashura'.", TK),
   ("What did the Prophet ﷺ say he left among us, in Sahih Muslim?", "The Book of Allah and the people of his house", ["Gold and silver", "Only the Ka'bah", "A list of caliphs"], "'I remind you of Allah regarding the people of my house,' three times.", "Sahih Muslim"),
   ("Why may zakat not be given to Banu Hashim?", "Out of honour for the Prophet's family ﷺ", ["Because they are all wealthy", "Because they refused it", "There is no reason"], "Help them with gifts and charity that is not zakat.", "Mukhtasar al-Quduri"),
 ]),
 ("sh_love", "Loving both, the way of Ahl al-Sunnah", "Holding the Companions and the Ahl al-Bayt together in the heart.", [
   ("Both together", "Ahl al-Sunnah love the Companions and the Ahl al-Bayt together, with no contradiction. 'Ali named his sons Abu Bakr, 'Umar and 'Uthman, and 'Umar married Umm Kulthum, daughter of 'Ali and Fatimah.", f"{TK}, 'Ali"),
   ("Their order", "We believe the caliphate after the Prophet ﷺ was for Abu Bakr, then 'Umar, then 'Uthman, then 'Ali, the Rightly Guided Caliphs, and their excellence is in that order.", f"{TH}, the caliphs"),
   ("Avoiding both extremes", "We do not curse any Companion, as some do, and we do not belittle the Ahl al-Bayt, as others do. Whoever speaks well of the Companions, the Prophet's wives and his descendants is free of hypocrisy.", f"{TH}, the Companions"),
  ], [
   ("Who are the four Rightly Guided Caliphs, in order?", "Abu Bakr, 'Umar, 'Uthman, 'Ali", ["'Ali, Abu Bakr, 'Umar, 'Uthman", "Abu Bakr, 'Ali, 'Umar, 'Uthman", "'Umar, Abu Bakr, 'Uthman, 'Ali"], "Their excellence follows the order of their caliphate.", TH),
   ("Which shows the love between 'Ali and the other caliphs?", "'Ali named his sons Abu Bakr, 'Umar and 'Uthman", ["'Ali never spoke to them", "'Ali left Madinah", "'Ali refused to pray behind them"], "Names a father gives his sons show his love.", TK),
   ("What is the way of Ahl al-Sunnah with the Companions and the Ahl al-Bayt?", "To love both, and curse none", ["To love the Companions only", "To love the Ahl al-Bayt only", "To stay neutral and love neither"], "Al-Tahawi: whoever speaks well of them is free of hypocrisy.", TH),
 ]),
]}

ADAB = {"id":"adab", "title":"Daily life: adab and adhkar", "ar":"الْآدَابُ وَالْأَذْكَارُ",
 "sub":"The sunnah way to wake, eat, dress, greet, sleep, and guard the limbs", "book":"Bidayat al-Hidayah, al-Adhkar and Riyad al-Salihin", "color":"#3B6B6B", "lessons":[
 ("ad_wake", "Waking up and the morning", "Starting the day the sunnah way.", [
   ("On waking", "Say: 'Al-hamdu lillahi alladhi ahyana ba'da ma amatana wa ilayhi al-nushur' (praise be to Allah who gave us life after He caused us to die, and to Him is the return). Use the siwak.", f"{AD}, on waking"),
   ("Before Fajr", "Al-Ghazali advises waking before dawn, making wudu, praying the two sunnah rak'ahs of Fajr at home, then going to pray Fajr in congregation.", f"{BH}, the adab of waking"),
   ("After Fajr", "Sitting in remembrance of Allah after Fajr until the sun has risen, then praying two rak'ahs, carries the reward of a complete Hajj and 'umrah, as in the hadith.", "Sunan al-Tirmidhi, Book of Prayer"),
  ], [
   ("What do you say on waking up?", "'Al-hamdu lillahi alladhi ahyana ba'da ma amatana…'", ["'Bismika Allahumma amutu wa ahya'", "'Subhana rabbiya al-a'la'", "'A'udhu billahi min al-khubuthi wa al-khaba'ith'"], "Praise to Allah who gave us life after death (sleep). The second option is said before sleeping.", AD),
   ("What reward is in the hadith for staying in dhikr after Fajr until sunrise, then praying two rak'ahs?", "Like a complete Hajj and 'umrah", ["Like fasting a month", "Like freeing a slave", "No special reward"], "Narrated by al-Tirmidhi.", "Sunan al-Tirmidhi"),
   ("Where does al-Ghazali advise praying the sunnah of Fajr?", "At home, before going to the masjid", ["Only in the masjid", "After the fard", "It may be left out"], "The sunnah prayers are best at home.", BH),
 ]),
 ("ad_adhkar", "Morning and evening adhkar", "The daily protection every Muslim should keep.", [
   ("The three Quls", "Recite Surat al-Ikhlas, al-Falaq and al-Nas three times in the morning and three in the evening; the Prophet ﷺ said they will suffice you against everything.", "Sunan Abi Dawud, Book of Manners"),
   ("Ayat al-Kursi", "Whoever recites Ayat al-Kursi in the morning is protected until evening, and in the evening until morning.", f"{AD}, morning and evening"),
   ("The master of seeking forgiveness", "'Allahumma anta rabbi, la ilaha illa ant, khalaqtani wa ana 'abduk…' Whoever says it with certainty in the morning and dies that day is of the people of Paradise; the same for the evening.", "Sahih al-Bukhari, Book of Supplications"),
   ("Simple and great", "'Subhan Allahi wa bi-hamdih' a hundred times a day wipes away sins even if they are like the foam of the sea.", "Sahih al-Bukhari, Book of Supplications"),
  ], [
   ("How many times are the three Quls recited morning and evening?", "Three times each", ["Once each", "Seven times each", "Ten times each"], "The Prophet ﷺ said they suffice against everything.", "Sunan Abi Dawud"),
   ("What is 'Sayyid al-Istighfar'?", "The master of seeking forgiveness: 'Allahumma anta rabbi…'", ["Ayat al-Kursi", "Surat al-Fatihah", "The adhan"], "Said with certainty morning or evening, it is a means to Paradise.", "Sahih al-Bukhari"),
   ("Saying 'Subhan Allahi wa bi-hamdih' a hundred times a day…", "Wipes away sins, even like the foam of the sea", ["Replaces the prayer", "Is only for Fridays", "Is disliked"], "Narrated by al-Bukhari.", "Sahih al-Bukhari"),
   ("Which verse protects you from morning until evening when recited?", "Ayat al-Kursi", ["The last verse of al-Baqarah only", "The first verse of al-Kahf", "Surat al-Kawthar"], "Al-Baqarah 255.", AD),
 ]),
 ("ad_afterprayer", "After the prayer", "What the Prophet ﷺ said after every fard prayer.", [
   ("Seeking forgiveness", "After the salam, say 'Astaghfirullah' three times, then 'Allahumma anta al-salam wa minka al-salam, tabarakta ya dha al-jalali wa al-ikram.'", "Sahih Muslim, Book of Prayer"),
   ("The tasbih", "Say 'Subhan Allah' 33 times, 'Al-hamdu lillah' 33 times and 'Allahu akbar' 34 times (or 33 and then 'La ilaha illa Allahu wahdahu la sharika lah…'). Sins are forgiven even if like the foam of the sea.", "Sahih Muslim, Book of Prayer"),
   ("Ayat al-Kursi", "Whoever recites Ayat al-Kursi after every fard prayer, nothing stands between him and Paradise except death.", "Sunan al-Nasa'i al-Kubra"),
  ], [
   ("What is said three times right after the salam?", "'Astaghfirullah'", ["'Allahu akbar'", "'Subhan Allah'", "'Bismillah'"], "Then 'Allahumma anta al-salam…'.", "Sahih Muslim"),
   ("How many times is 'Allahu akbar' said in the tasbih after prayer?", "34 (or 33, then the tahlil)", ["10", "99", "7"], "33 Subhan Allah, 33 Al-hamdu lillah, 34 Allahu akbar.", "Sahih Muslim"),
   ("What reward is mentioned for Ayat al-Kursi after every fard prayer?", "Only death stands between him and Paradise", ["A palace in this world", "Wealth", "Nothing specific"], "Narrated by al-Nasa'i.", "Sunan al-Nasa'i"),
 ]),
 ("ad_salam", "Greeting with salam", "Spreading salam, and how to reply.", [
   ("Spread it", "The Prophet ﷺ said: you will not enter Paradise until you believe, and you will not believe until you love one another. Shall I tell you what will make you love one another? Spread salam among you.", "Sahih Muslim, Book of Faith"),
   ("Its rulings", "Beginning the salam is a sunnah; replying is wajib. Reply with the same or better: to 'al-salamu 'alaykum' reply 'wa 'alaykum al-salam wa rahmatullah'.", f"{RS}, the chapter on salam"),
   ("Who greets first", "The rider greets the one walking, the walker the one sitting, the smaller group the larger, and the young the old.", "Sahih al-Bukhari, Book of Seeking Permission"),
  ], [
   ("What is the ruling of replying to a salam?", "Wajib", ["Sunnah", "Optional", "Disliked"], "Beginning it is sunnah; replying is wajib.", RS),
   ("What did the Prophet ﷺ say makes people love one another?", "Spreading salam", ["Giving expensive gifts", "Eating together only", "Speaking little"], "Narrated by Muslim.", "Sahih Muslim"),
   ("Who should greet first, the one walking or the one sitting?", "The one walking", ["The one sitting", "Whoever is older", "It does not matter"], "And the rider greets the walker, the few greet the many.", "Sahih al-Bukhari"),
   ("Someone says 'al-salamu 'alaykum wa rahmatullah'. What is the better reply?", "'Wa 'alaykum al-salam wa rahmatullahi wa barakatuh'", ["'Wa 'alaykum'", "'Hello'", "Silence"], "Reply with the same or better.", "Qur'an, al-Nisa' 86"),
 ]),
 ("ad_eat", "Eating and drinking", "The sunnahs of the table.", [
   ("Before and with", "Wash the hands, say 'Bismillah', and eat with the right hand from what is in front of you. If you forget bismillah, say 'Bismillahi awwalahu wa akhirah.'", "Sahih al-Bukhari, Book of Food"),
   ("How much", "Do not fill the stomach: a third for food, a third for drink and a third for breath. Never criticise food: eat it if you like it, leave it if you don't.", "Sunan al-Tirmidhi, Book of Asceticism"),
   ("Drinking", "Drink sitting, in three breaths, with the right hand, and not from the mouth of a container. Gold and silver vessels are haram.", f"{BH}, the adab of eating"),
   ("After", "Lick the fingers, and say 'Al-hamdu lillahi alladhi at'amani hadha wa razaqanihi min ghayri hawlin minni wa la quwwah.'", "Sunan Abi Dawud, Book of Clothing"),
  ], [
   ("You forgot to say bismillah at the start of the meal. What do you say?", "'Bismillahi awwalahu wa akhirah'", ["Nothing, it is too late", "Start the meal again", "'Al-hamdu lillah' only"], "In the name of Allah at its beginning and its end.", "Sunan Abi Dawud"),
   ("How did the Prophet ﷺ describe the right amount to eat?", "A third food, a third drink, a third breath", ["Until completely full", "Only one meal a day", "Half food, half drink"], "Narrated by al-Tirmidhi.", "Sunan al-Tirmidhi"),
   ("Which hand do you eat and drink with?", "The right hand", ["Either hand", "The left hand", "Whichever is stronger"], "Shaytan eats and drinks with his left.", "Sahih Muslim"),
   ("What did the Prophet ﷺ do with food he did not like?", "He left it without criticising it", ["He criticised it to teach others", "He threw it away", "He ate it anyway"], "He never found fault with food.", "Sahih al-Bukhari"),
 ]),
 ("ad_dress", "Dressing and the sunnahs of the body", "Clothing, and the fitrah.", [
   ("Dressing", "Begin with the right when dressing and the left when undressing. Say 'Al-hamdu lillahi alladhi kasani hadha wa razaqanihi…' when putting on clothes.", f"{AD}, on dressing"),
   ("For men", "Gold and silk are haram for men. A man's garment should not drag below the ankles out of pride.", "Sahih al-Bukhari, Book of Clothing"),
   ("The fitrah", "The acts of the fitrah: circumcision, removing pubic hair, plucking the armpits, trimming the moustache and clipping the nails. Do not leave them more than forty days.", "Sahih Muslim, Book of Purity"),
  ], [
   ("Which foot or sleeve do you begin with when dressing?", "The right", ["The left", "Either", "Both together"], "Right when dressing, left when undressing.", AD),
   ("What is the longest these acts of the fitrah should be left?", "Forty days", ["One week", "Three months", "One year"], "Anas رَضِيَ اللَّهُ عَنْهُ narrated the limit of forty days.", "Sahih Muslim"),
   ("Which of these is haram for men to wear?", "Silk and gold", ["White clothes", "A turban", "A ring of silver"], "A silver ring of modest weight is allowed for men.", "Sahih al-Bukhari"),
 ]),
 ("ad_home", "The home and the masjid", "Entering, leaving, and the adab of the masjid.", [
   ("Leaving home", "Say: 'Bismillah, tawakkaltu 'ala Allah, wa la hawla wa la quwwata illa billah.' It is said to him: you are guided, protected and sufficed.", "Sunan Abi Dawud, Book of Manners"),
   ("Entering the masjid", "Enter with the right foot saying 'Allahumma iftah li abwaba rahmatik', and leave with the left saying 'Allahumma inni as'aluka min fadlik.' Pray two rak'ahs greeting the masjid before sitting.", "Sahih Muslim, Book of Prayer"),
   ("In the masjid", "Do not come after eating raw onion or garlic, do not raise your voice, do not pass in front of someone praying, and do not trade or look for lost things in it.", f"{BH}, the adab of the masjid"),
  ], [
   ("With which foot do you enter the masjid?", "The right", ["The left", "Either", "Whichever is first"], "Right to enter the masjid; left to enter the toilet.", "Sahih Muslim"),
   ("What do you say when entering the masjid?", "'Allahumma iftah li abwaba rahmatik'", ["'Allahumma inni as'aluka min fadlik'", "'Bismika Allahumma amutu wa ahya'", "'Subhanaka Allahumma'"], "Open for me the doors of Your mercy. The second is said when leaving.", "Sahih Muslim"),
   ("What should you avoid before going to the masjid?", "Eating raw onion or garlic", ["Making wudu at home", "Wearing your best clothes", "Using perfume"], "Their smell harms the people and the angels.", "Sahih Muslim"),
   ("What is the prayer on entering the masjid before sitting?", "Two rak'ahs greeting the masjid", ["Four rak'ahs of sunnah", "One rak'ah of witr", "No prayer"], "Tahiyyat al-masjid, at a time when prayer is not disliked.", "Sahih Muslim"),
 ]),
 ("ad_social", "Sneezing, the sick and the funeral", "Small acts with great reward.", [
   ("Sneezing", "Whoever sneezes says 'Al-hamdu lillah'; the one who hears replies 'Yarhamuk Allah'; the sneezer answers 'Yahdikumu Allahu wa yuslihu balakum.' When yawning, cover the mouth and hold it back as much as you can.", "Sahih al-Bukhari, Book of Manners"),
   ("Visiting the sick", "Visiting the sick is among the rights of a Muslim. Whoever visits a sick person is among the fruits of Paradise until he returns. Pray for him: 'La ba's, tahurun in sha' Allah.'", "Sahih Muslim, Book of Righteousness"),
   ("The rights of a Muslim", "Six rights of a Muslim over another: return his salam, answer his invitation, give him sincere advice, reply when he sneezes and praises Allah, visit him when ill, and follow his funeral when he dies.", "Sahih Muslim, Book of Salam"),
  ], [
   ("Someone sneezes and says 'Al-hamdu lillah'. What do you reply?", "'Yarhamuk Allah'", ["'Bismillah'", "'Al-hamdu lillah' too", "'Bless you' only"], "May Allah have mercy on you.", "Sahih al-Bukhari"),
   ("Which is one of the six rights of a Muslim over another?", "To visit him when he is ill", ["To lend him money whenever asked", "To agree with him always", "To praise him in public"], "Narrated by Muslim.", "Sahih Muslim"),
   ("What should you do when yawning?", "Cover the mouth and hold it back", ["Yawn loudly", "Say 'Allahu akbar'", "Nothing"], "Yawning is from Shaytan; hold it back as much as you can.", "Sahih al-Bukhari"),
 ]),
 ("ad_sleep", "Before sleeping", "Ending the day the sunnah way.", [
   ("Preparing", "Sleep in wudu, dust the bed, lie on the right side with the right hand under the cheek. Close the doors and cover the vessels saying bismillah.", "Sahih al-Bukhari, Book of Supplications"),
   ("What to recite", "Ayat al-Kursi, the three Quls (blowing into the hands and wiping over the body three times), the last two verses of al-Baqarah, and 'Subhan Allah' 33, 'Al-hamdu lillah' 33, 'Allahu akbar' 34.", "Sahih al-Bukhari, Book of Virtues of the Qur'an"),
   ("The last words", "Say 'Bismika Allahumma amutu wa ahya' (in Your name, O Allah, I die and I live), and take account of your day: thank Allah for the good and repent of the wrong.", f"{BH}, the adab of sleeping"),
  ], [
   ("On which side is it sunnah to sleep?", "The right side", ["The left side", "On the back", "On the stomach"], "With the right hand under the cheek.", "Sahih al-Bukhari"),
   ("What do you say just before sleeping?", "'Bismika Allahumma amutu wa ahya'", ["'Al-hamdu lillahi alladhi ahyana'", "'Allahumma iftah li abwaba rahmatik'", "'Astaghfirullah' once"], "In Your name, O Allah, I die and I live.", AD),
   ("Which tasbih did the Prophet ﷺ teach 'Ali and Fatimah for bedtime?", "33 Subhan Allah, 33 Al-hamdu lillah, 34 Allahu akbar", ["100 Allahu akbar", "10 of each", "7 Subhan Allah"], "He said it is better for them than a servant.", "Sahih al-Bukhari"),
   ("What does al-Ghazali advise doing before sleep?", "Taking account of your day", ["Planning tomorrow's meals", "Reading the news", "Nothing at all"], "Thank Allah for the good and repent of the wrong.", BH),
 ]),
 ("ad_limbs", "Guarding the seven limbs", "Al-Ghazali's guide to avoiding sins.", [
   ("The seven", "Al-Ghazali says religion has two parts: doing what is commanded and leaving what is forbidden, and leaving sins is the harder and more important. Guard seven limbs: the eyes, ears, tongue, stomach, private parts, hands and feet.", f"{BH}, avoiding sins"),
   ("Eyes and ears", "Lower the gaze from what is haram, and do not look at a Muslim with contempt. Do not listen to backbiting, obscenity or idle talk about others' faults; the listener shares the sin of the speaker.", f"{BH}, the eye and the ear"),
   ("The tongue", "Guard it from eight things: lying, breaking promises, backbiting, arguing, praising yourself, cursing, praying against people, and joking that hurts or mocks.", f"{BH}, the tongue"),
   ("Stomach, hands, feet", "Eat only halal, and not too much. Do not use the hands to harm, take or write what is haram. Do not walk to a ruler's door to flatter, or anywhere sinful.", f"{BH}, the stomach, hands and feet"),
  ], [
   ("According to al-Ghazali, which part of religion is harder: doing good, or leaving sins?", "Leaving sins", ["Doing good deeds", "They are equally easy", "Neither matters"], "Anyone can do good deeds; only the truthful leave their desires.", BH),
   ("Listening to backbiting…", "Shares in the sin of the speaker", ["Is fine if you say nothing", "Is only disliked", "Is good, to know what is happening"], "Stop it, leave, or at least hate it in your heart.", BH),
   ("Which of these is among the eight sins of the tongue al-Ghazali lists?", "Praising yourself", ["Reciting the Qur'an", "Giving salam", "Saying 'in sha' Allah'"], "Along with lying, broken promises, backbiting, arguing, cursing, praying against others and hurtful joking.", BH),
   ("How many limbs does al-Ghazali tell us to guard?", "Seven", ["Five", "Three", "Ten"], "Eyes, ears, tongue, stomach, private parts, hands and feet.", BH),
 ]),
 ("ad_teach", "Seeking knowledge and passing it on", "You have learnt the basics. Now keep learning, and teach.", [
   ("A duty", "The Prophet ﷺ said: seeking knowledge is an obligation on every Muslim. What you must know for your own worship and dealings is fard al-'ayn; going deeper is a virtue, and some must do it for the whole community.", "Sunan Ibn Majah, Introduction"),
   ("Pass it on", "He ﷺ said: convey from me, even one verse. And: whoever guides to good has the reward of the one who does it. Teach your family first what you have learnt.", "Sahih al-Bukhari, Book of the Prophets"),
   ("How to teach", "Teach only what you know well, say 'I don't know' when you don't, mention your source, be gentle and make it easy.", f"{BH}, the adab of the scholar"),
   ("Keep going", "Al-Ghazali warns: knowledge that is not acted on is a proof against you. Act on what you learn, then study further with a teacher, in the Course and in our live classes.", f"{BH}, introduction"),
  ], [
   ("What did the Prophet ﷺ say about passing on knowledge?", "'Convey from me, even one verse'", ["'Only scholars may teach'", "'Keep knowledge to yourself'", "'Teach only after forty'"], "Narrated by al-Bukhari.", "Sahih al-Bukhari"),
   ("Someone asks you a question you are unsure about. What should you do?", "Say 'I don't know', or refer them to a scholar", ["Guess so you don't look ignorant", "Give your opinion", "Make up a hadith"], "Speaking about the religion without knowledge is a grave sin; 'I don't know' protects you.", BH),
   ("Who should you teach first?", "Your family", ["Strangers online", "Only scholars", "No one"], "'Protect yourselves and your families from a Fire.' (al-Tahrim 6)", "Qur'an"),
   ("What does al-Ghazali say about knowledge that is not acted on?", "It is a proof against you", ["It is still enough", "It earns the same reward", "It does not matter"], "Act on what you learn.", BH),
 ]),
]}
