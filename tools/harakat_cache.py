"""Keep the harakat the CATT model added (see harakat.py) when the app's data files are rebuilt from these scripts:
strings the model voweled are swapped for their voweled form, and the honorifics always get their fixed spelling."""
import json, os, re
_C = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "harakat_cache.json"), encoding="utf-8"))
HONOR = {"رحمه الله": "رَحِمَهُ اللَّهُ", "رحمهما الله": "رَحِمَهُمَا اللَّهُ", "رحمهم الله": "رَحِمَهُمُ اللَّهُ",
  "رضي الله عنه": "رَضِيَ اللَّهُ عَنْهُ", "رضي الله عنها": "رَضِيَ اللَّهُ عَنْهَا", "رضي الله عنهما": "رَضِيَ اللَّهُ عَنْهُمَا", "رضي الله عنهم": "رَضِيَ اللَّهُ عَنْهُمْ",
  "عليه السلام": "عَلَيْهِ السَّلَامُ", "عليها السلام": "عَلَيْهَا السَّلَامُ", "عليهما السلام": "عَلَيْهِمَا السَّلَامُ", "عليهم السلام": "عَلَيْهِمُ السَّلَامُ",
  "صلى الله عليه وسلم": "صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ"}
def _pat(b): return re.compile("(?<![ء-ي])" + "".join(re.escape(ch) + "[ً-ْٰ]*" if ch != " " else " " for ch in b) + "(?![ء-يً-ْ])")
_H = [(_pat(k), v) for k, v in sorted(HONOR.items(), key=lambda x: -len(x[0]))]
def fix(s):
    s = _C.get(s, s)
    for r, v in _H: s = r.sub(v, s)
    return s
def apply(x):
    if isinstance(x, str): return fix(x)
    if isinstance(x, list): return [apply(v) for v in x]
    if isinstance(x, dict): return {k: apply(v) for k, v in x.items()}
    return x
