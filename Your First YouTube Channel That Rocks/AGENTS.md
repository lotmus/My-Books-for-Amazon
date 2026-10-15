# Repository Guidelines

## Project Structure

This folder contains the *Your First YouTube Channel* book project. The current working manuscript is `Your_First_YouTube_Channel_REV23_sources.docx`. Draft Markdown in `chapters/`, scripts in `scripts/`, and figures in `figures/` include older material and are not a complete source for REV23. `notes/` holds project status, editorial rules, and review materials; `_source/` contains reference material; `bak/` holds historical files.

Before editing, read the current-state section at the top of `notes/_STATUS.md` and follow `notes/CLAUDE.md` for the detailed editorial constraints. Keep work within this book folder.

## Build and Development

The legacy builder is not compatible with the current manuscript. Do not run it against REV23 or treat it as a reproducible build. Before proposing a replacement workflow, establish and verify a complete source-to-DOCX process.

Run commands from this directory only for targeted checks that do not overwrite the manuscript:

- `python -m py_compile scripts\build_docx.py` — syntax-check the legacy builder only; this does not validate or build the current manuscript.

The builder uses `python-docx`. There is no separate local server or configured automated test suite; inspect the generated DOCX after substantial manuscript or layout changes.

## Writing and File Conventions

Keep any edits to legacy Markdown consistent with its UTF-8 encoding and existing Roman-numeral heading style. Do not assume those files regenerate REV23. Name new figures descriptively in lowercase kebab case.

For Python, use four-space indentation, descriptive names, and standard-library or already-used project dependencies. Avoid adding a second manuscript builder.

## Verification and Review

Do not replace the current DOCX with output from the legacy builder. For a new edition, identify its true source first, then render and inspect the complete DOCX and verify links, figures, and metadata. There is no configured automated test suite.

## Commits and Pull Requests

Recent repository commits use short, descriptive summaries, often naming the project or change (for example, `WIP: ...` or `Wee Scallywag: ...`). Use a concise imperative summary with the book or task identified. Pull requests should describe manuscript and generated-file changes, list the build or review performed, and include screenshots only when visual layout is relevant. Stage and commit only files from this project folder.
