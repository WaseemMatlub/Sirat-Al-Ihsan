import os
import json,re
head=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'head.html')).read()
head=head.replace('<title>Deen Path</title>','<title>Ihsan</title>').replace('<span>Deen Path</span>','<span>Ihsan</span>')
css='''
.seg{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;background:var(--line);padding:4px;border-radius:14px}
.seg button{border:0;background:transparent;border-radius:10px;padding:10px 6px;font:inherit;font-weight:700;color:var(--muted);cursor:pointer}
.seg button.on{background:var(--surface);color:var(--ink);box-shadow:0 1px 3px rgba(0,0,0,.12)}
.setlist{background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden}
.setrow{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 14px;border-bottom:1px solid var(--line)}.setrow:last-child{border-bottom:0}
.setrow label{display:flex;flex-direction:column;gap:2px;min-width:0}.setrow label span{font-size:.8rem;color:var(--muted)}
.setrow select{max-width:140px}
.setgroup{margin-top:10px}.setgroup>summary{list-style:none;display:flex;align-items:center;gap:8px;padding:14px;background:var(--surface);border:1px solid var(--line);border-radius:16px;font-weight:700;color:var(--ink);cursor:pointer}
.setgroup>summary::-webkit-details-marker{display:none}.setgroup>summary::after{content:"›";margin-left:auto;font-size:1.3rem;color:var(--muted);transition:transform .2s}
.setgroup[open]>summary::after{transform:rotate(90deg)}.setgroup[open]>summary{margin-bottom:8px}
input.switch{appearance:none;-webkit-appearance:none;width:46px;height:28px;border-radius:99px;background:var(--line);position:relative;flex:none;cursor:pointer;transition:background .2s}
input.switch::after{content:"";position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.25);transition:transform .2s}
input.switch:checked{background:var(--brand)}input.switch:checked::after{transform:translateX(18px)}

.chip.iconbtn{background:var(--surface);border:1px solid var(--line);color:var(--ink);cursor:pointer;padding:5px 8px}.chip.iconbtn svg{width:16px;height:16px}
.coursebar{display:flex;flex-direction:column;align-items:stretch;gap:6px;width:100%;text-align:left;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:12px 14px;font:inherit;color:var(--ink);cursor:pointer}
.coursebar .pill{font-size:.66rem;padding:2px 7px;margin-left:4px;vertical-align:2px}
.carousel{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;margin:12px -16px 4px;padding:2px 16px 14px;scrollbar-width:none}
.carousel::-webkit-scrollbar{display:none}
.lcard{flex:0 0 80%;max-width:330px;scroll-snap-align:center;background:var(--surface);border:1px solid var(--line);border-radius:22px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 6px 18px rgba(60,50,20,.06)}
.lcard .pic{height:180px;display:grid;place-items:center}
.lcard .lbody{padding:12px 16px 4px;flex:1}.lcard h3{font-family:var(--display);font-size:1.22rem;margin:4px 0 2px;line-height:1.3}
.lcard .lbtn{display:flex;align-items:center;justify-content:center;gap:6px;margin:10px 0 0;border:0;background:var(--brand);color:var(--brand-ink);font:inherit;font-weight:800;font-size:.85rem;padding:15px;cursor:pointer}
.lcard .lbtn.off{background:var(--line);color:var(--muted);cursor:default}.lcard .lbtn svg{width:16px;height:16px}
.lcard.locked{opacity:.6}.lcard.locked .pic{filter:grayscale(.7)}
.minicard{display:flex;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:12px 14px;margin-top:10px}
.minicard .mi{width:38px;height:38px;border-radius:12px;display:grid;place-items:center;background:color-mix(in srgb,var(--gold) 14%,var(--surface));color:var(--brand)}.minicard .mi svg{width:20px;height:20px}
.small-btn{width:auto!important;padding:9px 16px!important;font-size:.8rem!important}

.reader .fs0 .ar-read{font-size:1.15rem}.reader .fs0 .en-read{font-size:.9rem}
.reader .fs1 .ar-read{font-size:1.3rem}.reader .fs1 .en-read{font-size:.97rem}
.reader .fs2 .ar-read{font-size:1.5rem}.reader .fs2 .en-read{font-size:1.04rem}
.reader .fs3 .ar-read{font-size:1.75rem}.reader .fs3 .en-read{font-size:1.14rem}
.reader .fs4 .ar-read{font-size:2rem}.reader .fs4 .en-read{font-size:1.25rem}
.reader .fs5 .ar-read{font-size:2.35rem}.reader .fs5 .en-read{font-size:1.38rem}
.reader .ar-read{line-height:2.2!important;word-spacing:.06em}
.reader .en-read{line-height:1.7;letter-spacing:.005em}
.reader .para{border-radius:12px;padding:4px 8px;margin:0 -8px;transition:background .25s}
.reader .para.speaking{background:color-mix(in srgb,var(--gold) 16%,transparent)}
.tool.listen{color:var(--brand);border-color:color-mix(in srgb,var(--brand) 40%,var(--line))}
.tool.listen.on{background:var(--brand);color:var(--brand-ink)}
body{letter-spacing:.003em}

.tags{display:inline-flex;flex-wrap:wrap;gap:4px;margin-top:4px}.tags .pill{font-size:.68rem;padding:2px 7px}
.item.lib-link{border-style:dashed}

.reader .ar-read{font-family:var(--arabic);direction:rtl;text-align:right;font-size:1.45rem;line-height:2.15;margin:0 0 6px}
.reader .en-read{margin:0 0 16px;color:var(--ink);line-height:1.6;padding-bottom:12px;border-bottom:1px dashed var(--line)}
.reader .en-read:last-child{border-bottom:0;padding-bottom:0}
.reader .card .ar-read+.ar-read{border-top:1px dashed var(--line);padding-top:8px}

.tools{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.tool{display:inline-flex;align-items:center;gap:6px;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:7px 12px;font:inherit;font-size:.82rem;font-weight:700;color:var(--muted)}
.tool svg{width:16px;height:16px}.tool.on{color:var(--warn);border-color:color-mix(in srgb,var(--gold) 50%,transparent)}
.tool:active{transform:scale(.96)}
.toast{position:fixed;left:50%;bottom:110px;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:10px 16px;border-radius:12px;font-size:.9rem;font-weight:600;z-index:60;max-width:90vw;text-align:center;animation:pop .3s ease-out}

.grades.two{grid-template-columns:1fr 1fr}
.grades.two .grade{padding:14px 8px;font-size:1.05rem}

/* calmer palette: warm cream base, green as an accent only */
:root{--bg:#FAF7F0;--line:#E9E2D3;--muted:#6B6B60;--ink:#1F2420}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141412;--surface:#1D1C19;--line:#302E29;--muted:#A19D92;--ink:#EEEBE3;--brand:#4DB58C;--brand-ink:#0B1410;--ok-soft:#1E2E24;--gold-soft:#3A2F17}}
:root[data-theme="dark"]{--bg:#141412;--surface:#1D1C19;--line:#302E29;--muted:#A19D92;--ink:#EEEBE3;--brand:#4DB58C;--brand-ink:#0B1410;--ok-soft:#1E2E24;--gold-soft:#3A2F17}
@media (prefers-color-scheme:dark){.today{box-shadow:none}.continue{box-shadow:none}}
.topbar{background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px)}
.today{background:var(--surface);color:var(--ink);border:1px solid var(--line);border-top:4px solid var(--gold);box-shadow:0 6px 18px rgba(60,50,20,.06)}
.today .nums div{background:color-mix(in srgb,var(--gold) 9%,var(--bg))}
.today .nums b{color:var(--brand)}
.today .nums span{color:var(--muted);opacity:1}
.hero{background:color-mix(in srgb,var(--c,var(--brand)) 8%,var(--surface));color:var(--ink);border:1px solid color-mix(in srgb,var(--c,var(--brand)) 22%,transparent)}
.hero h1{color:var(--c,var(--brand))}
.hero p{color:var(--muted);opacity:1}
.hero-art{opacity:.55!important}
.yr-badge{background:color-mix(in srgb,var(--brand) 10%,var(--surface));color:var(--brand)}
.year.current .yr-badge{background:var(--brand);color:var(--brand-ink)}
.btn.gold,.today .btn{background:var(--gold);color:#2A1E05;box-shadow:0 4px 0 color-mix(in srgb,var(--gold) 60%,#000)}

.modules{display:flex;flex-direction:column;gap:10px}
details.module{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:4px 12px}
details.module>summary{list-style:none;display:flex;align-items:center;gap:12px;padding:10px 0;cursor:pointer}
details.module>summary::-webkit-details-marker{display:none}
details.module>summary .m-txt{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
details.module>summary .t{font-weight:800;font-size:1.05rem}
details.module>summary .s{font-size:.82rem;color:var(--muted)}
details.module>summary .bar{margin-top:6px}
details.module[open]>summary{border-bottom:1px solid var(--line);margin-bottom:10px}
details.module>.stack{padding-bottom:12px}
.item.soon{opacity:.75;border-style:dashed}

.continue{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:18px;margin:0 0 14px;overflow:hidden;box-shadow:0 6px 18px rgba(14,90,67,.07)}
.continue h2{margin:2px 0 0;font-size:1.25rem;max-width:62%}
.continue .c-art{position:absolute;right:10px;top:8px;opacity:.95}
.continue .btn{width:auto;padding:12px 22px}
.week{display:flex;justify-content:space-between;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:10px 12px;margin:0 0 14px}
.wd{display:flex;flex-direction:column;align-items:center;gap:4px;font-size:.75rem;font-weight:700;color:var(--muted)}
.wd svg{filter:grayscale(1);opacity:.3}.wd.on svg{filter:none;opacity:1}
.wd.now span{color:var(--brand);text-decoration:underline;text-underline-offset:3px}
.art-ico{background:transparent!important;width:44px;height:48px;display:grid;place-items:center}
.hero{position:relative;overflow:hidden}.hero-art{position:absolute;right:-6px;bottom:-10px;opacity:.35;pointer-events:none}
.hero h1,.hero p{position:relative;max-width:78%}
ol.pts{margin:0;padding-left:1.4em}ol.pts li{margin:0 0 6px;line-height:1.5}ol.pts li::marker{color:var(--gold);font-weight:800}
.explain{margin:14px 0 120px;border-left:4px solid var(--gold);background:color-mix(in srgb,var(--gold) 9%,var(--surface));border-radius:12px;padding:12px 14px}
.burst{display:flex;gap:12px;align-items:center;text-align:left;background:color-mix(in srgb,var(--gold) 14%,var(--surface));border:1px solid color-mix(in srgb,var(--gold) 40%,transparent);border-radius:16px;padding:12px 16px;animation:pop .5s ease-out}
.burst b{display:block}.burst span{font-size:.85rem;color:var(--muted)}
@keyframes pop{0%{transform:scale(.8);opacity:0}70%{transform:scale(1.04)}100%{transform:scale(1);opacity:1}}
@media (prefers-reduced-motion:reduce){.burst{animation:none}}
input.search,textarea.search{width:100%;box-sizing:border-box;font:inherit;font-size:1rem;padding:14px 16px;border-radius:14px;border:1.5px solid var(--line);background:var(--surface);color:var(--ink)}
input.search:focus,textarea.search:focus{outline:none;border-color:var(--brand);box-shadow:0 0 0 3px color-mix(in srgb,var(--brand) 18%,transparent)}
nav.tabs .in{grid-template-columns:repeat(4,1fr)}

.welcome{min-height:100%;display:grid;place-items:center;padding:28px 18px;background:radial-gradient(120% 60% at 50% 0%,color-mix(in srgb,var(--gold) 18%,var(--bg)),var(--bg))}
.welcome-in{max-width:440px;width:100%;text-align:center}
.w-logo{width:72px;margin:0 auto 6px}
.w-ar{font-size:2.4rem;color:var(--brand);margin:0;line-height:1.4}
.welcome h1{font-size:2.6rem;margin:0}
.w-tag{color:var(--muted);margin:6px 0 22px;font-size:1.05rem}
.w-points{display:grid;gap:10px;text-align:left;margin-bottom:20px}
.w-points div{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 14px;display:grid;gap:2px}
.w-points span{color:var(--muted);font-size:.9rem}
.w-hadith{font-family:var(--display);font-size:1.05rem;margin:0 0 18px}
.w-hadith span{display:block;font-family:var(--body);font-size:.78rem;color:var(--muted);margin-top:4px;font-style:italic}
.coming{display:grid;gap:8px}
.item[disabled]{opacity:.8}
'''
head=head.replace('</style>',css+'</style>',1)
meta=json.load(open('data/meta.json'))
import glob as _g, os as _o
meta['decks']={_o.path.basename(f)[:-5]:len(json.load(open(f))) for f in _g.glob('data/decks/*.json')}
meta['lines']={_o.path.basename(f)[:-5]:len(json.load(open(f))) for f in _g.glob('data/lines/*.json')}
for _k in ['1','2','3','4','5','fard']: meta.pop(_k, None)
meta['texts']={_o.path.basename(f)[:-5]:len(json.load(open(f))['sections']) for f in _g.glob('data/texts/*.json')}
meta['textsAudio']={_o.path.basename(f)[:-5]:any(x.get('aud_en') or x.get('audio') for x in json.load(open(f))['sections']) for f in _g.glob('data/texts/*.json')}
meta['textsAi']={_o.path.basename(f)[:-5]:bool(json.load(open(f)).get('ai')) for f in _g.glob('data/texts/*.json')}
meta['textsEn']={_o.path.basename(f)[:-5]:(lambda d: bool(d.get('bilingual') or d.get('ai') or any(x.get('en') for x in d['sections'])))(json.load(open(f))) for f in _g.glob('data/texts/*.json')}
js=open('app3.js').read().replace('/*META*/',json.dumps(meta))
open('index.html','w').write(head+'<script>\n'+js+'\n</script>\n</body>\n</html>\n')
print('ok',len(head)+len(js))

# ---- PWA: manifest link, icons, service worker (registered only on the real host) ----
import hashlib, glob
h=open('index.html').read()
ver=hashlib.sha1((h+''.join(open(f,'rb').read().hex()[:2000] for f in sorted(glob.glob('data/*.json')))).encode()).hexdigest()[:10]
h=h.replace('</head>','<link rel="manifest" href="manifest.json"><meta name="theme-color" content="#0E5A43"><link rel="apple-touch-icon" href="icon-192.png"><meta name="apple-mobile-web-app-capable" content="yes"></head>',1)
h=h.replace('</body>','<script>if("serviceWorker" in navigator && /github\\.io$/.test(location.hostname)) navigator.serviceWorker.register("sw.js?v=%s");</script></body>'%ver,1)
open('index.html','w').write(h)
open('sw.js','w').write("""const V="ihsan-%s", D="ihsan-data", F="ihsan-fonts";
const CORE=["./","index.html","manifest.json","icon-192.png","icon-512.png","data/meta.json"];
self.addEventListener("push",e=>{let d={};try{d=e.data.json()}catch(x){d={title:"Ihsan",body:e.data?e.data.text():""}} e.waitUntil(self.registration.showNotification(d.title||"Ihsan",{body:d.body||"",icon:"icon-192.png",badge:"icon-192.png",tag:"streak"}))});
self.addEventListener("notificationclick",e=>{e.notification.close(); e.waitUntil(clients.matchAll({type:"window"}).then(ws=>{for(const w of ws){if("focus" in w) return w.focus()} return clients.openWindow("./")}))});
self.addEventListener("install",e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k.startsWith("ihsan-")&&![V,D,F].includes(k)).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
/* Three stores: V = the app itself (replaced on each update), D = lessons, books and audio (kept across updates, refreshed in the background),
   F = fonts. So anything learnt or saved for offline stays available without internet. */
self.addEventListener("fetch",e=>{const r=e.request; if(r.method!=="GET") return; const u=new URL(r.url);
  if(/fonts\\.(googleapis|gstatic)\\.com$/.test(u.hostname)){ e.respondWith(caches.open(F).then(c=>c.match(r).then(hit=>hit||fetch(r).then(res=>{if(res.ok||res.type==="opaque")c.put(r,res.clone());return res})))); return; }
  if(u.origin!==location.origin) return;
  if(u.pathname.endsWith("config.json")) return;
  if(r.mode==="navigate"||r.destination==="document"){ e.respondWith(fetch(r).then(res=>{caches.open(V).then(c=>c.put("index.html",res.clone()));return res}).catch(()=>caches.match("index.html"))); return; }
  if(u.pathname.endsWith("fixes.json")){ e.respondWith(fetch(r).then(res=>{caches.open(D).then(c=>c.put(u.pathname,res.clone()));return res}).catch(()=>caches.match(u.pathname))); return; }
  if(/\\/(data|audio)\\//.test(u.pathname)){ const key=u.origin+u.pathname; e.respondWith(caches.open(D).then(c=>c.match(key).then(hit=>{const net=fetch(r).then(res=>{if(res.ok)c.put(key,res.clone());return res}).catch(()=>hit);return hit||net}))); return; }
  e.respondWith(caches.match(r,{ignoreSearch:true}).then(hit=>hit||fetch(r).then(res=>{if(res.ok)caches.open(V).then(c=>c.put(r,res.clone()));return res})))});
"""%ver)
print("pwa",ver)
