"""Second pass on the Learn (Fard al-'Ayn) courses, after review by Abd al-Rahman Naqshbandi.
Every question must make sense on its own (say what it is about), every Arabic term is explained the first
time it appears, and the explanation teaches, not just repeats the answer.
CHECKS replaces a lesson's questions; CARDS replaces or adds cards; NEW_LESSONS adds lessons."""

UB, TH = "Umm al-Barahin", "al-'Aqidah al-Tahawiyyah"
NI, QD = "Nur al-Idah", "Mukhtasar al-Quduri"

# ---------------------------------------------------------------- cards: (lesson, index) -> (title, text). index "+N" inserts before N; "+" appends.
CARDS = {
 # Aqeedah
 ("belief1", 0): ("Your first duty", "Aqeedah means belief: what a Muslim holds to be true in the heart. Every Muslim who has reached adulthood and is sane must know what is necessary for Allah, what is impossible for Him, and what is possible for Him, and the same for the Messengers عليهم السلام."),
 ("belief1", 1): ("Three kinds of judgement", "Scholars sort everything the mind can think of into three. Necessary (wajib): the mind cannot picture it not being there, like Allah's existence. Impossible (mustahil): the mind cannot picture it existing, like Allah having a partner. Possible (ja'iz): it may exist or not, like rain tomorrow."),
 ("aq_proof", 0): ("Everything changes", "Look at the world: things move then stop, grow then fade, arrive then leave. Each new state had a beginning. Imam al-Sanusi رحمه الله says something that is never free of changes that begin must itself have begun. So the world came into being; it has not always been there."),
 ("aq_proof", 1): ("It needs a Maker", "Something that came into being cannot bring itself into being, just as a house does not build itself. So the world needs a Maker who did not come into being: Allah."),
 ("aq_proof", 2): ("A proof for each", "Imam al-Sanusi gives a proof for each attribute he mentions, so that the believer holds each one with understanding and not only by copying others (taqlid)."),
 ("belief4", "+3"): ("Twenty in all", "Umm al-Barahin lists twenty necessary attributes. Existence (wujud). Five that negate what does not befit Him (salbiyyah): no beginning, no end, unlike creation, needing nothing, and Oneness. Seven attributes of meaning (ma'ani): power, will, knowledge, life, hearing, sight and speech. And seven that follow from those: that He is Powerful, Willing, Knowing, Living, Hearing, Seeing and Speaking."),
 ("belief4", "+4"): ("The Maturidi view", "The Maturidis, the school of Imam Abu Mansur al-Maturidi رحمه الله followed by most Hanafis, add an eighth attribute of meaning: takwin, Allah's bringing things into being. The Ash'aris count this under power and will. Both schools are Ahl al-Sunnah.", "al-'Aqa'id al-Nasafiyyah, the attributes"),
 ("aq_ruya", 1): ("As Allah meant it", "Imam al-Tahawi رحمه الله says the meaning of seeing Allah is as Allah intended and knows. The sound hadith say the believers will see their Lord as clearly as the full moon. We accept these as the Prophet ﷺ said them, without picturing how and without comparing Allah to creation."),
 ("aq_signs", 0): ("The signs", "The Hour is the Day of Judgement. Before it comes there are signs. Among the great signs Imam al-Tahawi mentions: the coming of the Dajjal (the great deceiver), and 'Isa ibn Maryam عليه السلام coming down from the sky."),
 ("aq_signs", 1): ("The last ones", "Two more of the great signs, close to the very end: the sun will rise from the west, where it normally sets, and the Beast of the Earth will come out. After the sun rises from the west, repentance is no longer accepted."),
 ("aq_qadr", 0): ("Known and written", "Qadr (decree) means Allah knew everything before it happened, wrote it, and nothing happens in His kingdom except what He wills, good or bad."),
 # Fiqh
 ("f_istinja", "+0"): ("Words to know", "Istinja' means cleaning the private parts after using the toilet, with water or with something like stones or tissue. Istibra' means making sure the urine has completely stopped before cleaning. Najasah means impurity, such as urine or faeces."),
 ("f_istinja", 0): ("Make sure it has stopped", "A man must make sure the last drops of urine have stopped before he cleans himself and makes wudu, in whatever way works for him, such as walking a little, coughing or waiting. If drops come out after wudu, the wudu breaks."),
 ("f_istinja", "+1"): ("For women", "A woman does not need the man's istibra'. She waits a moment until the flow has stopped, then cleans herself. She should wipe and wash from front to back, so that impurity is not carried forward."),
 ("f_istinja", 1): ("Water or stones", "Istinja' is a sunnah. Wiping with clean stones (or tissue) is allowed, washing with water is better, and the best is to wipe first and then wash. If impurity spreads beyond the opening more than the size of a dirham (about the hollow of the palm), washing it becomes fard."),
 ("purity1", 0): ("Seven waters", "You may make wudu and ghusl with seven kinds of water: rain water, sea water, river water, well water, melted snow, melted hail and spring water. In short: any natural water that is still plain water."),
 ("purity3", 2): ("The rest", "Wash each part three times, except the head: it is wiped once, all of it, and the ears with it. Run water between the fingers and toes, start with the right, follow the order Allah mentions, and keep going without long breaks."),
 ("purity5", 0): ("When it is fard", "Ghusl is washing the whole body. It becomes fard after the release of semen with desire, after intercourse even without release, and when menstruation (hayd) or post-natal bleeding (nifas) ends."),
 ("f_najasa", "+0"): ("What is a dirham?", "A dirham was a silver coin. In this chapter it is a measure. For liquid impurity it is an area: the hollow of your palm when you cup it, roughly 3 cm across, about the size of a 2p coin. For solid impurity it is a weight of 20 qirats (a mithqal), a few grams."),
 ("purity6", 0): ("When it is allowed", "Tayammum is purifying with clean earth when water cannot be used. It is allowed when you are a mile or more from water (a Hanafi mile is about 1.8 km), when using water would make you ill or worse, when it is dangerously cold, or when you need the water to drink."),
 ("fiqh_khuff", "+0"): ("What are khuffs?", "Khuffs are leather socks that cover the ankles. If you put them on while in wudu, then later make wudu again, you may wipe over them with wet hands instead of washing your feet, for a set time."),
 ("fiqh_hayd", 0): ("How long", "Hayd is menstruation, the monthly period. Nifas is the bleeding after giving birth. The shortest hayd is three days and the longest ten. Nifas is at most forty days, with no minimum: it can end after a day."),
 ("f_adhan", "+2"): ("What the adhan means", "Allahu akbar: Allah is the Greatest. Ashhadu an la ilaha illa Allah: I bear witness there is no god but Allah. Ashhadu anna Muhammadan rasulullah: I bear witness Muhammad is the Messenger of Allah. Hayya 'ala al-salah: come to prayer. Hayya 'ala al-falah: come to success. La ilaha illa Allah: there is no god but Allah."),
 ("f_adhan", 2): ("Additions", "In the adhan of Fajr add 'al-salatu khayrun min al-nawm' (prayer is better than sleep) twice after 'hayya 'ala al-falah'. In the iqamah add 'qad qamat al-salah' (the prayer has begun) twice. Give the adhan slowly and the iqamah quickly."),
 ("f_times", 0): ("Fajr and Zuhr", "Fajr is from true dawn (when light spreads across the horizon) until just before sunrise. Zuhr is from when the sun passes its highest point until an object's shadow is twice its length (once, in the view of the two companions), not counting its midday shadow."),
}

CARDS.update({
 ("prayer1", 1): ("Covering", "The 'awrah is the part of the body that must be covered. In prayer, for a man it is from the navel to below the knees. For a woman it is the whole body except the face, the hands and the feet."),
 ("f_qada", 1): ("In order", "Someone who owes fewer than six prayers must make them up in order, before the current prayer. The order falls away if the time is too short, if he forgot he owed them, or once six or more prayers are owed."),
 ("f_travel", 0): ("Shortening", "Someone who sets out intending a journey of three days (about 77 km by the usual modern estimate) shortens the four-rak'ah fard prayers (Zuhr, 'Asr and 'Isha') to two, once he has passed the buildings of his town."),
 ("zakat1", 1): ("The nisab", "The nisab is the minimum wealth on which zakat is due: 200 dirhams of silver (about 612 g) or 20 mithqals of gold (about 87.5 g), or the same value in money or trade goods."),
 ("f_fitr", 1): ("How much", "Half a sa' of wheat (about 1.6 kg), or a full sa' of dates, raisins or barley, or the value of it in money. A sa' is a measure of volume used in the time of the Prophet ﷺ."),
 ("f_sahw", "+0"): ("What it is", "Sajdat al-sahw, the prostration of forgetfulness, is two extra prostrations at the end of the prayer that repair a mistake, such as forgetting the first sitting."),
})

APPEND = {
 "belief2": [("Why must Allah have no beginning?", "If He had a beginning, He would need a maker, like everything that begins", ["Because the Qur'an is old", "Because time began with Him", "There is no reason"], "Anything that begins needs a cause. Allah needs nothing, so He has no beginning.", UB)],
 "aq_speech": [("Someone hears the Qur'an recited and says 'this is just human speech'. What does al-Tahawi say?", "He has disbelieved", ["He is right", "It is a small mistake", "He is excused if he is new"], "Al-Tahawi says whoever hears it and claims it is human speech has disbelieved. Allah threatened such a person with Saqar.", TH)],
 "aq_jaiz": [("Allah punishes someone for their sins. Is that unjust?", "No, it is pure justice", ["Yes, if they were sorry", "Only if they were young", "No one can say"], "If He rewards it is bounty; if He punishes it is justice. Nothing He does is wrong.", "Jawharat al-Tawhid")],
 "belief5": [("Which is impossible for a Messenger of Allah?", "Lying, even once", ["Falling ill", "Getting married", "Being hungry"], "The opposites of truthfulness, trustworthiness and conveying are impossible for them.", UB)],
 "aq_kutub": [("Which Prophet did Allah take as His close friend (khalil)?", "Ibrahim عليه السلام", ["Musa عليه السلام", "Yusuf عليه السلام", "Nuh عليه السلام"], "'And Allah took Ibrahim as a close friend.' (al-Nisa' 125), quoted by al-Tahawi.", TH)],
 "aq_shahada": [("Why should we know the meaning of 'la ilaha illa Allah', not only say it?", "Because every belief about Allah follows from its meaning", ["Because the words alone are magic", "Only scholars need the meaning", "It has no meaning"], "Al-Sanusi shows that all the attributes are contained in it, so knowing it strengthens faith.", UB)],
 "belief6": [("Who are the Companions (Sahabah)?", "Muslims who met the Prophet ﷺ and died as Muslims", ["Any Muslim of the first century", "Only the ten promised Paradise", "Only his family"], "We love them all and speak of them only with good.", TH)],
 "aq_sins": [("A believer commits a major sin. Can repentance (tawbah) wipe it out?", "Yes, Allah accepts sincere repentance", ["No, never", "Only minor sins", "Only on Laylat al-Qadr"], "Allah forgives all sins for the one who repents sincerely, before death or the sun rising from the west.", TH)],
 "aq_ruya": [("Imam al-Tahawi says nobody's religion is safe except…", "The one who submits to Allah and His Messenger ﷺ", ["The one who argues best", "The one who travels most", "The one who reads philosophy"], "Submitting, and leaving what is unclear to the One who knows it, keeps religion safe.", TH)],
 "aq_qadr": [("Something bad happens to you. What does belief in qadr (decree) teach?", "It was decreed by Allah; be patient and trust Him", ["It happened by pure chance", "Allah did not know about it", "Someone's evil eye controls it alone"], "Good and bad are by Allah's decree. The believer is grateful in ease and patient in hardship.", TH)],
 "aq_signs": [("What is the Dajjal?", "A great deceiver who will appear before the end", ["An angel", "A Prophet", "A city"], "The Dajjal is one of the great signs. The Prophet ﷺ taught us to seek refuge from his trial in every prayer.", TH)],
 "aq_awliya": [("Who are the awliya' (friends) of Allah, according to al-Tahawi?", "All the believers, and the most obedient are most honoured", ["Only people with miracles", "Only descendants of the Prophet ﷺ", "Only scholars"], "All believers are friends of the Most Merciful, in different ranks.", TH)],
 "aq_jamaa": [("A Muslim dies. Do we pray the funeral prayer over him, even if he sinned?", "Yes, we pray over every Muslim of the qiblah", ["No, only the righteous", "Only if a scholar agrees", "Only relatives pray"], "Al-Tahawi: we pray over those of them who die, righteous or sinful.", TH)],
}

# ---------------------------------------------------------------- questions: lesson -> [(q, a, [w,w,w], why, src)]
CHECKS = {
 "belief1": [
  ("Knowing what is necessary, impossible and possible for Allah is a duty on whom?", "Every sane Muslim who has reached adulthood", ["Only scholars", "Only those who study Arabic", "Only people who were not born Muslim"], "Umm al-Barahin makes it a duty on every sane adult Muslim, not only on scholars, because belief must rest on knowledge.", UB),
  ("In aqeedah, something the mind cannot picture not existing is called…", "Necessary (wajib)", ["Possible (ja'iz)", "Impossible (mustahil)", "Hidden"], "Necessary means the mind cannot picture it absent. Allah's existence is the clearest example.", UB),
  ("In aqeedah, something that may exist or may not, like rain tomorrow, is called…", "Possible (ja'iz)", ["Necessary (wajib)", "Impossible (mustahil)", "Eternal"], "Everything in creation is possible: it can be or not be, and only exists because Allah brings it into being.", UB),
  ("Allah having a partner is, for the mind…", "Impossible (mustahil)", ["Possible", "Necessary", "Unknown"], "The mind cannot picture two gods each in full control, so a partner for Allah is impossible.", UB),
 ],
 "aq_proof": [
  ("Imam al-Sanusi proves the world had a beginning. What does he point to?", "Everything in it keeps changing", ["It is very old", "It is beautiful", "It is full of people"], "Things move then stop, grow then fade. Each new state began, and something never free of beginnings must itself have begun.", UB),
  ("Once we know the world had a beginning, why does it need a Maker?", "Something that began cannot bring itself into being", ["Because it is very large", "Because people say so", "Because it will last forever"], "A house does not build itself. What came into being needs someone to bring it into being: Allah.", UB),
  ("Could the Maker of the world also have had a beginning?", "No, otherwise He too would need a maker, without end", ["Yes, just before the world", "Yes, at the same time as the world", "No one can know"], "If the Maker began, He would need a maker, and that one another, forever. So the Maker has no beginning.", UB),
  ("Why does al-Sanusi give a proof for each attribute of Allah?", "So the believer holds belief with understanding, not only by copying", ["To make the book longer", "Because proofs replace faith", "Only for debating others"], "He wants each Muslim to know why, so their belief is firm against doubt.", UB),
 ],
 "belief2": [
  ("Allah has no beginning (qidam). What does that mean?", "He never came into being; He always was", ["He was created before everything else", "He began when the universe began", "No one knows"], "Qidam means Allah never came into being. Everything else existed after not existing; He did not.", UB),
  ("Allah has no end (baqa'). What does that mean?", "He will never cease to exist", ["He will end after the Last Day", "He ends when the world ends", "He changes into something else"], "Baqa' means He never ceases. Al-Tahawi: Eternal without a beginning, Everlasting without an end.", TH),
  ("Does Allah's existence depend on anything, the way ours depends on Him?", "No, it depends on nothing", ["Yes, on the heavens", "Yes, on His creation", "Yes, on time"], "Allah's existence has no cause. Everything else depends on Him.", UB),
 ],
 "belief3": [
  ("Which of these is true about Allah?", "He does not resemble anything He created", ["He has a body unlike ours", "He is in one particular place", "He is bound by time like us"], "Allah is not a body, not in a place and not bound by time. 'There is nothing like Him.' (al-Shura 11)", UB),
  ("Allah 'stands by Himself' (qiyam bi-nafsihi). What does that mean?", "He needs nothing, while everything needs Him", ["He needs His Throne to exist", "He stands in one place", "He needs worship to exist"], "He needs no place and no one to bring Him into being, while all things need Him.", UB),
  ("Allah is One (wahdaniyyah). His Oneness covers…", "His Self, His attributes and His actions", ["Only His Self", "Only His actions", "Only His names"], "No one shares His Self, no one has attributes like His, and no one else truly creates.", UB),
  ("Which verse sums up that Allah is unlike creation?", "'There is nothing like Him, and He is the All-Hearing, the All-Seeing'", ["'Read in the name of your Lord'", "'Allah is the light of the heavens and the earth'", "'Say: I seek refuge in the Lord of daybreak'"], "Al-Shura 11 denies any likeness, and still affirms hearing and sight, without likeness.", UB),
 ],
 "belief4": [
  ("Allah has the attribute of will (iradah). So in creation…", "Nothing happens except what He wills", ["People's choices happen without Him", "Nature decides on its own", "Angels decide what happens"], "Nothing happens in His kingdom except what He wills, good or bad.", UB),
  ("Allah hears and sees. How?", "Without ears or eyes, unlike creation", ["With ears and eyes like ours", "Only through the angels", "He does not hear or see"], "His attributes are real but unlike ours. He hears every sound and sees everything without organs.", UB),
  ("Allah's attribute of speech (kalam) is…", "Eternal, and not made of letters or sounds", ["Created like ours", "Only the Arabic language", "Something that began with the Qur'an"], "His speech has no beginning. The Qur'an is His speech.", UB),
  ("How many necessary attributes does Umm al-Barahin list?", "Twenty", ["Seven", "Ninety-nine", "Thirteen"], "One of existence, five negating, seven of meaning and seven that follow from them: twenty.", UB),
  ("What extra attribute do the Maturidis count, that the Ash'aris place under power and will?", "Takwin: bringing things into being", ["Hearing", "Mercy", "Beauty"], "Both views are Ahl al-Sunnah. It is a difference of how to count, not of belief in Allah's perfection.", "al-'Aqa'id al-Nasafiyyah"),
 ],
 "aq_speech": [
  ("What is the Qur'an, according to Imam al-Tahawi?", "The speech of Allah, not created", ["The words of the Prophet ﷺ", "A book written by the Companions", "Created speech like ours"], "Al-Tahawi: it came from Allah and is not created like the speech of creation.", TH),
  ("Imam Abu Hanifah says some things about the Qur'an are created. Which?", "Our reciting and writing of it", ["The Qur'an itself", "Allah's speech", "Allah's knowledge"], "Our voices, ink and paper are created. The Qur'an itself, Allah's speech, is not.", "al-Fiqh al-Akbar"),
  ("Where is the Qur'an, according to Imam Abu Hanifah in al-Fiqh al-Akbar?", "Written in copies, kept in hearts, recited by tongues", ["Only in the copies", "Only in the hearts", "Only in the Preserved Tablet"], "He described it in all three ways, while it remains Allah's uncreated speech.", "al-Fiqh al-Akbar"),
 ],
 "aq_jaiz": [
  ("Which of these is impossible for Allah?", "Needing anything", ["Creating whatever He wills", "Forgiving whom He wills", "Giving provision"], "Needing is the opposite of 'standing by Himself', so it is impossible for Him.", UB),
  ("What is possible (ja'iz) for Allah, according to al-Sanusi?", "Doing or leaving anything that is possible", ["Only what His creation asks", "Only what is best for creation", "Nothing at all"], "He may create or not create, give or withhold. Nothing forces Him.", UB),
  ("Is Allah obliged to reward people for good deeds?", "No, His reward is pure bounty", ["Yes, always", "Yes, if they pray", "Only the Prophets"], "Nothing is obligatory upon Allah. He promised reward out of generosity, and He keeps His promise.", "Jawharat al-Tawhid"),
 ],
 "belief5": [
  ("Which three qualities are necessary for every Messenger of Allah?", "Truthfulness, trustworthiness and conveying the message", ["Wealth, power and fame", "Never falling ill", "Knowing the unseen by themselves"], "Sidq (truthfulness), amanah (trustworthiness) and tabligh (conveying) are necessary for them.", UB),
  ("Which of these human things is possible for a Messenger?", "Eating, sleeping and marrying", ["Hiding part of the message", "Telling a lie", "Betraying a trust"], "Human things that do not lower their rank are possible for them.", UB),
  ("Who is the last Prophet, after whom there is no prophet?", "Muhammad ﷺ", ["'Isa عليه السلام", "Ibrahim عليه السلام", "There will be another"], "He ﷺ is the Seal of the Prophets. 'Isa عليه السلام will return, but as a follower of his law.", TH),
 ],
 "aq_kutub": [
  ("How do Muslims believe in the Messengers of Allah?", "In all of them, without rejecting any", ["Only in the last one", "Only in those named in the Qur'an", "In most of them"], "Al-Tahawi: we make no distinction between His Messengers in believing them.", TH),
  ("To which Prophet did Allah speak directly, without an angel?", "Musa عليه السلام", ["Ibrahim عليه السلام", "'Isa عليه السلام", "Nuh عليه السلام"], "'And Allah spoke to Musa directly.' (al-Nisa' 164), quoted by al-Tahawi.", TH),
  ("Who are the 'noble scribes' (kiraman katibin)?", "The angels who record our deeds", ["The Companions who wrote the Qur'an", "The scholars", "The Prophets"], "Allah has made them guardians over us, writing what we do.", TH),
 ],
 "aq_shahada": [
  ("Al-Sanusi explains 'la ilaha illa Allah' (no god but Allah). What does it mean?", "None is free of need of all else, and needed by all, except Allah", ["Allah is the greatest of many gods", "There are many gods but Allah is best", "Allah is in every place"], "Every attribute of Allah follows from this: He needs nothing, and everything needs Him.", UB),
  ("Belief in the angels and the Last Day is contained in which half of the Shahadah?", "'Muhammadun Rasulullah' (Muhammad is the Messenger of Allah)", ["The opening takbir", "The adhan alone", "Neither half"], "Accepting the Messenger ﷺ means accepting everything he brought, including the angels, the books and the Last Day.", UB),
  ("How does al-Sanusi advise us to say the Shahadah?", "Often, knowing what it means", ["Once in your life", "Only in prayer", "Leave it to scholars"], "He closes the book urging the believer to say it often with awareness of its meaning.", UB),
 ],
 "belief6": [
  ("How does Imam al-Tahawi define faith (iman)?", "Affirming with the tongue and believing with the heart", ["Only doing good deeds", "Only believing, never saying it", "Only saying it with the tongue"], "Faith is believing in the heart and declaring with the tongue all the Prophet ﷺ brought.", TH),
  ("Which of these is one of the six articles of faith?", "Belief in Allah's decree, the good and the bad", ["Belief in lucky days", "Belief that the stars decide events", "Belief that some saints are prophets"], "The six: Allah, His angels, books, Messengers, the Last Day, and the decree.", TH),
  ("How do we speak about the Companions of the Prophet ﷺ?", "Only with good, without going to excess about any", ["Praise some and disown others", "Not mention them", "Judge their disputes"], "We love them all, go to excess with none, disown none, and mention them only with good.", TH),
 ],
 "aq_sins": [
  ("A Muslim commits a sin. Does that make him a disbeliever?", "No, unless he claims the sin is lawful", ["Yes, always", "Only for major sins", "Only if he repeats it"], "Al-Tahawi: we do not call anyone of the qiblah a disbeliever for a sin, unless he holds it lawful.", TH),
  ("A believer dies with major sins he did not repent from. What is his state?", "He is under Allah's will, and will not stay in the Fire forever", ["He is in the Fire forever", "He is certainly forgiven", "He was never a believer"], "If Allah wills He forgives him; if He wills He punishes him, then admits him to Paradise.", TH),
  ("Between feeling safe from Allah's punishment and despairing of His mercy, where is the right path?", "Between hope and fear", ["Feeling completely safe", "Despairing of mercy", "Ignoring the hereafter"], "Both extremes take a person away from Islam. The believer hopes and fears.", TH),
 ],
 "aq_akhira": [
  ("Which two angels question a person in the grave?", "Munkar and Nakir", ["Jibril and Mika'il", "The recording angels", "No one"], "They ask about one's Lord, religion and Prophet. The grave is a garden of Paradise or a pit of the Fire.", TH),
  ("What does Imam al-Tahawi say about Paradise and the Fire?", "They already exist and will never end", ["They will be created on the Last Day", "They end after a long time", "Only Paradise lasts forever"], "They are created now, and they never end or perish.", TH),
  ("What is the Pool (hawd) of the Prophet ﷺ on the Day of Judgement?", "A real pool from which he gives his Ummah to drink", ["A symbol only", "For the Prophets alone", "A pool in this world"], "It is an honour Allah gave him ﷺ, to quench the thirst of his Ummah.", TH),
  ("On the Day of Judgement, what is the Sirat?", "The Bridge over the Fire that people cross", ["A book of deeds", "The gate of Paradise", "A river in Paradise"], "Al-Tahawi lists the Bridge with the Scales, the reckoning and the books of deeds.", TH),
 ],
 "aq_ruya": [
  ("Will the believers see Allah in Paradise?", "Yes, without picturing how", ["No, never", "Yes, in this world too", "Only the Prophets"], "Al-Tahawi: the seeing is true for the people of Paradise, without encompassing Him and without 'how'.", TH),
  ("Which verse does Imam al-Tahawi quote as proof that believers will see Allah?", "'Faces that Day will be radiant, looking at their Lord'", ["Ayat al-Kursi", "'Say: He is Allah, One'", "'There is nothing like Him'"], "Al-Qiyamah 22–23 speaks of faces on the Day of Judgement looking at their Lord.", TH),
  ("How do we understand the hadith that say believers will see Allah?", "As the Prophet ﷺ said them, meant as Allah intends", ["By our own opinions", "We reject them", "By comparing Allah to creation"], "We accept them, without imagining how and without likening Allah to anything.", TH),
 ],
 "aq_qadr": [
  ("Can anything happen in creation that Allah did not will?", "No, only what He wills happens", ["Yes, whatever people want", "Some things against His will", "Only good things are His will"], "Al-Tahawi: nothing happens in His kingdom except what He wills.", TH),
  ("What does Imam al-Tahawi say about digging deep into the secret of qadr (decree)?", "It is Allah's secret; delving into it leads to ruin", ["Everyone must study it in detail", "It is easy to understand", "Only Prophets may ask about it"], "No angel or Prophet has been shown it. We believe in it and act.", TH),
  ("If Allah has decreed everything, how are we responsible for our actions?", "Allah creates our actions and we earn (kasb) them by choosing", ["We create them alone", "We are forced with no choice", "Allah does not know them beforehand"], "We choose and are accountable, while Allah creates. So we act, take responsibility, and trust Him.", TH),
 ],
 "aq_signs": [
  ("Which is one of the great signs before the Day of Judgement that al-Tahawi mentions?", "'Isa عليه السلام coming down from the sky", ["A great flood", "The return of Pharaoh", "The end of all rain"], "He lists the Dajjal, the descent of 'Isa, the sun rising from the west and the Beast of the Earth.", TH),
  ("Near the end of time, from where will the sun rise?", "From the west, where it normally sets", ["From the north", "From two places", "From the east, but red"], "This great sign is close to the very end. After it, repentance is no longer accepted.", TH),
  ("A fortune-teller predicts your future. What does al-Tahawi say?", "We do not believe them", ["Believe them if they come true", "Ask them about the future", "Believe them sometimes"], "Only Allah knows the unseen. We do not believe soothsayers or fortune-tellers.", TH),
 ],
 "aq_awliya": [
  ("A wali is a close friend of Allah. Can a wali be better than a Prophet?", "No, one Prophet is better than all the awliya' together", ["Yes, the greatest ones", "Yes, if he has wonders", "They are equal"], "Al-Tahawi: one Prophet is better than all the awliya' together.", TH),
  ("Karamat are wonders Allah does at the hands of His friends. Are they true?", "Yes, when reported by trustworthy narrators", ["Never possible", "Only stories", "They are signs of prophethood"], "We believe in the karamat of the awliya' as reported by trustworthy narrators.", TH),
  ("Who is most honoured with Allah?", "The most obedient and best follower of the Qur'an", ["The one with most wonders", "The one with most followers", "The one from the best family"], "Al-Tahawi ties honour with Allah to obedience and following the Qur'an.", TH),
 ],
 "aq_jamaa": [
  ("Behind which Muslims may we pray in congregation?", "Any Muslim of the qiblah, righteous or sinful", ["Only the most pious", "Only people of our group", "Only scholars"], "Al-Tahawi: we pray behind every Muslim who faces the qiblah, righteous or sinful.", TH),
  ("May we declare that a particular Muslim is going to the Fire?", "No, we leave what is hidden to Allah", ["Yes, if he sins", "Yes, if we dislike him", "Only after he dies"], "We do not place any of them in Paradise or the Fire. Only Allah knows how a person ends.", TH),
  ("How does al-Tahawi describe splitting away from the main body of Muslims (the Jama'ah)?", "As straying and a punishment", ["As a mercy", "As necessary", "As a sign of knowledge"], "We follow the Sunnah and the Jama'ah, and see division as straying.", TH),
 ],
 # ---- Fiqh
 "f_istinja": [
  ("What is istinja'?", "Cleaning the private parts after using the toilet", ["A du'a before sleeping", "Washing the whole body", "A kind of prayer"], "Istinja' is cleaning yourself after the toilet, with water, stones or tissue.", NI),
  ("For istinja', which way of cleaning is best?", "Wiping first, then washing with water", ["Stones only", "Water only, always", "Tissue only"], "Water is better than stones, and joining both is best.", NI),
  ("Before a man cleans himself and makes wudu, what must he make sure of?", "That the last drops of urine have stopped", ["That he has said the adhan", "That he has changed clothes", "Nothing"], "This is istibra'. Drops coming out after wudu break it.", NI),
  ("How does a woman clean herself after the toilet?", "Waits a moment, then cleans from front to back", ["Walks around first like a man", "Must always use stones only", "Does not need to clean"], "She does not need the man's istibra'. Front to back stops impurity being carried forward.", "Maraqi al-Falah"),
  ("With which foot do you enter the toilet?", "The left, leaving with the right", ["The right", "Either", "Both together"], "Enter with the left foot, seeking refuge in Allah, and leave with the right.", NI),
 ],
 "purity1": [
  ("Which of these may be used for wudu?", "Rain water", ["Rose water", "Fruit juice", "Water already used for ghusl"], "Rain water is one of the seven natural waters.", NI),
  ("Water that was already used for someone's wudu or ghusl: can it be used for wudu again?", "No: it is pure, but it does not purify", ["Yes, it purifies again", "Only for the feet", "Only if warm"], "Used water is clean, but cannot lift impurity a second time.", NI),
  ("Nur al-Idah lists seven waters you may use. Which list is right?", "Rain, sea, river, well, melted snow, melted hail and spring", ["Rain, juice, milk, sea, river, well, spring", "Only rain and river", "Zamzam only"], "Any natural water that is still plain water may be used.", NI),
 ],
 "purity3": [
  ("In the Hanafi school, rinsing the mouth during wudu is…", "A sunnah", ["One of the four obligations", "Disliked", "Only for ghusl"], "In wudu it is sunnah. In ghusl it is fard.", NI),
  ("By the sunnah, how many times is each part washed in wudu?", "Three times, except the head, which is wiped once", ["Once only", "Three times, including the head", "Seven times"], "Once is enough for validity; three is sunnah. The head is wiped once, all of it, with the ears.", NI),
  ("Which of these is a sunnah of wudu?", "Starting with the right side", ["Starting with the feet", "Talking during wudu", "Washing each part four times"], "Starting with the right is sunnah, as is following the order and not pausing long.", NI),
 ],
 "purity5": [
  ("What is ghusl?", "Washing the whole body", ["Washing the hands only", "Wiping the head", "A du'a after prayer"], "Ghusl is the full bath, needed after janabah, hayd and nifas.", NI),
  ("In the Hanafi school, rinsing the mouth during ghusl is…", "Fard", ["Sunnah only", "Disliked", "Not needed"], "In ghusl, rinsing the whole mouth and washing inside the nose are fard.", NI),
  ("Which of these makes ghusl fard?", "The end of menstruation (hayd)", ["Touching a dog", "Eating camel meat", "Sleeping"], "Ghusl is fard when hayd or nifas ends, after intercourse, and after release of semen with desire.", NI),
  ("For ghusl, must a woman undo her plaited hair?", "No, if water reaches the roots", ["Yes, always", "Only in winter", "Only after menstruation"], "Water reaching the roots is enough.", NI),
 ],
 "f_najasa": [
  ("In this chapter a dirham is a measure. How big is it for liquid impurity?", "The hollow of the palm, about 3 cm across", ["The whole hand", "A single drop", "A metre square"], "For liquid impurity it is an area: the cupped palm, roughly a 2p coin. For solid impurity it is a weight.", NI),
  ("Heavy impurity (like urine or flowing blood) on your clothes: how much is excused in prayer?", "Up to the size of a dirham", ["None at all", "A quarter of the garment", "Any amount if dry"], "Up to a dirham is excused, though washing it is still better.", NI),
  ("Flowing blood is which kind of impurity?", "Heavy (ghalizah)", ["Light (khafifah)", "Pure", "Excused in any amount"], "Flowing blood is listed among the heavy impurities.", NI),
  ("Light impurity (like the urine of animals that are eaten) is excused if it is…", "Less than a quarter of the garment or limb", ["Less than a dirham only", "Never excused", "Any amount"], "Light impurity has a wider allowance: less than a quarter.", NI),
 ],
 "purity6": [
  ("What is tayammum?", "Purifying with clean earth when water can't be used", ["Washing with less water", "Wiping the socks", "Washing only the face"], "Tayammum stands in place of wudu and ghusl when water cannot be used.", NI),
  ("You can't find water. How far away must it be for tayammum to be allowed?", "A mile or more, about 1.8 km", ["Ten metres", "A hundred miles", "Any distance at all"], "A Hanafi mile is 4,000 cubits, about 1.8 km.", NI),
  ("In tayammum, how many times are the hands struck on the earth?", "Twice: once for the face, once for the arms", ["Once only", "Three times", "Seven times"], "Strike, wipe the face; strike again, wipe both arms with the elbows.", NI),
  ("What ends tayammum, besides what breaks wudu?", "Finding water you are able to use", ["The next prayer time", "Sunrise", "Nothing"], "It stands in place of water only until water can be used.", NI),
 ],
 "fiqh_khuff": [
  ("What are khuffs?", "Leather socks covering the ankles, which may be wiped over", ["Cotton socks of any kind", "Shoes worn in the masjid", "A cloth for the head"], "If put on while in wudu, you may wipe over them instead of washing your feet, for a set time.", NI),
  ("How long may a traveller wipe over leather socks (khuffs)?", "Three days and nights", ["One day and night", "Until the journey ends", "One week"], "A resident wipes one day and night; a traveller three.", NI),
  ("When wiping over leather socks (khuffs), when does the time limit start?", "From the first thing that breaks wudu after putting them on", ["When you put them on", "At Fajr", "When you first wipe"], "Put them on in wudu at Fajr, and your wudu breaks at noon: the count starts at noon.", NI),
  ("When wiping over leather socks (khuffs), what is the least you must wipe?", "Three fingers' width on the top of each foot", ["The whole sock", "The sole of the foot", "Any single touch"], "The fard is the size of three of the hand's small fingers on the top front of each foot.", NI),
 ],
 "fiqh_hayd": [
  ("What is nifas?", "The bleeding after giving birth", ["The monthly period", "A kind of ghusl", "Bleeding from a cut"], "Nifas is post-natal bleeding. Hayd is the monthly period.", NI),
  ("In the Hanafi school, what is the longest a period (hayd) can last?", "Ten days", ["Seven days", "Fifteen days", "No limit"], "The shortest hayd is three days and the longest ten. Bleeding beyond that is not hayd.", NI),
  ("What is the longest nifas (bleeding after giving birth) can last?", "Forty days", ["Ten days", "Sixty days", "Two weeks"], "Nifas is at most forty days, with no minimum: it may end after a day.", NI),
  ("After her period, what does a woman make up?", "The fasts, not the prayers", ["The prayers and fasts", "The prayers only", "Nothing"], "She makes up missed fasts. Missed prayers are forgiven, a mercy from Allah.", NI),
 ],
 "prayer1": [
  ("In prayer, the 'awrah (what must be covered) for a man is…", "From the navel to below the knees", ["Only the private parts", "From the chest to the ankles", "The whole body except the face"], "A man's 'awrah is from the navel to below the knees; a woman's is all but the face, hands and feet.", NI),
  ("You pray Zuhr before its time has come in. Is it valid?", "No, the time having come in is a condition", ["Yes, if you meant well", "Yes, it counts as early", "It is only disliked"], "A prayer before its time is not valid; pray it again once the time comes in.", NI),
  ("Which of these is a condition for the prayer to be valid?", "A clean body, clothes and place", ["Praying in a masjid", "Wearing white", "Praying in congregation"], "Purity of body, clothes and place, covering the 'awrah, facing the qiblah, the time and the intention.", NI),
 ],
 "prayer2": [
  ("Which of these is a pillar (fard part) inside the prayer?", "Bowing (ruku')", ["Raising the hands at takbir", "Saying 'amin'", "Placing the right hand over the left"], "The pillars inside the prayer: standing, reciting, ruku' and sujud, and the final sitting.", NI),
  ("You missed a pillar of the prayer, like a sujud. What do you do?", "Pray it again; it is not valid", ["Two prostrations of forgetfulness fix it", "Nothing", "Add one rak'ah"], "A missing pillar cannot be repaired by sajdat al-sahw.", NI),
  ("How long must the final sitting of the prayer be, at least?", "As long as it takes to recite the tashahhud", ["A moment", "As long as the whole prayer", "As long as one rak'ah"], "The final sitting is fard for at least the length of the tashahhud.", NI),
 ],
 "f_sahw": [
  ("What is sajdat al-sahw?", "Two prostrations at the end of prayer that repair a mistake", ["A prostration when reciting certain verses", "A prayer at night", "Prostrating in thanks"], "It repairs a wajib act left out by mistake.", NI),
  ("By the sunnah, when is the prostration of forgetfulness (sajdat al-sahw) made?", "After one salam to the right", ["Before the first takbir", "After both salams and leaving", "In the middle of the prayer"], "Give one salam to the right, two sujud, then tashahhud and salam.", NI),
  ("What makes the prostration of forgetfulness (sajdat al-sahw) wajib?", "Leaving a wajib act by mistake", ["Leaving a pillar", "Leaving a sunnah", "Praying late"], "It repairs a forgotten wajib. A missed pillar needs the prayer repeated.", NI),
  ("You left a wajib act of prayer on purpose. What follows?", "You are sinful and repeat the prayer", ["Sajdat al-sahw fixes it", "Nothing", "Pray two extra rak'ahs"], "The prostration is for mistakes, not deliberate omissions.", NI),
 ],
 "f_travel": [
  ("Which prayers does a traveller shorten?", "The four-rak'ah fard prayers: Zuhr, 'Asr and 'Isha'", ["All prayers", "Fajr and Maghrib", "Only Jumu'ah"], "They become two rak'ahs. Fajr and Maghrib stay as they are.", NI),
  ("How far must a journey be for prayers to be shortened?", "Three days' journey, about 77 km", ["Any distance outside your house", "10 km", "Only flights abroad"], "Al-Quduri: three days' travel at a normal pace, commonly estimated today at about 77 km.", QD),
  ("A traveller arrives in a town. How long must he intend to stay to stop shortening?", "Fifteen days or more", ["Three days", "Four days", "One month"], "Intending fifteen days or more in one town ends the travel ruling.", NI),
  ("In the Hanafi school, is shortening the prayer while travelling optional?", "No, it is required", ["Yes, optional", "It is disliked", "Only by camel"], "Shortening is 'azimah (the rule), not just a permission.", NI),
 ],
 "f_qada": [
  ("You missed 'Asr while travelling and make it up at home. How many rak'ahs?", "Two", ["Four", "Three", "None"], "A prayer is made up as it was missed: two for a traveller.", NI),
  ("You owe two missed prayers. Must you make them up in order, before the current prayer?", "Yes, while you owe fewer than six", ["No, never", "Only Fajr", "Only in Ramadan"], "Order is required for one who owes fewer than six, unless time is short or he forgot.", NI),
  ("What happens to a prayer that was missed?", "It stays owed and must be made up", ["It is forgiven automatically", "Charity replaces it", "Only du'a is needed"], "Make it up, and repent if it was missed deliberately.", NI),
 ],
 "zakat1": [
  ("When does zakat become due on your wealth?", "When a full lunar year has passed while you own the nisab", ["As soon as you earn it", "Only in Ramadan", "Every month"], "The nisab is the minimum amount. Zakat is due after a lunar year with it.", NI),
  ("The nisab is the minimum wealth for zakat. What is the nisab of gold?", "20 mithqals, about 87.5 g", ["200 mithqals", "5 mithqals", "20 grams"], "Gold: 20 mithqals (about 87.5 g). Silver: 200 dirhams (about 612 g).", QD),
  ("A person has the nisab but also owes debts. What happens?", "Debts are taken off first; zakat is due if the rest reaches the nisab", ["Debts are ignored", "Zakat is doubled", "Zakat is never due"], "Subtract what you owe; if what remains still reaches the nisab, zakat is due.", QD),
 ],
 "f_adhan": [
  ("What does 'hayya 'ala al-falah' in the adhan mean?", "Come to success", ["Come to prayer", "Allah is the Greatest", "Prayer has begun"], "'Hayya 'ala al-salah' is 'come to prayer'; 'hayya 'ala al-falah' is 'come to success'.", NI),
  ("What is the ruling of the adhan for a fard prayer?", "A stressed sunnah", ["Fard", "Wajib", "Only for Jumu'ah"], "A stressed sunnah for every fard prayer, for men.", NI),
  ("In the adhan of Fajr, what is added, and what does it mean?", "'Al-salatu khayrun min al-nawm': prayer is better than sleep", ["'Qad qamat al-salah': prayer has begun", "An extra 'Allahu akbar'", "Nothing"], "It is said twice after 'hayya 'ala al-falah', reminding the sleeper.", NI),
  ("What is added in the iqamah, and what does it mean?", "'Qad qamat al-salah': the prayer has begun", ["'Al-salatu khayrun min al-nawm'", "A second shahadah", "Nothing"], "The iqamah is said just before the prayer starts, and said quickly.", NI),
 ],
}

# ---------------------------------------------------------------- whole new lessons
NEW_LESSONS = {
 "aqeedah": [
  ("belief4", {"id": "aq_twenty", "title": "The twenty attributes", "about": "The full list from Umm al-Barahin, and what each group means.",
   "cards": [
    ("Existence", "The first attribute is existence (wujud): Allah truly exists. Al-Sanusi calls it the attribute of the Self (nafsiyyah).", UB + ", the necessary attributes"),
    ("Five that negate", "Five attributes deny what does not befit Allah (salbiyyah): no beginning (qidam), no end (baqa'), unlike creation (mukhalafah), needing nothing (qiyam bi-nafsihi) and Oneness (wahdaniyyah).", UB + ", the necessary attributes"),
    ("Seven of meaning", "Seven real attributes (ma'ani): power, will, knowledge, life, hearing, sight and speech.", UB + ", the necessary attributes"),
    ("Seven that follow", "Seven more follow from those (ma'nawiyyah): that He is Powerful, Willing, Knowing, Living, Hearing, Seeing and Speaking.", UB + ", the necessary attributes"),
   ],
   "checks": [
    ("Which attribute does al-Sanusi call the attribute of the Self (nafsiyyah)?", "Existence (wujud)", ["Knowledge", "Power", "Speech"], "Existence is first: all the other attributes are of the One who exists.", UB),
    ("Which group are 'no beginning, no end, unlike creation, needing nothing, Oneness'?", "The five that negate (salbiyyah)", ["The seven of meaning", "The seven that follow", "The names of the Prophet ﷺ"], "Each one denies something that does not befit Allah.", UB),
    ("Which is one of the seven attributes of meaning (ma'ani)?", "Knowledge ('ilm)", ["Having no end", "Being unlike creation", "Oneness"], "The seven of meaning: power, will, knowledge, life, hearing, sight and speech.", UB),
    ("'Allah is Knowing' follows from which attribute?", "His attribute of knowledge", ["His existence alone", "His Oneness", "His having no end"], "Each of the seven that follow comes from one of the seven of meaning.", UB),
    ("How many attributes in total are necessary for Allah, in Umm al-Barahin?", "Twenty", ["Seven", "Thirteen", "Ninety-nine"], "1 + 5 + 7 + 7 = 20. His perfection is without limit; these are what every Muslim must know in detail.", UB),
   ]}),
 ],
}

def polish(courses):
    by_id = {l["id"]: l for c in courses for l in c["lessons"]}
    for cid, items in NEW_LESSONS.items():
        c = next(c for c in courses if c["id"] == cid)
        for after, L in items:
            if L["id"] in by_id: continue
            lesson = {"id": L["id"], "title": L["title"], "about": L["about"],
                      "cards": [{"t": t, "x": x, "src": s} for t, x, s in L["cards"]],
                      "checks": [{"q": q, "a": a, "w": w, "why": y, "src": s} for q, a, w, y, s in L["checks"]]}
            i = next((k for k, l in enumerate(c["lessons"]) if l["id"] == after), len(c["lessons"]) - 1)
            c["lessons"].insert(i + 1, lesson); by_id[lesson["id"]] = lesson
    inserts = {}
    for (lid, idx), v in CARDS.items():
        l = by_id[lid]; t, x = v[0], v[1]; src = v[2] if len(v) > 2 else None
        if isinstance(idx, int):
            l["cards"][idx]["t"], l["cards"][idx]["x"] = t, x
            if src: l["cards"][idx]["src"] = src
        else: inserts.setdefault(lid, []).append((idx, t, x, src))
    for lid, ins in inserts.items():     # insert from the back so earlier indexes stay right
        l = by_id[lid]; src0 = l["cards"][0]["src"]
        for idx, t, x, src in sorted(ins, key=lambda z: -(int(z[0][1:]) if z[0] != "+" else 999)):
            pos = len(l["cards"]) if idx == "+" else int(idx[1:])
            l["cards"].insert(pos, {"t": t, "x": x, "src": src or src0})
    for lid, extra in APPEND.items():
        CHECKS.setdefault(lid, [(c["q"], c["a"], c["w"], c["why"], c["src"]) for c in by_id[lid]["checks"]])
        CHECKS[lid] = CHECKS[lid] + extra
    for lid, checks in CHECKS.items():
        l = by_id[lid]
        for q, a, w, y, s in checks: assert len(w) == 3 and a not in w, (lid, q)
        l["checks"] = [{"q": q, "a": a, "w": w, "why": y, "src": s} for q, a, w, y, s in checks]
    return courses
