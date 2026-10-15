# Book 1 Release Work Queue

Updated 15 October 2026. Scope: *The Murder That Hadn't Happened Yet*, Book 1 of The Relativistic Investigation Bureau. REV14 remains the preserved release master; REV17 is the newest release candidate and current working pair. No publication or author-account decisions are recorded as final.

## Completed in this pass

- Compared the active Book 1 files with the fetched parent-repository `origin/main` state. The REV17 manuscript source, DOCX, EPUB, covers, and description candidate are the current set; REV14 DOCX remains the designated master.
- Moved clearly superseded Book 1 versions into `bak/superseded-through-REV17-2026-10-15/` (script/text versions are in its `scripts/` subfolder). Preserved the uniquely useful REV14 master, REV17 build scripts, REV17 source/DOCX/EPUB, figures, and single-space `Kindle Back Cover.jpg`.
- Replaced the canonical `kdp_description.docx` with the REV17 description candidate. Its prior listing copy is archived. The misleading double-space `Kindle Back  Cover.jpg` is archived; it is not the current back-cover image.

## Next work, in order

1. **Continuity review:** Read the complete REV17 candidate against `notes/_BOOK_SUMMARY.md`, series handoff/seam notes, and Book 2 setup. Check names, ages, dates/times, locations, chronology, physical props, relationships, clue plants/payoffs, chapter and lesson cross-references, and the final Book 2 hook. Report each inconsistency with location and proposed fix; correct confirmed errors and update the continuity notes.
2. **Editorial review:** Give the complete story and optional science material a fresh, critical line and developmental read. Assess clarity, voice, dialogue, description, pacing, suspense, humor, stakes, reveals, section boundaries, ending payoff, and suitability for curious SF readers without physics background. Fix specific, demonstrable issues in the REV17 source, rebuild the candidate, and preserve the REV14 master.
3. **Science and production verification:** Recheck scientific claims and mark the boundary between established physics and speculation; then preview the actual REV17 EPUB in Kindle Previewer across device layouts, orientations, and font sizes. Inspect cover, navigation, figures, equations, chapter starts, links, and final back-cover page; resolve defects and rerun preview after changes.
4. **KDP package sync:** Update `KDP_LAUNCH_CHECKLIST.txt`, `KDP_METADATA.txt`, and `notes/_BOOK_SUMMARY.md` to identify REV17 accurately and keep the listing description identical to the canonical REV17 copy. Confirm age guidance (14+, with adult support for denser physics discussions for strong 12–13 readers), categories, keywords, contributor fields, and AI-content disclosure in KDP.
5. **Release decisions:** Author confirms publication date, price, KDP Select, optional links/photo, and final cover. Current front JPEG is 1152×1728 RGB, below KDP's recommended 1600×2560; re-export from source art if possible, without stretching. Investigate the EPUB's ~4.52 MiB size and duplicated cover image after preview; this is a quality optimization, not a recorded KDP rejection.
6. **Availability check:** Verify whether *Physics, Actually* is publicly available under the title used in Book 1's back matter; adjust only if the claim is inaccurate. After publication, verify the live detail and series pages.

## Release state and handoff

Do not upload until continuity/editorial review, KDP preview, metadata verification, and author decisions are complete. Keep REV17 candidate/source/build files paired. Do not stage or commit anything under `bak/`; it is a local recovery archive. See `KDP_LAUNCH_CHECKLIST.txt` for the operational checklist and `notes/_BOOK_SUMMARY.md` for canon.
