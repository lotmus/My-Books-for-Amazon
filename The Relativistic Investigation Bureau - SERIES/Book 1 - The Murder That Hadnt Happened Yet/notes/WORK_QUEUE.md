# Book 1 Release Work Queue

Updated 17 October 2026. Scope: *The Murder That Hadn't Happened Yet*, Book 1 of The Relativistic Investigation Bureau. REV14 remains the preserved release master; REV20 is the current review candidate and working pair; REV18 and REV19 are superseded and locally archived. REV17 is superseded and archived locally. No publication or author-account decisions are recorded as final.

## Completed in the 15 October clean-up

- Compared the active Book 1 files with the fetched parent-repository `origin/main` state. The REV17 manuscript source, DOCX, EPUB, covers, and description candidate are the current set; REV14 DOCX remains the designated master.
- Moved clearly superseded Book 1 versions into `bak/superseded-through-REV17-2026-10-15/` (script/text versions are in its `scripts/` subfolder). Preserved the uniquely useful REV14 master, REV17 build scripts, REV17 source/DOCX/EPUB, figures, and single-space `Kindle Back Cover.jpg`.
- Replaced the canonical `kdp_description.docx` with the REV17 description candidate. Its prior listing copy is archived. The misleading double-space `Kindle Back  Cover.jpg` is archived; it is not the current back-cover image.
- Completed continuity and developmental editorial review; see `notes/CONTINUITY_EDITORIAL_REVIEW_20261015.md`. Corrected stale separation-date and active-revision references in the series handoff, seam, character bible, and RIB agent instructions.
- Completed a focused critical-reader and science-clarity pass in REV18; see `notes/CONTINUITY_EDITORIAL_REVIEW_20261017.md`. The gravity explanation is tighter, the singularity definition is plain-language, and the REV18 DOCX builder uses the required 3.6 × 4.8 in page with 0.3 in margins and 3.0 in image width and 4.2 in image height. The paired REV18 EPUB builder is prepared but the EPUB has not been generated. The six active figures were inspected; the apple diagram now labels its curved grid as schematic, and an unused old equation JPG is preserved under `bak/`.

## Next work, in order

1. **Science and production verification:** Recheck the remaining scientific claims and mark the boundary between established physics and speculation; then build and preview the REV20 EPUB in Kindle Previewer across device layouts, orientations, and font sizes. Inspect cover, navigation, figures, equations, chapter starts, links, and final back-cover page; resolve defects and rerun preview after changes.
2. **KDP account confirmation:** Verify the title, series/number, contributor fields, age guidance (14+, with adult support for denser physics discussions for strong 12–13 readers), categories, keywords, description, and AI-content disclosure in KDP. The repository checklist and metadata files identify REV20; the canonical listing copy and age guidance are unchanged.
3. **Release decisions:** Author confirms publication date, price, KDP Select, optional links/photo, and final cover. Current front JPEG is 1152×1728 RGB: above KDP’s minimum, but below the ideal 1600×2560 size and 1.6:1 ratio. Re-export from source art if possible, without stretching. Investigate the EPUB's ~4.52 MiB size and duplicated cover image after preview; this is a quality optimization, not a recorded KDP rejection.
4. **Availability check:** Verify whether *Physics, Actually* is publicly available under the title used in Book 1's back matter; adjust only if the claim is inaccurate. After publication, verify the live detail and series pages.

## Release state and handoff

Do not upload until KDP preview, metadata verification, and author decisions are complete. Continuity reviews are recorded in `notes/CONTINUITY_EDITORIAL_REVIEW_20261015.md`, `notes/CONTINUITY_EDITORIAL_REVIEW_20261017.md`, `notes/CONTINUITY_EDITORIAL_REVIEW_REV19_20261017.md`, and `notes/CONTINUITY_EDITORIAL_REVIEW_REV20_20261017.md`. Keep the REV20 review-candidate source/DOCX/builder paired. Do not treat the superseded REV17, REV18, or REV19 files in local `bak/` as active. Do not stage or commit anything under `bak/`; it is a local recovery archive. See `KDP_LAUNCH_CHECKLIST.txt` for the operational checklist and `notes/_BOOK_SUMMARY.md` for canon.


## REV19 focused line edit — 17 October 2026

- Built the REV19 source/DOCX pair from REV18. Eight of the eighteen chapter-end `Rule:` labels were removed where the aphoristic line already lands cleanly; the sentences and course cross-links were retained. This addresses the cadence concern without removing the recurring motif.
- REV18 source, DOCX, and version-specific builder files were moved into `bak/superseded-by-REV19-2026-10-17/` (local recovery only; never commit `bak/`). REV14 remains release master.
- Prepared the REV19 EPUB builder from the previous version; it is available but was not run while the manuscript remains under review. See `notes/CONTINUITY_EDITORIAL_REVIEW_REV19_20261017.md` for the focused rescore. Full candidate is still not final: independent reader and Kindle visual QA remain open.


## REV20 opening-spoiler correction — 17 October 2026

- Removed the pre-story disclosure that the photograph did not come from the future and that a filing-system error resolved the case. Also removed the preview line about an incompetent filing system creating paradoxes. Kept the welcoming note, the fact/invention boundary, and the established science qualifications.
- Rebuilt the REV20 source/DOCX pair and prepared its EPUB builder; no EPUB was generated while the book remains under review. REV19 files are archived locally under `bak/superseded-by-REV20-2026-10-17/`; REV14 remains release master.
- The spoiler fix improves the mystery’s promise and protects its reveal. See `notes/CONTINUITY_EDITORIAL_REVIEW_REV20_20261017.md` for the focused reassessment.
