# Your First Book That Sells — the single KDP-publishing book

Merged 1 October 2026. This folder is the only home of the KDP/self-publishing book. "How to Publish and Make Good Money", the "How  to  Pubish and Make Good Money" folder, and the plain-language "Your First Book That Sells" edition are now one book with one master.

## Layout

- `Your First Book That Sells.docx` — the master (book root). Docx only; never build PDF or EPUB.
- `KDP_Description.md` — the KDP listing (book root).
- `chapters/` — the source, in build order:
  - `00_front_matter.md` — title page, copyright, How to Read This Book (who it is for and not for, author positioning, the five claim labels)
  - `01_part_one_short_road.md` — Part I, chapters 1–15: one action per chapter, ending with "Do these seven things this week"
  - `02_parts_two_to_eight_full_guide.md` — Parts II–VIII, chapters 16–32 (the old *How to Publish and Make Good Money*, chapters 1–17, renumbered +15, with cross-references and figure numbers updated)
  - `03_back_matter.md` — A Closing Word, Appendices A–D (D = thirty-two ways a book can pay you), Glossary, Notes [1]–[30] (checked 3 October 2026), About the Author
  - `04_also_by.md` — shared Also-by list (canonical; do not edit here)
- `figures/` — every picture used by either half.
- `scripts/build_master.py` — rebuilds the master from `chapters/`. `scripts/make_figures.py` draws all 12 figures used by the book (matplotlib). Older figures (fig01–fig15, etc.) are no longer referenced and kept for history.
- `notes/` — this file, `MERGE_2026-10-01.md`, and the old status/instruction files of both editions (history only; their author and folder instructions are superseded).
- `bak/` — ignored by git. Old docx versions, old build scripts, the misspelled folder, the nested `.git`.

## Rules

- Author: the pen name “Kevin Drew Peters” alone, as Lothar decided on 2026-10-03. Use it on the cover, title page, copyright line, also-by heading, About the Author, KDP files and the build script (`AUTHOR`); no real name in the book.
- The companion *Your First YouTube Channel That Rocks* (formerly *…That Sells*) is a separate book in its own folder.
- Facts last rechecked 3 October 2026 (see `notes/REVISION_2026-10-03.md`). Recheck KDP Help before every upload.
- Every platform claim carries a numbered note [n]; every claim is labelled Platform rule / Worked example / Field practice / Recommendation / Test it yourself.
- Examples use generic people and kinds of books only: no personal names, none of Lothar's own titles.
- Stage only this folder when committing.
