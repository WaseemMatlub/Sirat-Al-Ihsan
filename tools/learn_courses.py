"""LEARN courses (Jibreel-style "Switch course"). Each course follows the order of a classical book.
Every card names its book and chapter. Lessons keep their old ids so people's progress carries over.
New lesson: (id, title, about, [cards (title, text, source)], [checks (question, answer, [3 wrong], why)])
Old lessons come from learn_content.UNITS / learn_extra; their sources get a chapter added below.
Written for the app from our library texts; every lesson is to be checked by a teacher."""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from learn_content import UNITS
from learn_extra import ABOUT, WHY

NI, QD, UB, TH, FA = "Nur al-Idah", "Mukhtasar al-Quduri", "Umm al-Barahin", "al-'Aqidah al-Tahawiyyah", "al-Fiqh al-Akbar"
BH, RQ, AW = "Bidayat al-Hidayah", "al-Risalah al-Qushayriyyah", "Ayyuha al-Walad"

# chapter added to an old card whose source is just a book name
CHAPTER = {
 "belief1": {UB: "opening: the three judgements"}, "belief2": {UB: "the necessary attributes", TH: "on Allah's Oneness"},
 "belief3": {UB: "the necessary attributes"}, "belief4": {UB: "the attributes of meaning"},
 "belief5": {UB: "on the Messengers", TH: "on the Prophet ﷺ"}, "belief6": {TH: "on faith and the Companions"},
 "purity1": {NI: "the waters that may be used"}, "purity2": {NI: "the obligations of wudu"},
 "purity3": {NI: "the sunnahs of wudu"}, "purity4": {NI: "what breaks wudu, and what does not"},
 "purity5": {NI: "what makes ghusl necessary, and how it is done"}, "purity6": {NI: "chapter on tayammum"},
 "prayer1": {NI: "the conditions of the prayer"}, "prayer2": {NI: "the pillars of the prayer"},
 "prayer3": {NI: "the wajib acts, and the prostration of forgetfulness"}, "prayer4": {NI: "what breaks the prayer"},
 "prayer5": {NI: "chapter on witr and qunut"},
 "fasting1": {NI: "what does not break the fast"}, "fasting2": {NI: "what breaks the fast and requires expiation"},
 "fasting3": {NI: "excuses for not fasting; the fidyah"},
 "zakat1": {QD: "Book of Zakat"}, "zakat2": {QD: "zakat on silver, gold and trade goods"}, "zakat3": {QD: "who may receive zakat"},
 "heart1": {BH: "introduction"}, "heart2": {RQ: "chapter on repentance"}, "heart3": {BH: "the faults of the tongue"},
 "heart4": {BH: "the faults of the heart"}, "heart5": {AW: "the letter", BH: "on guarding your time"},
}

def L(id, title, about, cards, checks): return (id, title, about, cards, checks)

NEW = {
# ---------------- AQEEDAH (order of Umm al-Barahin, then al-Tahawiyyah) ----------------
"aq_proof": L("aq_proof", "How we know Allah exists", "Imam al-Sanusi's proof from the world around us.", [
  ("Everything changes", "Everything in the world moves, rests, grows and fades. Things that are always changing are things that came into being.", "Umm al-Barahin, proof of His existence"),
  ("It needs a Maker", "What came into being cannot bring itself into being. So the world needs a Maker who did not come into being: Allah.", "Umm al-Barahin, proof of His existence"),
  ("A proof for each", "Imam al-Sanusi رحمه الله gives a proof for every attribute he mentions, so that the believer holds each one with understanding.", "Umm al-Barahin, the proofs of the attributes"),
 ], [
  ("Why does the world need a Maker?", "Because it came into being and cannot bring itself into being", ["Because it is very large", "Because people say so", "Because it will last forever"], "Something that came into being after not existing needs someone to bring it into being. That is Allah, who never came into being.", "Umm al-Barahin"),
  ("What shows the world came into being?", "It is always changing", ["It is very old", "It is beautiful", "It is full of people"], "Al-Sanusi points to the constant change in the world: movement, rest, coming and going. What changes like this came into being.", "Umm al-Barahin"),
  ("Can the Maker of the world have come into being too?", "No, otherwise He would need a maker as well", ["Yes, after the world", "Yes, at the same time as the world", "No one can know"], "If the Maker had come into being He would need a maker too, which never ends. So He has no beginning.", "Umm al-Barahin"),
 ]),
"aq_speech": L("aq_speech", "The Speech of Allah", "The Qur'an is Allah's speech, not created like ours.", [
  ("His speech", "Allah speaks with an eternal speech. The Qur'an is the speech of Allah: it came from Him, without asking how, and He sent it down to His Messenger ﷺ as revelation.", "al-'Aqidah al-Tahawiyyah, on the Qur'an"),
  ("Not like ours", "The believers are certain it is truly Allah's speech, not created like the speech of creation. Whoever hears it and claims it is human speech has disbelieved.", "al-'Aqidah al-Tahawiyyah, on the Qur'an"),
  ("Written, memorised, recited", "Imam Abu Hanifah رحمه الله said: the Qur'an is written in the copies, preserved in the hearts and recited by the tongues. Our pronouncing, writing and reciting it are created; the Qur'an itself is not created.", "al-Fiqh al-Akbar, on the Qur'an"),
 ], [
  ("What is the Qur'an?", "The speech of Allah, not created", ["The words of the Prophet ﷺ", "A book written by the Companions", "Created speech like ours"], "Al-Tahawi: the Qur'an is the speech of Allah, from Him it came, not created like the speech of creation.", "al-'Aqidah al-Tahawiyyah"),
  ("According to Imam Abu Hanifah, which of these is created?", "Our reciting of the Qur'an", ["The Qur'an itself", "Allah's speech", "Allah's knowledge"], "Our pronouncing, writing and reciting are created. The Qur'an, Allah's speech, is not.", "al-Fiqh al-Akbar"),
  ("Where is the Qur'an, according to al-Fiqh al-Akbar?", "Written in the copies, preserved in hearts, recited by tongues", ["Only in the copies", "Only in the hearts", "Only in the Preserved Tablet"], "Abu Hanifah described it in all three ways: written, preserved in hearts and recited by tongues.", "al-Fiqh al-Akbar"),
 ]),
"aq_jaiz": L("aq_jaiz", "What is impossible and possible for Allah", "The opposites of His attributes, and what He freely does.", [
  ("Impossible for Him", "The opposite of every necessary attribute is impossible for Allah: non-existence, having a beginning or end, resembling creation, needing anything, having a partner, weakness, ignorance, death and so on.", "Umm al-Barahin, what is impossible for Allah"),
  ("Possible for Him", "What is possible for Allah is doing or leaving anything that is possible. Nothing obliges Him: if He rewards us it is pure bounty, and if He punishes it is pure justice.", "Umm al-Barahin, what is possible for Allah; Jawharat al-Tawhid"),
  ("Why it matters", "This protects you from two mistakes: thinking Allah is like us, and thinking anything is forced upon Him.", "Umm al-Barahin, what is possible for Allah"),
 ], [
  ("Which is impossible for Allah?", "Needing anything", ["Creating whatever He wills", "Forgiving whom He wills", "Giving provision"], "Needing is the opposite of qiyam bi-nafsihi (standing by Himself), so it is impossible for Allah.", "Umm al-Barahin"),
  ("What is possible for Allah?", "Doing or leaving anything possible", ["Only what His creation asks", "Only what is best for creation", "Nothing at all"], "Al-Sanusi: what is possible for Allah is doing or leaving any possible thing.", "Umm al-Barahin"),
  ("Is Allah obliged to reward anyone?", "No, His reward is from His bounty", ["Yes, always", "Yes, if they pray", "Only the Prophets"], "Nothing is obligatory upon Allah. Al-Laqqani: if He rewards us it is pure bounty.", "Jawharat al-Tawhid"),
 ]),
"aq_shahada": L("aq_shahada", "The meaning of the Shahadah", "How 'la ilaha illa Allah' gathers all of belief.", [
  ("Everything in two phrases", "Imam al-Sanusi ends by showing that all of belief is gathered in 'La ilaha illa Allah, Muhammadun Rasulullah'.", "Umm al-Barahin, the meaning of the Shahadah"),
  ("No god but Allah", "Its meaning: there is none who is free of need of everything else, and whom everything else needs, except Allah. Every attribute we learnt follows from this.", "Umm al-Barahin, the meaning of the Shahadah"),
  ("Muhammad is the Messenger", "'Muhammadun Rasulullah' brings in belief in all the Prophets and angels, the books and the Last Day, because he ﷺ came with all of it. So say it often, knowing what it means.", "Umm al-Barahin, the meaning of the Shahadah"),
 ], [
  ("What does 'la ilaha illa Allah' mean, according to al-Sanusi?", "None is free of need of all else, and needed by all, except Allah", ["Allah is the greatest god", "There are many gods but Allah is the best", "Allah is in every place"], "Al-Sanusi explains it as: none is free of need of everything else and needed by everything else except Allah.", "Umm al-Barahin"),
  ("Belief in the angels and the Last Day is contained in…", "'Muhammadun Rasulullah'", ["Only the opening takbir", "The adhan alone", "Nothing in the Shahadah"], "Accepting the Messenger ﷺ means accepting everything he brought, including the angels, the books and the Last Day.", "Umm al-Barahin"),
  ("What does al-Sanusi advise about the Shahadah?", "Say it often, knowing its meaning", ["Say it once in your life", "Only say it in prayer", "Leave it to scholars"], "He closes by urging the believer to say it often while aware of what it means.", "Umm al-Barahin"),
 ]),
"aq_akhira": L("aq_akhira", "The grave and the Last Day", "What al-Tahawi tells us to believe about what comes after death.", [
  ("The grave", "We believe in the punishment of the grave for those who deserve it, and in the questioning by Munkar and Nakir about one's Lord, religion and Prophet. The grave is a garden of Paradise or a pit of the Fire.", "al-'Aqidah al-Tahawiyyah, on the hereafter"),
  ("The Day", "We believe in the resurrection, the recompense of deeds on the Day of Judgement, the presenting of records, the reckoning, the reading of the book, the reward and punishment, the Bridge and the Scales.", "al-'Aqidah al-Tahawiyyah, on the hereafter"),
  ("Pool and intercession", "The Pool (hawd) with which Allah honoured the Prophet ﷺ, to quench his Ummah, is true. The intercession he has stored for them is true.", "al-'Aqidah al-Tahawiyyah, the Pool and the intercession"),
  ("Paradise and the Fire", "Paradise and the Fire are created. They will never end and never perish.", "al-'Aqidah al-Tahawiyyah, on Paradise and the Fire"),
 ], [
  ("Who questions a person in the grave?", "Munkar and Nakir", ["Jibril and Mika'il", "The recording angels", "No one"], "Al-Tahawi: we believe in the questioning of Munkar and Nakir about one's Lord, religion and Prophet.", "al-'Aqidah al-Tahawiyyah"),
  ("What does al-Tahawi say about Paradise and the Fire?", "They are created and will never end", ["They will be created on the Last Day", "They end after a long time", "Only Paradise lasts forever"], "They are already created, and they never end or perish.", "al-'Aqidah al-Tahawiyyah"),
  ("The Pool (hawd) is…", "True: Allah honoured the Prophet ﷺ with it for his Ummah", ["A symbol only", "For the Prophets alone", "A pool in this world"], "Al-Tahawi affirms the Pool as true, an honour for the Prophet ﷺ to quench his Ummah.", "al-'Aqidah al-Tahawiyyah"),
 ]),
"aq_awliya": L("aq_awliya", "Prophets, saints and wonders", "The rank of the awliya' and their karamat.", [
  ("Prophets first", "We do not prefer any wali to any Prophet عليهم السلام. One Prophet is better than all the awliya' together.", "al-'Aqidah al-Tahawiyyah, Prophets and awliya'"),
  ("Their wonders are true", "We believe in the wonders (karamat) of the awliya' that are reported by trustworthy narrators.", "al-'Aqidah al-Tahawiyyah, Prophets and awliya'"),
  ("Who is a wali", "The believers are all friends (awliya') of the Most Merciful. The most honoured of them with Allah are the most obedient and the best followers of the Qur'an.", "al-'Aqidah al-Tahawiyyah, on faith"),
 ], [
  ("Can a wali be better than a Prophet?", "No, one Prophet is better than all the awliya'", ["Yes, the greatest ones", "Yes, if he has karamat", "They are equal"], "Al-Tahawi: one Prophet is better than all the awliya' together.", "al-'Aqidah al-Tahawiyyah"),
  ("The karamat of the awliya' are…", "True, when reported by trustworthy narrators", ["Never possible", "Only stories", "Signs of prophethood"], "We believe in their wonders, as reported by trustworthy narrators.", "al-'Aqidah al-Tahawiyyah"),
  ("Who is most honoured with Allah?", "The most obedient and best follower of the Qur'an", ["The one with the most wonders", "The one with most followers", "The one from the best family"], "Al-Tahawi ties honour with Allah to obedience and following the Qur'an.", "al-'Aqidah al-Tahawiyyah"),
 ]),
"aq_qadr": L("aq_qadr", "Allah's decree (qadr)", "Everything happens by His knowledge and will.", [
  ("Known and written", "Allah knew everything before creating it, and decreed it. Nothing happens in His kingdom except what He wills.", "al-'Aqidah al-Tahawiyyah, on decree"),
  ("Do not dig too deep", "The decree is Allah's secret in His creation. No angel near to Him nor Prophet sent has been shown it. Looking too deeply into it leads to ruin.", "al-'Aqidah al-Tahawiyyah, on decree"),
  ("Our part", "Our actions are created by Allah and earned (kasb) by us. So we act, we take responsibility, and we trust Him.", "al-'Aqidah al-Tahawiyyah, on decree"),
 ], [
  ("What happens in Allah's kingdom?", "Only what He wills", ["Whatever people want", "Some things against His will", "Only good things"], "Al-Tahawi: nothing happens except what He wills.", "al-'Aqidah al-Tahawiyyah"),
  ("What does al-Tahawi say about looking deeply into decree?", "It is Allah's secret; delving into it leads to ruin", ["Everyone must study it in detail", "It is easy to understand", "Only Prophets may ask about it"], "The decree is Allah's secret in His creation; no one has been shown it.", "al-'Aqidah al-Tahawiyyah"),
  ("Our actions are…", "Created by Allah and earned by us", ["Created by us alone", "Forced on us with no choice", "Not known to Allah beforehand"], "They are Allah's creation and our earning (kasb), so we are responsible for them.", "al-'Aqidah al-Tahawiyyah"),
 ]),

# ---------------- FIQH (order of Nur al-Idah; zakat from al-Quduri) ----------------
"fiqh0": L("fiqh0", "Foundations: fard, wajib and sunnah", "The school we follow and the words fiqh uses.", [
  ("Our school", "This course follows the Hanafi school of Imam Abu Hanifah al-Nu'man رحمه الله, through Nur al-Idah of Imam al-Shurunbulali رحمه الله and Mukhtasar al-Quduri of Imam al-Quduri رحمه الله.", "Nur al-Idah; Mukhtasar al-Quduri"),
  ("Fard", "Fard is what is established by a definitive proof with no doubt in it. You must act on it and believe in it.", "Usul al-Shashi, on fard and wajib"),
  ("Wajib", "Wajib is established by a proof with some doubt in it. It is like fard in action, so you may not leave it, but you are not required to believe in it with certainty as you do with fard.", "Usul al-Shashi, on fard and wajib"),
 ], [
  ("Fard is established by…", "A definitive proof with no doubt in it", ["A proof with some doubt", "The habit of a town", "A scholar's preference"], "Al-Shashi: fard is what is established by a definitive proof with no doubt in it.", "Usul al-Shashi"),
  ("Can you leave a wajib act?", "No, it is like fard in action", ["Yes, it is optional", "Yes, if you are busy", "Only in Ramadan"], "Wajib is like fard in action: you may not leave it.", "Usul al-Shashi"),
  ("How is wajib different from fard?", "You are not required to believe in it with certainty", ["It is more important than fard", "You may leave it freely", "It has no reward"], "Wajib is fard in action but not in belief, because its proof carries some doubt.", "Usul al-Shashi"),
 ]),
"fiqh_khuff": L("fiqh_khuff", "Wiping over leather socks (khuffs)", "When you may wipe, for how long, and how.", [
  ("How long", "A resident wipes for one day and night, a traveller for three days and nights. The time starts from the first thing that breaks wudu after putting them on.", "Nur al-Idah, the time limit for wiping"),
  ("Conditions", "Put them on after washing the feet, in wudu. They must cover the ankles, be strong enough to walk in, and have no hole the size of three small toes.", "Nur al-Idah, conditions for wiping"),
  ("How to wipe", "The fard is wiping the top of the front of each foot, the size of three of the hand's small fingers. The sunnah is drawing spread fingers from the toes up towards the shin.", "Nur al-Idah, the amount that is fard"),
 ], [
  ("How long may a traveller wipe?", "Three days and nights", ["One day and night", "Until the journey ends", "One week"], "A resident wipes one day and night; a traveller three days and nights.", "Nur al-Idah"),
  ("When does the time start?", "From the first thing that breaks wudu after putting them on", ["When you put them on", "At Fajr", "When you first wipe"], "Nur al-Idah: the time starts from the hadath after wearing the khuffs.", "Nur al-Idah"),
  ("What is the fard amount to wipe?", "Three of the hand's small fingers on the top of each foot", ["The whole sock", "The sole of the foot", "Any single touch"], "The fard is the size of three small fingers on the top front of each foot.", "Nur al-Idah"),
 ]),
"fiqh_hayd": L("fiqh_hayd", "Menstruation and post-natal bleeding", "Its length and what is not allowed during it.", [
  ("How long", "The least menstruation is three days and the most is ten. Post-natal bleeding (nifas) is at most forty days, with no minimum.", "Nur al-Idah, chapter on menstruation"),
  ("What is not allowed", "During menstruation and nifas: prayer, fasting, reciting a verse of the Qur'an, touching the Qur'an without a cover, entering a masjid, tawaf, and intercourse.", "Nur al-Idah, what menstruation forbids"),
  ("Making up", "She makes up the fasts she missed, but not the prayers.", "Nur al-Idah, making up the obligations"),
 ], [
  ("What is the longest menstruation in the Hanafi school?", "Ten days", ["Seven days", "Fifteen days", "There is no limit"], "Nur al-Idah: the least is three days and the most is ten.", "Nur al-Idah"),
  ("What is the longest nifas?", "Forty days", ["Ten days", "Sixty days", "Two weeks"], "Nifas is at most forty days, with no minimum.", "Nur al-Idah"),
  ("After menstruation, what does she make up?", "The fasts, not the prayers", ["The prayers and the fasts", "The prayers only", "Nothing"], "She makes up the missed fasts but not the prayers.", "Nur al-Idah"),
 ]),

# ---------------- HALAL & HARAM (Ihya, Book of the Lawful and Unlawful; al-Quduri) ----------------
"hh1": L("hh1", "Why halal matters", "Al-Ghazali on the lawful and the unlawful.", [
  ("Good accepts good", "The Prophet ﷺ said Allah is good and accepts only what is good. He mentioned a traveller, dishevelled and dusty, raising his hands: 'O Lord!', while his food, drink and clothing are haram. 'How can he be answered?'", "Hadith, Sahih Muslim; quoted in Ihya', Book of the Lawful and Unlawful"),
  ("Where he begins", "Imam al-Ghazali رحمه الله opens this book with the virtue of the lawful and the blame of the unlawful, bringing verses and hadiths on how what we consume affects our worship.", "Ihya' 'Ulum al-Din, Book of the Lawful and Unlawful"),
  ("Clear and doubtful", "The Prophet ﷺ said: the halal is clear and the haram is clear, and between them are doubtful matters. Whoever avoids the doubtful has protected his religion and honour.", "Hadith, al-Bukhari and Muslim (al-Nawawi's Forty, 6)"),
 ], [
  ("Why was the traveller's du'a not answered?", "His food, drink and clothing were haram", ["He did not raise his hands", "He was travelling", "He was dusty"], "In the hadith, the reason given is that his food, drink and clothing were haram.", "Sahih Muslim"),
  ("Between clear halal and clear haram are…", "Doubtful matters", ["Nothing", "Only recommended things", "Only disliked things"], "Between them are doubtful matters that many people do not know.", "al-Bukhari and Muslim"),
  ("Avoiding doubtful things protects…", "Your religion and your honour", ["Only your wealth", "Only your health", "Nothing"], "'Whoever avoids the doubtful has protected his religion and his honour.'", "al-Bukhari and Muslim"),
 ]),
"hh2": L("hh2", "The four degrees of carefulness", "Al-Ghazali's levels of wara'.", [
  ("First and second", "The first degree, of the upright, is avoiding what the fatwa says is haram. The second, of the righteous, is also avoiding what is doubtful.", "Ihya', Book of the Lawful and Unlawful, the degrees of wara'"),
  ("Third", "The third, of the God-fearing, is leaving some things that are fine for fear they lead to what is not.", "Ihya', Book of the Lawful and Unlawful, the degrees of wara'"),
  ("Fourth", "The fourth, of the siddiqin, is leaving even what is harmless if it is taken for other than Allah, or not to gain strength for His worship.", "Ihya', Book of the Lawful and Unlawful, the degrees of wara'"),
 ], [
  ("Avoiding what the fatwa calls haram is the wara' of…", "The upright ('udul)", ["The siddiqin", "The God-fearing", "No one: it is optional"], "The first degree, required of everyone, is the wara' of the upright.", "Ihya'"),
  ("Leaving harmless things done for other than Allah is the wara' of…", "The siddiqin", ["The upright", "The righteous", "The scholars of fiqh"], "Al-Ghazali calls this highest degree the wara' of the siddiqin.", "Ihya'"),
  ("How many degrees of wara' does al-Ghazali give?", "Four", ["Two", "Three", "Seven"], "He describes four: of the upright, the righteous, the God-fearing and the siddiqin.", "Ihya'"),
 ]),
"hh3": L("hh3", "Food and slaughter", "What may be eaten, and whose slaughter is lawful.", [
  ("Whose slaughter", "The slaughter of a Muslim or of a Jew or Christian (Ahl al-Kitab) is halal. The slaughter of a Magian, an apostate or an idol-worshipper is not eaten.", "Mukhtasar al-Quduri, Book of Hunting and Slaughter"),
  ("The name of Allah", "If the one slaughtering leaves out Allah's name on purpose, the animal is carrion and may not be eaten. If he forgot, it may be eaten.", "Mukhtasar al-Quduri, Book of Hunting and Slaughter"),
  ("From the water", "Of sea creatures, only fish are eaten in the Hanafi school, and a fish that died by itself and floats is disliked. Locusts may be eaten without slaughter.", "Mukhtasar al-Quduri, Book of Hunting and Slaughter"),
 ], [
  ("Is meat slaughtered by a Christian halal?", "Yes, the slaughter of Ahl al-Kitab is halal", ["No, never", "Only if a Muslim watches", "Only chicken"], "Al-Quduri: the slaughter of a Muslim or a Kitabi is halal.", "Mukhtasar al-Quduri"),
  ("The slaughterer forgot to say bismillah. The meat…", "May be eaten", ["Is carrion", "Is disliked", "Must be given away"], "Leaving it out by forgetting does not make it haram; leaving it on purpose does.", "Mukhtasar al-Quduri"),
  ("Which sea creatures may be eaten in the Hanafi school?", "Fish only", ["Everything from the sea", "Fish and crabs", "Only shellfish"], "Al-Quduri: of water animals, only fish are eaten.", "Mukhtasar al-Quduri"),
 ]),
"hh4": L("hh4", "Gold, silk and vessels", "What men and women may wear and use.", [
  ("Silk", "Silk is not lawful for men to wear, and it is lawful for women.", "Mukhtasar al-Quduri, Book of the Forbidden and the Permitted"),
  ("Gold and silver", "Men may not wear gold or silver, except a silver ring, a belt fitting and a sword decoration of silver. Women may wear gold and silver.", "Mukhtasar al-Quduri, Book of the Forbidden and the Permitted"),
  ("Vessels", "Eating, drinking, oiling and perfuming from vessels of gold and silver is not allowed, for men or women. Glass and crystal are fine.", "Mukhtasar al-Quduri, Book of the Forbidden and the Permitted"),
 ], [
  ("May a man wear a gold ring?", "No, only a silver ring", ["Yes, a small one", "Yes, if it is a wedding ring", "Only on Eid"], "Men may not wear gold; a silver ring is allowed.", "Mukhtasar al-Quduri"),
  ("Drinking from a silver cup is…", "Not allowed for men or women", ["Allowed for women", "Allowed for guests", "Disliked only for men"], "Eating and drinking from gold and silver vessels is not allowed for either.", "Mukhtasar al-Quduri"),
  ("Wearing silk is lawful for…", "Women", ["Men", "Both", "Neither"], "Silk is not lawful for men to wear, and lawful for women.", "Mukhtasar al-Quduri"),
 ]),
"hh5": L("hh5", "Lowering the gaze", "What may be looked at, according to al-Quduri.", [
  ("Non-mahram women", "A man may not look at a woman who is not his mahram except at her face and hands. If he is not safe from desire, he does not look even at her face, except for a need.", "Mukhtasar al-Quduri, Book of the Forbidden and the Permitted"),
  ("Needs", "A judge, a witness and a doctor may look as their work requires.", "Mukhtasar al-Quduri, Book of the Forbidden and the Permitted"),
  ("Between men", "A man may look at another man except between the navel and the knee.", "Mukhtasar al-Quduri, Book of the Forbidden and the Permitted"),
 ], [
  ("If a man fears desire, may he look at a non-mahram's face?", "No, except for a need", ["Yes, always", "Yes, briefly", "Only at weddings"], "Al-Quduri: if he is not safe from desire he does not look even at her face, except for a need.", "Mukhtasar al-Quduri"),
  ("Which part of a man may another man not look at?", "Between the navel and the knee", ["Only the face", "The arms", "Nothing at all"], "Between the navel and the knee is 'awrah for men.", "Mukhtasar al-Quduri"),
  ("Who may look as their work requires?", "A doctor", ["A shopkeeper", "Anyone curious", "A neighbour"], "A judge, a witness and a doctor may look as needed.", "Mukhtasar al-Quduri"),
 ]),
"hh6": L("hh6", "Riba (interest)", "What riba is, and why it is so serious.", [
  ("It is haram", "Riba is haram. The Prophet ﷺ cursed the one who consumes riba, the one who pays it, the one who writes it and its two witnesses, and said: they are all the same.", "Hadith, Sahih Muslim"),
  ("What it is", "Al-Quduri: riba is in anything measured by volume or weight, when sold for the same kind with an increase. Like for like is allowed; with an increase it is not.", "Mukhtasar al-Quduri, Chapter on Riba"),
  ("In the market", "Al-Ghazali lists riba among the common wrongs of the marketplace that must be stopped.", "Ihya' 'Ulum al-Din, Book of Commanding Good"),
 ], [
  ("Who did the Prophet ﷺ curse in the hadith on riba?", "The one who takes it, pays it, writes it and witnesses it", ["Only the one who takes it", "Only the bank", "No one"], "All four were cursed, and he said they are all the same.", "Sahih Muslim"),
  ("Selling a kilo of dates for two kilos of dates, on the spot, is…", "Riba", ["Allowed", "Recommended", "Disliked only"], "Same kind, weighed or measured, with an increase is riba.", "Mukhtasar al-Quduri"),
  ("Selling gold for the same weight of gold, hand to hand, is…", "Allowed", ["Riba", "Disliked", "Allowed only for women"], "Like for like of the same kind is allowed.", "Mukhtasar al-Quduri"),
 ]),

# ---------------- DEALING WITH DOUBTS (al-Munqidh min al-Dalal) ----------------
"dd1": L("dd1", "A doubt is not disbelief", "What the Prophet ﷺ said to Companions troubled by thoughts.", [
  ("Clear faith", "Some Companions told the Prophet ﷺ they found thoughts in themselves too terrible to speak. He asked, 'Do you really find that?' They said yes. He said: 'That is clear faith.'", "Hadith, Sahih Muslim, Book of Faith"),
  ("What to do", "The Prophet ﷺ said Shaytan comes and asks: who created this, who created that, until he asks who created your Lord. When that happens, seek refuge in Allah and stop.", "Hadith, al-Bukhari and Muslim"),
  ("Hating it is a sign", "Being troubled by such a thought shows your faith rejects it. You are not blamed for a passing thought.", "Hadith, Sahih Muslim, Book of Faith"),
 ], [
  ("What did the Prophet ﷺ call hating these whispers?", "Clear faith", ["Weak faith", "Hypocrisy", "Disbelief"], "He said, 'That is clear faith', about the Companions who were troubled by them.", "Sahih Muslim"),
  ("When the thought 'who created Allah?' comes, you should…", "Seek refuge in Allah and stop", ["Keep thinking about it alone", "Hide it and feel guilty", "Stop praying"], "The hadith's instruction is to seek refuge in Allah and stop.", "al-Bukhari and Muslim"),
  ("Is a person sinful for a passing doubt they dislike?", "No", ["Yes, always", "Only if it lasts a day", "Only scholars are excused"], "Disliking it shows faith; a passing thought is not held against you.", "Sahih Muslim"),
 ]),
"dd2": L("dd2", "Al-Ghazali's own doubts", "A great Imam's honest account of his crisis.", [
  ("He went through it", "Imam al-Ghazali رحمه الله wrote that doubt overcame him so strongly that for nearly two months he could not trust even the basic truths of the mind.", "al-Munqidh min al-Dalal, introduction"),
  ("How it ended", "He was cured, he says, not by arranging proofs, but by a light that Allah cast into his breast. That light is the key to most knowledge.", "al-Munqidh min al-Dalal, introduction"),
  ("Mercy is wide", "Al-Ghazali warns that whoever thinks unveiling depends only on written proofs has narrowed the vast mercy of Allah.", "al-Munqidh min al-Dalal, introduction"),
 ], [
  ("How long did al-Ghazali's worst doubt last?", "Nearly two months", ["Ten years", "One night", "His whole life"], "He says it lasted close to two months.", "al-Munqidh"),
  ("What cured al-Ghazali, in his words?", "A light Allah cast into his breast", ["A debate he won", "A book of philosophy", "Travelling to Makkah"], "Not arranged proofs but a light Allah cast into his breast.", "al-Munqidh"),
  ("What does al-Ghazali say about Allah's mercy?", "It is wider than written proofs alone", ["It only comes through proofs", "It is limited to scholars", "It comes after death only"], "Thinking unveiling depends only on proofs narrows Allah's vast mercy.", "al-Munqidh"),
 ]),
"dd3": L("dd3", "Know the truth, then its people", "Judging ideas by truth, not by who says them.", [
  ("Ali's rule", "Al-Ghazali quotes 'Ali ibn Abi Talib رضي الله عنه: 'Do not know the truth by men. Know the truth, and you will know its people.'", "al-Munqidh min al-Dalal, on the sciences of the philosophers"),
  ("Weak minds", "He says it is the habit of weak minds to know truth by people, instead of knowing people by the truth.", "al-Munqidh min al-Dalal, on the sciences of the philosophers"),
  ("He studied them all", "Al-Ghazali examined the theologians, the philosophers, the Batinis and the Sufis, and found what he sought in the way of the Sufis: knowledge joined with action.", "al-Munqidh min al-Dalal, the ways of the Sufis"),
 ], [
  ("Who said 'Know the truth and you will know its people'?", "'Ali ibn Abi Talib رضي الله عنه", ["Abu Hanifah", "al-Ghazali himself", "Ibn Sina"], "Al-Ghazali quotes it from 'Ali رضي الله عنه.", "al-Munqidh"),
  ("Al-Ghazali calls knowing truth by people…", "The habit of weak minds", ["The best method", "Required for everyone", "The way of the Sufis"], "He says the intelligent person knows people by the truth, not the other way round.", "al-Munqidh"),
  ("Where did al-Ghazali find what he was seeking?", "The way of the Sufis", ["Philosophy", "The Batinis", "Arguing with people"], "He found it in the way of the Sufis, which joins knowledge and action.", "al-Munqidh"),
 ]),
"dd4": L("dd4", "How we know the Prophet ﷺ is true", "Al-Ghazali's way to certainty about prophethood.", [
  ("Like knowing a doctor", "Al-Ghazali says: if you know some medicine, you can recognise a real doctor by his words and his work. In the same way you can come to know the Prophet ﷺ by his words and states.", "al-Munqidh min al-Dalal, the reality of prophethood"),
  ("Test it yourself", "Then strengthen it by experience: act on what he ﷺ taught about worship, and see how it purifies the heart.", "al-Munqidh min al-Dalal, the reality of prophethood"),
  ("Act on what you know", "Al-Ghazali cites: 'Whoever acts on what he knows, Allah gives him knowledge of what he did not know.' You will find it true.", "al-Munqidh min al-Dalal, the reality of prophethood"),
 ], [
  ("Al-Ghazali compares knowing the Prophet ﷺ to knowing…", "A real doctor by his words and work", ["A king by his crown", "A rich man by his house", "A stranger by his name"], "As you can recognise a real doctor or faqih, you can recognise the Prophet ﷺ.", "al-Munqidh"),
  ("How does al-Ghazali say certainty is strengthened?", "By acting on his teachings and seeing their effect on the heart", ["By reading philosophy", "By waiting for a miracle", "By arguing"], "Experience of his teachings purifying the heart strengthens certainty.", "al-Munqidh"),
  ("Whoever acts on what he knows…", "Allah gives him knowledge of what he did not know", ["Needs no teacher", "Will never doubt again", "Must stop learning"], "Al-Ghazali cites this saying as something you will find true by experience.", "al-Munqidh"),
 ]),
"dd5": L("dd5", "Leave what makes you doubt", "Simple Prophetic advice for daily doubts.", [
  ("The rule", "The Prophet ﷺ said: 'Leave what makes you doubt for what does not make you doubt.'", "Hadith, al-Tirmidhi and al-Nasa'i (al-Nawawi's Forty, 11)"),
  ("Ask people of knowledge", "Allah says: 'Ask the people of remembrance if you do not know.' (al-Nahl 43) Doubts are answered by learning, not by hiding them.", "Qur'an, al-Nahl 43"),
  ("Turn to Allah", "Al-Ghazali describes leaving his position in Baghdad and turning to seclusion, disciplining the self and the remembrance of Allah.", "al-Munqidh min al-Dalal, the ways of the Sufis"),
 ], [
  ("'Leave what makes you doubt for…'", "What does not make you doubt", ["Whatever you like", "What others do", "Nothing at all"], "The hadith: leave what makes you doubt for what does not.", "al-Nawawi's Forty"),
  ("If you have a question about the religion, you should…", "Ask the people of knowledge", ["Keep it to yourself forever", "Search random videos only", "Stop practising"], "'Ask the people of remembrance if you do not know.' (al-Nahl 43)", "Qur'an"),
  ("What did al-Ghazali turn to besides study?", "Seclusion, self-discipline and remembrance of Allah", ["Leaving the religion", "More debates", "Worldly fame"], "In al-Munqidh he describes leaving Baghdad for seclusion, discipline and dhikr.", "al-Munqidh"),
 ]),

# ---------------- SEERAH (order of Ibn Kathir's al-Fusul fi Sirat al-Rasul ﷺ) ----------------
"sr1": L("sr1", "His lineage and birth ﷺ", "The Prophet's family and early years.", [
  ("His name", "Muhammad ﷺ, son of 'Abdullah, son of 'Abd al-Muttalib, son of Hashim, of Quraysh, from the descendants of Isma'il عليه السلام.", "al-Fusul fi Sirat al-Rasul, his lineage"),
  ("His birth", "He ﷺ was born on a Monday in Rabi' al-Awwal, in the Year of the Elephant, according to the sound view.", "al-Fusul fi Sirat al-Rasul, his birth and nursing"),
  ("An orphan", "His father died before he was born. His mother Aminah died when he was six, his grandfather 'Abd al-Muttalib when he was eight; then his uncle Abu Talib took care of him.", "al-Fusul fi Sirat al-Rasul, his birth and nursing"),
 ], [
  ("On which day was the Prophet ﷺ born?", "Monday", ["Friday", "Thursday", "Sunday"], "Ibn Kathir: he was born on a Monday in Rabi' al-Awwal.", "al-Fusul"),
  ("In which year was he born ﷺ?", "The Year of the Elephant", ["The year of the Hijrah", "The year of the Trench", "The Year of Sorrow"], "The sound view is that he was born in the Year of the Elephant.", "al-Fusul"),
  ("Who raised him after his grandfather died?", "His uncle Abu Talib", ["His uncle Abu Lahab", "Halimah", "Waraqah"], "After 'Abd al-Muttalib, Abu Talib took care of him.", "al-Fusul"),
 ]),
"sr2": L("sr2", "The first revelation", "The cave of Hira and the first words of the Qur'an.", [
  ("In Hira", "Before prophethood, he ﷺ loved seclusion and would worship in the cave of Hira for nights at a time.", "Hadith, Sahih al-Bukhari, Book of Revelation (3)"),
  ("'Read!'", "The angel came and said 'Read!' He ﷺ said, 'I am not one who reads.' Then the angel recited: 'Read in the name of your Lord who created…' (al-'Alaq 1–5)", "Hadith, Sahih al-Bukhari, Book of Revelation (3)"),
  ("Khadijah رضي الله عنها", "He returned trembling. Khadijah comforted him: 'Allah will never disgrace you. You keep ties of kinship, carry the burdens of the weak and help the needy.'", "Hadith, Sahih al-Bukhari, Book of Revelation (3)"),
 ], [
  ("Where did the first revelation come?", "The cave of Hira", ["The cave of Thawr", "The Ka'bah", "Madinah"], "He ﷺ was worshipping in the cave of Hira when the angel came.", "Sahih al-Bukhari"),
  ("What were the first words revealed?", "'Read in the name of your Lord who created'", ["Al-Fatihah", "Ayat al-Kursi", "'O you wrapped in garments'"], "The opening verses of Surah al-'Alaq were the first revealed.", "Sahih al-Bukhari"),
  ("Who comforted him ﷺ when he came home?", "Khadijah رضي الله عنها", ["Abu Bakr", "Abu Talib", "Fatimah"], "Khadijah reassured him that Allah would never disgrace him.", "Sahih al-Bukhari"),
 ]),
"sr3": L("sr3", "Hardship in Makkah", "Persecution, Abyssinia and the Year of Sorrow.", [
  ("The tortured", "Quraysh tortured the weak Muslims to make them leave Islam. They held firm.", "al-Fusul fi Sirat al-Rasul, the trial of the tortured"),
  ("Abyssinia", "The Prophet ﷺ allowed a group of Muslims to migrate to Abyssinia, to the just king al-Najashi, where they were safe.", "al-Fusul fi Sirat al-Rasul, the migration to Abyssinia"),
  ("The boycott and Ta'if", "Quraysh boycotted Banu Hashim. Later the Prophet ﷺ went to Ta'if to call its people, and they drove him out. He returned to Makkah under protection.", "al-Fusul fi Sirat al-Rasul, the boycott; going out to Ta'if"),
 ], [
  ("To which land did the first Muslims migrate?", "Abyssinia", ["Madinah", "Syria", "Yemen"], "They migrated to Abyssinia, to the just king al-Najashi.", "al-Fusul"),
  ("Who did Quraysh boycott?", "Banu Hashim", ["Banu Umayyah", "The Ansar", "The Jews of Madinah"], "Ibn Kathir has a chapter on Quraysh's boycott of Banu Hashim and Banu al-Muttalib.", "al-Fusul"),
  ("How did the people of Ta'if respond?", "They drove him out", ["They accepted Islam", "They made him king", "They gave him protection"], "The people of Ta'if rejected him and drove him out.", "al-Fusul"),
 ]),
"sr4": L("sr4", "The Night Journey and the Hijrah", "From al-Isra' to the arrival in Madinah.", [
  ("Isra' and Mi'raj", "Allah took His Messenger ﷺ by night from al-Masjid al-Haram to al-Masjid al-Aqsa, and up through the heavens. The five daily prayers were made fard on that night.", "al-Fusul fi Sirat al-Rasul, the Isra' and Mi'raj"),
  ("The pledges of 'Aqabah", "Believers from Madinah met him ﷺ at 'Aqabah and pledged to follow and protect him. Islam spread in Madinah.", "al-Fusul fi Sirat al-Rasul, the first and second pledges of 'Aqabah"),
  ("The Hijrah", "He ﷺ migrated with Abu Bakr رضي الله عنه, hiding in the cave of Thawr, then reached Quba' and Madinah, built the masjid and joined the Muhajirun and Ansar in brotherhood.", "al-Fusul fi Sirat al-Rasul, the Hijrah; brotherhood"),
 ], [
  ("What was made fard on the night of the Mi'raj?", "The five daily prayers", ["Fasting Ramadan", "Zakat", "Hajj"], "The five prayers were made obligatory on that night.", "al-Fusul"),
  ("Who migrated with the Prophet ﷺ?", "Abu Bakr رضي الله عنه", ["'Umar رضي الله عنه", "'Ali رضي الله عنه", "Bilal رضي الله عنه"], "Abu Bakr was his companion in the Hijrah and the cave.", "al-Fusul"),
  ("In which cave did they hide?", "Thawr", ["Hira", "Uhud", "Badr"], "They hid in the cave of Thawr.", "al-Fusul"),
 ]),
"sr5": L("sr5", "Badr, Uhud and the Trench", "The great battles of the Madinan years.", [
  ("Badr", "At Badr, in Ramadan of the second year, Allah gave victory to a small number of believers over a much larger army of Quraysh.", "al-Fusul fi Sirat al-Rasul, the great Battle of Badr"),
  ("Uhud", "At Uhud the archers left their post against the Prophet's ﷺ order, and the Muslims suffered. Hamzah رضي الله عنه was martyred.", "al-Fusul fi Sirat al-Rasul, the Battle of Uhud"),
  ("The Trench", "When the confederate tribes came to Madinah, the Muslims dug a trench. After a long siege, Allah sent a wind and the confederates left.", "al-Fusul fi Sirat al-Rasul, the Battle of the Trench"),
 ], [
  ("In which month was Badr?", "Ramadan", ["Muharram", "Shawwal", "Dhu al-Hijjah"], "Badr took place in Ramadan of the second year after the Hijrah.", "al-Fusul"),
  ("What went wrong at Uhud?", "The archers left their post", ["The Muslims ran out of water", "They lost their way", "Rain stopped the battle"], "The archers left their position against his ﷺ order.", "al-Fusul"),
  ("How did the Muslims defend Madinah from the confederates?", "They dug a trench", ["They built a wall", "They left the city", "They paid the tribes"], "Hence its name: the Battle of the Trench (al-Khandaq).", "al-Fusul"),
 ]),
"sr6": L("sr6", "Victory and farewell", "Hudaybiyah, the opening of Makkah, and his passing ﷺ.", [
  ("Hudaybiyah", "In the sixth year he ﷺ set out for 'umrah and made a treaty with Quraysh at al-Hudaybiyah. Allah called it a clear victory.", "al-Fusul fi Sirat al-Rasul, al-Hudaybiyah"),
  ("The opening of Makkah", "In Ramadan of the eighth year he ﷺ entered Makkah with humility, cleared the Ka'bah of idols and forgave the people who had fought him.", "al-Fusul fi Sirat al-Rasul, the opening of Makkah"),
  ("The farewell", "He ﷺ performed the Farewell Hajj in the tenth year, and passed away in Madinah in Rabi' al-Awwal of the eleventh year.", "al-Fusul fi Sirat al-Rasul, the Farewell Hajj; his passing"),
 ], [
  ("When was Makkah opened?", "Ramadan, in the 8th year after the Hijrah", ["The 2nd year", "The 10th year", "Muharram of the 5th year"], "The opening of Makkah was in Ramadan of the eighth year.", "al-Fusul"),
  ("What did he ﷺ do with the people of Makkah?", "Forgave them", ["Expelled them", "Took their wealth", "Punished all of them"], "He forgave those who had fought him.", "al-Fusul"),
  ("In which year was the Farewell Hajj?", "The 10th year after the Hijrah", ["The 6th", "The 8th", "The 11th"], "The Farewell Hajj was in the tenth year; he passed away in the eleventh.", "al-Fusul"),
 ]),
"sr7": L("sr7", "His character ﷺ", "How he looked and how he treated people.", [
  ("His appearance", "Anas رضي الله عنه described him ﷺ: neither very tall nor short, neither very white nor dark, his hair neither tightly curled nor straight.", "al-Shama'il al-Muhammadiyyah, his appearance"),
  ("His gentleness", "Anas رضي الله عنه served him for ten years, and he ﷺ never once said 'uff' to him, nor asked 'why did you do that?'", "al-Shama'il al-Muhammadiyyah, his character"),
  ("The Qur'an walking", "'A'ishah رضي الله عنها was asked about his character. She said: 'His character was the Qur'an.'", "Hadith, Sahih Muslim"),
 ], [
  ("How long did Anas serve the Prophet ﷺ?", "Ten years", ["Two years", "Twenty years", "One year"], "Anas served him for ten years and never heard 'uff' from him.", "al-Shama'il"),
  ("How did 'A'ishah describe his character?", "'His character was the Qur'an'", ["'He was very strict'", "'He spoke very little'", "'He was like a king'"], "Her answer: his character was the Qur'an.", "Sahih Muslim"),
  ("Which describes his height ﷺ?", "Neither very tall nor short", ["Very tall", "Short", "Unknown"], "Anas described him as neither very tall nor short.", "al-Shama'il"),
 ]),

# ---------------- QUR'AN: REVELATION AND PRESERVATION (Sahih al-Bukhari; al-Tibyan) ----------------
"qr1": L("qr1", "How revelation came", "What the Prophet ﷺ said about receiving the wahy.", [
  ("Like a bell", "Asked how revelation came, he ﷺ said: sometimes it comes like the ringing of a bell, and that is the hardest on me; then it leaves me and I have taken in what was said.", "Hadith, Sahih al-Bukhari, Book of Revelation (2)"),
  ("As a man", "'And sometimes the angel comes to me in the form of a man, speaks to me, and I take in what he says.'", "Hadith, Sahih al-Bukhari, Book of Revelation (2)"),
  ("The weight of it", "'A'ishah رضي الله عنها said she saw revelation come to him on a very cold day, and when it left him his forehead was dripping with sweat.", "Hadith, Sahih al-Bukhari, Book of Revelation (2)"),
 ], [
  ("Which way of revelation did he ﷺ say was hardest?", "Like the ringing of a bell", ["The angel as a man", "In a dream", "Through a book"], "He said the bell-like way was the hardest on him.", "Sahih al-Bukhari"),
  ("In what form did the angel sometimes come?", "In the form of a man", ["As a bird", "As light only", "As a voice from a tree"], "'Sometimes the angel comes to me in the form of a man.'", "Sahih al-Bukhari"),
  ("What did 'A'ishah notice on a very cold day?", "His forehead dripping with sweat", ["He fell asleep", "He laughed", "He was silent all day"], "Even on a cold day his forehead dripped with sweat from the weight of revelation.", "Sahih al-Bukhari"),
 ]),
"qr2": L("qr2", "Revealed bit by bit", "Twenty-three years, and Jibril's yearly review.", [
  ("In stages", "Allah sent the Qur'an down in parts over the years of prophethood: 'A Qur'an We have divided, so that you may recite it to people slowly.' (al-Isra' 106)", "Qur'an, al-Isra' 106"),
  ("Every Ramadan", "Jibril عليه السلام met the Prophet ﷺ every night of Ramadan and studied the Qur'an with him.", "Hadith, Sahih al-Bukhari, Book of Revelation (6)"),
  ("Twice in the last year", "Jibril reviewed the Qur'an with him ﷺ once every year, and twice in the year he passed away.", "Hadith, Sahih al-Bukhari, Book of the Virtues of the Qur'an"),
 ], [
  ("How was the Qur'an sent down?", "In parts over the years", ["All at once in one night only", "In one year", "After his passing"], "'A Qur'an We have divided, so that you may recite it slowly.' (al-Isra' 106)", "Qur'an"),
  ("When did Jibril study the Qur'an with him ﷺ?", "Every night of Ramadan", ["Every Friday", "Only on Laylat al-Qadr", "Every Hajj"], "Ibn 'Abbas: Jibril met him every night of Ramadan and studied the Qur'an with him.", "Sahih al-Bukhari"),
  ("How many times was it reviewed in his final year?", "Twice", ["Once", "Three times", "Not at all"], "Once every year, and twice in the year he passed away.", "Sahih al-Bukhari"),
 ]),
"qr3": L("qr3", "Gathered into one book", "Abu Bakr's collection and 'Uthman's copies.", [
  ("After Yamamah", "After many reciters were martyred at Yamamah, 'Umar رضي الله عنه urged Abu Bakr رضي الله عنه to collect the Qur'an. Abu Bakr gave the task to Zayd ibn Thabit رضي الله عنه, a scribe of revelation.", "Hadith, Sahih al-Bukhari, Book of the Virtues of the Qur'an"),
  ("Carefully", "Zayd gathered it from palm stalks, flat stones and the memories of men. The sheets stayed with Abu Bakr, then 'Umar, then Hafsah رضي الله عنهم.", "Hadith, Sahih al-Bukhari, Book of the Virtues of the Qur'an"),
  ("'Uthman's copies", "When Hudhayfah رضي الله عنه saw people differing in recitation, 'Uthman رضي الله عنه had copies made from Hafsah's sheets and sent one to each region.", "Hadith, Sahih al-Bukhari, Book of the Virtues of the Qur'an"),
 ], [
  ("Who first ordered the Qur'an to be collected into one book?", "Abu Bakr رضي الله عنه", ["'Ali رضي الله عنه", "Mu'awiyah رضي الله عنه", "The Umayyad caliphs"], "Abu Bakr ordered it, on 'Umar's advice, after Yamamah.", "Sahih al-Bukhari"),
  ("Who did the collecting?", "Zayd ibn Thabit رضي الله عنه", ["Abu Hurayrah رضي الله عنه", "Ibn 'Abbas رضي الله عنهما", "Bilal رضي الله عنه"], "Zayd ibn Thabit, a scribe of revelation, was given the task.", "Sahih al-Bukhari"),
  ("Why did 'Uthman send copies to the regions?", "People were differing in recitation", ["The sheets were lost", "Abu Bakr's sheets were wrong", "To add new chapters"], "Hudhayfah warned him of differences, so he sent unified copies from Hafsah's sheets.", "Sahih al-Bukhari"),
 ]),
"qr4": L("qr4", "Preserved by Allah", "Seven modes, memorisers, and Allah's promise.", [
  ("His promise", "'Indeed it is We who sent down the Reminder, and indeed We will preserve it.' (al-Hijr 9)", "Qur'an, al-Hijr 9"),
  ("Seven modes", "'Umar رضي الله عنه heard Hisham ibn Hakim رضي الله عنه recite differently and brought him to the Prophet ﷺ, who approved both and said the Qur'an was revealed in seven modes (ahruf).", "Hadith, Sahih al-Bukhari, Book of the Virtues of the Qur'an"),
  ("In hearts", "The Qur'an is preserved in hearts as well as written in copies, as Imam Abu Hanifah رحمه الله said. Every generation has had countless people who memorised it.", "al-Fiqh al-Akbar, on the Qur'an"),
 ], [
  ("Who preserves the Qur'an, according to al-Hijr 9?", "Allah", ["Only the scholars", "Only the copies", "No one"], "'It is We who sent down the Reminder, and We will preserve it.'", "Qur'an"),
  ("In how many modes (ahruf) was the Qur'an revealed?", "Seven", ["One", "Three", "Ten"], "The Prophet ﷺ said it was revealed in seven ahruf.", "Sahih al-Bukhari"),
  ("When 'Umar and Hisham recited differently, the Prophet ﷺ…", "Approved both", ["Corrected Hisham only", "Corrected 'Umar only", "Told them to stop reciting"], "He approved both and explained the seven modes.", "Sahih al-Bukhari"),
 ]),
"qr5": L("qr5", "Honouring the Qur'an", "Al-Nawawi's manners with the Book of Allah.", [
  ("Be pure", "Recite in a state of purity, with a clean mouth, using the siwak, facing the qiblah and sitting with humility.", "al-Tibyan fi Adab Hamalat al-Qur'an, manners of the Qur'an"),
  ("Recite slowly", "Recite with tartil, reflecting on the meaning. Reflection is the whole purpose of recitation.", "al-Tibyan fi Adab Hamalat al-Qur'an, manners of the Qur'an"),
  ("Touching it", "In the Hanafi school, a person without wudu may not touch the Qur'an except with a separate cover. Someone in janabah may not recite it either.", "Nur al-Idah, what is forbidden without purity"),
 ], [
  ("According to al-Nawawi, what is the purpose of recitation?", "Reflection", ["Speed", "Finishing quickly", "Showing others"], "Al-Nawawi says reflection is the point of reciting.", "al-Tibyan"),
  ("Without wudu, may you touch the Qur'an in the Hanafi school?", "No, only with a separate cover", ["Yes, freely", "Only with your left hand", "Only at home"], "Nur al-Idah lists touching the Qur'an among what is forbidden without purity.", "Nur al-Idah"),
  ("Which is a manner of recitation al-Nawawi mentions?", "Using the siwak before reciting", ["Reciting while laughing", "Reciting as fast as possible", "Reciting only in public"], "A clean mouth and siwak are among the manners he gives.", "al-Tibyan"),
 ]),
}

COURSES = [
 ("aqeedah", "Aqeedah", "العقيدة", "Learn about Allah, His Messengers ﷺ and the Last Day", "Umm al-Barahin and al-'Aqidah al-Tahawiyyah", "#0E5A43",
  ["belief1", "aq_proof", "belief2", "belief3", "belief4", "aq_speech", "aq_jaiz", "belief5", "aq_shahada", "belief6", "aq_akhira", "aq_qadr", "aq_awliya"]),
 ("fiqh", "Fiqh", "الفقه", "Purification, prayer, fasting and zakat, in the Hanafi school", "Nur al-Idah and Mukhtasar al-Quduri", "#1F5F8B",
  ["fiqh0", "purity1", "purity2", "purity3", "purity4", "purity5", "purity6", "fiqh_khuff", "fiqh_hayd",
   "prayer1", "prayer2", "prayer3", "prayer4", "prayer5", "fasting1", "fasting2", "fasting3", "zakat1", "zakat2", "zakat3"]),
 ("halal", "Halal & Haram", "الحلال والحرام", "Food, dress, the gaze and earning, and the levels of carefulness", "Ihya' 'Ulum al-Din and Mukhtasar al-Quduri", "#8A5A1F",
  ["hh1", "hh2", "hh3", "hh4", "hh5", "hh6"]),
 ("doubts", "Dealing with Doubts", "اليقين", "What to do with doubts, from the Prophet ﷺ and Imam al-Ghazali", "al-Munqidh min al-Dalal", "#5B4B8A",
  ["dd1", "dd2", "dd3", "dd4", "dd5"]),
 ("seerah", "Seerah of the Prophet ﷺ", "السيرة النبوية", "His life ﷺ from birth to his passing", "al-Fusul fi Sirat al-Rasul by Ibn Kathir", "#2E6B4F",
  ["sr1", "sr2", "sr3", "sr4", "sr5", "sr6", "sr7"]),
 ("quran", "Qur'an: Revelation and Preservation", "علوم القرآن", "How the Qur'an came down, was gathered and is preserved", "Sahih al-Bukhari and al-Tibyan", "#7A3B3B",
  ["qr1", "qr2", "qr3", "qr4", "qr5"]),
 ("tazkiyah", "Tazkiyah", "التزكية", "Sincerity, repentance and the illnesses of the heart", "Bidayat al-Hidayah and al-Risalah al-Qushayriyyah", "#4E6B2E",
  ["heart1", "heart2", "heart3", "heart4", "heart5"]),
]

def old_lessons():
    out = {}
    for uid, _t, _s, _c, lessons in UNITS:
        for k, (lt, cards, checks) in enumerate(lessons):
            lid = f"{uid}{k+1}"; ch = CHAPTER.get(lid, {})
            cs = [{"t": t, "x": x, "src": f"{s}, {ch[s]}" if s in ch else s} for t, x, s in cards]
            srcs = list(dict.fromkeys(c["src"] for c in cs))
            out[lid] = {"id": lid, "title": lt, "about": ABOUT[lid], "cards": cs,
                        "checks": [{"q": q, "a": a, "w": w, "why": y, "src": " · ".join(srcs)} for (q, a, w), y in zip(checks, WHY[lid])]}
    return out

if __name__ == "__main__":
    OLD = old_lessons(); used = set(); out = []
    for cid, title, ar, sub, book, color, ids in COURSES:
        ls = []
        for lid in ids:
            assert lid not in used, lid; used.add(lid)
            if lid in OLD: ls.append(OLD[lid]); continue
            _id, lt, about, cards, checks = NEW[lid]
            for c in checks: assert len(c[2]) == 3 and c[1] not in c[2], (lid, c[0])
            ls.append({"id": lid, "title": lt, "about": about, "cards": [{"t": t, "x": x, "src": s} for t, x, s in cards],
                       "checks": [{"q": q, "a": a, "w": w, "why": y, "src": s} for q, a, w, y, s in checks]})
        out.append({"id": cid, "title": title, "ar": ar, "sub": sub, "book": book, "color": color, "lessons": ls})
    missing = set(OLD) - used; assert not missing, missing
    assert set(NEW) <= used, set(NEW) - used
    for c in out:
        for l in c["lessons"]:
            for x in l["cards"]: assert "," in x["src"] or x["src"].startswith(("Hadith", "Qur'an")) or ";" in x["src"], (l["id"], x["src"])
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(out, open(os.path.join(here, "..", "app", "data", "learn.json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print("courses", len(out), "lessons", sum(len(c["lessons"]) for c in out), "checks", sum(len(l["checks"]) for c in out for l in c["lessons"]))
