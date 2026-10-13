# Start Here: Continuing the Lolly Wren Series

Updated 12 October 2026. This page is the current entry point for planning the next installment. It summarizes authority and workflow; the Series Bible remains the detailed canon.

## Read in this order

1. Root `AGENTS.md` for repository editing rules.
2. `notes/SERIES_BIBLE.md` for fixed story facts, character voices, locations, timeline, physics already taught, and jokes/set pieces already used.
3. `notes/EDITORIAL_REVIEW_20261012.md` for the latest line/science review and checks.
4. `notes/SENSITIVITY_REVIEW_20261012.md` for the identity and representation review.
5. `notes/READER_EXPERIENCE_REVIEW_20261013.md` for the non-specialist reading path and front-matter guidance.
6. `notes/HANDOVER.md` for dated project history. Its older dated sections are historical; this page and the latest book status notes identify the current files.
7. The relevant book's `notes/MANUSCRIPT_GUIDE.md` and `_STATUS.md`. For Book 1 also read `notes/CHARACTER_AND_PLACE_GUIDE.md`.
8. Read the active manuscript itself before adding continuity that is not covered in the Bible.

## Active manuscript files

| Book | Current continuity source | File status |
|---|---|---|
| 1 | `Book 1 - Schrodingers Paperwork/Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx` | Canonical Book 1 master. |
| 2 | `Book 2 - The Permitted Options/The_Permitted_Options_BOOK_2_REVISION_20261005.docx` | Current reviewed working copy and continuity source. |
| 2 source | `Book 2 - The Permitted Options/The_Permitted_Options_BOOK_2_DRAFT.docx` | Original canonical draft; it was not promoted or overwritten by the review copy. Do not silently copy one over the other. |

Book 1's Kindle output is `Book 1 - Schrodingers Paperwork/Schrodingers_Paperwork_KINDLE.epub`. Book 2's current Kindle output is `Book 2 - The Permitted Options/The_Permitted_Options_KINDLE.epub`, built from the reviewed working copy. Their front covers are `KINDLE_COVER_FINAL_2560.jpg` in the corresponding book folders.

## Continuity at the end of Book 2

Book 1's 4C crisis is over: Gideon cut the coupling, 308 states were recovered as records, 103 were not, Margaret Chain did not return as a person, and the nine thousand dwellings remain uncertain by design. Lolly accepted the Principal Officer, Relational Integrity post. Do not reverse those outcomes.

Book 2 ends on 9 February 2027. Its fourteen citizens are not signed off as having gone anywhere; Ellen Prosper's card remains outside the file. The bench reading of 411 attometres is a measured displacement, not a wormhole width or identification. The nine cores remain unresolved; thirty-one are advancing, with the count unchanged for six weeks. Article Two's invitation clause and Eilstein's public schedule stand. The remaining open threads are catalogued in the Bible; use those entries rather than inventing a resolution.

## What the next book should do

Book 3 has no title, case, new department, instrument, or central physics topic selected yet. Treat unresolved threads as available story seeds, not decisions that already have an outcome. Before drafting, create `Book 3 - <Title>/` with `chapters/`, `notes/`, `scripts/`, and `bak/`; choose one DOCX master and record its authority in this page and the Series Bible.

The next story needs a new case and may introduce a new department, instrument, or area of physics not already covered in the Bible's teaching map. Keep Lolly central and let the Ministry's pressure for premature certainty create the human cost. Order still has a bill, and the bill must land somewhere. Keep the novels readable on their own while preserving the series history.

Do not replay the threshold arrival, 4C shutdown, the fourteen's case, the 411-attometre reading, or earlier consultant debates as if they were new. Do not resolve open threads merely to tidy the plot. Lolly and Gideon are close friends, never a romance subplot unless the author explicitly changes canon. Read the Bible's "Tone and humour" and "Stories already used" sections before drafting; vary recurring notebook, hat, ledger, instrument, and bureaucratic jokes instead of repeating their original beats.

## Science and editorial standard

Keep established evidence, interpretation, open theory, and invented story mechanisms distinct. Attribute real results accurately, state important assumptions, and say when a calculation is model-dependent or not experimentally tested. A fictional instrument may create the plot's effect, but a real theorem or measurement must not be presented as proof of that invention. The lessons may explain the real analogy; label the boundary plainly in the manuscript.

For an occasional SF reader who is curious but not science-trained, the scene and its stakes must work before the terminology does. Define a needed term in plain language at the point of use, and keep the optional lectures after the story. Put a brief front-matter note in each book: no science background is required, and the optional explanations are there if the story sparks curiosity.

Preserve voices, scene order, Word styles, links, bookmarks, and established punctuation. Make a backup under that book's `bak/` before edits. The DOCX master wins over chapter working copies. After substantial prose changes, run the root `scripts/dupscan.py` and `scripts/phrasescan.py` and review matches in context; planned refrains, headings, legal documents, and bibliography echoes may be intentional.

## Kindle EPUB workflow

From the repository root, convert the chosen DOCX with Pandoc EPUB3. Example (replace the title and paths):

```powershell
pandoc "Book 3 - <Title>/<BOOK_3_MASTER.docx>" --from=docx --to=epub3 --standalone --toc --toc-depth=3 --split-level=2 --metadata="title=Book 3 Title" --metadata="author=Quentin Edmund Darling" --metadata="language=en-GB" --epub-cover-image="Book 3 - <Title>/KINDLE_COVER_FINAL_2560.jpg" --css="scripts/kindle.css" --output="Book 3 - <Title>/<BOOK_3_KINDLE.epub>"
```

Write the EPUB beside its DOCX. Validate that it opens as a ZIP, contains `EPUB/nav.xhtml`, a cover image and cover metadata, and well-formed XHTML/OPF. Rebuild after every manuscript edit; never describe an older EPUB as current.
