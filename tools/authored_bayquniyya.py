"""al-Manzumah al-Bayquniyyah: the 34 verses (text from OpenITI) with an English rendering, for Year 4 lessons."""
EN = [
 "I begin with praise of Allah, sending blessings upon Muhammad ﷺ, the best Prophet ever sent.",
 "Here are the categories of hadith, counted out, each one coming with its definition.",
 "The first is the ṣaḥīḥ (sound): one whose chain is connected, and which is neither anomalous (shādhdh) nor defective (muʿall),",
 "narrated by an upright, precise narrator from one like him, relied upon in his precision and his transmission.",
 "The ḥasan (good) has known routes, but its narrators are not as renowned for precision as those of the ṣaḥīḥ.",
 "Everything that falls short of the rank of ḥasan is the ḍaʿīf (weak), and it has many kinds.",
 "What is ascribed to the Prophet ﷺ is the marfūʿ (raised); what is ascribed to a Follower (tābiʿī) is the maqṭūʿ (severed).",
 "The musnad is one whose chain is connected from its narrator all the way to the Chosen One ﷺ, without a break.",
 "One in which every narrator heard it from the next, so that its chain reaches the Chosen One ﷺ, is the muttaṣil (connected).",
 "Call musalsal (chained) a hadith that comes with a recurring feature, such as: 'By Allah, the young man told me',",
 "or: 'He narrated it to me while standing', or: 'After he narrated it to me he smiled.'",
 "ʿAzīz is narrated by two or three; mashhūr is narrated by more than three.",
 "Muʿanʿan is like 'from Saʿīd, from Karam'; mubham is one with a narrator who is not named.",
 "Every chain with few narrators is ʿālī (high); its opposite is nāzil (descended).",
 "What you ascribe to the Companions, of word or deed, is mawqūf (stopped), so know it.",
 "Mursal is one from which the Companion has dropped; and say gharīb (rare) is what only one narrator transmits.",
 "Every chain that is not connected in any way is munqaṭiʿ (broken), its links cut.",
 "The muʿḍal is one from which two have dropped; and the mudallas (concealed) is of two kinds:",
 "The first: dropping one's own teacher and transmitting from the one above him with 'from' or 'that'.",
 "The second: not dropping him, but describing him by traits by which he is not known.",
 "What a reliable narrator narrates against the majority is the shādhdh; and the maqlūb (inverted) follows, in two kinds:",
 "replacing one narrator with another is one kind, and giving a text the chain of another is the second kind.",
 "The fard (singular) is what you restrict to one reliable narrator, or to one group, or to one transmission.",
 "What has a hidden or subtle defect is known among them as the muʿallal (defective).",
 "One with conflicting versions in its chain or its text is the muḍṭarib (shaky) according to the people of this art.",
 "The mudraj (interpolated) in hadith are words of some narrators that became joined to it.",
 "When each of two peers narrates from the other, it is mudabbaj; know it well and be proud of it.",
 "Names agreeing in sound and in writing are the muttafiq; their opposite, in what we said, is the muftariq.",
 "The muʾtalif agrees in writing only, and its opposite is the mukhtalif; so beware of mistakes.",
 "The munkar is what a single narrator transmits alone whose reliability cannot bear that he alone narrates it.",
 "Its matrūk (abandoned) is what one narrator alone transmits whom all agree is weak, so it is rejected.",
 "The lie invented and fabricated against the Prophet ﷺ: that is the mawḍūʿ (forged).",
 "They have come like a hidden jewel; I named them the Poem of al-Bayquni.",
 "They number thirty and four, and its categories are complete, sealed with good.",
]
if __name__ == "__main__":
    import json
    ar = json.load(open("app/data/texts/bayquniyya.json"))["sections"][0]["p"]
    assert len(ar) == len(EN) == 34
    rows = [{"id": f"bq{i}", "ar": a, "en": e, "note": ""} for i, (a, e) in enumerate(zip(ar, EN))]
    json.dump(rows, open("app/data/lines/bayquniyya.json", "w"), ensure_ascii=False, separators=(",", ":"))
    d = json.load(open("app/data/texts/bayquniyya.json")); d["sections"][0]["en"] = EN; d["bilingual"] = True
    json.dump(d, open("app/data/texts/bayquniyya.json", "w"), ensure_ascii=False, separators=(",", ":"))
    print("bayquniyya", len(rows))
