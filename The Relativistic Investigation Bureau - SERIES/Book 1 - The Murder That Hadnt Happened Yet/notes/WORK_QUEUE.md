# Book 1 Release Work Queue

Updated 15 October 2026. Scope: *The Murder That Hadn't Happened Yet*, Book 1 of The Relativistic Investigation Bureau. REV14 remains the preserved release master; REV17 is the newest release candidate and current working pair. No publication or author-account decisions are recorded as final.

## Completed in this pass

- Compared the active Book 1 files with the fetched parent-repository `origin/main` state. The REV17 manuscript source, DOCX, EPUB, covers, and description candidate are the current set; REV14 DOCX remains the designated master.
- Moved clearly superseded Book 1 versions into `bak/superseded-through-REV17-2026-10-15/` (script/text versions are in its `scripts/` subfolder). Preserved the uniquely useful REV14 master, REV17 build scripts, REV17 source/DOCX/EPUB, figures, and single-space `Kindle Back Cover.jpg`.
- Replaced the canonical `kdp_description.docx` with the REV17 description candidate. Its prior listing copy is archived. The misleading double-space `Kindle Back  Cover.jpg` is archived; it is not the current back-cover image.
- Completed continuity and developmental editorial review; see `notes/CONTINUITY_EDITORIAL_REVIEW_20261015.md`. Corrected stale separation-date and active-revision references in the series handoff, seam, character bible, and RIB agent instructions. No story-text continuity defect requiring a manuscript edit was found.

## Next work, in order

1. **Science and production verification:** Recheck scientific claims and mark the boundary between established physics and speculation; then preview the actual REV17 EPUB in Kindle Previewer across device layouts, orientations, and font sizes. Inspect cover, navigation, figures, equations, chapter starts, links, and final back-cover page; resolve defects and rerun preview after changes.
2. **KDP account confirmation:** Verify the title, series/number, contributor fields, age guidance (14+, with adult support for denser physics discussions for strong 12–13 readers), categories, keywords, description, and AI-content disclosure in KDP. The repository checklist and metadata files already identify REV17 accurately.
3. **Release decisions:** Author confirms publication date, price, KDP Select, optional links/photo, and final cover. Current front JPEG is 1152×1728 RGB, below KDP's recommended 1600×2560; re-export from source art if possible, without stretching. Investigate the EPUB's ~4.52 MiB size and duplicated cover image after preview; this is a quality optimization, not a recorded KDP rejection.
4. **Availability check:** Verify whether *Physics, Actually* is publicly available under the title used in Book 1's back matter; adjust only if the claim is inaccurate. After publication, verify the live detail and series pages.

## Release state and handoff

Do not upload until KDP preview, metadata verification, and author decisions are complete. Continuity and editorial review is recorded in `notes/CONTINUITY_EDITORIAL_REVIEW_20261015.md`. Keep REV17 candidate/source/build files paired. Do not stage or commit anything under `bak/`; it is a local recovery archive. See `KDP_LAUNCH_CHECKLIST.txt` for the operational checklist and `notes/_BOOK_SUMMARY.md` for canon.
