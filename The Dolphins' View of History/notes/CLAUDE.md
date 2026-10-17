# REV4 source-of-truth update — 15 October 2026

This section overrides older instructions below wherever they conflict. `The Dolphins' View of History - REV4.docx` is the current master and source of truth. REV3, REV4 batch drafts, and the former `chapters/*.docx` build outputs are superseded and belong in ignored `bak/`; do not use them to rebuild or replace REV4. The active Markdown working copies and `notes/The Dolphins' View of History - Complete Manuscript.md` were synced from REV4. They contain the Prologue, 40 chapters, and active appendices/back matter. The Timeline remains DOCX-only.

The generator `scripts/_generate.js` predates REV4 and is not synchronized with the current master. **Do not run it** until it has been deliberately ported to REV4 and audited; it would overwrite the current deliverable with older text and chapter files.

Standing rule: no sentence may repeat within this book. Run `scripts/check_repeats.js` against the current REV4 master after any text change. It checks exact repeated sentences, runs of seven or more words, near-duplicate sentences, and duplicate notes entries. It must report `No repeated sentences found.` Before a future build, update this checker to read that build's actual master.

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
     through `44 - ...md` as of 2026-10-05 — the count keeps shifting as
     chapters get inserted; check `ls chapters/` rather than trust a number
     written here — plus `Epilogue...md` and `Further Reading...md`,
     moved there from the top level on 2026-09-27 to sit next to their
     `.docx` counterparts) and the concatenated
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
    has an `.md` counterpart in `chapters/`. The physics chapter's two former `.md`-only
    sections were decided on 2026-10-11: "The rest of the ledger" is in the
    build (sourced); "The outlook, without a trumpet" is in the Held Back note,
    with the reasons.
  - 2026-10-04 coverage pass: the chapter `.md` files match the build again, except for the physics chapter's two
    documented sections. Chapters 21 and 22 are new (Latin America; the Ottoman Empire and the Middle East), so
    everything after them moved up by two. `notes/Held Back - Sections Written but Not in the Build.md` keeps the
    text of the sections that had been written for the `.md` track on 2026-10-01 and never ported, including two
    held for Lothar's decision (the Xi/Winnie-the-Pooh passage and the Greenland purchase-offer passage), both INCLUDED on 2026-10-11. Never add
    a section to a chapter `.md` without adding it to `_generate.js` in the same change, and give every new factual
    section matching entries in "Notes and Sources" (`chapters/Notes and Sources.md` and the `notes` array in
    `_generate.js`), each checked against Open Library, Crossref, or the publisher before it goes in.
  - **No repeated sentences** (Lothar, 2026-10-04): no sentence appears twice anywhere in the book, and a Timeline,
    Notes, or Further Reading entry may not restate a sentence from its chapter. Near-copies count. After every
    build, run `node scripts/check_repeats.js`; it reads `chapters/*.docx` and must report nothing. Its `ALLOWED`
    list holds the only exemptions (the Professor's "in the margin" lead-in, the Society-minutes label, Jefferson's
    phrase in the American Republic chapter, a Timeline date label shared by two events); add to it only for
    something that is repeated on purpose.
  - The back-matter appendix "A Timeline — For Humans Who Like Their
    History in Order" is the one exception: it exists only inside
    `_generate.js` (built via the `grade(date, description)` helper,
    grouped under `subhead()` era labels), with no `.md` counterpart to
    keep in sync. As of 2026-09-27 it runs from deep time through 2024,
    then two new eras, "The Near Future" and "The Far Future," extending it
    out to the heat death of the universe — sourced from Wikipedia's
    Timeline of the far future, 3rd millennium, and Anthropocene articles.
  - The "Half the World, All the Time" chapter does NOT exist as a standalone
    chapter (re-fixed 2026-10-05, after an earlier fix to the same effect did
    not survive a subsequent restructuring): it used to sit between the
    thesis-summarizing Long View chapter and the Epilogue, a catch-up chapter
    whose own text admits it's a catch-up chapter, breaking the book's
    momentum right before its climax. Its four timelines (population,
    suffrage, the UDHR, the history of zero/algebra/calculus) are folded
    into the Long View chapter's body and verdict, in both tracks and
    `_generate.js`; the Epilogue follows the Long View directly. Do not
    re-add it as a standalone chapter without re-solving this placement
    problem first — `scripts/check_repeats.js` will catch the reintroduced
    duplication if someone does. The Prologue's ancestor passages
    (Pakicetus/Ambulocetus/the hippo connection, the primate lineage) are
    unaffected and remain in sync across both tracks.
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
  `node_modules/` is already present; `scripts/check_repeats.js` also uses `jszip`, which `docx` installs).

## Rescore and Kindle pass, 10 October 2026

- **Score 7.8 → 8.7** (sampled reread of about a fifth of the book, front and back matter in full; see `SCORES.md`).
- **The build is the master again.** About the Author (bio B) and the review invitation had been added to the shipped `.docx` by hand and were missing from `_generate.js`; both are now in the build (`reviewLine`, `aboutAuthor`), so `node scripts/_generate.js` reproduces the deliverable.
- **Contents page:** a static list of links to every chapter heading (each `heading()` gets a bookmark), built in reading order. No Word TOC field any more, so nothing has to be updated in Word before upload.
- **Typography in one place:** `_generate.js` wraps `TextRun` so every run gets curly apostrophes and single quotes and an en dash in number ranges (1914–1918). Keep typing straight apostrophes in the source; identifiers like SP-2000-4408 are left alone.
- **Linked sources:** `scripts/source_links.json` maps a citation (Notes and Sources) or a Further Reading label to a verified link: Crossref DOI, Open Library work, or the official page. The title is the link text; no URL is printed. 254 of 278 notes and 20 of 21 Further Reading entries are linked; the rest (classical texts, constitutions and laws, reports with no stable record, A Fistful of Shells) stay plain. Never add an entry without checking that it resolves. `notes` and `furtherReading` are built by functions (`makeNotes`, `makeFurtherReading`) because docx records a link's relationship only in the first document an `ExternalHyperlink` is saved into.
- The five web sources no longer print their URLs; the titles link instead.
- Text: "the 2010s and 2020s" (Fractured Present); the Long View's seam into the four folded timelines now reads "Several timelines ran underneath everything else in this book…".
- **Covers (new):** `KINDLE_COVER_FINAL_2560.jpg` (1600×2560: parchment and sea, a navy dolphin leaping across a gold timeline, Cinzel title) and `KINDLE_BACK_COVER_2560.jpg` (single-colour navy, text only), from `scripts/make_front_cover.py` (+ `dolphin.py`) and `scripts/make_back_cover.py`.
- Known gap, not fixed here: the `.md` track has drifted from the build in places (the Complete Manuscript `.md` and chapter 44's `.md` do not carry the folded population, suffrage, UDHR and mathematics timelines in their current wording). The build is authoritative.

## Held-back pass, 11 October 2026

- **Both held passages are INCLUDED** (Lothar, 2026-10-11). Winnie-the-Pooh: two paragraphs in the China chapter after the Xi paragraph; the passage says "the leader the internet nicknamed Pooh" and does not name him. Greenland purchase offers: three paragraphs in the Climate chapter after the polar paragraph (1946, 2019, 2024-25). Both rewritten neutral and factual; sources in Notes and Sources (BBC, AFP/The Guardian, Foreign Relations of the United States, CNBC, BBC), linked by keyword, no printed URLs.
- **The current American president is never named:** the Greenland passage is a one-off exception for the subject only. The name never appears anywhere in this book or its notes; write "the American president", "Washington" or "the US government". Check with a search for the name before every commit (the word "trumpet" in a physics heading is not the name).
- **Physics chapter:** "The rest of the ledger" ported (trimmed, corrected, 13 sourced notes); "The outlook, without a trumpet" HELD in the Held Back note (repeats the appendix, Epilogue and Fractured Present chapter; dated claims; unsourced).
- **The `.md` track matches the build again.** The changed chapter `.md` files and the Complete Manuscript `.md` were regenerated from the built `.docx` (unchanged paragraphs kept verbatim; new ones written with straight quotes; source links as Markdown links). The Long View `.md` now has the four folded timelines; the Complete Manuscript `.md` now has the Timeline, the review line, About the Author and the current Also-by. The known gap noted on 10 October is closed. `chapters/Also by Lothar J. Musiol.md` is kept by the Also-by process and matches the build in content.
- Old master and old `.md` files: `bak/2026-10-11 pre-held-back/`.


## Review refinements, 16 October 2026

REV4 received a focused follow-up pass against an external review. The dictator overview’s repeated account of authoritarian takeovers was removed. Climate’s heat-dome paragraph now identifies the 619 heat-related deaths in British Columbia and summarizes the coroner’s profile of victims; the official report is cited in Notes and Sources. The Ottoman chapter now reads Articles 8 and 11 of the 1876 constitution together, with a cited primary-source entry. The Timeline’s Artemis II line reflects the completed 2026 mission. Six timeline strips, image alt text, and the Japanese primary-source/Professor scene were already present and verified. The Latin America chapter’s commission report and witness-based material were retained without expansion. No repeated sentences found after the edit.
