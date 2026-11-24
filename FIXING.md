# Fixing reported problems

Students report problems from inside the app (the flag button on a card, line or book section).
Each report arrives as an email whose subject starts with **"Ihsan:"** and whose body has one block per report:

```
Ihsan report [c|nur123]          <- key: c = flashcard id, l|book|index = lesson line, t|book|section = Library section
Problem: The answer is wrong
Note: <what the student wrote>

<the card or line as the student saw it>
```

## How to fix

1. **One card or line is wrong** → add a correction to `data/fixes.json`. No rebuild is needed.
   ```json
   { "cards": { "nur123": { "b": "corrected answer" }, "qd88": { "hide": true } },
     "lines": { "t12": { "en": "corrected translation" } } }
   ```
   - Fields replace the original (`f` question, `b` answer for cards; `ar`, `en`, `note` for lines).
   - `"hide": true` removes it from study and tests (use for broken or context-dependent cards).
   - Line ids are the `id` field of the line (e.g. `t12` in the Tahawiyyah, `jw3` in the Jawharah). The report key `l|book|index` gives the book and the line's index; look the id up in `data/year<N>.json` under `books.<book>[index].id`.
2. **The same kind of mistake keeps coming up** (for example a pattern of bad multiple-choice options) → fix the rule in `app3.js`, then rebuild: `python3 tools/build_app3.py` (run from the repo root; it rewrites `index.html` and `sw.js`).
3. **A Library book section is wrong** (`t|book|section`) → edit the section in `data/texts/<file>.json` (or `data/texts/<file>/<part>.json` for big books: part = floor(section / split)).

## What not to change without a teacher

Anything that changes a ruling, a creed statement, a translation of Qur'an or hadith, or an attribution.
Note these in the weekly summary for Waseem and his teacher instead of editing them. Spelling, harakat that are plainly wrong,
missing honorifics (ﷺ, رضي الله عنه/عنها/عنهما, عليه السلام, رحمه الله), broken formatting and nonsensical quiz questions can be fixed directly.

## Checks before pushing

- `node -e "const h=require('fs').readFileSync('index.html','utf8');new Function(h.match(/<script>([\s\S]*?)<\/script>/)[1])"` (syntax)
- `python3 -c "import json;json.load(open('data/fixes.json'))"` (valid JSON)
- Full test: `pip install playwright --break-system-packages && python3 -m playwright install chromium`, then serve the repo root (`python3 -m http.server 8765`) and run `python3 tools/test_app.py`. It must end with `ERRORS []`.

Commit as Waseem Matlub <WaseemMatlub@users.noreply.github.com>, pull with rebase first, push with `git -c push.negotiate=true push`.
