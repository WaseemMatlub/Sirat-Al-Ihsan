"use strict";
/* ============================ SYLLABUS ============================ */
const META = /*META*/;
const YEARS = [   // THE COURSE PLAN. To move or add something, edit this list only: decks are in data/decks/<id>.json, lesson books in data/lines/<id>.json, full texts are LIBRARY ids (read:[...]).
 { n:1, title:"Foundations", desc:"The most common words of the Qur'an, the first books of sarf and nahw, the life of the Prophet ﷺ, and Nur al-Idah.",
   books:[
     { id:"w_quran", type:"words", deck:"quran", per:5, title:"Qur'an words", sub:"The most common words of the Qur'an, five at a time", glyph:"", color:"#B5651D", subject:"Arabic" },
     { id:"w_verbs1", type:"words", deck:"verbs1", per:5, title:"Verb drills", sub:"Sarf drilling: the most used verbs, five at a time, with their forms", glyph:"", color:"#B5651D", subject:"Arabic" },
     { id:"signs", fard:true, type:"hadith", per:3, title:"Signs of the Hour", sub:"An introduction, from Kitab al-Fitan of Imam al-Bukhari رحمه الله", glyph:"س", color:"#8C3B3B", subject:"Signs of the Hour" } ],
   decks:[
     { id:"quran", title:"Qur'an words: top 500", sub:"Vocabulary: about 86% of the Qur'an's text", glyph:"ق", color:"#8A4FA3", subject:"Arabic" },
     { id:"bina", simple:true, title:"Bina' al-Af'al", sub:"Sarf: how Arabic verbs are built", glyph:"", color:"#B5651D", subject:"Arabic" },
     { id:"verbs1", title:"Arabic verbs: 1–700", sub:"Sarf drilling: past, present and verbal noun", glyph:"ف", color:"#B5651D", subject:"Arabic" },
     { id:"ajr", simple:true, title:"al-Ajurrumiyyah", sub:"Nahw: the first text, question by question", glyph:"", color:"#B5651D", subject:"Arabic" },
     { id:"seerah1", simple:true, title:"Seerah essentials", sub:"The life of the Prophet ﷺ from birth to his passing", glyph:"", color:"#9A6A1F", subject:"Seerah" },
     { id:"nur", simple:true, title:"Nur al-Idah", sub:"Imam al-Shurunbulali رحمه الله: purification, prayer, fasting", glyph:"ن", color:"#2F6E8F", subject:"Fiqh" },
     { id:"themed", opt:true, title:"Vocabulary list", sub:"Everyday Arabic words grouped by topic: the body, home, food, travel and more", glyph:"", color:"#B5651D", subject:"Arabic" } ],
   read:["t_azhari", "t_nawawi_seerah", "t_nur"] },
 { n:2, title:"The Arabic of the Qur'an", desc:"Qur'anic vocabulary, Qatr al-Nada with i'rab practice, and al-Suyuti's works of the day and night.",
   books:[
     { id:"juz_amma", type:"lines", per:5, title:"Translating Juz' 'Amma", sub:"The meaning of each ayah, from al-Nas back to al-Naba'", glyph:"", color:"#1F6F78", subject:"Tafsir", ask:"What does this ayah mean?", askTitle:"The ayah" },
     { id:"irab", type:"lines", per:6, title:"I'rab practice", sub:"Al-Fatihah and five short surahs, word by word", glyph:"", color:"#B5651D", subject:"Arabic", ask:"What is the i'rab of this word?", askTitle:"Its i'rab" } ],
   decks:[
     { id:"roots", title:"Qur'an roots: top 1,000", sub:"Qur'an dictionary: the roots, ranked by how often they occur", glyph:"ج", color:"#8A4FA3", subject:"Arabic" },
     { id:"mufradat", title:"Mufradat al-Qur'an", sub:"Qur'an dictionary: Imam al-Raghib's رحمه الله root meanings, in Arabic and English", glyph:"", color:"#B5651D", subject:"Arabic" },
     { id:"qatr", simple:true, title:"Sharh Qatr al-Nada", sub:"Nahw: Ibn Hisham's رحمه الله text, question by question", glyph:"", color:"#B5651D", subject:"Arabic" } ],
   read:["t_qatr", "t_adhkar"] },
 { n:3, title:"Core texts", desc:"The Tahawiyyah, al-Quduri, the Forty Hadith, the Shama'il, Bidayat al-Hidayah, the End Times and Usul al-Shashi.",
   books:[
     { id:"tahawiyya", type:"lines", per:8, title:"Al-'Aqidah al-Tahawiyyah", sub:"The creed of Imam al-Tahawi رحمه الله, line by line", glyph:"ط", color:"#0E5A43", subject:"Aqeedah" },
     { id:"arbain", type:"lines", per:4, title:"The Forty Hadith", sub:"Imam al-Nawawi's رحمه الله forty, in Arabic and English", glyph:"", color:"#7A5230", subject:"Hadith" } ],
   decks:[
     { id:"quduri", simple:true, title:"Mukhtasar al-Quduri", sub:"Imam al-Quduri's رحمه الله Hanafi primer, question by question", glyph:"ق", color:"#2F6E8F", subject:"Fiqh" },
     { id:"shamail_qa", simple:true, title:"al-Shama'il, question by question", sub:"How the Prophet ﷺ looked, lived, ate, slept and prayed, from Imam al-Tirmidhi's رحمه الله collection", glyph:"", color:"#9A6A1F", subject:"Seerah" } ],
   read:["t_tahawiyya", "t_quduri", "t_shamail", "t_bidaya", "t_nihaya_fitan", "t_shashi"] },
 { n:4, title:"Higher texts", desc:"Al-Hidayah volume 1, Riyad al-Salihin, the sciences of hadith, and Sirr al-Asrar.",
   books:[
     { id:"bayquniyya", type:"lines", per:4, title:"al-Bayquniyyah", sub:"The 34 verses on the terms of hadith, with their meaning", glyph:"", color:"#7A5230", subject:"Hadith" } ],
   decks:[
     { id:"hidaya1", simple:true, title:"al-Hidayah, part 1", sub:"Volume 1: Imam al-Marghinani's رحمه الله Hanafi fiqh with its proofs", glyph:"", color:"#2F6E8F", subject:"Fiqh" },
     { id:"hidaya2", simple:true, title:"al-Hidayah, part 2", sub:"Volume 1, continued", glyph:"", color:"#2F6E8F", subject:"Fiqh" },
     { id:"sirr", simple:true, title:"Sirr al-Asrar", sub:"Shaykh 'Abd al-Qadir al-Jilani رحمه الله on the secret of secrets", glyph:"", color:"#5C6B2E", subject:"Tasawwuf" } ],
   read:["t_hidaya", "t_riyad", "t_nuzha", "t_bayquniyya"],
   coming:[["al-'Aqa'id al-Nasafiyyah","Aqeedah"],["al-Balaghah al-Wadihah","Arabic"]] },
 { n:5, title:"Dawrah", desc:"Tafsir al-Jalalayn on Juz' 'Amma, al-Taftazani on al-'Aqa'id al-Nasafiyyah, al-Hidayah volume 2, and Mukhtasar al-Bukhari.",
   books:[],
   decks:[
     { id:"jalalayn_amma", title:"Tafsir al-Jalalayn: Juz' 'Amma", sub:"Ayah by ayah, from al-Naba' to al-Nas", glyph:"", color:"#1F6F78", subject:"Tafsir" },
     { id:"nasafiyyah", simple:true, title:"Sharh al-'Aqa'id al-Nasafiyyah", sub:"The commentary of al-Taftazani رحمه الله, question by question", glyph:"ع", color:"#0E5A43", subject:"Aqeedah" },
     { id:"hidaya3", simple:true, title:"al-Hidayah, part 3", sub:"Volume 2: Imam al-Marghinani's رحمه الله Hanafi fiqh with its proofs", glyph:"", color:"#2F6E8F", subject:"Fiqh" },
     { id:"hidaya4", simple:true, title:"al-Hidayah, part 4", sub:"Volume 2, continued", glyph:"", color:"#2F6E8F", subject:"Fiqh" } ],
   read:["t_jalalayn", "t_tajrid"],
   coming:[["Isaghuji (mantiq)","Mantiq"],["al-Fawz al-Kabir fi Usul al-Tafsir","Tafsir"]] },
];
/* The Library: complete books, by year. Covers are drawn from these fields. */
const LIBRARY = [
  [1,"t_tahawiyya","tahawiyya_full","Aqeedah","The Creed of Imam al-Tahawi","العقيدة الطحاوية","Imam Abu Ja'far al-Tahawi","الإمام أبو جعفر الطحاوي","d. 321 AH","The creed of Ahl al-Sunnah, point by point"],
  [1,"t_umm","umm","Aqeedah","Umm al-Barahin","أم البراهين","Imam Muhammad ibn Yusuf al-Sanusi","الإمام محمد بن يوسف السنوسي","d. 895 AH","What is necessary, impossible and possible for Allah and His messengers ﷺ"],
  [1,"t_nur","nur_idah","Fiqh","Nur al-Idah","نور الإيضاح","Imam Hasan al-Shurunbulali","الإمام حسن الشرنبلالي","d. 1069 AH","Hanafi fiqh of purification, prayer and fasting"],
  [1,"t_ajurrum","ajurrumiyya","Arabic","al-Ajurrumiyyah","المقدمة الآجرومية","Imam Ibn Ajurrum al-Sanhaji","الإمام ابن آجروم الصنهاجي","d. 723 AH","The first text of Arabic grammar"],
  [1,"t_arbain","arbain","Hadith","The Forty Hadith","الأربعون النووية","Imam Yahya ibn Sharaf al-Nawawi","الإمام يحيى بن شرف النووي","d. 676 AH","Forty-two hadith on which the religion turns"],
  [2,"t_jawhara","jawhara","Aqeedah","Jawharat al-Tawhid","جوهرة التوحيد","Imam Ibrahim al-Laqqani","الإمام إبراهيم اللقاني","d. 1041 AH","The Ash'ari creed in verse"],
  [2,"t_fiqhakbar","fiqh_akbar","Aqeedah","al-Fiqh al-Akbar","الفقه الأكبر","Imam Abu Hanifah al-Nu'man","الإمام أبو حنيفة النعمان","d. 150 AH","The greatest understanding: the Imam's creed"],
  [2,"t_quduri","quduri","Fiqh","Mukhtasar al-Quduri","مختصر القدوري","Imam Abu'l-Husayn al-Quduri","الإمام أبو الحسين القدوري","d. 428 AH","The classic Hanafi manual, every kitab"],
  [2,"t_maraqi","maraqi","Fiqh","Maraqi al-Falah","مراقي الفلاح","Imam Hasan al-Shurunbulali","الإمام حسن الشرنبلالي","d. 1069 AH","The commentary on Nur al-Idah"],
  [2,"t_shashi","usul_shashi","Usul al-Fiqh","Usul al-Shashi","أصول الشاشي","Imam Nizam al-Din al-Shashi","الإمام نظام الدين الشاشي","d. 344 AH","The first text of Hanafi usul"],
  [2,"t_qatr","qatr","Arabic","Sharh Qatr al-Nada","شرح قطر الندى","Imam Jamal al-Din Ibn Hisham","الإمام جمال الدين ابن هشام","d. 761 AH","Arabic grammar, explained by its author"],
  [2,"t_riyad","riyad","Hadith","Riyad al-Salihin","رياض الصالحين","Imam Yahya ibn Sharaf al-Nawawi","الإمام يحيى بن شرف النووي","d. 676 AH","The gardens of the righteous, bab by bab"],
  [2,"t_muslim","muslim","Hadith","Sahih Muslim","صحيح مسلم","Imam Muslim ibn al-Hajjaj","الإمام مسلم بن الحجاج","d. 261 AH","The complete collection, in Arabic and English"],
  [2,"t_burda","burda","Seerah","Qasidat al-Burdah","قصيدة البردة","Imam Sharaf al-Din al-Busiri","الإمام شرف الدين البوصيري","d. 696 AH","The poem of the Cloak, in praise of the Prophet ﷺ"],
  [3,"t_majalla","majalla","Fiqh","The Majallah","مجلة الأحكام العدلية","The Ottoman committee of jurists","لجنة من فقهاء الدولة العثمانية","1293 AH","The Hanafi civil code, all sixteen books"],
  [3,"t_kanz","kanz","Fiqh","Kanz al-Daqa'iq","كنز الدقائق","Imam Hafiz al-Din al-Nasafi","الإمام حافظ الدين النسفي","d. 710 AH","The treasure of fine points: advanced Hanafi fiqh"],
  [3,"t_jalalayn","jalalayn","Tafsir","Tafsir al-Jalalayn","تفسير الجلالين","Imams al-Mahalli and al-Suyuti","الإمامان المحلي والسيوطي","d. 864 and 911 AH","Tafsir of the whole Qur'an"],
  [4,"t_hidaya","hidaya","Fiqh","al-Hidayah","الهداية","Imam Burhan al-Din al-Marghinani","الإمام برهان الدين المرغيناني","d. 593 AH","The great Hanafi commentary, with its proofs"],
  [4,"t_mughni","mughni","Arabic","Mughni al-Labib","مغني اللبيب","Imam Jamal al-Din Ibn Hisham","الإمام جمال الدين ابن هشام","d. 761 AH","Advanced grammar: particles and sentences"],
  [4,"t_iqtisad","iqtisad","Aqeedah","al-Iqtisad fi'l-I'tiqad","الاقتصاد في الاعتقاد","Imam Abu Hamid al-Ghazali","الإمام أبو حامد الغزالي","d. 505 AH","Moderation in belief, with its proofs"],
  [5,"t_bukhari","bukhari","Hadith","Sahih al-Bukhari","صحيح البخاري","Imam Muhammad ibn Isma'il al-Bukhari","الإمام محمد بن إسماعيل البخاري","d. 256 AH","The complete collection, in Arabic and English"],
  [5,"t_shamail","shamail","Seerah","al-Shama'il al-Muhammadiyyah","الشمائل المحمدية","Imam Abu 'Isa al-Tirmidhi","الإمام أبو عيسى الترمذي","d. 279 AH","The description and character of the Prophet ﷺ"],
  [1,"t_fusul","fusul","Seerah","al-Fusul fi Sirat al-Rasul ﷺ","الفصول في سيرة الرسول","Imam Ibn Kathir","الإمام ابن كثير","d. 774 AH","A short seerah, chapter by chapter"],
  [2,"t_jazariyya","jazariyya","Tajweed","al-Muqaddimah al-Jazariyyah","المقدمة الجزرية","Imam Ibn al-Jazari","الإمام ابن الجزري","d. 833 AH","The classic poem on tajweed, with harakat and English"],
  [2,"t_nuryaqin","nuryaqin","Seerah","Nur al-Yaqin","نور اليقين في سيرة سيد المرسلين","Shaykh Muhammad al-Khudari","الشيخ محمد الخضري","d. 1345 AH","The seerah taught in madrasas for a century"],
  [3,"t_tamhid","tamhid","Tajweed","al-Tamhid fi 'Ilm al-Tajwid","التمهيد في علم التجويد","Imam Ibn al-Jazari","الإمام ابن الجزري","d. 833 AH","Ibn al-Jazari's prose work on tajweed"],
  [4,"t_ibnhisham","ibnhisham","Seerah","al-Sirah al-Nabawiyyah","السيرة النبوية","Imam Ibn Hisham","الإمام ابن هشام","d. 213 AH","The great early seerah, from Ibn Ishaq"],
  [1,"t_nahwmir","nahwmir","Arabic","Nahw Mir","نحو مير","Mir Sayyid Sharif al-Jurjani","مير سيد شريف الجرجاني","d. 816 AH","First steps in Arabic grammar, fully vowelled"],
  [1,"t_azhari","azhari","Arabic","Sharh al-Ajurrumiyyah of Khalid al-Azhari","شرح الشيخ خالد الأزهري على الآجرومية","Shaykh Khalid al-Azhari","الشيخ خالد الأزهري","d. 905 AH","The Ajurrumiyyah explained line by line, fully vowelled"],
  [1,"t_miatamil","miatamil","Arabic","Sharh Mi'at 'Amil","شرح مائة عامل","Imam 'Abd al-Rahman al-Jami","الإمام عبد الرحمن الجامي","d. 898 AH","The hundred words that govern endings, explained"],
  [2,"t_hidayatnahw","hidayatnahw","Arabic","Hidayat al-Nahw","هداية النحو","Shaykh Siraj al-Din 'Uthman al-Awadhi","الشيخ سراج الدين عثمان الأودهي","d. 758 AH","The whole of nahw in clear, vowelled Arabic"],
  [4,"t_hikam","hikam","Tasawwuf","al-Hikam al-'Ata'iyyah","الحكم العطائية","Imam Ibn 'Ata' Allah al-Iskandari","الإمام ابن عطاء الله السكندري","d. 709 AH","The 264 aphorisms, the letters and the intimate prayers, fully vowelled"],
  [1,"t_adhkar","adhkar","Tasawwuf","al-Adhkar","الأذكار","Imam al-Nawawi","الإمام النووي","d. 676 AH","The remembrances of the day and night, from the Sunnah"],
  [1,"t_tibyan","tibyan","Tajweed","al-Tibyan fi Adab Hamalat al-Qur'an","التبيان في آداب حملة القرآن","Imam al-Nawawi","الإمام النووي","d. 676 AH","The manners of those who carry the Qur'an"],
  [2,"t_munqidh","munqidh","Tasawwuf","al-Munqidh min al-Dalal","المنقذ من الضلال","Imam Abu Hamid al-Ghazali","الإمام أبو حامد الغزالي","d. 505 AH","Al-Ghazali's own account of his search for certainty"],
  [3,"t_ikhtiyar","ikhtiyar","Fiqh","al-Ikhtiyar li-Ta'lil al-Mukhtar","الاختيار لتعليل المختار","Imam 'Abd Allah ibn Mahmud al-Mawsili","الإمام عبد الله بن محمود الموصلي","d. 683 AH","Hanafi fiqh with the reasons behind each ruling"],
  [3,"t_tuhfa","tuhfa","Fiqh","Tuhfat al-Fuqaha'","تحفة الفقهاء","Imam 'Ala' al-Din al-Samarqandi","الإمام علاء الدين السمرقندي","d. 539 AH","The Hanafi text that Bada'i' al-Sana'i' explains"],
  [3,"t_shatibiyya","shatibiyya","Tajweed","al-Shatibiyyah (Hirz al-Amani)","حرز الأماني ووجه التهاني","Imam al-Qasim ibn Firruh al-Shatibi","الإمام القاسم بن فيره الشاطبي","d. 590 AH","The poem of the seven readings"],
  [4,"t_usul_sarakhsi","usul_sarakhsi","Usul al-Fiqh","Usul al-Sarakhsi","أصول السرخسي","Imam Shams al-A'immah al-Sarakhsi","الإمام شمس الأئمة السرخسي","d. 483 AH","The Hanafi principles of fiqh, dictated by the author"],
  [4,"t_mizan_usul","mizan_usul","Usul al-Fiqh","Mizan al-Usul","ميزان الأصول في نتائج العقول","Imam 'Ala' al-Din al-Samarqandi","الإمام علاء الدين السمرقندي","d. 539 AH","Usul al-fiqh on the method of the Hanafi mutakallimun"],
  [4,"t_nasafi","nasafi","Tafsir","Tafsir al-Nasafi (Madarik al-Tanzil)","مدارك التنزيل وحقائق التأويل","Imam Hafiz al-Din al-Nasafi","الإمام حافظ الدين النسفي","d. 710 AH","A Hanafi, Maturidi tafsir of the whole Qur'an"],
  [5,"t_tabyin","tabyin","Fiqh","Tabyin al-Haqa'iq","تبيين الحقائق شرح كنز الدقائق","Imam Fakhr al-Din al-Zayla'i","الإمام فخر الدين الزيلعي","d. 743 AH","The great commentary on Kanz al-Daqa'iq, with al-Shalabi's notes"],
  [5,"t_badai","badai","Fiqh","Bada'i' al-Sana'i'","بدائع الصنائع في ترتيب الشرائع","Imam 'Ala' al-Din al-Kasani","الإمام علاء الدين الكاساني","d. 587 AH","Hanafi fiqh arranged by its principles"],
  [5,"t_mabsut","mabsut","Fiqh","al-Mabsut","المبسوط","Imam Shams al-A'immah al-Sarakhsi","الإمام شمس الأئمة السرخسي","d. 483 AH","The vast Hanafi encyclopaedia, dictated from prison"],
  [1,"t_ayyuha","ayyuha","Tasawwuf","Ayyuha al-Walad","أيها الولد","Imam Abu Hamid al-Ghazali","الإمام أبو حامد الغزالي","d. 505 AH","A letter of advice to a student: knowledge is for acting on"],
  [1,"t_nawawi_seerah","nawawi_seerah","Seerah","The Life of the Prophet ﷺ (from Tahdhib al-Asma')","الترجمة النبوية من تهذيب الأسماء واللغات","Imam al-Nawawi","الإمام النووي","d. 676 AH","His lineage, description, family, character and miracles"],
  [3,"t_nihaya_fitan","nihaya_fitan","Signs of the Hour","al-Nihayah fi'l-Fitan wa'l-Malahim","النهاية في الفتن والملاحم","Imam Ibn Kathir","الإمام ابن كثير","d. 774 AH","The trials and great battles before the Hour"],
  [4,"t_nuzha","nuzha","Hadith","Nuzhat al-Nazar (Sharh Nukhbat al-Fikar)","نزهة النظر في توضيح نخبة الفكر","Imam Ibn Hajar al-'Asqalani","الإمام ابن حجر العسقلاني","d. 852 AH","The sciences of hadith, explained by their author"],
  [4,"t_bayquniyya","bayquniyya","Hadith","al-Manzumah al-Bayquniyyah","المنظومة البيقونية","Imam 'Umar al-Bayquni","الإمام عمر البيقوني","d. 1080 AH","The 34-line poem on the terms of hadith"],
  [5,"t_tajrid","tajrid","Hadith","Mukhtasar Sahih al-Bukhari (al-Tajrid al-Sarih)","التجريد الصريح لأحاديث الجامع الصحيح","Imam Zayn al-Din al-Zabidi","الإمام زين الدين الزبيدي","d. 893 AH","Sahih al-Bukhari without the repeats and chains"],
  [2,"t_qisas","qisas","History","Qisas al-Anbiya'","قصص الأنبياء","Imam Ibn Kathir","الإمام ابن كثير","d. 774 AH","The stories of the prophets عليهم السلام, from Adam to 'Isa"],
  [3,"t_tarikh_khulafa","tarikh_khulafa","History","Tarikh al-Khulafa'","تاريخ الخلفاء","Imam Jalal al-Din al-Suyuti","الإمام جلال الدين السيوطي","d. 911 AH","The caliphs from Abu Bakr رضي الله عنه to the author's own time"],
  [1,"t_bidaya","bidaya","Tasawwuf","Bidayat al-Hidayah","بداية الهداية","Imam Abu Hamid al-Ghazali","الإمام أبو حامد الغزالي","d. 505 AH","The beginning of guidance: a day of worship, and keeping away from sin"],
  [3,"t_taarruf","taarruf","Tasawwuf","al-Ta'arruf li-Madhhab Ahl al-Tasawwuf","التعرف لمذهب أهل التصوف","Imam Abu Bakr al-Kalabadhi","الإمام أبو بكر الكلاباذي","d. 380 AH","What the early Sufis believed and taught"],
  [4,"t_qut","qut","Tasawwuf","Qut al-Qulub","قوت القلوب","Imam Abu Talib al-Makki","الإمام أبو طالب المكي","d. 386 AH","Nourishment of the hearts: the inner life of worship"],
  [5,"t_ghunya","ghunya","Tasawwuf","al-Ghunyah li-Talibi Tariq al-Haqq","الغنية لطالبي طريق الحق","Shaykh 'Abd al-Qadir al-Jilani","الشيخ عبد القادر الجيلاني","d. 561 AH","Belief, worship, manners and the path, for seekers of the truth"],
  [5,"t_alfiyya","alfiyya","Arabic","Alfiyyat Ibn Malik","ألفية ابن مالك","Imam Jamal al-Din Ibn Malik","الإمام جمال الدين ابن مالك","d. 672 AH","The thousand-line poem of grammar"],
  [2,"t_risala","risala","Tasawwuf","al-Risalah al-Qushayriyyah","الرسالة القشيرية","Imam Abu'l-Qasim al-Qushayri","الإمام أبو القاسم القشيري","d. 465 AH","The classic guide to Tasawwuf: its people, stations and states"],
  [3,"t_kafiya","kafiya","Arabic","al-Kafiyah","الكافية في النحو","Imam Ibn al-Hajib","الإمام ابن الحاجب","d. 646 AH","The classic concise text of nahw"],
  [3,"t_maqamat","maqamat","Arabic","Maqamat al-Hariri","مقامات الحريري","Imam Abu Muhammad al-Hariri","الإمام أبو محمد الحريري","d. 516 AH","Fifty tales in the finest Arabic prose"],
  [3,"t_manar","manar","Usul al-Fiqh","al-Manar","منار الأنوار","Imam Hafiz al-Din al-Nasafi","الإمام حافظ الدين النسفي","d. 710 AH","The usul text explained in Nur al-Anwar"],
  [3,"t_shifa","shifa","Seerah","al-Shifa","الشفا بتعريف حقوق المصطفى","Qadi 'Iyad","القاضي عياض","d. 544 AH","The rights of the Prophet ﷺ and his perfect qualities"],
  [3,"t_tadhkira","tadhkira","Signs of the Hour","al-Tadhkirah","التذكرة بأحوال الموتى وأمور الآخرة","Imam al-Qurtubi","الإمام القرطبي","d. 671 AH","Death, the grave, the Hour and the Hereafter"],
  [4,"t_baydawi","baydawi","Tafsir","Tafsir al-Baydawi","أنوار التنزيل وأسرار التأويل","Qadi Nasir al-Din al-Baydawi","القاضي ناصر الدين البيضاوي","d. 685 AH","The lights of revelation: tafsir of the whole Qur'an"],
  [4,"t_mukhtasar","mukhtasar_maani","Arabic","Mukhtasar al-Ma'ani","مختصر المعاني","Imam Sa'd al-Din al-Taftazani","الإمام سعد الدين التفتازاني","d. 792 AH","Balaghah: meanings, expression and ornament"],
  [4,"t_milal","milal","Comparative Aqeedah","al-Milal wa'l-Nihal","الملل والنحل","Imam al-Shahrastani","الإمام الشهرستاني","d. 548 AH","The religions and sects, and what each one holds"],
  [4,"t_ihya","ihya","Tasawwuf","Ihya' 'Ulum al-Din","إحياء علوم الدين","Imam Abu Hamid al-Ghazali","الإمام أبو حامد الغزالي","d. 505 AH","The revival of the religious sciences, all forty books"],
  [4,"t_tawdih","tawdih","Usul al-Fiqh","al-Tawdih","التوضيح في حل غوامض التنقيح","Imam Sadr al-Shari'ah al-Mahbubi","الإمام صدر الشريعة المحبوبي","d. 747 AH","Advanced Hanafi usul al-fiqh"],
  [5,"t_muwatta","muwatta","Hadith","al-Muwatta'","الموطأ","Imam Malik ibn Anas","الإمام مالك بن أنس","d. 179 AH","The first great book of hadith and fiqh"],
  [5,"t_abudawud","abudawud","Hadith","Sunan Abi Dawud","سنن أبي داود","Imam Abu Dawud al-Sijistani","الإمام أبو داود السجستاني","d. 275 AH","The hadith of rulings"],
  [5,"t_tirmidhi","tirmidhi","Hadith","Jami' al-Tirmidhi","جامع الترمذي","Imam Abu 'Isa al-Tirmidhi","الإمام أبو عيسى الترمذي","d. 279 AH","Hadith with their grading and the views of the jurists"],
  [5,"t_nasai","nasai","Hadith","Sunan al-Nasa'i","سنن النسائي","Imam Ahmad ibn Shu'ayb al-Nasa'i","الإمام أحمد بن شعيب النسائي","d. 303 AH","al-Mujtaba, the shorter Sunan"],
  [5,"t_ibnmajah","ibnmajah","Hadith","Sunan Ibn Majah","سنن ابن ماجه","Imam Ibn Majah al-Qazwini","الإمام ابن ماجه القزويني","d. 273 AH","The sixth of the six books"],
  [5,"t_sharhmaani","sharh_maani","Hadith","Sharh Ma'ani al-Athar","شرح معاني الآثار","Imam Abu Ja'far al-Tahawi","الإمام أبو جعفر الطحاوي","d. 321 AH","Hadith that seem to differ, reconciled with Hanafi reasoning"],
].map(([y,id,file,subject,title,ar,author,authorAr,when,sub]) => ({ y, id, file, subject, title, ar, author, authorAr, when, sub, type:"text", per:1, glyph:"",
  honor: author.startsWith("The Ottoman") ? "" : author.startsWith("Imams") ? "رحمهما الله" : "رحمه الله" }));
YEARS.forEach(y => (y.read||[]).forEach(id => { const b = LIBRARY.find(x => x.id === id); if (b) b.y = y.n; }));
LIBRARY.forEach(b => { if (b.y >= 1) YEARS[b.y-1].books.push(b); });   // Fard al-'Ayn books live in the Library only
/* After Year 5: one year of further study in a module the student chooses */
const SPEC_YEAR = 6;
/* Each year's syllabus is made of these modules */
const MODULES = [
  { name:"Aqeedah", art:"light", color:"#0E5A43", about:"What a Muslim believes, in the Ash'ari and Maturidi tradition." },
  { name:"Comparative Aqeedah", art:"scales", color:"#3E5C76", about:"How Ahl al-Sunnah answer other sects and creeds." },
  { name:"Tajweed", art:"rehal", color:"#8A4FA3", about:"Reciting the Qur'an correctly." },
  { name:"Tafsir", art:"pen", color:"#1F6F78", about:"Translating and explaining the meanings of the Qur'an." },
  { name:"Hadith", art:"scroll", color:"#7A5230", about:"The hadith collections and the sciences of hadith." },
  { name:"Arabic", art:"letter", color:"#B5651D", about:"Sarf, nahw, balaghah and adab: the Arabic of the Qur'an." },
  { name:"Fiqh", art:"drop", color:"#2F6E8F", about:"Hanafi fiqh, from purification to inheritance." },
  { name:"Usul al-Fiqh", art:"tree", color:"#4E6B3A", about:"The principles behind Hanafi rulings." },
  { name:"Tasawwuf", art:"star", color:"#5C6B2E", about:"Purifying the heart, open to all the turuq." },
  { name:"Signs of the Hour", art:"hourglass", color:"#8C3B3B", about:"The minor and major signs before the Last Day." },
  { name:"Seerah", art:"moon", color:"#9A6A1F", about:"The life of the Prophet ﷺ, his family and Companions." },
  { name:"Mantiq", art:"logic", color:"#5A5A78", about:"Logic: the tool for reading the higher texts." } ];
/* Takhassus: what further study looks like in each module */
const SPEC_TEXTS = {
  "Aqeedah":["Sharh al-Mawaqif (selections)","al-Musamarah"], "Comparative Aqeedah":["Tabsirat al-Adillah of Abu'l-Mu'in al-Nasafi","al-Fisal and refutations (selections)"],
  "Tajweed":["al-Shatibiyyah","The ten qira'at: al-Durrah and Tayyibat al-Nashr"], "Tafsir":["Ruh al-Ma'ani (selections)","al-Itqan fi 'Ulum al-Qur'an"],
  "Hadith":["Fath al-Bari and 'Umdat al-Qari (selections)","Tadrib al-Rawi"], "Arabic":["Alfiyyat Ibn Malik with Sharh Ibn 'Aqil","al-Mutawwal"],
  "Fiqh":["Ifta': Radd al-Muhtar of Ibn 'Abidin","Sharh 'Uqud Rasm al-Mufti"], "Usul al-Fiqh":["Kashf al-Asrar 'ala Usul al-Bazdawi","al-Tahrir of Ibn al-Humam"],
  "Tasawwuf":["Ihya' 'Ulum al-Din","'Awarif al-Ma'arif"], "Signs of the Hour":["al-Tadhkirah of al-Qurtubi","al-Nihayah fi'l-Fitan wa'l-Malahim"],
  "Seerah":["al-Mawahib al-Ladunniyyah with al-Zurqani","Subul al-Huda wa'l-Rashad"], "Mantiq":["Sharh Sullam al-'Ulum (Hamdullah)","al-Qadi Mubarak"] };
const TARIQA_OPTIONAL = ["Qadiri: Sirr al-Asrar","Chishti: Kashf al-Mahjub","Naqshbandi: Etiquettes of the Path","Shadhili: further Ibn 'Ata'illah"];
const DATA = {};
/* Corrections from reports (data/fixes.json): { cards:{ id:{f?,b?,hide?} }, lines:{ id:{ar?,en?,note?,hide?} } }.
   Applied on top of the decks, so a fix never needs the decks rebuilt. */
let FIXES = null;
async function loadFixes(){ if (FIXES) return FIXES; try { const r = await fetch("data/fixes.json", { cache:"no-cache" }); FIXES = r.ok ? await r.json() : {}; } catch(e){ FIXES = {}; } return FIXES; }
const fixAll = (list, kind) => { const F = (FIXES && FIXES[kind]) || {}; return list.map(x => F[x.id] ? { ...x, ...F[x.id] } : x).filter(x => !x.hide); };
async function loadYear(n){ INDEX = null; await loadFixes();
  if (DATA[n]) return DATA[n];
  const y = yearOf(n); if (!y.prepared) return (DATA[n] = {});
  const on = d => !d.opt || (S.optOn||{})[d.id];
  await Promise.all([...y.decks.filter(on), ...(n === 1 ? FARD_DECKS.filter(on) : [])].map(d => loadDeck(d).catch(() => {})));
  await Promise.all(y.books.filter(b => b.type === "lines" || b.type === "hadith").map(async b => {
    if (b.lines) return; const r = await fetch(`data/lines/${b.id}.json`); if (r.ok) b.lines = fixAll(await r.json(), "lines"); }));
  for (const b of y.books) if (b.type === "words") { const dk = wordDeck(b); if (dk && dk.cards) b.lines = dk.cards.map(c => ({ id:c.id, ar:c.f, en:c.b, note:c.s || "", ex:c.ex, exr:c.exr, card:c })); }
  return (DATA[n] = {});
}
const yearOf = n => YEARS[n-1];
const loaded = y => !!DATA[y.n];
const wordDeck = b => allDecks().find(d => d.id === b.deck);
const lessonsOf = b => b.type === "words" ? Math.ceil(deckSize(wordDeck(b)) / b.per) : b.type === "text" ? ((META.texts||{})[b.file]||1) : Math.ceil((b.lines ? b.lines.length : (META.lines||{})[b.id] || 0) / b.per);
/* Full texts load one book at a time */
const TEXTS = {};
async function loadText(file){ if (TEXTS[file]) return TEXTS[file]; const r = await fetch(`data/texts/${file}.json`); if (!r.ok) throw new Error("Could not load text"); return (TEXTS[file] = await r.json()); }
/* Big books (Bukhari, Muslim, al-Hidayah…) come as an index plus parts; fetch the part a section is in */
async function loadSection(file, i){
  const T = await loadText(file); if (!T.split || T.sections[i].p) return T;
  const k = Math.floor(i / T.split), r = await fetch(`data/texts/${file}/${k}.json`); if (!r.ok) throw new Error("Could not load text");
  (await r.json()).forEach((s, j) => Object.assign(T.sections[k*T.split + j], s)); return T; }
const secLen = s => s.p ? s.p.length : s.n || 0;
const bookById = id => YEARS.flatMap(y=>y.books).find(x=>x.id===id);
const lessonBooks = y => y.books.filter(b => b.type !== "text" && !b.fard);
YEARS.forEach(y => { y.prepared = lessonBooks(y).filter(b => b.type !== "words").length + y.decks.length > 0; y.books.forEach(b => b.year = y.n); y.decks.forEach(d => d.year = y.n); });
const deckSize = d => d.cards ? d.cards.length : (META.decks||{})[d.id] || 0;
const core = decks => decks.filter(d => !d.opt);
/* What each text is, in plain English: shown first, with the classical title under it */
const PLAIN = { nur:"Hanafi fiqh: purification, prayer, fasting", ajr:"Arabic grammar: first steps", bina:"How Arabic verbs are built", izzi:"The patterns of the Arabic verb",
  tahawiyya:"The core beliefs of Sunni Islam", umm:"What we believe about Allah and His messengers ﷺ", signs:"Signs of the Hour, from al-Bukhari", jawhara:"The creed, in verse",
  quduri:"Hanafi fiqh: the complete manual", ithaf:"Fiqh questions and answers", qatr:"Arabic grammar: the next level", burda:"The Poem of the Cloak", signs2:"Signs of the Hour, from Muslim",
  mufradat:"Qur'an words and their root meanings", themed:"Everyday Arabic words", sirr:"The secret of secrets", naqsh:"Manners of the Naqshbandi path",
  majalla:"99 principles of Islamic law", nasafiyyah:"Islamic theology, explained", kanz:"Hanafi fiqh: the advanced manual", sharhizzi:"Verb patterns, explained",
  jalalayn:"Tafsir of the whole Qur'an", fuqaha:"Dictionary of fiqh terms", ghawth:"On the awliya' and the Qutb", qasaid:"Poems in praise of the Prophet ﷺ",
  mughni:"Advanced Arabic grammar", iqtisad:"Belief, with its rational proofs", qushayri:"Tafsir of the heart", nuqaya:"A Hanafi summary in Arabic",
  philosophy:"Terms of logic and theology", tajwid:"How to recite the Qur'an correctly", seerah1:"The life of the Prophet ﷺ", jazariyya:"The tajweed poem", poetry:"Classical Arabic poetry", hidaya1:"Hanafi fiqh with proofs: part 1", hidaya2:"Hanafi fiqh with proofs: part 2", hidaya3:"Hanafi fiqh with proofs: part 3", hidaya4:"Hanafi fiqh with proofs: part 4", alfiyya:"The thousand-line grammar poem", proofs:"The evidence for Hanafi rulings" };
const nameOf = x => PLAIN[x.id] || x.title;
const classicOf = x => PLAIN[x.id] && PLAIN[x.id] !== x.title ? `<span class="classic">${esc(x.title)}</span>` : "<br>";          // optional decks never gate a year or appear in its test
/* Optional decks: one file each, fetched the first time a student opens one, then on every start */
async function loadDeck(d){ if (d.cards) return d; const r = await fetch(`data/decks/${d.id}.json`); if (!r.ok) throw new Error("Could not load " + d.title);
  await loadFixes(); d.cards = fixAll(await r.json(), "cards").map((c,k) => ({ ...c, deck:d.id, _i:k })); INDEX = null; return d; }

/* ============================ STATE ============================ */
const KEY = "ihsan.v3";
const PASS = 0.8, MASTER_IVL = 7, RETAIN = 0.85, TEST_LEN = 40;
function fresh(){ return { welcomed:false, xp:0, streak:0, lastDay:null, days:{}, offset:0, newPerDay:10, newDone:{}, books:{}, cards:{}, log:[], tests:{}, unlocked:[1], spec:null, advancedGrades:false, saved:[], reports:[] }; }
function load(){ try{ const s = JSON.parse(localStorage.getItem(KEY)); return s && s.cards ? Object.assign(fresh(), s) : fresh(); }catch(e){ return fresh(); } }
function save(){ try{ localStorage.setItem(KEY, JSON.stringify(S)); }catch(e){} }
let S = load();
const today = () => Math.floor((Date.now() - new Date().getTimezoneOffset()*60000) / 864e5) + S.offset;
/* ---- Global leaderboard (opt-in). Needs data/config.json {url, key} for a Supabase project; hidden until then. ---- */
let SBC = null;
async function sbConf(){ if (SBC !== null) return SBC; try { const r = await fetch("data/config.json", { cache:"no-store" }); const c = r.ok ? await r.json() : null; SBC = c && c.url && c.key ? c : false; } catch(e){ SBC = false; } return SBC; }
function lbIdentity(){                         // no account: a random id and a secret code kept on this device
  S.lb = S.lb || {};
  if (!S.lb.id) { const h = n => [...crypto.getRandomValues(new Uint8Array(n))].map(b => b.toString(16).padStart(2, "0")).join("");
    S.lb.id = crypto.randomUUID ? crypto.randomUUID() : h(4)+"-"+h(2)+"-4"+h(2).slice(1)+"-a"+h(2).slice(1)+"-"+h(6); S.lb.secret = h(24); save(); }
  return S.lb;
}
async function sbRpc(fn, body){ const c = await sbConf(); if (!c) return false;
  try { const r = await fetch(`${c.url}/rest/v1/rpc/${fn}`, { method:"POST", headers:{ apikey:c.key, "Content-Type":"application/json" }, body:JSON.stringify(body||{}) }); return r.ok; } catch(e){ return false; } }
async function lbSubmit(force){
  const L = S.lb; if (!L || !L.on || !L.name || !navigator.onLine) return;
  if (!force && (!L.pending || Date.now() - (L.sent||0) < 60000)) return;
  const gain = Math.min(L.pending||0, 400);
  const I = lbIdentity();
  if (await sbRpc("submit_score", { p_id:I.id, p_secret:I.secret, p_name:L.name, p_total:S.xp, p_gain:gain, p_streak:S.streak })) { L.pending = Math.max(0, (L.pending||0) - gain); L.sent = Date.now(); save(); }
}
const weekStartUTC = () => { const d = new Date(), k = (d.getUTCDay() + 6) % 7; d.setUTCDate(d.getUTCDate() - k); return d.toISOString().slice(0,10); };
async function lbFetch(mode){
  const c = await sbConf(); if (!c) return null;
  const q = mode === "all" ? "order=xp.desc" : `order=week_xp.desc&week_start=eq.${weekStartUTC()}&week_xp=gt.0`;
  try { const r = await fetch(`${c.url}/rest/v1/leaderboard?select=id,name,xp,week_xp,streak&${q}&limit=50`, { headers:{ apikey:c.key } }); return r.ok ? await r.json() : null; } catch(e){ return null; }
}
async function fillLeaderboard(){
  const box = document.getElementById("lb"); if (!box || !(await sbConf())) return;
  const L = S.lb || {}, mode = L.mode || "week";
  box.hidden = false;
  if (!L.on) { box.innerHTML = `<p class="label" style="margin-top:0">Leaderboard</p>
      <p class="small muted" style="margin:0 0 10px">See how you compare with other students around the world. Only a nickname you choose is shown.</p>
      <div style="display:flex;gap:8px"><input id="lb-name" maxlength="20" placeholder="Nickname (not your full name)" value="${esc(S.name||"")}" style="flex:1;min-width:0">
      <button class="btn small-btn" id="lb-join" style="width:auto">Join</button></div>`;
    $("#lb-join").onclick = async () => { const n = $("#lb-name").value.trim().replace(/[<>]/g, ""); if (n.length < 2) return toast("Choose a nickname of at least 2 letters");
      S.lb = { ...(S.lb||{}), on:true, name:n, pending:0, mode:"week" }; save(); box.innerHTML = `<p class="small muted" style="margin:0">Joining…</p>`;
      await lbSubmit(true); fillLeaderboard(); };
    return; }
  box.innerHTML = `<div class="spread"><p class="label" style="margin:0">Leaderboard</p><div class="seg mini">${[["week","This week"],["all","All time"]].map(([k,t]) => `<button data-lbm="${k}" class="${mode===k?"on":""}">${t}</button>`).join("")}</div></div><p class="small muted" style="margin:8px 0">Loading…</p>`;
  box.querySelectorAll("[data-lbm]").forEach(b => b.onclick = () => { S.lb.mode = b.dataset.lbm; save(); fillLeaderboard(); });
  await lbSubmit();
  const rows = await lbFetch(mode), me = L.id;
  const list = rows === null ? `<p class="small muted">The leaderboard couldn't load. Check your connection.</p>` : !rows.length ? `<p class="small muted">No one yet this week. Finish a lesson to be first.</p>` :
    `<ol class="lb-list">${rows.map((r,i) => `<li class="${r.id===me?"me":""}"><span class="lb-rank">${i+1}</span><span class="lb-name">${esc(r.name)}${r.id===me?" (you)":""}</span><span class="lb-pts">${(mode==="all"?r.xp:r.week_xp).toLocaleString()} XP</span></li>`).join("")}</ol>`;
  box.querySelector("p.small.muted").outerHTML = list + `<button class="linkbtn small" id="lb-leave">Leave the leaderboard</button>`;
  $("#lb-leave").onclick = async () => { if (!confirmInline("lb-leave", "Tap again to remove your name")) return; await sbRpc("leave_leaderboard", { p_id:S.lb.id, p_secret:S.lb.secret }); S.lb = { ...S.lb, on:false }; save(); fillLeaderboard(); };
}
function confirmInline(id, msg){ const b = document.getElementById(id); if (b.dataset.sure) return true; b.dataset.sure = "1"; b.textContent = msg; return false; }
/* ---- Streak reminder: a phone notification in the evening if today's study isn't done yet. Needs the "remind" Supabase function. ---- */
const pushOK = () => "serviceWorker" in navigator && "PushManager" in window && "Notification" in window;
const b64u = s => { const p = "=".repeat((4 - s.length % 4) % 4), b = atob((s + p).replace(/-/g, "+").replace(/_/g, "/")); return Uint8Array.from(b, c => c.charCodeAt(0)); };
async function remindOn(){
  const c = await sbConf(); if (!c) return "Reminders aren't available yet.";
  if (!pushOK()) return /iPhone|iPad/.test(navigator.userAgent) ? "On iPhone, add the app to your Home Screen first (Share, then Add to Home Screen), then turn this on from there." : "This browser can't show reminders.";
  if (await Notification.requestPermission() !== "granted") return "Notifications are blocked. Allow them for this app in your phone's settings.";
  try {
    const { key } = await fetch(`${c.url}/functions/v1/remind?key=1`, { headers:{ Authorization:`Bearer ${c.anon}` } }).then(r => r.json());
    const reg = await navigator.serviceWorker.ready;
    const sub = (await reg.pushManager.getSubscription()) || await reg.pushManager.subscribe({ userVisibleOnly:true, applicationServerKey:b64u(key) });
    const j = sub.toJSON(), I = lbIdentity();
    const ok = await sbRpc("save_push", { p_id:I.id, p_secret:I.secret, p_endpoint:j.endpoint, p_p256dh:j.keys.p256dh, p_auth:j.keys.auth, p_tz:new Date().getTimezoneOffset(), p_hour:S.remindHour||20, p_streak:S.streak, p_day:S.lastDay||0 });
    if (!ok) return "Couldn't turn reminders on. Check your connection and try again.";
    S.remind = true; save(); return null;
  } catch(e){ return "Couldn't turn reminders on on this device."; }
}
async function remindOff(){ try { const reg = await navigator.serviceWorker.ready, sub = await reg.pushManager.getSubscription(); if (sub) await sub.unsubscribe(); } catch(e){}
  const I = lbIdentity(); await sbRpc("remove_push", { p_id:I.id, p_secret:I.secret }); S.remind = false; save(); }
function remindProgress(){ if (!S.remind) return; const I = lbIdentity(); sbRpc("push_progress", { p_id:I.id, p_secret:I.secret, p_streak:S.streak, p_day:S.lastDay }); }
/* Save a whole year for offline study: its flashcards, lessons, books to read and word audio go into the lasting "ihsan-data" store */
async function saveOffline(n, btn){
  if (!("caches" in window)) return toast("This browser can't save for offline use");
  const st = document.getElementById(`offst-${n}`), y = yearOf(n), urls = new Set(["data/meta.json", "data/fixes.json", "data/wordaudio.json", `data/daily/${new Date().getMonth()}.json`]);
  btn.disabled = true; st.textContent = "Getting ready…";
  try { if (navigator.storage && navigator.storage.persist) navigator.storage.persist(); } catch(e){}
  await loadYear(n).catch(() => {});
  const decks = [...y.decks.filter(d => !d.opt || (S.optOn||{})[d.id]), ...(n === 1 ? FARD_DECKS : [])];
  decks.forEach(d => urls.add(`data/decks/${d.id}.json`));
  y.books.filter(b => b.type === "lines" || b.type === "hadith").forEach(b => urls.add(`data/lines/${b.id}.json`));
  const have = await wordAudio();
  y.books.filter(b => b.type === "words").forEach(b => (b.lines||[]).forEach(l => { if (have.has(l.id)) urls.add(`audio/words/${l.id}.mp3`); }));
  for (const id of [...(y.read||[]), ...(n === 1 ? ["t_ayyuha"] : [])]) { const b = bookById(id); if (!b) continue;
    urls.add(`data/texts/${b.file}.json`);
    try { const T = await loadText(b.file); if (T.split) for (let k = 0; k * T.split < T.sections.length; k++) urls.add(`data/texts/${b.file}/${k}.json`); } catch(e){} }
  const c = await caches.open("ihsan-data"), list = [...urls]; let done = 0, failed = 0;
  const one = async u => { const key = new URL(u, location.href); key.search = "";
    try { if (!(await c.match(key.href))) { const r = await fetch(u); if (r.ok) await c.put(key.href, r); else failed++; } } catch(e){ failed++; }
    done++; if (done % 5 === 0 || done === list.length) st.textContent = `Saving… ${Math.round(done / list.length * 100)}%`; };
  for (let i = 0; i < list.length; i += 6) await Promise.all(list.slice(i, i + 6).map(one));
  btn.disabled = false;
  if (failed) { st.textContent = `Saved most of it. ${failed} file${failed>1?"s":""} couldn't be fetched; try again on Wi-Fi.`; return; }
  S.offline = { ...(S.offline||{}), [n]: Date.now() }; save(); st.textContent = "Saved. Year " + n + " now works without internet."; btn.textContent = "Update";
}
function touchDay(xp){ if (S.lb && S.lb.on) S.lb.pending = (S.lb.pending||0) + xp; setTimeout(() => lbSubmit(), 1500);
 const t = today(), adv = S.lastDay !== t; if (adv) S.streak = (S.lastDay === t-1) ? S.streak + 1 : 1; S.lastDay = t; S.xp += xp; S.days[t] = (S.days[t]||0) + xp; save(); if (adv) remindProgress(); return adv; }
if (S.lastDay !== null && today() - S.lastDay > 1) { S.streak = 0; save(); }

/* ======================= SPACED REPETITION ======================= */
function schedule(st, g){
  const s = st ? { ...st } : { ivl:0, ease:2.5, reps:0, lapses:0, due:today() };
  const wasReview = s.ivl >= 1;
  if (g === 0){ if (wasReview){ s.lapses++; s.ease = Math.max(1.3, s.ease-0.2); } s.ivl = 0; }
  else if (g === 1){ if (wasReview){ s.ivl = Math.max(s.ivl+1, Math.round(s.ivl*1.2)); s.ease = Math.max(1.3, s.ease-0.15); } else s.ivl = 0; }
  else if (g === 2){ s.ivl = wasReview ? Math.max(s.ivl+1, Math.round(s.ivl*s.ease)) : 1; }
  else { s.ivl = wasReview ? Math.max(s.ivl+2, Math.round(s.ivl*s.ease*1.3)) : 3; s.ease += 0.15; }
  s.reps++; s.due = today() + s.ivl;
  return { s, wasReview };
}
const ivlLabel = (st, g) => { const n = schedule(st, g).s.ivl; return n === 0 ? "again" : n < 30 ? n + "d" : Math.round(n/30) + "mo"; };
function deckStats(deck){
  if (!deck.cards) return { total:deckSize(deck), nw:deck.opt ? 0 : deckSize(deck), learning:0, due:0, mastered:0 };
  let nw=0, learning=0, due=0, mastered=0; const t = today();
  for (const c of deck.cards){ const st = S.cards[c.id];
    if (!st) nw++; else { if (st.ivl >= MASTER_IVL) mastered++; else learning++; if (st.due <= t) due++; } }
  return { total:deck.cards.length, nw, learning, due, mastered };
}
function retention(){ const r = S.log.slice(-300); return r.length ? r.filter(x=>x).length / r.length : null; }
const newToday = () => Object.values(S.newDone[today()]||{}).reduce((p,q)=>p+q,0);
const newLeft = () => Math.max(0, S.newPerDay - newToday());          // one daily total across every deck
const newAvail = decks => Math.min(newLeft(), decks.reduce((s,d) => s + deckStats(d).nw, 0));
const activeYears = () => YEARS.filter(y => S.unlocked.includes(y.n) && loaded(y));

/* ======================= YEAR PROGRESS ======================= */
const bookDone = b => Math.min((S.books[b.id]||[]).length, lessonsOf(b));
function yearStatus(y){
  const gb = lessonBooks(y), lt = gb.reduce((a,b)=>a+lessonsOf(b),0), ld = gb.reduce((a,b)=>a+bookDone(b),0);
  const ct = core(y.decks).reduce((a,d)=>a+deckSize(d),0), cm = core(y.decks).reduce((a,d)=>a+deckStats(d).mastered,0);
  const ret = retention(), booksOk = ld >= lt, cardsOk = ct === 0 || (cm >= ct && ret !== null && ret >= RETAIN);
  const reads = (y.read||[]).map(bookById).filter(Boolean), rt = reads.reduce((a,b)=>a+lessonsOf(b),0), rd = reads.reduce((a,b)=>a+bookDone(b),0);
  const t = S.tests[y.n], readOk = rd >= rt;
  return { reads:rt?rd/rt:1, readOk, rd, rt, open:y.prepared && booksOk && readOk, books:lt?ld/lt:0, booksOk, ld, lt, flash:ct?cm/ct:0, cardsOk, cm, ct, ret, ready:y.prepared && booksOk && cardsOk, passed:!!(t && t.passed), best:t ? t.best : null };
}

/* ============================ HELPERS ============================ */
const $ = s => document.querySelector(s);
const AR_RUN = /[\u0600-\u06FF\uFDF0-\uFDFF\uFE70-\uFEFF](?:[\u0600-\u06FF\uFDF0-\uFDFF\uFE70-\uFEFF\u064B-\u065F\s]*[\u0600-\u06FF\uFDF0-\uFDFF\uFE70-\uFEFF])?/g;
/* escape HTML; in English text, isolate Arabic phrases (ﷺ, رضي الله عنه…) so word order stays correct */
window.escH = s => esc(s);
/* Harakat on/off, one setting for the whole app. Qur'anic text (﴿…﴾, {…}, Qur'an-word cards) always keeps its harakat. */
const HARAKAT = /[\u064B-\u0652\u0670\u0653-\u0655]/g;
const stripH = s => s.replace(/(﴿[^﴾]*﴾|\{[^}]*\})|([^﴿{]+)/g, (m, q, t) => q ? q : t.replace(HARAKAT, ""));
const escQ = s => { s = String(s ?? ""); const mixed = /[A-Za-z]/.test(s);       // test before escaping: "&quot;" is not English
  s = s.replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  return mixed ? s.replace(AR_RUN, m => "\u2068" + m + "\u2069") : s; };
const esc = s => { s = String(s ?? ""); if (typeof S !== "undefined" && S && S.harakat === false && /[\u064B-\u0652]/.test(s)) s = stripH(s); return escQ(s); };
const shuffle = a => { a = a.slice(); for (let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; };
const pct = x => Math.round(x*100) + "%";
const isAr = s => /[؀-ۿ]/.test(String(s).slice(0,40));
const snip = (s, n=170) => { s = String(s).replace(/^Narrated [^:]{1,80}:\s*/,""); return s.length > n ? s.slice(0, n).replace(/\s+\S*$/,"") + "…" : s; };
/* ---- Multiple choice that makes sense ----
   Only standalone questions; wrong options come from the same part of the same book, in the same language and of a similar length */
const STOP = new Set("what which when where does with that this from have there their they them into about would could should what's whose these those than then also only such upon been being because according".split(" "));
const kw = s => new Set((s.toLowerCase().match(/[a-zʿʾāīūḥṣḍṭẓ\u0621-\u064A'’]{4,}/g)||[]).filter(w => !STOP.has(w)));
const arRatio = s => ((s.match(/[\u0621-\u064A]/g)||[]).length) / Math.max(1, s.replace(/[\s\p{P}\d]/gu,"").length);
const yesNo = s => /^(yes|no|neither|both)\b/i.test(s.trim());
const CONTEXTUAL = /\[i\.e\.|^(how does (he|she|one) do (that|this)|is there anything|and if\b|what if (he|she|it)\b|does the ruling change|why\?|explain\.?$)|\b(the above|mentioned above|in this case|in that case|the previous)\b|^(he|she|they|it)\b/i;
function mcqOK(c){
  const q = c.f || "", a = c.b || "";
  if (a.length < 2 || a.length > 170 || q.length < 2) return false;
  if (!c.fa && yesNo(a)) return false;                                   // a bare yes/no can be guessed from the other options
  if (CONTEXTUAL.test(q)) return false;                                  // needs the previous card to make sense
  if (!c.fa && /\b(additional|anything else|what else|another|the same|the rest|these|those|its ruling|the ruling)\b/i.test(q) && kw(q).size < 3) return false;
  if (!c.fa && arRatio(q) < .5 && kw(q).size < 2) return false;          // too vague to stand alone
  if (/\n/.test(a) || /^\(?\d\.\s/.test(a)) return false;                // numbered lists don't fit an option button
  if (/\b(AH|CE)\b/.test(a) && /\b1[34]\d\d\b/.test(a)) return false;      // editors' notes about the printed edition
  return true;
}
function pickDistractors(c, pool, n=3){
  const qk = kw(c.f), al = Math.max(4, c.b.length), aAr = arRatio(c.b) > .5, i0 = c._i ?? 0, out = [];
  for (const x of pool){
    if (x === c || !x.b || x.b === c.b || x.b.length > 200) continue;
    if ((arRatio(x.b) > .5) !== aAr || yesNo(x.b) !== yesNo(c.b)) continue;
    const lr = x.b.length / al; if (lr < .35 || lr > 2.8) continue;
    let ov = 0; for (const w of kw(x.f)) if (qk.has(w)) ov++;
    const near = Math.max(0, 1 - Math.abs((x._i ?? 0) - i0) / 80);
    out.push([ov*2 + near*2.5 + (x.g && x.g === c.g ? 3 : 0) - Math.abs(Math.log(lr)) + Math.random()*.8, x.b]);
  }
  out.sort((p,q) => q[0]-p[0]);
  return distinct(out.slice(0, 10).map(s => s[1]), c.b, n);
}
function narrator(en){
  const m = (en||"").match(/^(?:Narrated\s+|It (?:is|was) narrated (?:on the authority of|from|that)\s+|This hadith has been (?:narrated|reported) (?:on the authority of|by)\s+)?([A-Z][A-Za-z'`’ .-]{2,50}?)(?:\s*رضي الله عن\S*)?\s*(?::|,|\breported\b|\bnarrated\b|\bsaid\b|\bthat\b)/);
  return m && !/^(The|Allah|He|She|They|This|It)\b/.test(m[1]) ? m[1].replace(/\s+(b\.|bin|ibn)$/,"").trim() : null;
}
function distinct(pool, answer, n){ const seen = new Set([answer]), out = []; for (const x of shuffle(pool)){ if (!seen.has(x)){ seen.add(x); out.push(x); if (out.length === n) break; } } return out; }
const ICON = {
  gear:`<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>`,
  globe:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/></svg>',
  play:'<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M7 4.5v15a1 1 0 0 0 1.5.9l12-7.5a1 1 0 0 0 0-1.7l-12-7.5A1 1 0 0 0 7 4.5z"/></svg>',
  pause:'<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4.5" height="16" rx="1"/><rect x="13.5" y="4" width="4.5" height="16" rx="1"/></svg>',
  ear:'<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="5" height="7" rx="2"/><rect x="16" y="14" width="5" height="7" rx="2"/></svg>',
  flame:'<svg viewBox="0 0 24 24"><path d="M12 2c1 4 5 5.5 5 11a5 5 0 0 1-10 0c0-2.5 1.2-4 2.5-5 .2 2 1 3 2 3.5C11 9 11 5.5 12 2Z" fill="var(--gold)"/></svg>',
  star:'<svg viewBox="0 0 24 24"><path d="m12 2.8 2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9L12 2.8Z" fill="var(--brand)"/></svg>',
  learn:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5.5C5 4 9 4 12 6c3-2 7-2 10-.5V19c-3-1.5-7-1.5-10 .5-3-2-7-2-10-.5Z"/><path d="M12 6v13.5"/></svg>',
  home:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"><path d="M4 10.5 12 4l8 6.5V20h-5.5v-5.5h-5V20H4z"/></svg>',
  shelf:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5h3v14M9 19V7h3v12M14.5 19.2 17.8 6l2.9.7-3.3 13.2"/><path d="M3 19.5h18"/></svg>',
  search:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>',
  user:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4.5 4.5-6.5 8-6.5s7 2 8 6.5"/></svg>',
  save:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"><path d="M6 3h12v18l-6-4.5L6 21z"/></svg>',
  saved:'<svg viewBox="0 0 24 24" fill="var(--gold)" stroke="var(--gold)" stroke-width="2.2" stroke-linejoin="round"><path d="M6 3h12v18l-6-4.5L6 21z"/></svg>',
  flag:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21V4m0 0h11l-2 4 2 4H5"/></svg>',
  know:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m4 12 5 5L20 6"/></svg>',
  x:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>',
  back:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>',
  lock:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
  check:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></svg>',
  logo:'<svg viewBox="0 0 32 32"><path d="M16 2 19 8.5 26 6l-2.5 7L30 16l-6.5 3L26 26l-7-2.5L16 30l-3-6.5L6 26l2.5-7L2 16l6.5-3L6 6l7 2.5Z" fill="var(--brand)"/><circle cx="16" cy="16" r="5.5" fill="var(--bg)"/><circle cx="16" cy="16" r="3" fill="var(--gold)"/></svg>'
};
/* ---- Original illustration set: an arch with a motif per subject ---- */
const ART_OF = { tahawiyya:"light", umm:"star", signs:"hourglass", jawhara:"star", majalla:"scales", quran:"rehal", nur:"drop", quduri:"drop", kanz:"scales", ithaf:"pen", roots:"tree", verbs1:"letter", verbs2:"letter", nasafiyyah:"light" };
function art(kind, color, size=44){
  const c = color, g = "#C8912B";
  const motif = {
    light:`<polygon points="50,22 30,96 70,96" fill="${g}" opacity=".45"/><circle cx="50" cy="24" r="7" fill="${g}"/><ellipse cx="50" cy="98" rx="38" ry="12" fill="${c}"/>`,
    star:`<g transform="translate(50 62)"><rect x="-20" y="-20" width="40" height="40" fill="${c}"/><rect x="-20" y="-20" width="40" height="40" fill="${c}" transform="rotate(45)"/><circle r="10" fill="${g}"/></g>`,
    hourglass:`<path d="M32 30h36M32 94h36M36 30c0 18 28 22 28 32s-28 14-28 32M64 30c0 18-28 22-28 32s28 14 28 32" stroke="${c}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M41 86c4-8 14-8 18 0z" fill="${g}"/><path d="M44 44h12l-6 10z" fill="${g}"/>`,
    scales:`<path d="M50 30v62M30 92h40M24 44h52" stroke="${c}" stroke-width="5" stroke-linecap="round"/><path d="M24 44l-9 22h18zM76 44l-9 22h18z" fill="${g}"/><circle cx="50" cy="30" r="5" fill="${c}"/>`,
    rehal:`<path d="M26 86l48-30M74 86L26 56" stroke="${c}" stroke-width="6" stroke-linecap="round"/><path d="M22 56c10-8 22-8 28 0 6-8 18-8 28 0v-26c-10-6-22-6-28 2-6-8-18-8-28-2z" fill="${g}"/><path d="M50 32v24" stroke="${c}" stroke-width="2"/>`,
    drop:`<path d="M50 28c12 18 22 30 22 44a22 22 0 0 1-44 0c0-14 10-26 22-44z" fill="${c}"/><path d="M42 74a9 9 0 0 0 9 9" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/><ellipse cx="50" cy="100" rx="30" ry="5" fill="${g}" opacity=".7"/>`,
    scroll:`<rect x="28" y="34" width="44" height="58" rx="4" fill="${c}"/><circle cx="28" cy="38" r="7" fill="${c}"/><circle cx="72" cy="88" r="7" fill="${c}"/><path d="M38 50h24M38 60h24M38 70h16" stroke="${g}" stroke-width="4" stroke-linecap="round"/>`,
    logic:`<path d="M50 34L28 84h44z" fill="none" stroke="${c}" stroke-width="5" stroke-linejoin="round"/><circle cx="50" cy="34" r="8" fill="${g}"/><circle cx="28" cy="84" r="8" fill="${c}"/><circle cx="72" cy="84" r="8" fill="${c}"/>`,
    moon:`<path d="M62 34a26 26 0 1 0 6 44 22 22 0 1 1-6-44z" fill="${c}"/><polygon points="70,46 73,54 81,54 75,59 77,67 70,62 63,67 65,59 59,54 67,54" fill="${g}"/>`,
    pen:`<path d="M30 92l40-58 8 6-40 58-10 4z" fill="${c}"/><path d="M26 100c14-6 30-2 48-8" stroke="${g}" stroke-width="5" fill="none" stroke-linecap="round"/>`,
    tree:`<path d="M50 96V58M50 72l-12-10M50 66l12-10" stroke="${c}" stroke-width="5" stroke-linecap="round"/><circle cx="50" cy="44" r="18" fill="${c}"/><circle cx="34" cy="54" r="11" fill="${c}"/><circle cx="66" cy="54" r="11" fill="${c}"/><path d="M50 96l-12 8M50 96l12 8M50 96v10" stroke="${g}" stroke-width="4" stroke-linecap="round"/>`,
    letter:`<text x="50" y="86" text-anchor="middle" font-family="Amiri, serif" font-size="62" fill="${c}">ع</text><circle cx="72" cy="40" r="5" fill="${g}"/>`,
  }[kind] || "";
  return `<svg class="art" width="${size}" height="${size*1.1}" viewBox="0 0 100 110" aria-hidden="true"><path d="M8 110V46a42 42 0 0 1 84 0v64z" fill="${c}" opacity=".14"/><path d="M8 110V46a42 42 0 0 1 84 0v64z" fill="none" stroke="${c}" stroke-opacity=".25" stroke-width="2"/>${motif}</svg>`;
}
const artFor = (x, size) => art(ART_OF[x.id] || (MODULES.find(m => m.name === x.subject)||{}).art || "star", x.color, size);
/* ---- Jibreel-style numbered points for long English answers ---- */
function points(text){
  const t = String(text).trim();
  const bold = s => { const m = s.match(/^([^:–—]{2,40})(:|\s[–—]\s)(.+)$/); return m ? `<b>${esc(m[1])}</b>${esc(m[2])}${esc(m[3])}` : esc(s); };
  const list = (intro, items) => `${intro?`<p style="margin:0 0 10px">${esc(intro)}</p>`:""}<ol class="pts">${items.map(i=>`<li>${bold(i.replace(/^(and|or)\s+/i,"").replace(/[.;,]\s*$/,""))}</li>`).join("")}</ol>`;
  const ci = t.indexOf(":");
  if (ci > 0 && ci < 140){ const items = t.slice(ci+1).split(/;\s+|,\s+(?![^()]*\))/).map(s=>s.trim()).filter(Boolean);
    if (items.length >= 3 && items.every(i => i.length <= 110)) return list(t.slice(0, ci+1), items); }
  const semi = t.split(/;\s+/); if (semi.length >= 3) return list("", semi);
  const sent = t.match(/[^.!?]+[.!?]+(\s|$)/g);
  if (t.length > 260 && sent && sent.length >= 3) return list("", sent.map(s=>s.trim()));
  return `<p style="margin:0">${esc(t)}</p>`;
}
function weekStrip(){
  const t = today(), dow = (new Date((t)*864e5).getUTCDay()+6)%7, start = t - dow;
  return `<div class="week">${["Mo","Tu","We","Th","Fr","Sa","Su"].map((l,i)=>{ const d = start+i, on = (S.days[d]||0) > 0;
    return `<div class="wd ${d===t?"now":""} ${on?"on":""}"><span>${l}</span>${ICON.flame.replace('<svg','<svg width="22" height="22"')}</div>`; }).join("")}</div>`;
}
function nextLesson(){
  const ord = b => (b.type === "words" ? 100 : 0) + MODULES.findIndex(m => m.name === b.subject);     // belief first; word sets after the book lessons
  for (const y of activeYears()) for (const b of lessonBooks(y).sort((p,q) => ord(p) - ord(q))){ const L = lessonsOf(b), done = S.books[b.id]||[];
    for (let i=0;i<L;i++) if (!done.includes(i)) return { b, i, L, y }; }
  return null;
}
function modal(html, onReady){ const d = document.createElement("div"); d.className = "modal"; d.innerHTML = `<div class="card" role="dialog">${html}</div>`; document.body.appendChild(d); onReady && onReady(d, () => d.remove()); return d; }
function confirmBox(text, onYes){ modal(`<p style="margin-top:0;font-weight:700">${esc(text)}</p><div class="btnrow"><button class="btn ghost" id="mno">Cancel</button><button class="btn" id="myes">Yes</button></div>`, (d, close) => { d.querySelector("#mno").onclick = close; d.querySelector("#myes").onclick = () => { close(); onYes(); }; }); }

/* ============================ VIEWS ============================ */
let view = { name:"home" };
const isLibBook = () => view.name === "book" && bookById(view.id) && bookById(view.id).type === "text";
function applyTheme(){ const t = S.theme || "auto", r = document.documentElement; if (t === "auto") r.removeAttribute("data-theme"); else r.setAttribute("data-theme", t);
  const dark = t === "dark" || (t === "auto" && matchMedia("(prefers-color-scheme: dark)").matches), m = document.querySelector('meta[name="theme-color"]'); if (m) m.content = dark ? "#141412" : "#FAF7F0"; }
function go(v){ if (typeof stopAudio === "function" && AUD.on) stopAudio(); view = v; render(); window.scrollTo(0,0); }
function shell(inner){
  return `<header class="topbar"><div class="brandmark">${ICON.logo}<span>Dār aṣ-Ṣiddīq</span></div>
    <div class="stats"><button class="chip iconbtn" data-go="search" aria-label="Search">${ICON.search}</button><button class="chip iconbtn" data-go="settings" aria-label="Settings">${ICON.gear}</button><span class="chip" aria-label="${S.streak} day streak">${ICON.flame}${S.streak}</span></div></header>
    <main>${inner}</main>
    <nav class="tabs"><div class="in"><button data-go="home" ${["home","unit"].includes(view.name)?'aria-current="page"':""}>${ICON.home}Learn</button><button data-go="syllabus" ${["syllabus","year","spec"].includes(view.name)||(view.name==="book"&&!isLibBook())?'aria-current="page"':""}>${ICON.learn}Course</button><button data-go="library" ${view.name==="library"||isLibBook()?'aria-current="page"':""}>${ICON.shelf}Library</button><button data-go="profile" ${view.name==="profile"?'aria-current="page"':""}>${ICON.user}Progress</button></div></nav>`;
}
/* First visit: three short steps, then straight into learning */
const ARCH = (w=170) => `<svg class="arch" viewBox="0 0 200 240" width="${w}" aria-hidden="true"><defs><pattern id="ob-p" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M10 1l2.6 6.4L19 10l-6.4 2.6L10 19l-2.6-6.4L1 10l6.4-2.6z" fill="none" stroke="#E2C27A" stroke-width=".7" opacity=".45"/></pattern></defs>
  <path d="M20 236V96Q20 24 100 8Q180 24 180 96V236Z" fill="#0E5A43"/><path d="M20 236V96Q20 24 100 8Q180 24 180 96V236Z" fill="url(#ob-p)" opacity=".5"/>
  <path d="M38 236V102Q38 46 100 30Q162 46 162 102V236" fill="none" stroke="#E2C27A" stroke-width="2"/>
  <path class="ob-star" d="M100.0 72.0 L105.0 88.0 L119.8 80.2 L112.0 95.0 L128.0 100.0 L112.0 105.0 L119.8 119.8 L105.0 112.0 L100.0 128.0 L95.0 112.0 L80.2 119.8 L88.0 105.0 L72.0 100.0 L88.0 95.0 L80.2 80.2 L95.0 88.0Z" fill="#E2C27A"/>
  <text x="100" y="186" text-anchor="middle" font-family="Amiri, serif" font-weight="700" font-size="25" fill="#E2C27A" direction="rtl">دار الصديق</text><text x="100" y="214" text-anchor="middle" font-family="Amiri, serif" font-weight="700" font-size="19" fill="#E2C27A" direction="rtl">الأكبر</text></svg>`;
let OB = { step:1 };
function welcomeView(){
  const dots = `<div class="ob-dots" aria-hidden="true">${[1,2,3].map(k => `<i class="${k===OB.step?"on":""}"></i>`).join("")}</div>`;
  if (OB.step === 1) return `<div class="welcome"><div class="welcome-in">${ARCH()}
    <h1>Dār aṣ-Ṣiddīq al-Akbar</h1><p class="w-tag">Learn your deen from the classical books, made simple, a few minutes a day.</p>
    <ul class="ob-points"><li><b>The essentials, for everyone.</b> Belief, purification, prayer, fasting, zakat and the heart, in short lessons.</li>
      <li><b>The Course, for students of knowledge.</b> The classical books year by year, with lessons and flashcards.</li>
      <li><b>A library of complete books.</b> From the Tahawiyyah to Sahih al-Bukhari, free to read.</li></ul>
    <p class="w-hadith">The Prophet ﷺ said: “Whoever takes a path seeking knowledge, Allah makes easy for him a path to Paradise.” <span>Sahih Muslim</span></p>
    <button class="btn gold" id="ob-next">Continue</button>${dots}</div></div>`;
  if (OB.step === 2) return `<div class="welcome"><div class="welcome-in left"><button class="back" id="ob-back">${ICON.back} Back</button>
    <h1>Where would you like to start?</h1><p class="muted">You can change this later.</p>
    <div class="choices">
      <button class="choice" data-start="fard"><b>The essentials</b><span>Fard al-'Ayn: what every Muslim must know, in short lessons. The best place for most people.</span></button>
      <button class="choice" data-start="y1"><b>The Course</b><span>For students of knowledge: the classical books, starting from Year 1.</span></button>
      <button class="choice" data-start="place"><b>I've studied before</b><span>Take a placement test and start in a later year.</span></button></div>${dots}</div></div>`;
  return `<div class="welcome"><div class="welcome-in left"><button class="back" id="ob-back">${ICON.back} Back</button>
    <h1>How much time each day?</h1><p class="muted">This sets how many new flashcards you get. Lessons stay short either way.</p>
    <div class="choices">${[[5,"Light","About 10 minutes"],[10,"Steady","About 20 minutes"],[20,"Serious","About 40 minutes"]].map(([n,t,d]) => `<button class="choice ${S.newPerDay===n?"on":""}" data-pace="${n}"><b>${t}</b><span>${d}</span></button>`).join("")}</div>
    <label class="ob-name"><span>What should we call you? <em>Optional</em></span><input id="ob-name" autocomplete="given-name" maxlength="30" value="${esc(S.name||"")}"></label>
    <button class="btn gold" id="begin">Bismillah, let's begin</button>${dots}</div></div>`;
}
function bindWelcome(){
  const app = $("#app"), redraw = () => { app.innerHTML = welcomeView(); bindWelcome(); window.scrollTo(0,0); };
  const nx = $("#ob-next"); if (nx) nx.onclick = () => { OB.step = 2; redraw(); };
  const bk = $("#ob-back"); if (bk) bk.onclick = () => { OB.step--; redraw(); };
  app.querySelectorAll("[data-start]").forEach(b => b.onclick = () => { OB.start = b.dataset.start; OB.step = 3; redraw(); });
  app.querySelectorAll("[data-pace]").forEach(b => b.onclick = () => { S.newPerDay = +b.dataset.pace; app.querySelectorAll("[data-pace]").forEach(x => x.classList.toggle("on", x === b)); });
  const bg = $("#begin"); if (bg) bg.onclick = () => { const n = $("#ob-name").value.trim(); if (n) S.name = n; S.welcomed = true; S.start = OB.start || "y1"; save();
    if (S.start === "fard") { go({ name:"home" }); }
    else go({ name:"syllabus" }); };
}
let INSTALL = null; window.addEventListener("beforeinstallprompt", e => { e.preventDefault(); INSTALL = e; if (view.name === "home") render(); });
const standalone = () => matchMedia("(display-mode: standalone)").matches || navigator.standalone;
function installCard(){
  if (S.noInstall || standalone()) return ""; const ios = /iphone|ipad|ipod/i.test(navigator.userAgent);
  if (!INSTALL && !ios) return "";
  return `<section class="card install"><b>Put the app on your home screen</b><p class="small muted" style="margin:4px 0 10px">${INSTALL ? "It opens like an app and works offline for the pages you've visited." : "Tap the Share button in Safari, then “Add to Home Screen”."}</p>
    <div class="btnrow">${INSTALL?`<button class="btn small-btn" id="inst">Add to home screen</button>`:""}<button class="btn ghost small-btn" id="noinst">Not now</button></div></section>`;
}
/* ---- Home: hadith of the day ---- */
const DAILY = {};
async function hadithOfDay(){
  const d = new Date(), m = d.getMonth(); if (!DAILY[m]) { try { const r = await fetch(`data/daily/${m}.json`); DAILY[m] = await r.json(); } catch(e){ return null; } }
  return DAILY[m][(d.getDate()-1) % DAILY[m].length];
}
let QUOTES = null;
async function fillHome(){                    // the daily card: a hadith one day, a saying of the Awliya' the next
  const box = $("#hotd"); if (!box) return;
  const day = Math.floor((Date.now() - new Date().getTimezoneOffset()*60000) / 864e5);
  if (day % 2) {
    if (!QUOTES) { try { QUOTES = await fetch("data/quotes.json").then(r => r.json()); } catch(e){ QUOTES = []; } }
    const q = QUOTES.length && QUOTES[Math.floor(day/2) % QUOTES.length];
    if (q) { box.innerHTML = `<p class="label" style="margin-top:0">Wisdom of the day</p><p class="ar hotd-ar">${esc(q.ar)}</p><p class="hotd-en">${esc(q.en)}</p>
      <div class="small muted">${esc(q.by)}, ${esc(q.src)}</div>`; box.hidden = false; return; }
  }
  const h = await hadithOfDay();
  if (h) box.innerHTML = `<p class="label" style="margin-top:0">Hadith of the day</p><p class="hotd-en">${esc(h.e)}</p>
    <div class="spread small muted"><span>${esc(h.r)}, ${esc(h.c)}</span><button class="linkbtn" data-read="t_bukhari|${h.i}">Read in context</button></div>`, box.hidden = false, bindReadLinks(box);
}
function leftToday(){ const d = new Date(), m = (24*60) - (d.getHours()*60 + d.getMinutes()); return m >= 60 ? `${Math.floor(m/60)}h ${m%60}m` : `${m} min`; }
setInterval(() => { const el = document.getElementById("sk-left"); if (el) el.textContent = leftToday(); }, 30000);
function appBadge(){ try { if (!navigator.setAppBadge) return; const due = S.welcomed && S.lastDay !== today(); due ? navigator.setAppBadge(1) : navigator.clearAppBadge(); } catch(e){} }   // installed app icon shows a dot until today's study is done
function bindReadLinks(root){ root.querySelectorAll("[data-read]").forEach(b => b.onclick = () => { const [id, i] = b.dataset.read.split("|"); openRead(id, +i); }); }
/* ============================ LEARN: the Fard al-'Ayn for everyone ============================
   Short lessons in simple English, written from our books; everything is open. Data: data/learn.json */
let LEARN = null, LS = null;
const LEARN_DECK = { belief:"fard_aqeedah", purity:"fard_tahara", prayer:"fard_salah", fasting:"fard_sawm", zakat:"fard_zakat" };
async function loadLearn(){ if (LEARN) return LEARN; try { LEARN = await fetch("data/learn.json").then(r => r.json()); } catch(e){ LEARN = []; } return LEARN; }
const learnDone = id => !!(S.learn||{})[id];
function nextLearn(){ for (const u of LEARN||[]) for (let k = 0; k < u.lessons.length; k++) if (!learnDone(u.lessons[k].id)) return { u, k }; return null; }
function learnHome(){
  if (!LEARN) { loadLearn().then(() => { if (view.name === "home") render(); }); return `<p class="muted">Loading…</p>`; }
  const nx = nextLearn(), u = LEARN.find(x => x.id === S.topic) || (nx && nx.u) || LEARN[0];
  const d = u.lessons.filter(l => learnDone(l.id)).length, n = u.lessons.length, pct = Math.round(d / n * 100);
  const head = `<section class="card topic"><div class="topic-r"><span class="topic-t">${esc(u.title)}</span><button class="chip-btn" id="topic-change" aria-haspopup="dialog">Change</button></div>
    <div class="topic-p"><span class="bar"><i style="width:${Math.max(2, pct)}%;background:${u.color}"></i></span><span class="small muted">${pct}%</span></div></section>`;
  const card = (l, k) => { const ok = learnDone(l.id);
    return `<article class="lcard" style="--uc:${u.color}"><div class="lc-art" aria-hidden="true"><span class="ar">${esc(u.ar || "")}</span><span class="lc-n">${k+1} of ${n}</span></div>
      <div class="lc-body"><p class="lc-k">${esc(u.title)}</p><h3>${esc(l.title)}</h3><p class="lc-a">${esc(l.about || "")}</p></div>
      ${ok ? `<button class="lc-btn done" data-learn="${u.id}|${k}">${ICON.check.replace("<svg",'<svg width="16" height="16"')} Lesson complete<span class="small"> · go over it again</span></button>`
           : `<button class="lc-btn" data-learn="${u.id}|${k}">Start lesson</button>`}</article>`; };
  const deck = LEARN_DECK[u.id] && FARD_DECKS.find(x => x.id === LEARN_DECK[u.id]);
  return `${head}<div class="lcards" id="lcards" data-topic="${u.id}" aria-label="${esc(u.title)} lessons, swipe to see more">${u.lessons.map(card).join("")}</div>${deck ? `<div class="stack" style="margin-top:4px">${itemDeck(deck, true)}</div>` : ""}`;
}
function topicSheet(){
  const d = modal(`<h2 style="margin:4px 0 4px;text-align:center">Choose a topic</h2><p class="small muted" style="text-align:center;margin:0 0 14px">Every lesson is open. Switch whenever you like.</p>
    <div class="stack">${LEARN.map(u => { const dn = u.lessons.filter(l => learnDone(l.id)).length, on = (S.topic || (nextLearn()||{u:LEARN[0]}).u.id) === u.id;
      return `<button class="item topic-i ${on ? "on" : ""}" data-topic="${u.id}" style="--uc:${u.color}"><span style="flex:1;min-width:0"><span class="t">${esc(u.title)}</span><br><span class="s">${esc(u.sub)}</span></span><span class="small muted">${dn}/${u.lessons.length}</span></button>`; }).join("")}</div>
    <button class="btn ghost" id="topic-x" style="margin-top:14px">Close</button>`, (el, close) => {
      el.querySelectorAll("[data-topic]").forEach(b => b.onclick = () => { S.topic = b.dataset.topic; save(); close(); render(); });
      el.querySelector("#topic-x").onclick = close; el.onclick = e => { if (e.target === el) close(); }; });
  d.classList.add("sheet");
}
function fitLearnCards(){
  const c = $("#lcards"); if (!c || !LEARN) return; const u = LEARN.find(x => x.id === c.dataset.topic);
  const k = u.lessons.findIndex(l => !learnDone(l.id)); if (k > 0) c.scrollLeft = c.children[k].offsetLeft - 16;
  const ch = $("#topic-change"); if (ch) ch.onclick = topicSheet;
}
function unitView(id){
  const u = (LEARN||[]).find(x => x.id === id); if (!u) { loadLearn().then(render); return shell(`<p class="muted">Loading…</p>`); }
  const deck = LEARN_DECK[id] && FARD_DECKS.find(d => d.id === LEARN_DECK[id]);
  return shell(`<button class="back" data-go="home">${ICON.back} Home</button>
    <h1 style="margin-bottom:2px">${esc(u.title)}</h1><p class="muted" style="margin:0 0 16px">${esc(u.sub)}</p>
    <div class="stack">${u.lessons.map((l, k) => `<button class="item" data-learn="${u.id}|${k}"><span class="lnum" style="background:${u.color}">${learnDone(l.id) ? ICON.check.replace("<svg",'<svg width="14" height="14"') : k+1}</span>
      <span style="flex:1;min-width:0"><span class="t">${esc(l.title)}</span><br><span class="s">${l.cards.length} cards, ${l.checks.length} questions</span></span>${learnDone(l.id) ? `<span class="pill ok">Done</span>` : ""}</button>`).join("")}</div>
    ${deck ? `<p class="label">Keep it fresh</p>${itemDeck(deck, true)}` : ""}`);
}
function startLearn(uid, k){
  const u = LEARN.find(x => x.id === uid), l = u.lessons[k];
  const checks = shuffle(l.checks.map(c => ({ kind:"mcq", q:c.q, answer:c.a, why:c.why, options:shuffle([c.a, ...c.w]) })));
  LS = { u, k, l, steps:[...l.cards.map((c, j) => ({ kind:"card", c, j })), ...checks, { kind:"recap" }], i:0, sel:null, answered:false, right:0 };
  renderLearn();
}
function renderLearn(){
  const st = LS.steps[LS.i]; if (!st) return finishLearn();
  let body, foot;
  if (st.kind === "card") return renderSwipe(st.j);
  {
    if (st.kind === "recap") {
      const nxt = LS.u.lessons[LS.k + 1];
      body = `<div class="kicker">To recap</div><h2 style="margin:4px 0 12px">${esc(LS.l.title)}</h2>
        <ol class="recap">${LS.l.cards.map(c => `<li><b>${esc(c.t)}</b></li>`).join("")}</ol>
        ${nxt ? `<p class="muted" style="margin-top:16px">Next time: ${esc(nxt.title)}.</p>` : ""}`;
      foot = `<div class="pfoot"><button class="btn" id="next">Finish lesson</button></div>`;
    } else {
    const q = LS.steps.slice(0, LS.i).filter(x => x.kind === "mcq").length + 1, nq = LS.l.checks.length;
    body = `<div class="kicker">Question ${q} of ${nq}</div><p class="q" style="font-size:1.1rem">${esc(st.q)}</p>
      <div class="opts">${st.options.map((o, i) => { let cls = ""; if (LS.answered) { if (o === st.answer) cls = "right"; else if (i === LS.sel) cls = "wrong"; } else if (i === LS.sel) cls = "sel";
        return `<button class="opt ${cls}" data-o="${i}" ${LS.answered ? "disabled" : ""}>${esc(o)}</button>`; }).join("")}</div>`;
    if (!LS.answered) foot = `<div class="pfoot"><button class="btn" id="check" ${LS.sel === null ? "disabled" : ""}>Check answer</button></div>`;
    else { const ok = st.options[LS.sel] === st.answer;
      body += `<section class="explain-box ${ok ? "ok" : "bad"}" role="status"><p class="eb-h"><span>Explanation</span><span class="eb-tag">${ok ? ICON.check.replace("<svg",'<svg width="13" height="13"') + " Correct" : "✕ Incorrect"}</span></p>
        ${ok ? "" : `<p class="eb-a">The answer is: <b>${esc(st.answer)}</b></p>`}<p>${esc(st.why || "")}</p></section>`;
      foot = `<div class="pfoot"><button class="btn" id="next">Next</button></div>`; }
    }
  }
  $("#app").innerHTML = `<div class="player"><div class="player-in"><div class="phead"><button class="x" id="quit" aria-label="Leave lesson">${ICON.x}</button><div class="bar"><i style="width:${LS.i/LS.steps.length*100}%;background:${LS.u.color}"></i></div></div><div class="pbody">${body}</div>${foot}</div></div>`;
  document.querySelectorAll("[data-o]").forEach(x => x.onclick = () => { LS.sel = +x.dataset.o; renderLearn(); });
  const ck = $("#check"); if (ck) ck.onclick = () => { LS.answered = true; if (st.options[LS.sel] === st.answer) LS.right++; renderLearn(); };
  const eb = document.querySelector(".explain-box"); if (eb) eb.scrollIntoView({ block:"nearest", behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
  const nx = $("#next"); if (nx) nx.onclick = () => { LS.i++; LS.sel = null; LS.answered = false; renderLearn(); window.scrollTo(0,0); };
  $("#quit").onclick = () => confirmBox("Leave this lesson? It won't be marked as done.", () => { LS = null; go({ name:"home" }); });
}
// Lesson cards as a swipeable deck: swipe (or arrows / buttons) between cards; questions follow the last card
function renderSwipe(start){
  const cards = LS.l.cards, n = cards.length, steps = LS.steps.length;
  $("#app").innerHTML = `<div class="player"><div class="player-in"><div class="phead"><button class="x" id="quit" aria-label="Leave lesson">${ICON.x}</button><div class="bar"><i id="pbar" style="background:${LS.u.color}"></i></div></div>
    <div class="kicker swipe-k">${esc(LS.l.title)}</div>
    <div class="swipe" id="swipe" style="--uc:${LS.u.color}" tabindex="0" aria-roledescription="carousel" aria-label="Lesson cards, swipe to move between them">${cards.map((c, j) => `<article class="card learncard sw-card" aria-roledescription="slide" aria-label="Card ${j+1} of ${n}"><h2>${esc(c.t)}</h2><p>${esc(c.x)}</p><p class="src">From ${esc(c.src)}</p></article>`).join("")}</div>
    <div class="dots" aria-hidden="true">${cards.map(() => `<i></i>`).join("")}</div>
    <div class="pfoot swipe-foot"><button class="btn ghost" id="prev" aria-label="Previous card">${ICON.back}</button><button class="btn" id="next"></button></div></div></div>`;
  const sw = $("#swipe"), dots = [...document.querySelectorAll(".dots i")], prev = $("#prev"), next = $("#next"), bar = $("#pbar");
  const smooth = matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth";
  const at = () => { const c = sw.scrollLeft + sw.clientWidth / 2; let b = 0, bd = 1e9;
    [...sw.children].forEach((el, k) => { const d = Math.abs(el.offsetLeft + el.offsetWidth / 2 - c); if (d < bd) { bd = d; b = k; } }); return b; };
  const show = j => { LS.i = j; dots.forEach((d, k) => d.classList.toggle("on", k === j)); prev.disabled = j === 0;
    next.textContent = j === n - 1 ? "Check what you learnt" : "Next"; bar.style.width = j / steps * 100 + "%"; };
  const goTo = j => sw.children[j].scrollIntoView({ behavior:smooth, inline:"center", block:"nearest" });
  let t; sw.onscroll = () => { clearTimeout(t); t = setTimeout(() => show(Math.min(n - 1, Math.max(0, at()))), 60); };
  prev.onclick = () => goTo(Math.max(0, LS.i - 1));
  next.onclick = () => { if (LS.i < n - 1) goTo(LS.i + 1); else { LS.i = n; LS.sel = null; LS.answered = false; renderLearn(); } };
  sw.onkeydown = e => { if (e.key === "ArrowRight") { e.preventDefault(); next.onclick(); } if (e.key === "ArrowLeft") { e.preventDefault(); prev.onclick(); } };
  $("#quit").onclick = () => confirmBox("Leave this lesson? It won't be marked as done.", () => { LS = null; go({ name:"home" }); });
  show(start); if (start) sw.scrollLeft = sw.children[start].offsetLeft - (sw.clientWidth - sw.children[start].offsetWidth) / 2;
  sw.focus({ preventScroll:true });
}
function finishLearn(){
  const { u, k, l, right } = LS, first = !learnDone(l.id);
  S.learn = { ...(S.learn||{}), [l.id]: Date.now() }; const adv = touchDay(first ? 10 : 2); save();
  const next = u.lessons[k+1];
  $("#app").innerHTML = `<div class="player"><div class="player-in"><div class="done-screen"><h2>Lesson complete</h2><p class="muted">${esc(l.title)}</p>
    <div class="tiles"><div class="tile"><b>${Math.round(right / l.checks.length * 100)}%</b><span>Lesson score</span></div><div class="tile"><b>${S.streak}</b><span>Day streak</span></div></div></div>
    <div class="pfoot">${next ? `<button class="btn" id="nextl">Next: ${esc(next.title)}</button>` : ""}<button class="btn ${next ? "ghost" : ""}" id="cont">${next ? "Continue later" : "Done"}</button></div></div></div>`;
  if (adv) toast(`${S.streak} day streak! Keep going`);
  const nl = $("#nextl"); if (nl) nl.onclick = () => startLearn(u.id, k+1);
  $("#cont").onclick = () => { S.topic = u.id; save(); LS = null; go({ name:"home" }); };
}
function homeView(){
  const y = yearOf(Math.max(...S.unlocked.filter(n => loaded(yearOf(n))))), st = yearStatus(y);
  const nl = nextLesson(), decks = studyDecks(), due = decks.reduce((s,d) => s + deckStats(d).due, 0), cards = due + newAvail(decks);
  const inCourse = S.start === "y1" || S.start === "place" || Object.keys(S.books||{}).some(id => !bookById(id) || bookById(id).type !== "text");
  const course = inCourse && nl ? `<button class="card simple-row" data-startlesson="${nl.b.id}|${nl.i}"><span class="sr-ico">${ICON.learn}</span>
      <span style="flex:1;min-width:0"><b>Your Course: Year ${y.n}</b><span class="small muted" style="display:block">Next: ${esc(nameOf(nl.b))}, lesson ${nl.i+1}</span></span><span class="pill brand">Continue</span></button>`
    : `<button class="card simple-row" data-go="syllabus"><span class="sr-ico">${ICON.learn}</span><span style="flex:1"><b>Go deeper with the Course</b><span class="small muted" style="display:block">For students of knowledge: the classical books, year by year</span></span></button>`;
  const cardsRow = cards ? `<button class="card simple-row" data-study="all"><span class="sr-ico">${ICON.flame}</span>
      <span style="flex:1"><b>Flashcards</b><span class="small muted" style="display:block">${cards} to review, about ${Math.max(2, Math.round(cards*0.15))} min</span></span><span class="pill brand">Review</span></button>` : "";
  const last = S.lastRead && bookById(S.lastRead.id);
  const readRow = last ? `<button class="card simple-row" data-read="${last.id}|${S.lastRead.i}"><span class="libthumb">${cover(last, 30)}</span>
      <span style="flex:1;min-width:0"><b>Keep reading</b><span class="small muted" style="display:block">${esc(last.title)}</span></span><span class="pill">Read</span></button>` : "";
  const atRisk = S.streak > 0 && S.lastDay === today() - 1;            // studied yesterday, not yet today
  const streakCard = atRisk ? `<section class="streak-card" role="status"><span class="sk-ico">${ICON.flame.replace("<svg",'<svg width="26" height="26"')}</span>
      <span style="flex:1"><b id="sk-left">${leftToday()}</b><span class="small" style="display:block;opacity:.85">left today to keep your ${S.streak}-day streak</span></span></section>` : "";
  const signs = YEARS[0].books.find(b => b.id === "signs"), tj = FARD_DECKS.find(d => d.id === "tajwid"), ayy = bookById("t_ayyuha");
  const more = `<p class="label">More to explore</p><div class="stack">${tj ? itemDeck(tj, true) : ""}${signs ? itemBook(signs, true) : ""}
      ${ayy ? `<button class="item" data-read="t_ayyuha|0"><span class="libthumb">${cover(ayy, 34)}</span><span style="flex:1;min-width:0"><span class="t">Ayyuha al-Walad</span><br><span class="s">Imam al-Ghazali's رحمه الله letter of advice to a student</span></span><span class="pill">Read</span></button>` : ""}</div>`;
  return shell(`
    <section class="illum"><p class="ar illum-ar">السَّلَامُ عَلَيْكُمْ</p><p class="illum-en">Assalamu 'alaykum${S.name?`, ${esc(S.name)}`:""}</p></section>
    ${streakCard}
    ${learnHome()}
    <section class="card hotd" id="hotd" hidden></section>
    ${cardsRow}${course}${readRow}
    ${more}
    ${installCard()}`);
}
/* Optional course before Year 1: what every Muslim must know. Never required, never locks anything. */
/* Optional course before Year 1: what every Muslim must know. Never required, never locks anything.
   Its cards are taken from Umm al-Barahin, Nur al-Idah and Mukhtasar al-Quduri. */
const FARD_DECKS = [
  ["fard_aqeedah","Belief","What every Muslim must believe about Allah and His messengers ﷺ, from Umm al-Barahin","Aqeedah","#0E5A43","t_umm"],
  ["fard_tahara","Purification","Water, wudu, ghusl, tayammum and impurities, from Nur al-Idah","Fiqh","#2F6E8F","t_nur"],
  ["fard_salah","Prayer","The prayer: its conditions, pillars and what breaks it, from Nur al-Idah","Fiqh","#2F6E8F","t_nur"],
  ["fard_sawm","Fasting","Ramadan, what breaks the fast and making it up, from Nur al-Idah","Fiqh","#2F6E8F",""],
  ["fard_zakat","Zakat","Who pays zakat, on what, and how much, from Mukhtasar al-Quduri","Fiqh","#1F6F78",""],
  ["tajwid","Tajweed and the letters","Points of articulation, qualities, nun and mim, madd and stopping","Tajweed","#1E4D3B",""],
  ["history","Islamic history","From the Rightly Guided Caliphs to the Ottomans, question by question","History","#6B4E2E",""],
  ["fard_halal","Halal food and drink","Slaughter, hunting and what may be eaten and drunk, from Mukhtasar al-Quduri","Fiqh","#1F6F78",""],
].map(([id,title,sub,subject,color,read]) => ({ id, title, sub, subject, color, read, opt:true, fard:true, simple:true, glyph:"", year:1, get size(){ return (META.decks||{})[id]||0; } }));
const allDecks = () => [...YEARS.flatMap(y=>y.decks), ...FARD_DECKS];
const studyDecks = () => [...activeYears().flatMap(y=>y.decks), ...FARD_DECKS].filter(d => d.cards);
function historyCard(){                    // extra study, alongside any year: doesn't count towards passing
  const d = FARD_DECKS.find(x => x.id === "history"), books = ["t_qisas", "t_ibnhisham", "t_tarikh_khulafa"].map(bookById).filter(Boolean);
  return `<details class="module fard" ${S.openHist?"open":""} id="hist"><summary><span class="yr-badge" style="width:44px;height:44px;background:#6B4E2E;color:#fff">${ICON.shelf}</span>
      <span class="m-txt"><span class="t">Islamic history</span>
      <span class="s">Extra study for anyone who wants it, alongside any year.</span></span></summary>
    <div class="stack"><p class="sublabel">Questions and answers</p>${itemDeck(d, true)}
      <p class="sublabel">Books to read</p>${books.map(b => `<button class="item" data-read="${b.id}|0"><span class="libthumb">${cover(b, 34)}</span><span style="flex:1;min-width:0"><span class="t">${esc(b.title)}</span><br><span class="s">${esc(b.author)}</span></span><span class="pill">Read</span></button>`).join("")}</div></details>`;
}
function fardAynCard(){                     // Fard al-'Ayn: optional, for anyone who wants the essentials first
  const D = id => FARD_DECKS.find(d => d.id === id), signs = YEARS[0].books.find(b => b.id === "signs"), ayy = bookById("t_ayyuha");
  return `<details class="module fard" ${S.openFard?"open":""}><summary><span class="yr-badge" style="width:44px;height:44px">${ICON.check}</span>
      <span class="m-txt"><span class="t">Fard al-'Ayn</span>
      <span class="s">What every Muslim must know. Optional: start here, or go straight to Year 1.</span></span></summary>
    <div class="stack"><p class="sublabel">Tajweed and the letters</p>${itemDeck(D("tajwid"), true)}
      <p class="sublabel">Fiqh and Aqeedah</p>${FARD_DECKS.filter(d => d.id.startsWith("fard_")).map(d => itemDeck(d, true)).join("")}
      <div class="item soon"><span style="flex:1"><span class="kicker" style="margin:0">Coming soon</span><span class="t" style="display:block">Is'af al-Muridin</span></span></div>
      <p class="sublabel">Tasawwuf</p>${ayy ? `<button class="item" data-read="t_ayyuha|0"><span class="libthumb">${cover(ayy, 34)}</span><span style="flex:1"><span class="t">Ayyuha al-Walad</span><br><span class="s">Imam al-Ghazali's رحمه الله letter of advice to a student</span></span><span class="pill gold">Read</span></button>` : ""}
      <p class="sublabel">The End Times</p>${signs ? itemBook(signs, true) : ""}</div></details>`;
}
function syllabusView(){
  const N = Math.max(...S.unlocked), place = N <= YEARS.length && !(S.tests[N] && S.tests[N].passed);
  return shell(`<h1>Course</h1><p class="muted" style="margin:0 0 14px">For students of knowledge: the classical books, year by year. Each year opens when you have read the one before.</p>
    <div class="stack">${YEARS.map(yearCard).join("")}${specCard()}</div>
    <p class="label">Extra study</p>${historyCard()}
    ${place ? `<p class="label">Skip ahead</p><button class="card simple-row" data-place="${N}"><span style="flex:1"><b>Studied before?</b><span class="small muted" style="display:block">Take the Year ${N} test now. Pass it to skip ahead.</span></span><span class="pill">Test</span></button>` : ""}`);
}
function step3(n, title, sub, status, frac, done){ return `<div class="step3 ${done?"done":""}"><span class="s3n">${done?ICON.check.replace("<svg",'<svg width="13" height="13"'):n}</span><div class="s3b"><div class="spread"><b>${title}</b><span class="small muted">${status}</span></div>${sub?`<span class="s3s">${sub}</span>`:""}<div class="bar"><i style="width:${Math.min(100,frac*100)}%;${done?"background:var(--ok)":""}"></i></div></div></div>`; }
function gate(label, frac, done){ return `<div class="gate ${done?"done":""}"><span>${label}</span><div class="bar"><i style="width:${Math.min(100,frac*100)}%;${done?"background:var(--ok)":""}"></i></div></div>`; }
function yearCard(y){
  const open = S.unlocked.includes(y.n), st = yearStatus(y), cur = open && y.n === Math.max(...S.unlocked) && y.prepared;
  if (!cur) return `<button class="year row ${open?"":"locked"}" data-year="${y.n}"><span class="yr-badge">${y.n}</span><span style="flex:1;text-align:left"><b>Year ${y.n}</b><span class="small muted" style="display:block">${esc(y.title)}</span></span>
      ${open && y.prepared ? `<span class="pill ok">Done</span>` : open ? `<span class="pill">Soon</span>` : `<span class="lockic">${ICON.lock}</span>`}</button>`;
  return `<button class="year current" data-year="${y.n}">
    <div class="head"><span class="yr-badge">${y.n}</span><div style="flex:1"><h2>Year ${y.n}</h2><div class="small muted">${esc(y.title)}</div></div></div>
    <div class="steps3">${step3(1, "Lessons", "", `${st.ld} of ${st.lt}`, st.books, st.booksOk)}${step3(2, "Read the books", "", st.rt ? `${Math.round(st.reads*100)}% read` : "None this year", st.reads, st.readOk)}</div>
    <p class="small muted" style="margin:10px 0 0">${y.n < YEARS.length ? `Finish both to open Year ${y.n+1}.` : "Finish both to complete the course."} Flashcards and a practice test are there to help.</p>
    <span class="btn" style="margin-top:14px">Open Year ${y.n}</span></button>`;
}
function itemBook(b, open){
  const d = bookDone(b), L = lessonsOf(b);
  if (b.type === "text") return `<button class="item" ${open?`data-book="${b.id}"`:"disabled"}><span class="ico art-ico">${artFor(b,40)}</span>
    <span><span class="t">${esc(b.title)}</span><br><span class="s">${esc(b.sub)} · ${L} ${L>1?"sections":"section"}</span></span>
    ${!open?ICON.lock:d>=L?`<span class="pill ok">Read</span>`:`<span class="pill">${d?`${d}/${L}`:"Read"}</span>`}</button>`;
  return `<button class="item" ${open?`data-book="${b.id}"`:"disabled"}><span class="ico art-ico">${artFor(b,40)}</span>
    <span><span class="t">${esc(nameOf(b))}</span>${classicOf(b)}<span class="s">${b.type==="words" ? `${L} sets of ${b.per} words` : `${L} short lessons`}</span></span>
    ${!open?ICON.lock:d>=L?`<span class="pill ok">Done</span>`:`<span class="pill">${d}/${L}</span>`}</button>`;
}
function itemDeck(d, open){
  const s = deckStats(d), avail = s.due + Math.min(newLeft(d), s.nw);
  if (d.opt && !d.cards) return `<button class="item" ${open?`data-deck="${d.id}"`:"disabled"}><span class="ico art-ico">${artFor(d,40)}</span>
    <span><span class="t">${esc(nameOf(d))}</span>${classicOf(d)}<span class="s">${s.total.toLocaleString()} cards</span></span>
    ${open?(d.fard?`<span class="pill brand">Start</span>`:`<span class="pill">Optional</span>`):ICON.lock}</button>`;
  return `<button class="item" ${open?`data-deck="${d.id}"`:"disabled"}><span class="ico art-ico">${artFor(d,40)}</span>
    <span><span class="t">${esc(nameOf(d))}</span>${classicOf(d)}<span class="s">${s.total.toLocaleString()} cards${open && s.mastered?`, ${s.mastered.toLocaleString()} learnt`:""}</span>
    ${open?`<span class="bar" style="display:block;margin-top:6px"><i style="width:${s.mastered/s.total*100}%;background:${d.color}"></i></span>`:""}</span>
    ${!open?ICON.lock:avail?`<span class="pill brand">${avail} to study</span>`:`<span class="pill ok">Done today</span>`}${d.opt && !d.fard?`<span class="pill" style="margin-left:4px">Optional</span>`:""}</button>`;
}
function yearView(n){
  const y = yearOf(n), open = S.unlocked.includes(n) && loaded(y), st = yearStatus(y);
  const ord = s => MODULES.findIndex(m => m.name === s);
  const lessons = lessonBooks(y).sort((p,q) => ord(p.subject) - ord(q.subject));
  const reads = (y.read||[]).map(id => bookById(id)).filter(Boolean);
  const decks = core(y.decks).filter(d => !d.opt), extra = y.decks.filter(d => d.opt), ready = open ? decks.filter(d=>d.cards).reduce((s,d)=>s+deckStats(d).due,0) + newAvail(decks.filter(d=>d.cards)) : 0;
  const head = (k, t, sub, right) => `<div class="stephead"><span class="s3n">${k}</span><div style="flex:1"><h2>${t}</h2><p class="small muted">${sub}</p></div>${right||""}</div>`;
  const lessonRow = b => { const L = lessonsOf(b), d = bookDone(b); return `<button class="item" ${open?`data-book="${b.id}"`:"disabled"}><span class="ico art-ico">${artFor(b,36)}</span>
      <span style="flex:1;min-width:0"><span class="kicker" style="margin:0">${esc(b.subject)}</span><span class="t" style="display:block">${esc(nameOf(b))}</span></span>
      ${!open?ICON.lock:d>=L?`<span class="pill ok">Done</span>`:`<span class="pill">${d}/${L}</span>`}</button>`; };
  return shell(`<button class="back" data-go="syllabus">${ICON.back} Course</button>
    <h1 style="margin-bottom:4px">Year ${n}: ${esc(y.title)}</h1>
    ${open ? "" : `<div class="notice">${ICON.lock}<span>Pass the Year ${n-1} final test to open this year.</span></div>`}
    ${open && !y.prepared ? `<div class="notice"><span>The books for Year ${n} are still being prepared.</span></div>` : ""}
    <section class="stepsec">${head(1, "Lessons", "Short lessons from this year's books.", `<span class="small muted">${st.ld} of ${st.lt}</span>`)}
      <div class="stack">${lessons.length ? lessons.map(lessonRow).join("") : `<p class="small muted" style="margin:0">No short lessons this year.</p>`}</div></section>
    <section class="stepsec">${head(2, "Read the books", "Read each one to the end, or mark it finished from its page.", `<span class="small muted">${st.rt ? Math.round(st.reads*100) + "%" : ""}</span>`)}
      ${reads.length ? `<div class="stack">${reads.map(b => { const L = lessonsOf(b), d = bookDone(b), nxt = Math.min(d, L-1);
        return `<button class="item" ${open?`data-read="${b.id}|${S.lastRead && S.lastRead.id === b.id ? S.lastRead.i : nxt}"`:"disabled"}><span class="libthumb">${cover(b, 34)}</span>
        <span style="flex:1;min-width:0"><span class="kicker" style="margin:0">${esc(b.subject)}</span><span class="t" style="display:block">${esc(b.title)}</span></span>${!open?ICON.lock:d>=L?`<span class="pill ok">Read</span>`:`<span class="pill">${Math.round(d/L*100)}%</span>`}</button>`; }).join("")}</div>` : `<p class="small muted" style="margin:0">No books to read this year.</p>`}
      ${(y.coming||[]).length ? `<p class="sublabel">Coming soon</p><div class="stack">${y.coming.map(([t,s]) => `<div class="item soon"><span style="flex:1;min-width:0"><span class="kicker" style="margin:0">${esc(s)}</span><span class="t" style="display:block">${esc(t)}</span></span></div>`).join("")}</div>` : ""}</section>
    <p class="small muted" style="margin:14px 2px 0">${n < YEARS.length ? `When steps 1 and 2 are done, Year ${n+1} opens.` : "When steps 1 and 2 are done, the course is complete."}</p>
    <p class="label" style="margin-top:26px">Practice (optional)</p>
    <section class="stepsec" style="margin-top:6px"><div class="stephead"><div style="flex:1"><h2>Flashcards</h2><p class="small muted">Questions from this year's books. Review a few each day.</p></div><span class="small muted">${st.cm.toLocaleString()} of ${st.ct.toLocaleString()}</span></div>
      ${open ? `<button class="btn" data-study="all" ${ready?"":"disabled"}>${ready ? `Review flashcards (${ready})` : "All done for today"}</button>` : ""}
      <details class="more"><summary>See all flashcard sets</summary><div class="stack" style="margin-top:8px">${decks.map(d => itemDeck(d, open)).join("")}
        ${extra.length ? `<p class="sublabel">Extra (optional)</p>${extra.map(d => itemDeck(d, open)).join("")}` : ""}</div></details></section>
    <section class="stepsec"><div class="stephead"><div style="flex:1"><h2>Practice test</h2><p class="small muted">${TEST_LEN} questions from this year, to see how much has stayed with you.</p></div></div>
      ${st.best!==null?`<p class="small muted" style="margin:0 0 10px">Best so far: <b>${pct(st.best)}</b></p>`:""}
      <button class="btn ghost" data-test="${n}" ${open?"":"disabled"}>${st.best!==null?"Try it again":"Take the practice test"}</button></section>
`);
}
function bookView(id){
  const b = YEARS.flatMap(y=>y.books).find(x=>x.id===id); if (b.type === "text") return textView(b);
  const L = lessonsOf(b), done = S.books[id]||[];
  const nextIdx = [...Array(L).keys()].find(i => !done.includes(i));
  const items = [...Array(L).keys()].map(i => {
    const first = b.lines[i*b.per], isDone = done.includes(i), locked = !isDone && i !== nextIdx;
    const label = b.type === "hadith" ? `<span class="t" style="display:block">${esc(snip(first.en, 70))}</span>` : `<span class="t ar" style="display:block;font-weight:700;font-size:1.1rem">${esc(snip(first.ar, 48))}</span>`;
    return `<button class="item" data-lesson="${i}" ${locked?'disabled style="opacity:.55"':""}>
      <span class="ico" style="background:${isDone?"var(--ok)":locked?"var(--line)":b.color};font-family:var(--body);font-size:1rem;font-weight:800">${isDone?ICON.check.replace("<svg",'<svg width="20" height="20"'):i+1}</span>
      <span>${label}<span class="s">Lesson ${i+1} · ${Math.min(b.per, b.lines.length-i*b.per)} ${b.type==="hadith"?"hadith":"lines"}</span></span>
      ${locked?ICON.lock:isDone?`<span class="pill ok">Review</span>`:`<span class="pill gold">Next</span>`}</button>`; }).join("");
  return shell(`<button class="back" data-year="${b.year}">${ICON.back} Year ${b.year}</button>
    <section class="hero" style="--c:${b.color}"><div class="hero-art">${art(ART_OF[b.id]||"star",b.color,84)}</div><h1>${esc(b.title)}</h1><p>${esc(b.sub)}. ${b.type==="hadith"?"Read each hadith in Arabic and English, then check what you remember.":"Read each line in Arabic and English, then check your understanding."}</p></section>
    <p class="label">${done.length} of ${L} lessons done</p><div class="stack">${items}</div>`);
}
function profileView(){
  const ret = retention(), seen = Object.keys(S.cards).length, cy = Math.max(...S.unlocked), th = S.theme || "auto";
  const row = (id, label, hint, control) => `<div class="setrow"><label for="${id}"><b>${label}</b>${hint?`<span>${hint}</span>`:""}</label>${control}</div>`;
  const toggle = (id, on) => `<input type="checkbox" class="switch" id="${id}" ${on?"checked":""}>`;
  return shell(`<h1>Progress</h1>
    <div class="tiles" style="max-width:none;margin-top:12px"><div class="tile"><b>${S.streak}</b><span>Day streak</span></div><div class="tile"><b>${S.xp}</b><span>Total XP</span></div>
    <div class="tile"><b>${seen.toLocaleString()}</b><span>Cards started</span></div><div class="tile"><b>${ret===null?"–":pct(ret)}</b><span>Recall rate</span></div></div>
    ${weekStrip()}
    <section class="card lb" id="lb" hidden></section>
    <button class="card simple-row" data-go="settings"><span class="sr-ico">${ICON.gear}</span><span style="flex:1"><b>Settings</b><span class="small muted" style="display:block">Appearance, reminders, offline, listening</span></span></button>`);
}
function settingsView(){
  const ret = retention(), seen = Object.keys(S.cards).length, cy = Math.max(...S.unlocked), th = S.theme || "auto";
  const row = (id, label, hint, control) => `<div class="setrow"><label for="${id}"><b>${label}</b>${hint?`<span>${hint}</span>`:""}</label>${control}</div>`;
  const toggle = (id, on) => `<input type="checkbox" class="switch" id="${id}" ${on?"checked":""}>`;
  return shell(`<button class="back" data-go="profile">${ICON.back} Progress</button><h1>Settings</h1>
    <p class="label">Appearance</p>
    <div class="seg" role="radiogroup" aria-label="Appearance">${[["auto","Automatic"],["light","Light"],["dark","Dark"]].map(([k,l]) => `<button role="radio" aria-checked="${th===k}" class="${th===k?"on":""}" data-theme="${k}">${l}</button>`).join("")}</div>
    <p class="label">Study</p>
    <div class="setlist">
      ${row("remind","Streak reminder","A notification at 8pm if you haven't studied yet that day", toggle("remind", !!S.remind))}
      ${row("hk","Show harakat","Qur'anic text always keeps its harakat", toggle("hk", S.harakat!==false))}
      ${row("clang","Question and answer language","Applies to every Q&A deck. More languages are planned", `<select id="clang"><option value="" ${!S.cardLang?"selected":""}>As written</option><option value="en" ${S.cardLang==="en"?"selected":""}>English</option><option value="ar" ${S.cardLang==="ar"?"selected":""}>العربية</option></select>`)}
      ${row("npd","New flashcards a day","Across all subjects", `<select id="npd">${[5,10,15,20,30,50].map(n=>`<option ${n===S.newPerDay?"selected":""}>${n}</option>`).join("")}</select>`)}
      ${row("tl","Pronunciation guide","English letters under new Arabic words, e.g. kitāb", `<select id="tl">${[["y1","Year 1 only"],["on","Always"],["off","Off"]].map(([v,t]) => `<option value="${v}" ${(S.translit||"y1")===v?"selected":""}>${t}</option>`).join("")}</select>`)}
      ${row("madhab","Madhab","Other madhabs are coming", `<select id="madhab"><option selected>Hanafi</option><option disabled>Maliki</option><option disabled>Shafi'i</option><option disabled>Hanbali</option></select>`)}
    </div>
    <p class="label">Use without internet</p>
    <div class="setlist"><p class="small muted" style="margin:4px 2px 10px">Anything you open is kept on this phone. Save a whole year to study with no connection.</p>
      ${S.unlocked.filter(n => n <= YEARS.length).map(n => row(`off-${n}`, `Year ${n}: ${esc(yearOf(n).title)}`, `<span id="offst-${n}">${(S.offline||{})[n] ? `Saved ${new Date(S.offline[n]).toLocaleDateString()}` : "Not saved yet"}</span>`, `<button class="btn ghost small-btn" id="off-${n}" data-off="${n}" style="width:auto">${(S.offline||{})[n] ? "Update" : "Save"}</button>`)).join("")}</div>
    <details class="setgroup"><summary>Listening</summary><div class="setlist">
      ${row("arvoice","Read Arabic with the device voice","Recorded narration is always used when a book has it", toggle("arvoice", S.arVoice!==false))}
      ${["en","ar"].map(l => row(`v-${l}`, l==="en"?"English voice":"Arabic voice", "", `<span style="display:flex;gap:6px;min-width:0;flex:1;justify-content:flex-end"><select id="v-${l}" style="max-width:150px">${voicesFor(l).length ? voicesFor(l).map(v => `<option ${voiceFor(l)&&voiceFor(l).name===v.name?"selected":""}>${esc(v.name)}</option>`).join("") : `<option>None found</option>`}</select><button class="tool" data-vtest="${l}" aria-label="Test voice">${ICON.play}</button></span>`)).join("")}
      <p class="small muted" style="margin:8px 2px 0">Better voices on iPhone: Settings → Accessibility → Spoken Content → Voices, and download one marked “Enhanced” or “Premium”.</p></div></details>
    <details class="setgroup"><summary>Your reports${(S.reports||[]).some(r=>!r.sent)?` <span class="pill gold">${S.reports.filter(r=>!r.sent).length} unsent</span>`:""}</summary><div class="card small" style="margin-top:8px">${(S.reports||[]).length ? `${S.reports.slice(-5).reverse().map(r=>{ const it=itemByKey(r.k); return `<div class="spread" style="padding:4px 0;border-bottom:1px solid var(--line)"><span>${esc(it?it.src.title:r.k)}: ${esc(r.why)}</span><span class="pill ${r.sent?"ok":"gold"}">${r.sent?"Sent":"Not sent"}</span></div>`; }).join("")}
      ${S.reports.some(r=>!r.sent)?`<button class="btn ghost" id="sendall" style="margin-top:10px">Send unsent reports</button>`:""}` : `<p style="margin:0" class="muted">Spotted a mistake? Tap ${ICON.flag.replace("<svg",'<svg width="14" height="14" style="vertical-align:-2px"')} Report on any card, line or hadith.</p>`}</div></details>
    <details class="setgroup"><summary>About the app</summary><div class="card small" style="margin-top:8px"><p style="margin-top:0">Dār aṣ-Ṣiddīq al-Akbar teaches the Fard al-'Ayn to everyone in simple lessons, and trains students year by year through the classical texts: Hanafi fiqh, Ash'ari and Maturidi creed, tasawwuf open to all the turuq, and the Arabic of the Qur'an.</p>
      <p style="margin-bottom:0">Flashcards are adapted from shared Anki decks; Qur'an word frequencies come from the Quranic Arabic Corpus; full Arabic texts come from the OpenITI corpus. Anything marked <span class="pill gold">AI · needs review</span> awaits a teacher's check.</p></div></details>
    <details class="setgroup"><summary>Advanced</summary><div class="setlist">
      ${row("advgrades","Advanced grading","Four buttons (Again, Hard, Good, Easy) instead of Got it / Redo", toggle("advgrades", !!S.advancedGrades))}</div>
      ${S.dev ? `<div class="card small" style="margin-top:8px"><b>Testing tools</b><p class="muted" style="margin:2px 0 8px">Only shown in testing mode.</p>
      <div class="btnrow"><button class="btn ghost" id="skipday">Skip to tomorrow</button><button class="btn ghost" id="fasttrack">Fast-track Year ${cy}</button></div></div>` : ""}
      <div class="btnrow" style="margin-top:8px"><button class="btn ghost" id="reset">Reset all progress</button></div></details>`);
}

function streakBurst(){ return `<div class="burst">${ICON.flame.replace('<svg','<svg width="34" height="34"')}<div><b>${S.streak} day streak!</b><span>${S.streak===1?"A new streak begins, bismillah.":"Keep going, may Allah put barakah in it."}</span></div></div>`; }
/* ---- Search across everything loaded, Arabic diacritics ignored ---- */
const norm = s => String(s||"").normalize("NFKD").replace(/[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0640]/g,"").replace(/[أإآٱ]/g,"ا").replace(/ى/g,"ي").replace(/ة/g,"ه").replace(/[\u0300-\u036f]/g,"").toLowerCase();
let INDEX = null;
function buildIndex(){
  INDEX = [];
  for (const y of YEARS){ if (!loaded(y)) { for (const b of y.books.filter(b => b.type === "text" && TEXTS[b.file])) TEXTS[b.file].sections.forEach((s,i) => s.p && INDEX.push({ y:y.n, src:b, kind:"sec", i, a:(s.v||s.p).join(" "), e:s.he||s.h, k:norm(s.h+" "+(s.he||"")+" "+s.p.join(" ")+" "+(s.en||[]).join(" ")) })); continue; }
    for (const b of y.books.filter(b => b.type !== "text")) (b.lines||[]).forEach((l,i) => INDEX.push({ y:y.n, src:b, kind:"line", i, a:l.ar, e:l.en, n:l.note||"", k:norm(l.ar+" "+l.en+" "+(l.note||"")) }));
    for (const b of y.books.filter(b => b.type === "text" && TEXTS[b.file])) TEXTS[b.file].sections.forEach((s,i) => s.p && INDEX.push({ y:y.n, src:b, kind:"sec", i, a:(s.v||s.p).join(" "), e:s.he||s.h, k:norm(s.h+" "+(s.he||"")+" "+s.p.join(" ")+" "+(s.en||[]).join(" ")) }));
    for (const d of y.decks) (d.cards||[]).forEach(c => INDEX.push({ y:y.n, src:d, kind:"card", c, a:c.fa?c.f:(c.ba?c.b:""), e:(c.fa?"":c.f)+" — "+(c.ba?"":c.b), k:norm(c.f+" "+c.b+" "+(c.s||"")) }));
  }
}
function searchResults(q){
  const n = norm(q).trim(); if (n.length < 2) return savedList();
  if (!INDEX) buildIndex();
  const words = n.split(/\s+/), hits = INDEX.filter(x => words.every(w => x.k.includes(w))).slice(0, 60);
  if (!hits.length) return `<p class="muted">No matches for “${esc(q)}”.</p>`;
  return `<p class="label">${hits.length===60?"First 60":hits.length} results</p><div class="stack">${hits.map((h,j)=>`<button class="item" data-hit="${j}"><span class="ico art-ico">${artFor(h.src,36)}</span><span style="min-width:0">${h.a?`<span class="t ar" style="display:block;font-size:1.1rem">${esc(snip(h.a,70))}</span>`:""}<span class="s" style="display:block">${esc(snip(h.e.replace(/^ — /,""),110))}</span><span class="s">${esc(h.src.title)} · Year ${h.y}</span></span></button>`).join("")}</div>`;
}
function savedList(){
  const items = (S.saved||[]).map(k => ({ k, it:itemByKey(k) })).filter(x => x.it && x.it.kind !== "sec");
  const secs = (S.saved||[]).map(k => ({ k, it:itemByKey(k) })).filter(x => x.it && x.it.kind === "sec");
  return `<p class="muted small">Type at least two letters, in English or Arabic. Searches every book and flashcard in the years you have opened.</p>
    <p class="label">${ICON.saved.replace("<svg",'<svg width="14" height="14" style="vertical-align:-2px"')} Saved (${items.length})</p>
    ${savedSecs() ? `<div class="stack" style="margin-bottom:8px">${savedSecs()}</div>` : ""}
    ${items.length ? `<div class="stack">${items.map(({k,it})=>{ const a = it.kind==="card" ? (it.c.fa?it.c.f:it.c.ba?it.c.b:"") : it.l.ar||"", e = it.kind==="card" ? (it.c.fa?"":it.c.f) : it.l.en;
      return `<button class="item" data-open="${esc(k)}"><span class="ico art-ico">${artFor(it.src,36)}</span><span style="min-width:0">${a?`<span class="t ar" style="display:block;font-size:1.1rem">${esc(snip(a,70))}</span>`:""}<span class="s" style="display:block">${esc(snip(e||"",110))}</span><span class="s">${esc(it.src.title)} · Year ${it.y}</span></span></button>`; }).join("")}</div>`
    : secs.length ? "" : `<div class="card small muted">Tap ${ICON.save.replace("<svg",'<svg width="14" height="14" style="vertical-align:-2px"')} Save on any flashcard, line or hadith to keep it here.</div>`}`;
}
function savedSecs(){ return (S.saved||[]).map(k => ({ k, it:itemByKey(k) })).filter(x => x.it && x.it.kind === "sec")
  .map(({k,it}) => `<button class="item" data-read="${it.src.id}|${it.i}"><span class="ico art-ico">${artFor(it.src,36)}</span><span><span class="t">${esc(it.src.title)}</span><br><span class="s">Section ${it.i+1}${it.s?` · ${esc(it.s.he||it.s.h)}`:""}</span></span></button>`).join(""); }
function openItem(k){
  const it = itemByKey(k); if (!it) return;
  const body = it.kind === "card" ? cardFront(it.c, it.src) + cardBack(it.c)
    : `<div class="kicker">${esc(it.src.title)}</div>${it.l.ar?`<p class="line-ar">${esc(it.l.ar)}</p>`:""}<p>${esc(it.l.en)}</p>${it.l.note?`<div class="small muted">${points(it.l.note)}</div>`:""}`;
  modal(`<div style="max-height:62vh;overflow:auto">${body}</div>${toolRow(k,false)}<div class="btnrow" style="margin-top:12px"><button class="btn" id="mok">Close</button></div>`, (d,c) => {
    d.querySelector("#mok").onclick = c;
    d.querySelectorAll("[data-save]").forEach(b => b.onclick = () => { toggleSave(k); c(); if (view.name === "search") render(); });
    d.querySelectorAll("[data-report]").forEach(b => b.onclick = () => { c(); openReport(k); }); });
}
let HITS = [];
function bindResults(){
  const q = norm(($("#sq")||{}).value||"").trim(); if (!INDEX) buildIndex(); const words = q.split(/\s+/);
  HITS = q.length < 2 ? [] : INDEX.filter(x => words.every(w => x.k.includes(w))).slice(0, 60);
  document.querySelectorAll("[data-open]").forEach(b => b.onclick = () => openItem(b.dataset.open));
  document.querySelectorAll("[data-hit]").forEach(b => b.onclick = () => { const h = HITS[+b.dataset.hit];
    if (h.kind === "sec") return openRead(h.src.id, h.i);
    if (h.kind === "card") return openItem(keyCard(h.c)); if (h.src.lines) return openItem(keyLine(h.src, h.src.lines[h.i]));
    const body = h.kind === "card" ? cardFront(h.c, h.src) + cardBack(h.c)
      : `<div class="kicker">${esc(h.src.title)}</div>${h.a?`<p class="line-ar">${esc(h.a)}</p>`:""}<p>${esc(h.e)}</p>${h.n?`<div class="small muted">${points(h.n)}</div>`:""}`;
    modal(`<div style="max-height:70vh;overflow:auto">${body}</div><div class="btnrow" style="margin-top:12px"><button class="btn" id="mok">Close</button></div>`, (d,c)=>d.querySelector("#mok").onclick=c); });
}
function searchView(){
  return shell(`<h1>Search</h1><p class="muted" style="margin:0 0 12px">Find any line, hadith or flashcard you have unlocked.</p>
    <input id="sq" class="search" type="search" placeholder="e.g. wudu, Dajjal, رحمة" value="${esc(view.q||"")}" autocomplete="off" aria-label="Search">
    ${LIB().every(b => TEXTS[b.file]) ? "" : `<button class="btn ghost" id="loadall" style="margin-top:10px">Also search the full books in the Library</button>`}
    <div id="sres" style="margin-top:12px">${searchResults(view.q||"")}</div>`);
}

/* ---- Library: every full text, open to all ---- */
const LIB = () => YEARS.flatMap(y => y.books.filter(b => b.type === "text"));
const hasAr = t => /[\u0621-\u064A]/.test(t||"");
/* Book covers: original designs drawn in SVG (cloth colour by subject, gold frame, arch panel, Arabic title, author) */
const CLOTH = { History:"#4A3423", Aqeedah:"#14463A", Fiqh:"#1D3557", Hadith:"#5E1F2B", Arabic:"#5B3418", Tafsir:"#0F4A52", Seerah:"#4A2444", "Usul al-Fiqh":"#2E3B4E", Tasawwuf:"#3B4520", "Signs of the Hour":"#4B2323", "Comparative Aqeedah":"#3A2F55", Mantiq:"#3D3D55", Tajweed:"#1E4D3B" };
let COVER_N = 0;
function wrapAr(t, max){ const w = t.split(" "), out = [""]; for (const x of w){ const l = out[out.length-1]; if (l && (l+" "+x).length > max) out.push(x); else out[out.length-1] = l ? l+" "+x : x; } return out; }
function cover(b, w=120){
  const id = "cv" + (++COVER_N), base = CLOTH[b.subject] || "#2B3A4A", gold = "#E2C27A", h = Math.round(w*1.45);
  const hash = [...b.id].reduce((s,c)=>s+c.charCodeAt(0),0), pat = hash % 3;
  const tl = wrapAr(b.ar || b.title, 11), fs = tl.length === 1 ? (tl[0].length > 8 ? 24 : 30) : tl.length === 2 ? 21 : 17, y0 = 132 - (tl.length-1)*fs*0.62;
  const al = wrapAr(b.authorAr || "", 20).slice(0,2);
  const motif = pat === 0 ? `<path d="M12 2l3 7 7 3-7 3-3 7-3-7-7-3 7-3z" fill="none" stroke="${gold}" stroke-width=".7"/>`
    : pat === 1 ? `<rect x="6" y="6" width="12" height="12" transform="rotate(45 12 12)" fill="none" stroke="${gold}" stroke-width=".7"/><circle cx="12" cy="12" r="2" fill="${gold}"/>`
    : `<path d="M0 12h24M12 0v24" stroke="${gold}" stroke-width=".5"/><circle cx="12" cy="12" r="5" fill="none" stroke="${gold}" stroke-width=".7"/>`;
  return `<svg class="cover" viewBox="0 0 200 290" width="${w}" height="${h}" role="img" aria-label="${esc(b.title)}">
    <defs><pattern id="${id}p" width="24" height="24" patternUnits="userSpaceOnUse">${motif}</pattern>
      <linearGradient id="${id}g" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".38"/><stop offset=".07" stop-color="#000" stop-opacity=".05"/><stop offset=".09" stop-color="#fff" stop-opacity=".06"/><stop offset=".2" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient></defs>
    <rect width="200" height="290" rx="5" fill="${base}"/><rect width="200" height="290" fill="url(#${id}p)" opacity=".16"/>
    <rect x="24" y="14" width="164" height="262" fill="none" stroke="${gold}" stroke-width="1.6"/><rect x="29" y="19" width="154" height="252" fill="none" stroke="${gold}" stroke-width=".6"/>
    <path d="M44 236V100Q44 52 106 40Q168 52 168 100V236Z" fill="#000" fill-opacity=".22" stroke="${gold}" stroke-width="1.2"/>
    <path d="M106 54l4 8 8 4-8 4-4 8-4-8-8-4 8-4z" fill="${gold}"/>
    ${tl.map((l,k)=>`<text x="106" y="${y0+k*fs*1.25}" text-anchor="middle" font-family="Amiri, serif" font-weight="700" font-size="${fs}" fill="${gold}" direction="rtl">${esc(l)}</text>`).join("")}
    <path d="M78 ${y0+(tl.length-1)*fs*1.25+16}h56" stroke="${gold}" stroke-width=".8"/><circle cx="106" cy="${y0+(tl.length-1)*fs*1.25+16}" r="2.4" fill="${gold}"/>
    ${al.map((l,k)=>`<text x="106" y="${206+k*16}" text-anchor="middle" font-family="Amiri, serif" font-size="12.5" fill="${gold}" fill-opacity=".9" direction="rtl">${esc(l)}</text>`).join("")}
    <circle cx="35" cy="25" r="2" fill="${gold}"/><circle cx="177" cy="25" r="2" fill="${gold}"/><circle cx="35" cy="265" r="2" fill="${gold}"/><circle cx="177" cy="265" r="2" fill="${gold}"/>
    <rect width="200" height="290" rx="5" fill="url(#${id}g)"/></svg>`;
}
const byline = b => `${esc(b.author)}${b.honor?` <span class="ar">${b.honor}</span>`:""}`;
const hasEn = b => (META.textsEn||{})[b.file];
function bookCard(b){
  const d = bookDone(b), L = lessonsOf(b);
  return `<button class="bookcard" data-book="${b.id}"><span class="cv">${cover(b, 140)}${d?`<span class="cvbar"><i style="width:${Math.max(4,d/L*100)}%"></i></span>`:""}</span>
    <span class="bt">${esc(b.title)}</span><span class="ba">${esc(b.author.replace(/^Imams? /,""))}</span>
    <span class="bl">${hasEn(b)?"Arabic and English":"Arabic"}${(META.textsAudio||{})[b.file]?"":""}</span></button>`;
}
const LIB_SUBJECTS = ["Aqeedah","Fiqh","Usul al-Fiqh","Tasawwuf","Hadith","Tafsir","Tajweed","Seerah","History","Signs of the Hour","Arabic"];
const libSubject = b => b.subject === "Comparative Aqeedah" ? "Aqeedah" : b.subject;
function libraryView(){
  const books = LIB(), last = S.lastRead && bookById(S.lastRead.id), f = LIB_SUBJECTS.includes(S.libSub) ? S.libSub : "";
  const cont = last ? `<section class="continue lib-cont"><span class="cv">${cover(last, 74)}</span><span style="flex:1;min-width:0"><span class="kicker" style="margin:0">Continue reading</span><b style="display:block">${esc(last.title)}</b>
      <span class="small muted">Section ${S.lastRead.i+1} of ${lessonsOf(last)}</span></span><button class="btn small-btn" data-read="${last.id}|${S.lastRead.i}">Read</button></section>` : "";
  const chips = `<div class="ychips" role="group" aria-label="Subject">${["", ...LIB_SUBJECTS].map(x => `<button class="ychip ${f===x?"on":""}" data-libsub="${x}" aria-pressed="${f===x}">${x||"All"}</button>`).join("")}</div>`;
  const shelves = LIB_SUBJECTS.filter(x => !f || x === f).map(x => { const bs = books.filter(b => libSubject(b) === x).sort((a, c) => a.year - c.year);
    return !bs.length ? "" : f ? `<p class="label">${esc(x)} <span class="muted small">${bs.length} books</span></p><div class="shelf">${bs.map(bookCard).join("")}</div>`
      : `<div class="shelf-h"><p class="label">${esc(x)}</p><button class="linkbtn" data-libsub="${esc(x)}">See all ${bs.length}</button></div><div class="shelf row">${bs.map(bookCard).join("")}</div>`; }).join("");
  return shell(`<h1>Library</h1><p class="muted" style="margin:0 0 12px">${books.length} complete books, from the first texts to Sahih al-Bukhari. Free to read, bab by bab.</p>
    ${cont}${chips}${shelves}
    <p class="small muted" style="margin-top:18px">Arabic texts from the OpenITI corpus. Harakat and English marked “Awaiting a teacher's check” are waiting for a teacher's check.</p>`);
}
/* ---- Full-text reader ---- */
function textView(b){
  const T = TEXTS[b.file], done = S.books[b.id]||[];
  if (!T) return shell(`<p class="muted">Loading…</p>`);
  const n = T.sections.length, next = T.sections.findIndex((_,i) => !done.includes(i));
  const row = (s,i) => `<button class="item toc" data-read="${b.id}|${i}"><span class="num ${done.includes(i)?"on":""}">${done.includes(i)?ICON.check.replace("<svg",'<svg width="14" height="14"'):i+1}</span>
      <span style="min-width:0;flex:1"><span class="t ${hasAr(s.h)?"ar":""}" style="display:block">${esc(snip(s.h,70))}</span>${s.he?`<span class="s" style="display:block">${esc(s.he)}</span>`:""}</span></button>`;
  let toc;
  const groups = []; T.sections.forEach((s,i) => { const p = s.parent || s.h; if (!groups.length || groups[groups.length-1].p !== p) groups.push({ p, is:[] }); groups[groups.length-1].is.push(i); });
  if (n > 60 && groups.length > n/2) { groups.length = 0; for (let k = 0; k < n; k += 50) groups.push({ p:`Sections ${k+1}–${Math.min(n, k+50)}`, is:[...Array(Math.min(50, n-k)).keys()].map(j => k+j) }); }
  if (n > 30 && groups.length > 1 && groups.length < n) toc = groups.map(g => { if (g.is.length === 1) return `<div class="stack" style="margin-bottom:8px">${row(T.sections[g.is[0]], g.is[0])}</div>`; const read = g.is.filter(i => done.includes(i)).length, here = g.is.includes(next);
      return `<details class="kitab" ${here?"open":""}><summary><span class="${hasAr(g.p)?"ar":""}" style="flex:1">${esc(snip(g.p,60))}</span><span class="small muted">${read?`${read}/`:""}${g.is.length}</span></summary><div class="stack">${g.is.map(i => row(T.sections[i], i)).join("")}</div></details>`; }).join("");
  else toc = `<div class="stack">${T.sections.map(row).join("")}</div>`;
  return shell(`<button class="back" data-go="library">${ICON.back} Library</button>
    <section class="bookhead"><span class="cv">${cover(b, 128)}</span><div style="min-width:0">
      <h1>${esc(b.title)}</h1><p class="ar booktitle-ar">${esc(b.ar||"")}</p>
      <p class="byline">${byline(b)}</p><p class="small muted" style="margin:0">${esc(b.when||"")}</p></div></section>
    <p style="margin:12px 0 8px">${esc(b.sub)}.</p>
    <div class="tags" style="margin-bottom:12px"><span class="pill">${esc(b.subject)}</span><span class="pill">${n} sections</span>${hasEn(b)?`<span class="pill gold">Arabic + English</span>`:`<span class="pill">Arabic</span>`}${(META.textsAudio||{})[b.file]?`<span class="pill ok">${ICON.ear} Narrated</span>`:""}</div>
    ${done.length?`<div class="spread small muted"><span>${done.length} of ${n} read</span><span>${Math.round(done.length/n*100)}%</span></div><span class="bar" style="display:block;margin:4px 0 10px"><i style="width:${done.length/n*100}%;background:var(--brand)"></i></span>`:""}
    ${next>=0?`<button class="btn" data-read="${b.id}|${next}" style="margin:4px 0 6px">${done.length?`Continue from section ${next+1}`:"Start reading"}</button>
      <button class="linkbtn small" id="markread" data-mark="${b.id}" style="display:block;margin:2px 0 8px">I've already read this book</button>`:`<div class="notice">${ICON.check}<span>You've read the whole book, alhamdulillah.</span></div>`}
    <p class="label">Contents</p>${toc}
    <p class="small muted" style="margin-top:14px">${T.ai?"The harakat and English are awaiting a teacher's check. ":""}${hasEn(b)?"":"Arabic text from the OpenITI corpus; English will be added."}</p>`);
}
function readView(b, i){
  const T = TEXTS[b.file]; if (!T) return `<p class="muted">Loading…</p>`;
  const s = T.sections[i], P = S.readPrefs = Object.assign({ harakat:true, english:true, size:2, rate:1 }, S.readPrefs||{}), key = `t|${b.id}|${i}`;
  const ar = s.v || s.p;   // esc() removes harakat when they're switched off, but never inside ayat
  const paras = ar.map((t,j) => `<div class="para" data-pj="${j}"><p class="ar-read">${esc(t)}</p>${P.english && s.en && s.en[j] ? `<p class="en-read">${esc(s.en[j])}</p>` : ""}</div>`).join("");
  return `<div class="player"><div class="player-in"><div class="phead"><button class="x" id="rquit" aria-label="Close">${ICON.x}</button><div class="bar"><i style="width:${(i+1)/T.sections.length*100}%;background:${b.color}"></i></div><span class="count">${i+1}/${T.sections.length}</span></div>
    <div class="pbody reader"><div class="kicker">${esc(b.title)}${s.parent?` · <span class="${hasAr(s.parent)?"ar":""}">${esc(s.parent)}</span>`:""}</div>
      ${hasAr(s.h)?`<h2 class="ar" style="text-align:right;font-size:1.5rem;margin:4px 0 2px">${esc(s.h)}</h2>`:`<h2 style="font-size:1.25rem;margin:4px 0 2px">${esc(s.h)}</h2>`}${s.he?`<p class="muted" style="margin:0 0 8px">${esc(s.he)}</p>`:""}
      <div class="tools" style="margin:6px 0 10px"><button class="tool listen ${AUD.on?"on":""}" id="listen">${AUD.on?ICON.pause+" Pause":ICON.play+" Listen"}</button>
        ${s.v ? `<button class="tool ${S.harakat!==false?"on":""}" id="tg-h">حَ Harakat ${S.harakat!==false?"on":"off"}</button>` : `<button class="tool" disabled style="opacity:.55" title="Harakat for this book are being added">حَ No harakat yet</button>`}${s.en?`<button class="tool ${P.english?"on":""}" id="tg-e">EN English</button>`:""}
        <button class="tool" id="fsdn" aria-label="Smaller text">A−</button><button class="tool" id="fsup" aria-label="Larger text">A+</button>
        ${AUD.on?`<button class="tool" id="rate">${P.rate}× speed</button>`:""}</div>
      ${S.dictUsed ? "" : `<p class="small muted" style="margin:0 0 8px">Tip: tap any Arabic word to look it up in the dictionary.</p>`}<div class="card fs${P.size}">${paras}</div>${toolRow(key,false)}</div>
    <div class="pfoot"><div class="grades two"><button class="grade" id="rprev" style="background:var(--surface);color:var(--ink);border:1px solid var(--line)" ${i===0?"disabled":""}>← Previous</button><button class="grade g2" id="rnext">${i+1<T.sections.length?"✓ Read · next":"✓ Finish"}</button></div></div></div></div>`;
}
/* ---- Dictionary: tap an Arabic word in the reader ----
   Lane's Lexicon (English, public domain) and a classical Arabic dictionary, fetched by the word's first two letters */
const DICT = {};
const normAr = s => s.replace(/[ً-ٰٟـ]/g,"").replace(/[أإآٱ]/g,"ا").replace(/ى/g,"ي");
const bucketOf = k => [...k.slice(0,2)].map(c => c.charCodeAt(0).toString(16).padStart(4,"0")).join("_");
async function dictGet(src, k){ const key = src + bucketOf(k);
  if (!(key in DICT)) { try { const r = await fetch(`data/dict/${src}/${bucketOf(k)}.json`); DICT[key] = r.ok ? await r.json() : {}; } catch(e){ DICT[key] = {}; } }
  return DICT[key][k]; }
function stems(w){
  const P = ["وال","فال","بال","كال","لل","ال","و","ف","ب","ك","ل","س"], X = ["هما","كما","هم","هن","كم","كن","نا","ها","ات","ون","ين","ان","وا","تم","ه","ك","ي","ة","ت"];
  const out = new Set([w]);
  for (const p of P) if (w.startsWith(p) && w.length - p.length >= 2) out.add(w.slice(p.length));
  for (const x of [...out]) for (const s of X) if (x.endsWith(s) && x.length - s.length >= 2) out.add(x.slice(0, -s.length));
  return [...out];
}
function rootsOf(w){                                   // rough guesses at the three root letters
  const out = new Set();
  for (let x of stems(w)) {
    const m = x.match(/^(است|مست|ان|ت|م|ي|ن|ا)/); if (m && x.length - m[0].length >= 3) x = x.slice(m[0].length);
    const core = x.length > 3 ? x[0] + x.slice(1,-1).replace(/[اوي]/g,"") + x.slice(-1) : x;
    if (core.length === 3) out.add(core); if (core.length === 2) out.add(core + core[1]);
    if (core.length === 4 && core[1] === "ت") out.add(core[0] + core.slice(2));          // ifta'ala
  }
  return [...out];
}
async function lookup(word){
  const w = normAr(word), st = stems(w), rt = rootsOf(w), res = { lane:null, ar:null };
  for (const k of [...st, ...rt]) { const e = await dictGet("lane", k); if (e) { res.lane = { k, e }; break; } }
  for (const k of [...rt, ...st]) { const e = await dictGet("ar", k); if (e) { res.ar = { k, e }; break; } }
  return res;
}
function wordAt(x, y){
  let node, off; if (document.caretRangeFromPoint) { const r = document.caretRangeFromPoint(x, y); if (!r) return ""; node = r.startContainer; off = r.startOffset; }
  else if (document.caretPositionFromPoint) { const p = document.caretPositionFromPoint(x, y); if (!p) return ""; node = p.offsetNode; off = p.offset; }
  if (!node || node.nodeType !== 3) return "";
  const t = node.textContent, L = /[ء-يً-ٰٟ]/; let s = off, e = off;
  while (s > 0 && L.test(t[s-1])) s--; while (e < t.length && L.test(t[e])) e++;
  return t.slice(s, e);
}
async function showLookup(word){
  const d = modal(`<div class="dict"><div class="spread"><span class="ar dword">${esc(word)}</span><button class="x" id="dclose" aria-label="Close">${ICON.x}</button></div><p class="muted small">Looking up…</p></div>`, (d, close) => { d.querySelector("#dclose").onclick = close; d.onclick = e => { if (e.target === d) close(); }; });
  d.classList.add("sheet"); S.dictUsed = true; save();
  const r = await lookup(word), box = d.querySelector(".dict");
  const lane = r.lane ? `<p class="label">Lane's Lexicon · <span class="ar">${esc(r.lane.k)}</span></p>${[...r.lane.e].sort((x,y) => /^\S+\s*:\s*see /.test(x) - /^\S+\s*:\s*see /.test(y)).slice(0,4).map(t => t.replace(/\s*(===|___)\s*/g, "\n")).map((t,k) => `<p class="dent ${k?"more":""}">${esc(t.length > 700 ? t.slice(0,700) + "…" : t)}</p>`).join("")}` : "";
  const ar = r.ar ? `<p class="label">Arabic dictionary · <span class="ar">${esc(r.ar.k)}</span></p>${r.ar.e.slice(0,2).map(t => `<p class="dent ar" style="text-align:right">${esc(t.length > 900 ? t.slice(0,900) + "…" : t)}</p>`).join("")}` : "";
  box.querySelector("p.muted").outerHTML = lane || ar ? lane + ar + `<p class="small muted" style="margin:10px 0 0">Matched by guessing the root, so check it fits the sentence.</p>`
    : `<p class="muted">No entry found for this word. Particles and names usually aren't in the dictionary.</p>`;
}
function bindRead(b, i){
  const T = TEXTS[b.file]; bindTools($("#app"), () => { $("#app").innerHTML = readView(b, i); bindRead(b, i); });
  $("#app").querySelectorAll(".ar-read").forEach(p => p.onclick = e => { if (String(getSelection())) return; const w = wordAt(e.clientX, e.clientY); if (normAr(w).length >= 2) showLookup(w); });
  const tg = (k) => () => { S.readPrefs[k] = !S.readPrefs[k]; save(); $("#app").innerHTML = readView(b, i); bindRead(b, i); };
  const th = $("#tg-h"); if (th) th.onclick = () => { S.harakat = S.harakat === false; save(); $("#app").innerHTML = readView(b, i); bindRead(b, i);
    if (S.harakat && !T.sections[i].v) toast("This book doesn't have harakat added yet. They'll appear when they're ready."); }; const te = $("#tg-e"); if (te) te.onclick = tg("english");
  const redraw = () => { $("#app").innerHTML = readView(b, i); bindRead(b, i); if (AUD.on) markPara(AUD.j); };
  $("#fsdn").onclick = () => { S.readPrefs.size = Math.max(0, S.readPrefs.size-1); save(); redraw(); };
  $("#fsup").onclick = () => { S.readPrefs.size = Math.min(5, S.readPrefs.size+1); save(); redraw(); };
  const rt = $("#rate"); if (rt) rt.onclick = () => { const r = [0.8,1,1.2,1.5]; S.readPrefs.rate = r[(r.indexOf(S.readPrefs.rate)+1) % r.length]; save(); redraw(); speakFrom(b, i, AUD.j); };
  $("#listen").onclick = () => { if (AUD.on) { stopAudio(); redraw(); } else { AUD.on = true; redraw(); speakFrom(b, i, 0); } };
  $("#rquit").onclick = () => { stopAudio(); go({ name:"book", id:b.id }); };
  $("#rprev").onclick = () => { stopAudio(); if (i > 0) openRead(b.id, i-1); };
  $("#rnext").onclick = () => { const d = S.books[b.id] = S.books[b.id]||[]; const first = !d.includes(i); if (first) d.push(i); S.readDay = today();
    const adv = touchDay(first ? 2 : 0); if (adv) toast(`${S.streak} day streak! Keep going`);
    stopAudio(); if (i+1 < T.sections.length) openRead(b.id, i+1); else { toast("Book finished, alhamdulillah"); go({ name:"book", id:b.id }); } };
}
/* ---- Listen: device voices now; recorded audio (s.audio[j]) is used when a section has it ---- */
const AUD = { on:false, j:0, el:null, token:0 };
const hasTTS = () => "speechSynthesis" in window;
// Pick the most natural voice the device has; a student's own choice (Progress → Voices) wins.
function voiceScore(v){ const n = (v.name||"").toLowerCase(); let s = 0;
  if (/premium|enhanced|natural|neural|online|wavenet|studio/.test(n)) s += 50;
  if (/google/.test(n)) s += 20; if (/siri/.test(n)) s += 30;
  if (/compact|espeak|robot|novelty|bad news|bells|boing|bubbles|cellos|whisper|zarvox|trinoids|albert|jester|organ|superstar|wobble|fred|junior|ralph|kathy|bahh/.test(n)) s -= 80;
  if (/en-gb/i.test(v.lang)) s += 6; if (/en-us/i.test(v.lang)) s += 4; if (/ar-sa/i.test(v.lang)) s += 6;
  if (v.localService === false) s += 5; return s; }
function voicesFor(lang){ return (hasTTS() ? speechSynthesis.getVoices() : []).filter(v => v.lang && v.lang.toLowerCase().startsWith(lang)).sort((a,b) => voiceScore(b) - voiceScore(a)); }
function voiceFor(lang){ const vs = voicesFor(lang), pick = (S.voices||{})[lang]; return vs.find(v => v.name === pick) || vs[0] || null; }
// Never let a synthetic voice recite the Qur'an: ayat in ﴿…﴾ or {…} are skipped with a short pause.
const speakable = t => String(t).replace(/﴿[^﴾]*﴾|\{[^}]*\}/g, " … ").replace(/[ﷺ]/g, " صلى الله عليه وسلم ").replace(/\s+/g, " ").trim();
function stopAudio(){ AUD.on = false; AUD.token++; if (hasTTS()) speechSynthesis.cancel(); if (AUD.el) { AUD.el.pause(); AUD.el = null; } document.querySelectorAll(".para.speaking").forEach(x => x.classList.remove("speaking")); }
function markPara(j){ document.querySelectorAll(".para").forEach(x => x.classList.toggle("speaking", +x.dataset.pj === j)); const el = document.querySelector(`.para[data-pj="${j}"]`); if (el) el.scrollIntoView({ block:"center", behavior:"smooth" }); }
function sayOne(text, lang, rate, token){ return new Promise(res => { if (!text || token !== AUD.token) return res();
  const u = new SpeechSynthesisUtterance(text), v = voiceFor(lang); u.lang = v ? v.lang : (lang === "ar" ? "ar-SA" : "en-GB"); if (v) u.voice = v; u.rate = rate;
  u.onend = u.onerror = () => res(); speechSynthesis.speak(u); }); }
function playFile(url, rate, token){ return new Promise(res => { if (token !== AUD.token) return res(); const a = AUD.el = new Audio(url); a.playbackRate = rate; a.onended = a.onerror = () => res(); a.play().catch(() => res()); }); }
async function speakFrom(b, i, j0){
  const token = ++AUD.token; if (hasTTS()) speechSynthesis.cancel(); if (AUD.el) { AUD.el.pause(); AUD.el = null; } AUD.on = true;
  const T = TEXTS[b.file], s = T.sections[i], P = S.readPrefs, ar = s.v || s.p;
  if (!s.audio && !s.aud_en && !hasTTS()) { toast("This device can't read aloud"); return stopAudio(); }
  if (!s.audio && S.arVoice !== false && !voiceFor("ar")) toast("No Arabic voice on this device, so only English is read. Add an Arabic voice in your phone's speech settings.");
  for (let j = j0; j < ar.length; j++){
    if (token !== AUD.token) return; AUD.j = j; markPara(j);
    if (s.audio && s.audio[j]) await playFile(s.audio[j], P.rate, token);
    else if (S.arVoice !== false && voiceFor("ar")) await sayOne(speakable(ar[j]), "ar", P.rate*0.95, token);
    if (token !== AUD.token) return;
    if (P.english && s.aud_en && s.aud_en[j]) await playFile(s.aud_en[j], P.rate, token);
    else { if (P.english && s.en && s.en[j]) await sayOne(speakable(s.en[j]).replace(/صلى الله عليه وسلم/g, "peace and blessings be upon him").replace(/عليه السلام/g, "peace be upon him").replace(/رضي الله عنهما?|رضي الله عنها|رضي الله عنهم/g, "may Allah be pleased with them").replace(/رحمه الله/g, "may Allah have mercy on him"), "en", P.rate*0.95, token); }
  }
  if (token !== AUD.token) return;
  // audiobook: carry on to the next section
  const d = S.books[b.id] = S.books[b.id]||[]; if (!d.includes(i)) { d.push(i); touchDay(2); }
  if (i+1 < T.sections.length) { await openRead(b.id, i+1); AUD.on = true; $("#app").innerHTML = readView(b, i+1); bindRead(b, i+1); speakFrom(b, i+1, 0); }
  else { stopAudio(); toast("Book finished, alhamdulillah"); }
}
if (hasTTS()) { speechSynthesis.getVoices(); speechSynthesis.onvoiceschanged = () => speechSynthesis.getVoices(); }
async function openRead(id, i){
  const b = bookById(id); if (!TEXTS[b.file] || !TEXTS[b.file].sections[i].p) { $("#app").innerHTML = `<div class="done-screen" style="min-height:60vh"><p class="muted">Loading ${esc(b.title)}…</p></div>`; try { await loadSection(b.file, i); } catch(e){ toast(navigator.onLine ? "Couldn't open this book. Please try again." : "This book isn't saved on this phone yet. Open it once with internet, or save its year in Settings."); return go({name:"library"}); } }
  view = { name:"read", id, i }; S.lastRead = { id, i }; save(); $("#app").innerHTML = readView(b, i); bindRead(b, i); window.scrollTo(0,0); const pb = document.querySelector(".pbody"); if (pb) pb.scrollTop = 0;
}

/* ---- Specialisation (further studies) ---- */
const specOpen = () => !!(S.tests[YEARS.length] && S.tests[YEARS.length].passed);
function specCard(){
  const open = specOpen(), m = MODULES.find(x => x.name === S.spec);
  return `<button class="year row ${open?"":"locked"}" data-spec="1"><span class="yr-badge">${ICON.star.replace("<svg",'<svg width="20" height="20"')}</span>
    <span style="flex:1;text-align:left"><b>Specialisation</b><span class="small muted" style="display:block">${m ? esc(m.name) : "One subject in depth, after Year 5"}</span></span>
    ${m ? `<span class="pill ok">Chosen</span>` : open ? `<span class="pill gold">Choose</span>` : `<span class="lockic">${ICON.lock}</span>`}</button>`;
}
function specView(){
  const open = specOpen(), chosen = MODULES.find(x => x.name === S.spec);
  const intro = `<button class="back" data-go="syllabus">${ICON.back} Course</button>
    <section class="hero" style="--c:var(--gold)"><div class="hero-art">${art("star","#C8912B",84)}</div><h1>Specialisation (Takhassus)</h1>
    <p>After the Dawrat al-Hadith, spend a year of further study in one module, going deeper into its texts with a teacher.</p></section>
    ${open?"":`<div class="notice">${ICON.lock}<span>Pass the Year ${YEARS.length} final test to choose your specialisation. You can look at the options now.</span></div>`}`;
  if (chosen) return shell(`${intro}<p class="label">Your specialisation</p>
    <div class="card"><div class="row" style="gap:12px;align-items:center">${art(chosen.art, chosen.color, 54)}<div><h2 style="margin:0">${esc(chosen.name)}</h2><p class="small muted" style="margin:2px 0 0">${esc(chosen.about)}</p></div></div>
    <p class="label" style="margin-top:14px">Texts for further study</p>${(SPEC_TEXTS[chosen.name]||[]).map(t=>`<div class="item soon"><span class="ico art-ico" style="opacity:.5">${art(chosen.art, chosen.color, 36)}</span><span><span class="t">${esc(t)}</span><br><span class="s">Coming soon</span></span></div>`).join("")}
    <div class="btnrow" style="margin-top:12px"><button class="btn ghost" id="changespec">Change specialisation</button></div></div>`);
  return shell(`${intro}<p class="label">Choose a module</p><div class="stack">${MODULES.map(m => `<button class="item" data-pick="${esc(m.name)}" ${open?"":"disabled"}>
      <span class="ico art-ico">${art(m.art, m.color, 40)}</span><span><span class="t">${esc(m.name)}</span><br><span class="s">${esc((SPEC_TEXTS[m.name]||[]).join(" · ")||m.about)}</span></span>${open?`<span class="pill gold">Choose</span>`:ICON.lock}</button>`).join("")}</div>`);
}

/* ---- Save, report, "I know this" ---- */
// Where reports go. Set to an email address (or leave empty to use the phone's share sheet / copy).
const REPORT_TO = "";
const isSaved = k => (S.saved||[]).includes(k);
function toggleSave(k){ S.saved = S.saved||[]; const i = S.saved.indexOf(k); if (i >= 0) S.saved.splice(i,1); else S.saved.unshift(k); save(); toast(i >= 0 ? "Removed from saved" : "Saved. Find it under Search"); }
function toast(t){ document.querySelectorAll(".toast").forEach(x => x.remove()); const el = document.createElement("div"); el.className = "toast"; el.setAttribute("role","status"); el.textContent = t; document.body.appendChild(el); setTimeout(() => el.remove(), 2200); }
function toolRow(k, know){ const it = k.startsWith("c|") ? itemByKey(k) : null, qa = it && it.kind === "card" && isQA(it.c);
  const langBtn = qa ? `<button class="tool lang" data-lang="1" aria-label="Switch question and answer language">${ICON.globe} ${shownLang(it.c) === "ar" ? "English" : "العربية"}</button>` : "";
  return `<div class="tools">${langBtn}<button class="tool ${isSaved(k)?"on":""}" data-save="${esc(k)}" aria-label="Save">${isSaved(k)?ICON.saved:ICON.save}<span>${isSaved(k)?"Saved":"Save"}</span></button>
  <button class="tool" data-report="${esc(k)}" aria-label="Report a problem">${ICON.flag}<span>Report</span></button>
  <button class="tool ${S.harakat!==false?"on":""}" data-harakat="1" aria-label="Harakat on or off">حَ ${S.harakat!==false?"on":"off"}</button>
  ${know?`<button class="tool" id="know" aria-label="I already know this">${ICON.know}<span>I know this</span></button>`:""}</div>`; }
function itemByKey(k){
  const [kind, id, i] = k.split("|");
  if (kind === "c") for (const d of allDecks()) { const c = (d.cards||[]).find(c => c.id === id); if (c) return { kind:"card", c, src:d, y:d.year }; }
  if (kind === "t") { const b = bookById(id), T = b && TEXTS[b.file]; if (b) return { kind:"sec", src:b, y:b.year, i:+i, s:T ? T.sections[+i] : null }; }
  if (kind === "l") for (const y of YEARS) for (const b of y.books) if (b.id === id && b.lines && b.lines[+i]) return { kind:"line", l:b.lines[+i], src:b, y:y.n, i:+i };
  return null;
}
const keyCard = c => `c|${c.id}`, keyLine = (b, l) => `l|${b.id}|${b.lines.indexOf(l)}`;
function reportText(r){ const it = itemByKey(r.k); const what = !it ? r.k : it.kind === "sec" ? `${it.src.title}, section ${it.i+1}${it.s?`: ${it.s.h}\n${(it.s.p||[]).slice(0,2).join("\n")}`:""}` : it.kind === "card" ? `${it.src.title}\nQ: ${it.c.f}\nA: ${it.c.b}` : `${it.src.title}, ${it.src.type==="hadith"?"hadith":"line"} ${it.i+1}\n${it.l.ar||""}\n${it.l.en||""}`;
  return `Dar as-Siddiq report [${r.k}]\nProblem: ${r.why}${r.note?`\nNote: ${r.note}`:""}\n\n${what}`; }
async function sendReports(list){
  const body = list.map(reportText).join("\n\n----------\n\n"), subject = `Dar as-Siddiq: ${list.length} card report${list.length>1?"s":""}`;
  if (REPORT_TO) { location.href = `mailto:${REPORT_TO}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`; }
  else if (navigator.share) { try { await navigator.share({ title:subject, text:body }); } catch(e){ return false; } }
  else { try { await navigator.clipboard.writeText(body); toast("Report copied. Paste it to the team"); } catch(e){ return false; } }
  list.forEach(r => r.sent = true); save(); return true;
}
function openReport(k){
  const reasons = ["The answer is wrong","Spelling or translation mistake","Arabic text or harakat mistake","Missing or wrong honorific","Something else"];
  modal(`<h2 style="margin:0 0 4px">Report a problem</h2><p class="small muted" style="margin:0 0 12px">Our teachers will check it and correct it, in sha' Allah.</p>
    <div class="opts" id="why">${reasons.map((r,i)=>`<button class="opt" data-why="${i}">${r}</button>`).join("")}</div>
    <textarea id="rnote" rows="3" placeholder="What should it say? (optional)" class="search" style="margin-top:10px;resize:vertical"></textarea>
    <div class="btnrow" style="margin-top:12px"><button class="btn ghost" id="mno">Cancel</button><button class="btn" id="msend" disabled>Send report</button></div>`, (d, close) => {
    let why = null;
    d.querySelectorAll("[data-why]").forEach(b => b.onclick = () => { why = reasons[+b.dataset.why]; d.querySelectorAll("[data-why]").forEach(x => x.classList.toggle("sel", x === b)); d.querySelector("#msend").disabled = false; });
    d.querySelector("#mno").onclick = close;
    d.querySelector("#msend").onclick = async () => { const r = { k, why, note:d.querySelector("#rnote").value.trim(), at:Date.now(), sent:false };
      S.reports = S.reports||[]; S.reports.push(r); save(); close(); const ok = await sendReports([r]); toast(ok ? "Thank you, jazak Allahu khayran" : "Saved. You can send it later from Progress"); };
  });
}
function bindTools(root, rerender){
  root.querySelectorAll("[data-lang]").forEach(b => b.onclick = () => { const k = b.closest(".tools").querySelector("[data-save]").dataset.save, it = itemByKey(k);
    S.cardLang = shownLang(it.c) === "ar" ? "en" : "ar"; save(); rerender && rerender(); });
  root.querySelectorAll("[data-harakat]").forEach(b => b.onclick = () => { S.harakat = S.harakat === false; save(); toast(S.harakat ? "Harakat on" : "Harakat off (Qur'anic text keeps its harakat)"); rerender && rerender(); });
  root.querySelectorAll("[data-save]").forEach(b => b.onclick = () => { toggleSave(b.dataset.save); rerender && rerender(); });
  root.querySelectorAll("[data-report]").forEach(b => b.onclick = () => openReport(b.dataset.report));
}

/* ======================= STUDY SESSION ======================= */
let Q = null;
function startStudy(decks){
  const t = today(), q = [];
  for (const d of decks){ if (!d.cards) continue;
    q.push(...d.cards.filter(c => S.cards[c.id] && S.cards[c.id].due <= t).sort((a,b)=>S.cards[a.id].due-S.cards[b.id].due)); }
  const pools = decks.filter(d => d.cards).map(d => d.cards.filter(c => !S.cards[c.id])); let left = newLeft();   // new cards, a few from each subject in turn
  for (let k = 0; left > 0 && pools.some(p => p.length); k = (k+1) % pools.length) if (pools[k].length) { q.push(pools[k].shift()); left--; }
  if (!q.length) return modal(`<p style="margin-top:0;font-weight:700">Nothing to study right now.</p><p class="small muted">Come back tomorrow for your next reviews, or raise new cards per day in Progress.</p><button class="btn" id="mok">OK</button>`, (d,c)=>d.querySelector("#mok").onclick=c);
  const deckById = Object.fromEntries(decks.map(d=>[d.id,d]));
  Q = { q, i:0, shown:false, total:q.length, done:0, xp:0, deckById };
  renderStudy();
}
/* ---- Bilingual Q&A: one switch shows question AND answer in Arabic or English (more languages later) ---- */
const LANGS = { ar:"العربية", en:"English" };
const isQA = c => !!c.tr || !!c.fa === !!c.ba;           // switchable: same-language Q&A, or any card carrying a translation
const origLang = c => c.lang || (c.fa && c.ba ? "ar" : c.fa && !c.ba ? "en" : c.fa ? "ar" : "en");
function viewCard(c){
  if (!isQA(c)) return c;
  const want = S.cardLang || origLang(c); if (want === origLang(c)) return c;
  const t = c.tr && c.tr[want];
  if (!t) return { ...c, missing:want };
  return { ...c, f:t.f, b:t.b, fa: want === "ar" || /^[\u0600-\u06FF\s]+$/.test(t.f) ? 1 : 0, ba: want === "ar" ? 1 : 0, translated:want, ai:!!t.ai };
}
const shownLang = c => { const v = viewCard(c); return v.translated || origLang(c); };
function cardFront(c, d){
  c = viewCard(c);
  const esc = c.deck === "quran" ? escQ : window.escH;
  const big = c.fa && c.f.length < 24;
  return `<div class="kicker">${esc(d.title)}${c.g?` · ${esc(c.g)}`:""}</div>
    <div class="card" style="${big?"text-align:center;padding:26px 16px":""}">
      ${big?`<div class="big-ar">${esc(c.f)}</div>`:`<p class="q ${c.fa?"ar":""}" style="margin:0;${c.fa?"font-size:1.4rem;line-height:1.9;text-align:right":""}">${esc(c.f)}</p>`}
      ${c.s?`<span class="pill" style="margin-top:8px">${esc(c.s)}</span>`:""}</div>`;
}
function cardBack(c){
  c = viewCard(c);
  const note = c.missing ? `<p class="small muted" style="margin:0 0 8px">Not available in ${LANGS[c.missing]} yet, so you're seeing the original.</p>` : c.ai ? `<span class="pill gold" style="margin-bottom:8px;display:inline-block">AI translation · needs review</span>` : "";
  const esc = c.deck === "quran" ? escQ : window.escH;
  return `<div class="card answer" style="margin-top:12px">${note}
    ${c.ba ? `<div class="ar" style="font-size:1.3rem;line-height:1.9;text-align:right">${esc(c.b)}</div>`
      : c.b.length < 80 ? `<div style="font-size:1.2rem;font-weight:800">${esc(c.b)}</div>` : points(c.b)}
    ${c.aw||c.ai?`<p class="review-note">Awaiting a teacher's check</p>`:""}
    ${c.ex?`<div class="ayah">${escQ(c.ex)}</div>`:""}${c.exr?`<div class="ref">${esc(c.exr)}</div>`:""}</div>`;
}
function renderStudy(){
  const c = Q.q[Q.i]; if (!c) return finishStudy();
  const st = S.cards[c.id], d = Q.deckById[c.deck];
  const simple = !S.advancedGrades;
  const foot = !Q.shown ? `<div class="pfoot"><button class="btn" id="show">Show answer</button></div>`
    : simple ? `<div class="pfoot"><div class="grades two"><button class="grade g0" data-g="0">↻ Redo<span>see it again soon</span></button><button class="grade g2" data-g="2">✓ Got it<span>${st && st.ivl >= 1 ? `next check in ${ivlLabel(st,2)}` : "tick it off"}</span></button></div></div>`
    : `<div class="pfoot"><div class="grades">${["Again","Hard","Good","Easy"].map((l,g)=>`<button class="grade g${g}" data-g="${g}">${l}<span>${ivlLabel(st,g)}</span></button>`).join("")}</div></div>`;
  $("#app").innerHTML = `<div class="player"><div class="player-in"><div class="phead"><button class="x" id="quit" aria-label="Stop studying">${ICON.x}</button><div class="bar"><i style="width:${Q.done/Q.total*100}%"></i></div><span class="count">${Q.q.length-Q.i} left</span></div>
    <div class="pbody">${cardFront(c,d)}${Q.shown?cardBack(c):""}${toolRow(keyCard(c), !st || st.ivl < MASTER_IVL)}</div>${foot}</div></div>`;
  bindTools($("#app"), renderStudy);
  const kn = $("#know"); if (kn) kn.onclick = () => knowCard(c);
  const sh = $("#show"); if (sh) sh.onclick = () => { Q.shown = true; renderStudy(); };
  document.querySelectorAll("[data-g]").forEach(b => b.onclick = () => grade(+b.dataset.g));
  $("#quit").onclick = () => { Q = null; touchDay(0); render(); };
}
function knowCard(c){
  if (!S.cards[c.id]){ const t = today(); S.newDone[t] = S.newDone[t]||{}; S.newDone[t][c.deck] = (S.newDone[t][c.deck]||0) + 1; }
  S.cards[c.id] = { ivl:21, ease:2.6, reps:1, lapses:0, due:today()+21, known:true };
  Q.q = Q.q.filter((x, j) => j <= Q.i || x.id !== c.id); Q.done++; Q.i++; Q.shown = false; save();
  toast("Marked as known. It returns in 3 weeks for a quick check"); renderStudy();
}
function grade(g){
  const c = Q.q[Q.i], prev = S.cards[c.id];
  if (!prev){ const t = today(); S.newDone[t] = S.newDone[t]||{}; S.newDone[t][c.deck] = (S.newDone[t][c.deck]||0) + 1; }
  const { s, wasReview } = schedule(prev, g); S.cards[c.id] = s;
  if (wasReview){ S.log.push(g >= 1 ? 1 : 0); if (S.log.length > 1000) S.log = S.log.slice(-600); }
  if (s.ivl === 0){ Q.q.splice(Math.min(Q.q.length, Q.i + 4), 0, c); Q.total++; }
  Q.done++; Q.i++; Q.shown = false; Q.xp++; S.xp++; S.days[today()] = (S.days[today()]||0) + 1; save(); renderStudy();
}
function finishStudy(){
  const xp = Q.xp, adv = touchDay(0); Q = null;
  $("#app").innerHTML = `<div class="player"><div class="player-in"><div class="done-screen"><div class="seal" aria-hidden="true"><svg viewBox="0 0 120 120" width="112"><path class="seal-ring" d="M60.0 6.0 L75.3 23.0 L98.2 21.8 L97.0 44.7 L114.0 60.0 L97.0 75.3 L98.2 98.2 L75.3 97.0 L60.0 114.0 L44.7 97.0 L21.8 98.2 L23.0 75.3 L6.0 60.0 L23.0 44.7 L21.8 21.8 L44.7 23.0Z" fill="none" stroke="var(--gold)" stroke-width="3" stroke-linejoin="round"/><circle class="seal-in" cx="60" cy="60" r="26" fill="var(--brand)"/><path class="seal-tick" d="M48 60l8 8 16-17" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg></div><div class="big">Session complete</div>${adv?streakBurst():""}
    <div class="tiles"><div class="tile"><b>${xp}</b><span>Cards studied</span></div><div class="tile"><b>${S.streak}</b><span>Day streak</span></div></div>
    <p class="muted small" style="margin:0;max-width:320px">Cards you knew well come back in a few days. Ones you missed come back sooner.</p></div><div class="pfoot"><button class="btn" id="cont">Continue</button></div></div></div>`;
  $("#cont").onclick = () => render();
}

/* ======================= BOOK LESSON ======================= */
let B = null;
function bookQuiz(b, l){
  const i = b.lines.indexOf(l), near = (fn, ok) => b.lines.map((x,k) => ({ x, k })).filter(({x,k}) => k !== i && ok(x)).sort((p,q) => Math.abs(p.k-i) - Math.abs(q.k-i) + (Math.random()-.5)*6).slice(0, 12).map(({x}) => fn(x));
  if (b.type === "hadith"){
    const who = narrator(l.en); if (!who) return null;
    const others = distinct([...new Set(b.lines.map(x => narrator(x.en)).filter(n => n && n !== who))], who, 3); if (others.length < 3) return null;
    const saying = l.en.replace(/^[^:"“]{0,160}?:\s*/, "").replace(/^Allah's (Messenger|Apostle)[^:]{0,40}:\s*/, "");
    return { prompt:null, q:`Who narrated this hadith? “${snip(saying, 200)}”`, answer:who, options:shuffle([who, ...others]), explain:{ title:l.note, body:snip(l.en, 420) } };
  }
  if (l.en.length <= 240) {
    const head = s => s.split(/[\s(,;:]/)[0].toLowerCase();          // i'rab and ayah practice: no choice that is the same word or starts the same way
    const opts = distinct(near(x => x.en, x => x.en.length <= 240 && x.en.length > l.en.length*.35 && x.en.length < l.en.length*2.8 && (!b.ask || (x.ar !== l.ar && head(x.en) !== head(l.en)))).filter((e, k, arr) => !b.ask || arr.findIndex(f => head(f) === head(e)) === k), l.en, 3);
    if (opts.length === 3) return { prompt:l.ar, q:b.ask || "What does this line mean?", answer:l.en, options:shuffle([l.en, ...opts]), explain:{ title:b.askTitle || "The full line", body:l.en, note:l.note && snip(l.note, 360) } };
  }
  const opts = distinct(near(x => x.ar, x => x.ar.length < 220), l.ar, 3);         // long English: ask the other way round
  return { prompt:null, q:`Which line says: “${snip(l.en, 220)}”`, answer:l.ar, ansAr:true, options:shuffle([l.ar, ...opts]), explain:{ title:"The full line", body:l.en, note:l.note && snip(l.note, 360) } };
}
/* ---- Word lessons: meet each word (big, with harakat, meaning, pronunciation guide and audio), then check both ways ---- */
const TL = { "ب":"b","ت":"t","ث":"th","ج":"j","ح":"ḥ","خ":"kh","د":"d","ذ":"dh","ر":"r","ز":"z","س":"s","ش":"sh","ص":"ṣ","ض":"ḍ","ط":"ṭ","ظ":"ẓ","ع":"ʿ","غ":"gh","ف":"f","ق":"q","ك":"k","ل":"l","م":"m","ن":"n","ه":"h","و":"w","ي":"y","ء":"'","أ":"'","إ":"'","ؤ":"'","ئ":"'","ة":"h" };
const SUN = "تثدذرزسشصضطظلن", VOW = { "َ":"a", "ُ":"u", "ِ":"i" }, TAN = { "ً":"an", "ٌ":"un", "ٍ":"in" };
function translit(w){
  w = (w||"").replace(/ٱ/g,"ا").trim(); if (!/[ً-ْ]/.test(w) || /\s/.test(w)) return "";      // single words that carry harakat
  let out = "", i = 0, prevV = "";
  if (/^ال[\u0652]?[\u0621-\u064A]/.test(w) && w.length > 3) { const n = w.replace(/^ال\u0652?/, "")[0]; out = SUN.includes(n) ? "a" + TL[n] + "-" : "al-"; i = w[2] === "\u0652" ? 3 : 2; }
  for (; i < w.length; i++){
    const ch = w[i]; if (!/[ء-يآ]/.test(ch)) continue;
    let marks = ""; while (/[ً-ْٰ]/.test(w[i+1]||"")) marks += w[++i];
    const v = [...marks].map(m => VOW[m]).find(Boolean) || "", tan = [...marks].map(m => TAN[m]).find(Boolean) || "", sh = marks.includes("ّ"), dag = marks.includes("ٰ"), suk = marks.includes("ْ");
    if (ch === "ا" || ch === "آ") { if (ch === "آ") { out += out ? "'ā" : "ā"; prevV = ""; continue; }
      if (prevV === "a") { out = out.replace(/a$/, "ā"); prevV = ""; continue; }
      if (!out) { out += v || "a"; prevV = v || "a"; continue; }
      if (/ū$/.test(out) && i === w.length - 1) continue;                                // silent alif after the plural waw
      if (tan) continue; out += "ā"; prevV = ""; continue; }
    if (ch === "ى" && (v || suk)) { out += "y" + v; prevV = v; continue; }
    if (ch === "ى") { if (prevV === "a") out = out.replace(/a$/, "ā"); else out += "ā"; prevV = ""; continue; }
    if ((ch === "و" || ch === "ي") && !v && !sh && !tan && !suk) { const long = ch === "و" ? "u" : "i";
      if (prevV === long) { out = out.replace(new RegExp(long + "$"), long === "u" ? "ū" : "ī"); prevV = ""; continue; } }
    let c = TL[ch] || ""; if (ch === "ة") c = tan ? "t" : "";
    if (!out && "أإء".includes(ch)) c = "";                                          // no mark for a word-initial hamzah
    if (out.endsWith("-") && SUN.includes(ch) && sh) out += c; else out += sh ? c + c : c;
    out += (dag ? "ā" : v) + tan; prevV = tan || dag ? "" : v;
    if (ch === "ة" && !tan && !out.endsWith("a")) out += "a";
  }
  return out.replace(/'+/g, "'").replace(/-'/, "-").replace(/^-/, "");
}
const showTranslit = b => S.translit === "on" || (S.translit !== "off" && (b ? b.year : 1) <= 1);
let WORDAUDIO = null;
async function wordAudio(){ if (WORDAUDIO) return WORDAUDIO; try { const r = await fetch("data/wordaudio.json"); WORDAUDIO = r.ok ? new Set(await r.json()) : new Set(); } catch(e){ WORDAUDIO = new Set(); } return WORDAUDIO; }
let WAUD = null;
async function sayWord(l){
  try { if (WAUD) WAUD.pause(); const have = await wordAudio();
    if (have.has(l.id)) { WAUD = new Audio(`audio/words/${l.id}.mp3`); await WAUD.play(); return; }
    if (window.speechSynthesis) { speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance(l.ar); u.lang = "ar-SA"; const v = voiceFor("ar"); if (v) u.voice = v; speechSynthesis.speak(u); }
  } catch(e){}
}
function wordQuiz(b, l, k){
  const i0 = b.lines.indexOf(l), near = b.lines.map((x,k2) => ({ x, d:Math.abs(k2 - i0) + Math.random()*8 })).filter(o => o.x !== l).sort((p,q) => p.d - q.d).slice(0, 14).map(o => o.x);
  if (k % 2 === 0) {                                                                   // Arabic -> meaning
    const opts = distinct(near.map(x => x.en).filter(e => e.length < 90), l.en, 3); if (opts.length < 3) return null;
    return { prompt:l.ar, q:"What does this word mean?", answer:l.en, options:shuffle([l.en, ...opts]), word:true };
  }
  const opts = distinct(near.map(x => x.ar).filter(x => x.length < 30), l.ar, 3); if (opts.length < 3) return null;   // meaning -> Arabic
  return { prompt:null, q:`Which word means “${l.en}”?`, answer:l.ar, ansAr:true, options:shuffle([l.ar, ...opts]), word:true, guide:true };
}
function startLesson(bookId, idx){
  const b = YEARS.flatMap(y=>y.books).find(x=>x.id===bookId), lines = b.lines.slice(idx*b.per, idx*b.per+b.per);
  if (b.type === "words") {
    const quiz = shuffle(lines.map((l,k) => wordQuiz(b, l, k)).filter(Boolean)).map(q => ({ kind:"mcq", ...q }));
    B = { b, idx, steps:[...lines.map(l => ({ kind:"word", l })), ...quiz], i:0, sel:null, answered:false, correct:0, nq:quiz.length };
    wordAudio(); renderLesson(); return sayWord(lines[0]);
  }
  const quiz = shuffle(lines).map(l => bookQuiz(b, l)).filter(Boolean).slice(0, Math.min(3, lines.length)).map(q => ({ kind:"mcq", ...q }));
  B = { b, idx, steps:[...lines.map(l=>({kind:"read", l})), ...quiz], i:0, sel:null, answered:false, correct:0, nq:quiz.length };
  renderLesson();
}
function renderLesson(){
  const st = B.steps[B.i]; if (!st) return finishLesson();
  let body, foot;
  if (st.kind === "word"){
    const nth = B.steps.filter((x,j)=>x.kind==="word" && j<=B.i).length, n = B.steps.filter(x=>x.kind==="word").length, tl = showTranslit(B.b) ? translit(st.l.ar) : "";
    body = `<div class="kicker">New word ${nth} of ${n}</div><div class="card wordcard">
        <p class="ar word-ar">${escQ(st.l.ar)}</p>${tl?`<p class="word-tl">${esc(tl)}</p>`:""}<p class="word-en">${esc(st.l.en)}</p>
        ${st.l.note?`<p class="small muted" style="margin:0">${esc(st.l.note.replace(/ · #\d+ most frequent/,""))}</p>`:""}
        ${st.l.ex?`<div class="word-ex"><p class="ar" style="margin:0;font-size:1.15rem">${escQ(st.l.ex)}</p>${st.l.exr?`<p class="small muted" style="margin:4px 0 0">${esc(st.l.exr.split(" · ")[0])}</p>`:""}</div>`:""}
        <button class="btn ghost small-btn" id="say" style="margin-top:12px">${ICON.play} Hear it</button></div>`;
    foot = `<div class="pfoot"><button class="btn" id="next">${nth === n ? "Check what you learnt" : "Next word"}</button></div>`;
  } else if (st.kind === "read"){
    const nth = B.steps.filter((x,j)=>x.kind==="read" && j<=B.i).length;
    body = `<div class="kicker">${esc(B.b.title)} · ${B.b.type==="hadith"?"hadith":"line"} ${nth}</div><div class="card">
      ${B.b.type==="hadith"
        ? `<p style="margin:0 0 10px;font-size:1.02rem">${esc(st.l.en)}</p><details><summary>Arabic text</summary><p class="line-ar" style="font-size:1.25rem;margin-top:8px">${esc(st.l.ar)}</p></details><p class="ref" style="margin-top:10px">${esc(st.l.note)}</p>`
        : `<p class="line-ar">${esc(st.l.ar)}</p><p style="margin:0">${esc(st.l.en)}</p>${st.l.note?`<details><summary>${B.b.id==="majalla"?"Explanation and example":"Commentary"}</summary><div class="small answer">${points(st.l.note)}</div></details>`:""}`}</div>`;
    body += toolRow(keyLine(B.b, st.l), false);
    foot = `<div class="pfoot"><button class="btn" id="next">Continue</button></div>`;
  } else {
    body = `<div class="kicker">Check your understanding</div>${st.prompt?`<p class="line-ar">${esc(st.prompt)}</p>`:""}<p class="q" style="font-size:1.05rem">${esc(st.q)}</p>
      <div class="opts">${st.options.map((o,i)=>{ let cls=""; if (B.answered){ if (o===st.answer) cls="right"; else if (i===B.sel) cls="wrong"; } else if (i===B.sel) cls="sel";
        const g = st.guide && showTranslit(B.b) ? translit(o) : "";
        return `<button class="opt ${cls} ${st.ansAr?"ar":""}" style="${st.ansAr?"text-align:right;font-size:1.15rem":""}" data-o="${i}" ${B.answered?"disabled":""}>${st.word?escQ(o):esc(o)}${g?`<span class="opt-tl">${esc(g)}</span>`:""}</button>`; }).join("")}</div>
      ${B.answered && st.explain ? `<div class="explain"><div class="kicker" style="margin:0 0 6px">${esc(st.explain.title)}</div><p style="margin:0">${esc(st.explain.body)}</p>${st.explain.note?`<div class="small muted" style="margin-top:8px">${points(st.explain.note)}</div>`:""}</div>` : ""}`;
    if (!B.answered) foot = `<div class="pfoot"><button class="btn" id="check" ${B.sel===null?"disabled":""}>Check</button></div>`;
    else { const ok = st.options[B.sel] === st.answer; foot = `<div class="pfoot ${ok?"ok":"bad"}" role="status"><div class="fb"><strong>${ok?"Correct, masha'Allah":"Not quite"}</strong>${ok?"":`<span class="small">The highlighted answer is correct.</span>`}</div><button class="btn" id="next">Continue</button></div>`; }
  }
  $("#app").innerHTML = `<div class="player"><div class="player-in"><div class="phead"><button class="x" id="quit" aria-label="Leave lesson">${ICON.x}</button><div class="bar"><i style="width:${B.i/B.steps.length*100}%;background:${B.b.color}"></i></div></div><div class="pbody">${body}</div>${foot}</div></div>`;
  bindTools($("#app"), renderLesson);
  document.querySelectorAll("[data-o]").forEach(x => x.onclick = () => { B.sel = +x.dataset.o; renderLesson(); });
  const ck = $("#check"); if (ck) ck.onclick = () => { B.answered = true; if (st.options[B.sel] === st.answer) B.correct++; renderLesson(); };
  const nx = $("#next"); if (nx) nx.onclick = () => { B.i++; B.sel = null; B.answered = false; renderLesson(); const n2 = B && B.steps[B.i]; if (n2 && n2.kind === "word") sayWord(n2.l); };
  const sy = $("#say"); if (sy) sy.onclick = () => sayWord(st.l);
  $("#quit").onclick = () => confirmBox("Leave this lesson? It won't be marked as done.", () => { const id = B.b.id; B = null; go({name:"book", id}); });
}
function finishLesson(){ try { navigator.vibrate && navigator.vibrate([12, 60, 18]); } catch(e){}
  const done = S.books[B.b.id] = S.books[B.b.id] || [], first = !done.includes(B.idx); if (first) done.push(B.idx);
  S.lessonDay = { d:today(), n:(S.lessonDay && S.lessonDay.d === today() ? S.lessonDay.n : 0) + 1 };
  if (B.b.type === "words") for (const st of B.steps) if (st.kind === "word" && st.l.card && !S.cards[st.l.id]) {   // learnt words join the flashcards, first review tomorrow
    S.cards[st.l.id] = schedule(undefined, 2).s; const t = today(); S.newDone[t] = S.newDone[t]||{}; S.newDone[t][st.l.card.deck] = (S.newDone[t][st.l.card.deck]||0) + 1; }
  const xp = first ? 10 + B.correct*2 : 3, adv = touchDay(xp);
  const id = B.b.id, score = `${B.correct}/${B.nq}`; B = null;
  $("#app").innerHTML = `<div class="player"><div class="player-in"><div class="done-screen"><div class="seal" aria-hidden="true"><svg viewBox="0 0 120 120" width="112"><path class="seal-ring" d="M60.0 6.0 L75.3 23.0 L98.2 21.8 L97.0 44.7 L114.0 60.0 L97.0 75.3 L98.2 98.2 L75.3 97.0 L60.0 114.0 L44.7 97.0 L21.8 98.2 L23.0 75.3 L6.0 60.0 L23.0 44.7 L21.8 21.8 L44.7 23.0Z" fill="none" stroke="var(--gold)" stroke-width="3" stroke-linejoin="round"/><circle class="seal-in" cx="60" cy="60" r="26" fill="var(--brand)"/><path class="seal-tick" d="M48 60l8 8 16-17" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg></div><div class="big">Lesson complete</div>${adv?streakBurst():""}
    <div class="tiles"><div class="tile"><b>+${xp}</b><span>XP</span></div><div class="tile"><b>${score}</b><span>Questions right</span></div></div></div><div class="pfoot"><button class="btn" id="cont">Continue</button></div></div></div>`;
  $("#cont").onclick = () => go({name:"book", id});
}

/* ======================= FINAL TEST ======================= */
let T = null;
function makeTest(y){
  const lines = lessonBooks(y).filter(b => b.lines && b.type !== "words").flatMap(b => b.lines.map(l => ({ l, b })));
  const qs = [], have = new Set(), decks = core(y.decks).filter(d => d.cards), fromCards = lines.length ? 30 : TEST_LEN;
  const fromCard = (d, c) => { if (have.has(c.b)) return false; const ds = pickDistractors(c, d.cards); if (ds.length < 3) return false; have.add(c.b);
    qs.push({ src:d.title, promptAr:c.fa && c.f.length < 60 ? c.f : null, q:c.fa && c.f.length < 60 ? "What does this mean?" : c.f, qAr:c.fa && c.f.length >= 60, answer:c.b, ansAr:arRatio(c.b) > .5, options:shuffle([c.b, ...ds]) }); return true; };
  const pools = decks.map(d => ({ d, p:shuffle(d.cards.filter(mcqOK)) })).filter(x => x.p.length);
  for (let round = 0; qs.length < fromCards && pools.some(x => x.p.length); round++)            // take turns between decks so every book is tested
    for (const x of pools) { if (qs.length >= fromCards) break; while (x.p.length && !fromCard(x.d, x.p.pop())); }
  for (const { l, b } of shuffle(lines)) { if (qs.length >= TEST_LEN) break; const q = bookQuiz(b, l); if (q) qs.push({ src:b.title, promptAr:q.prompt, q:q.q, answer:q.answer, ansAr:q.ansAr, options:q.options }); }
  return shuffle(qs);
}
function startTest(n, place){ T = { n, place:!!place, qs:makeTest(yearOf(n)), i:0, sel:null, wrong:[], right:0 }; renderTest(); }
function renderTest(){
  const q = T.qs[T.i]; if (!q) return finishTest();
  $("#app").innerHTML = `<div class="player"><div class="player-in"><div class="phead"><button class="x" id="quit" aria-label="Leave test">${ICON.x}</button><div class="bar"><i style="width:${T.i/T.qs.length*100}%;background:var(--gold)"></i></div><span class="count">${T.i+1}/${T.qs.length}</span></div>
    <div class="pbody"><div class="kicker">Year ${T.n} final test</div>
    ${q.promptAr?`<p class="line-ar" style="text-align:center;font-size:${q.promptAr.length<20?"2.2rem":"1.4rem"}">${esc(q.promptAr)}</p>`:""}
    <p class="q ${q.qAr?"ar":""}" style="${q.qAr?"text-align:right;font-size:1.3rem;line-height:1.9":""}">${esc(q.q)}</p>
    <div class="opts">${q.options.map((o,i)=>`<button class="opt ${i===T.sel?"sel":""} ${q.ansAr?"ar":""}" style="${q.ansAr?"text-align:right;font-size:1.15rem":""}" data-o="${i}">${esc(o)}</button>`).join("")}</div></div>
    <div class="pfoot"><button class="btn" id="next" ${T.sel===null?"disabled":""}>${T.i+1<T.qs.length?"Next question":"Finish test"}</button></div></div></div>`;
  document.querySelectorAll("[data-o]").forEach(x => x.onclick = () => { T.sel = +x.dataset.o; renderTest(); });
  $("#next").onclick = () => { if (q.options[T.sel] === q.answer) T.right++; else T.wrong.push({ ...q, given:q.options[T.sel] }); T.i++; T.sel = null; renderTest(); };
  $("#quit").onclick = () => confirmBox("Leave the test? This attempt won't count.", () => { const n=T.n; T = null; go({name:"year", n}); });
}
async function finishTest(){
  const score = T.right / T.qs.length, passed = score >= PASS, n = T.n;
  const rec = S.tests[n] = S.tests[n] || { attempts:0, best:0, passed:false }; rec.attempts++; rec.best = Math.max(rec.best, score);
  const firstPass = passed && !rec.passed;
  if (passed){ rec.passed = true; if (T.place && n < YEARS.length && !S.unlocked.includes(n+1)) S.unlocked.push(n+1); }   // the year test is practice; only the placement test skips ahead
  touchDay(firstPass ? 100 : 5);
  const wrong = T.wrong; T = null;
  if (passed && n < YEARS.length) { try { await loadYear(n+1); } catch(e){} }
  $("#app").innerHTML = `<div class="player"><div class="player-in"><div class="pbody"><div class="done-screen" style="padding:24px 0 8px"><div style="width:80px">${ICON.logo}</div><div class="big">${passed ? "Passed, alhamdulillah" : "Not yet"}</div>
    <div class="tiles"><div class="tile"><b>${pct(score)}</b><span>Your score</span></div><div class="tile"><b>${PASS*100}%</b><span>Pass mark</span></div></div>
    <p class="muted" style="margin:0;max-width:340px">${passed ? (n < YEARS.length ? `Year ${n+1} is now unlocked.` : "You have completed the five years. Your specialisation year is now open: choose the module you want to study further.") : "Review the questions below, keep up your flashcards, and try again when you're ready."}</p></div>
    ${wrong.length?`<p class="label">Questions to review (${wrong.length})</p><div class="stack review-list">${wrong.map(w=>`<div class="card">${w.promptAr?`<p class="line-ar" style="font-size:1.2rem;margin:0">${esc(w.promptAr)}</p>`:""}<p style="margin:0 0 6px;font-weight:700" class="${w.qAr?"ar":""}">${esc(w.q)}</p>
      <p class="small" style="margin:0;color:var(--ok)"><b>Correct:</b> ${esc(w.answer)}</p><p class="small" style="margin:4px 0 0;color:var(--bad)"><b>You chose:</b> ${esc(w.given)}</p></div>`).join("")}</div>`:""}
    </div><div class="pfoot"><button class="btn" id="cont">Continue</button></div></div></div>`;
  $("#cont").onclick = () => go({ name:"home" });
}

/* ======================= RENDER ======================= */
if (/[?&]dev=1/.test(location.search)) { S.dev = true; save(); } else if (/[?&]dev=0/.test(location.search)) { delete S.dev; save(); }
/* ﷺ and similar marks: always draw them with an Arabic font, at a readable size */
(function(){ const RX = /[ﷺﷻ﷽]/, AR = /[؀-ۿﷰ-﷿]/, LAT = /[A-Za-z]/, RUN = /([؀-ۿﷰ-﷿]+(?:[  ]+[؀-ۿﷰ-﷿]+)*)/;
  // In English text, Arabic phrases (رضي الله عنه, ﷺ) are isolated so they keep their order and use an Arabic font
  const skip = n => n.parentNode && n.parentNode.closest && n.parentNode.closest(".saw,svg,textarea,input,.ar,.ar-read,.line-ar,.word-ar,[dir=rtl]");
  const wrap = root => { const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: n => AR.test(n.nodeValue) && (RX.test(n.nodeValue) || LAT.test(n.nodeValue)) && !skip(n) ? 1 : 2 });
    const list = []; while (w.nextNode()) list.push(w.currentNode);
    for (const n of list){ const mixed = LAT.test(n.nodeValue), parts = n.nodeValue.split(mixed ? RUN : /([ﷺﷻ﷽])/), f = document.createDocumentFragment();
      for (const p of parts){ if (!p) continue; if (mixed ? AR.test(p) : RX.test(p)) { const s = document.createElement("bdi"); s.className = "saw"; s.dir = "rtl"; s.textContent = p; f.appendChild(s); } else f.appendChild(document.createTextNode(p)); }
      n.parentNode.replaceChild(f, n); } };
  new MutationObserver(ms => ms.forEach(m => m.addedNodes.forEach(n => n.nodeType === 1 ? wrap(n) : n.nodeType === 3 && n.parentNode && wrap(n.parentNode)))).observe(document.getElementById("app"), { childList:true, subtree:true });
})();
function checkUnlock(){                     // the next year opens when this year's lessons and books are read
  const n = Math.max(...S.unlocked); if (n >= YEARS.length) return;
  const y = yearOf(n); if (y.prepared && yearStatus(y).open) { S.unlocked.push(n+1); save(); setTimeout(() => toast(`Year ${n+1} is now open, alhamdulillah`), 400); }
}
function render(){ appBadge(); checkUnlock();
  const app = $("#app");
  if (!S.welcomed){ app.innerHTML = welcomeView(); bindWelcome(); return; }
  if (view.name === "home") app.innerHTML = homeView();
  else if (view.name === "year") app.innerHTML = yearView(view.n);
  else if (view.name === "book") { const b = bookById(view.id); if (b.type === "text" && !TEXTS[b.file]) { app.innerHTML = shell(`<p class="muted">Loading ${esc(b.title)}…</p>`); loadText(b.file).then(render, () => { toast("Could not load the text. Check your connection."); go({name:"year", n:b.year}); }); return; } app.innerHTML = bookView(view.id); }
  else if (view.name === "read") return openRead(view.id, view.i);
  else if (view.name === "search") app.innerHTML = searchView();
  else if (view.name === "spec") app.innerHTML = specView();
  else if (view.name === "library") app.innerHTML = libraryView();
  else if (view.name === "syllabus") app.innerHTML = syllabusView();
  else if (view.name === "settings") app.innerHTML = settingsView();
  else if (view.name === "unit") app.innerHTML = unitView(view.id);
  else app.innerHTML = profileView();
  app.querySelectorAll("[data-go]").forEach(b => b.onclick = () => go({ name:b.dataset.go }));
  app.querySelectorAll("[data-unit]").forEach(b => b.onclick = () => go({ name:"unit", id:b.dataset.unit }));
  app.querySelectorAll("[data-learn]").forEach(b => b.onclick = async () => { const [u, k] = b.dataset.learn.split("|"); await loadLearn(); startLearn(u, +k); });
  if (view.name === "home") { fillHome(); fitLearnCards();
    const ins = $("#inst"); if (ins) ins.onclick = async () => { INSTALL.prompt(); await INSTALL.userChoice; INSTALL = null; render(); };
    const ni = $("#noinst"); if (ni) ni.onclick = () => { S.noInstall = true; save(); render(); }; }
  app.querySelectorAll("[data-year]").forEach(b => b.onclick = () => go({ name:"year", n:+b.dataset.year }));
  app.querySelectorAll("[data-book]").forEach(b => b.onclick = () => go({ name:"book", id:b.dataset.book }));
  app.querySelectorAll("[data-lesson]").forEach(b => b.onclick = () => { if (!b.disabled) startLesson(view.id, +b.dataset.lesson); });
  app.querySelectorAll("[data-deck]").forEach(b => b.onclick = async () => { const d = allDecks().find(d=>d.id===b.dataset.deck);
    if (d.opt && !d.cards) { b.disabled = true; b.querySelector(".s").textContent = "Loading…"; try { await loadDeck(d); } catch(e){ toast("Could not load this deck. Check your connection."); b.disabled = false; return; } }
    if (d.opt) { S.optOn = S.optOn||{}; S.optOn[d.id] = true; save(); }
    startStudy([d]); });
  app.querySelectorAll("[data-study]").forEach(b => b.onclick = () => startStudy(studyDecks()));
  app.querySelectorAll("[data-test]").forEach(b => b.onclick = () => { if (!b.disabled) startTest(+b.dataset.test); });
  app.querySelectorAll("[data-startlesson]").forEach(b => b.onclick = () => { const [id, i] = b.dataset.startlesson.split("|"); startLesson(id, +i); });
  bindReadLinks(app);
  app.querySelectorAll("[data-spec]").forEach(b => b.onclick = () => go({ name:"spec" }));
  app.querySelectorAll("[data-pick]").forEach(b => b.onclick = () => { if (!specOpen()) return; const m = b.dataset.pick;
    confirmBox(`Choose ${m} as your specialisation?`, () => { S.spec = m; save(); render(); }); });
  const cs = $("#changespec"); if (cs) cs.onclick = () => confirmBox("Change your specialisation? Your progress in the five years is kept.", () => { S.spec = null; save(); render(); });
  const cn = $("#continue"); if (cn) cn.onclick = () => { const nl = nextLesson(); if (nl) startLesson(nl.b.id, nl.i); };
  app.querySelectorAll("[data-place]").forEach(b => b.onclick = () => { const n = +b.dataset.place; b.disabled = true; b.textContent = "Preparing the test…"; loadYear(n).then(() => startTest(n, true), () => { toast("Could not load the test. Check your connection."); b.disabled = false; }); });
  app.querySelectorAll("[data-libsub]").forEach(c => c.onclick = () => { S.libSub = c.dataset.libsub; save(); render(); });
  const la = $("#loadall"); if (la) la.onclick = async () => { la.disabled = true; la.textContent = "Loading the books…"; try { await Promise.all(LIB().map(b => loadText(b.file))); } catch(e){ toast("Some books could not load"); } INDEX = null; render(); };
  const sq = $("#sq"); if (sq){ sq.oninput = () => { view.q = sq.value; $("#sres").innerHTML = searchResults(sq.value); bindResults(); }; bindResults(); if (view.q !== undefined) { sq.focus(); sq.setSelectionRange(sq.value.length, sq.value.length); } }
  const sd = $("#sendall"); if (sd) sd.onclick = async () => { const ok = await sendReports(S.reports.filter(r=>!r.sent)); if (ok) { toast("Thank you, jazak Allahu khayran"); render(); } };
  ["en","ar"].forEach(l => { const sel = $(`#v-${l}`); if (sel) sel.onchange = () => { S.voices = S.voices||{}; S.voices[l] = sel.value; save(); }; });
  app.querySelectorAll("[data-vtest]").forEach(b => b.onclick = () => { if (!hasTTS()) return toast("This device can't read aloud"); const l = b.dataset.vtest; speechSynthesis.cancel(); AUD.token++;
    sayOne(l === "en" ? "Whoever takes a path seeking knowledge, Allah makes easy for him a path to Paradise." : "مَنْ سَلَكَ طَرِيقًا يَلْتَمِسُ فِيهِ عِلْمًا، سَهَّلَ اللهُ لَهُ بِهِ طَرِيقًا إِلَى الْجَنَّةِ", l, l === "en" ? 0.95 : 0.9, AUD.token); });
  if (hasTTS() && view.name === "settings" && !voicesFor("en").length) speechSynthesis.onvoiceschanged = () => { if (view.name === "settings") render(); };
  const av = $("#arvoice"); if (av) av.onchange = () => { S.arVoice = av.checked; save(); };
  const cl = $("#clang"); if (cl) cl.onchange = () => { S.cardLang = cl.value || null; save(); };
  const hk = $("#hk"); if (hk) hk.onchange = () => { S.harakat = hk.checked; save(); };
  app.querySelectorAll("[data-theme]").forEach(b => b.onclick = () => { S.theme = b.dataset.theme; save(); applyTheme(); render(); });
  fillLeaderboard();
  const mk = $("#markread"); if (mk) mk.onclick = () => confirmBox("Mark the whole book as read? This counts towards opening the next year.", () => { const b = bookById(mk.dataset.mark), n = lessonsOf(b); S.books[b.id] = [...Array(n).keys()]; save(); toast("Marked as read"); render(); });
  app.querySelectorAll("[data-off]").forEach(b => b.onclick = () => saveOffline(+b.dataset.off, b));
  const rm = $("#remind"); if (rm) rm.onchange = async () => { rm.disabled = true;
    if (rm.checked) { const err = await remindOn(); if (err) { rm.checked = false; toast(err); } else toast("Reminder on: 8pm, if you haven't studied yet"); }
    else { await remindOff(); toast("Reminder off"); } rm.disabled = false; };
  const tl = $("#tl"); if (tl) tl.onchange = () => { S.translit = tl.value; save(); toast("Saved"); };
  const ag = $("#advgrades"); if (ag) ag.onchange = () => { S.advancedGrades = ag.checked; save(); };
  const npd = $("#npd"); if (npd) npd.onchange = () => { S.newPerDay = +npd.value; save(); };
  const sk = $("#skipday"); if (sk) sk.onclick = () => { S.offset++; save(); render(); };
  const ft = $("#fasttrack"); if (ft) ft.onclick = () => { const y = yearOf(Math.max(...S.unlocked));
    if (!y.prepared) return confirmBox(`Year ${y.n} has no texts yet. Mark its final test as passed? (Testing only)`, () => {
      S.tests[y.n] = { attempts:1, best:1, passed:true }; if (y.n < YEARS.length && !S.unlocked.includes(y.n+1)) S.unlocked.push(y.n+1);
      save(); loadYear(Math.min(y.n+1, YEARS.length)).then(() => go({ name:"home" })); });
    confirmBox(`Mark every Year ${y.n} lesson done and every flashcard mastered, so you can try the final test? (Testing only)`, () => {
      y.books.forEach(b => S.books[b.id] = [...Array(lessonsOf(b)).keys()]);
      core(y.decks).forEach(d => d.cards.forEach(c => S.cards[c.id] = { ivl:MASTER_IVL+3, ease:2.5, reps:4, lapses:0, due:today()+10 }));
      S.log = S.log.concat(Array(60).fill(1)); save(); go({ name:"year", n:y.n }); }); };
  const rs = $("#reset"); if (rs) rs.onclick = () => confirmBox("Reset all progress, XP, flashcards and test results?", () => { S = fresh(); save(); go({ name:"home" }); });
}
applyTheme(); try { matchMedia("(prefers-color-scheme: dark)").addEventListener("change", applyTheme); } catch(e){}
(async function init(){
  $("#app").innerHTML = `<div class="done-screen" style="min-height:60vh"><div style="width:64px">${ICON.logo}</div><p class="muted">Loading…</p></div>`;
  try { await Promise.all(S.unlocked.map(loadYear)); }
  catch(e){ $("#app").innerHTML = `<div class="done-screen"><p><b>Couldn't load the lessons.</b></p><p class="muted small">Check your connection and refresh the page.</p></div>`; return; }
  render();
})();
