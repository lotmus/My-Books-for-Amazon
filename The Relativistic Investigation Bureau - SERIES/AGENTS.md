# Repository Guidelines

## Project Structure

This repository holds the Relativistic Investigation Bureau mystery series and its publishing materials. Each book has its own folder for manuscripts, covers, metadata, notes, and scripts. Book 1 REV20 is the current review candidate: `Book 1 - The Murder That Hadnt Happened Yet/scripts/manuscript_text_REV20_REVIEW_CANDIDATE.txt` and `Book 1 - The Murder That Hadnt Happened Yet/The_Murder_That_Hadnt_Happened_Yet_REV20_REVIEW_CANDIDATE.docx`. Its EPUB has not been generated; the paired builder is `scripts/build_epub_REV20.py`. REV17–REV19 are superseded and locally archived; REV14 remains the release master. See Book 1 `notes/WORK_QUEUE.md` and `notes/CONTINUITY_EDITORIAL_REVIEW_REV20_20261017.md`. Book 2's active working pair is `The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV05_LINE_EDIT_DRAFT.md` and its matching DOCX; the release master remains `The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV04.docx`. Start story work with `notes/NEXT_BOOK_HANDOFF.md`, then consult `SERIES_SEAM.md`, `CHARACTER_AND_SETTING_BIBLE.md`, and `SERIES_BIBLE_continuity_chart.md`. Figures are in Book 1's `scripts/figures/`. There is no conventional application source or test tree.

## Manuscript and Build Workflow

Read the handoff and shared continuity notes before changing story material. Preserve British spelling, established character facts, case chronology, and series voice. Book 1 REV20 and Book 2 REV05 are the current candidate/working revisions; do not replace release masters without explicit direction. The old Book 1 `manuscript_text.txt` export and current build scripts may target older revisions. Before syncing or building either book, inspect the script's source and output paths and use the matching active revision. Keep source text and its paired review DOCX in sync. Label generated files clearly.

## Style and Naming

Write prose in paragraphs and place each line of dialogue in its own paragraph. Use stable, descriptive filenames with book and revision identifiers (for example, `...BOOK_2_REV04`). Name review scripts for their task and include a date when appropriate. Use four-space indentation in Python; prefer the standard library or dependencies already used by the project. Avoid unrelated formatting changes.

## Validation

No automated test suite or coverage requirement is configured. For manuscript edits, compare the edited text with the current DOCX master, verify continuity against `notes/`, and review headings, links, figures, and Kindle layout in the generated document. Run only the build or review script relevant to the book you changed.

## Commits and Pull Requests

Use short, imperative commit subjects, as in recent history: `Trim two remaining Appendix repetitions`. A pull request should name the book and revision, summarize story or production changes, list rebuilt files, and report continuity and layout checks. Include rendered-page images when the layout changes.
