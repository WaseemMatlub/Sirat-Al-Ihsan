"""Respectful honorifics for English (and mixed) text.
ﷺ for the Prophet, عليه السلام for prophets and angels, رضي الله عنه/عنها/عنهما for
Companions, رحمه الله for the imams. Arabic-only strings are left untouched, and the
build skips the Qur'an-vocabulary and dictionary decks entirely."""
import re

SAL = "ﷺ"
_H = r"(?:ﷺ|\(ﷺ\)|صلى|عليه|عليها|عليهم|رضي|رحم|\(?peace|\(?may Allah|\(?blessings|\(pbuh|\(saw|\(s\.a)"
# no honorific right after the name, nor after a short bracketed gloss: "'Isa (Jesus), peace be upon him"
NOT_HAS = rf"(?!\s*[,.]?\s*{_H})(?!\s*\([^()]{{0,40}}\)\s*[,.]?\s*{_H})"
Q = r"[`'ʿ‘’]?"
W = r"[\w\-ʿ’'`]"
NISBA = rf"(?:\s(?:al|Al|an|An|as|As|az|Az|ad|Ad|ash|Ash)-{W}+)*"
NM = rf"(?:(?:al|Al|an|An|as|As|az|Az|ad|Ad)-)?{Q}[A-ZĀĪŪḤṢṬẒ]{W}*"
CHAIN = rf"(?:\s(?:bin|ibn|b\.|bint)\s(?:Ab[iī]\s|Ab[uū]\s)?{NM}{NISBA})*"

GROUP_AFTER = r"(?!(?:,?\s+(?:and|then)\s+(?:{Q}?[A-ZĀĪŪʿ][\w\-ʿ’'`]*\s?){1,3}){0,3}\s*رضي الله عنهم)".replace("{Q}", Q)
def _tag(text, name_re, honor, pre=""):
    # atomic group: match the WHOLE name (with lineage and nisba) or nothing, no backtracking
    pat = rf"(?<![\w`'ʿ]){pre}((?>{name_re}{NISBA}{CHAIN}(?:'s|’s)?))(?![\w])" + NOT_HAS + GROUP_AFTER
    return re.sub(pat, lambda m: f"{m.group(1)} {honor}", text)

COMPANIONS_M = [rf"Ab[uū] Bakr(?! and {Q}Umar)", r"Talha[h]?", r"(?:al-|Al-|Az-|az-)Zuba[iy]r(?! bin `Adi)", rf"{Q}Abd al-Rahman ibn {Q}Awf",
    rf"Abu {Q}Ubayda[h]?", rf"Sa{Q}d ibn Abi Waqqas", r"Abu Bakra", rf"{Q}Umar", rf"{Q}Uthman", rf"{Q}Ali", r"Abu Hura[iy]ra[h]?", r"Anas",
    r"Abu Musa", r"Hudhaifa", r"Hudhayfa[h]?", r"Jabir", rf"Abu Sa{Q}id", rf"Mu{Q}a[dz]h?", r"Abu Dharr", r"Usama",
    rf"Ibn Mas{Q}ud", r"Abu Ayyub", r"al-Mughira[h]?", rf"{Q}Ammar", r"Salama"]
COMPANIONS_F = [rf"{Q}A{Q}isha[h]?", rf"Asma{Q}", r"Umm Salama[h]?", r"Zainab", r"Khadija[h]?", r"Fatima[h]?"]
COMPANIONS_2 = [rf"Ibn {Q}Abbas", rf"Ibn {Q}Umar", rf"{Q}Abdullah (?:bin|ibn) {Q}Umar", rf"{Q}Abdullah (?:bin|ibn) {Q}Amr"]
PROPHETS = [r"Musa", r"Moses", rf"{Q}Isa", r"Jesus", r"Ibrahim", r"Abraham", r"Nuh", r"Noah", r"Sulaym[aā]n",
    r"Dawud", rf"Ya{Q}qub(?! ibn| bin)", r"Jibril", rf"Jibra{Q}il", r"Gabriel", rf"Isma{Q}il", r"Yunus", r"Khidr", r"Adam"]
IMAMS = [r"Ab[uū] [HḤ]an[iī]fa[h]?", r"ABu Hanifa", rf"Ab[uū] Y[uū]suf(?:\sYa{Q}qub)?", r"Imam Muhammad", r"Imaam Muhammed", r"Imaam Zufar",
    r"Imam (?:[Aa]l-)?Tahawi", r"al-Taft[aā]z[aā]n[iī]", r"Imam al-Nasafi", r"al-Ghazali", r"Imam al-Suyuti", r"Imam al-Nawawi"]
NOT_AFTER = r"(?<!Abu )(?<!Abū )(?<!bin )(?<!ibn )(?<!Ibn )(?<!Governor )(?<!Banu )(?<!Bani )(?<!\()(?<!Surah )"

def honor(text):
    if not text or not re.search(r"[A-Za-z]", text): return text
    t = text
    # 1. normalise what's already there
    t = re.sub(r"\s*\((?:peace be upon him|pbuh|PBUH|saw|SAW|s\.a\.w\.?|ﷺ)\)", f" {SAL}", t)
    t = t.replace("رحم الله تعالى", "رحمه الله تعالى")
    t = re.sub(r"\s*\((?:ra|RA|r\.a\.?|R\.A\.?)\)\s*(?=[:,.)]|$)", " رضي الله عنه", t)
    # 2. the Prophet ﷺ
    t = re.sub(r"\b((?>Prophet Mu[hḥ]ammad))(?![\w])" + NOT_HAS, rf"\1 {SAL}", t)
    for nm in [r"the Prophet", r"The Prophet", r"the Holy Prophet", r"Allah['’]s Messenger", r"[Tt]he Messenger of Allah",
               r"Messenger of Allah", r"the Messenger(?! of)", r"Rasulull?aa?h", r"Rasul Allah", r"the Nabi"]:
        t = re.sub(rf"\b((?>{nm}(?:['’]s)?))(?![\w])(?!\s+Mu[hḥ]ammad)" + NOT_HAS, rf"\1 {SAL}", t)
    t = re.sub(r"\b(that|And|testify that) Muhammad\b(?!['’]s)" + NOT_HAS, rf"\1 Muhammad {SAL}", t)
    t = re.sub(r"(^|\n)Muhammad,", rf"\1Muhammad {SAL},", t)
    # 3. Companions
    t = re.sub(rf"\b(Ab[uū] Bakr and {Q}Umar)\b" + NOT_HAS, r"\1 رضي الله عنهما", t)
    for nm in COMPANIONS_2:
        t = _tag(t, nm, "رضي الله عنهما")
        t = re.sub(rf"((?<![\w`'ʿ]){nm}{CHAIN}) رضي الله عنه(?![م])", r"\1 رضي الله عنهما", t)
    for nm in COMPANIONS_F: t = _tag(t, nm, "رضي الله عنها", pre=NOT_AFTER)
    for nm in COMPANIONS_M: t = _tag(t, nm, "رضي الله عنه", pre=NOT_AFTER)
    t = t.replace("Sa'd, Sa'id, 'Abd al-Rahman", "Sa'd رضي الله عنه, Sa'id رضي الله عنه, 'Abd al-Rahman")
    # 4. prophets and angels
    for nm in PROPHETS: t = _tag(t, nm, "عليه السلام", pre=NOT_AFTER)
    # 5. imams
    for nm in IMAMS: t = _tag(t, nm, "رحمه الله")
    t = re.sub(r"([Aa]ccording to) Muhammad\b" + NOT_HAS, r"\1 Imam Muhammad رحمه الله", t)
    return t

def honor_all(obj, skip_keys=()):
    if isinstance(obj, dict): return {k: (v if k in skip_keys else honor_all(v, skip_keys)) for k, v in obj.items()}
    if isinstance(obj, list): return [honor_all(v, skip_keys) for v in obj]
    if isinstance(obj, str): return honor(obj)
    return obj


# A deck may already carry a one-glyph honorific (ؓ ؒ ؑ ؐ) next to the words we insert: keep one.
import re as _re
_DUP = _re.compile(r"((?:رضي الله عن\S*|رحمه الله|رحمهما الله|عليه السلام|ﷺ))\s*[\u0610-\u0614]")
_honor_orig = honor
def honor(text):
    return _DUP.sub(r"\1", _honor_orig(text)) if isinstance(text, str) else text
