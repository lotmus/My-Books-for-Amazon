# Repository Guidelines

## Project Structure & Module Organization

This repository contains the *Protocol Flamingo* manuscript and its Amazon KDP materials. `Protocol_Flamingo_REV10.docx` is the current manuscript; make story edits in that Word file. `build_docx.js` contains an earlier, shorter draft as JavaScript data and is not the source for REV10. `KDP_LISTING.md` holds the listing copy, keywords, categories, and pricing. The two `kdp ... Protocol Flamingo.jpg` files are cover assets. `notes/` contains status and editorial working notes; `bak/` contains dated and superseded snapshots. Keep new working notes in `notes/` and archival copies in `bak/`.

## Build, Test, and Development Commands

- `node build_docx.js` generates `Protocol_Flamingo_script_draft.docx` from the legacy script. It requires Node.js and the installed `docx` package. It does not rebuild REV10; do not treat its output as the current book.
- No automated test or lint command is configured. For manuscript changes, review the edited document in Word and confirm front matter, chapter order, and layout before delivery.

## Coding Style & Naming Conventions

The generator uses CommonJS JavaScript, two-space indentation, semicolons, and double-quoted strings. Preserve its existing helper and content patterns when editing it. Name dated backups descriptively (for example, `REV10 - YYYY-MM-DD pre-edit.docx`). Keep the canonical manuscript filename and KDP asset names stable unless a coordinated release requires renaming.

## Testing Guidelines

There is no test framework or coverage requirement. If you change `build_docx.js`, run `node build_docx.js` and inspect the generated draft; verify the script writes only `Protocol_Flamingo_script_draft.docx`. For Word edits, inspect the exported file visually, especially page breaks, headings, and front matter.

## Commit & Pull Request Guidelines

Recent repository commits use short, descriptive summaries, often naming the book or work and the concrete change (for example, `Wee Scallywag: ...`). Follow that pattern: state the project and change plainly. A pull request should summarize manuscript or production changes, list the files changed, and include relevant visual checks for layout or cover updates. Link an issue when one exists.

## Editorial and Release Notes

Keep listing details consistent with the title page and manuscript. Update `KDP_LISTING.md` when release metadata or description changes. Preserve prior deliverables in `bak/` before replacing a release file, and record meaningful editorial decisions in `notes/`.
