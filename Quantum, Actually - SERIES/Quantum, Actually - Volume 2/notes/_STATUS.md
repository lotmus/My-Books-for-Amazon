# Quantum, Actually, Volume 2 (A QED Course): status

## 16 Oct 2026, current-master and version-history verification

Confirmed `Quantum, Actually - Volume 2.docx` as the latest master. Its content is byte-identical to the master already tracked on `origin/main`; no older manuscript content needed to be restored. All clearly superseded manuscript versions remain under this book's `bak/`, while unique source, reference, and production files remain preserved.

The immediately preceding master differs only in the updated *Gravity, Actually* title in the Also By material. The current master retains the public-reader fixes: one true Prologue, nine Opening Chapters, one Epilogue, 87 lessons, 52 lesson concept maps plus three table-replacement images, alt text for every image, no live Word tables, 880 glossary links, 17 external links, and linked bibliography references. No manuscript rewrite was made during this verification because the latest master already contains the required fixes.

Still open: a full continuous read-through.

## 10 Oct 2026, strict rescore from a careful sampled reread: 8.7 -> 9.0

Sampled: front matter, How to read this book, the Contents, Opening Chapters 1 and 6, Lesson 1 exercises and solutions, Lesson 77 (Lamb shift, numbers checked), the Interlude, Epilogue, Bibliography and back matter. Not a full read-through. (The SCORES row said 8.8, undated; 8.7 is my strict score before today's fixes.)
Prose 8.7, structure 9.1, facts 9.3 (Lamb shift 1057.845 MHz, 2p fine-structure 10,969 MHz, 2s lifetime 0.12 s, CODATA R-infinity, Compton massless limit, Lesson 1 solutions rechecked), formatting/KDP 9.2, covers 8.5.

Fixes (`scripts/rescore_2026-10-10.py`):
- Curly quotes throughout the prose (2,178 paragraphs; equations are OMML and untouched), matching Volume 1.
- The nine opening chapters were still called prologues in 50 places ("Prologues 1-6", "How to use this prologue", "Idea in this prologue", "the last of the four prologues" in what is the sixth Feynman-style chapter). Now "Opening Chapters", "this chapter", "the last of the six opening chapters". The real Prologue ("Why learn QED this way") keeps its name.
- Three double spaces.
- Link rule: the Bibliography already links every entry by keyword; seven entries now get a bookmark, and the first mention of each in the text links to it (Feynman's QED, Mead, Lamb and Retherford, Bethe, Uehling, Bloch-Nordsieck, CODATA). Grangier's first mention is already a DOI link.
- KDP description and both covers: "9 prologues" -> "9 opening chapters" (covers re-rendered by the unchanged script on Windows, which reproduces the old covers pixel for pixel; only that text changed). Old covers in bak.

Exercises: none cut, none changed.
Still open: a full read-through.
