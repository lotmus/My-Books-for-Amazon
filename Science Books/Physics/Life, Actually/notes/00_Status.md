# Status: *Life, Actually* (2 October 2026)

- Master: `Life, Actually.docx`, built by `scripts/build_book.py` from `chapters/*.md`.
- 11 Parts, 84 numbered chapters, Prologue, Epilogue; 50 figures; about 195,000 words; 716 pages at 6 × 9 in (LibreOffice render).
- Contents page numbers are pre-filled from a LibreOffice render (`scripts/toc_pages.py` → `notes/toc_pages.json`). Word refreshes them on opening (answer Yes to the update-fields prompt), because Word's pagination differs slightly.
- Part XI (chapters 77–84) is new, current to October 2026. Facts that are still moving and should be re-checked before publication: Mars Sample Return funding, Tianwen-3 and Rosalind Franklin dates, TRAPPIST-1 e and K2-18 b reanalyses, Venus phosphine, exoplanet count, Europa Clipper and Dragonfly schedules, mirror-life policy.
- Open decisions for Lothar: see the final report and the "Deliberate deviations" list in `00_Plan.md`.

## Rebuild

    python scripts/build_book.py              # writes Life, Actually.docx
    python scripts/toc_pages.py "Life, Actually.docx" && python scripts/build_book.py   # refresh Contents page numbers (needs LibreOffice)
    python scripts/draw_new_figs.py           # only if Figures 48–50 change
