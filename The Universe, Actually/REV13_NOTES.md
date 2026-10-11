# The Universe, Actually - REV13 (2026-10-10)

Master: `The_Universe_Actually__REV13.docx` (REV11 moved to `bak\`; REV12 was an intermediate build left open in Word - safe to delete).

## What changed from REV11
- Structure: 8 Parts, 81 numbered chapters (Heading 2), 524 sections (Heading 3). Contents lists every Part and chapter with working links (0 dead links, unique bookmarks). The old 54-line TOC, the four dead links and the 633 flat page-per-section headings are gone.
- Duplicates: 26 sections that appeared twice word for word, six "consolidated" blocks (Arrow of Time, Black Holes, Quantum Foundations, Dark Sector, Earth Climate History, Human Evolution) that were verbatim re-pastes of earlier sections, and about 80 near-identical mini-sections were merged or removed. Exact repeated sentences: 2,368 (about 28,000 words) -> 0. Near-duplicates: 278 pairs -> 8 short rhetorical parallels.
- Text defects fixed: broken sentences left by an earlier name redaction ("the earlier guides"), two wrong Hawking-temperature examples, a GPS eccentricity figure, a population-genetics example, the 3-vs-4 papers of 1905, raw LaTeX in 382 paragraphs (now real superscripts/subscripts/Unicode), literal ** markers (now bold), duplicate Epilogue paragraphs, merged Reichenbach "Integration" restatements.
- New sections (own words, from the author's reading lists): Cosmic Calendar, Why the Night Sky Is Dark, Far Future of the Universe, A Table of Limits (Motion Mountain), Feynman's Ratchet, Energy Is Only a Number, The Atomic Hypothesis (Feynman Lectures), Core Theory, Many Levels of Description (Carroll), Analogy / MIU puzzle / Superrationality (Hofstadter), Thought Experiments About the Self (The Mind's I), What Neanderthals Were Like, What Made Our Species Different, Cave Art, After the Ice, Horses/Wheels/Languages, Vaccines and mRNA Medicine, Pandemics. Bibliography extended and sorted.
- Length: about 126,800 words, about 318 pages (US Letter, Georgia 11 pt) in LibreOffice rendering.

## Rebuilding
`scripts\make.py <out.docx>` rebuilds from `scripts\pool.json` + `structure.txt` (chapter map) + `ops\*.py` (the edit layer, applied in order) + `frontback.json`. `scripts\rep.py` scans the model for repeated and near-repeated sentences; run it after every edit round. Source text for the pool is REV11 (`bak\`).
