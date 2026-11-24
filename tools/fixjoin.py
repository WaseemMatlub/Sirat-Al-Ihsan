import re
from wordfreq import zipf_frequency as Z
CAPOK={'you','i','in','on','if','as','at','by','his','her','our','not','no','for','from','with','the','he','what','they','she','we','it','and','but','then','his','this','when','so'}
def fixjoin(text):
    out=[]
    for tok in re.split(r'(\s+)',text):
        m=re.match(r'^([^A-Za-z]*)([A-Za-z]+)([^A-Za-z]*)$',tok)
        if not m or len(m.group(2))<5: out.append(tok);continue
        w=m.group(2); lw=w.lower()
        if Z(lw,'en')>0: out.append(tok);continue
        best=None
        for i in range(1,len(w)):
            a,b=w[:i],w[i:]
            if len(a)==1 and a.lower() not in('a','i'): continue
            if len(b)<2: continue
            if w[0].isupper() and not (a.lower() in CAPOK or b[0].isupper()): continue
            if Z(a.lower(),'en')>=3.3 and Z(b.lower(),'en')>=3.0:
                s=min(Z(a.lower(),'en'),Z(b.lower(),'en'))
                if not best or s>best[0]: best=(s,i)
        out.append(m.group(1)+w[:best[1]]+' '+w[best[1]:]+m.group(3) if best else tok)
    return ''.join(out)
if __name__=='__main__':
    import json
    bk=json.load(open('json/Hadith__Sahih_Bukhari.json'))
    import difflib
    ch=[]
    for r in bk:
        if not r['Chapter'].startswith('Afflictions'): continue
        a=r['English'].split(); b=fixjoin(r['English']).split()
        ch+= [x for x in a if x not in b]
    print(len(ch), ch[:120])
