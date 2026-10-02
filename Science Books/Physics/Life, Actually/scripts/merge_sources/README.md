# Merge sources (one-time, 2 October 2026)

These scripts produced the first version of `chapters/` from the two retired books.
They were run once on a scratch copy and are kept for the record; the chapters in
`chapters/` are now the sources to edit, and `scripts/build_book.py` builds the master.

- `evo2md.py` converted *Life: Evolution - Full Manuscript.docx* to Markdown and reflowed its
  one-sentence-per-line layout into paragraphs.
- `assemble.py` merged that with the Markdown chapters of *The Copy Is Never Exact*,
  renumbered every chapter and figure reference, and applied `patches.py`
  (overlap cuts, rewritten bridge sections, cross-reference fixes, Part openings)
  and `genheads.py` (section headings for the former Genetics chapters).
- `figcaps.py` holds the Genetics figure captions (old numbering 0–46; new number = old + 1).

The retired books are in `D:\bak\2026-10-02 Life merge\`.
