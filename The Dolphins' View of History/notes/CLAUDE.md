# The Dolphins' View of History — working instructions

## Scope: stay in this folder

This folder is its own book: *The Dolphins' View of History*, canonically at
https://github.com/lotmus/My-Books-for-Amazon/tree/main/The%20Dolphins'%20View%20of%20History
(the folder was called `History/` until 2026-10-01, when it was renamed with
`git mv`; it is the only book that folder ever held, so the wrapper name went).

**Do not leave this folder.** Don't read, edit, or comment on any other book,
folder, or repo in this account (Science Books, Schrödinger's Paperwork, the
Auswandern guide, Lothar's Holistic Brain Farts, other PRs, etc.) while
working on this book, even if a fix elsewhere looks related or an error here
also appears to exist there. If something outside this folder seems worth
touching, say so and wait to be asked — don't go do it.

## Project facts

- **Two parallel content tracks exist and must be kept in sync by hand:**
  1. Numbered `.md` chapter files in `chapters/` (`00 - Prologue...md`
     through `40 - ...md` — file 41 was folded into 40 on 2026-10-04, see
     below — plus `Epilogue...md` and `Further Reading...md`, moved there
     from the top level on 2026-09-27 to sit next to their `.docx`
     counterparts) and the concatenated
     `notes/The Dolphins' View of History - Complete Manuscript.md` — the
     human-readable/diffable track. Everything per-chapter is in
     `chapters/`.
  - **Rule: every other `.md` file goes in `notes/`** (Lothar's rule,
     2026-10-01): this file, the Book Plan, the Complete Manuscript `.md`
     and `KDP_Description.md` all live there. The top level holds only
     `_generate.js`, the package files, the Complete Manuscript `.docx`,
     `chapters/`, `notes/` and the ignored `bak/`.
  2. `scripts/_generate.js` (moved from the top level on 2 Oct 2026; it chdirs to the book root, so outputs land where they always did) — a ~1,300-line, self-contained Node script
     (using the `docx` package) with the entire book's text hardcoded as JS
     calls (`heading()`, `body()`, `subhead()`, `grade()`, `verdict()`,
     etc.). Running `node scripts/_generate.js` is what actually builds
     `chapters/*.docx` (one file per chapter) and the shipped deliverable,
     `The Dolphins' View of History - Complete Manuscript.docx`. It does
     not read the `.md` files at all — the two tracks are independent copies.
  - **Editing only the `.md` files does not change the deliverable docx.**
    Any content fix (typo, fact correction, wording change) has to be
    ported into the matching spot in `_generate.js` too, then rebuilt — see
    commit "Port content-audit fixes from the parallel .md track into
    _generate.js" for precedent. Always check both tracks before treating a
    fix as done.
  - Front and back matter (since 2026-10-01, in `_generate.js` and the
    Complete Manuscript `.md`): title page bylined **Lothar J. Musiol**, "As
    told by Professor Click-Click-Whoosh, Cetacean Academy of Oceanic
    Studies" (the professor is the narrator persona, never the author); a
    copyright page; then, after Further Reading, "Also by Lothar J. Musiol",
    whose groups and titles match the Brain Farts almanac `ALSO_BY` list
    (Look First Book 2 under its current title, *A Trip Is Not a New
    Life*). Keep it in step with his other books.
  - Appendix "What the Physics Is For — An Appendix on Uses and the One
    Theory Not Yet Found" (2026-10-01) holds the two essay sections that
    used to close the physics chapter ("What the physics is for", "One theory, not
    yet"); the physics chapter now ends on a one-line pointer and its verdict. It
    has an `.md` counterpart in `chapters/`. The `.md` physics chapter still
    carries two sections the build never had ("The rest of the ledger",
    "The outlook, without a trumpet"); Lothar decides whether they go into
    the build or are cut.
  - The back-matter appendix "A Timeline — For Humans Who Like Their
    History in Order" is the one exception: it exists only inside
    `_generate.js` (built via the `grade(date, description)` helper,
    grouped under `subhead()` era labels), with no `.md` counterpart to
    keep in sync. As of 2026-09-27 it runs from deep time through 2024,
    then two new eras, "The Near Future" and "The Far Future," extending it
    out to the heat death of the universe — sourced from Wikipedia's
    Timeline of the far future, 3rd millennium, and Anthropocene articles.
  - The "Half the World, All the Time" chapter (file 41) no longer exists as
    a standalone chapter (2026-10-04 mean-reviewer fix): it sat between the
    thesis-summarizing Long View chapter and the Epilogue, breaking the
    book's momentum right before its climax with a chapter whose own text
    admits it's a catch-up chapter ("this chapter is the dolphins going back
    for them"). Its four timelines (population, suffrage, the UDHR, the
    history of zero/algebra/calculus) are now folded into the Long View
    chapter's body and verdict, in both tracks and `_generate.js`; the
    Epilogue follows the Long View directly again. Do not re-add file 41 as
    a standalone chapter without re-solving this placement problem first.
    The Prologue's ancestor passages (Pakicetus/Ambulocetus/the hippo
    connection, the primate lineage) are unaffected and remain in sync
    across both tracks.
- **Flagged 2026-10-04, not yet fixed — the `.md` tracks have grown ahead
    of `_generate.js` in more than one place, not just the Soviet Union
    chapter:**
  - The Soviet Union chapter's `.md` track (`chapters/26 - ...md` and the
    Complete Manuscript) carries two entire `###` subsections not present
    in `_generate.js` at all — "The man who won the succession" (Stalin)
    and "The man who came back" (Yeltsin/Putin, including the 2014/2022
    Ukraine war) — several hundred words the generator's `chapter17` never
    received. `_generate.js`'s heading still reads "1917–1991," matching
    its own unexpanded content; the `.md` tracks' chapter now runs well
    past 1991.
  - Leaving the Cradle's `.md` track (`chapters/30 - ...md`) has a full
    SpaceX paragraph (reusable-booster landings in detail, the NASA
    contract dispute) that `_generate.js`'s `chapter23space` only
    summarizes in one sentence.
  - Both need a deliberate port (with each chapter's own word-count rule
    re-checked once ported, the way Genius and Catastrophe's overrun
    needs the same treatment — see the Book Plan) rather than a quick
    copy-paste; there may be others not yet found. Made two small fixes
    in the meantime, in all tracks that had them: the `.md`-only line "The
    titles changed. The offer did not: order, pride, and someone to
    blame," which exactly repeated the Genius and Catastrophe chapter's
    own diagnosis, now reads as an explicit callback; and one of two
    near-identical "which dolphin historians regard as a[n] ___" lines in
    Leaving the Cradle (44 lines apart) was reworded to break the repeated
    scaffolding.
- Back matter "Notes and Sources" (2026-10-03) sits between the physics
    appendix and Further Reading, in `_generate.js` (`const notes`, built with
    the `note(supports, citation)` helper), in `chapters/Notes and Sources.md`
    and in the Complete Manuscript `.md`. Every entry was verified (Crossref,
    Open Library, publisher or official page). Add a source only after
    verifying it; never invent one. A `minutes(label, text)` helper renders
    Society minutes (bold label, italic text). Four chapters deliberately end
    without a verdict (Africa's kingdoms, Ships, Soviet Union, Jewish history).
- **`notes/00 - Book Plan - The Dolphins' View of History.md`** is the book
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
- The two old freeform `.txt` files (`A Dolphin's History of
  Humanity .txt`, `The dolphins' view of history.txt`, dated mid-September,
  before the chapter split) are early drafts/notes, not live content. Since
  2026-10-01 they live in `bak/early drafts (Sep 2026)/` — read for context
  only, don't restyle or merge them back in unasked.
- Housekeeping 2026-10-01: the old Sep 20–23 chapter builds that sat at the
  top level (with two competing numberings) are in
  `bak/old root chapter builds (Sep 20-23)/`; `chapters/*.docx` is the only
  live per-chapter output. One-off porting scraps (`_port_missing.js`,
  `_africa_rich.md`, `_america_19.md`, `_america_later.md`) are in
  `bak/scratch 2026-10-01/`. `bak/` is gitignored.
- Build/deps: `node scripts/_generate.js` (only dependency is `docx`;
  `node_modules/` is already present).
