"""LEARN: the Fard al-'Ayn for everyone, in short simple lessons (Hanafi, Ash'ari/Maturidi), written from our books.
Each lesson: a few short cards, then checks. Sources are named on each card. Written for the app; to be checked by a teacher.
Card: (title, text, source). Check: (question, right answer, [three wrong answers])."""

UNITS = [
 ("belief", "Belief", "What every Muslim must believe about Allah and His Messengers ﷺ", "#0E5A43", [
  ("Why we learn belief", [
    ("Your first duty", "Every Muslim who has reached adulthood and is sane must know what is necessary for Allah, what is impossible for Him, and what is possible for Him. The same applies to the Messengers عليهم السلام.", "Umm al-Barahin"),
    ("Three kinds of judgement", "Something is necessary if the mind cannot picture it not being there. It is impossible if the mind cannot picture it existing. It is possible if the mind can picture it existing or not existing.", "Umm al-Barahin"),
    ("Why it matters", "Knowing these things protects your belief from doubt. You don't need to be a scholar: you need to know them clearly and be sure of them.", "Umm al-Barahin"),
   ], [
    ("Who must know what is necessary, impossible and possible for Allah?", "Every sane adult Muslim", ["Only scholars", "Only those who study Arabic", "Only people born outside Islam"]),
    ("Something the mind cannot picture not existing is called…", "Necessary", ["Possible", "Impossible", "Hidden"]),
    ("Something the mind can picture existing or not existing is called…", "Possible", ["Necessary", "Impossible", "Eternal"]),
   ]),
  ("Allah exists, without beginning or end", [
    ("He exists", "Allah exists. His existence has no cause and does not depend on anything.", "Umm al-Barahin"),
    ("Without beginning", "Allah has no beginning (qidam). Everything else came into being after not existing; He did not.", "Umm al-Barahin"),
    ("Without end", "Allah has no end (baqa'). He will never cease to be. As Imam al-Tahawi رحمه الله says: He is Eternal without a beginning and Everlasting without an end.", "al-'Aqidah al-Tahawiyyah"),
   ], [
    ("What does it mean that Allah has no beginning?", "He never came into being; He always was", ["He was created before everything else", "He began when the universe began", "No one knows if He has a beginning"]),
    ("What does it mean that Allah has no end?", "He will never cease to exist", ["He will end after the Last Day", "He ends when the world ends", "He changes into something else"]),
    ("Does Allah's existence depend on anything?", "No, it depends on nothing", ["Yes, on the heavens", "Yes, on His creation", "Yes, on time"]),
   ]),
  ("Allah is unlike anything", [
    ("Unlike His creation", "Allah does not resemble anything He created. He is not a body, He is not in a place, and He is not bound by time. 'There is nothing like Him, and He is the All-Hearing, the All-Seeing.' (al-Shura 11)", "Umm al-Barahin"),
    ("Needs nothing", "Allah stands by Himself (qiyam bi-nafsihi): He needs no place and no one to bring Him into being. Everything needs Him.", "Umm al-Barahin"),
    ("One", "Allah is One (wahdaniyyah): One in His Self, One in His attributes and One in His actions. He has no partner and no equal.", "Umm al-Barahin"),
   ], [
    ("Which is true about Allah?", "He does not resemble anything He created", ["He has a body unlike ours", "He is in one particular place", "He is bound by time like us"]),
    ("What does it mean that Allah 'stands by Himself'?", "He needs nothing, while everything needs Him", ["He needs His throne to exist", "He stands in one place", "He needs worship to exist"]),
    ("Allah's Oneness covers…", "His Self, His attributes and His actions", ["Only His Self", "Only His actions", "Only His names"]),
   ]),
  ("Seven attributes of Allah", [
    ("Power and will", "Allah has Power (qudrah) over every possible thing, and Will (iradah): nothing happens except what He wills.", "Umm al-Barahin"),
    ("Knowledge and life", "Allah has Knowledge ('ilm) of everything: what was, what is, what will be, and what would be. He is Living (hayah) with a life unlike ours.", "Umm al-Barahin"),
    ("Hearing, sight and speech", "Allah hears (sam') and sees (basar) all that exists, without ears or eyes. He speaks (kalam) with an eternal speech that is not letters or sounds. The Qur'an is His speech.", "Umm al-Barahin"),
   ], [
    ("Nothing happens in creation except…", "What Allah wills", ["What people choose alone", "What nature decides", "What angels decide"]),
    ("How does Allah hear and see?", "Without ears or eyes, unlike creation", ["With ears and eyes like ours", "Only through the angels", "He does not hear or see"]),
    ("Allah's speech is…", "Eternal, and not made of letters or sounds", ["Created like ours", "Only the Arabic language", "Something that began with the Qur'an"]),
   ]),
  ("The Messengers عليهم السلام", [
    ("What is necessary for them", "The Messengers are truthful (sidq), trustworthy (amanah) and convey everything they were commanded to convey (tabligh).", "Umm al-Barahin"),
    ("What is impossible for them", "Lying, betraying trust, and hiding what they were commanded to convey are impossible for them.", "Umm al-Barahin"),
    ("What is possible for them", "Human things that do not lower their rank are possible for them, such as eating, sleeping, marriage and illness that is not repulsive.", "Umm al-Barahin"),
    ("The Seal", "Muhammad ﷺ is the last Prophet and the Messenger to all of mankind and jinn. There is no prophet after him.", "al-'Aqidah al-Tahawiyyah"),
   ], [
    ("Which is necessary for every Messenger?", "Truthfulness, trustworthiness and conveying the message", ["Wealth and power", "Never falling ill", "Knowing the unseen by themselves"]),
    ("Which is possible for a Messenger?", "Eating, sleeping and marrying", ["Hiding part of the message", "Telling a lie", "Betraying a trust"]),
    ("Who is the last Prophet?", "Muhammad ﷺ", ["'Isa عليه السلام", "Ibrahim عليه السلام", "There will be another after him"]),
   ]),
  ("What a believer believes", [
    ("The articles of faith", "A believer believes in Allah, His angels, His books, His Messengers, the Last Day, and that good and bad are by Allah's decree.", "al-'Aqidah al-Tahawiyyah"),
    ("What faith is", "Faith (iman) is affirming with the tongue and believing with the heart everything the Prophet ﷺ brought from Allah.", "al-'Aqidah al-Tahawiyyah"),
    ("Love of the Companions", "We love the Companions of the Messenger of Allah ﷺ. We do not go to excess in loving any one of them, and we do not disown any of them. We mention them only with good.", "al-'Aqidah al-Tahawiyyah"),
   ], [
    ("According to al-Tahawi, faith is…", "Affirming with the tongue and believing with the heart", ["Only good deeds", "Only believing, with no need to say it", "Only saying it with the tongue"]),
    ("Which is one of the articles of faith?", "Belief in Allah's decree, the good and the bad", ["Belief in lucky days", "Belief that the stars decide events", "Belief that some saints are prophets"]),
    ("How do we speak of the Companions?", "Only with good, without going to excess about any of them", ["We praise some and disown others", "We do not mention them", "We judge their disputes"]),
   ]),
 ]),
 ("purity", "Purification", "Water, wudu, ghusl and tayammum", "#2F6E8F", [
  ("Water you can use", [
    ("Seven waters", "You may purify yourself with seven kinds of water: rain, sea, river, well, melted snow, melted hail and spring water.", "Nur al-Idah"),
    ("Water that changes", "If something pure is mixed with water and the water is still called water, you may use it. If it has become something else, like juice or soup, you may not.", "Nur al-Idah"),
    ("Used water", "Water that has already been used for wudu or ghusl is pure, but you cannot purify yourself with it again.", "Nur al-Idah"),
   ], [
    ("Which water can be used for wudu?", "Rain water", ["Rose water", "Fruit juice", "Water already used for ghusl"]),
    ("Can you make wudu with water used for someone's ghusl?", "No: it is pure but does not purify", ["Yes, it purifies again", "Only for the feet", "Only if it is warm"]),
    ("How many kinds of water does Nur al-Idah list for purification?", "Seven", ["Three", "Four", "Ten"]),
   ]),
  ("The four obligations of wudu", [
    ("Face", "Wash the whole face: from the top of the forehead to under the chin, and from one earlobe to the other.", "Nur al-Idah"),
    ("Arms", "Wash both hands and arms, including the elbows.", "Nur al-Idah"),
    ("Head", "Wipe at least a quarter of the head with a wet hand.", "Nur al-Idah"),
    ("Feet", "Wash both feet, including the ankles. If any of these four is missed, the wudu is not valid.", "Nur al-Idah"),
   ], [
    ("How much of the head must be wiped in wudu?", "At least a quarter", ["Just three hairs", "The whole head, every time", "The forehead only"]),
    ("How far must the arms be washed?", "Including the elbows", ["Up to the wrists", "Up to the shoulders", "Half the forearm"]),
    ("Which of these is one of the four obligations of wudu?", "Washing the feet including the ankles", ["Rinsing the mouth", "Wiping the ears", "Saying bismillah"]),
   ]),
  ("The sunnahs of wudu", [
    ("Before you begin", "Have the intention, say bismillah, wash the hands to the wrists and use the siwak (even a finger if you have no siwak).", "Nur al-Idah"),
    ("Mouth and nose", "Rinse the mouth three times and sniff water into the nose three times.", "Nur al-Idah"),
    ("The rest", "Wash each part three times, wipe the whole head once and the ears, run water between the fingers and toes, start with the right, follow the order Allah mentions, and keep going without long breaks.", "Nur al-Idah"),
   ], [
    ("In the Hanafi school, rinsing the mouth in wudu is…", "A sunnah", ["One of the four obligations", "Disliked", "Only for ghusl"]),
    ("How many times is each part washed according to the sunnah?", "Three times", ["Once only", "Five times", "Seven times"]),
    ("Which is a sunnah of wudu?", "Starting with the right side", ["Starting with the feet", "Talking during wudu", "Washing each part four times"]),
   ]),
  ("What breaks wudu", [
    ("From the body", "Anything that comes out of the front or back passage, flowing blood or pus, and vomit that fills the mouth all break wudu.", "Nur al-Idah"),
    ("Sleep and losing the mind", "Sleeping without being seated firmly on the ground breaks it, as do fainting, insanity and drunkenness.", "Nur al-Idah"),
    ("Laughing in prayer", "Laughing out loud in a prayer with bowing and prostration breaks both the prayer and the wudu, for a sane, awake adult.", "Nur al-Idah"),
    ("What does not break it", "Touching your private part, touching a woman, blood that does not flow, vomit that does not fill the mouth, and dozing while sitting firmly do not break wudu.", "Nur al-Idah"),
   ], [
    ("Which breaks wudu in the Hanafi school?", "Blood flowing from a cut", ["Touching a woman", "Touching one's private part", "A spot of blood that does not flow"]),
    ("Which kind of sleep breaks wudu?", "Sleep without being seated firmly on the ground", ["Dozing while sitting firmly", "Sleeping in the sunnah way in prostration", "A moment of drowsiness while sitting"]),
    ("Laughing out loud during the prayer…", "Breaks both the prayer and the wudu", ["Breaks only the wudu", "Breaks nothing", "Breaks only the prayer"]),
   ]),
  ("Ghusl: the full bath", [
    ("When it is fard", "Ghusl becomes fard after the release of semen with desire, after intercourse even without release, and when menstruation or post-natal bleeding ends.", "Nur al-Idah"),
    ("Its obligations", "Rinse the whole mouth, wash inside the nose, and wash the whole body once, so that no dry spot remains, including the navel and under the beard.", "Nur al-Idah"),
    ("Hair", "A man must wet the inside of his plaited hair. A woman does not have to undo her plaits if water reaches the roots.", "Nur al-Idah"),
   ], [
    ("In the Hanafi school, rinsing the mouth in ghusl is…", "Fard", ["Sunnah only", "Disliked", "Not needed"]),
    ("Which makes ghusl fard?", "The end of menstruation", ["Touching a dog", "Eating camel meat", "Sleeping"]),
    ("Must a woman undo her plaits for ghusl?", "No, if water reaches the roots of her hair", ["Yes, always", "Only in winter", "Only after menstruation"]),
   ]),
  ("Tayammum: when there is no water", [
    ("When it is allowed", "When you are a mile or more from water, when using water would make you ill or worse, when it is dangerously cold, or when you need the water to drink.", "Nur al-Idah"),
    ("How to do it", "Make the intention, strike clean earth with both palms and wipe the whole face; strike again and wipe both arms including the elbows.", "Nur al-Idah"),
    ("What it does", "Tayammum stands in place of wudu and ghusl. It ends when water becomes available and you are able to use it.", "Nur al-Idah"),
   ], [
    ("Which of these allows tayammum?", "Water is a mile or more away", ["The water is slightly cold", "You are in a hurry", "You don't feel like washing"]),
    ("How many times are the hands struck on the earth?", "Twice: once for the face, once for the arms", ["Once only", "Three times", "Seven times"]),
    ("What ends tayammum, besides what breaks wudu?", "Finding water you are able to use", ["The next prayer time", "Sunrise", "Nothing at all"]),
   ]),
 ]),
 ("prayer", "Prayer", "Its conditions, pillars and the mistakes that ruin it", "#1F4E79", [
  ("Before you pray", [
    ("Purity", "You must be in wudu (and ghusl if needed), and your body, clothes and the place you pray on must be clean of impurity.", "Nur al-Idah"),
    ("Covering", "Cover the 'awrah. For a man it is from the navel to below the knees. For a woman it is the whole body except the face, the hands and the feet.", "Nur al-Idah"),
    ("Qiblah, time and intention", "Face the qiblah, pray after the time has come in, and intend the prayer you are praying, such as today's Zuhr.", "Nur al-Idah"),
    ("Opening takbir", "Begin with 'Allahu akbar' while standing, saying it so that you hear yourself.", "Nur al-Idah"),
   ], [
    ("What is a man's 'awrah in prayer?", "From the navel to below the knees", ["Only the private parts", "From the chest to the ankles", "The whole body except the face"]),
    ("If you pray before the time has come in…", "The prayer is not valid", ["It counts if you meant well", "It counts as early", "It is only disliked"]),
    ("Which is a condition for the prayer?", "Clean clothes and place", ["Praying in a mosque", "Wearing white", "Praying in congregation"]),
   ]),
  ("The pillars of prayer", [
    ("Four pillars", "Inside the prayer, four things are pillars: standing, reciting, bowing (ruku') and prostrating (sujud).", "Nur al-Idah"),
    ("The final sitting", "Nur al-Idah names these four, then adds that the final sitting, for as long as it takes to recite the tashahhud, is also said to be a pillar. Either way it is fard: the prayer is not valid without it.", "Nur al-Idah"),
    ("Without a pillar", "If a pillar is missed, the prayer is not valid and must be prayed again. The prostration of forgetfulness cannot fix it.", "Nur al-Idah"),
   ], [
    ("Which is a pillar of prayer?", "Bowing (ruku')", ["Raising the hands at takbir", "Saying 'amin'", "Placing the right hand over the left"]),
    ("If you miss a pillar…", "The prayer must be prayed again", ["Two prostrations of forgetfulness fix it", "Nothing is needed", "You add one rak'ah"]),
    ("How long is the final sitting at least?", "As long as it takes to recite the tashahhud", ["Just a moment", "As long as the whole prayer", "As long as one rak'ah"]),
   ]),
  ("The wajib acts of prayer", [
    ("What they are", "Wajib acts include: reciting al-Fatihah, adding a surah or three verses, calmness in every position, the first sitting, the tashahhud, and ending with 'al-salam'.", "Nur al-Idah"),
    ("Forgetting one", "If you leave a wajib act by mistake, make two prostrations of forgetfulness (sajdat al-sahw) at the end, with tashahhud and salam.", "Nur al-Idah"),
    ("Leaving one on purpose", "If you leave a wajib act deliberately, you are sinful and must repeat the prayer.", "Nur al-Idah"),
   ], [
    ("In the Hanafi school, reciting al-Fatihah is…", "Wajib", ["A pillar", "Sunnah", "Recommended only in the first rak'ah"]),
    ("You forgot the first sitting. What do you do?", "Make the two prostrations of forgetfulness at the end", ["Start the prayer again straight away", "Nothing, it is only sunnah", "Add an extra rak'ah"]),
    ("You left a wajib act on purpose. What follows?", "You are sinful and must repeat the prayer", ["Two prostrations of forgetfulness are enough", "Nothing", "Give charity instead"]),
   ]),
  ("What breaks the prayer", [
    ("Speaking", "Speaking breaks the prayer, even by forgetfulness or mistake.", "Nur al-Idah"),
    ("Eating and drinking", "Eating or drinking anything, even a little, breaks it.", "Nur al-Idah"),
    ("Movement and turning", "A lot of movement, or turning the chest away from the qiblah, breaks it.", "Nur al-Idah"),
    ("Answering people", "Returning a greeting, or replying to someone with words such as 'al-hamdu lillah' as an answer, breaks it.", "Nur al-Idah"),
   ], [
    ("You forgot you were praying and said a word. Is the prayer broken?", "Yes, speaking breaks it even by forgetfulness", ["No, forgetting is excused", "Only if it was a long sentence", "Only in the fard prayer"]),
    ("Someone greets you while you pray. If you reply 'wa 'alaykum al-salam'…", "Your prayer is broken", ["It is rewarded", "It is fine if said quietly", "It is only disliked"]),
    ("Which breaks the prayer?", "Turning the chest away from the qiblah", ["Glancing to the side without turning", "Closing the eyes", "Scratching once"]),
   ]),
  ("Witr", [
    ("Its ruling", "In the Hanafi school, the witr prayer is wajib.", "Nur al-Idah"),
    ("How it is prayed", "Witr is three rak'ahs with one salam at the end, and a surah after al-Fatihah in every rak'ah.", "Nur al-Idah"),
    ("Qunut", "In the third rak'ah, before bowing, say 'Allahu akbar', raise the hands and recite the qunut.", "Nur al-Idah"),
   ], [
    ("In the Hanafi school, witr is…", "Wajib", ["Sunnah only", "Fard like Zuhr", "Only in Ramadan"]),
    ("How many rak'ahs is witr in the Hanafi school?", "Three, with one salam", ["One", "Two, then one", "Eleven"]),
    ("When is the qunut recited in witr?", "In the third rak'ah, before bowing", ["After bowing in the second rak'ah", "After the salam", "Only in Ramadan's last ten nights"]),
   ]),
 ]),
 ("fasting", "Fasting", "Ramadan: what breaks the fast and what doesn't", "#7A5230", [
  ("What does not break the fast", [
    ("Forgetting", "If you eat, drink or have intercourse having forgotten you are fasting, your fast is not broken.", "Nur al-Idah"),
    ("Small things", "Applying kohl or oil, smoke or dust entering the throat without your doing, and waking up in a state of janabah do not break the fast.", "Nur al-Idah"),
    ("But the tongue", "Backbiting does not break the fast, but it ruins its reward. Guard your tongue while fasting.", "Nur al-Idah"),
   ], [
    ("You forgot you were fasting and drank water. Your fast…", "Is not broken", ["Is broken and must be made up", "Needs expiation", "Becomes voluntary"]),
    ("Does applying kohl break the fast?", "No", ["Yes", "Only in Ramadan", "Only if done at night"]),
    ("Waking up in janabah while fasting…", "Does not break the fast", ["Breaks it", "Requires expiation", "Makes the fast disliked and void"]),
   ]),
  ("Breaking the fast on purpose", [
    ("The serious ones", "Deliberately eating, drinking, or having intercourse during a Ramadan fast, with no excuse and not forced, requires a make-up day and the expiation.", "Nur al-Idah"),
    ("The expiation", "Fast two months in a row. If you truly cannot, feed sixty poor people two meals each, or give their value.", "Nur al-Idah"),
    ("Make-up only", "Some things break the fast but need only a make-up day, such as swallowing a pebble, or medicine reaching the stomach.", "Nur al-Idah"),
   ], [
    ("Someone eats on purpose in Ramadan with no excuse. What is due?", "A make-up day and the expiation", ["Only a make-up day", "Only charity", "Nothing if they repent"]),
    ("The expiation for breaking a Ramadan fast, for one who can fast, is…", "Fasting two months in a row", ["Fasting ten days", "Fasting three days", "Feeding one poor person"]),
    ("Swallowing a small pebble while fasting requires…", "A make-up day only", ["The expiation", "Nothing", "Repeating the whole month"]),
   ]),
  ("Who may leave the fast", [
    ("Travel and illness", "A traveller and someone who is ill may break the fast and make it up later.", "Nur al-Idah"),
    ("Menstruation", "A woman in menstruation or post-natal bleeding does not fast, and makes up the days later. She does not make up the prayers.", "Nur al-Idah"),
    ("The very old", "Someone too old to fast who will not become able gives a fidyah for each day instead.", "Nur al-Idah"),
   ], [
    ("A woman misses fasts because of menstruation. She…", "Makes up the fasts later", ["Never makes them up", "Makes up the prayers too", "Pays expiation"]),
    ("Who may break the fast and make it up later?", "A traveller", ["Someone who feels tired", "Someone with guests", "Someone at work"]),
    ("A very old person who cannot fast…", "Gives a fidyah for each day", ["Must fast anyway", "Fasts double later", "Does nothing at all"]),
   ]),
 ]),
 ("zakat", "Zakat", "Who pays, how much, and who may receive it", "#1F6F78", [
  ("Who pays zakat", [
    ("The person", "Zakat is fard on a free, adult, sane Muslim who fully owns the nisab, once a full (lunar) year has passed on it.", "Mukhtasar al-Quduri"),
    ("The nisab", "The nisab is 200 dirhams of silver or 20 mithqals of gold, or the same value in money or trade goods.", "Mukhtasar al-Quduri"),
    ("Debts", "Take away what you owe. If what remains still reaches the nisab, zakat is due on it.", "Mukhtasar al-Quduri"),
   ], [
    ("When does zakat become due on wealth?", "When a full year has passed on the nisab", ["As soon as you earn it", "Only in Ramadan", "Every month"]),
    ("What is the nisab of gold?", "20 mithqals", ["200 mithqals", "5 mithqals", "20 dirhams"]),
    ("A person has the nisab but also debts. What happens?", "The debt is taken away first; zakat is due if the rest reaches the nisab", ["Debts are ignored", "Zakat is doubled", "No zakat is ever due"]),
   ]),
  ("How much, and on what", [
    ("The rate", "Zakat on gold, silver, money and trade goods is a fortieth (2.5%).", "Mukhtasar al-Quduri"),
    ("Trade goods", "Goods bought to sell are valued, and zakat is paid on their value.", "Mukhtasar al-Quduri"),
    ("Giving it quietly", "You don't have to say 'this is zakat'. You may give it like a gift, as long as you intend it as zakat.", "Mukhtasar al-Quduri"),
   ], [
    ("What is the rate of zakat on money?", "2.5% (a fortieth)", ["10%", "5%", "20%"]),
    ("Must you tell the poor person 'this is zakat'?", "No, the intention is enough", ["Yes, or it does not count", "Only for large amounts", "Only to relatives"]),
    ("Is zakat due on goods you bought to sell?", "Yes, on their value", ["No, never", "Only on food", "Only if you sell them that year"]),
   ]),
  ("Who may receive zakat", [
    ("The recipients", "The poor, the needy, those who collect it, those in debt, those striving in the path of Allah, the stranded traveller, and (in its time) freeing captives.", "Mukhtasar al-Quduri"),
    ("Family", "You may not give your zakat to your parents, grandparents, children or grandchildren, nor to your spouse (a wife giving to her husband is also not allowed, in Imam Abu Hanifah's view).", "Mukhtasar al-Quduri"),
    ("Banu Hashim", "Zakat may not be given to Banu Hashim, the family of the Prophet ﷺ, even if they are poor. Help them with gifts instead.", "Mukhtasar al-Quduri"),
   ], [
    ("Can you give your zakat to your own mother?", "No", ["Yes, she has priority", "Only half of it", "Only if she asks"]),
    ("How are poor descendants of Banu Hashim helped?", "With gifts and charity that is not zakat", ["With zakat like anyone else", "They are not helped", "Only with zakat al-fitr"]),
    ("Which may receive zakat?", "A stranded traveller in need", ["A wealthy friend", "Your own child", "A mosque building fund"]),
   ]),
 ]),
 ("heart", "The heart", "Tazkiyah: sincerity, repentance and guarding yourself", "#5C6B2E", [
  ("Sincerity", [
    ("Why you seek knowledge", "Imam al-Ghazali رحمه الله begins by asking why you seek knowledge. If it is to compete, show off and win people's attention, you are tearing down your religion. If it is for guidance, the angels spread their wings for you as you walk.", "Bidayat al-Hidayah"),
    ("The heart first", "The Prophet ﷺ said: 'Actions are only by intentions, and each person will have only what he intended.'", "Hadith, al-Bukhari"),
   ], [
    ("According to al-Ghazali, seeking knowledge to show off…", "Tears down your religion", ["Is fine if the knowledge is true", "Doubles your reward", "Is the best intention"]),
    ("According to the hadith, actions are judged by…", "Their intentions", ["Their size", "How many people see them", "How hard they are"]),
   ]),
  ("Repentance", [
    ("What it is", "Repentance (tawbah) means turning back from what the Shari'ah blames to what it praises.", "al-Risalah al-Qushayriyyah"),
    ("Its three conditions", "Regret for what you did, stopping the sin straight away, and resolving never to return to it.", "al-Risalah al-Qushayriyyah"),
    ("Rights of people", "If the sin wronged another person, there is a fourth condition: freeing yourself of their right, by returning what you took or asking their forgiveness.", "Riyad al-Salihin, chapter on repentance"),
   ], [
    ("Which is a condition of repentance?", "Regretting the sin", ["Telling people about it", "Waiting until old age", "Doing it less often"]),
    ("How many conditions does al-Qushayri give for repentance?", "Three", ["One", "Five", "Seven"]),
    ("Repentance means turning…", "From what the Shari'ah blames to what it praises", ["From one school to another", "Away from people", "From work to worship"]),
   ]),
  ("Guarding the tongue", [
    ("The danger", "Al-Ghazali warns of the faults of the tongue, among them lying, backbiting, arguing, praising yourself and cursing.", "Bidayat al-Hidayah"),
    ("Backbiting", "The Prophet ﷺ described backbiting as mentioning your brother with something he would dislike. If it is true, it is backbiting; if it is false, it is slander.", "Hadith, Muslim"),
    ("Silence", "The Prophet ﷺ said: 'Whoever believes in Allah and the Last Day, let him say what is good or stay silent.'", "Hadith, al-Bukhari and Muslim"),
   ], [
    ("Mentioning a brother's real fault behind his back is…", "Backbiting", ["Allowed because it is true", "Advice", "Slander only if false"]),
    ("Which is one of the faults of the tongue al-Ghazali lists?", "Praising yourself", ["Saying salam", "Reciting Qur'an", "Making du'a for others"]),
   ]),
  ("Three illnesses of the heart", [
    ("Envy", "Envy (hasad) is wanting a blessing to leave someone, even when you gain nothing from it. Al-Ghazali quotes the hadith: 'Envy eats good deeds as fire eats wood.'", "Bidayat al-Hidayah"),
    ("Showing off", "Showing off (riya') is the hidden shirk: seeking a place in people's hearts through your worship. Al-Ghazali says most people are ruined by it.", "Bidayat al-Hidayah"),
    ("Self-admiration", "Self-admiration ('ujb) is being pleased with yourself and seeing yourself better than others. It leads to pride.", "Bidayat al-Hidayah"),
   ], [
    ("Wishing someone's blessing would leave them is…", "Envy", ["Ambition", "Showing off", "Self-admiration"]),
    ("Praying longer because people are watching is…", "Showing off (riya')", ["Sincerity", "Patience", "Humility"]),
    ("Seeing yourself as better than others is…", "Self-admiration, which leads to pride", ["Confidence", "Gratitude", "Hope"]),
   ]),
  ("Advice to a student", [
    ("Knowledge and action", "Al-Ghazali wrote to his student: 'Knowledge without action is madness, and action without knowledge does not happen.'", "Ayyuha al-Walad"),
    ("Today matters", "Knowledge will not keep you away from sins today, nor bring you to obey, unless you act on it.", "Ayyuha al-Walad"),
    ("Your time", "Al-Ghazali says: your moments are your life, and your life is your capital. Every breath is a jewel that cannot be replaced once it is gone.", "Bidayat al-Hidayah"),
   ], [
    ("Al-Ghazali said knowledge without action is…", "Madness", ["Enough", "Wisdom", "Better than action"]),
    ("What makes knowledge benefit you?", "Acting on it", ["Memorising more", "Debating others", "Collecting books"]),
    ("Al-Ghazali calls your life…", "Your capital", ["Your test score", "A short dream", "Your reward"]),
   ]),
 ]),
]

if __name__ == "__main__":
    import json
    from learn_extra import ABOUT, WHY
    AR = {"belief":"العقيدة","purity":"الطهارة","prayer":"الصلاة","fasting":"الصوم","zakat":"الزكاة","heart":"تزكية القلب"}
    out = []
    for uid, title, sub, color, lessons in UNITS:
        L = []
        for k, (lt, cards, checks) in enumerate(lessons):
            lid = f"{uid}{k+1}"; why = WHY[lid]; assert len(why) == len(checks), lid
            L.append({"id": lid, "title": lt, "about": ABOUT[lid],
                      "cards": [{"t": t, "x": x, "src": s} for t, x, s in cards],
                      "checks": [{"q": q, "a": a, "w": w, "why": y} for (q, a, w), y in zip(checks, why)]})
            for q, a, w in checks: assert len(w) == 3 and a not in w, (lt, q)
        out.append({"id": uid, "title": title, "ar": AR[uid], "sub": sub, "color": color, "lessons": L})
    json.dump(out, open("app/data/learn.json", "w"), ensure_ascii=False, separators=(",", ":"))
    print("units", len(out), "lessons", sum(len(u["lessons"]) for u in out), "checks", sum(len(l["checks"]) for u in out for l in u["lessons"]))
