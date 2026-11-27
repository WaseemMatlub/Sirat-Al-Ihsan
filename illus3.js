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
