"""Lessons added on 27 Nov 2026 to complete the basics (Fard al-'Ayn)."""
import json, os
NUR, QD = "Nur al-Idah", "Mukhtasar al-Quduri"
G = json.load(open(os.path.join(os.path.dirname(__file__), "..", "app", "data", "guides.json")))

def guide_items():
    out = {}
    def walk(x):
        if isinstance(x, dict):
            if "ar" in x and x.get("label"): out.setdefault(x["label"], x)
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
    walk(G)
    return out

def texts_lesson():
    it = guide_items()
    order = [("Thana'", "The opening praise (thana')"), ("Ta'awwudh and basmalah", "Seeking refuge and bismillah"), ("Al-Fatihah", "Al-Fatihah"),
             ("For example, al-Ikhlas", "A short surah: al-Ikhlas"), ("In ruku' (3 times)", "In ruku' (three times)"), ("Rising and standing", "Rising from ruku'"),
             ("In sujud (3 times)", "In sujud (three times)"), ("Tashahhud", "The tashahhud"), ("Salawat Ibrahimiyyah", "The salawat (al-Salat al-Ibrahimiyyah)"),
             ("The du'a taught to Abu Bakr al-Siddiq رَضِيَ اللَّهُ عَنْهُ", "A du'a before the salam"), ("Right, then left", "The salam"), ("Du'a al-qunut", "The qunut in witr")]
    cards = []
    for k, t in order:
        x = it.get(k)
        if not x: continue
        src = x.get("src") or "Mukhtasar al-Quduri, how to pray"
        if "," not in src and not src.startswith("Qur'an"): src += ", how to pray"
        cards.append({"t": t, "ar": x["ar"], "x": x.get("en", ""), "src": src})
    return {"id": "f_texts", "title": "What you recite in prayer", "about": "Every word a beginner must know by heart to pray, with its meaning.",
      "cards": [{"t": "Learn them by heart", "x": "These are the words of the prayer, in order. Al-Fatihah and a short surah are wajib; the rest are sunnah or wajib as the earlier lessons explain. Turn on Transliteration (Aa) if you cannot yet read Arabic, and learn one a day. The How to pray guide in Tools has the same words with audio.", "src": "Nur al-Idah, how the prayer is put together"}] + cards,
      "checks": [
        {"q": "What is said in ruku'?", "a": "Subhana rabbiya al-'azim", "w": ["Subhana rabbiya al-a'la", "Sami' Allahu li-man hamidah", "Al-tahiyyatu lillah"], "why": "'Al-'azim' (the Magnificent) in ruku', 'al-a'la' (the Most High) in sujud.", "src": "Mukhtasar al-Quduri, how to pray"},
        {"q": "Which words begin the tashahhud?", "a": "Al-tahiyyatu lillahi wa al-salawatu wa al-tayyibat", "w": ["Subhanaka Allahumma wa bi-hamdik", "Allahumma salli 'ala Muhammad", "Allahumma inna nasta'inuk"], "why": "The tashahhud of Ibn Mas'ud رَضِيَ اللَّهُ عَنْهُ, which the Hanafis follow.", "src": "Mukhtasar al-Quduri, how to pray"},
        {"q": "Which is recited in the third rak'ah of witr before ruku'?", "a": "The qunut: 'Allahumma inna nasta'inuk…'", "w": ["The tashahhud", "Al-Salat al-Ibrahimiyyah", "The opening praise"], "why": "The qunut is wajib in witr, said after raising the hands with takbir.", "src": "Nur al-Idah, the wording of the qunut"},
        {"q": "What is said straight after the opening takbir?", "a": "Subhanaka Allahumma wa bi-hamdik…", "w": ["Al-Fatihah", "Subhana rabbiya al-'azim", "Al-salamu 'alaykum"], "why": "The opening praise comes first, then seeking refuge and bismillah, then al-Fatihah.", "src": "Mukhtasar al-Quduri, how to pray"},
      ]}

# (id, title, about, cards, checks) for learn_polish._lesson
MADHUR = ("f_madhur", "Constant bleeding, wounds and casts", "For anyone with a flow they cannot stop, or a dressing they cannot remove.", [
  ("Who is excused (ma'dhur)", "Someone with a constant flow that breaks wudu, such as drops of urine, wind, a bleeding wound or irregular bleeding (istihadah), is excused (ma'dhur) once it continues through a whole prayer time without a break long enough to make wudu and pray the fard.", f"{NUR}, when an excuse is established"),
  ("Their wudu", "They make wudu once the prayer time has begun, and pray with it every fard and voluntary prayer they wish in that time. That flow does not break it, though anything else does. When the time ends, the wudu ends.", f"{NUR}, the ruling of istihadah and similar cases"),
  ("Staying excused", "Once established, the excuse continues as long as the flow appears at least once in each later prayer time. If a whole prayer time passes without it, the person is no longer excused.", f"{NUR}, when an excuse is established"),
  ("Casts and dressings", "If a limb has a cast, splint or dressing and washing it or taking it off would cause harm, wipe once over most of it with a wet hand in wudu or ghusl, and wash the rest. It has no time limit and need not be put on in wudu.", f"{NUR}, splints and the like"),
  ("Keep a record", "Women's bleeding has detailed rulings built on each woman's habit. Note the start and end of every period and every bleeding, and ask a qualified teacher when it is irregular.", f"{NUR}, menstruation"),
 ], [
  ("Drops of urine come throughout every prayer time. With one wudu, the person may pray…", "Every prayer they wish until that time ends", ["Only one fard prayer", "Nothing; each drop breaks it", "Until the next day"], "The flow they are excused for does not break their wudu until the time ends.", f"{NUR}, the ruling of istihadah and similar cases"),
  ("Your arm is in a cast and washing it would harm you. In wudu you…", "Wipe over most of the cast and wash the rest", ["Do tayammum for the whole wudu", "Leave the arm and pray anyway", "Remove the cast regardless"], "Wiping over a splint or dressing stands in place of washing beneath it.", f"{NUR}, splints and the like"),
  ("When does an excused person's wudu end?", "When the prayer time ends, or something else breaks it", ["After one prayer", "At sunrise only", "It never ends"], "A new time needs a new wudu.", f"{NUR}, the ruling of istihadah and similar cases"),
 ])

DEATH = ("f_death", "When someone dies", "What to do from the last moments to the burial, and what follows.", [
  ("The last moments", "Turn the dying person towards the qiblah on the right side, and say the Shahadah gently near them so they may remember it, without pressing them to repeat it.", f"{NUR}, what is done for one who is dying"),
  ("Straight after death", "Close the eyes, tie the jaw, straighten the limbs and cover the body. Say: 'Inna lillahi wa inna ilayhi raji'un.' Hurry to wash, pray over and bury him, and settle his debts quickly.", f"{NUR}, what is done when he dies"),
  ("Washing", "Washing the deceased is fard kifayah. Men wash men and women wash women. A wife may wash her husband, but in the Hanafi school a husband does not wash his wife. Give him wudu first without rinsing the mouth and nose, then wash an odd number of times.", f"{NUR}, preparing and washing him"),
  ("The shroud", "The sunnah shroud is white: three cloths for a man (a wrap, a long shirt and an outer sheet) and five for a woman (those three, a headscarf and a chest cloth).", f"{NUR}, the shroud according to the Shari'ah"),
  ("Burial", "After the funeral prayer, carry the bier quickly. Lay him in the grave on his right side facing the qiblah, saying 'Bismillahi wa 'ala millati Rasulillah.' Building over graves for show is disliked.", f"{NUR}, burying it"),
  ("Grief, debts and inheritance", "Weeping is allowed; wailing, tearing clothes and striking oneself are forbidden. Condolence is sunnah for three days. From his wealth come first the funeral costs, then his debts, then any bequest up to a third, then the shares of inheritance. A widow keeps an 'iddah of four months and ten days.", f"{QD}, Book of Inheritance"),
 ], [
  ("How is the deceased laid in the grave?", "On the right side, facing the qiblah", ["On the back, feet to the qiblah", "On the left side", "Sitting upright"], "Facing the qiblah on the right side, saying 'Bismillahi wa 'ala millati Rasulillah'.", f"{NUR}, burying it"),
  ("How many cloths make the sunnah shroud for a man?", "Three", ["One", "Five", "Seven"], "Three for a man, five for a woman.", f"{NUR}, the shroud according to the Shari'ah"),
  ("From a deceased's wealth, what is paid after the funeral costs?", "His debts", ["The heirs' shares", "A bequest of half", "Charity for his soul"], "Funeral costs, then debts, then a bequest up to a third, then inheritance.", f"{QD}, Book of Inheritance"),
  ("Crying at a death is…", "Allowed, but wailing and tearing clothes are forbidden", ["Forbidden", "Required", "Disliked in every case"], "The Prophet ﷺ wept at the death of his son Ibrahim.", "Sahih al-Bukhari, Book of Funerals"),
  ("What is the 'iddah of a widow who is not pregnant?", "Four months and ten days", ["Three months", "Forty days", "One year"], "Al-Baqarah 234 sets four months and ten days.", "Qur'an, al-Baqarah 2:234"),
 ])

MONEY = ("f_money", "Money: riba, loans and earning", "How to keep your income and spending halal in a world built on interest.", [
  ("War from Allah", "Riba (interest) is among the major sins. Allah made trade lawful and riba unlawful, and told those who will not give it up to expect war from Allah and His Messenger.", "Qur'an, al-Baqarah 2:275"),
  ("Every loan with interest", "Any loan where you must pay back more than you borrowed is riba: a mortgage with interest, a personal loan, car finance with interest, an overdraft or a credit card that charges interest. There is no exception for buying a home, however normal it has become.", f"{QD}, chapter on riba"),
  ("Everyone in it is sinful", "The Prophet ﷺ cursed the one who takes riba, the one who pays it, the one who writes it and its two witnesses, and said they are all the same. So a job that arranges or writes interest contracts is not halal income.", "Sahih Muslim, Book of Musaqah"),
  ("Interest paid to you", "Do not take interest on savings. If a bank has paid interest into your account, do not use it for yourself: give it away to the poor without intending reward, to rid yourself of it.", "Radd al-Muhtar, on unlawful wealth"),
  ("Gambling", "Gambling is haram in every form: betting, lottery tickets, scratchcards, and paid entries where you may win more than you paid or lose it.", "Qur'an, al-Ma'idah 5:90"),
  ("Before you sign", "Earning a halal living is an obligation. Before taking out insurance, a pension, investments or any finance product, ask a qualified scholar: many contain riba or gambling hidden in the terms.", "Ihya' 'Ulum al-Din, Book of Earning and Livelihood"),
 ], [
  ("Is a mortgage with interest allowed to buy a family home?", "No; any loan with interest is riba", ["Yes, a home is a necessity", "Yes, if the rate is low", "Yes, for a first home only"], "Riba is haram whatever it is used for.", "Qur'an, al-Baqarah 2:275"),
  ("A bank has paid interest into your savings. What do you do?", "Give it to the poor without intending reward", ["Spend it on yourself", "Count it as your zakat", "Leave it to grow"], "It is not yours to use; you rid yourself of it.", "Radd al-Muhtar, on unlawful wealth"),
  ("Buying a lottery ticket is…", "Haram, because it is gambling", ["Allowed if it is for charity", "Disliked only", "Allowed if you rarely win"], "Gambling is filth from the work of Shaytan (al-Ma'idah 90).", "Qur'an, al-Ma'idah 5:90"),
  ("Whom did the Prophet ﷺ curse in the hadith of riba?", "The taker, the payer, the writer and the witnesses", ["Only the taker", "Only the bank", "Only the payer"], "He said they are all the same.", "Sahih Muslim, Book of Musaqah"),
 ])

NIKAH = ("f_nikah", "Marriage and the family", "What every Muslim must know before marrying and while raising a family.", [
  ("The contract", "Marriage (nikah) is made by an offer and an acceptance spoken in the presence of two Muslim witnesses: two men, or one man and two women.", f"{QD}, Book of Marriage"),
  ("The mahr", "The mahr is the wife's right, owed by the husband, whether or not it was named. In the Hanafi school it is at least ten dirhams of silver.", f"{QD}, Book of Marriage"),
  ("Consent and guardian", "No one may marry a woman without her consent. In the Hanafi school an adult woman's marriage is valid without her guardian, but it is sunnah for him to arrange it, and he may object if the husband is not a suitable match.", f"{QD}, Book of Marriage"),
  ("Rights", "The husband must provide his wife's food, clothing and housing, and live with her in kindness. The wife obeys him in what is right and guards his home and honour. The Prophet ﷺ said: the best of you are the best to their wives.", f"{QD}, Book of Maintenance"),
  ("Divorce", "Divorce (talaq) is the most disliked of lawful things to Allah. The sunnah way is one talaq in a time of purity without intimacy. Three talaqs said at once count as three in the Hanafi school, and saying them is sinful. A divorced woman who menstruates keeps an 'iddah of three periods.", f"{QD}, Book of Divorce"),
  ("Children and neighbours", "Give children good names, teach them the prayer at seven, and be fair between them. The Prophet ﷺ said Jibril kept advising him about the neighbour until he thought he would make him an heir.", "Sahih al-Bukhari, Book of Good Manners"),
 ], [
  ("What makes a nikah valid?", "Offer and acceptance before two witnesses", ["A celebration with guests", "A signature at the registry only", "The bride's family agreeing alone"], "Al-Quduri: offer and acceptance, with two witnesses.", f"{QD}, Book of Marriage"),
  ("Whose right is the mahr?", "The wife's", ["Her father's", "The husband's", "The imam's"], "It is owed to her by her husband.", f"{QD}, Book of Marriage"),
  ("In the Hanafi school, three talaqs said at once count as…", "Three, and saying them that way is sinful", ["One", "None", "Two"], "They take effect as three, so the marriage cannot be resumed without the conditions the Qur'an sets.", f"{QD}, Book of Divorce"),
  ("May a woman be married without her consent?", "No", ["Yes, by her father", "Yes, if she is young", "Yes, by her brother"], "Her consent is required.", f"{QD}, Book of Marriage"),
  ("At what age are children taught to pray?", "Seven", ["Three", "Ten", "Fifteen"], "Teach them at seven; be firmer at ten (Abu Dawud).", "Sunan Abi Dawud, Book of Prayer"),
 ])

MODERN = ("dd6", "Questions people ask today", "Short, sound answers to the doubts you are most likely to meet.", [
  ("Why is there suffering?", "This world is a test, not the final home. Allah created death and life to test which of you is best in deeds. Every wrong will be settled on the Day of Judgement, and the patient will be given their reward without measure.", "Qur'an, al-Mulk 67:2"),
  ("Science and revelation", "The Qur'an calls us again and again to study creation, and true knowledge never contradicts revelation. Where a theory clashes with what the Qur'an states clearly, such as Adam عَلَيْهِ السَّلَامُ being created directly by Allah as the first human, the believer holds to revelation, because theories change and revelation does not.", "al-Munqidh min al-Dalal, on the sciences of the philosophers"),
  ("Can we trust the hadith?", "The hadith reached us through chains of named narrators, each one examined for honesty and precision. Scholars built a whole science to sort the sound from the weak, and no other record of history has been checked like it.", "Nuzhat al-Nazar, the kinds of hadith"),
  ("Women in Islam", "Islam gave women the right to own and earn, to inherit, and to consent to marriage. Paradise is at the feet of mothers, and Allah says: 'I will not let the deed of any of you be lost, male or female.'", "Qur'an, Al 'Imran 3:195"),
  ("When you meet a doubt", "Do not hide it and do not panic. Write it down, ask a qualified teacher, keep praying and making du'a. Al-Ghazali was cured not by arguing alone but by a light Allah placed in his heart.", "al-Munqidh min al-Dalal, the cure"),
 ], [
  ("Why does Allah allow hardship in this world?", "It is a test, and every wrong is settled on the Day of Judgement", ["Allah does not know about it", "It happens by chance", "Allah cannot stop it"], "'He created death and life to test which of you is best in deeds.'", "Qur'an, al-Mulk 67:2"),
  ("A theory contradicts something the Qur'an states clearly. The believer…", "Holds to revelation, since theories change", ["Changes the meaning of the Qur'an", "Leaves Islam", "Ignores both"], "True knowledge and revelation do not contradict.", "al-Munqidh min al-Dalal, on the sciences of the philosophers"),
  ("How were the hadith checked?", "Through chains of named narrators examined for honesty and precision", ["They were never checked", "By how popular they were", "By whether they sounded nice"], "The science of hadith sorts the sound from the weak.", "Nuzhat al-Nazar, the kinds of hadith"),
  ("You meet a doubt you cannot answer. What is best?", "Ask a qualified teacher and keep praying", ["Keep it secret", "Stop practising until it is solved", "Search random videos"], "'Ask the people of knowledge if you do not know.' (al-Nahl 43)", "Qur'an, al-Nahl 16:43"),
 ])

PATH = ("tz_path", "Walking the path", "Turning what you have learnt into a daily practice, with a guide.", [
  ("A daily wird", "Keep a small daily practice (wird) you can hold to: the morning and evening adhkar, a portion of Qur'an, salawat on the Prophet ﷺ and seeking forgiveness. The deeds most loved by Allah are the most constant, even if small.", "Sahih al-Bukhari, Book of Softening the Heart"),
  ("A guide", "The masters of tazkiyah advise travelling the path with a guide (shaykh) who is firm on the Shari'ah, has a connected chain to the Prophet ﷺ, and is known for knowledge and godliness.", "al-Risalah al-Qushayriyyah, chapter on adab"),
  ("Adab with the guide", "Come with sincerity and respect, be honest about your state, act on the advice given, and do not jump from guide to guide. The Shari'ah stays above everything.", "al-Risalah al-Qushayriyyah, chapter on adab"),
  ("A false guide", "Whoever neglects the prayer, permits what is haram, or says the Shari'ah is not for him is no guide, whatever wonders are claimed. Al-Qushayri teaches that this path is built on the Book and the Sunnah.", "al-Risalah al-Qushayriyyah, introduction"),
  ("Good company", "The Prophet ﷺ said: a person follows the religion of his close friend, so let each of you look at whom he befriends.", "Sunan Abi Dawud, Book of Good Manners"),
 ], [
  ("Which deeds are most loved by Allah?", "The most constant, even if small", ["The longest", "The most public", "Those done once a year"], "A small wird kept every day beats a large one dropped.", "Sahih al-Bukhari, Book of Softening the Heart"),
  ("A man says he is a shaykh but does not pray and says the Shari'ah is not for him. He is…", "Not a guide, whatever wonders are claimed", ["A great wali", "Above the Shari'ah", "Excused because of his rank"], "The path is built on the Book and the Sunnah.", "al-Risalah al-Qushayriyyah, introduction"),
  ("What should a sound guide have?", "Firmness on the Shari'ah, a connected chain, knowledge and godliness", ["Many followers on social media", "Wealth and fame", "Only a good voice"], "This is how the masters describe the guide.", "al-Risalah al-Qushayriyyah, chapter on adab"),
 ])

PLACE = [("fiqh", "f_rakahs", "TEXTS"), ("fiqh", "fiqh_hayd", MADHUR), ("fiqh", "f_janazah", DEATH),
         ("halal", "hh6", MONEY), ("halal", "hh_parents", NIKAH), ("doubts", None, MODERN), ("tazkiyah", None, PATH)]
