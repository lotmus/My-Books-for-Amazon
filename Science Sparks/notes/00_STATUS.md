# Science Sparks status — 16 October 2026

## Current version

- The active candidate is `scripts/build/Science Sparks - REV5.docx`, built from the Markdown source files.
- REV5 is a review candidate, not a publication-final master. The renderer required for page-by-page visual QA is unavailable in this environment, so layout sign-off remains open.
- The user's organized working folder is `D:\My Books for Amazon\SCIENCE  Series\Science Sparks`; the revised Markdown, DOCX, description, and build metadata are synchronized there under REV5 filenames.
- Rebuild source: `scripts/build_almanac.py`; chapter sources are in `chapters/`.

## Structure and references

- The eight parts are Mathematics, Physics and the Cosmos, Quantum Physics, Biology, Science in the Novels, Information, Computation and Intelligence, Earth, Climate and the Living Planet, and When Science Can Harm.
- Chapter numbers run continuously through 389. The current build has 430 contents entries, 1,084 cross-reference links, 20 figures, and 161 glossary terms.
- Mathematics already contains the five requested engineering-mathematics topics as chapters 4, 10, 8, 11, and 12. They remain together in Mathematics; no duplicate chapters were added.
- Quantum material remains together under Quantum Physics. Pointers now name only the current two books: *Quantum, Actually, Volume 1: Questions and Answers from the Double Slit to the Superconducting Wire* and *Quantum, Actually, Volume 2: A QED Course*.
- The book-specific Also-by exclusions requested by Lothar are applied; the shared canonical list was not changed.
- The mathematical and physics reader route no longer includes the device-focused reading list.
- The new Part 8 includes government and military research as one strand in a broader treatment of dual use, human research ethics, environmental harm, surveillance, risk and safeguards.
- EPUB is deferred until REV5 is reviewed and settled, per the user's instruction.

## Source recovery

- The main Git branch had no glossary Markdown source or figure assets, although the current DOCX contained both. The glossary was recovered from that master into `chapters/90_glossary.md`; figures were regenerated with `scripts/make_figures.py` so future builds preserve them.
- The build script now uses the canonical Version B author bio.
- `chapters/95_sources.md` supplies selected further reading and chapter-specific sources for selected time-sensitive, medical, or otherwise high-impact claims. It is not a citation for every claim in the older chapters.
- `notes/CRITICAL_REVIEW_REV2.md` records the baseline review. `notes/CRITICAL_REVIEW_REV5.md` records the post-revision review and remaining issues.
