# Repository Guidelines

## Project Structure & Manuscript Organization

This repository contains the source and production files for *How to Publish Your First Kindle Book*. Edit the Markdown chapters in `chapters/`; their `00_`–`04_` prefixes define reading order. `scripts/build_master.py` assembles those files into a Word manuscript at the repository root. `visuals/` contains image assets, `bak/` holds prior working copies, and the root also contains the current REV41 DOCX and KDP description. Keep source edits in Markdown and treat generated manuscripts as build outputs. The Markdown and builder still need synchronization with the REV41 master before treating a new build as release-ready.

## Build, Test, and Development Commands

Run the builder from any directory with Python:

```powershell
python scripts/build_master.py
```

It requires `python-docx` (`python -m pip install python-docx`) and writes `How to Publish Your First Kindle Book.docx` in the project root. The builder currently references a `figures/` directory and named assets that are absent from this checkout; restore the matching illustrations before rebuilding. It reports unresolved internal-link anchors and an approximate word count. There is no separate automated test or lint command; review the generated document in Word after substantive changes.

## Writing and Formatting Conventions

Use UTF-8 Markdown, descriptive heading levels, and the existing chapter/appendix organization. Preserve numbered source notes such as `[1]` and Markdown links: the builder turns these into document links and bookmarks. Use standard Markdown for lists, tables, emphasis, and standalone image references. Keep chapter filenames zero-padded and descriptive (for example, `01_part_one_short_road.md`). The generated DOCX uses Georgia typography; make layout changes in the builder rather than manually styling an output file.

## Validation Guidelines

Before delivery, rebuild the DOCX and confirm the script reports no missing anchors. Check that chapter order, tables, links, image references, and page breaks render correctly in Word. For claims about current KDP policies, verify the linked official source and update the numbered note as needed.

## Commit and Pull Request Guidelines

Recent commits use concise, descriptive subjects, often naming the book and the change; no strict prefix convention is evident. Follow that pattern (for example, `How to Publish: fix chapter 8 cross-reference`). A pull request should summarize the manuscript change, identify affected chapters and generated files, and include relevant review notes or screenshots for layout changes. Keep unrelated book projects and backup files out of the change.
