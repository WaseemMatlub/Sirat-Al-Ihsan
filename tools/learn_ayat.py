"""Qur'an verses for each lesson: the Arabic is the Uthmani text (tools/data/quran_uthmani.json, from quran-json,
CC-BY-SA, text from the Noble Qur'an Encyclopedia). The English is our own rendering of the meaning."""
import json, os
Q = json.load(open(os.path.join(os.path.dirname(__file__), "data", "quran_uthmani.json")))
NAME = {1: "al-Fatihah", 2: "al-Baqarah", 3: "Al 'Imran", 4: "al-Nisa'", 5: "al-Ma'idah", 6: "al-An'am", 7: "al-A'raf", 8: "al-Anfal", 9: "al-Tawbah",
  13: "al-Ra'd", 15: "al-Hijr", 16: "al-Nahl", 17: "al-Isra'", 21: "al-Anbiya'", 23: "al-Mu'minun", 24: "al-Nur", 31: "Luqman", 33: "al-Ahzab",
  37: "al-Saffat", 39: "al-Zumar", 42: "al-Shura", 48: "al-Fath", 49: "al-Hujurat", 51: "al-Dhariyat", 52: "al-Tur", 54: "al-Qamar", 56: "al-Waqi'ah",
  57: "al-Hadid", 62: "al-Jumu'ah", 65: "al-Talaq", 67: "al-Mulk", 66: "al-Tahrim", 68: "al-Qalam", 73: "al-Muzzammil", 75: "al-Qiyamah", 83: "al-Mutaffifin",
  96: "al-'Alaq", 10: "Yunus", 47: "Muhammad", 98: "al-Bayyinah", 99: "al-Zalzalah", 112: "al-Ikhlas", 14: "Ibrahim", 20: "Ta Ha", 25: "al-Furqan", 30: "al-Rum", 64: "al-Taghabun"}

# lesson -> [(surah, from, to, meaning)]
AYAT = {
 "aq_islam": [(3, 19, 19, "Truly, the religion with Allah is Islam.")],
 "aq_proof": [(52, 35, 35, "Or were they created by nothing, or are they themselves the creators?")],
 "belief2": [(57, 3, 3, "He is the First and the Last, the Manifest and the Hidden, and He has knowledge of all things.")],
 "belief3": [(112, 1, 4, "Say: He is Allah, One. Allah, the Self-Sufficient on whom all depend. He does not beget, nor was He begotten. And there is none equal to Him."),
             (42, 11, 11, "There is nothing like Him, and He is the All-Hearing, the All-Seeing.")],
 "belief4": [(65, 12, 12, "…so that you may know that Allah has power over all things, and that Allah encompasses all things in knowledge.")],
 "aq_speech": [(4, 164, 164, "And Allah spoke to Musa directly."), (9, 6, 6, "If one of the idolaters seeks your protection, grant it to him so that he may hear the speech of Allah.")],
 "belief5": [(33, 40, 40, "Muhammad is not the father of any of your men, but he is the Messenger of Allah and the Seal of the Prophets. And Allah has knowledge of all things.")],
 "aq_nabi": [(33, 56, 56, "Truly Allah and His angels send blessings upon the Prophet. O you who believe, send blessings upon him and greet him with abundant peace."),
             (21, 107, 107, "We did not send you except as a mercy to all the worlds."), (68, 4, 4, "And truly you are of a tremendous character."),
             (3, 31, 31, "Say: If you love Allah, follow me, and Allah will love you and forgive you your sins. Allah is Forgiving, Merciful.")],
 "aq_kutub": [(2, 285, 285, "The Messenger believes in what was sent down to him from his Lord, and so do the believers. Each believes in Allah, His angels, His books and His messengers: 'We make no distinction between any of His messengers.'"),
              (66, 6, 6, "…angels stern and severe, who do not disobey Allah in what He commands them, and do what they are commanded.")],
 "aq_shahada": [(47, 19, 19, "So know that there is no god but Allah, and ask forgiveness for your sin.")],
 "aq_sins": [(39, 53, 53, "Say: O My servants who have wronged themselves, do not despair of Allah's mercy. Truly Allah forgives all sins. He is the Forgiving, the Merciful.")],
 "aq_riddah": [(9, 65, 66, "If you ask them, they will say: 'We were only chatting and joking.' Say: 'Was it Allah, His signs and His Messenger that you were mocking? Make no excuses: you have disbelieved after your belief.'")],
 "aq_shirk": [(4, 48, 48, "Truly Allah does not forgive that partners be associated with Him, but He forgives anything less than that to whom He wills."),
              (31, 13, 13, "Luqman said to his son, advising him: 'My son, do not associate partners with Allah. Truly, associating partners is a tremendous wrong.'")],
 "aq_akhira": [(99, 7, 8, "Whoever does an atom's weight of good will see it, and whoever does an atom's weight of evil will see it."),
               (21, 47, 47, "We will set up the just scales for the Day of Resurrection, so no soul will be wronged in the least.")],
 "aq_ruya": [(75, 22, 23, "Faces that Day will be radiant, looking at their Lord.")],
 "aq_qadr": [(54, 49, 49, "Truly, We have created everything according to a measure."), (37, 96, 96, "When Allah has created you and what you do.")],
 "aq_awliya": [(10, 62, 63, "Truly the friends of Allah: no fear shall be upon them, nor shall they grieve. Those who believe and are mindful of Allah.")],
 "purity2": [(5, 6, 6, "O you who believe, when you rise for the prayer, wash your faces and your arms up to the elbows, wipe your heads, and wash your feet up to the ankles. If you are in janabah, purify yourselves…")],
 "purity6": [(4, 43, 43, "…and you find no water, then seek clean earth and wipe your faces and your hands. Truly Allah is Pardoning, Forgiving.")],
 "f_times": [(4, 103, 103, "Truly, the prayer is prescribed for the believers at set times."), (2, 238, 238, "Guard the prayers, and the middle prayer, and stand before Allah in devotion.")],
 "f_how1": [(23, 1, 2, "Successful indeed are the believers: those who are humble in their prayer.")],
 "f_travel": [(4, 101, 101, "When you travel in the land, there is no blame on you if you shorten the prayer…")],
 "f_jumuah": [(62, 9, 9, "O you who believe, when the call is made for the prayer on Friday, hasten to the remembrance of Allah and leave off trade. That is better for you, if only you knew.")],
 "f_sawm0": [(2, 183, 183, "O you who believe, fasting is prescribed for you as it was prescribed for those before you, so that you may become mindful of Allah."),
             (2, 185, 185, "The month of Ramadan, in which the Qur'an was sent down… whoever of you witnesses the month, let him fast it.")],
 "zakat1": [(2, 43, 43, "Establish the prayer, give the zakat, and bow with those who bow."),
            (9, 34, 34, "…those who hoard gold and silver and do not spend it in the way of Allah: give them tidings of a painful punishment.")],
 "zakat3": [(9, 60, 60, "Zakat is only for the poor and the needy, those who work to collect it, those whose hearts are to be won over, freeing captives, those in debt, the cause of Allah, and the stranded traveller: an obligation from Allah. Allah is Knowing, Wise.")],
 "hj1": [(3, 97, 97, "Pilgrimage to the House is a duty owed to Allah by people who are able to find a way there.")],
 "hj3": [(2, 197, 197, "Hajj is in well-known months. Whoever sets out to do Hajj in them, let there be no intimacy, no sinning and no quarrelling in Hajj.")],
 "hj6": [(2, 198, 198, "When you pour down from 'Arafat, remember Allah at the Sacred Landmark (Muzdalifah).")],
 "hh1": [(2, 168, 168, "O people, eat of what is on the earth, lawful and good, and do not follow the footsteps of Shaytan.")],
 "hh_kabair": [(4, 31, 31, "If you avoid the major sins you are forbidden, We will remove your lesser sins and admit you through a noble entrance."),
               (49, 12, 12, "Do not spy, and do not backbite one another. Would any of you like to eat the flesh of his dead brother? You would hate it.")],
 "hh_parents": [(17, 23, 23, "Your Lord has decreed that you worship none but Him, and be good to parents. If one or both reach old age with you, do not say to them even 'uff', nor scold them, but speak to them with noble words.")],
 "hh3": [(5, 3, 3, "Forbidden to you are carrion, blood, the flesh of swine, and what was dedicated to other than Allah…"),
         (6, 121, 121, "And do not eat of that over which the name of Allah has not been mentioned.")],
 "hh5": [(24, 30, 31, "Tell the believing men to lower their gaze and guard their chastity… and tell the believing women to lower their gaze and guard their chastity.")],
 "hh6": [(2, 275, 275, "Those who consume riba will not stand except as one stands whom Shaytan has struck with madness. That is because they say trade is just like riba, but Allah has made trade lawful and riba unlawful."),
         (2, 278, 279, "O you who believe, be mindful of Allah and give up what remains of riba, if you are believers. If you do not, then be warned of war from Allah and His Messenger.")],
 "hh7": [(83, 1, 3, "Woe to those who give short measure: who, when they take from people, take in full, but when they measure or weigh for them, give them less.")],
 "f_money": [(5, 90, 90, "O you who believe, wine, gambling, idols and divining arrows are only filth from the work of Shaytan, so avoid it, that you may succeed."), (2, 275, 275, "Allah has made trade lawful and riba unlawful."), (2, 278, 279, "O you who believe, be mindful of Allah and give up what remains of riba, if you are believers. If you do not, then be warned of war from Allah and His Messenger.")],
 "heart1": [(98, 5, 5, "They were only commanded to worship Allah, making the religion sincerely His.")],
 "heart2": [(66, 8, 8, "O you who believe, turn to Allah in sincere repentance."), (24, 31, 31, "And turn to Allah all together, O believers, so that you may succeed.")],
 "tz_dhikr": [(2, 152, 152, "So remember Me; I will remember you. Be grateful to Me, and do not be ungrateful."), (13, 28, 28, "Truly, in the remembrance of Allah hearts find rest.")],
 "tz_tawakkul": [(65, 3, 3, "Whoever puts his trust in Allah, He is enough for him.")],
 "tz_sabr": [(2, 153, 153, "O you who believe, seek help through patience and prayer. Truly Allah is with the patient.")],
 "qr2": [(17, 106, 106, "A Qur'an which We have divided into parts, so that you may recite it to people slowly, and We sent it down in stages.")],
 "qr4": [(15, 9, 9, "Truly, it is We who sent down the Reminder, and truly We will preserve it.")],
 "qr5": [(73, 4, 4, "And recite the Qur'an in measured recitation (tartil)."), (56, 79, 79, "None touch it except the purified.")],
 "sr2": [(96, 1, 5, "Read in the name of your Lord who created: created man from a clinging clot. Read, and your Lord is the Most Generous, who taught by the pen, taught man what he did not know.")],
 "sr4": [(17, 1, 1, "Glory be to the One who took His servant by night from the Sacred Masjid to the Furthest Masjid, whose surroundings We have blessed.")],
 "sr5": [(3, 123, 123, "Allah had already helped you at Badr when you were weak. So be mindful of Allah, so that you may be grateful.")],
 "sr_hudaybiyah": [(48, 1, 1, "Truly, We have given you a clear victory."), (48, 18, 18, "Allah was pleased with the believers when they pledged to you under the tree.")],
 "sr_farewell": [(5, 3, 3, "Today I have perfected your religion for you, completed My favour upon you, and chosen Islam as your religion.")],
 "sr_passing": [(3, 144, 144, "Muhammad is only a messenger; messengers have passed away before him. If he dies or is killed, will you turn back on your heels?")],
 "sr7": [(68, 4, 4, "And truly you are of a tremendous character."), (33, 21, 21, "In the Messenger of Allah you have a beautiful example.")],
 "sh_who": [(9, 100, 100, "And the foremost, the first of the Muhajirun and the Ansar, and those who followed them in excellence: Allah is pleased with them and they are pleased with Him."),
            (48, 29, 29, "Muhammad is the Messenger of Allah, and those with him are firm against the disbelievers, merciful to one another.")],
 "sh_abubakr": [(9, 40, 40, "…the second of two, when they were in the cave, when he said to his companion: 'Do not grieve, Allah is with us.'")],
 "sh_mothers": [(33, 6, 6, "The Prophet is closer to the believers than their own selves, and his wives are their mothers.")],
 "sh_bayt": [(33, 33, 33, "Allah only wishes to remove impurity from you, O people of the House, and to purify you completely.")],
 "ad_salam": [(4, 86, 86, "When you are greeted with a greeting, reply with a better one, or return it.")],
 "ad_eat": [(7, 31, 31, "Eat and drink, but do not waste. Truly He does not love the wasteful.")],
 "ad_teach": [(20, 114, 114, "And say: My Lord, increase me in knowledge."), (39, 9, 9, "Say: Are those who know equal to those who do not know?")],
 "ad_limbs": [(17, 36, 36, "Do not follow what you have no knowledge of. Truly the hearing, the sight and the heart: each of these will be asked about.")],
 "f_madhur": [(2, 286, 286, "Allah does not burden a soul beyond what it can bear.")],
 "dd6": [(67, 2, 2, "He who created death and life to test you, which of you is best in deeds. He is the Mighty, the Forgiving.")],
 "f_death": [(2, 156, 156, "…those who, when struck by a calamity, say: 'Truly we belong to Allah, and to Him we return.'")],
 "f_nikah": [(30, 21, 21, "Among His signs is that He created for you spouses from among yourselves so that you may find tranquillity in them, and He placed between you affection and mercy.")],
}

import re as _re
def simple(t):
    # the app's Arabic font lacks some Uthmani marks: use standard script with the same vowels
    t = t.replace("\u0671", "\u0627").replace("\u06E1", "\u0652").replace("\u06E5", "").replace("\u06E6", "")
    t = _re.sub("[\u06D6-\u06ED]", "", t)
    return _re.sub(" +", " ", t).strip()

def text(s, a, b):
    vs = {v["id"]: simple(v["text"]) for v in Q[s - 1]["verses"]}
    ind = lambda n: str(n).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
    return " ".join(f"{vs[i]} ﴿{ind(i)}﴾" for i in range(a, b + 1))

def label(s, a, b): return f"Qur'an, {NAME.get(s, Q[s-1]['transliteration'])} {s}:{a}" + (f"–{b}" if b != a else "")

def add_ayat(courses, jal_ref):
    les = {l["id"]: l for c in courses for l in c["lessons"]}
    for lid, vv in AYAT.items():
        if lid not in les: continue
        l = les[lid]; l["cards"] = [c for c in l["cards"] if not c.get("ar")]
        for k, (s, a, b, en) in enumerate(vv):
            c = {"t": "From the Qur'an", "ar": text(s, a, b), "x": en, "src": label(s, a, b), "q": [s, a]}
            r = jal_ref(s, a)
            if r: c["ref"] = r
            l["cards"].insert(min(1 + k, len(l["cards"])), c)
    return courses
