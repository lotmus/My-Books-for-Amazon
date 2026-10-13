# Book 9 Series Integration Status

Updated 12 October 2026 after the repository production audit.

## Completed in this repository

- Books 1–7 now follow the canonical series order and list both Book 8 and Book 9, with matching Kindle link rules. Book 9 itself lists Books 1–8.
- Book 7 Chapter 19 points to Book 9 Chapter 36 for production-test workflows. Chapter 28 points to Book 9 Chapter 33 for EMC pre-compliance instruments.
- Book 6 now has `kindle_links - Power_and_Energy_Book6.json`.
- Chapter text and figure mirrors for Books 6, 7, and 9 have been refreshed from their DOCX masters. Book 9's mirror contains all 38 chapters.

## Refreshing Book 9 source mirrors

The DOCX master remains authoritative. After editing it, run from the repository root:

```powershell
python scripts/diagrams/b9/refresh_sources.py --chapters 38
```

This extracts `front.txt`, one `src/chNN.txt` per chapter, `src/back.txt`, and the figures into `chapters/Book9/`. It does not rebuild the DOCX from the tagged-text mirror.

## Shared series files

The canonical list and `SCORES.md` live in the parent workspace; both include Book 9. Book 8's master has since been restored and reviewed; see `notes/EE8_REVIEW_2026-10-12.md`. Book 9's review and safety corrections are recorded in `notes/EE9_REVIEW_2026-10-12.md`. No cover files are maintained here.
