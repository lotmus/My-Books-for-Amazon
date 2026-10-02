# Your First Book That Sells — the single KDP-publishing book

Merged 1 October 2026. This folder is the only home of the KDP/self-publishing book. "How to Publish and Make Good Money", the "How  to  Pubish and Make Good Money" folder, and the plain-language "Your First Book That Sells" edition are now one book with one master.

## Layout

- `Your First Book That Sells.docx` — the master (book root). Docx only; never build PDF or EPUB.
- `KDP_Description.md` — the KDP listing (book root).
- `chapters/` — the source, in build order:
  - `00_front_matter.md` — title page, copyright, How to Read This Book
  - `01_part_one_short_road.md` — Part I, chapters 1–15 (the old plain edition, `easy_book.md`)
  - `02_parts_two_to_eight_full_guide.md` — Parts II–VIII, chapters 16–32 (the old *How to Publish and Make Good Money*, chapters 1–17, renumbered +15, with cross-references and figure numbers updated)
  - `03_back_matter.md` — Appendices A–C, Glossary, Official sources, A Closing Word
- `figures/` — every picture used by either half.
- `scripts/build_master.py` — rebuilds the master from `chapters/`. `scripts/make_figures.py` redraws the Part I pictures.
- `notes/` — this file, `MERGE_2026-10-01.md`, and the old status/instruction files of both editions (history only; their author and folder instructions are superseded).
- `bak/` — ignored by git. Old docx versions, old build scripts, the misspelled folder, the nested `.git`.

## Rules

- Author: Lothar J. Musiol.
- The companion *Your First YouTube Channel That Rocks* (formerly *…That Sells*) is a separate book in its own folder.
- Facts last rechecked 1 October 2026. Recheck KDP Help before every upload.
- Stage only this folder when committing.
