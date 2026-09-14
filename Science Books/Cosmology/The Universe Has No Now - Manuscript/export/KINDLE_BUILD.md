# Kindle build — *The Universe Has No Now*

Reflowable book. Not fixed-layout. Meaning is never color-only.

## What should already be on disk

- Assembled manuscript: `..\The_Universe_Has_No_Now.md`
- Word (6×9 in., preferred KDP ingest): `The_Universe_Has_No_Now.docx`
- EPUB (if pandoc ran): `The_Universe_Has_No_Now.epub`

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

Then, from the manuscript folder:

```
pandoc The_Universe_Has_No_Now.md --from markdown+raw_tex+tex_math_dollars --toc --toc-depth=2 --resource-path=".;Figures/figs" --metadata title="The Universe Has No Now" --metadata author="Lothar J. Musiol" --to epub3 --epub-chapter-level=2 -o export/The_Universe_Has_No_Now.epub
```

Word via the Python builder (preferred over pandoc docx — 6×9, Georgia, one figure per chapter):

```
python Figures\build_docx.py "export\The_Universe_Has_No_Now.docx"
```

## KDP ingest

1. Cover JPEG (2560×1600 or KDP’s current ratio) — not in this folder.
2. Manuscript: the `.docx` or the `.epub`.
3. Product description: paste from `..\KDP_Description.md` (sell copy, then Credits).
4. Open the file in Kindle Create or KDP previewer. Check TOC, chapter starts, grayscale figures, and the six placeholder photos.
5. Drop real JPEGs for `fig00`, `fig01`, `fig31`, `fig32`, `fig34`, `fig42` into `Figures\figs\` and rebuild if you do not want framed slots in the store file.
