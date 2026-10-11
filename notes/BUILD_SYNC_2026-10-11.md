# Build sync, 11 Oct 2026

The 10 Oct 2026 back-matter edits (hyperlinked contents, Also-by list, About the Author, review invitation) were made in the docx masters only. This pass puts them into the build scripts. No master was changed; rebuilds went to `*_REBUILD_CHECK.docx` copies (not committed).

One place for the texts: `tools/canonical_text.py` reads `notes/ABOUT_THE_AUTHOR - canonical.md` (Version B) and `notes/ALSO_BY - canonical list.md`. Builders no longer hold copies. The review invitation is the same in all masters and sits in each script.

## Per book

| Book | Script | Result |
|---|---|---|
| Science Sparks | `scripts/build_almanac.py` | Full build ran. Review line, About, Also-by and their contents entries match the master. |
| Life, Actually | `scripts/build_book.py` | Cannot rebuild here: `chapters/` is not in git. Script adds review, About and Also-by in the master's order whatever the md holds; checked on a synthetic book only. |
| Quantum, Actually Vol 2 | `scripts/_finish_book.py` | Back matter and contents functions run on a copy of the master and match it. `main()` was not run on the master copy (see below). |
| The Dolphins' View of History | `scripts/_generate.js` | Full build ran in a scratch copy. All 1,533 paragraphs identical to the master, curly quotes included. |
| Look First Vol 2 | `Figures/build_docx.py`, `13_Also_By.md` | Built with grey placeholder figures (the figure PNGs are not in git). Contents (121 entries) and the 45 paragraphs from the review line to the end are identical to the master. `13_Also_By.md` now holds only its heading. |
| Math, Actually Vols 1-4 | none | No build script exists: the one-off builder is in bak and the masters are edited directly (`notes/CLAUDE.md` section 0). All four masters already match the canonical bio and list, and their contents link every section. Only `scripts/ma_text.py` changed (dead copy replaced by a canonical read). |

## Remaining differences and gaps

- Science Sparks: the rebuild lacks the Glossary, its contents entry and the figures, because `chapters/90_glossary.md` and `figures/` are not in git. The md chapters still say "Quanta, Actually ... (The Quantum World)" in three "Going deeper" lines where the master says "Quantum, Actually, Volume 1/2" (retired names; prose, so left alone). The master's Also-by links all point to the Physics Vol 1 search; the script gives each title its own search.
- Life, Actually: `notes/toc_pages.json` is not in git, so a rebuild shows page number 1 until Word updates the fields (the script sets update-on-open). The master has page numbers, so the rebuild keeps them.
- Quantum Vol 2: the finish script is behind the master. Run on the master it moved the front matter and put back "Prologues 1-6" wording from before the 10 Oct rescore. Do not run `main()` on the master. The contents entry "Prologue: Why learn QED this way" sits above the intro line in the master; the script lists it in reading order, after "How to read this book".
- Look First Vol 2: tables lay out differently from the master's. About the Author and Also by share a page in the master and in the rebuild.
- Quantum Vol 2 and Look First Vol 2: Also by and About the Author follow the master and share a page (no page break between).
