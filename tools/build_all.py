import json,re,collections,os,sys
sys.path.insert(0,'tools'); from fixjoin import fixjoin
from honorifics import honor_all
NOHONOR={'quran','roots','verbs1','verbs2'}  # dictionary glosses / Qur'an vocab: left untouched
from wordfreq import zipf_frequency as Z
J=lambda f: json.load(open(f'json/{f}.json'))
STRIP=lambda s: re.sub(r'[ً-ٰٟۖ-ۭـ]','',s)
HAM=lambda s: STRIP(s).replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ٱ','ا').replace('ء','ا').replace('ؤ','و').replace('ئ','ي').replace('ى','ي')
def card(id,f,b,fa=0,ba=0,s='',ex='',exr='',ai=0,g=''):
    c={'id':id,'f':f,'b':b}
    for k,v in dict(fa=fa,ba=ba,s=s,ex=ex,exr=exr,ai=ai,g=g).items():
        if v: c[k]=v
    return c
meta={}
def save(n,books,decks,opt=None):
    """opt: optional decks, saved one file each (data/decks/<id>.json) and loaded only when a student opens them."""
    opt=opt or {}
    os.makedirs('app/data/decks',exist_ok=True)
    for k,v in opt.items():
        v=honor_all(v); attach_tr(k,v)
        json.dump(v,open(f'app/data/decks/{k}.json','w'),ensure_ascii=False,separators=(',',':'))
    books=honor_all(books); decks={k:(v if k in NOHONOR else honor_all(v)) for k,v in decks.items()}
    for dk, cards in decks.items(): attach_tr(dk, cards)
    json.dump({'books':books,'decks':decks},open(f'app/data/year{n}.json','w'),ensure_ascii=False,separators=(',',':'))
    meta[n]={'books':{k:len(v) for k,v in books.items()},'decks':{k:len(v) for k,v in decks.items()},'opt':{k:len(v) for k,v in opt.items()}}
    print('year',n,meta[n],os.path.getsize(f'app/data/year{n}.json')//1024,'KB')
def attach_tr(dk, cards):
    """translations: tools/<deck>_<lang>.json, one {f,b} per card in deck order (AI, needs review)"""
    for lang in ('en','ar','de','tr','ur'):
        tp = f'tools/{dk}_{lang}.json'
        if os.path.exists(tp):
            for c, t in zip(cards, json.load(open(tp))): c.setdefault('tr', {})[lang] = {**t, 'ai': 1}
NOTES=re.compile(r'\[\[.*?\]\]',re.S)
def fb(f,pre,F='Front',B='Back',fa=1,ba=0,s=lambda r:''):
    out=[]
    for i,r in enumerate(J(f)):
        a,b=r.get(F,'').strip(),r.get(B,'').strip()
        if a and b: out.append(card(f'{pre}{i}',a,b,fa=fa,ba=ba,s=s(r)))
    return out
def bilingual(f,pre):
    """Q&A where each field is 'English / Arabic': English shown, Arabic as the ar translation"""
    out=[]
    for i,r in enumerate(J(f)):
        q,a=r['Question'].strip(),r['Answer'].strip()
        if not(q and a): continue
        qs,as_=q.rsplit(' / ',1) if ' / ' in q else (q,''),a.rsplit(' / ',1) if ' / ' in a else (a,'')
        c=card(f'{pre}{i}',qs[0].strip(),as_[0].strip(),s=r.get('Bayt',''))
        if re.search('[\u0600-\u06FF]',qs[1]+as_[1]) and qs[1] and as_[1]: c['tr']={'ar':{'f':qs[1].strip(),'b':as_[1].strip()}}
        out.append(c)
    return out
def lines(f,pre,note=lambda r:r.get('Notes','')):
    out=[]
    for i,r in enumerate(J(f)):
        if r.get('Arabic','').strip() and r.get('English','').strip():
            out.append({'id':f'{pre}{i}','ar':r['Arabic'],'en':r['English'],'note':note(r)[:1500]})
    return out
def qa(f,pre,ar=False):
    out=[]
    for i,r in enumerate(J(f)):
        q=re.sub(r'^\s*\d+\)\s*','',r['Question']).strip(); a=r['Answer'].strip()
        if q and a: out.append(card(f'{pre}{i}',q,a,fa=int(ar),ba=int(ar)))
    return out
# ---------- YEAR 1 ----------
y1=json.load(open('year1.json'))
quran=[card(v['id'],v['ar'],v['en'],fa=1,s=f"{v['pos']} · #{v['rank']} most frequent",ex=v['ayah'],exr=f"Qur'an {v['ref']} · knowing words 1–{v['rank']} covers {v['cov']}% of the Qur'an",ai=int(v['src']=='ai')) for v in y1['vocab']]
nur=[]
for ci,ch in enumerate(y1['nur']):
    for c in ch['cards']: nur.append(card('nur'+c['id'][1:],c['q'],c['a'],g=ch['title']))
bk=J('Hadith__Sahih_Bukhari')
signs=[{'id':f"sg{r['Hadithnumber']}",'ar':r['Arabic'],'en':fixjoin(r['English']),'note':f"Sahih al-Bukhari {r['Hadithnumber']}"} for r in bk if r['Chapter'].startswith('Afflictions')]
from authored_tajwid import T as _TJ
from authored_seerah import S as _SR
_aw=lambda rows,pre: [dict(card(f'{pre}{i}',q,a),aw=1) for i,(q,a) in enumerate(rows)]
save(1,{'tahawiyya':y1['tahawiyya'],'umm':y1['umm'],'signs':signs},
       {'tajwid':_aw(_TJ,'tj'),'seerah1':_aw(_SR,'sr'),'quran':quran,'nur':nur,'ajr':qa('Nahw__Ajrumiyyah_QA','aj'),'bina':qa('Sarf__Bina_al-Afaal','bn'),'izzi':qa('Sarf__Tasreef_Izzi','iz')})
# ---------- verbs (merge, dedup, rank by MSA frequency) ----------
seen={};
for f in ['Arabic_Verbs__2000_Most_Frequent','Arabic_Verbs__1800_Most_Frequent']:
    for r in J(f):
        k=(STRIP(r['Maadi']),r['Verb_Form'])
        if k in seen or not r['English'].strip(): continue
        sc=(Z(STRIP(r['Mudaari']),'ar')+Z(STRIP(r['Masdar']),'ar')*1.2 + (Z(STRIP(r['Maadi']),'ar') if len(STRIP(r['Maadi']))>=3 and STRIP(r['Maadi']) not in ('على','علي','كان','عن','من','قد','بعد','قبل','مع','ان','الى') else 0)*0.5)/2.7
        seen[k]=(sc,r)
verbs=sorted(seen.values(),key=lambda x:-x[0])
vc=[card(f'vb{i}',r['Maadi'],r['English'],fa=1,s=f"Form {r['Verb_Form']}",ex=f"{r['Maadi']} – {r['Mudaari']} – {r['Masdar']}",exr='past – present – verbal noun') for i,(sc,r) in enumerate(verbs)]
print('verbs merged',len(vc))
# ---------- Qur'an roots ranked by corpus frequency ----------
rootf=collections.Counter()
for line in open('morph.txt',encoding='utf-8'):
    m=re.search(r'ROOT:([^|\t]+)',line)
    if m: rootf[HAM(m.group(1))]+=1
roots=[]
for i,r in enumerate(J('Quran_Roots')):
    k=HAM(r['Front'].replace('-','').replace(' ',''))
    if r['Back'].strip(): roots.append((rootf.get(k,0),r))
roots.sort(key=lambda x:-x[0])
print('roots matched',sum(1 for n,_ in roots if n),'of',len(roots))
rc=[card(f'rt{i}',' '.join(r['Front'].replace('-',' ').split()),r['Back'],fa=1,s=(f'#{i+1} · {n} occurrences in the Qur\'an' if n else 'Qur\'anic root')) for i,(n,r) in enumerate(roots[:1000])]
# ---------- YEAR 2 ----------
mus=J('Hadith__Sahih_Muslim')
signs2=[{'id':f"sm{r['Hadithnumber']}",'ar':r['Arabic'],'en':fixjoin(r['English']),'note':f"Sahih Muslim {r['Hadithnumber']}"} for r in mus if r['Chapter'].startswith('The Book of Tribulations')]
mufr=[]
for i,r in enumerate(J('Mufradat_al-Raghib__English')):
    if r['Root'].strip() and r['Definition'].strip():
        c=card(f'mf{i}',r['Root'].strip(),NOTES.sub('',r['Definition']).strip(),fa=1); c['lang']='en'
        if r.get('Original','').strip(): c['tr']={'ar':{'f':r['Root'].strip(),'b':NOTES.sub('',r['Original']).strip()}}
        mufr.append(c)
burda=fb('Qasida_al-Burdah__','bd')
from jazariyya import V as _JZ
save(2,{'jawhara':lines('Aqeedah_Ashari__Jawharat_al-Tawhid','jw'),'signs2':signs2,'jazariyya':[{'id':f'jz{i}','ar':a,'en':e,'note':'','aw':1} for i,(ch,a,e) in enumerate(_JZ)]},
       {'quduri':qa('Fiqh_Hanafi__Mukthasar_Quduri_QA','qd'),'roots':rc,'verbs1':vc[:700],'ithaf':qa('Fiqh_Hanafi__Ithaf_al-Talib','it',ar=True),
        'qatr':bilingual('Nahw__Sharh_Qatr_al-Nada_QA','qt'),'burda':burda},
       {'mufradat':mufr,'themed':fb('Arabic_Themed_Dictionary','th','Singular','English',s=lambda r:r.get('Category','')),
        'sirr':qa('Sufism__Secret_of_Secrets','ss'),'naqsh':qa('Sufism__The_Praiseworthy_Etiquettes_of_the_Naqshbandi_Path','nq')})
# ---------- YEAR 3 ----------
maj=lines('Fiqh_Hanafi__99_Maxims_-_Al-Majalla_al-Ahkam_al-Adaliyyah','mj',note=lambda r:('Explanation: '+r.get('Explanation','')+'\n\nExample: '+r.get('Example','')).strip())
hw=fb('Hans_Wehr_Core_Vocabulary','hw','Arabic','English')
save(3,{'majalla':maj},{'nasafiyyah':qa('Aqeedah_Maturidi__Shar_al-Aqid_al-Nasafiyyah_QA','ns'),'kanz':qa('Fiqh_Hanafi__Kanz_al_Daqaiq','kz'),'verbs2':[dict(c,id='v2'+c['id'][2:]) for c in vc[700:1400]]},
       {'sharhizzi':bilingual('Sarf__Sharh_Tasreef_Izzi','sz'),'jalalayn':fb('Tafsir__Al-Jalalayn','jl',fa=0),'msa1':hw[:3400],
        'fuqaha':fb('Fiqh__Mujam_Lughat_al-Fuqaha','lf','Arabic','English'),'ghawth':qa('Sufism__The_Answer_Concerning_the_Ghawth','gw'),
        'qasaid':fb('Qasida_Collection__Islamic_Poetry_from_Around_the_World','qc')})
# ---------- YEAR 4 ----------
# al-Hidayah: 25,000 cards in four parts, cut where a chapter's numbering restarts
_h=qa('Fiqh_Hanafi__Al-Hidayah','hd'); _raw=J('Fiqh_Hanafi__Al-Hidayah')
_starts=[i for i,r in enumerate(_raw) if re.match(r'\s*1\.',r['Question'])]
_cuts=[min(_starts,key=lambda x:abs(x-len(_raw)*k/4)) for k in (1,2,3)]
_ids=[f'hd{i}' for i in range(len(_raw))]; _pos={c['id']:k for k,c in enumerate(_h)}
_bounds=[0]+[next((k for k,c in enumerate(_h) if int(c['id'][2:])>=cut),len(_h)) for cut in _cuts]+[len(_h)]
HID=[_h[_bounds[k]:_bounds[k+1]] for k in range(4)]
print('hidayah parts',[len(x) for x in HID])
save(4,{},{'mughni':bilingual('Nahw__Mukthasar_Mughni_al-Labib_QA','mg'),'iqtisad':qa('Aqeedah_Ashari__Al-Iqtisad_fi_al-Itiqad_QA','iq')},
       {'msa2':hw[3400:],'qushayri':fb('Tafsir__Al-Qushayris_Lataif_Al-Isharat','qs',fa=0),'mercy':qa('Fiqh__Mercy_in_the_Difference_of_the_Four_Schools_of_Law','mc'),
        'nuqaya':qa('Fiqh_Hanafi__Nuqaya','nu',ar=True),'philosophy':fb('Dictionary_of_Arabic_Philosophy','ph'),
        'poetry':fb('Classical_Arabic_Poetry_Collection','cp'),'hidaya1':HID[0],'hidaya2':HID[1]})
# ---------- YEAR 5 ----------
save(5,{},{'alfiyya':bilingual('Nahw__Alfiyyah_ibn_Malik_QA','af'),'proofs':qa('Fiqh_Hanafi__Fiqh_al_Imam_Key_Proofs','kp')},{'hidaya3':HID[2],'hidaya4':HID[3]})
# ---------- FARD 'AYN (optional, before Year 1) ----------
_nur=qa('Fiqh_Hanafi__Nur_al-Idah','nur'); _qd=qa('Fiqh_Hanafi__Mukthasar_Quduri_QA','qd')
def pick(cards,pat,pre): 
    rx=re.compile(pat,re.I); return [dict(c,id=pre+c['id']) for c in cards if rx.search(c['f'])]
_umm=lines('Aqeedah_Ashari__Umm_al-Barahin','u')
_zk0=next(i for i,r in enumerate(J('Fiqh_Hanafi__Mukthasar_Quduri_QA')) if i>370 and re.search('Zaka',r['Question']))
FARD={'fard_aqeedah':[card('fa'+l['id'],l['ar'],l['en'],fa=1) for l in _umm],
      'fard_tahara':pick(_nur,r'\b(water|wud[uū]|ablution|ghusl|bath|tayammum|purif|impur|najas|menstr|istinj|khuff|socks)','f'),
      'fard_salah':pick(_nur,r'\b(pray|prayer|salah|sal[aā]t|rak.?ah|sujud|prostrat|qibla|adhan|imam|witr|qada|makeup|recit)','f'),
      'fard_sawm':pick(_nur,r'\b(fast|ramadan|suhur|iftar|i.?tikaf|kaffar)','f'),
      'fard_zakat':[dict(c,id='f'+c['id']) for c in _qd if 'qd' in c['id'] and _zk0<=int(c['id'][2:])<467],
      'fard_halal':[dict(c,id='f'+c['id']) for c in _qd if 2019<=int(c['id'][2:])<2069]}
for k,v in FARD.items():
    v=honor_all(v); json.dump(v,open(f'app/data/decks/{k}.json','w'),ensure_ascii=False,separators=(',',':'))
meta['fard']={k:len(v) for k,v in FARD.items()}; print('fard',meta['fard'])
json.dump(meta,open('app/data/meta.json','w'))
print('top verbs',[c['f']+'='+c['b'] for c in vc[:12]])
print('top roots',[c['f'] for c in rc[:10]])
