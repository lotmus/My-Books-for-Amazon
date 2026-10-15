# Repository Guidelines

## Project Structure & Content

This repository contains the source and production files for *The Will Is Not the Legacy, Actually*. The book's editable manuscript is split into ordered Markdown chapters in `md/` (`00_front.md`, `01_part1.md`, etc.). Python utilities live in `src/`; the manuscript-to-Word builder is `scripts/build_docx.py`. `about.md` and `alsoby.md` supply back matter. Diagrams are in `src/diagrams/`, cover artwork and the current master `.docx` are at the repository root, `out/` receives generated builds, and `bak/` contains dated snapshots. `FACT_CHECK.md`, `Picture credits - The Will Is Not the Legacy, Actually.md`, `KDP_Description.md`, and `kindle_links.json` support fact checking and publication.

## Build and Development

The builder uses Python and `python-docx` to assemble chapter Markdown into a formatted Word file and reports heading/link and document-object counts:

```powershell
python scripts/build_docx.py
```

The script reads manuscript and image files relative to the repository and writes the generated `.docx` to `out/`. It requires Python and `python-docx`. No separate test suite or package manifest is present. Review the generated document in Word and compare it with the source before treating it as publication-ready.

## Editing and Style

Keep chapter filenames numbered and descriptive so alphabetical order preserves book order. Write manuscript changes in `md/`; avoid hand-editing generated Word output when the source can be changed. Python utilities use four-space indentation where blocks are present, descriptive snake_case names, and standard-library imports alongside `python-docx`. Preserve UTF-8 text and existing Markdown heading, link, and list conventions. Update fact-check and picture-credit records when the relevant manuscript or art changes.

## Verification

There are no automated tests or stated coverage requirements. For manuscript changes, rebuild the `.docx` when the build paths are configured, then inspect chapter order, internal links, images, tables, and page layout. For utility changes, run the affected script against a copy or controlled inputs and inspect its output before replacing deliverables.

## Commits and Reviews

Recent commits use concise, book-specific summaries describing the change and often the production result (for example, “...; docx and EPUB rebuilt”). Follow that pattern. A review should summarize changed chapters/assets, note any build or visual checks performed, and include screenshots only when layout or artwork changes need visual review. Keep backup snapshots clearly dated and do not commit temporary build output as source.
