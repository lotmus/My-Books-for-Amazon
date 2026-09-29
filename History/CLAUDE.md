# The Dolphins' View of History — working instructions

## Scope: stay in this folder

This folder is its own book: *The Dolphins' View of History*, canonically at
https://github.com/lotmus/My-Books-for-Amazon/tree/main/History

**Do not leave this folder.** Don't read, edit, or comment on any other book,
folder, or repo in this account (Science Books, Schrödinger's Paperwork, the
Auswandern guide, Lothar's Holistic Brain Farts, other PRs, etc.) while
working on this book, even if a fix elsewhere looks related or an error here
also appears to exist there. If something outside this folder seems worth
touching, say so and wait to be asked — don't go do it.

## Project facts

- **Two parallel content tracks exist and must be kept in sync by hand:**
  1. Numbered `.md` chapter files in `chapters/` (`00 - Prologue...md`
     through `41 - ...md`, plus `Epilogue...md` and `Further Reading...md`,
     moved there from the top level on 2026-09-27 to sit next to their
     `.docx` counterparts) and the concatenated
     `The Dolphins' View of History - Complete Manuscript.md`, which stays
     at the top level — the human-readable/diffable track. Only the
     top-level Book Plan and Complete Manuscript live outside `chapters/`
     now; everything per-chapter is inside it.
  2. `_generate.js` (top level) — a ~1,300-line, self-contained Node script
     (using the `docx` package) with the entire book's text hardcoded as JS
     calls (`heading()`, `body()`, `subhead()`, `grade()`, `verdict()`,
     etc.). Running `node _generate.js` is what actually builds
     `chapters/*.docx` (one file per chapter) and the shipped deliverable,
     `The Dolphins' View of History - Complete Manuscript.docx`. It does
     not read the `.md` files at all — the two tracks are independent copies.
  - **Editing only the `.md` files does not change the deliverable docx.**
    Any content fix (typo, fact correction, wording change) has to be
    ported into the matching spot in `_generate.js` too, then rebuilt — see
    commit "Port content-audit fixes from the parallel .md track into
    _generate.js" for precedent. Always check both tracks before treating a
    fix as done.
  - The back-matter appendix "A Timeline — For Humans Who Like Their
    History in Order" is the one exception: it exists only inside
    `_generate.js` (built via the `grade(date, description)` helper,
    grouped under `subhead()` era labels), with no `.md` counterpart to
    keep in sync. As of 2026-09-27 it runs from deep time through 2024,
    then two new eras, "The Near Future" and "The Far Future," extending it
    out to the heat death of the universe — sourced from Wikipedia's
    Timeline of the far future, 3rd millennium, and Anthropocene articles.
  - Chapter 41 ("Half the World, All the Time") and the Prologue's ancestor
    passages (Pakicetus/Ambulocetus/the hippo connection, the primate
    lineage) are confirmed in sync across both tracks and rebuilt as of
    2026-09-27; `chapters/*.docx` is current for every chapter including 41.
- **`00 - Book Plan - The Dolphins' View of History.md`** is the book
  bible: premise, part/chapter arc, running themes (war, greed, and racism
  named plainly wherever they're the real reason something happened; a
  recurring soft spot for pacifist low-tech sects like Quakers/Amish/
  Mennonites), voice rules (short paragraphs; a distant, dry,
  admiring-but-unfooled dolphin narrator; no hard-coded chapter-number
  cross-references, since renumbering has happened repeatedly), and a full
  dated changelog of every editorial pass (700-word floor, repetition
  sweeps, American-English spelling audits, Nav Pane/heading-style fixes).
  Read it before writing or restyling any chapter.
- **American English only** — a prior full-book audit already fixed stray
  British spellings (colour → color, catalogued → cataloged, etc.); don't
  reintroduce them.
- The two old freeform `.txt` files at root (`A Dolphin's History of
  Humanity .txt`, `The dolphins' view of history.txt`, dated mid-September,
  before the chapter split) are early drafts/notes, not live content — read
  for context only, don't restyle or merge them back in unasked.
- Build/deps: `node _generate.js` (only dependency is `docx`;
  `node_modules/` is already present).
