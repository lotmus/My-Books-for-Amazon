# Kindle build — *The Universe Has No Now*

Reflowable book. Not fixed-layout. Meaning is never color-only.

## What should already be on disk

- Assembled manuscript: `..\The_Universe_Has_No_Now.md`
- Word (6×9 in., preferred KDP ingest): `The_Universe_Has_No_Now.docx`
- No EPUB and no PDF. Docx only (standing rule, 1 Oct 2026). Older EPUBs are in `..\bak\`.

## Rebuild

Double-click `..\BUILD_KINDLE.bat`, or from the manuscript folder:

```
python export\assemble_export.py
```

PowerShell-only fallback (no Python):

```
powershell -NoProfile -ExecutionPolicy Bypass -File export\concat_markdown.ps1
```

That concatenates front matter + Parts I–X + appendix, rewrites figure paths to `Figures/figs/`, and (if Python ran) calls `Figures\build_docx.py`.

Pandoc from the part files directly (no assembled file required):

```
pandoc 00_Front_Matter.md 01_Part_One_No_Now.md 02_Part_Two_Past.md 03_Part_Three_Burst.md 04_Part_Four_Missing.md 05_Part_Five_Horizons.md 06_Part_Six_Getting_There.md 07_Part_Seven_Loops.md 08_Part_Eight_Copies.md 09_Part_Nine_Filter.md 10_Part_Ten_Future.md 11_Appendix.md 12_Notes_and_Sources.md --from markdown+raw_tex --toc --toc-depth=2 --resource-path=".;Figures/figs" --metadata title="The Universe Has No Now" --metadata author="Lothar J. Musiol" --to docx -o export/The_Universe_Has_No_Now.docx
```

## Pandoc (if you need to rebuild by hand)

Install Pandoc from https://pandoc.org or:

```
winget install --id JohnMacFarlane.Pandoc -e
```

Pandoc is only a fallback for the docx; do not build an EPUB.

Word via the Python builder (preferred over pandoc docx — 6×9, Georgia, one figure per chapter):

```
python Figures\build_docx.py "export\The_Universe_Has_No_Now.docx"
```

## KDP ingest

1. Cover JPEG — `cover_typographic_v2_clockring.jpg` (1600×2560, no NASA), the clock-ring design the author chose on 1 Oct 2026. Upload this file as the Kindle eBook cover. `..\Figures\make_cover.py` draws it again. The light-cone cover is in `D:\bak\2026-10-01 Look First Book 1 cover\`. KDP’s current ratio still wins if Amazon has moved.
2. Manuscript: the `.docx`.
3. Product description: paste from `..\KDP_Description.md` (sell copy, then Credits).
4. Open the file in Kindle Create or KDP previewer. Check TOC, chapter starts and grayscale figures. All 20 photo slots hold real photographs since 14 Sep 2026 (sources and licences in `..\Figures\CREDITS.md`).
5. To swap any of `fig00`, `fig01`, `fig31`, `fig32`, `fig34`, `fig42` for an author photo, drop the JPEG into `Figures\figs\`, update its credit line in `KDP_Description.md` and `CREDITS.md`, and rebuild.

## Notes and sources (3 Oct 2026)

`12_Notes_and_Sources.md` comes after the appendix. It holds the numbered endnotes (`[^n]: …`) and a bibliography by chapter. In the chapters, the references are `[^n]` in reading order; a source cited again reuses its number. `build_docx.py` turns each reference into a superscript link to its note and makes each note’s own number a link back to the first reference. Outside links are ordinary hyperlinks (DOI, arXiv, SEP, NASA). Spacetime diagrams SD1–SD7 come from `Figures\draw_spacetime_figs.py`; run it before the build.

## 46 chapters (3 Oct 2026)

Chapter 30 was split into 30 and 31, so the book has 46 chapters and appendix notes A0–A46. Printed figure numbers follow chapter numbers, but figure files kept their names: `fig31`–`fig45` print as Figures 32–46, and `fig46.png` (from `Figures\draw_spacetime_figs.py`) prints as Figure 31. The mapping is `CHAPTER_FIG` in `Figures\build_docx.py`; `assemble_export.py` takes the file from the image path, not the caption number.
