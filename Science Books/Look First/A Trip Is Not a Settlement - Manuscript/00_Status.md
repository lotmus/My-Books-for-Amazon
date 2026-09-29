# Book 2 status — *A Trip Is Not a Settlement*

**Kitchen date:** 16 September 2026.  
**Author:** Lothar J. Musiol.  
**Title:** A Trip Is Not a Settlement.  
**Subtitle:** The Moon, Mars, and Why Leaving Does Not Clean the Earth.  
Folder on disk is `A Trip Is Not a Settlement - Manuscript`. The previous Kindle file, `A Permit Is Not a City - Kindle.docx`, is in `bak`.  
**Subtitle:** Moon, Mars, and Why Leaving Does Not Clean the Kitchen.  
**Series:** Volume 2 of *Look First*. Books 1 and 3 were not reopened in this pass.

## Manuscript

- 16 chapters in four part files plus front matter and appendix. Headings match `00_Chapter_Outline.md` (Ch 1–16 / A0–A16).
- Front-matter order: title → How to Read (temperatures) → stands-alone note → Author’s Note → TOC marker.
- Photo credits belong in `KDP_Description.md` for the Amazon field, not under figures.
- Sequel rooms stayed closed: no CMB / wormhole courtroom, no CRISPR / healthspan / 10% brain unlock, no official-year Gantt as destiny.

## Word count

**Stamp after 16 Sep thicken pass:** **48,627 words** in an earlier script count. The markdown in this folder measured shorter. **29 Sep 2026** second thicken: landing attempt, who stays, recovery clocks, cleanup arithmetic, and the bill of going brought up toward the chapters that already teach (about 1,300 words). Script total for the folder about 25,000 words; reader text (front, parts, appendix) about 23,000.

## Figures

| | Count |
|---|---:|
| Drawn diagrams (PNG) | **15** (`fig01`–`fig12`, `fig14`–`fig16`) |
| Real photograph | **1** (`fig13.jpg`, Earth — NASA/DSCOVR EPIC class) |
| Framed placeholders still live | **0** in the build path if `fig13.jpg` wins over `fig13_slot.png` |
| **Total figure embeds in text** | **16** |

Plan: `00_Figure_Plan.md`. Pixels: `Figures/`.

## Kindle-ready vs still a drop-in

**On disk**

- Part markdown + appendix as listed above.
- Kindle Word: `A Trip Is Not a Settlement - Kindle.docx` (rebuild with `python Figures\build_book.py permit`).
- Amazon paste: `KDP_Description.md`.

**Still human**

- Open the rebuilt `.docx` in Kindle Create / KDP previewer (TOC, chapter starts, grayscale).
- Confirm Fig 13 credit line on the Amazon Credits block.

## What this pass did

- Thickened remaining thin popular chapters in Parts II–IV.
- Wrote this status file and `KDP_Description.md`.
- Rebuilt the Kindle `.docx` via `build_book.py permit`.
- Did not open Books 1 or 3. Did not make a git commit --trailer "Co-authored-by: Cursor <cursoragent@cursor.com>".


## Close-out, 16 Sep 2026

- SP-method gap close: popular-wrong + Rule on every Ch1–16; invented cast → roles (Mara/Rohan kept).
- Rebuilt `A Trip Is Not a Settlement - Kindle.docx` — KINDLE_CREATE READY (validate pass).
- Stamp: **48,627** words. Thin: none. Missing Rules: none.
- Human only: Kindle Create / KDP previewer.

## Gap close (SP method)

- Stamp: **48,627** words. Thin: none. Chapters missing Rule: none.
- Every popular chapter now ends with popular-wrong + Rule.
- Kindle rebuilt this pass.

## "Gentle on the clueless reader" pass extended to front matter + appendix, 2026-09-26

Following the standing rule added 2026-09-25 (main chapters only, at that point — see [[books-workflow-preferences]] in memory), Lothar asked for the same check on `00_Front_Matter.md` and `11_Appendix.md`. Read both directly (85 and 354 lines). Both were already close to clean — front matter teaches its own temperature system from scratch, and the appendix mostly reuses terms the main chapters had already glossed. Real gaps found and fixed:

- **"the aerosol parasol"** — used with zero explanation in the front matter's "Warm" bullet (and in the identical duplicate sentence that opens Chapter 1's own temperature definitions), even though the concept — industrial haze masking part of greenhouse warming — isn't explained until deep into Part Four (Ch 15/A15). Added "the industrial haze that has been quietly blocking some sunlight and masking part of the warming" at both the front-matter and Chapter-1 occurrences.
- **"LEO → TLI"** (Appendix A4's Δv sketch) — both acronyms bare, never expanded anywhere in the book (main chapters always spell out "low Earth orbit" in full and never use "TLI" at all). Expanded both inline: "LEO (low Earth orbit) → TLI (trans-lunar injection, the burn that leaves Earth orbit for the Moon)."
- **"cis-lunar"** — used in Appendix A6 and, at its true first use, in Chapter 2's own Artemis-II section, with no gloss in either place. Added "a path that stays within the Earth-Moon system rather than landing" at both spots.
- **Bonus fix found while cross-checking, unrelated to jargon:** a pre-existing straight apostrophe in Chapter 2 ("Chapter 8's appendix") — the one straight quote left anywhere in the book — converted to curly.

Left alone on purpose, matching the appendix's own denser-reference calibration: "HLS" (expanded in the line immediately below its own heading), "NRHO" and "ILRS" (both already glossed at first use, in the appendix and in Chapter 2 respectively), "MOXIE" (already explained functionally in Chapter 3 and reused correctly). **Noted but not fixed, flag to Lothar:** the "Equations at a Glance" table lists a relation (14), "Overrun ratio: 1× (Apollo) ≪ several× (ISS) ≪ 20× (a space telescope)," with no corresponding explanatory note anywhere in the appendix body (A1–A16) — looks like a genuine leftover gap, not a gentleness issue, and fixing it properly would need real sourced numbers rather than a quick gloss.

One edit (the Chapter 2 fixes) hit repeated "file modified since read" conflicts on the first several attempts, consistent with another session actively touching this file at the same time (per the BOOKS parallel-session note in memory) — waited and re-read fresh each time rather than forcing an overwrite; all edits eventually landed cleanly and were confirmed present in the rebuilt docx.

Rebuilt via `python Figures\build_book.py permit`. Verified after rebuild: 36 Heading 2s, 16 Figure Captions, **0 straight quotes/apostrophes anywhere in the book** (down from 1 pre-existing one). Word count moved to 73,785 at this check, though a concurrent session's own edits were also landing on Chapter 2 during this pass, so that number reflects both changes, not just this one.
