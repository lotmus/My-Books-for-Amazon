# Series Figure Accessibility Audit

**Audit date:** 13 October 2026  
**Scope:** Embedded figures in all nine DOCX masters and their extracted tagged-text mirrors.

## Findings and Fixes

- Checked 402 embedded figures across the nine masters. Books 3–9 already had substantive figure descriptions in DOCX image metadata.
- Added descriptions to the 38 undescribed Book 1 figures and 34 undescribed Book 2 figures. The descriptions name the visible components, axes, relationships, or trends, based on the figure contact sheets and their adjacent captions.
- Updated `scripts/diagrams/common/docx2src.py` to preserve each image's DOCX `descr` in the third field of its `FIG: image | caption | alt text` mirror line. Regenerated all nine book mirrors. All 402 extracted figure references now have a nonempty description.
- Corrected the Book 8 LoRa transmit frequency literal to `868.1f` in the current master and listing source. This makes the intended float conversion explicit and removes MSVC's narrowing warning.

## Verification and Limits

All nine DOCX packages opened; each contains a substantive description for every embedded figure, and each mirror contains the corresponding figure reference and description. Kindle Previewer reconverted the changed Books 1, 2, and 8 with Enhanced Typesetting supported, zero errors, and zero quality issues. The five Book 8 C++/Arduino listings compiled in a supplemental MSVC syntax pass with zero warnings after the literal change.

The visual inspection used contact sheets for Books 1 and 2, not full-resolution review of every image. No screen-reader usability session was conducted. These checks establish that descriptions are present and preserved into the mirrors; they do not prove that every description is optimal for every assistive workflow.


Figure 9.1 accessible-description correction (13 Oct 2026): a line-by-line comparison found stale approximate totals (2.52 W, 4.13 W, 1.90 W) in the figure's alt description although the caption, plot, and worked examples reported 2.552 W, 4.204 W, and 1.974 W. Updated the embedded DOCX image description to the exact worked totals and clarified the common 0.90 W conduction segment; regenerated Book 6's mirror. The saved master contains one updated description, the mirror contains the new values with all three stale totals absent, and the embedded chart asset is unchanged and visually shows the exact values. This corrects accessible text; it does not verify screen-reader usability.


## Current KPF package check (13 October 2026)

After the latest all-nine Kindle Previewer conversion, inspected each KPF archive. Each contains a `book.docx` whose SHA-256 matches the corresponding current root master exactly. Parsed those embedded DOCX files and confirmed all 402 figure descriptions remain present and nonempty (Books 1-9: 56, 59, 33, 54, 34, 27, 35, 54, and 50). This proves the current source and descriptions are packaged with the KPF; it does not prove that every Kindle app/device announces the descriptions correctly or that the descriptions meet each reader's needs. A screen-reader and device review remains open.


### Compiled resource verification

Checked each compiled `resources/book.kdf`: all 402 exact UTF-8 figure-description strings occur in the corresponding KPF resource. The descriptions therefore survive Kindle Previewer compilation. This does not prove that every Kindle app/device exposes or announces them correctly, or that the descriptions meet each reader's needs.
