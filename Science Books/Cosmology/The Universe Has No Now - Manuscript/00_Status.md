# Book 1 status — *The Universe Has No Now*

**Kitchen date:** 13 September 2026.  
**Author:** Lothar J. Musiol.  
**Title:** The Universe Has No Now.  
**Series:** Volume 1 of *Look First*. Books 2 and 3 were not opened.

This file is the close-out checklist after the Kindle-ready pass.

## Manuscript (closed)

- 45-chapter book in ten part files plus front matter and appendix. Headings match `00_Chapter_Outline.md` (Ch 1–45 / A0–A45).
- Front-matter order: title (Lothar J. Musiol) → minimal copyright (2026, all rights reserved) → How to Read → series note → Author’s Note → TOC marker → Prologue.
- No acknowledgments, credits, or NASA wall in the book body. Photo credits live only in `KDP_Description.md` for the Amazon field.
- Chapter 30 includes the 30-centimeter intelligence passage (after the saurian-mind paragraph, before “Civilization is the extra invoice”). Appendix A30 has the matching packing / neuron-count note.
- In-text figures remapped to Fig 0–45 (one per chapter). Dropped merge leftovers: leak-ring, second tree, stacked throat, landscape, cylinder helix, blocked throat, Goldilocks orbit-dots. No “Chapter 52” leftovers. No film titles.

## Word count

Popular text (front matter + Parts I–X + appendix). Stamp by running `BUILD_KINDLE.bat` (writes `export\WORD_COUNT.txt`). Chapter 30 added about 280 words; no settlement, longevity, or 10k-year rooms.

<!-- WORD_COUNT -->
**Manuscript words (body Markdown, 00_Front through 11_Appendix):** run `BUILD_KINDLE.bat` or `python export\assemble_export.py` — the integer is written to `export\WORD_COUNT.txt`. Order of magnitude remains ~120–130k words ≈ 400 Kindle pages if that file is not yet stamped in this session.
<!-- /WORD_COUNT -->

## Figures (honest tally)

| | Count |
|---|---:|
| Drawn diagrams (PNG line art) | **26** |
| Real photographs (NASA/ESA/EHT/SDSS JPEGs, credited in the Amazon description only) | **14** |
| Framed placeholders (real PNG files, auto-swap) | **6** |
| Missing slots with no file | **0** |
| **Total** | **46** |

Credits for the store page: `KDP_Description.md`. Author/production ledger: `Figures/CREDITS.md`.  
Pixels: `Figures/figs/`.  
Plan: `00_Figure_Plan.md` (45-chapter remap; old 52-grid retired).

## Kindle-ready vs still a drop-in

**On disk for ingest**

- Assembled manuscript builder: `BUILD_KINDLE.bat` → `The_Universe_Has_No_Now.md` plus `export\The_Universe_Has_No_Now.docx` (6×9, via `Figures\build_docx.py`) and `.epub` if pandoc is installed.
- Exact rebuild commands: `export\KINDLE_BUILD.md`.
- Amazon paste: `KDP_Description.md` (sell copy ~350 words, then Credits).
- Chapter headings are `##` so TOC/NCX works. Reflowable, not fixed-layout. No color-only meaning. Figure credits stripped from the Word body.

**Still not upload-ready**

- Cover JPEG (KDP’s current ratio; not in this folder).
- Six author/licensed stills: `fig00.jpg` · `fig01.jpg` · `fig31.jpg` · `fig32.jpg` · `fig34.jpg` · `fig42.jpg`. Framed placeholders ship until those drop in. Do not invent Hubble/Planck/EHT/rover/Cassini fakes for them.
- Kindle Create / KDP previewer pass (TOC, chapter starts, grayscale figures).
- Fig 20 is EHT CC BY 4.0 — attribution is in the Amazon Credits block, not under the picture.

## What this close did

- Wrote the 30 cm intelligence passage into Chapter 30 and A30.
- Reordered front matter; added a legal-minimum copyright page.
- Remapped figure numbers in Parts V–X; dropped extras from the old 52-chapter grid.
- Created the KDP description (sell copy + Credits only).
- Wired a one-click Kindle assemble/export. Did not open Books 2 or 3. Did not make a git commit.
