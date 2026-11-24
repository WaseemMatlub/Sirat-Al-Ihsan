const V="ihsan-539aea514f";
const CORE=["./","index.html","manifest.json","icon-192.png","icon-512.png","data/meta.json","data/year1.json"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{const r=e.request; if(r.method!=="GET"||new URL(r.url).origin!==location.origin) return;
  if(r.mode==="navigate"||r.destination==="document"){ e.respondWith(fetch(r).then(res=>{caches.open(V).then(c=>c.put(r,res.clone()));return res}).catch(()=>caches.match(r,{ignoreSearch:true}).then(h=>h||caches.match("index.html")))); return; }
  e.respondWith(caches.open(V).then(c=>c.match(r,{ignoreSearch:true}).then(hit=>{const net=fetch(r).then(res=>{if(res.ok)c.put(r,res.clone());return res}).catch(()=>hit);return hit||net})))});
