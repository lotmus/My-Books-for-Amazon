# Repository Guidelines

## Project Structure & Module Organization

This repository contains the Bavarian Cooking Kindle book and its production materials. The current `.docx` and `.epub` files are deliverables; `KDP_listing_draft.md` and `Bavarian Cooking - Recipe Review.md` hold publishing copy and editorial notes. `build/` contains Python production scripts, intermediate data, and generated working files. `photos/` holds recipe images and image review material. `source/` contains original and backup inputs; `bak/` preserves dated snapshots. Many working assets are excluded by `.gitignore`, so check ignore rules before assuming a new file will be committed.

## Build, Test, and Development Commands

Run the EPUB builder from the `build` directory, as its own header specifies:

```powershell
Set-Location build
python -I build.py
```

This rebuilds the Kindle EPUB from `build/pandoc_base.epub`, recipe transformation modules, and available photos. The build script removes and recreates its `build/x` extraction directory. Review `build/build_report.txt` after a build. The repository has no dedicated test framework or one-command test suite. `build/validate.py` checks generated XHTML after the build; run it from `build` when its expected `x/EPUB/text` output exists.

## Coding Style & Naming Conventions

Production utilities are Python scripts in `build/`. Follow nearby conventions: four-space indentation, descriptive `snake_case` names, UTF-8 text, and small focused changes. Recipe photo filenames use lowercase hyphenated slugs (for example, `bread-dumplings.png`). Preserve German dish names and units consistently with surrounding recipes. Do not edit generated EPUB internals by hand when the builder can regenerate them.

## Testing Guidelines

For recipe or layout changes, rebuild the EPUB and inspect the affected recipe pages and build report. Run `python validate.py` from `build` to check recipe sections and photo markup. There are no stated coverage thresholds; report any manual visual checks performed.

## Commit & Pull Request Guidelines

Recent commits use concise, descriptive subjects, often prefixed by the project name (for example, `Wee Scallywag: ...`). Use an imperative summary that identifies the book and change. A pull request should describe editorial or production changes, list the generated deliverables affected, link relevant review notes, and include screenshots only when they clarify a layout or image change.

## Assets & Publishing

Keep source images and licensing/credit information with the project records. Before preparing a KDP upload, verify the final DOCX/EPUB and cover together; do not treat intermediate files under `build/` as publication-ready.
