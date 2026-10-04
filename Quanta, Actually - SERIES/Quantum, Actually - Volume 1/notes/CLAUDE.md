# Quantum, Actually — Volume 1 — working instructions

## Scope: stay in this folder

This folder is its own book: *Quantum, Actually — Volume 1: Questions and Answers from the Double Slit to the Superconducting Wire*
(titled *The Quantum World* until 2026-10-03), canonically at
https://github.com/lotmus/My-Books-for-Amazon/tree/main/Quanta%2C%20Actually%20-%20SERIES/Quantum%2C%20Actually%20-%20Volume%201

**Do not leave this folder.** Don't read, edit, or comment on any other book,
folder, or repo in this account (the almanac *Lothar's Holistic Brain Farts*,
other Science Books, the History or Math Tower projects, other PRs, etc.)
while working on this book, even if a fix elsewhere looks related or an
error here also appears to exist there. If something outside this folder
seems worth touching, say so and wait to be asked — don't go do it.

## Project facts

- **The deliverable is `Quantum, Actually - Volume 1.docx`** (until 2026-10-03
  `The Quantum World.docx`; that file is kept in
  `D:\bak\2026-10-03 quanta merge\`) — the single master (no
  separate KINDLE/FINAL copies; the old `The_Quantum_World__FINAL.docx` and
  `__KINDLE.docx` were retired 2026-10-02 to
  `D:\bak\2026-10-02 Quantum World single master\`). It has been through
  many editorial passes (fact-check, style, accessibility, hyperlink fixes);
  treat it as mature, not a draft needing a rewrite.
- `bak/` holds editorial feedback (ChatGPT/Grok/Gemini/Copilot). Old drafts
  and KINDLE/FINAL backups now live in
  `D:\bak\2026-10-02 Quantum World single master\`. Read for context; don't restyle or
  clean it up unasked.
- `kdp_description_QA1.txt` (formerly `kdp_description_QW.txt`) is the live KDP listing copy — treat claims in it
  (illustration count, simulator links, companion-volume framing) as things
  the manuscript should stay consistent with.
- Before editing the `.docx` directly (it's a zip), verify round-trip
  integrity: `testzip()` clean, entry list unchanged, `word/document.xml`
  still parses, and check `word/_rels/document.xml.rels` against a working
  backup copy before assuming a relationship is broken — this book has at
  least one hyperlink (`rId12`, the Schrödinger's-cat image) whose correct
  form looks broken to a naive check but isn't.
- Title and series (Lothar, 2026-10-03): **Quantum, Actually — Volume 1:
  Questions and Answers from the Double Slit to the Superconducting Wire**. Volume 2 is
  *Quantum, Actually — Volume 2: A QED Course* (its own reviser owns that
  book's files). Quantum, Actually belongs to the Actually family with Physics,
  Life and Math, Actually; "Quanta, Actually" and "The Quantum World" are
  retired as names (Chapter 1 keeps its chapter title "The Quantum World:
  Nature Stops Behaving"). Title page follows the Physics, Actually layout:
  Title "Quantum, Actually", Heading 1 "Volume 1", the subtitle, the series
  line "A Volume in the Quantum, Actually Series", author "Lothar J. Musiol";
  the copyright page opens with "Quantum, Actually" and "Volume 1 — subtitle"
  and ends with "Quantum, Actually series". The book has no running heads
  (empty headers, page number in the footer); keep it that way. Refer to the
  QED Course as "*A QED Course* (Volume 2)". The series folder is still named
  `Quanta, Actually - SERIES` because it also holds the QED Course; renaming it
  is Lothar's call.
- **Merge (2026-10-03, Lothar's decision):** *The Quantum Conversation* was
  merged into this book as **Part Two, "One Road Through It"** (Chapters
  10–31, condensed from its 47 chapters). Part One, "The Map", is the original
  nine chapters. Appendix 4 (Collective Electrodynamics) and the Alice/Bob
  dialogue were removed; Chapter 7's QED material that Part Two repeats was
  cut back to pointers. Q&A devices: every chapter opens with "The question:",
  "Questions This Book Answers" follows the contents, QUESTION AND ANSWER boxes
  sit in Chapters 12, 15, 19, 20, 26, 30, each Part ends with a COMMON
  QUESTIONS box, and Appendix 2 is a narrator Q&A. Everything cut is kept in
  `..\Quantum, Actually - Volume 2\notes\Unused from merge for QED Course.docx`. The old
  masters and the whole Quantum Conversation folder are in
  `D:\bak\2026-10-03 quanta merge\`.
- Part Two working copies: `chapters\ch10.md`–`ch31.md` (md, the source used
  for Part Two), `chapters\back\*.md` (Part Two equations, symbols, notes on
  sources, its glossary entries), figures in `Figures\`. The merged docx was
  built by `scripts\build_merged.py` from the pre-merge master (last rebuilt
  2026-10-03 for the fact-check pass, the Part Two bibliography entries and the
  retitle); from now on **the docx is the master** again, so edit it directly
  and keep the md in step only if you rebuild.
