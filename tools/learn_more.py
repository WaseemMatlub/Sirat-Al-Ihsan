"""More Learn lessons, for a stronger foundation. Same format as learn_courses.NEW.
Fiqh from Nur al-Idah (al-Shurunbulali) and Mukhtasar al-Quduri; creed from al-'Aqidah al-Tahawiyyah;
Seerah from al-Fusul (Ibn Kathir); Qur'an from al-Tibyan (al-Nawawi); Tazkiyah from al-Risalah al-Qushayriyyah.
Checked against the Arabic in our library copies. To be reviewed by a teacher."""

def L(id, title, about, cards, checks): return (id, title, about, cards, checks)
NI, QD, TH = "Nur al-Idah", "Mukhtasar al-Quduri", "al-'Aqidah al-Tahawiyyah"

MORE = {
# ======================= FIQH =======================
"f_istinja": L("f_istinja", "Using the toilet and istinja'", "Cleaning yourself properly, and the manners of the toilet.", [
  ("Make sure it has stopped", "A man must make sure the last drops of urine have stopped before he starts wudu, in whatever way works for him, such as walking a little or clearing the throat.", "Nur al-Idah, chapter on istinja'"),
  ("Water or stones", "Istinja' is a sunnah. Wiping with clean stones is allowed, washing with water is better, and the best is to wipe and then wash. If impurity spreads beyond the opening more than the size of a dirham, washing it becomes fard.", "Nur al-Idah, the ruling of istinja'"),
  ("Entering and leaving", "Enter with the left foot, seeking refuge in Allah from Shaytan before going in, and leave with the right foot saying: 'Al-hamdu lillahi alladhi adhhaba 'anni al-adha wa 'afani.'", "Nur al-Idah, manners of relieving oneself"),
  ("What to avoid", "Do not face or turn your back to the qiblah, even indoors. Do not speak without need. Do not relieve yourself in water, in shade people use, on a path or under a fruit tree, and do not urinate standing without an excuse.", "Nur al-Idah, manners of relieving oneself"),
 ], [
  ("Which way of cleaning is best?", "Wiping with stones and then washing with water", ["Stones only", "Water only, always", "Tissue only"], "Nur al-Idah: water is better than stones, and joining both is best.", "Nur al-Idah, the ruling of istinja'"),
  ("With which foot do you enter the toilet?", "The left", ["The right", "Either", "Both together"], "Enter with the left foot and leave with the right.", "Nur al-Idah, manners of relieving oneself"),
  ("Facing the qiblah while relieving yourself indoors is…", "Prohibitively disliked", ["Allowed indoors", "Recommended", "Only disliked outdoors"], "Nur al-Idah says it is makruh tahrimi, even inside buildings.", "Nur al-Idah, manners of relieving oneself"),
 ]),
"f_najasa": L("f_najasa", "Impurities and what is excused", "Heavy and light impurity, and how much prevents prayer.", [
  ("Heavy impurity", "Heavy (ghalizah) impurities include wine, flowing blood, urine of animals that are not eaten, dog and predator droppings, and anything from the human body that breaks wudu when it comes out.", "Nur al-Idah, types of impurity"),
  ("Light impurity", "Light (khafifah) impurities include the urine of a horse or of animals that are eaten, and droppings of birds that are not eaten.", "Nur al-Idah, types of impurity"),
  ("What is excused", "Up to the size of a dirham of heavy impurity is excused, and less than a quarter of a garment or limb of light impurity. Tiny splashes of urine like pinheads are excused too.", "Nur al-Idah, what is excused"),
 ], [
  ("How much heavy impurity is excused in prayer?", "Up to the size of a dirham", ["None at all", "A quarter of the garment", "Any amount if dry"], "Nur al-Idah: the size of a dirham of heavy impurity is excused.", "Nur al-Idah, what is excused"),
  ("Flowing blood is…", "Heavy impurity", ["Light impurity", "Pure", "Excused in any amount"], "Flowing blood is listed among the heavy impurities.", "Nur al-Idah, types of impurity"),
  ("Light impurity is excused if it is…", "Less than a quarter of the garment or limb", ["Less than a dirham only", "Never excused", "Any amount at all"], "Less than a quarter is excused for light impurity.", "Nur al-Idah, what is excused"),
 ]),
"f_times": L("f_times", "The five prayer times", "When each prayer starts and ends, and the forbidden times.", [
  ("Fajr and Zuhr", "Fajr is from true dawn until just before sunrise. Zuhr is from when the sun passes its height until an object's shadow is twice its length (or once, in the view of the two companions), not counting its midday shadow.", "Nur al-Idah, the prayer times"),
  ("'Asr, Maghrib, 'Isha'", "'Asr is from the end of Zuhr until sunset. Maghrib is from sunset until the red twilight disappears. 'Isha' and witr are from then until dawn; witr is not prayed before 'Isha'.", "Nur al-Idah, the prayer times"),
  ("Three forbidden times", "No fard or wajib prayer owed from before is valid at sunrise until the sun rises, when it is at its height, and when it turns yellow until it sets. Voluntary prayer is prohibitively disliked then.", "Nur al-Idah, the times when prayer is not valid"),
 ], [
  ("When does the time of Fajr end?", "Just before sunrise", ["An hour after sunrise", "At Zuhr", "At the first light of dawn"], "Fajr lasts from true dawn until just before the sun rises.", "Nur al-Idah, the prayer times"),
  ("When does Maghrib end in the Hanafi fatwa?", "When the red twilight disappears", ["When the white twilight disappears", "At midnight", "Twenty minutes after sunset"], "Nur al-Idah: until the red twilight is gone, on the view the fatwa follows.", "Nur al-Idah, the prayer times"),
  ("Which is a time when prayer is not valid?", "While the sun is rising", ["In the middle of the night", "Before Zuhr", "After 'Isha'"], "Sunrise, the sun's height and its setting are the three forbidden times.", "Nur al-Idah, the times when prayer is not valid"),
 ]),
"f_adhan": L("f_adhan", "The adhan and iqamah", "Their ruling and their words.", [
  ("A stressed sunnah", "The adhan and iqamah are a stressed sunnah for every fard prayer, for men, whether praying alone or in a group, at home or travelling, on time or making up.", "Nur al-Idah, the ruling of the adhan and iqamah"),
  ("The words", "Say 'Allahu akbar' four times at the start, then each phrase twice, ending with 'Allahu akbar' twice and 'La ilaha illa Allah'. The iqamah is the same.", "Nur al-Idah, how the adhan is given"),
  ("Additions", "In the adhan of Fajr add 'al-salatu khayrun min al-nawm' twice after 'hayya 'ala al-falah'. In the iqamah add 'qad qamat al-salah' twice. Give the adhan slowly and the iqamah quickly.", "Nur al-Idah, how the adhan is given"),
 ], [
  ("What is the ruling of the adhan for a fard prayer?", "A stressed sunnah", ["Fard", "Wajib", "Only for Jumu'ah"], "Nur al-Idah: a stressed sunnah for the fard prayers.", "Nur al-Idah, the ruling of the adhan"),
  ("What is added in the adhan of Fajr?", "'Al-salatu khayrun min al-nawm'", ["'Qad qamat al-salah'", "An extra takbir", "Nothing"], "It is added twice after 'hayya 'ala al-falah' in Fajr.", "Nur al-Idah, how the adhan is given"),
  ("How is the iqamah said compared with the adhan?", "More quickly", ["More slowly", "Silently", "Only once"], "The adhan is slow and the iqamah quick.", "Nur al-Idah, how the adhan is given"),
 ]),
"f_how1": L("f_how1", "How to pray (1): from takbir to ruku'", "The prayer step by step, as Nur al-Idah describes it.", [
  ("Opening", "Raise the hands to the ears (a woman to her shoulders) and say 'Allahu akbar', intending the prayer. A man places his right hand over his left below the navel; a woman places them on her chest.", "Nur al-Idah, how the prayer is put together"),
  ("Before reciting", "Say the opening praise: 'Subhanaka Allahumma wa bi-hamdika, wa tabaraka ismuka, wa ta'ala jadduka, wa la ilaha ghayruk.' Then seek refuge (a'udhu billah) and say bismillah quietly.", "Nur al-Idah, how the prayer is put together"),
  ("Recitation", "Recite al-Fatihah, say 'amin' quietly, then a surah or three verses.", "Nur al-Idah, how the prayer is put together"),
  ("Ruku'", "Say 'Allahu akbar' and bow, back straight with the head level with it, holding the knees with fingers spread. Say 'Subhana rabbiya al-'azim' three times, the least of the sunnah.", "Nur al-Idah, how the prayer is put together"),
 ], [
  ("Where does a man place his hands after the takbir?", "Right over left, below the navel", ["On the chest", "By his sides", "Above the navel"], "Nur al-Idah: right over left below the navel for a man; a woman places them on her chest.", "Nur al-Idah"),
  ("What is said straight after the opening takbir?", "'Subhanaka Allahumma wa bi-hamdika…'", ["Al-Fatihah", "The tashahhud", "'Sami' Allahu li-man hamidah'"], "The opening praise (thana') comes first, then ta'awwudh and bismillah.", "Nur al-Idah"),
  ("How many times is the tasbih of ruku' said at least, by the sunnah?", "Three", ["Once", "Seven", "Ten"], "Three times is the least of the sunnah.", "Nur al-Idah"),
 ]),
"f_how2": L("f_how2", "How to pray (2): from rising to salam", "Prostration, sitting, tashahhud and ending the prayer.", [
  ("Rising", "Rise saying 'Sami' Allahu li-man hamidah, rabbana laka al-hamd' (a follower says only the second part), and stand still for a moment.", "Nur al-Idah, how the prayer is put together"),
  ("Sujud", "Go down with 'Allahu akbar', placing knees, then hands, then face between the hands, nose and forehead on the ground. Say 'Subhana rabbiya al-a'la' three times. Sit calmly, then make the second sujud the same way.", "Nur al-Idah, how the prayer is put together"),
  ("Sitting", "After the second rak'ah, sit on the left foot with the right foot upright, hands on the thighs, and recite the tashahhud: 'Al-tahiyyatu lillahi wa al-salawatu wa al-tayyibat…'", "Mukhtasar al-Quduri, how to pray"),
  ("Ending", "In the final sitting, after the tashahhud send blessings on the Prophet ﷺ and make du'a in words like the Qur'an and the reported supplications. Then say 'al-salamu 'alaykum wa rahmatullah' to the right and to the left.", "Mukhtasar al-Quduri, how to pray"),
 ], [
  ("Which touches the ground first when going into sujud?", "The knees", ["The hands", "The forehead", "The nose"], "Knees, then hands, then the face.", "Nur al-Idah"),
  ("What does a follower say when rising from ruku'?", "Only 'rabbana laka al-hamd'", ["Only 'sami' Allahu li-man hamidah'", "Both phrases", "Nothing"], "The imam or one praying alone says both; the follower says only the praise.", "Nur al-Idah"),
  ("What comes after the tashahhud in the final sitting?", "Blessings on the Prophet ﷺ, then du'a, then salam", ["Salam straight away", "Another sujud", "Al-Fatihah"], "Al-Quduri: tashahhud, blessings on the Prophet ﷺ, du'a, then salam right and left.", "Mukhtasar al-Quduri"),
 ]),
"f_sahw": L("f_sahw", "The prostration of forgetfulness", "How to fix a mistake in prayer.", [
  ("When it is wajib", "Two prostrations, with tashahhud and salam, become wajib when a wajib act of the prayer is left out by mistake, even if it happens more than once.", "Nur al-Idah, sujud al-sahw: its ruling"),
  ("How it is done", "The sunnah is to do it after the salam: give one salam to the right, make the two sujud, then sit for tashahhud and end with salam. Doing it before salam is mildly disliked.", "Nur al-Idah, the time of the prostration"),
  ("Not for deliberate mistakes", "If a wajib act is left on purpose, the person is sinful and the prayer must be repeated; the prostration of forgetfulness does not fix it.", "Nur al-Idah, leaving a wajib on purpose"),
 ], [
  ("When is the prostration of forgetfulness made, by the sunnah?", "After one salam to the right", ["Before the first takbir", "After both salams and leaving", "In the middle of the prayer"], "Nur al-Idah: after salam, with one salam to the right.", "Nur al-Idah"),
  ("What makes it wajib?", "Leaving a wajib act by mistake", ["Leaving a pillar", "Leaving a sunnah", "Praying late"], "It repairs a wajib left by mistake. A missed pillar needs the prayer repeated.", "Nur al-Idah"),
  ("You left a wajib act on purpose. What follows?", "You are sinful and repeat the prayer", ["Make the prostration of forgetfulness", "Nothing", "Pray two extra rak'ahs"], "The prostration is for mistakes, not deliberate omissions.", "Nur al-Idah"),
 ]),
"f_jamaah": L("f_jamaah", "Praying in congregation", "Its ruling, who leads, and following the imam.", [
  ("Its ruling", "Praying in congregation is a stressed sunnah.", "Mukhtasar al-Quduri, how to pray"),
  ("Who leads", "The most entitled to lead is the one who knows the sunnah best; if equal, the best reciter; then the most scrupulous; then the oldest.", "Mukhtasar al-Quduri, how to pray"),
  ("Following", "Whoever joins another's prayer needs two intentions: the prayer itself and following the imam. In the Hanafi school the follower does not recite behind the imam.", "Mukhtasar al-Quduri, how to pray"),
 ], [
  ("Who has most right to lead the prayer?", "The one who knows the sunnah best", ["The oldest", "The richest", "The one with the best voice only"], "Al-Quduri puts knowledge of the sunnah first, then recitation, then scrupulousness, then age.", "Mukhtasar al-Quduri"),
  ("Does a follower recite al-Fatihah behind the imam in the Hanafi school?", "No", ["Yes, always", "Only in loud prayers", "Only the first rak'ah"], "Al-Quduri: the follower does not recite behind the imam.", "Mukhtasar al-Quduri"),
  ("What two intentions does a follower need?", "The prayer and following the imam", ["Only the prayer", "Only following", "None"], "Two intentions: the prayer and following.", "Mukhtasar al-Quduri"),
 ]),
"f_travel": L("f_travel", "The traveller's prayer", "When to shorten, and for how long.", [
  ("Shortening", "Someone who intends a journey of three days or more shortens the four-rak'ah fard prayers to two, once he has passed the buildings of his town.", "Nur al-Idah, shortening the prayer; conditions of travel"),
  ("It is required", "In the Hanafi school shortening is required ('azimah), not just allowed. Praying four with a sitting after two is valid but disliked.", "Nur al-Idah, the ruling of shortening"),
  ("How long", "He keeps shortening until he returns home or intends to stay fifteen days or more in one town. If he intends less, or does not know when he will leave, he keeps shortening even for years.", "Nur al-Idah, the period of shortening"),
 ], [
  ("Which prayers are shortened when travelling?", "The four-rak'ah fard prayers", ["All prayers", "Fajr and Maghrib", "Only Jumu'ah"], "Zuhr, 'Asr and 'Isha' become two rak'ahs.", "Nur al-Idah"),
  ("How long must a stay be to stop shortening?", "Fifteen days or more", ["Three days", "Four days", "One month"], "Intending fifteen days or more in one place ends the travel ruling.", "Nur al-Idah"),
  ("In the Hanafi school, shortening is…", "Required", ["Optional", "Disliked", "Only for long journeys by camel"], "Shortening is 'azimah in the school.", "Nur al-Idah"),
 ]),
"f_qada": L("f_qada", "Making up missed prayers", "Missed prayers stay owed until made up.", [
  ("Still owed", "A missed prayer must be made up. A prayer missed while travelling is made up as two rak'ahs, and one missed at home as four, whenever it is made up.", "Nur al-Idah, making up missed prayers"),
  ("In order", "Keeping the order between a missed prayer and the current one, and between missed prayers, is required.", "Nur al-Idah, the ruling of order"),
  ("A grave matter", "Leaving a prayer deliberately out of laziness is so serious that the jurists set a punishment for it in an Islamic state. Make up what you missed, and repent.", "Nur al-Idah, the one who leaves the prayer"),
 ], [
  ("You missed 'Asr on a journey and make it up at home. How many rak'ahs?", "Two", ["Four", "Three", "None"], "It is made up as it was missed: two for a traveller.", "Nur al-Idah"),
  ("Is order between missed prayers required?", "Yes", ["No", "Only for Fajr", "Only in Ramadan"], "Nur al-Idah: the order is required.", "Nur al-Idah"),
  ("A missed prayer…", "Must be made up", ["Is forgiven automatically", "Is replaced by charity", "Only needs du'a"], "It remains owed and must be made up.", "Nur al-Idah"),
 ]),
"f_jumuah": L("f_jumuah", "The Jumu'ah prayer", "Who must attend, and the khutbah.", [
  ("Who must pray it", "Jumu'ah is fard on a man who is free, resident in a town, healthy, safe, able to see and able to walk.", "Nur al-Idah, Jumu'ah: conditions of obligation"),
  ("The khutbah", "Its sunnahs include purity, standing, facing the people, beginning with praise of Allah, the two testimonies, blessings on the Prophet ﷺ, admonition, reciting a verse, and two khutbahs with a sitting between them.", "Nur al-Idah, the khutbah and its sunnahs"),
  ("Women and travellers", "Women and travellers do not have to attend. If someone not obliged attends and prays it, it counts in place of Zuhr.", "Nur al-Idah, Jumu'ah: various rulings"),
 ], [
  ("Is Jumu'ah fard on a traveller?", "No", ["Yes", "Only if near a masjid", "Only in Ramadan"], "Residence is one of its conditions of obligation.", "Nur al-Idah"),
  ("How many khutbahs are given, by the sunnah?", "Two, with a sitting between them", ["One", "Three", "None"], "Two khutbahs with a sitting in between are among its sunnahs.", "Nur al-Idah"),
  ("A woman attends Jumu'ah and prays it. Then…", "It counts in place of Zuhr", ["She must still pray Zuhr", "It does not count", "She prays four extra"], "If those not obliged attend and pray it, it is valid for them in place of Zuhr.", "Nur al-Idah"),
 ]),
"f_janazah": L("f_janazah", "The funeral prayer", "Its ruling, conditions and how it is prayed.", [
  ("Its ruling", "Praying over a Muslim who has died is fard kifayah: if some pray it, the rest are excused. Its pillars are the takbirs and standing.", "Nur al-Idah, the funeral prayer: ruling and pillars"),
  ("Conditions", "The deceased must be Muslim, washed, present and placed in front of the people, on the ground.", "Nur al-Idah, its conditions"),
  ("How it is prayed", "Four takbirs. After the first, praise Allah; after the second, send blessings on the Prophet ﷺ; after the third, make du'a for the deceased; after the fourth, give salam. The imam stands level with the chest.", "Nur al-Idah, its sunnahs"),
 ], [
  ("The funeral prayer is…", "Fard kifayah", ["Fard on everyone", "Sunnah", "Wajib on relatives only"], "If some pray it, the obligation is lifted from the rest.", "Nur al-Idah"),
  ("What is said after the third takbir?", "Du'a for the deceased", ["Blessings on the Prophet ﷺ", "The opening praise", "Salam"], "First praise, second blessings, third du'a, fourth salam.", "Nur al-Idah"),
  ("How many takbirs are in the funeral prayer?", "Four", ["Three", "Five", "Seven"], "The prayer is four takbirs and standing.", "Nur al-Idah"),
 ]),
"f_sawm0": L("f_sawm0", "Ramadan: who fasts and how it begins", "Conditions, the intention and sighting the moon.", [
  ("Who must fast", "Fasting Ramadan is fard on every Muslim who is sane and has reached puberty.", "Nur al-Idah, conditions of obligation"),
  ("What fasting is", "Its essence is holding back from eating, drinking and intercourse from true dawn to sunset, with the intention.", "Nur al-Idah, its pillar; Mukhtasar al-Quduri, Book of Fasting"),
  ("The intention", "For a Ramadan fast, the intention is valid from the night until before the middle of the day (midway between dawn and midday).", "Nur al-Idah, fasts that need no fixed intention"),
  ("The moon", "Ramadan begins by sighting its crescent, or by completing thirty days of Sha'ban if the sky is cloudy.", "Nur al-Idah, how Ramadan is established"),
 ], [
  ("Until when can you make the intention for a Ramadan fast?", "Before the middle of the day", ["Only before dawn", "Until sunset", "Until Zuhr ends"], "Nur al-Idah: from the night until before the 'great forenoon', the middle of the day.", "Nur al-Idah"),
  ("If the moon cannot be seen on the 29th of Sha'ban…", "Complete thirty days of Sha'ban", ["Start fasting anyway", "Follow a calculation only", "Fast half a day"], "Ramadan is established by sighting or by completing thirty days.", "Nur al-Idah"),
  ("Fasting means holding back from…", "Eating, drinking and intercourse from dawn to sunset", ["Only food", "Only during daylight hours of work", "Talking"], "That is the pillar of the fast, with the intention.", "Mukhtasar al-Quduri"),
 ]),
"f_fitr": L("f_fitr", "Zakat al-Fitr", "Who pays it, how much and when.", [
  ("Who pays", "It is wajib on a free Muslim who owns the nisab beyond his home, clothes, furniture and basic needs. He pays for himself and his young children.", "Mukhtasar al-Quduri, chapter on Sadaqat al-Fitr"),
  ("How much", "Half a sa' of wheat, or a sa' of dates, raisins or barley, or their value.", "Mukhtasar al-Quduri, chapter on Sadaqat al-Fitr"),
  ("When", "It becomes due at dawn on the day of Eid. It is recommended to give it before going out to the Eid prayer; giving it earlier is allowed, and delaying it does not cancel it.", "Mukhtasar al-Quduri, chapter on Sadaqat al-Fitr"),
 ], [
  ("When does zakat al-fitr become due?", "At dawn on the day of Eid", ["At the start of Ramadan", "After the Eid prayer", "On the 27th night"], "Al-Quduri: it is tied to the dawn of the day of Fitr.", "Mukhtasar al-Quduri"),
  ("Who does a father pay it for?", "Himself and his young children", ["Only himself", "His whole extended family", "His wife and adult children only"], "He pays for himself and his young children; not for his wife or adult children.", "Mukhtasar al-Quduri"),
  ("If it is delayed past Eid…", "It must still be paid", ["It is cancelled", "It doubles", "It turns into a fast"], "Delaying it does not make it fall away.", "Mukhtasar al-Quduri"),
 ]),

# ======================= AQEEDAH =======================
"aq_kutub": L("aq_kutub", "Angels, Books and Messengers", "Believing in all of them without distinction.", [
  ("All of them", "We believe in the angels, the Prophets and the Books sent down to the Messengers, and we bear witness that they were upon the clear truth.", "al-'Aqidah al-Tahawiyyah, on the angels and books"),
  ("No distinction", "We make no distinction between any of His Messengers, and we accept all of them in what they brought.", "al-'Aqidah al-Tahawiyyah, on the Messengers"),
  ("Honoured ones", "Allah took Ibrahim عليه السلام as His close friend and spoke to Musa عليه السلام directly. Muhammad ﷺ is the Seal of the Prophets and the master of the Messengers.", "al-'Aqidah al-Tahawiyyah, on the Prophet ﷺ"),
  ("The recording angels", "We believe in the noble scribes whom Allah has made guardians over us, and in the Angel of Death who takes the souls.", "al-'Aqidah al-Tahawiyyah, on the hereafter"),
 ], [
  ("How do we believe in the Messengers?", "In all of them, without distinction", ["Only in the last one", "Only in those we know by name", "In most of them"], "Al-Tahawi: we make no distinction between any of His Messengers.", TH),
  ("To whom did Allah speak directly?", "Musa عليه السلام", ["Ibrahim عليه السلام", "'Isa عليه السلام", "Nuh عليه السلام"], "'Allah spoke to Musa directly' — quoted by al-Tahawi from the Qur'an.", TH),
  ("Who are the 'noble scribes'?", "The angels who record our deeds", ["The Companions who wrote the Qur'an", "The scholars", "The Prophets"], "Allah has made them guardians over us, recording our deeds.", TH),
 ]),
"aq_ruya": L("aq_ruya", "Seeing Allah in Paradise", "A truth for the people of Paradise, without 'how'.", [
  ("It is true", "The believers will see Allah in Paradise, without encompassing Him and without asking how. 'Faces that Day will be radiant, looking at their Lord.' (al-Qiyamah 22–23)", "al-'Aqidah al-Tahawiyyah, the seeing of Allah"),
  ("As Allah meant it", "Its meaning is as Allah intended and knows. Whatever the sound hadith say about it is as the Prophet ﷺ said.", "al-'Aqidah al-Tahawiyyah, the seeing of Allah"),
  ("Submit", "No one's religion is safe except the one who submits to Allah and His Messenger ﷺ and leaves what is unclear to the One who knows it.", "al-'Aqidah al-Tahawiyyah, the seeing of Allah"),
 ], [
  ("Will the believers see Allah?", "Yes, in Paradise, without 'how'", ["No, never", "Yes, in this world", "Only the Prophets"], "Al-Tahawi: the seeing is true for the people of Paradise without encompassing or 'how'.", TH),
  ("Which verse does al-Tahawi cite?", "'Faces that Day will be radiant, looking at their Lord'", ["Ayat al-Kursi", "'Say: He is Allah, One'", "'There is nothing like Him'"], "He cites al-Qiyamah 22–23.", TH),
  ("How do we take the hadith about it?", "As the Prophet ﷺ said, meant as Allah intends", ["By our own opinions", "We reject them", "By comparing to creation"], "We do not interpret by our opinions or imagine with our desires.", TH),
 ]),
"aq_sins": L("aq_sins", "Sin, faith and hope", "A sin does not take a believer out of Islam.", [
  ("No takfir for sin", "We do not declare anyone of the people of the qiblah a disbeliever for a sin, as long as he does not hold it to be lawful.", "al-'Aqidah al-Tahawiyyah, on sin and faith"),
  ("Major sins", "Those of the Ummah who commit major sins will not be in the Fire forever if they die believing in Allah's Oneness. They are in His will: if He wills He forgives them, and if He wills He punishes them by His justice.", "al-'Aqidah al-Tahawiyyah, the people of major sins"),
  ("Between hope and fear", "We hope for the good-doers and fear for the wrongdoers, without despairing for them. Feeling safe from Allah and despairing of Him both take one away from Islam; the path of truth is between them.", "al-'Aqidah al-Tahawiyyah, on sin and faith"),
 ], [
  ("Is a Muslim who commits a sin a disbeliever?", "No, unless he holds it to be lawful", ["Yes, always", "Only for major sins", "Only if he repeats it"], "Al-Tahawi: no takfir for a sin unless he deems it lawful.", TH),
  ("A believer who dies with major sins…", "Is under Allah's will; he will not be in the Fire forever", ["Is in the Fire forever", "Is certainly forgiven", "Is not a believer"], "He will not remain forever, and is under Allah's will.", TH),
  ("The path of truth is…", "Between hope and fear", ["Feeling completely safe", "Despairing of mercy", "Ignoring the hereafter"], "Both feeling safe and despairing are dangerous; the way is between them.", TH),
 ]),
"aq_signs": L("aq_signs", "Signs of the Hour", "The major signs al-Tahawi lists.", [
  ("The signs", "We believe in the signs of the Hour, among them: the emergence of the Dajjal, and the descent of 'Isa ibn Maryam عليه السلام from the sky.", "al-'Aqidah al-Tahawiyyah, the signs of the Hour"),
  ("The last ones", "We believe in the rising of the sun from where it sets, and the emergence of the Beast of the Earth from its place.", "al-'Aqidah al-Tahawiyyah, the signs of the Hour"),
  ("Fortune-tellers", "We do not believe a soothsayer or fortune-teller, nor anyone who claims something against the Book, the Sunnah and the consensus of the Ummah.", "al-'Aqidah al-Tahawiyyah, conclusion"),
 ], [
  ("Which is a sign of the Hour al-Tahawi mentions?", "The descent of 'Isa عليه السلام", ["A great flood", "The return of the Pharaoh", "The end of all rain"], "He lists the Dajjal, the descent of 'Isa, the sun rising from the west and the Beast.", TH),
  ("The sun will rise from…", "Where it sets", ["The north", "Two places", "The same place, but red"], "The rising of the sun from where it sets is one of the signs.", TH),
  ("What do we do with a fortune-teller's claims?", "We do not believe them", ["Believe them if they come true", "Ask them about the future", "Believe them on Fridays"], "Al-Tahawi: we do not believe a soothsayer or fortune-teller.", TH),
 ]),
"aq_jamaa": L("aq_jamaa", "Following the Sunnah and the Jama'ah", "Unity, good opinion of Muslims, and leaving judgement to Allah.", [
  ("Praying together", "We pray behind every Muslim of the qiblah, righteous or sinful, and pray over those of them who die.", "al-'Aqidah al-Tahawiyyah, the people of the qiblah"),
  ("Leave it to Allah", "We do not place any of them in Paradise or the Fire, nor accuse them of disbelief, shirk or hypocrisy unless it shows. We leave what is hidden to Allah.", "al-'Aqidah al-Tahawiyyah, the people of the qiblah"),
  ("The Jama'ah", "We follow the Sunnah and the Jama'ah, and avoid oddity, dispute and division. We see the Jama'ah as true and right, and division as straying and punishment.", "al-'Aqidah al-Tahawiyyah, the imams and the Jama'ah; conclusion"),
 ], [
  ("Behind whom may we pray?", "Every Muslim of the qiblah, righteous or sinful", ["Only the most pious", "Only people of our group", "Only scholars"], "Al-Tahawi: behind every righteous or sinful one of the people of the qiblah.", TH),
  ("May we declare a particular Muslim to be in the Fire?", "No, we leave what is hidden to Allah", ["Yes, if he sins", "Yes, if we dislike him", "Only after he dies"], "We do not place any of them in Paradise or the Fire.", TH),
  ("How does al-Tahawi describe division?", "Straying and punishment", ["Mercy", "Necessary", "A sign of knowledge"], "He calls the Jama'ah true and division straying and punishment.", TH),
 ]),

# ======================= HALAL & HARAM =======================
"hh7": L("hh7", "Honesty in trade", "Cheating in the market, from al-Ghazali.", [
  ("Lying about the price", "Al-Ghazali names, among the common wrongs of the market, lying about what you paid for goods so you can sell at a 'profit'. Whoever knows of it should tell the buyer.", "Ihya' 'Ulum al-Din, Book of Commanding Good: wrongs of the market"),
  ("Hiding defects", "Hiding a fault in what you sell is also forbidden. Whoever knows the fault must point it out, or he is content with his brother's loss.", "Ihya' 'Ulum al-Din, Book of Commanding Good: wrongs of the market"),
  ("Weights and measures", "Giving short weight or short measure must be stopped. The Prophet ﷺ said: 'Whoever cheats us is not one of us.'", "Ihya', wrongs of the market; Hadith, Sahih Muslim"),
 ], [
  ("Saying 'I bought it for ten' when you paid less is…", "Lying, and forbidden", ["Good business", "Allowed if the buyer agrees", "Only disliked"], "Al-Ghazali lists lying in the cost price among the wrongs of the market.", "Ihya'"),
  ("If you know a fault in an item you are selling…", "You must point it out", ["Stay quiet unless asked", "Lower the price only", "Sell it quickly"], "Hiding it means being content with your brother's loss.", "Ihya'"),
  ("'Whoever cheats us…'", "'…is not one of us'", ["'…must pay double'", "'…will be poor'", "'…is forgiven if he repents later'"], "The hadith in Sahih Muslim.", "Sahih Muslim"),
 ]),

# ======================= SEERAH =======================
"sr1b": L("sr1b", "Childhood and youth ﷺ", "With Halimah, Abu Talib, and his marriage to Khadijah.", [
  ("In the desert", "He ﷺ was nursed by Halimah al-Sa'diyyah among Banu Sa'd and stayed with her about four years. There his chest was opened.", "al-Fusul fi Sirat al-Rasul, his birth, nursing and upbringing"),
  ("Losing his mother", "His mother took him to visit relatives in Madinah and died at al-Abwa' on the way back, when he was six. Years later, passing al-Abwa' in the year of the Opening, he visited her grave and wept.", "al-Fusul fi Sirat al-Rasul, his birth, nursing and upbringing"),
  ("To Syria", "At twelve his uncle Abu Talib took him on a trade journey to Syria. Later he travelled there again trading for Khadijah رضي الله عنها.", "al-Fusul fi Sirat al-Rasul, his birth, nursing and upbringing"),
  ("Marriage", "Khadijah saw his honesty and character and wished to marry him. He married her when he was twenty-five.", "al-Fusul fi Sirat al-Rasul, his birth, nursing and upbringing"),
 ], [
  ("Who nursed the Prophet ﷺ?", "Halimah al-Sa'diyyah", ["Aminah only", "Umm Ayman", "Khadijah"], "He was nursed among Banu Sa'd by Halimah.", "al-Fusul"),
  ("Where did his mother pass away?", "At al-Abwa'", ["In Makkah", "In Ta'if", "In Syria"], "She died at al-Abwa' returning from Madinah.", "al-Fusul"),
  ("How old was he ﷺ when he married Khadijah?", "Twenty-five", ["Forty", "Twenty", "Thirty"], "Ibn Kathir: he married her at twenty-five.", "al-Fusul"),
 ]),
"sr_family": L("sr_family", "His family ﷺ", "His children and his wives, the Mothers of the Believers.", [
  ("His children", "All his children were from Khadijah رضي الله عنها except Ibrahim, from Mariyah. They were al-Qasim (his kunyah Abu al-Qasim is from him), Zaynab, Ruqayyah, Umm Kulthum, Fatimah, 'Abdullah and Ibrahim.", "al-Fusul fi Sirat al-Rasul, his children"),
  ("Fatimah رضي الله عنها", "All of his children died before him except Fatimah رضي الله عنها, who passed away a few months after him.", "al-Fusul fi Sirat al-Rasul, his children"),
  ("Khadijah first", "His first wife was Khadijah رضي الله عنها, the first to believe in him. He married no one else in her lifetime.", "al-Fusul fi Sirat al-Rasul, his wives"),
  ("'A'ishah رضي الله عنها", "Of his wives, no woman of this Ummah is known to have reached her level of knowledge.", "al-Fusul fi Sirat al-Rasul, his wives"),
 ], [
  ("Which of his children outlived him ﷺ?", "Fatimah رضي الله عنها", ["Zaynab", "Ibrahim", "Al-Qasim"], "All died before him except Fatimah, who died a few months after.", "al-Fusul"),
  ("Who was his first wife ﷺ?", "Khadijah رضي الله عنها", ["'A'ishah رضي الله عنها", "Sawdah رضي الله عنها", "Hafsah رضي الله عنها"], "Khadijah was first, and he married no one else in her lifetime.", "al-Fusul"),
  ("Why was he called Abu al-Qasim?", "After his son al-Qasim", ["After his grandfather", "After a Companion", "It was his father's name"], "Al-Qasim was his eldest, and the kunyah is from him.", "al-Fusul"),
 ]),

# ======================= QUR'AN =======================
"qr0": L("qr0", "The virtue of the Qur'an", "Why learning and reciting it matters, from al-Tibyan.", [
  ("The best of you", "The Prophet ﷺ said: 'The best of you is the one who learns the Qur'an and teaches it.'", "al-Tibyan, chapter one; Hadith, Sahih al-Bukhari"),
  ("Even when it is hard", "'The one skilled in the Qur'an is with the noble, righteous scribes (angels), and the one who stumbles over it and finds it hard has two rewards.'", "al-Tibyan, chapter one; Hadith, al-Bukhari and Muslim"),
  ("Every letter", "'Whoever reads a letter of the Book of Allah has a good deed, and a good deed is multiplied ten times. I do not say Alif Lam Mim is a letter: Alif is a letter, Lam is a letter and Mim is a letter.'", "al-Tibyan, chapter one; Hadith, al-Tirmidhi"),
 ], [
  ("Who is 'the best of you', in the hadith?", "The one who learns the Qur'an and teaches it", ["The richest", "The one who fasts most", "The eldest"], "Narrated by al-Bukhari and quoted by al-Nawawi in al-Tibyan.", "al-Tibyan"),
  ("The one who stumbles while reciting…", "Has two rewards", ["Has no reward", "Should stop reciting", "Has half a reward"], "The hadith gives him two rewards for his effort.", "al-Tibyan"),
  ("How many good deeds for one letter?", "One good deed, multiplied ten times", ["One only", "A hundred", "None until the surah is finished"], "Each letter is a good deed, multiplied by ten.", "al-Tibyan"),
 ]),

# ======================= TAZKIYAH =======================
"tz_dhikr": L("tz_dhikr", "Remembrance of Allah", "The heart is polished by dhikr.", [
  ("A command", "Al-Qushayri opens his chapter on dhikr with: 'O you who believe, remember Allah much.' (al-Ahzab 41)", "al-Risalah al-Qushayriyyah, chapter on dhikr"),
  ("He remembers you", "Allah says: 'So remember Me, I will remember you.' (al-Baqarah 152)", "Qur'an, al-Baqarah 152"),
  ("Hearts at rest", "'Truly, in the remembrance of Allah hearts find rest.' (al-Ra'd 28)", "Qur'an, al-Ra'd 28"),
 ], [
  ("Which verse opens al-Qushayri's chapter on dhikr?", "'O you who believe, remember Allah much'", ["Ayat al-Kursi", "'Read in the name of your Lord'", "Al-Fatihah"], "He begins with al-Ahzab 41.", "al-Risalah al-Qushayriyyah"),
  ("'Remember Me…'", "'…I will remember you'", ["'…and you will be rich'", "'…once a day'", "'…in Ramadan'"], "Al-Baqarah 152.", "Qur'an"),
  ("In what do hearts find rest?", "The remembrance of Allah", ["Wealth", "Praise from people", "Rest from work"], "Al-Ra'd 28.", "Qur'an"),
 ]),
"tz_tawakkul": L("tz_tawakkul", "Trust in Allah (tawakkul)", "Relying on Allah while taking the means.", [
  ("He is enough", "Al-Qushayri opens his chapter on trust with: 'Whoever puts his trust in Allah, He is enough for him.' (al-Talaq 3)", "al-Risalah al-Qushayriyyah, chapter on tawakkul"),
  ("Believers rely on Him", "'And upon Allah let the believers rely.' (Al 'Imran 122)", "al-Risalah al-Qushayriyyah, chapter on tawakkul"),
  ("Tie your camel", "A man asked whether to tie his camel and trust Allah, or leave it and trust. The Prophet ﷺ said: 'Tie it, and trust.'", "Hadith, al-Tirmidhi"),
 ], [
  ("'Whoever puts his trust in Allah…'", "'…He is enough for him'", ["'…will never be tested'", "'…need not work'", "'…will be rich'"], "Al-Talaq 3, quoted at the start of al-Qushayri's chapter.", "al-Risalah al-Qushayriyyah"),
  ("Does trusting Allah mean leaving the means?", "No: tie your camel, and trust", ["Yes, leave all means", "Only for scholars", "Only when travelling"], "The hadith joins taking the means with trust in Allah.", "al-Tirmidhi"),
  ("Upon whom should the believers rely?", "Allah", ["Their wealth", "Their family", "Their own strength"], "Al 'Imran 122.", "al-Risalah al-Qushayriyyah"),
 ]),
"tz_sabr": L("tz_sabr", "Patience (sabr)", "Patience is by Allah's help.", [
  ("By Allah", "Al-Qushayri opens his chapter on patience with: 'Be patient, and your patience is only by Allah.' (al-Nahl 127)", "al-Risalah al-Qushayriyyah, chapter on sabr"),
  ("With the patient", "'O you who believe, seek help through patience and prayer. Truly Allah is with the patient.' (al-Baqarah 153)", "Qur'an, al-Baqarah 153"),
  ("At the first blow", "The Prophet ﷺ said: 'Patience is at the first blow.'", "Hadith, al-Bukhari and Muslim"),
 ], [
  ("'Be patient, and your patience is only…'", "'…by Allah'", ["'…for a while'", "'…for the strong'", "'…in hardship'"], "Al-Nahl 127, quoted at the start of al-Qushayri's chapter.", "al-Risalah al-Qushayriyyah"),
  ("Allah is with…", "The patient", ["The wealthy", "The famous", "Those who never feel sad"], "Al-Baqarah 153.", "Qur'an"),
  ("When does true patience count most?", "At the first blow", ["After a week", "Once you feel better", "When others notice"], "'Patience is at the first blow.' (al-Bukhari and Muslim)", "al-Bukhari and Muslim"),
 ]),
}

ORDER = {
 "aqeedah": ["belief1", "aq_proof", "belief2", "belief3", "belief4", "aq_speech", "aq_jaiz", "belief5", "aq_kutub", "aq_shahada",
             "belief6", "aq_sins", "aq_akhira", "aq_ruya", "aq_qadr", "aq_signs", "aq_awliya", "aq_jamaa"],
 "fiqh": ["fiqh0", "f_istinja", "purity1", "purity2", "purity3", "purity4", "purity5", "f_najasa", "purity6", "fiqh_khuff", "fiqh_hayd",
          "f_times", "f_adhan", "prayer1", "prayer2", "prayer3", "f_how1", "f_how2", "f_sahw", "prayer4", "prayer5",
          "f_jamaah", "f_travel", "f_qada", "f_jumuah", "f_janazah",
          "f_sawm0", "fasting1", "fasting2", "fasting3", "zakat1", "zakat2", "zakat3", "f_fitr"],
 "halal": ["hh1", "hh2", "hh3", "hh4", "hh5", "hh6", "hh7"],
 "seerah": ["sr1", "sr1b", "sr2", "sr3", "sr4", "sr5", "sr6", "sr_family", "sr7"],
 "quran": ["qr0", "qr1", "qr2", "qr3", "qr4", "qr5"],
 "tazkiyah": ["heart1", "heart2", "heart3", "heart4", "heart5", "tz_dhikr", "tz_tawakkul", "tz_sabr"],
}

# ======================= HAJJ (Mukhtasar al-Quduri, Book of Hajj) =======================
HJ = "Mukhtasar al-Quduri, Book of Hajj"
MORE.update({
"hj1": L("hj1", "Who must perform Hajj", "The conditions, and the months of Hajj.", [
  ("Once in a lifetime", "Hajj is fard on free, adult, sane and healthy Muslims who can afford the provision and transport, beyond their home, their needs and their family's maintenance until they return, when the road is safe.", HJ),
  ("A woman's companion", "A woman must have a mahram or her husband with her if Makkah is three days' journey or more away. She may not go for Hajj without one of them.", HJ),
  ("The months", "The months of Hajj are Shawwal, Dhu al-Qa'dah and the first ten days of Dhu al-Hijjah.", "Mukhtasar al-Quduri, chapter on Tamattu'"),
 ], [
  ("Hajj is fard on someone who…", "Can afford provision and transport beyond their needs and family's maintenance", ["Has any savings at all", "Lives near Makkah only", "Has completed 'umrah"], "Al-Quduri ties it to affording provision and transport beyond needs and family maintenance, with a safe road.", HJ),
  ("Can a woman go for Hajj without a mahram or husband, from far away?", "No", ["Yes, with a group", "Yes, if she is over 40", "Only for 'umrah"], "Al-Quduri: she may not perform Hajj without a mahram or husband if the journey is three days or more.", HJ),
  ("Which are the months of Hajj?", "Shawwal, Dhu al-Qa'dah and ten days of Dhu al-Hijjah", ["Ramadan and Shawwal", "Only Dhu al-Hijjah", "Muharram to Rajab"], "Al-Quduri defines them in the chapter on tamattu'.", "Mukhtasar al-Quduri"),
 ]),
"hj2": L("hj2", "The miqat and entering ihram", "Where to enter ihram, and how.", [
  ("The miqats", "Do not pass these without ihram: Dhu al-Hulayfah for the people of Madinah, Dhat 'Irq for Iraq, al-Juhfah for Syria, Qarn al-Manazil for Najd, and Yalamlam for Yemen. Entering ihram before them is allowed.", "Mukhtasar al-Quduri, chapter on the miqats"),
  ("Preparing", "Make ghusl (or wudu, but ghusl is better), put on two clean sheets, a lower and an upper one, apply perfume if you have it, and pray two rak'ahs.", HJ),
  ("Intention and talbiyah", "Say: 'O Allah, I intend Hajj, make it easy for me and accept it from me.' Then say the talbiyah: 'Labbayk Allahumma labbayk, labbayk la sharika laka labbayk, inna al-hamda wa al-ni'mata laka wa al-mulk, la sharika lak.' With the talbiyah you are in ihram.", HJ),
 ], [
  ("What is the miqat for people coming from Madinah?", "Dhu al-Hulayfah", ["Yalamlam", "Qarn al-Manazil", "Al-Juhfah"], "Al-Quduri: Dhu al-Hulayfah for the people of Madinah.", "Mukhtasar al-Quduri"),
  ("When do you actually enter ihram?", "When you say the talbiyah with the intention", ["When you put on the sheets", "When you reach Makkah", "When you see the Ka'bah"], "'When he says the talbiyah, he has entered ihram.'", HJ),
  ("Before ihram, which is better?", "Ghusl", ["Wudu", "Tayammum", "Neither"], "Ghusl or wudu, and ghusl is better.", HJ),
 ]),
"hj3": L("hj3", "What ihram forbids", "What the muhrim must avoid.", [
  ("Behaviour", "Avoid intimacy and its talk, sinning and arguing. Do not hunt, or point out or direct anyone to game.", HJ),
  ("Clothing", "A man does not wear a shirt, trousers, turban, cap, cloak or khuffs (unless he has no sandals, then he cuts them below the ankles), and does not cover his head or face.", HJ),
  ("Body", "Do not use perfume, shave the head or body hair, trim the beard or cut the nails. Bathing, shade and wearing a money belt are allowed.", HJ),
  ("Women", "A woman is like a man in all this, except that she covers her head and uncovers her face, does not raise her voice in the talbiyah, does not jog in tawaf or run between the green markers, and trims her hair instead of shaving.", HJ),
 ], [
  ("May a man in ihram cover his head?", "No", ["Yes, with a cap", "Only at night", "Only in the sun"], "Al-Quduri: he does not cover his head or face.", HJ),
  ("Which is allowed in ihram?", "Taking a bath", ["Using perfume", "Cutting the nails", "Trimming the beard"], "Bathing, shade and a money belt are allowed.", HJ),
  ("In ihram, a woman…", "Covers her head and uncovers her face", ["Uncovers her head", "Shaves her head at the end", "Jogs in tawaf"], "She keeps her head covered and her face uncovered.", HJ),
 ]),
"hj4": L("hj4", "The three ways of Hajj", "Ifrad, tamattu' and qiran.", [
  ("Ifrad", "Entering ihram for Hajj alone.", HJ),
  ("Tamattu'", "Entering ihram for 'umrah in the months of Hajj, completing it and leaving ihram, then entering ihram for Hajj from Makkah on the 8th (Yawm al-Tarwiyah). A sacrifice is due; if you cannot, fast three days during Hajj and seven when you return.", "Mukhtasar al-Quduri, chapter on Tamattu'"),
  ("Qiran", "Entering ihram for 'umrah and Hajj together from the miqat. In the Hanafi school qiran is the best, then tamattu', then ifrad. It too requires a sacrifice.", "Mukhtasar al-Quduri, chapter on Qiran"),
  ("People of Makkah", "The people of Makkah do not do tamattu' or qiran; only ifrad.", "Mukhtasar al-Quduri, chapter on Tamattu'"),
 ], [
  ("Which way of Hajj is best in the Hanafi school?", "Qiran", ["Ifrad", "Tamattu'", "All are equal"], "Al-Quduri: qiran is better than tamattu' and ifrad.", "Mukhtasar al-Quduri"),
  ("In tamattu', when do you enter ihram for Hajj?", "On the 8th of Dhu al-Hijjah, from Makkah", ["At the miqat with the 'umrah", "On the day of 'Arafah at 'Arafah", "After the Eid prayer"], "After completing the 'umrah you stay in Makkah and enter ihram for Hajj on Yawm al-Tarwiyah.", "Mukhtasar al-Quduri"),
  ("A mutamatti' who cannot afford the sacrifice…", "Fasts three days in Hajj and seven at home", ["Pays nothing", "Fasts one month", "Must do Hajj again"], "Three days during Hajj and seven when he returns.", "Mukhtasar al-Quduri"),
 ]),
"hj5": L("hj5", "Tawaf and sa'y", "Arriving in Makkah.", [
  ("The Black Stone", "Enter al-Masjid al-Haram. On seeing the House say takbir and tahlil. Begin at the Black Stone: face it, say takbir, raise your hands and touch and kiss it if you can without harming anyone.", HJ),
  ("Seven circuits", "Go round the House seven times, with the Ka'bah on your left, outside the Hatim. Men uncover the right shoulder (idtiba') and jog (raml) in the first three circuits, then walk. Touch the Stone each time you pass it if you can, and end with it.", HJ),
  ("Two rak'ahs", "Pray two rak'ahs at the Station of Ibrahim, or wherever is easy in the masjid.", HJ),
  ("Sa'y", "Go to al-Safa, face the House, say takbir and tahlil, send blessings on the Prophet ﷺ and make du'a. Walk to al-Marwah, men running between the two green markers. That is one circuit; complete seven, starting at al-Safa and ending at al-Marwah.", HJ),
 ], [
  ("Where does each circuit of tawaf begin?", "At the Black Stone", ["At the door of the Ka'bah", "At the Station of Ibrahim", "At al-Safa"], "Al-Quduri: begin at the Black Stone.", HJ),
  ("In which circuits do men jog (raml)?", "The first three", ["All seven", "The last three", "Only the first"], "Raml is in the first three circuits.", HJ),
  ("Sa'y starts at… and ends at…", "Al-Safa, al-Marwah", ["Al-Marwah, al-Safa", "The Black Stone, al-Safa", "Zamzam, al-Marwah"], "Seven circuits, starting at al-Safa and ending at al-Marwah.", HJ),
 ]),
"hj6": L("hj6", "Mina, 'Arafah and Muzdalifah", "The 8th and 9th of Dhu al-Hijjah.", [
  ("To Mina", "On the 8th (Yawm al-Tarwiyah), after Fajr in Makkah, go to Mina and stay until you pray Fajr on the day of 'Arafah.", HJ),
  ("'Arafah", "The standing at 'Arafah is the heart of Hajj. Whoever is at 'Arafah at any time from midday on the 9th until dawn on the 10th has caught the Hajj. All of 'Arafah is a place of standing except Batn 'Uranah. Strive in du'a.", HJ),
  ("Muzdalifah", "After sunset, leave calmly for Muzdalifah. Pray Maghrib and 'Isha' there together. After Fajr, stand and make du'a, then leave for Mina before sunrise.", HJ),
 ], [
  ("When is the time for standing at 'Arafah?", "From midday on the 9th until dawn on the 10th", ["Only after 'Asr", "The whole of the 8th", "Only at sunset"], "Al-Quduri: from the sun's decline on the day of 'Arafah to dawn on the day of sacrifice.", HJ),
  ("Where are Maghrib and 'Isha' prayed on the night of the 9th?", "Together at Muzdalifah", ["At 'Arafah", "On the road", "In Makkah"], "Praying Maghrib on the road is not valid in the view of Abu Hanifah and Muhammad.", HJ),
  ("Which part of 'Arafah is not a place of standing?", "Batn 'Uranah", ["Jabal al-Rahmah", "The edges", "All of it is valid"], "All of 'Arafah is valid except Batn 'Uranah.", HJ),
 ]),
"hj7": L("hj7", "The Day of Sacrifice and after", "Stoning, sacrifice, shaving and tawaf al-ziyarah.", [
  ("Jamrat al-'Aqabah", "On the 10th, stone Jamrat al-'Aqabah with seven pebbles, saying takbir with each. Stop the talbiyah with the first pebble.", HJ),
  ("Sacrifice and shaving", "Then sacrifice, then shave or trim; shaving is better. Now everything is lawful except intimacy.", HJ),
  ("Tawaf al-Ziyarah", "Go to Makkah on the 10th, 11th or 12th and perform tawaf al-ziyarah, seven circuits. This is the fard tawaf of Hajj. After it, intimacy becomes lawful. Delaying it past these days requires a sacrifice, according to Abu Hanifah.", HJ),
  ("The days of Mina", "Return to Mina. On the 11th and 12th, after midday, stone the three jamarat, starting with the one nearest the Masjid al-Khayf, seven pebbles each, stopping to make du'a after the first two. You may leave on the 12th or stay for the 13th.", HJ),
 ], [
  ("Which jamrah is stoned on the 10th?", "Jamrat al-'Aqabah only", ["All three", "The small one", "None"], "On the day of sacrifice only Jamrat al-'Aqabah is stoned.", HJ),
  ("What is the fard tawaf of Hajj?", "Tawaf al-Ziyarah", ["Tawaf al-Qudum", "Tawaf al-Wada'", "Any voluntary tawaf"], "Al-Quduri: 'This tawaf is the one that is fard in Hajj.'", HJ),
  ("After stoning, sacrificing and shaving, what remains forbidden until tawaf al-ziyarah?", "Intimacy with one's spouse", ["Perfume", "Normal clothes", "Cutting nails"], "Everything becomes lawful except intimacy, which becomes lawful after tawaf al-ziyarah.", HJ),
 ]),
"hj8": L("hj8", "Farewell, and the wajibs of Hajj", "Tawaf al-Wada', and what a sacrifice repairs.", [
  ("Farewell tawaf", "Before leaving Makkah, perform tawaf al-sadr (the farewell tawaf), seven circuits without jogging. It is wajib, except for the people of Makkah. A woman who gets her period after tawaf al-ziyarah may leave without it.", HJ),
  ("Missed wajibs", "Leaving sa'y, the standing at Muzdalifah, the stoning, or the farewell tawaf requires a sheep, and the Hajj is still complete.", "Mukhtasar al-Quduri, chapter on the violations of the muhrim"),
  ("The pillars", "Missing the standing at 'Arafah means the Hajj is missed. Tawaf al-ziyarah must be done; a sacrifice cannot replace it.", "Mukhtasar al-Quduri, chapter on the violations of the muhrim"),
 ], [
  ("Someone left out sa'y. What follows?", "A sheep is due and the Hajj is complete", ["The Hajj is invalid", "Nothing", "He fasts three days"], "Al-Quduri: 'Whoever leaves the sa'y owes a sheep, and his Hajj is complete.'", "Mukhtasar al-Quduri"),
  ("Is the farewell tawaf wajib on the people of Makkah?", "No", ["Yes", "Only for women", "Only after qiran"], "It is wajib except on the people of Makkah.", HJ),
  ("A woman's period starts after tawaf al-ziyarah. Before leaving she…", "May leave without the farewell tawaf", ["Must wait until she is pure", "Owes a sheep", "Must repeat Hajj"], "Al-Quduri: she leaves, and owes nothing for missing tawaf al-sadr.", "Mukhtasar al-Quduri"),
 ]),
"hj9": L("hj9", "'Umrah", "Its ruling and its acts.", [
  ("Its ruling", "'Umrah is a sunnah. It can be done at any time of year, but is disliked on five days: the day of 'Arafah, the day of sacrifice and the three days of tashriq.", "Mukhtasar al-Quduri, chapter on missing Hajj"),
  ("Its acts", "'Umrah is: ihram, tawaf, sa'y, and shaving or trimming.", "Mukhtasar al-Quduri, chapter on missing Hajj"),
  ("The talbiyah", "The one in 'umrah stops the talbiyah when he starts the tawaf.", "Mukhtasar al-Quduri, chapter on Tamattu'"),
 ], [
  ("What is the ruling of 'umrah in the Hanafi school?", "Sunnah", ["Fard", "Wajib", "Disliked"], "Al-Quduri: 'umrah is sunnah.", "Mukhtasar al-Quduri"),
  ("On which day is 'umrah disliked?", "The day of 'Arafah", ["Any Friday", "In Ramadan", "In Rajab"], "It is disliked on 'Arafah, the day of sacrifice and the days of tashriq.", "Mukhtasar al-Quduri"),
  ("What are the acts of 'umrah?", "Ihram, tawaf, sa'y, then shaving or trimming", ["Tawaf only", "Standing at 'Arafah", "Stoning and sacrifice"], "Al-Quduri lists exactly these.", "Mukhtasar al-Quduri"),
 ]),
})
ORDER["fiqh"] = ORDER["fiqh"] + ["hj1", "hj2", "hj3", "hj4", "hj9", "hj5", "hj6", "hj7", "hj8"]
