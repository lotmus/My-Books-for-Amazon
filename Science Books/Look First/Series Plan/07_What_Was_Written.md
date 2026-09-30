# What Was Written — File Map and Honest Counts

**Kitchen date:** 15 September 2026. Counts are stamps from the files on disk, not estimates. Re-run the word counts before trusting them a month later.

Series root: `C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\`

---

## The three books at a glance

| Book | Manuscript folder | Chapters | Words (parts + appendix) | Kindle file | State |
|---|---|---:|---:|---|---|
| 1 | `The Universe Has No Now - Manuscript\` | 45 + Prologue | **112,690** (assembled) | `export\The_Universe_Has_No_Now.docx` (361 pp., 46 figures, rebuilt 15 Sep 2026) | Closed. Awaiting author cover check and KDP previewer pass. |
| 2 | `A Trip Is Not a Settlement - Manuscript\` | 16 | **17,884** (16,240 main + 1,721 appendix, 1,155 front) | `A Trip Is Not a Settlement - Kindle.docx` (built 13 Sep 2026, 16 figures) | First draft, outline-thin. |
| 3 | `A Longer Life Is Not a New Body - Manuscript\` | 16 | **18,152** (16,717 main + 1,513 appendix, 1,891 front) | `A Longer Life Is Not a New Body - Kindle.docx` (built 13 Sep 2026, 14 figures + 2 placeholders) | First draft, outline-thin. |

The bible's length target for Books 2 and 3 is ~70–90k words each. Both drafts sit at roughly one quarter of that. Book 1 was in the same state (44,172 words) before its lengthening pass took every thin chapter to ~1,800–2,200 words of body. The same pass is what Books 2 and 3 owe. Chapters are ~500–1,500 words each now; a teaching chapter in this series runs ~2,000.

---

## Book 1 — *The Universe Has No Now*

- Parts: `01_Part_One_No_Now.md` … `10_Part_Ten_Future.md`, plus `00_Front_Matter.md` and `11_Appendix.md` (A0–A45).
- Assembled markdown: `The_Universe_Has_No_Now.md`. Rebuild everything with `python export\assemble_export.py` from the manuscript folder.
- Word count stamp: `export\WORD_COUNT.txt` (112,690).
- Figures: 26 drawn diagrams + 14 space photographs + 6 earthly photographs = 46, one per chapter (Fig 0–45). No placeholders. Credits in `KDP_Description.md` (Amazon field) and `Figures\CREDITS.md`.
- Cover: `export\cover_typographic.jpg` (1600×2560), not yet checked by the author.
- Close-out record: `00_Status.md`.
- The older `The Universe Has No Now - Kindle.docx` in the manuscript root (12 Sep) is superseded by the export folder file. Do not upload it.

## Book 2 — *A Trip Is Not a Settlement*

- Parts: `01_Part_One_Dirt_Delay_Dates.md` (Ch 1–3), `02_Part_Two_The_Moon_First.md` (Ch 4–9), `03_Part_Three_Vehicle_Not_City.md` (Ch 10–12), `04_Part_Four_Who_Stays.md` (Ch 13–16); `00_Front_Matter.md`; `11_Appendix.md` (A0–A16).
- Chapter headlines and appendix map: `00_Chapter_Outline.md`. Matches the plan in `02_Book_2_Outline.md` title for title.
- Figures: `Figures\fig01–fig16`, 15 drawn + Fig 13 a NASA DSCOVR EPIC full-Earth frame. Build with `python Figures\build_book.py permit`.
- The sample pages `04_Sample_Earth_Recovery.md` and `05_Sample_Moon_Mars_How_Soon.md` have been folded into the draft (their sentences appear in Ch 1, Ch 11–12 and Ch 13–16). The samples are now historical.
- Thinnest rooms: Ch 9 (641 words), Ch 15 (672), Ch 13 (707), Ch 8 (781), Ch 6 (788).

## Book 3 — *A Longer Life Is Not a New Body*

- Parts: `01_Part_One_Many_Clocks.md` (Ch 1–5), `02_Part_Two_The_Organ_You_Already_Use.md` (Ch 6–8), `03_Part_Three_Not_A_Straight_Line.md` (Ch 9–12), `04_Part_Four_The_Honest_Body.md` (Ch 13–16); `00_Front_Matter.md` (with Prologue); `11_Appendix.md` (A0–A16).
- Chapter headlines and appendix map: `00_Chapter_Outline.md`. Matches `03_Book_3_Outline.md` title for title.
- Figures: 14 drawn; **Fig 1 and Fig 16 are framed placeholders** waiting for original still-life photographs (hands over a basil tray; the pH notebook). Drop `fig01.jpg` / `fig16.jpg` into `Figures\` and rerun `python Figures\build_book.py body`.
- The sample page `06_Sample_Longevity_Brain.md` has been folded into the draft (Front Matter and Ch 1–8). Historical.
- Thinnest rooms: Ch 15 (501 words), Ch 14 (573), Ch 16 (597), Ch 12 (719), Ch 11 (795). Part IV is the thinnest part in the series.

---

## Series Plan folder (this folder)

| File | Status |
|---|---|
| `00_Series_Bible.md` | Live. Furniture, IN/OUT, positioning. |
| `01_What_Stays_in_Book_1.md` | Done. Book 1 is closed; the solvent expansion it describes is written. |
| `02_Book_2_Outline.md`, `03_Book_3_Outline.md` | Superseded in detail by each book's `00_Chapter_Outline.md`; keep for the temperature tables and the queued-question map. |
| `04–06_Sample_*.md` | Historical. Text already lives in the manuscripts. |
| `07_What_Was_Written.md` | This file. |

Root file `00_Book_Spine.md` (one level up) is Book 1's original locked spine and still carries the old ~127k budget; the actual close-out figure is in `00_Status.md`.

---

## What is next, in order

1. Author: look at Book 1's cover JPEG, run the KDP previewer, paste `KDP_Description.md`.
2. Book 2: lengthening pass, chapter by chapter, to teaching length, then a **date pass** on Artemis / Starship / ILRS years before upload. Rebuild the Kindle file.
3. Book 3: lengthening pass, two still-life photographs, rebuild.
4. Neither Book 2 nor Book 3 has a `KDP_Description.md` or a cover yet.
