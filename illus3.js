// ---- course illustrations: one scene per course, drawn from exact geometry (no hand-drawn wobble), 360×200
const ILL = (() => {
  let n = 0;
  const f = v => +v.toFixed(2);
  // seeded random so every render is identical
  const rnd = seed => () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  // pointed (two-centred) arch: x,y = left springing point, w = span, k = sharpness (radius / span)
  const archD = (x, y, w, k = .8, foot = 0) => { const r = w * k, h = Math.sqrt(r * r - (r - w / 2) ** 2);
    return `M${f(x)} ${f(y + foot)}V${f(y)}A${f(r)} ${f(r)} 0 0 1 ${f(x + w / 2)} ${f(y - h)}A${f(r)} ${f(r)} 0 0 1 ${f(x + w)} ${f(y)}V${f(y + foot)}Z`; };
  const archH = (w, k = .8) => { const r = w * k; return Math.sqrt(r * r - (r - w / 2) ** 2); };
  // onion dome on a drum; returns svg
  const dome = (cx, base, w, h, fill, fin = "#E9C46A") => {
    const d = `M${f(cx - w / 2)} ${f(base)}C${f(cx - w / 2)} ${f(base - h * .55)} ${f(cx - w * .32)} ${f(base - h * .82)} ${f(cx)} ${f(base - h)}C${f(cx + w * .32)} ${f(base - h * .82)} ${f(cx + w / 2)} ${f(base - h * .55)} ${f(cx + w / 2)} ${f(base)}Z`;
    const t = base - h;
    return `<path d="${d}" fill="${fill}"/><rect x="${f(cx - .9)}" y="${f(t - 9)}" width="1.8" height="9" fill="${fin}"/><circle cx="${f(cx)}" cy="${f(t - 10.5)}" r="2" fill="${fin}"/>` +
      `<path d="M${f(cx + 1.2)} ${f(t - 19)}a4.4 4.4 0 1 0 0 6.6a3.4 3.4 0 1 1 0 -6.6z" fill="${fin}"/>`;
  };
  const minaret = (cx, base, w, h, fill, accent) => {
    const top = base - h, bw = w * 1.55;
    return `<rect x="${f(cx - w / 2)}" y="${f(top)}" width="${f(w)}" height="${f(h)}" fill="${fill}"/>` +
      `<rect x="${f(cx - bw / 2)}" y="${f(top + h * .28)}" width="${f(bw)}" height="${f(w * .45)}" rx="1" fill="${fill}"/>` +
      `<rect x="${f(cx - bw / 2)}" y="${f(top + h * .28 + w * .45)}" width="${f(bw)}" height="${f(w * .18)}" fill="${accent}" opacity=".55"/>` +
      `<path d="M${f(cx - w * .62)} ${f(top)}L${f(cx)} ${f(top - w * 2.1)}L${f(cx + w * .62)} ${f(top)}Z" fill="${fill}"/>` +
      `<rect x="${f(cx - .7)}" y="${f(top - w * 2.1 - 6)}" width="1.4" height="6" fill="${accent}"/><circle cx="${f(cx)}" cy="${f(top - w * 2.1 - 7)}" r="1.5" fill="${accent}"/>`;
  };
  // date palm: straight trunk with rings, fronds arranged symmetrically
  const palm = (x, base, h, fill, lean = 0) => {
    const tx = x + lean, ty = base - h; let s = `<path d="M${f(x - 2.4)} ${f(base)}Q${f(x + lean * .4 - 1.6)} ${f(base - h * .5)} ${f(tx - 1.2)} ${f(ty)}L${f(tx + 1.2)} ${f(ty)}Q${f(x + lean * .4 + 1.6)} ${f(base - h * .5)} ${f(x + 2.4)} ${f(base)}Z" fill="${fill}"/>`;
    const L = h * .42;
    [-160, -130, -100, -75, -50, -20, 10, 40].forEach(a0 => { const a = a0 * Math.PI / 180, ex = tx + Math.cos(a) * L, ey = ty + Math.sin(a) * L + L * .32,
      mx = tx + Math.cos(a) * L * .55, my = ty + Math.sin(a) * L * .55 - L * .12, nx = -Math.sin(a) * L * .09, ny = Math.cos(a) * L * .09;
      s += `<path d="M${f(tx)} ${f(ty)}Q${f(mx + nx)} ${f(my + ny)} ${f(ex)} ${f(ey)}Q${f(mx - nx)} ${f(my - ny)} ${f(tx)} ${f(ty)}Z" fill="${fill}"/>`; });
    return s + `<circle cx="${f(tx)}" cy="${f(ty + 2)}" r="2.2" fill="${fill}"/>`;
  };
  const stars = (seed, count, y1, fill = "#FFF6DD") => { const r = rnd(seed); let s = "";
    for (let i = 0; i < count; i++) s += `<circle cx="${f(r() * 360)}" cy="${f(r() * y1)}" r="${f(.5 + r() * 1.1)}" fill="${fill}" opacity="${f(.45 + r() * .55)}"/>`; return s; };
  // eight-pointed star (khatam)
  const khatam = (cx, cy, r, fill) => { let p = ""; for (let i = 0; i < 16; i++) { const a = Math.PI / 8 * i - Math.PI / 2, rr = i % 2 ? r * .62 : r; p += `${i ? "L" : "M"}${f(cx + Math.cos(a) * rr)} ${f(cy + Math.sin(a) * rr)}`; }
    return `<path d="${p}Z" fill="${fill}"/>`; };
  const grad = (id, stops, x2 = 0, y2 = 1) => `<linearGradient id="${id}" x1="0" y1="0" x2="${x2}" y2="${y2}">${stops.map(([o, c, a]) => `<stop offset="${o}" stop-color="${c}"${a != null ? ` stop-opacity="${a}"` : ""}/>`).join("")}</linearGradient>`;
  const rgrad = (id, cx, cy, r, stops) => `<radialGradient id="${id}" cx="${cx}" cy="${cy}" r="${r}">${stops.map(([o, c, a]) => `<stop offset="${o}" stop-color="${c}"${a != null ? ` stop-opacity="${a}"` : ""}/>`).join("")}</radialGradient>`;

  const S = {
    // Aqeedah: the night sky over the desert, a masjid under the crescent
    aqeedah: p => `<defs>${grad(p + "s", [[0, "#06202B"], [.5, "#0F4A4D"], [.82, "#4E7C6A"], [1, "#E7B877"]])}${rgrad(p + "g", .7, .3, .42, [[0, "#FFF1CF", .5], [1, "#FFF1CF", 0]])}
      ${grad(p + "d1", [[0, "#D59A57"], [1, "#9A6232"]])}${grad(p + "d2", [[0, "#AC6E3B"], [1, "#6E4123"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}s)"/><rect width="360" height="200" fill="url(#${p}g)"/>${stars(7, 46, 110)}
      <path d="M262 40a26 26 0 1 0 19.5 43.2a20.4 20.4 0 1 1 -19.5 -43.2z" fill="#FFE7AE"/>
      <path d="M0 150C70 128 120 142 190 136S300 120 360 130V200H0Z" fill="url(#${p}d1)"/>
      <g fill="#0E3534">${minaret(146, 146, 7, 52, "#0E3534", "#E9C46A")}${minaret(234, 146, 7, 52, "#0E3534", "#E9C46A")}
        <rect x="158" y="114" width="64" height="32"/>${dome(190, 116, 46, 34, "#0E3534")}<rect x="164" y="112" width="52" height="4"/>
        <path d="${archD(182, 130, 16, .75, 16)}" fill="#F2C977" opacity=".9"/><path d="${archD(166, 132, 9, .75, 8)}" fill="#F2C977" opacity=".55"/><path d="${archD(205, 132, 9, .75, 8)}" fill="#F2C977" opacity=".55"/></g>
      <path d="M0 172C90 156 170 170 250 162S330 158 360 160V200H0Z" fill="url(#${p}d2)"/>
      <path d="M0 186C80 178 200 188 360 180V200H0Z" fill="#5A341C" opacity=".6"/>`,

    // Fiqh: a masjid courtyard, arcade and wudu fountain
    fiqh: p => { let arc = ""; for (let i = 0; i < 5; i++) { const x = 16 + i * 68; arc += `<path d="${archD(x, 110, 54, .8, 56)}" fill="url(#${p}in)"/><path d="${archD(x + 3, 112, 48, .8, 54)}" fill="none" stroke="#C9A46A" stroke-width="1.2" opacity=".6"/>`; }
      let tiles = ""; for (let x = 0; x < 360; x += 18) tiles += khatam(x + 9, 171, 5.2, "#E9C46A");
      return `<defs>${grad(p + "s", [[0, "#9FD3EA"], [1, "#EAF4F2"]])}${grad(p + "w", [[0, "#F4E6C8"], [1, "#E3C996"]])}${grad(p + "in", [[0, "#FDF8EC"], [1, "#EBD9B4"]])}
        ${grad(p + "fl", [[0, "#D8BF91"], [1, "#BE9F6B"]])}${grad(p + "wa", [[0, "#8ED1E2"], [1, "#2E8CA6"]])}</defs>
        <rect width="360" height="200" fill="url(#${p}s)"/>
        <path d="M0 64Q180 30 360 64V70H0Z" fill="#1F5F8B" opacity=".1"/>
        <rect x="0" y="52" width="360" height="114" fill="url(#${p}w)"/><rect x="0" y="52" width="360" height="7" fill="#C9A46A"/>
        ${arc}<g>${[0, 1, 2, 3, 4, 5].map(i => khatam(9 + i * 68, 84, 6.5, "#1F5F8B")).join("")}</g>
        <rect x="0" y="164" width="360" height="14" fill="#1F5F8B"/>${tiles}
        <rect x="0" y="178" width="360" height="22" fill="url(#${p}fl)"/>
        <ellipse cx="180" cy="186" rx="74" ry="12" fill="#1F5F8B"/><ellipse cx="180" cy="184" rx="67" ry="8.5" fill="url(#${p}wa)"/>
        <path d="M176 184V160h8V184Z" fill="#1F5F8B"/><path d="M158 156h44a22 7 0 0 1 -44 0Z" fill="#1F5F8B"/><ellipse cx="180" cy="156" rx="22" ry="3" fill="#8ED1E2"/>
        <path d="M178 156V146h4V156Z" fill="#1F5F8B"/><circle cx="180" cy="144" r="3.2" fill="#E9C46A"/>
        <path d="M180 142c-6-6-14-4-19 9M180 142c6-6 14-4 19 9" fill="none" stroke="#DDF5FA" stroke-width="1.8" stroke-linecap="round"/>
        <path d="M160 158c-3 6-5 14-6 24M200 158c3 6 5 14 6 24" fill="none" stroke="#CFF0F7" stroke-width="1.6" stroke-linecap="round" opacity=".85"/>
        <path d="M152 184h56" stroke="#E4F7FB" stroke-width="1.5" opacity=".6"/>`; },

    // Reading the Qur'an: an open mushaf resting on a wooden stand (rahl), lamplight
    tilawah: p => { let lines = ""; for (let i = 0; i < 7; i++) { lines += `<path d="M${118 + i * .6} ${f(92 + i * 9)}Q${150} ${f(86 + i * 9)} 176 ${f(96 + i * 9)}" stroke="#7A5A33" stroke-width="1.6" stroke-linecap="round" fill="none" opacity=".55"/>`;
        lines += `<path d="M${184} ${f(96 + i * 9)}Q210 ${f(86 + i * 9)} ${242 - i * .6} ${f(92 + i * 9)}" stroke="#7A5A33" stroke-width="1.6" stroke-linecap="round" fill="none" opacity=".55"/>`; }
      return `<defs>${grad(p + "b", [[0, "#1E4B4B"], [1, "#0D2B2C"]])}${rgrad(p + "l", .5, .35, .55, [[0, "#FFE3A3", .55], [1, "#FFE3A3", 0]])}${grad(p + "pg", [[0, "#FFFAEE"], [1, "#F1E2C3"]], 1, 0)}
        ${grad(p + "pg2", [[0, "#F1E2C3"], [1, "#FFFAEE"]], 1, 0)}${grad(p + "wd", [[0, "#9A5E2E"], [1, "#5E3518"]])}</defs>
        <rect width="360" height="200" fill="url(#${p}b)"/><rect width="360" height="200" fill="url(#${p}l)"/>
        <g opacity=".14">${[0, 1, 2, 3, 4, 5].map(i => khatam(30 + i * 60, 30, 14, "#E9C46A")).join("")}</g>
        <path d="M150 160L118 194M210 160L242 194" stroke="url(#${p}wd)" stroke-width="10" stroke-linecap="round"/><path d="M134 178H226" stroke="url(#${p}wd)" stroke-width="5" stroke-linecap="round"/>
        <circle cx="180" cy="178" r="4" fill="#E9C46A"/>
        <path d="M108 84Q144 74 180 90V170Q144 156 108 164Z" fill="url(#${p}pg)"/><path d="M252 84Q216 74 180 90V170Q216 156 252 164Z" fill="url(#${p}pg2)"/>
        <path d="M104 86Q144 76 180 92V172Q144 158 104 166Z" fill="#1F5F5A" opacity=".9" transform="translate(-2 3)"/><path d="M256 86Q216 76 180 92V172Q216 158 256 166Z" fill="#1F5F5A" opacity=".9" transform="translate(2 3)"/>
        <path d="M108 84Q144 74 180 90V170Q144 156 108 164Z" fill="url(#${p}pg)"/><path d="M252 84Q216 74 180 90V170Q216 156 252 164Z" fill="url(#${p}pg2)"/>
        <path d="M112 88Q144 79 176 93V164Q144 152 112 159Z" fill="none" stroke="#C9A46A" stroke-width="1.2"/><path d="M248 88Q216 79 184 93V164Q216 152 248 159Z" fill="none" stroke="#C9A46A" stroke-width="1.2"/>
        ${lines}<path d="M180 90V170" stroke="#C9A46A" stroke-width="1.4"/>`; },

    // Daily life: a window at dawn, prayer beads, a lantern and a plant on the sill
    adab: p => `<defs>${grad(p + "s", [[0, "#F7C9A2"], [.55, "#FBE3C4"], [1, "#FFF6E4"]])}${grad(p + "w", [[0, "#2F5D5C"], [1, "#214645"]])}${rgrad(p + "sun", .5, .78, .3, [[0, "#FFF4D6"], [1, "#FFF4D6", 0]])}
      ${grad(p + "sill", [[0, "#C79A63"], [1, "#9C7344"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}w)"/>
      <path d="${archD(110, 96, 140, .72, 74)}" fill="url(#${p}s)"/><path d="${archD(110, 96, 140, .72, 74)}" fill="url(#${p}sun)"/>
      <circle cx="180" cy="148" r="20" fill="#FFD891"/>
      <path d="M110 170C150 158 210 160 250 168V170H110Z" fill="#E7A97A" opacity=".7"/><path d="M110 170C140 164 170 166 196 162S236 164 250 166V170H110Z" fill="#D88C63" opacity=".55"/>
      <path d="${archD(110, 96, 140, .72, 74)}" fill="none" stroke="#E9C46A" stroke-width="3"/><path d="M180 ${f(96 - archH(140, .72))}V170M110 120H250" stroke="#214645" stroke-width="3"/>
      <rect x="92" y="168" width="176" height="10" rx="2" fill="url(#${p}sill)"/><rect x="0" y="178" width="360" height="22" fill="#1A3938"/>
      <g transform="translate(128 140)"><path d="M-9 28h18l-3-14h-12z" fill="#B5673E"/><path d="M0 14C-6 6-10 2-12-8C-4-4-1 4 0 14Z" fill="#5E9C6A"/><path d="M0 14C6 4 10 0 13-6C6-3 2 4 0 14Z" fill="#4C8758"/><path d="M0 14C0 4 1-4 3-12C5-4 3 6 0 14Z" fill="#6FAE7A"/></g>
      <g fill="#7A3E2B">${[...Array(15)].map((_, i) => { const a = Math.PI * (i / 14), x = 224 + Math.cos(a) * 16, y = 156 + Math.sin(a) * 9; return `<circle cx="${f(x)}" cy="${f(y)}" r="2.3"/>`; }).join("")}<path d="M224 165v6" stroke="#7A3E2B" stroke-width="1.6"/><circle cx="224" cy="173" r="2" fill="#E9C46A"/></g>
      <g transform="translate(300 36)"><path d="M0 0V18" stroke="#E9C46A" stroke-width="1.4"/><path d="M-11 30Q0 14 11 30Z" fill="#E9C46A"/><rect x="-10" y="30" width="20" height="30" rx="3" fill="#E9C46A" opacity=".25"/><rect x="-10" y="30" width="20" height="30" rx="3" fill="none" stroke="#E9C46A" stroke-width="2"/>
        <circle cx="0" cy="45" r="5" fill="#FFE3A3"/><path d="M-12 60h24l-4 6h-16z" fill="#E9C46A"/></g>`,

    // Seerah: Madinah at dusk, the Green Dome among date palms
    seerah: p => `<defs>${grad(p + "s", [[0, "#2D4E6E"], [.5, "#C98767"], [.82, "#F2C38B"], [1, "#F7DCB2"]])}${grad(p + "g", [[0, "#3E8E5C"], [1, "#1F6B45"]])}${grad(p + "gr", [[0, "#7A5A3A"], [1, "#4D3522"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}s)"/>${stars(19, 14, 50, "#FFF3DA")}
      <circle cx="96" cy="128" r="22" fill="#FFE1A8" opacity=".85"/>
      <path d="M0 150C60 138 110 146 180 140S300 136 360 142V200H0Z" fill="#B97B57" opacity=".55"/>
      <g fill="#E9DFC9"><rect x="140" y="118" width="96" height="38"/><rect x="232" y="72" width="9" height="84"/><rect x="229" y="96" width="15" height="4"/><path d="M231.5 72L236.5 58L241.5 72Z"/></g>
      <rect x="168" y="104" width="40" height="14" fill="url(#${p}g)"/>${dome(188, 106, 34, 32, `url(#${p}g)`, "#F2D27A")}
      <g fill="#E9DFC9" opacity=".95">${[0, 1, 2, 3, 4].map(i => `<path d="${archD(146 + i * 18, 138, 12, .78, 18)}" fill="#B98A5E"/>`).join("")}</g>
      <g fill="#24402F">${palm(64, 172, 62, "#24402F", -6)}${palm(96, 176, 50, "#24402F", 5)}${palm(286, 172, 66, "#24402F", 7)}${palm(318, 178, 46, "#24402F", -4)}</g>
      <path d="M0 170C80 162 200 176 360 166V200H0Z" fill="url(#${p}gr)"/>`,

    // Companions and Ahl al-Bayt: Mount Uhud at dawn, a path through palm groves
    sahabah: p => `<defs>${grad(p + "s", [[0, "#F6D7A7"], [.6, "#F9E7C6"], [1, "#FCF2DD"]])}${grad(p + "m1", [[0, "#B5684A"], [1, "#8A4A33"]])}${grad(p + "m2", [[0, "#8E4F38"], [1, "#5E3122"]])}${grad(p + "f", [[0, "#C6A26F"], [1, "#A07E4E"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}s)"/><circle cx="250" cy="70" r="26" fill="#FFF1CF"/><circle cx="250" cy="70" r="40" fill="#FFF1CF" opacity=".35"/>
      <path d="M0 120L40 96L70 104L108 70L140 88L170 62L206 84L232 74L272 98L310 82L360 104V200H0Z" fill="url(#${p}m1)"/>
      <path d="M0 138L46 118L90 128L130 106L176 124L214 112L262 130L310 116L360 132V200H0Z" fill="url(#${p}m2)"/>
      <path d="M0 160C90 150 260 156 360 150V200H0Z" fill="url(#${p}f)"/>
      <path d="M140 200C168 184 196 168 214 158L219 158C204 170 186 186 176 200Z" fill="#E9D3A6"/>
      <g>${palm(40, 176, 56, "#3B5637", -4)}${palm(78, 180, 44, "#2F4A2E", 4)}${palm(276, 174, 58, "#3B5637", 6)}${palm(314, 182, 42, "#2F4A2E", -3)}${palm(116, 182, 36, "#46643F", 2)}</g>`,

    // Qur'an: Jabal al-Nur at night, light above the cave of Hira
    quran: p => `<defs>${grad(p + "s", [[0, "#0A1C2E"], [.7, "#22405A"], [1, "#3E5B6F"]])}${rgrad(p + "r", .5, .2, .55, [[0, "#FFF0C2", .6], [1, "#FFF0C2", 0]])}${grad(p + "m", [[0, "#3A3B3D"], [1, "#1C1D20"]])}${grad(p + "m2", [[0, "#2A2B2E"], [1, "#121315"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}s)"/>${stars(41, 60, 130)}<rect width="360" height="200" fill="url(#${p}r)"/>
      <path d="M180 0L120 200H240Z" fill="#FFF0C2" opacity=".07"/><path d="M180 0L150 200H210Z" fill="#FFF0C2" opacity=".08"/>
      <path d="M0 200L60 150L96 160L150 92L180 58L206 86L238 104L272 140L312 128L360 160V200Z" fill="url(#${p}m)"/>
      <path d="M180 58L150 92L120 150L128 152L156 98Z" fill="#5A5B5F" opacity=".5"/><path d="M180 58L206 86L238 104L230 106L202 90Z" fill="#5A5B5F" opacity=".35"/><ellipse cx="190" cy="90" rx="6" ry="4.5" fill="#FFE3A3"/><ellipse cx="190" cy="90" rx="14" ry="10" fill="#FFE3A3" opacity=".25"/>
      <path d="M0 200L40 176L84 184L130 160L170 178L220 166L270 186L320 172L360 186V200Z" fill="url(#${p}m2)"/>`,

    // Tazkiyah: a garden pool under the moon, cypresses mirrored in still water
    tazkiyah: p => { const cyp = (x, h) => `<path d="M${x} ${150 - h}C${x - 7} ${150 - h * .7} ${x - 9} ${150 - h * .25} ${x - 6} 150H${x + 6}C${x + 9} ${150 - h * .25} ${x + 7} ${150 - h * .7} ${x} ${150 - h}Z" fill="#1E4436"/>`;
      const trees = [44, 82, 278, 316].map((x, i) => cyp(x, [64, 52, 56, 66][i])).join("");
      return `<defs>${grad(p + "s", [[0, "#173B4A"], [.65, "#3F6E73"], [1, "#9DBEB2"]])}${grad(p + "wa", [[0, "#7FA8A6"], [1, "#2D5A5E"]])}${grad(p + "st", [[0, "#D9C7A2"], [1, "#B49E74"]])}</defs>
        <rect width="360" height="200" fill="url(#${p}s)"/>${stars(5, 30, 80)}<circle cx="180" cy="56" r="18" fill="#FFF3D1"/><circle cx="180" cy="56" r="34" fill="#FFF3D1" opacity=".18"/>
        <path d="M0 132C70 120 120 126 180 122S300 118 360 126V152H0Z" fill="#2B5A4C"/>${trees}
        <rect x="0" y="150" width="360" height="50" fill="url(#${p}st)"/>
        <path d="M60 156H300L320 196H40Z" fill="url(#${p}wa)"/><path d="M60 156H300L320 196H40Z" fill="none" stroke="#E9DDBF" stroke-width="3"/>
        <ellipse cx="180" cy="176" rx="12" ry="5" fill="#FFF3D1" opacity=".55"/><path d="M150 168h22M190 168h16M160 186h40" stroke="#E6F1EC" stroke-width="1.2" opacity=".45" stroke-linecap="round"/>
        <path d="M174 160h12M168 166h24" stroke="#FFF3D1" stroke-width="1.4" opacity=".5" stroke-linecap="round"/>`; },

    // Halal & Haram: a balanced scale with dates and wheat, under an arch
    halal: p => `<defs>${grad(p + "b", [[0, "#F6E9D0"], [1, "#EAD5AF"]])}${grad(p + "a", [[0, "#8A5A1F"], [1, "#6A4416"]])}${grad(p + "br", [[0, "#E9C46A"], [1, "#B68A2E"]])}${grad(p + "t", [[0, "#9A6B3A"], [1, "#6E4A26"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}b)"/><path d="${archD(100, 80, 160, .72, 120)}" fill="url(#${p}a)" opacity=".12"/>
      <g opacity=".22">${[0, 1, 2, 3, 4, 5].map(i => khatam(30 + i * 60, 26, 9, "#8A5A1F")).join("")}</g>
      <rect x="40" y="168" width="280" height="12" rx="3" fill="url(#${p}t)"/><rect x="0" y="180" width="360" height="20" fill="#8A6A44"/>
      <rect x="176" y="62" width="8" height="96" rx="2" fill="url(#${p}br)"/><path d="M160 168h40l-6-12h-28z" fill="url(#${p}br)"/><circle cx="180" cy="60" r="6" fill="url(#${p}br)"/>
      <rect x="104" y="64" width="152" height="5" rx="2.5" fill="url(#${p}br)"/>
      <path d="M112 68L96 116M112 68L128 116M248 68L232 116M248 68L264 116" stroke="#B68A2E" stroke-width="1.4"/>
      <path d="M88 116h48a24 10 0 0 1 -48 0z" fill="url(#${p}br)"/><path d="M224 116h48a24 10 0 0 1 -48 0z" fill="url(#${p}br)"/>
      <g fill="#6B2E1C">${[[100, 111], [110, 109], [120, 111], [105, 104], [116, 104]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="5.6" ry="3.6"/>`).join("")}</g>
      ${[-16, -8, 0, 8, 16].map(a => { const r = a * Math.PI / 180, L = 30, ex = 248 + Math.sin(r) * L, ey = 114 - Math.cos(r) * L;
        let g = `<path d="M248 114L${f(ex)} ${f(ey)}" stroke="#C8973F" stroke-width="1.5" stroke-linecap="round"/>`;
        for (let k = 0; k < 4; k++) { const t = .62 + k * .1, gx = 248 + Math.sin(r) * L * t, gy = 114 - Math.cos(r) * L * t;
          g += `<ellipse cx="${f(gx - 2.2)}" cy="${f(gy)}" rx="1.7" ry="3" fill="#D7A949" transform="rotate(${a - 22} ${f(gx - 2.2)} ${f(gy)})"/><ellipse cx="${f(gx + 2.2)}" cy="${f(gy)}" rx="1.7" ry="3" fill="#D7A949" transform="rotate(${a + 22} ${f(gx + 2.2)} ${f(gy)})"/>`; }
        return g + `<ellipse cx="${f(ex)}" cy="${f(ey - 1)}" rx="1.6" ry="3" fill="#D7A949" transform="rotate(${a} ${f(ex)} ${f(ey - 1)})"/>`; }).join("")}`,

    // Marriage, family and rights: a family home at evening, lamps lit in the windows
    family: p => `<defs>${grad(p + "s", [[0, "#2E4A6B"], [.55, "#B9786A"], [1, "#F0C08E"]])}${grad(p + "wl", [[0, "#F1E2C4"], [1, "#D9C197"]])}${grad(p + "win", [[0, "#FFE7A8"], [1, "#F6C15E"]])}${grad(p + "dr", [[0, "#6E4426"], [1, "#4C2D18"]])}${grad(p + "gd", [[0, "#7E9A62"], [1, "#55703F"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}s)"/>${stars(57, 18, 60, "#FFF3DA")}<path d="M300 26a15 15 0 1 0 11 25a12 12 0 1 1 -11 -25z" fill="#FFE7AE"/>
      <rect x="70" y="70" width="220" height="104" fill="url(#${p}wl)"/><rect x="62" y="64" width="236" height="8" rx="2" fill="#B08A4E"/>
      <path d="${archD(160, 116, 40, .78, 58)}" fill="url(#${p}dr)"/><circle cx="174" cy="148" r="2.2" fill="#E9C46A"/><circle cx="186" cy="148" r="2.2" fill="#E9C46A"/>
      ${[92, 236].map(x => `<path d="${archD(x, 104, 32, .78, 30)}" fill="url(#${p}win)"/><path d="${archD(x, 104, 32, .78, 30)}" fill="none" stroke="#2F5D5C" stroke-width="3"/><path d="M${x + 16} ${f(104 - archH(32, .78))}V134M${x} 116H${x + 32}" stroke="#2F5D5C" stroke-width="2"/>`).join("")}
      ${[92, 236].map(x => `<circle cx="${x + 16}" cy="120" r="30" fill="#FFE7A8" opacity=".14"/>`).join("")}
      <path d="M0 174C80 166 280 166 360 172V200H0Z" fill="url(#${p}gd)"/><path d="M162 174H198L210 200H150Z" fill="#E2CFA6"/>
      ${palm(34, 182, 64, "#2F4A2E", -4)}${palm(326, 184, 58, "#2F4A2E", 5)}
      <g transform="translate(136 96)"><path d="M0 0V8" stroke="#C9A24A" stroke-width="1.2"/><path d="M-6 14Q0 6 6 14Z" fill="#E9C46A"/><rect x="-5.5" y="14" width="11" height="14" rx="2" fill="#FFE3A3" stroke="#E9C46A" stroke-width="1.4"/></g>
      <g transform="translate(224 96)"><path d="M0 0V8" stroke="#C9A24A" stroke-width="1.2"/><path d="M-6 14Q0 6 6 14Z" fill="#E9C46A"/><rect x="-5.5" y="14" width="11" height="14" rx="2" fill="#FFE3A3" stroke="#E9C46A" stroke-width="1.4"/></g>`,

    // Dealing with doubts: a lantern lighting the way through the dark
    doubts: p => `<defs>${grad(p + "s", [[0, "#151A33"], [1, "#2E2A55"]])}${rgrad(p + "l", .5, .46, .5, [[0, "#FFD98A", .55], [.5, "#FFD98A", .12], [1, "#FFD98A", 0]])}${grad(p + "g", [[0, "#F6C766"], [1, "#C98A2E"]])}${grad(p + "pt", [[0, "#3B3666", 0], [1, "#E9C46A", .35]])}</defs>
      <rect width="360" height="200" fill="url(#${p}s)"/>${stars(23, 40, 120)}<rect width="360" height="200" fill="url(#${p}l)"/>
      <path d="M180 120L120 200H240Z" fill="url(#${p}pt)"/>
      <path d="M0 200L0 150Q60 140 110 156T200 160T300 150T360 156V200Z" fill="#1A1838"/>
      <g transform="translate(180 30)"><path d="M0 0V16" stroke="#E9C46A" stroke-width="1.6"/><circle cx="0" cy="0" r="3" fill="none" stroke="#E9C46A" stroke-width="1.6"/>
        <path d="M-16 34Q0 12 16 34Z" fill="url(#${p}g)"/><rect x="-1" y="13" width="2" height="6" fill="#E9C46A"/>
        <path d="M-16 34H16L19 74H-19Z" fill="#FFE3A3" opacity=".22"/><path d="M-16 34H16L19 74H-19Z" fill="none" stroke="url(#${p}g)" stroke-width="2.4"/>
        <path d="M0 34V74M-8 34L-9.5 74M8 34L9.5 74" stroke="url(#${p}g)" stroke-width="1.2" opacity=".8"/>
        <ellipse cx="0" cy="56" rx="7" ry="10" fill="#FFF0C4"/><ellipse cx="0" cy="58" rx="3.5" ry="6" fill="#FFFFFF"/>
        <path d="M-22 74H22L16 84H-16Z" fill="url(#${p}g)"/><path d="M-8 84H8L4 90H-4Z" fill="url(#${p}g)"/></g>`,
  };
  return (id, label) => { const fn = S[id]; if (!fn) return ""; const p = "il" + (++n) + "_";
    return `<svg xmlns="http://www.w3.org/2000/svg" class="illus" viewBox="0 0 360 200" role="img" aria-label="${label || ""}" preserveAspectRatio="xMidYMid slice">${fn(p)}</svg>`; };
})();

const _illU = {};
const illUrl = id => _illU[id] || (_illU[id] = ILL(id) ? "data:image/svg+xml;charset=utf-8," + encodeURIComponent(ILL(id)) : "");
const illImg = (id, cls) => illUrl(id) ? `<img class="${cls}" src="${illUrl(id)}" alt="" aria-hidden="true" decoding="async">` : "";

// ---- a scene for every lesson: 26 motifs × times of day, matched to the topic
const LILL = (() => {
  const f = v => +(+v).toFixed(2);
  const rnd = seed => () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const G = (id, stops, x2 = 0, y2 = 1) => `<linearGradient id="${id}" x1="0" y1="0" x2="${x2}" y2="${y2}">${stops.map(([o, c, a]) => `<stop offset="${o}" stop-color="${c}"${a != null ? ` stop-opacity="${a}"` : ""}/>`).join("")}</linearGradient>`;
  const R = (id, cx, cy, r, stops) => `<radialGradient id="${id}" cx="${cx}" cy="${cy}" r="${r}">${stops.map(([o, c, a]) => `<stop offset="${o}" stop-color="${c}"${a != null ? ` stop-opacity="${a}"` : ""}/>`).join("")}</radialGradient>`;
  const archD = (x, y, w, k = .8, foot = 0) => { const r = w * k, h = Math.sqrt(r * r - (r - w / 2) ** 2);
    return `M${f(x)} ${f(y + foot)}V${f(y)}A${f(r)} ${f(r)} 0 0 1 ${f(x + w / 2)} ${f(y - h)}A${f(r)} ${f(r)} 0 0 1 ${f(x + w)} ${f(y)}V${f(y + foot)}Z`; };
  const khatam = (cx, cy, r, fill) => { let p = ""; for (let i = 0; i < 16; i++) { const a = Math.PI / 8 * i - Math.PI / 2, rr = i % 2 ? r * .62 : r; p += `${i ? "L" : "M"}${f(cx + Math.cos(a) * rr)} ${f(cy + Math.sin(a) * rr)}`; } return `<path d="${p}Z" fill="${fill}"/>`; };
  const domeD = (cx, base, w, h) => `M${f(cx - w / 2)} ${f(base)}C${f(cx - w / 2)} ${f(base - h * .55)} ${f(cx - w * .32)} ${f(base - h * .82)} ${f(cx)} ${f(base - h)}C${f(cx + w * .32)} ${f(base - h * .82)} ${f(cx + w / 2)} ${f(base - h * .55)} ${f(cx + w / 2)} ${f(base)}Z`;
  const halfDome = (cx, base, w) => `M${f(cx - w / 2)} ${f(base)}A${f(w / 2)} ${f(w / 2)} 0 0 1 ${f(cx + w / 2)} ${f(base)}Z`;
  const minaretS = (cx, base, w, h, fill) => `<rect x="${f(cx - w / 2)}" y="${f(base - h)}" width="${f(w)}" height="${f(h)}" fill="${fill}"/><rect x="${f(cx - w * .8)}" y="${f(base - h * .72)}" width="${f(w * 1.6)}" height="${f(w * .4)}" fill="${fill}"/><path d="M${f(cx - w * .6)} ${f(base - h)}L${f(cx)} ${f(base - h - w * 2.4)}L${f(cx + w * .6)} ${f(base - h)}Z" fill="${fill}"/>`;
  const palmS = (x, base, h, fill, lean = 0) => { const tx = x + lean, ty = base - h, L = h * .42;
    let s = `<path d="M${f(x - 2.2)} ${f(base)}Q${f(x + lean * .4 - 1.5)} ${f(base - h * .5)} ${f(tx - 1.1)} ${f(ty)}L${f(tx + 1.1)} ${f(ty)}Q${f(x + lean * .4 + 1.5)} ${f(base - h * .5)} ${f(x + 2.2)} ${f(base)}Z" fill="${fill}"/>`;
    [-160, -130, -100, -75, -50, -20, 10, 40].forEach(a0 => { const a = a0 * Math.PI / 180, ex = tx + Math.cos(a) * L, ey = ty + Math.sin(a) * L + L * .32, mx = tx + Math.cos(a) * L * .55, my = ty + Math.sin(a) * L * .55 - L * .12, nx = -Math.sin(a) * L * .09, ny = Math.cos(a) * L * .09;
      s += `<path d="M${f(tx)} ${f(ty)}Q${f(mx + nx)} ${f(my + ny)} ${f(ex)} ${f(ey)}Q${f(mx - nx)} ${f(my - ny)} ${f(tx)} ${f(ty)}Z" fill="${fill}"/>`; }); return s; };
  const cypress = (x, base, h, fill) => `<path d="M${x} ${base - h}C${x - 7} ${base - h * .7} ${x - 9} ${base - h * .25} ${x - 6} ${base}H${x + 6}C${x + 9} ${base - h * .25} ${x + 7} ${base - h * .7} ${x} ${base - h}Z" fill="${fill}"/>`;
  const lamp = (x, y, s = 1, glow = true) => `<g transform="translate(${x} ${y}) scale(${s})">${glow ? `<circle cx="0" cy="40" r="26" fill="#FFE3A3" opacity=".22"/>` : ""}<path d="M0 0V16" stroke="#C9A24A" stroke-width="1.4"/><path d="M-11 28Q0 13 11 28Z" fill="#E9C46A"/><path d="M-10 28H10L12 52H-12Z" fill="#FFE3A3" opacity=".35"/><path d="M-10 28H10L12 52H-12Z" fill="none" stroke="#E9C46A" stroke-width="2"/><ellipse cx="0" cy="41" rx="4" ry="6" fill="#FFF3CF"/><path d="M-14 52H14L10 58H-10Z" fill="#E9C46A"/></g>`;
  const PAL = {
    dawn:  { s: ["#F2A97E", "#F7D3AE", "#FCEAD2"], orb: "#FFE7B5", oy: 150, night: 0, tint: ["#E89A6A", .10], g: ["#D9A36D", "#A8723F"] },
    day:   { s: ["#7FC3E4", "#BFE2F1", "#EAF5F3"], orb: "#FFF6D2", oy: 44, night: 0, tint: null, g: ["#E0B67A", "#B8874D"] },
    dusk:  { s: ["#33496F", "#C77C5E", "#F1BD87"], orb: "#FFD79B", oy: 120, night: 0, tint: ["#A9532E", .14], g: ["#B97B4E", "#7C4D2C"] },
    night: { s: ["#06192B", "#123A4E", "#2D5866"], orb: "#FFEFC2", oy: 46, night: 1, tint: ["#061528", .34], g: ["#6B5A45", "#3D3224"] },
  };
  const sky = (p, P, ox = 292) => `<rect width="360" height="200" fill="url(#${p}sky)"/>` + (P.night ? (() => { const r = rnd(ox * 7 + 3); let s = ""; for (let i = 0; i < 44; i++) s += `<circle cx="${f(r() * 360)}" cy="${f(r() * 120)}" r="${f(.5 + r())}" fill="#FFF6DD" opacity="${f(.4 + r() * .6)}"/>`;
      return s + `<path d="M${ox} ${P.oy - 16}a19 19 0 1 0 14 31.6a15 15 0 1 1 -14 -31.6z" fill="${P.orb}"/>`; })()
    : `<circle cx="${ox}" cy="${P.oy}" r="34" fill="${P.orb}" opacity=".35"/><circle cx="${ox}" cy="${P.oy}" r="20" fill="${P.orb}"/>`);
  const defs = (p, P, extra = "") => `<defs>${G(p + "sky", [[0, P.s[0]], [.6, P.s[1]], [1, P.s[2]]])}${G(p + "gr", [[0, P.g[0]], [1, P.g[1]]])}${extra}</defs>`;
  const tint = P => P.tint ? `<rect width="360" height="200" fill="${P.tint[0]}" opacity="${P.tint[1]}"/>` : "";

  const M = {
    kaaba: (p, P) => defs(p, P, G(p + "fl", [[0, "#F3EFE7"], [1, "#D9D3C8"]])) + sky(p, P, 60) +
      `<g fill="#E7DCC6">${[0, 1, 2, 3, 4, 5, 6, 7].map(i => `<path d="${archD(8 + i * 44, 104, 30, .8, 30)}"/>`).join("")}<rect x="0" y="96" width="360" height="10"/></g>
      ${minaretS(30, 96, 7, 46, "#E7DCC6")}${minaretS(330, 96, 7, 46, "#E7DCC6")}<rect x="0" y="132" width="360" height="68" fill="url(#${p}fl)"/>
      <ellipse cx="180" cy="168" rx="150" ry="26" fill="none" stroke="#CFC7B7" stroke-width="1.2"/><ellipse cx="180" cy="168" rx="110" ry="18" fill="none" stroke="#CFC7B7" stroke-width="1.2"/>
      <path d="M150 86H206V160H150Z" fill="#151515"/><path d="M206 86L228 92V154L206 160Z" fill="#262626"/><path d="M150 96H206V104H150Z" fill="#C9A24A"/><path d="M206 96L228 101V109L206 104Z" fill="#A8862E"/>
      <rect x="170" y="122" width="14" height="30" fill="#C9A24A"/><path d="M150 86L172 80L228 86L206 86Z" fill="#2E2E2E"/><ellipse cx="190" cy="164" rx="52" ry="5" fill="#000" opacity=".12"/>` + tint(P),
    mihrab: (p, P) => `<defs>${G(p + "w", [[0, "#F1E4C8"], [1, "#DCC596"]])}${G(p + "n", [[0, "#2F5D5C"], [1, "#1D3E3D"]])}${G(p + "rug", [[0, "#8E2F2B"], [1, "#6A1F1C"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}w)"/><g opacity=".25">${[0, 1, 2, 3, 4, 5, 6].map(i => khatam(20 + i * 54, 24, 9, "#B08A4E")).join("")}</g>
      <path d="${archD(122, 92, 116, .78, 82)}" fill="#C9A46A"/><path d="${archD(132, 96, 96, .78, 78)}" fill="url(#${p}n)"/>
      <path d="${archD(140, 100, 80, .78, 0)}" fill="none" stroke="#E9C46A" stroke-width="1.2" opacity=".55"/>
      ${lamp(180, 52, .9)}<path d="M96 200L130 168H230L264 200Z" fill="url(#${p}rug)"/><path d="M106 198L134 172H226L254 198Z" fill="none" stroke="#E9C46A" stroke-width="1.6"/>
      <path d="M160 172Q180 158 200 172" fill="none" stroke="#E9C46A" stroke-width="1.6"/><rect x="0" y="164" width="360" height="4" fill="#B08A4E" opacity=".5"/>` + (P.night ? `<rect width="360" height="200" fill="#0A1A2A" opacity=".22"/>` : ""),
    iftar: (p, P) => defs(p, P, G(p + "tb", [[0, "#8A5A34"], [1, "#5E3A1F"]]) + G(p + "gl", [[0, "#E8F6FA", .9], [1, "#BFE3EE", .7]])) + sky(p, P, 270) +
      `<path d="M0 132L28 118L52 126L80 108L108 122L140 112L176 124L210 104L246 118L280 110L320 124L360 114V160H0Z" fill="#2D3C4E" opacity=".55"/>
      <g fill="#2D3C4E" opacity=".7">${minaretS(90, 140, 5, 34, "#2D3C4E")}<path d="${domeD(120, 140, 30, 24)}"/><rect x="100" y="138" width="40" height="10"/></g>
      <rect x="0" y="150" width="360" height="50" fill="url(#${p}tb)"/><rect x="0" y="146" width="360" height="6" fill="#A8774A"/>
      <ellipse cx="150" cy="160" rx="40" ry="9" fill="#E9DAB7"/><path d="M110 156Q150 186 190 156Z" fill="#E9DAB7"/><path d="M114 156H186" stroke="#C9A46A" stroke-width="1.5"/>
      ${[[128, 152], [140, 149], [152, 152], [164, 149], [176, 152], [134, 145], [158, 145]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="7" ry="4.4" fill="#5B2416"/><ellipse cx="${x - 2}" cy="${y - 1.5}" rx="2.5" ry="1.2" fill="#8A3E26"/>`).join("")}
      <path d="M222 120H250L246 166H226Z" fill="url(#${p}gl)"/><path d="M224 132H248L245 164H227Z" fill="#9FD4E4" opacity=".6"/><path d="M228 124V160" stroke="#fff" stroke-width="1.6" opacity=".7"/>` + tint(P),
    coins: (p, P) => `<defs>${G(p + "w", [[0, "#1F4E4A"], [1, "#143533"]])}${G(p + "c", [[0, "#F3D27A"], [1, "#C9962E"]])}${G(p + "t", [[0, "#7A5434"], [1, "#4F341E"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}w)"/><g opacity=".18">${[0, 1, 2, 3, 4, 5, 6].map(i => khatam(20 + i * 54, 40, 12, "#E9C46A")).join("")}</g>${lamp(300, 6, .8)}
      <rect x="0" y="150" width="360" height="50" fill="url(#${p}t)"/>
      ${[[110, 8], [150, 12], [190, 6], [232, 10]].map(([x, n]) => [...Array(n)].map((_, i) => `<ellipse cx="${x}" cy="${f(152 - i * 5)}" rx="16" ry="5" fill="url(#${p}c)"/><ellipse cx="${x}" cy="${f(150 - i * 5)}" rx="16" ry="5" fill="#F7DE95"/>`).join("") + `<ellipse cx="${x}" cy="${f(150 - (n - 1) * 5)}" rx="10" ry="2.8" fill="none" stroke="#C9962E"/>`).join("")}
      <path d="M44 156L84 146L96 170L56 180Z" fill="#E9DAB7"/><path d="M52 160L84 152M54 166L86 158M56 172L88 164" stroke="#B49A6A" stroke-width="1"/>`,
    tents: (p, P) => defs(p, P) + sky(p, P, 70) + `<path d="M0 110L40 84L80 96L130 70L170 90L220 76L270 96L320 80L360 98V140H0Z" fill="#8E6A4E" opacity=".75"/>
      <rect x="0" y="126" width="360" height="74" fill="url(#${p}gr)"/>
      ${[0, 1, 2].map(row => { const y = 132 + row * 22, w = 24 + row * 10, gap = w * 1.75; let s = ""; for (let x = -12 + row * w * .8; x < 370; x += gap) s += `<path d="M${f(x)} ${y + 14 + row * 3}L${f(x + w / 2)} ${y}L${f(x + w)} ${y + 14 + row * 3}Z" fill="#F7F3EA"/><path d="M${f(x + w / 2)} ${y}L${f(x + w)} ${y + 14 + row * 3}H${f(x + w * .62)}Z" fill="#DCD4C2"/>`; return s; }).join("")}` + tint(P),
    sea: (p, P) => defs(p, P, G(p + "sea", [[0, P.night ? "#16384A" : "#4D9BB5"], [1, P.night ? "#0B2231" : "#1F5F7A"]])) + sky(p, P, 180) +
      `<path d="M0 116L30 108L60 112L90 100L130 110L170 104L200 112V118H0Z" fill="#4E6670" opacity=".55"/><rect x="0" y="116" width="360" height="84" fill="url(#${p}sea)"/>
      <path d="M180 118L170 200H190Z" fill="${P.orb}" opacity=".35"/>${[0, 1, 2, 3, 4, 5].map(i => `<path d="M${20 + (i * 53) % 300} ${130 + i * 11}h${30 + i * 4}" stroke="#E8F4F6" stroke-width="1.3" opacity=".45" stroke-linecap="round"/>`).join("")}
      <path d="M260 200C268 176 290 166 320 164S360 170 360 176V200Z" fill="#2E2A26"/>` + tint(P),
    well: (p, P) => defs(p, P, G(p + "st", [[0, "#CDB894"], [1, "#9C8562"]], 1, 0)) + sky(p, P, 280) +
      `<path d="M0 140C80 126 160 136 240 130S330 126 360 132V200H0Z" fill="url(#${p}gr)"/>${palmS(40, 150, 56, "#2F4A2E", -4)}${palmS(300, 146, 62, "#2F4A2E", 6)}
      <path d="M150 128H210V168Q180 176 150 168Z" fill="url(#${p}st)"/><ellipse cx="180" cy="128" rx="30" ry="8" fill="#B49E78"/><ellipse cx="180" cy="128" rx="24" ry="5" fill="#2A2018"/>
      <rect x="154" y="82" width="5" height="48" fill="#6B4A2C"/><rect x="201" y="82" width="5" height="48" fill="#6B4A2C"/><rect x="150" y="80" width="60" height="5" rx="2" fill="#7E5834"/>
      <path d="M180 85V108" stroke="#8A6A44" stroke-width="1.3"/><path d="M173 108H187L185 118H175Z" fill="#7E5834"/>
      ${[0, 1, 2].map(i => `<path d="M150 ${140 + i * 10}Q180 ${146 + i * 10} 210 ${140 + i * 10}" stroke="#8D7756" stroke-width=".8" fill="none"/>`).join("")}` + tint(P),
    cave: (p, P) => defs(p, P, G(p + "rk", [[0, "#5A4A3E"], [1, "#2E241D"]])) + sky(p, P, 90) +
      `<path d="M0 200L0 150L60 120L110 84L160 66L210 80L260 70L320 110L360 128V200Z" fill="url(#${p}rk)"/>
      <path d="M160 66L130 96L120 140L136 142L150 100Z" fill="#7A6658" opacity=".45"/>
      <path d="M190 132Q206 106 228 118Q240 134 232 150H192Z" fill="#120E0B"/><path d="M196 122L230 146M200 140L226 118M213 112V150M194 131H232" stroke="#D9D2C6" stroke-width=".6" opacity=".55"/>
      <path d="M0 200L40 176L100 186L160 170L230 184L300 172L360 182V200Z" fill="#241C16"/>` + tint(P),
    inkpot: (p, P) => `<defs>${G(p + "d", [[0, "#7A5434"], [1, "#4E331C"]])}${G(p + "pp", [[0, "#FFF9EC"], [1, "#EEDFC0"]])}${R(p + "l", .7, .2, .6, [[0, "#FFE3A3", .4], [1, "#FFE3A3", 0]])}</defs>
      <rect width="360" height="200" fill="#1F3A3A"/><rect width="360" height="200" fill="url(#${p}l)"/><rect x="0" y="96" width="360" height="104" fill="url(#${p}d)"/>
      <path d="M60 118L232 104L254 186L72 198Z" fill="url(#${p}pp)"/>${[0, 1, 2, 3, 4, 5].map(i => `<path d="M${84 + i * 1.8} ${f(130 + i * 11)}L${f(226 + i * 3.6)} ${f(118 + i * 11)}" stroke="#B49A6A" stroke-width="1.1" opacity=".7"/>`).join("")}
      <path d="M96 140Q130 128 160 138" fill="none" stroke="#2A2A2A" stroke-width="2" stroke-linecap="round"/><path d="M168 134Q186 124 204 132" fill="none" stroke="#2A2A2A" stroke-width="2" stroke-linecap="round"/>
      <ellipse cx="292" cy="150" rx="26" ry="8" fill="#141414"/><path d="M266 150V126Q292 116 318 126V150Z" fill="#202020"/><ellipse cx="292" cy="126" rx="26" ry="8" fill="#303030"/><ellipse cx="292" cy="126" rx="12" ry="4" fill="#0A0A0A"/>
      <path d="M292 126L222 54" stroke="#C99B5E" stroke-width="5" stroke-linecap="round"/><path d="M226 58L216 46" stroke="#8A6A44" stroke-width="5" stroke-linecap="round"/>`,
    skyline: (p, P) => { const fill = P.night ? "#17293A" : "#3A4F63";
      return defs(p, P, G(p + "wt", [[0, P.s[2]], [1, P.s[0]]])) + sky(p, P, 300) +
      `<g fill="${fill}">${minaretS(70, 128, 6, 62, fill)}${minaretS(112, 128, 6, 70, fill)}${minaretS(248, 128, 6, 70, fill)}${minaretS(290, 128, 6, 62, fill)}
      <rect x="120" y="100" width="120" height="30"/><path d="${domeD(180, 102, 76, 52)}"/><path d="${halfDome(140, 104, 40)}"/><path d="${halfDome(220, 104, 40)}"/>
      <path d="${domeD(96, 116, 30, 22)}"/><path d="${domeD(264, 116, 30, 22)}"/><rect x="70" y="114" width="220" height="16"/><rect x="179" y="34" width="2" height="16"/></g>
      <rect x="0" y="128" width="360" height="72" fill="url(#${p}wt)" opacity=".85"/><g opacity=".25" transform="translate(0 256) scale(1 -1)"><rect x="120" y="100" width="120" height="28" fill="${fill}"/><path d="${domeD(180, 102, 76, 30)}" fill="${fill}"/></g>
      ${[0, 1, 2, 3].map(i => `<path d="M${40 + i * 80} ${146 + i * 12}h40" stroke="#fff" opacity=".35" stroke-width="1.2" stroke-linecap="round"/>`).join("")}` + tint(P); },
    books: (p, P) => `<defs>${G(p + "w", [[0, "#2B2622"], [1, "#1A1714"]])}${R(p + "l", .78, .55, .5, [[0, "#FFD98A", .5], [1, "#FFD98A", 0]])}</defs>
      <rect width="360" height="200" fill="url(#${p}w)"/><rect width="360" height="200" fill="url(#${p}l)"/>
      ${[52, 120].map(y => `<rect x="20" y="${y + 58}" width="240" height="6" fill="#6B4A2C"/>` + [...Array(13)].map((_, i) => { const h = 44 + (i * 7) % 14, w = 14 + (i * 5) % 6, x = 26 + i * 17.6, c = ["#6E2B24", "#1F4E4A", "#2E3E6A", "#7A5A1F", "#4A2E52"][i % 5];
        return `<rect x="${f(x)}" y="${y + 58 - h}" width="${w}" height="${h}" fill="${c}"/><rect x="${f(x)}" y="${y + 58 - h + 6}" width="${w}" height="2" fill="#E9C46A" opacity=".8"/><rect x="${f(x)}" y="${y + 58 - 10}" width="${w}" height="2" fill="#E9C46A" opacity=".8"/>`; }).join("")).join("")}
      <path d="M262 178H330V184H262Z" fill="#6B4A2C"/><path d="M276 178Q296 158 316 178Z" fill="#C9A24A"/><path d="M288 168Q296 150 304 168" fill="#E9C46A"/><ellipse cx="296" cy="150" rx="5" ry="10" fill="#FFE7A6"/><ellipse cx="296" cy="153" rx="2.2" ry="5" fill="#fff"/>`,
    cosmos: (p) => { const P = PAL.night, r = rnd(91); let st = ""; for (let i = 0; i < 120; i++) st += `<circle cx="${f(r() * 360)}" cy="${f(r() * 170)}" r="${f(.3 + r() * 1.1)}" fill="#FFF6DD" opacity="${f(.3 + r() * .7)}"/>`;
      return `<defs>${G(p + "s", [[0, "#050B1E"], [1, "#1B2350"]])}${G(p + "mw", [[0, "#9FB4FF", 0], [.5, "#C9B8FF", .22], [1, "#9FB4FF", 0]], 1, 1)}</defs><rect width="360" height="200" fill="url(#${p}s)"/>
        <path d="M-20 160L380 20L380 70L-20 210Z" fill="url(#${p}mw)"/>${st}<ellipse cx="180" cy="96" rx="120" ry="34" fill="none" stroke="#CFC6FF" opacity=".25"/><ellipse cx="180" cy="96" rx="80" ry="22" fill="none" stroke="#CFC6FF" opacity=".3"/>
        <circle cx="180" cy="96" r="12" fill="#FFE7AE"/><circle cx="180" cy="96" r="22" fill="#FFE7AE" opacity=".2"/><circle cx="292" cy="80" r="5" fill="#9AC4E8"/><circle cx="102" cy="112" r="4" fill="#E8B49A"/>
        <path d="M0 200L0 176Q90 164 180 172T360 168V200Z" fill="#0B1022"/>`; },
    rain: (p, P) => { const cloud = (x, y, s) => `<g transform="translate(${x} ${y}) scale(${s})" fill="${P.night ? "#41506A" : "#F3F5F7"}"><circle cx="0" cy="0" r="14"/><circle cx="16" cy="-6" r="18"/><circle cx="36" cy="0" r="14"/><rect x="0" y="0" width="36" height="14"/></g>`;
      const P2 = { ...P, s: P.night ? P.s : ["#9DB6C6", "#C9D8DF", "#E6EEF0"] };
      return defs(p, P2) + `<rect width="360" height="200" fill="url(#${p}sky)"/>${cloud(60, 40, 1.4)}${cloud(220, 30, 1.7)}${cloud(160, 60, 1)}
        ${[...Array(40)].map((_, i) => { const x = (i * 37) % 360, y = 70 + (i * 23) % 60; return `<path d="M${x} ${y}l-4 10" stroke="#8FB4C8" stroke-width="1.2" opacity=".7" stroke-linecap="round"/>`; }).join("")}
        <path d="M0 140C60 120 120 132 180 124S300 116 360 128V200H0Z" fill="#5E8F5A"/><path d="M0 162C80 150 180 160 260 152S340 150 360 154V200H0Z" fill="#4A7A49"/>
        <path d="M100 200C130 180 170 172 220 166S300 162 360 166V176C300 172 240 178 200 186S140 196 130 200Z" fill="#7FB8D0"/>` + (P.night ? tint(P) : ""); },
    graves: (p, P) => defs(p, P) + sky(p, P, 300) + `<path d="M0 132C70 122 140 128 210 122S320 118 360 124V200H0Z" fill="#5C7A55"/><path d="M0 160C90 150 200 160 360 150V200H0Z" fill="#4C6A46"/>
      ${cypress(46, 140, 70, "#26402C")}${cypress(70, 142, 54, "#2D4A33")}${cypress(312, 138, 66, "#26402C")}
      ${[[130, 158], [170, 162], [210, 156], [250, 160], [150, 178], [200, 180], [240, 176]].map(([x, y]) => `<path d="M${x - 5} ${y}V${y - 14}Q${x} ${y - 20} ${x + 5} ${y - 14}V${y}Z" fill="#E4DCCB"/><rect x="${x - 12}" y="${y}" width="24" height="3" rx="1.5" fill="#B7AC94" opacity=".7"/>`).join("")}` + tint(P),
    door: (p, P) => defs(p, P, G(p + "wl", [[0, "#EDE0C6"], [1, "#D6C29C"]]) + G(p + "dr", [[0, "#6E4426"], [1, "#4C2D18"]])) + sky(p, P, 320) +
      `<rect x="0" y="34" width="360" height="166" fill="url(#${p}wl)"/><rect x="0" y="30" width="360" height="6" fill="#B08A4E"/>
      <path d="${archD(130, 96, 100, .78, 104)}" fill="#2F5D5C"/><path d="${archD(138, 100, 84, .78, 100)}" fill="url(#${p}dr)"/><path d="M180 ${f(100 - Math.sqrt((84 * .78) ** 2 - (84 * .78 - 42) ** 2))}V200" stroke="#3A2212" stroke-width="2"/>
      ${[0, 1, 2, 3].map(r => [0, 1, 2, 3].map(c => `<circle cx="${146 + c * 22}" cy="${116 + r * 22}" r="1.8" fill="#C9A24A"/>`).join("")).join("")}<circle cx="172" cy="150" r="3" fill="#E9C46A"/><circle cx="188" cy="150" r="3" fill="#E9C46A"/>
      ${lamp(92, 40, .8)}${lamp(268, 40, .8)}<g transform="translate(70 168)"><path d="M-12 32h24l-4-18h-16z" fill="#B5673E"/><path d="M0 14C-10 4-14-4-16-18C-4-10 0 2 0 14Z" fill="#4C8758"/><path d="M0 14C10 2 14-6 18-16C6-10 2 2 0 14Z" fill="#5E9C6A"/></g>
      <g transform="translate(290 168)"><path d="M-12 32h24l-4-18h-16z" fill="#B5673E"/><path d="M0 14C-10 4-14-4-16-18C-4-10 0 2 0 14Z" fill="#5E9C6A"/><path d="M0 14C10 2 14-6 18-16C6-10 2 2 0 14Z" fill="#4C8758"/></g>` + (P.night ? `<rect width="360" height="200" fill="#061528" opacity=".28"/>` : ""),
    table: (p, P) => `<defs>${G(p + "w", [[0, "#F1E4C8"], [1, "#DCC596"]])}${G(p + "cl", [[0, "#F7F1E3"], [1, "#E2D6BC"]])}${G(p + "j", [[0, "#3F7C8C"], [1, "#245766"]])}</defs>
      <rect width="360" height="200" fill="url(#${p}w)"/><path d="${archD(40, 70, 90, .78, 70)}" fill="#E6D2A9"/><path d="${archD(230, 70, 90, .78, 70)}" fill="#E6D2A9"/>
      <path d="M30 140H330L350 200H10Z" fill="url(#${p}cl)"/><path d="M30 140H330" stroke="#C9A46A" stroke-width="2"/><path d="M42 150H318M24 186H336" stroke="#C9A46A" stroke-width="1" opacity=".6"/>
      <ellipse cx="110" cy="160" rx="34" ry="10" fill="#C98A4B"/><ellipse cx="110" cy="156" rx="30" ry="8" fill="#E0A865"/><path d="M90 154h40M94 158h32" stroke="#B07038" stroke-width="1" opacity=".6"/>
      <ellipse cx="182" cy="166" rx="28" ry="8" fill="#E9DAB7"/>${[[170, 160], [180, 158], [190, 160], [176, 154], [188, 154]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="6" ry="3.8" fill="#5B2416"/>`).join("")}
      <path d="M244 116Q244 100 254 96V88H266V96Q276 100 276 116V156Q260 164 244 156Z" fill="url(#${p}j)"/><path d="M276 112Q290 116 284 132" stroke="#245766" stroke-width="3" fill="none"/><ellipse cx="260" cy="88" rx="8" ry="2.5" fill="#1C4652"/>`,
  };
  // course scenes count as motifs too
  ["aqeedah", "fiqh", "tilawah", "adab", "seerah", "sahabah", "quran", "tazkiyah", "halal", "doubts", "family"].forEach(id => { M["c_" + id] = null; });
  const INDOOR = new Set(["mihrab", "coins", "inkpot", "books", "table"]);
  // lesson → motif (explicit for the key ones, then a rotation per course)
  const PICK = {
    purity1: "rain", purity2: "c_fiqh", purity3: "mihrab", purity4: "c_aqeedah", purity5: "sea", f_najasa: "rain", purity6: "well", fiqh_khuff: "c_sahabah", fiqh_hayd: "c_tazkiyah", f_madhur: "c_adab", f_istinja: "door", fiqh0: "books",
    f_times: "skyline", f_adhan: "skyline", prayer1: "kaaba", prayer2: "mihrab", prayer3: "c_aqeedah", f_how1: "mihrab", f_how2: "c_fiqh", f_rakahs: "skyline", f_texts: "c_tilawah", f_sunan: "c_adab", f_sahw: "c_doubts",
    prayer4: "c_fiqh", prayer5: "c_doubts", f_sunnahs: "c_aqeedah", f_jamaah: "skyline", f_travel: "well", f_qada: "c_doubts", f_jumuah: "skyline", f_janazah: "graves", f_death: "graves", f_eid: "skyline",
    f_sawm0: "iftar", fasting1: "iftar", fasting2: "iftar", fasting3: "iftar", zakat1: "coins", zakat2: "coins", zakat3: "c_halal", f_fitr: "table", f_udhiyah: "tents",
    hj1: "kaaba", hj2: "well", hj3: "tents", hj4: "kaaba", hj9: "kaaba", hj5: "kaaba", hj6: "c_sahabah", hj7: "tents", hj8: "kaaba",
    hh1: "c_halal", hh_kabair: "c_doubts", hh2: "c_tazkiyah", hh3: "table", hh4: "c_adab", hh5: "c_adab", hh6: "coins", f_money: "coins", hh7: "c_halal",
    belief1: "books", aq_islam: "kaaba", aq_proof: "sea", belief2: "sea", belief3: "c_aqeedah", belief4: "rain", aq_twenty: "c_quran", aq_speech: "c_tilawah", aq_jaiz: "sea", belief5: "c_quran", aq_nabi: "c_seerah",
    aq_kutub: "books", aq_shahada: "skyline", belief6: "c_aqeedah", aq_sins: "c_doubts", aq_riddah: "c_doubts", aq_shirk: "c_halal", aq_akhira: "graves", aq_ruya: "c_tazkiyah", aq_qadr: "inkpot", aq_signs: "cosmos", aq_awliya: "c_tazkiyah", aq_jamaa: "skyline",
    sr1: "c_aqeedah", sr1b: "well", sr2: "c_quran", sr3: "tents", sr_sorrow: "graves", sr_aqabah: "c_sahabah", sr4: "cave", sr_madinah: "c_seerah", sr5: "well", sr_hudaybiyah: "tents", sr6: "kaaba", sr_farewell: "c_sahabah", sr_passing: "c_seerah", sr_family: "door", sr7: "c_tazkiyah",
    qr0: "c_tilawah", qr1: "c_quran", qr2: "cosmos", qr3: "inkpot", qr4: "books", qr5: "mihrab",
    heart1: "c_tazkiyah", heart2: "rain", heart3: "c_adab", heart4: "c_doubts", heart5: "books", tz_dhikr: "c_doubts", tz_tawakkul: "c_sahabah", tz_sabr: "sea", tz_path: "c_seerah",
    sh_who: "c_sahabah", sh_abubakr: "cave", sh_umar: "skyline", sh_uthman: "inkpot", sh_ali: "door", sh_ten: "c_seerah", sh_mothers: "c_tazkiyah", sh_bayt: "door", sh_love: "c_sahabah",
    ad_wake: "c_adab", ad_adhkar: "c_doubts", ad_afterprayer: "mihrab", ad_salam: "door", ad_eat: "table", ad_dress: "door", ad_home: "door", ad_social: "skyline", ad_sleep: "c_adab", ad_limbs: "c_tazkiyah", ad_teach: "books",
    fm_before: "c_family", f_nikah: "skyline", fm_mahram: "c_tazkiyah", fm_wife: "door", fm_husband: "c_adab", fm_together: "c_family", fm_divorce: "rain", hh_parents: "table", fm_children: "c_seerah", fm_kin: "door",
    dd1: "c_doubts", dd2: "c_tazkiyah", dd3: "books", dd4: "c_quran", dd5: "sea", dd6: "cosmos",
    tl_letters1: "inkpot", tl_letters2: "books", tl_harakat: "c_tilawah", tl_makharij: "mihrab", tl_nun: "mihrab", tl_meem: "c_tilawah", tl_madd: "skyline", tl_more: "c_quran", tl_fatihah: "c_tilawah",
  };
  if (typeof self !== "undefined") { self.__LM = M; self.__LPAL = PAL; }
  const ORDER = ["dawn", "day", "dusk", "night"];
  const cache = {};
  const plan = {};
  // choose a time of day for each card so that, as far as the scenes allow, no picture repeats in a course
  const keyFor = (u, k) => {
    if (!plan[u.id]) { const used = new Set(); plan[u.id] = u.lessons.map((l, j) => { const m = PICK[l.id] || "c_" + u.id;
      const vk = pl => m + "|" + (INDOOR.has(m) ? (pl === "night" ? "n" : "d") : pl);
      const opts = m === "cosmos" ? ["night"] : m === "iftar" ? ["dusk", "night", "dawn"] : [0, 1, 2, 3].map(n => ORDER[(j + u.id.length + n) % 4]);
      const pal = opts.find(o => !used.has(vk(o))) || opts.find(o => j === 0 || vk(o) !== [...used].pop()) || opts[0];
      used.add(vk(pal)); return { m, pal, key: vk(pal) }; }); }
    return plan[u.id][k];
  };
  const TINT = { dawn: ["#F2A273", .12], day: null, dusk: ["#C0603A", .15], night: ["#06132A", .42] };
  return (u, k) => {
    const { m, pal, key } = keyFor(u, k);
    if (cache[key]) return cache[key];
    let svg;
    if (m.startsWith("c_")) { const t = TINT[pal]; svg = ILL(m.slice(2)).replace("</svg>", t ? `<rect width="360" height="200" fill="${t[0]}" opacity="${t[1]}"/></svg>` : "</svg>"); }
    else { const p = "ls" + key.replace(/\W/g, "") + "_"; svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" preserveAspectRatio="xMidYMid slice">${M[m](p, PAL[pal])}</svg>`; }
    return cache[key] = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
  };
})();
const lessonImg = (u, k, cls) => `<img class="${cls}" src="${LILL(u, k)}" alt="" aria-hidden="true" decoding="async" loading="lazy">`;
