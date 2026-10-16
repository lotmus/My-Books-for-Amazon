# Repository Guidelines

## Project Structure

This repository holds the Relativistic Investigation Bureau mystery series and its publishing materials. Each book has its own folder for manuscripts, covers, metadata, notes, and scripts. Book 1's current candidate is the REV16 source and paired release-candidate DOCX listed in `notes/NEXT_BOOK_HANDOFF.md`; REV14 remains the release master until the author approves a replacement. Book 2's active working pair is `The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV05_LINE_EDIT_DRAFT.md` and its matching DOCX; the release master remains `The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV04.docx`. Start story work with `notes/NEXT_BOOK_HANDOFF.md`, then consult `SERIES_SEAM.md`, `CHARACTER_AND_SETTING_BIBLE.md`, and `SERIES_BIBLE_continuity_chart.md`. Figures are in Book 1's `scripts/figures/`. There is no conventional application source or test tree.

## Manuscript and Build Workflow

Read the handoff and shared continuity notes before changing story material. Every book must work as a reader's first RIB book: resolve its own investigation, explain any relationship context needed in that volume, and never require a prior book to follow the plot. Carryover mysteries may stay open, but must be clearly separate from the current case. Preserve British spelling, established character facts, case chronology, and series voice. REV16 and REV05 are working candidates; do not replace release masters without explicit direction. Book 1's builder defaults to the REV16 candidate source and output; inspect its paths before rebuilding. Keep source text and its paired review DOCX in sync. Label generated files clearly.

## Style and Naming

Write prose in paragraphs and place each line of dialogue in its own paragraph. Use stable, descriptive filenames with book and revision identifiers (for example, `...BOOK_2_REV04`). Name review scripts for their task and include a date when appropriate. Use four-space indentation in Python; prefer the standard library or dependencies already used by the project. Avoid unrelated formatting changes.

## Validation

No automated test suite or coverage requirement is configured. For manuscript edits, compare the edited text with the current DOCX master, verify continuity against `notes/`, and review headings, links, figures, and Kindle layout in the generated document. Run only the build or review script relevant to the book you changed.

## Commits and Pull Requests

Use short, imperative commit subjects, as in recent history: `Trim two remaining Appendix repetitions`. A pull request should name the book and revision, summarize story or production changes, list rebuilt files, and report continuity and layout checks. Include rendered-page images when the layout changes.
