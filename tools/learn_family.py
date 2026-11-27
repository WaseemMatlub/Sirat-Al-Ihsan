"""Marriage, family and rights: a course of its own in the basics (27 Nov 2026).
Rulings follow Mukhtasar al-Quduri (Books of Marriage, Fosterage, Divorce, Khul', 'Iddah, Maintenance) with
Ihya' 'Ulum al-Din (Book of the Etiquette of Marriage) for the manners, and the hadith collections."""
QD, IH = "Mukhtasar al-Quduri", "Ihya' 'Ulum al-Din, Book of the Etiquette of Marriage"
RM = "Radd al-Muhtar, chapter on maintenance"

LESSONS = [
 ("fm_before", "Before marriage", "Choosing a spouse, seeing them, and keeping the engagement halal.", [
   ("Marriage is a sunnah", "Marriage is a stressed sunnah, and it becomes wajib for someone who fears falling into zina and can afford it. The Prophet ﷺ said: whoever is able to marry, let him marry, for it lowers the gaze and guards chastity.", "Sahih al-Bukhari, Book of Marriage"),
   ("Choose for religion", "The Prophet ﷺ said a woman is married for four things: her wealth, her lineage, her beauty and her religion. 'Choose the one with religion and you will prosper.' The same holds for choosing a husband: look first at his deen and character.", "Sahih al-Bukhari, Book of Marriage"),
   ("Seeing each other", "It is sunnah for a man to see the woman he intends to marry, her face and hands, before proposing: the Prophet ﷺ said it is more likely to bring love between you. Pray istikharah and ask people who know them.", "Sunan al-Tirmidhi, Book of Marriage"),
   ("The engagement is not a marriage", "An engagement (khitbah) is only a promise. Until the nikah they are still strangers to each other: no being alone together, no touching, and no private talk beyond what is needed. 'No man is alone with a woman but Shaytan is the third.'", "Sunan al-Tirmidhi, Book of Fitan"),
   ("Do not cut in", "Do not propose to someone who is already engaged to another until he withdraws or is turned down.", "Sahih al-Bukhari, Book of Marriage"),
  ], [
   ("What did the Prophet ﷺ say to choose a spouse for above all?", "Their religion", ["Their wealth", "Their family name", "Their looks"], "'Choose the one with religion and you will prosper.'", "Sahih al-Bukhari, Book of Marriage"),
   ("May an engaged couple spend time alone together?", "No; they are not married yet", ["Yes, once engaged", "Yes, if the families agree", "Yes, in public places only"], "The engagement is only a promise; seclusion is not allowed until the nikah.", "Sunan al-Tirmidhi, Book of Fitan"),
   ("Before proposing, a man may look at…", "Her face and hands", ["Nothing at all", "Photos she shares privately", "Whatever he wishes"], "Looking at the face and hands with the intention of marriage is sunnah.", "Sunan al-Tirmidhi, Book of Marriage"),
  ]),
 ("f_nikah", "The marriage contract", "What makes a nikah valid, the mahr, consent and the walimah.", [
   ("The contract", "A nikah is made by an offer and an acceptance, in one sitting, spoken in the presence of two adult Muslim witnesses: two men, or one man and two women.", f"{QD}, Book of Marriage"),
   ("Consent and the guardian", "No one may marry an adult woman without her consent. In the Hanafi school her marriage is valid without her guardian, but it is sunnah for him to arrange it, and he may object if the husband is not a suitable match (kafa'ah).", f"{QD}, Book of Marriage"),
   ("The mahr", "The mahr is the wife's own property, owed by the husband, whether or not it was named; if none was named she is owed a mahr like that of women of her family. In the Hanafi school it is at least ten dirhams of silver.", f"{QD}, Book of Marriage"),
   ("Whom one may marry", "A Muslim man may marry a Muslim woman, or a chaste Christian or Jewish woman, though the Hanafi scholars dislike it, more so where it endangers the children's faith. A Muslim woman may only marry a Muslim man.", f"{QD}, Book of Marriage"),
   ("More than one wife", "A man may marry up to four, on condition of justice between them in nights, housing and spending. 'If you fear you will not be just, then one.' (al-Nisa' 3)", f"{QD}, Book of Marriage"),
   ("The walimah", "It is sunnah for the husband to hold a wedding meal (walimah) after the marriage, without waste or showing off, and to invite the poor as well as the rich.", "Sahih al-Bukhari, Book of Marriage"),
  ], [
   ("What makes a nikah valid?", "Offer and acceptance before two witnesses", ["A celebration with guests", "Registry papers only", "The families agreeing alone"], "Al-Quduri: offer and acceptance, with two witnesses.", f"{QD}, Book of Marriage"),
   ("Whose property is the mahr?", "The wife's", ["Her father's", "The husband's family's", "The imam's"], "It is owed to her and belongs to her alone.", f"{QD}, Book of Marriage"),
   ("May a Muslim woman marry a Christian man?", "No", ["Yes, if he is good", "Yes, with her father's permission", "Yes, if the children are Muslim"], "A Muslim woman may only marry a Muslim man.", f"{QD}, Book of Marriage"),
   ("What is the condition for marrying more than one wife?", "Justice between them in nights, housing and spending", ["The first wife's written permission", "Living in different cities", "None at all"], "If he fears injustice, one only.", "Qur'an, al-Nisa' 4:3"),
  ]),
 ("fm_mahram", "Whom you may never marry", "The mahram relatives, by blood, by marriage and by nursing.", [
   ("By blood", "A man may never marry his mother or grandmothers, daughters or granddaughters, sisters, aunts (father's or mother's sisters), or nieces. These are his mahrams: he may be alone with them and travel with them.", "Qur'an, al-Nisa' 4:23"),
   ("By marriage", "Also forbidden for ever: his wife's mother, his wife's daughter once he has consummated the marriage with the mother, his son's wife, and his father's wife. And while married, he may not combine two sisters, or a woman and her aunt.", f"{QD}, Book of Marriage"),
   ("By nursing", "Whatever blood makes forbidden, nursing makes forbidden. In the Hanafi school even a little milk counts, if the child nursed within the first two years (Abu Hanifah said thirty months). So the woman who nursed you is like your mother, and her children like your siblings.", f"{QD}, Book of Fosterage"),
   ("Cousins are not mahram", "Cousins, a brother-in-law or sister-in-law, and the spouse's siblings are not mahrams: they may marry, and the rules of covering and not being alone together apply to them.", f"{QD}, Book of Marriage"),
  ], [
   ("Is a cousin a mahram?", "No; cousins may marry and must keep the rules of covering", ["Yes, like a sister", "Only a father's brother's child", "Only if raised together"], "Cousins are not among the forbidden relatives.", "Qur'an, al-Nisa' 4:23"),
   ("A woman nursed a baby boy within his first two years. Her daughter is to him…", "Like his sister: he may never marry her", ["A cousin", "Unrelated", "His niece"], "Nursing forbids what blood forbids.", f"{QD}, Book of Fosterage"),
   ("May a man be married to two sisters at the same time?", "No", ["Yes, with justice", "Only if one is older", "Yes, if they agree"], "Combining two sisters is forbidden.", "Qur'an, al-Nisa' 4:23"),
  ]),
 ("fm_wife", "The rights of the wife", "What a husband owes his wife, before Allah and before the court.", [
   ("Kindness first", "'Live with them in kindness.' The Prophet ﷺ said: the most complete of the believers in faith are those best in character, and the best of you are the best to their wives.", "Sunan al-Tirmidhi, Book of Suckling"),
   ("Her mahr and her wealth", "Her mahr is hers, and so is everything she owns or earns. The husband has no right to her money, and she is not required to spend on the household.", f"{QD}, Book of Marriage"),
   ("Maintenance (nafaqah)", "He must provide her food, clothing and housing according to his means, even if she is wealthy. A man's spending on his family, seeking Allah's reward, is charity.", f"{QD}, Book of Maintenance"),
   ("A home of her own", "In the Hanafi school she has the right to her own quarters, with a door she can lock and a place to cook, where none of his relatives live with her unless she agrees. Living with his parents is a kindness she may choose, not a duty.", f"{QD}, Book of Maintenance"),
   ("Time, affection and teaching", "He gives her his company and affection, does not stay away from her bed for long, keeps her secrets, and teaches her the religion or lets her learn it. With more than one wife, he is just between them.", IH),
   ("Housework", "The Hanafi jurists say a court cannot force her to cook or clean, as it is not part of the contract. But serving the home is from good companionship, and the women of the Companions, Fatimah رَضِيَ اللَّهُ عَنْهَا among them, did so.", RM),
  ], [
   ("Whose is the money a wife earns?", "Hers alone", ["Her husband's", "Shared equally by law", "Her father's"], "Her wealth is hers; maintenance is on him.", f"{QD}, Book of Marriage"),
   ("In the Hanafi school, may a wife ask for housing separate from her in-laws?", "Yes, it is her right", ["No, she must live with them", "Only if they agree", "Only after children"], "Al-Quduri: he houses her where none of his family live, unless she chooses.", f"{QD}, Book of Maintenance"),
   ("Who must pay for the household's food, clothing and housing?", "The husband, even if the wife is wealthy", ["Whoever earns more", "The wife if she works", "Both equally"], "Maintenance is the husband's duty.", f"{QD}, Book of Maintenance"),
   ("'The best of you are…'", "The best to their wives", ["The richest", "The strictest at home", "The most travelled"], "Narrated by al-Tirmidhi.", "Sunan al-Tirmidhi, Book of Suckling"),
  ]),
 ("fm_husband", "The rights of the husband", "What a wife owes her husband.", [
   ("Obedience in what is right", "She follows him in what is right and reasonable in their married life. No one is obeyed in disobedience to Allah: if he tells her to sin, she refuses, gently.", f"{IH}"),
   ("The home and its doors", "She does not let into his home anyone he dislikes, and does not leave the home without his permission except for need, such as visiting her parents, which the Hanafi books allow once a week.", RM),
   ("His wealth and honour", "She guards his wealth, his honour and his secrets in his absence, and does not spend his money without his permission beyond what is customary.", IH),
   ("Closeness", "Each has a right to closeness from the other, and neither should refuse the other without a valid reason such as illness or menstruation.", IH),
   ("Her reward", "The Prophet ﷺ said: if a woman prays her five, fasts her month, guards her chastity and obeys her husband, she will be told: enter Paradise by whichever gate you wish.", "Musnad Ahmad, hadith of 'Abd al-Rahman ibn 'Awf"),
  ], [
   ("A husband tells his wife to do something sinful. She…", "Refuses gently", ["Must obey", "May obey if he insists", "Must leave the home"], "There is no obedience to a creature in disobedience to the Creator.", f"{IH}"),
   ("May a wife let into the home someone her husband dislikes?", "No", ["Yes, if they are her friends", "Yes, when he is out", "Only family"], "Guarding the home is his right.", IH),
   ("How often do the Hanafi books allow a wife to visit her parents?", "Once a week", ["Never without permission", "Once a year", "Only at Eid"], "Visiting parents is her right even if he dislikes it.", RM),
  ]),
 ("fm_together", "Living together", "The manners of intimacy, and what to do when there is discord.", [
   ("Before closeness", "Say: 'Bismillah. Allahumma jannibna al-shaytan wa jannib al-shaytana ma razaqtana' (In the name of Allah. O Allah, keep Shaytan away from us and from what You give us).", "Sahih al-Bukhari, Book of Wudu"),
   ("What is forbidden", "Intercourse during menstruation or nifas is haram, as is anal intercourse at any time. After intercourse ghusl is required before prayer.", "Qur'an, al-Baqarah 2:222"),
   ("Keep the secrets", "The Prophet ﷺ said among the worst people before Allah on the Day of Judgement is a man who is intimate with his wife and she with him, and then he spreads her secret.", "Sahih Muslim, Book of Marriage"),
   ("When there is discord", "The Qur'an's way is gentle steps: advice, then distance in bed, then family arbitrators from both sides to reconcile them (al-Nisa' 34–35). The scholars restricted anything beyond that to the lightest gesture that leaves no mark, never the face, and the Prophet ﷺ never struck a woman or a servant with his hand.", "Sahih Muslim, Book of Virtues"),
   ("Patience with each other", "The Prophet ﷺ said: let no believing man hate a believing woman; if he dislikes one trait in her, he will be pleased with another.", "Sahih Muslim, Book of Suckling"),
  ], [
   ("Intercourse during menstruation is…", "Haram", ["Disliked only", "Allowed with ghusl after", "Allowed in the last days"], "It is forbidden until her bleeding ends.", "Qur'an, al-Baqarah 2:222"),
   ("What does the Qur'an prescribe when a couple's dispute grows serious?", "Arbitrators from both families to reconcile them", ["Immediate divorce", "Telling everyone", "Ignoring it"], "Al-Nisa' 35.", "Qur'an, al-Nisa' 4:35"),
   ("Did the Prophet ﷺ ever strike a woman?", "No, never", ["Yes, lightly", "Once", "Only his servants"], "'A'ishah رَضِيَ اللَّهُ عَنْهَا reported he never struck a woman or servant with his hand.", "Sahih Muslim, Book of Virtues"),
  ]),
 ("fm_divorce", "Divorce, khul' and 'iddah", "Ending a marriage the right way, and the waiting period.", [
   ("Words that count", "Talaq takes effect when said clearly, even in anger, by text, or as a joke: 'three things are serious in earnest and in jest: marriage, divorce and taking back.' Only someone who has lost his mind entirely is excused.", "Sunan Abi Dawud, Book of Divorce"),
   ("One or two: taking back", "After one or two talaqs (raj'i), the husband may take her back during the 'iddah without a new nikah. After the 'iddah they need a new nikah, with her consent and a new mahr.", f"{QD}, Book of Divorce"),
   ("Three: final", "After three talaqs she is not lawful to him until she genuinely marries another man and that marriage ends. A pre-arranged 'halalah' to get around this is condemned: the Prophet ﷺ cursed the one who does it and the one it is done for.", "Sunan al-Tirmidhi, Book of Marriage"),
   ("Khul'", "If a wife wishes to leave and he will not divorce her, she may offer to return the mahr or something else in exchange for her release. If the fault is his, it is disliked for him to take anything; if it is hers, he should not take more than he gave.", f"{QD}, Book of Khul'"),
   ("'Iddah", "Divorced and menstruating: three periods. No periods (young or past menopause): three months. Pregnant: until she gives birth. Widowed: four months and ten days. During it she stays in her home, and may not be proposed to openly; a widow also leaves adornment and perfume.", f"{QD}, Book of 'Iddah"),
  ], [
   ("A man says 'I divorce you' as a joke. It…", "Counts as a divorce", ["Does not count", "Counts only if written", "Counts only with witnesses"], "Divorce is serious even in jest.", "Sunan Abi Dawud, Book of Divorce"),
   ("After one talaq, during the 'iddah, the husband may…", "Take her back without a new nikah", ["Never take her back", "Take her back only after another marriage", "Take her back only with a new mahr"], "This is a revocable (raj'i) divorce.", f"{QD}, Book of Divorce"),
   ("What is the 'iddah of a pregnant woman?", "Until she gives birth", ["Three months", "Four months and ten days", "Forty days"], "Al-Talaq 4.", f"{QD}, Book of 'Iddah"),
   ("What is khul'?", "The wife gives back the mahr or something else for her release", ["The husband divorcing three times", "A court annulment for impotence", "A trial separation"], "Agreed separation at the wife's request.", f"{QD}, Book of Khul'"),
  ]),
 ("hh_parents", "The rights of parents", "Honouring your parents, in their lives and after them.", [
   ("Next to Allah's right", "Allah joined thanks to Him with thanks to parents: 'Be grateful to Me and to your parents.' Disobeying parents is among the greatest of the major sins.", "Sahih al-Bukhari, Book of Good Manners (5976)"),
   ("Your mother, then your father", "A man asked who most deserves his good company. The Prophet ﷺ said: your mother, your mother, your mother, then your father. In another hadith (al-Nasa'i), Paradise lies at her feet.", "Sahih al-Bukhari, Book of Good Manners (5971)"),
   ("What you owe them", "Obey them in all that is not sin, speak gently, never say even 'uff', serve them, ask their permission before long travel, and spend on them if they are in need: in the Hanafi school this is wajib on a child who can.", f"{QD}, Book of Maintenance"),
   ("Even if they are not Muslim", "If they are not Muslim, you still keep them company in this world with kindness, but do not obey them in leaving Islam or in sin.", "Qur'an, Luqman 31:15"),
   ("Their pleasure", "The Prophet ﷺ said: the pleasure of the Lord is in the pleasure of the parent, and the anger of the Lord is in the anger of the parent.", "Sunan al-Tirmidhi, Book of Righteousness"),
   ("After they die", "Keep honouring them: make du'a and ask forgiveness for them, fulfil their promises, keep ties with their relatives, and honour their friends.", "Sunan Abi Dawud, Book of Good Manners"),
   ("Parents and spouse", "Marriage does not end your duty to your parents, and your parents' rights do not cancel your spouse's. Give each their right without wronging the other.", IH),
  ], [
   ("Your parents tell you to do something sinful. What do you do?", "Refuse gently, and keep being kind to them", ["Obey, they are your parents", "Cut contact", "Argue until they agree"], "Obey them in everything except sin.", "Qur'an, Luqman 31:15"),
   ("Who did the Prophet ﷺ name three times as most deserving of good company?", "Your mother", ["Your father", "Your spouse", "Your teacher"], "Mother three times, then father.", "Sahih al-Bukhari, Book of Good Manners (5971)"),
   ("Your parents are poor and you can support them. Spending on them is…", "Wajib", ["Optional charity", "Their own problem", "Only if they ask in writing"], "Supporting needy parents is a duty on a child who can.", f"{QD}, Book of Maintenance"),
   ("How do you honour parents after they die?", "Du'a, forgiveness, keeping their promises and ties", ["Nothing more can be done", "Only by building them a grave", "Only on the anniversary"], "Narrated by Abu Dawud.", "Sunan Abi Dawud, Book of Good Manners"),
  ]),
 ("fm_children", "The rights of children", "Raising children on the deen, and who looks after them.", [
   ("A trust", "'Protect yourselves and your families from a Fire.' Each of you is a shepherd and will be asked about his flock: children are a trust you will be questioned about.", "Sahih al-Bukhari, Book of Friday (893)"),
   ("From birth", "Say the adhan in the baby's right ear, give a good name, shave the head and give charity, and the 'aqiqah on the seventh day is recommended in the later Hanafi books.", "Sunan al-Tirmidhi, Book of Sacrifices"),
   ("Their maintenance", "The father must provide for his children: a son until he can earn, a daughter until she marries.", f"{QD}, Book of Maintenance"),
   ("Teaching the deen", "Teach them belief, purity and the Qur'an. Tell them to pray at seven, and be firmer at ten, and separate their beds.", "Sunan Abi Dawud, Book of Prayer"),
   ("Fairness", "'Fear Allah and be fair between your children.' Do not favour one child over another in gifts.", "Sahih al-Bukhari, Book of Gifts (2586)"),
   ("Custody after divorce", "The mother has the first right to raise young children, then her mother, then the father's mother. A boy stays with her until he can eat, dress and clean himself (about seven); a girl until she reaches puberty. The father still pays their maintenance.", f"{QD}, Book of Maintenance"),
  ], [
   ("Who must pay for the children's needs?", "The father", ["The mother", "Whoever has custody", "Both equally by law"], "Maintenance of children is on the father.", f"{QD}, Book of Maintenance"),
   ("At what age are children taught to pray?", "Seven", ["Three", "Ten", "Fifteen"], "Teach at seven; be firmer at ten.", "Sunan Abi Dawud, Book of Prayer"),
   ("After divorce, who has the first right to raise a young child?", "The mother", ["The father", "The father's mother", "The court"], "The mother first, then her mother.", f"{QD}, Book of Maintenance"),
   ("Giving one child a big gift and not the others is…", "Wrong; be fair between them", ["Allowed for the eldest", "Allowed for sons", "Required for the favourite"], "'Be fair between your children.'", "Sahih al-Bukhari, Book of Gifts (2586)"),
  ]),
 ("fm_kin", "Relatives and neighbours", "Keeping ties of kinship and honouring the neighbour.", [
   ("Ties of kinship", "Keeping ties with relatives (silat al-rahim) is wajib, and cutting them is a major sin: 'the one who cuts ties will not enter Paradise.' Visit them, help them, and keep in touch, even if they do not.", "Sahih al-Bukhari, Book of Good Manners"),
   ("It brings blessing", "The Prophet ﷺ said: whoever would like his provision increased and his life lengthened, let him keep ties with his relatives.", "Sahih al-Bukhari, Book of Good Manners"),
   ("The neighbour", "Jibril kept advising the Prophet ﷺ about the neighbour until he thought he would make him an heir. 'He is not a believer whose neighbour is not safe from his harm.'", "Sahih al-Bukhari, Book of Good Manners"),
   ("In practice", "Greet them, share food, visit them when ill, help when asked, avoid noise and nuisance, and be patient with their faults, whether or not they are Muslim.", "Ihya' 'Ulum al-Din, Book of Companionship"),
  ], [
   ("Cutting ties with relatives is…", "A major sin", ["Allowed if they wrong you", "Disliked only", "Your choice"], "Keeping ties is wajib.", "Sahih al-Bukhari, Book of Good Manners"),
   ("Who is not a believer, according to the hadith?", "One whose neighbour is not safe from his harm", ["One who has no neighbours", "One who lives alone", "One who moves house often"], "Narrated by al-Bukhari.", "Sahih al-Bukhari, Book of Good Manners"),
   ("Do neighbours' rights apply to non-Muslim neighbours?", "Yes", ["No", "Only if they are kind", "Only on Eid"], "Every neighbour has a right.", "Ihya' 'Ulum al-Din, Book of Companionship"),
  ]),
]
COURSE = {"id": "family", "title": "Marriage, family and rights", "ar": "الأُسْرَةُ وَالْحُقُوقُ",
  "sub": "Marriage, the rights of spouses, parents, children, relatives and neighbours", "book": "Mukhtasar al-Quduri, with Ihya' 'Ulum al-Din", "color": "#8A3B5C"}
AYAT = {
 "fm_before": [(24, 32, 32, "Marry those among you who are single, and the righteous among your servants. If they are poor, Allah will enrich them from His bounty.")],
 "fm_mahram": [(4, 23, 23, "Forbidden to you are your mothers, your daughters, your sisters, your fathers' sisters, your mothers' sisters, your brothers' daughters, your sisters' daughters, your mothers who nursed you, your sisters through nursing, your wives' mothers…")],
 "fm_wife": [(4, 19, 19, "…and live with them in kindness. If you dislike them, it may be that you dislike something in which Allah has placed much good.")],
 "fm_husband": [(2, 228, 228, "And they have rights like those upon them, in kindness, and men have a degree above them. Allah is Mighty, Wise.")],
 "fm_together": [(4, 35, 35, "If you fear a split between the two, appoint an arbitrator from his family and an arbitrator from hers. If they want reconciliation, Allah will bring them together.")],
 "fm_divorce": [(2, 229, 229, "Divorce is twice; then either keep her in kindness or release her with good.")],
 "hh_parents": [(17, 23, 24, "Your Lord has decreed that you worship none but Him, and be good to parents. If one or both reach old age with you, do not say to them even 'uff', nor scold them, but speak to them with noble words. Lower to them the wing of humility out of mercy, and say: My Lord, have mercy on them as they raised me when I was small."),
                (31, 14, 14, "We enjoined on man care for his parents: his mother carried him, weakness upon weakness… Be grateful to Me and to your parents; to Me is the return.")],
 "fm_children": [(66, 6, 6, "O you who believe, protect yourselves and your families from a Fire whose fuel is people and stones.")],
 "fm_kin": [(4, 36, 36, "Worship Allah and associate nothing with Him, and be good to parents, relatives, orphans, the needy, the near neighbour, the distant neighbour, the companion at your side and the traveller.")],
}
