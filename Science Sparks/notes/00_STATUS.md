# Science Sparks status — 16 October 2026

## Current version

- `Science Sparks.docx` is the current master, rebuilt from the Markdown sources with the figures and glossary present.
- The previous master is preserved in `bak/2026-10-16 structure-consolidation/Science Sparks.docx`.
- Rebuild source: `scripts/build_almanac.py`; chapter sources are in `chapters/`.

## Structure and references

- The five main sections are Mathematics, Physics and the Cosmos, Quantum Physics, Biology, and Science in the Novels.
- Mathematics already contains the five requested engineering-mathematics topics as chapters 4, 10, 8, 11, and 12. They remain together in Mathematics; no duplicate chapters were added.
- Quantum material remains together under Quantum Physics. Pointers now name only the current two books: *Quantum, Actually, Volume 1: Questions and Answers from the Double Slit to the Superconducting Wire* and *Quantum, Actually, Volume 2: A QED Course*.
- The book-specific Also-by exclusions requested by Lothar are applied; the shared canonical list was not changed.
- The mathematical and physics reader route no longer includes the device-focused reading list.

## Source recovery

- The main Git branch had no glossary Markdown source or figure assets, although the current DOCX contained both. The glossary was recovered from that master into `chapters/90_glossary.md`; figures were regenerated with `scripts/make_figures.py` so future builds preserve them.
- The build script now uses the canonical Version B author bio.
