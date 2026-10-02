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
pandoc 00_Front_Matter.md 01_Part_One_No_Now.md 02_Part_Two_Past.md 03_Part_Three_Burst.md 04_Part_Four_Missing.md 05_Part_Five_Horizons.md 06_Part_Six_Getting_There.md 07_Part_Seven_Loops.md 08_Part_Eight_Copies.md 09_Part_Nine_Filter.md 10_Part_Ten_Future.md 11_Appendix.md --from markdown+raw_tex --toc --toc-depth=2 --resource-path=".;Figures/figs" --metadata title="The Universe Has No Now" --metadata author="Lothar J. Musiol" --to docx -o export/The_Universe_Has_No_Now.docx
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

1. Cover JPEG — `cover_typographic_v2_clockring.jpg` (1600×2560, no NASA), the clock-ring design the author chose on 1 Oct 2026. Upload this file as the Kindle eBook cover. `..\Figures\make_cover.py` draws it again. The light-cone cover is in `..\bak\export\`. KDP’s current ratio still wins if Amazon has moved.
2. Manuscript: the `.docx`.
3. Product description: paste from `..\KDP_Description.md` (sell copy, then Credits).
4. Open the file in Kindle Create or KDP previewer. Check TOC, chapter starts and grayscale figures. All 20 photo slots hold real photographs since 14 Sep 2026 (sources and licences in `..\Figures\CREDITS.md`).
5. To swap any of `fig00`, `fig01`, `fig31`, `fig32`, `fig34`, `fig42` for an author photo, drop the JPEG into `Figures\figs\`, update its credit line in `KDP_Description.md` and `CREDITS.md`, and rebuild.
