# Repository Guidelines

## Project Structure & Source of Truth

This repository contains the Lolly Wren science mystery series. The book folders are `Book 1 - Schrodingers Paperwork/` and `Book 2 - The Permitted Options/`. Each holds its canonical master `.docx`, `chapters/` working text, `notes/` editorial references, `scripts/` book-specific utilities, and `bak/` snapshots. Series-wide continuity and handover material lives in `notes/`; shared scan and edit helpers live in root `scripts/`. Read `notes/SERIES_BIBLE.md` and the relevant book's `notes/MANUSCRIPT_GUIDE.md` before editorial changes. The master `.docx` is authoritative when it differs from chapter working files.

## Editing and Development

This is a manuscript repository, not a packaged software project; there is no general build or test command. Python utilities are run directly, for example `python scripts/dupscan.py "Book 1 - Schrodingers Paperwork/<master>.docx"` or `python scripts/phrasescan.py "Book 2 - The Permitted Options/<master>.docx"`. `scripts/apply_edits.py` supports guarded document edits; inspect its usage and the book-specific edit module, confirm the expected file size and timestamp, and run without `--write` first for a dry run. Use the relevant PowerShell scripts only for their documented book workflow.

## Manuscript and File Conventions

Keep chapter text in the existing `chapters/` organization and preserve its naming. Put editorial references and dated audit notes in `notes/`. Store snapshots under the book's `bak/`; never treat a backup as the live source or overwrite one. Preserve Word styles, links, bookmarks, paragraph order, and established punctuation when editing `.docx` files. Avoid broad reformatting or whole-document quote conversion during a targeted change. Keep generated `.epub`, `.pdf`, temporary, and backup artifacts out of commits as specified by `.gitignore`.

## Checks and Review

Run the relevant duplicate or phrase scan after substantial prose revisions, then review its findings in context; these scripts are aids, not automatic acceptance checks. Check manuscript-specific continuity, formatting, links, and notes before considering an edit complete. There is no configured coverage requirement or automated test suite.

## Commits and Pull Requests

Recent commits use concise, book-focused summaries describing the change and often its review or rebuild (for example, `The Permitted Options: front and back covers ...`). Follow that pattern. Describe the affected book and manuscript areas in the pull request, summarize editorial or formatting changes, and report the checks performed. Include before/after screenshots only when a visual layout change needs review. Do not commit or push unless the task explicitly requests it.
