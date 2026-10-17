# Handover

## Current package — REV02

- Author byline: Seamus O'Leary. The name is a nod to Edward Lear. Use no other author identity in this edition.
- About the Author: expanded into an in-character nonsense story, retaining the Lear nod.
- User-approved content: names and topics, including political figures, are permitted; keep the selected poems funny, readable, and well-rhymed.

- Manuscript: `Limericks_and_Other_Rhymes_for_People_Who_Should_Know_Better_v2.md`
- Kindle upload candidate: `Limericks_and_Other_Rhymes_for_People_Who_Should_Know_Better_REV02.epub`
- DOCX fallback: `Limericks_and_Other_Rhymes_for_People_Who_Should_Know_Better_REV02.docx`
- Cover image: `images/cover.png`
- KDP listing draft: `KDP_METADATA.md`
- Rebuild command: run `python build_book.py` from this folder with Pandoc available.
- Contents: 176 Lear-based limericks (166 retain the selected original wording; 10 have been adapted to repair weak rhymes), 122 modern limericks, including 100 newly added, and 381 four-line rhymes, including 100 newly added and 80 rebuilt from ideas and images in the 10,000-stanza archive. The longer-poem section has four Lear poems and two Lewis Carroll poems.
- Archive: `notes/ARCHIVE_SCREENING.md` records the computational rhyme and duplicate screen of all 10,000 four-line stanzas in the 20 nominal 500-poem files and two editorial salvage batches. The 8,910 exact ABAB matches are a candidate pool, not a quality verdict. Eighty poems have been rewritten from archive ideas with clearer grammar and comic turns; continue reviewing the remaining candidates. The raw files remain in the local book `bak` folder and are not committed.
- Art: ten AI-generated interior illustrations plus an AI-generated cover. Interior art is embedded in both book files.
- Project Gutenberg source references are listed in the manuscript. Verify every classic text against digitized original editions and retain records in case KDP requests public-domain proof.

## KDP checks still open

- Render and inspect the DOCX fallback; LibreOffice is unavailable in the current environment.
- Open the EPUB in Kindle Previewer, check navigation and image behavior on representative devices, and confirm image alt text.
- Verify classic texts against digitized original editions and retain records in case KDP requests public-domain proof.
- Do the publisher's AI-generated text and image disclosure in the KDP form.
- Keep `(Illustrated)` in the title field and the two short originality bullets first in the KDP description. The book has ten relevant interior illustrations; KDP decides whether the edition meets its public-domain differentiation requirements.
- Obtain external reviews; this remains a draft until the standing five-cycle review rule is met.

Follow repository-level authoring and Git instructions.

## 17 Oct 2026 checkout reconciliation

The D: folder now has 18 active files, all byte-identical to current `main`. Before sync it had 17 exact current-main files and lacked only the REV02 fallback DOCX. Nine copies in other worktrees all matched main by SHA-256, and no Word lock file was present. The exact main DOCX was copied into D: and hash-verified; no local DOCX variant existed to back up.

The current-main REV02 DOCX, EPUB, and Markdown manuscript, plus the D: EPUB and Markdown copies, still produce one automated name-scan match. This book instruction records user approval for names and political topics. No poem text or artwork was changed to suppress the scan. The D: folder now has the byte-identical main fallback DOCX. The old REV01 DOCX, EPUB, Markdown source, and JPEG cover from the archive branch are already preserved exactly in the book `bak`; no archive branch was merged. External reviews, original-source verification, Kindle Previewer inspection, and KDP checks remain open before publication.
