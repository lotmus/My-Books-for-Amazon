# Repository Guidelines

## Project Structure

This is a German-language emigration guide and Kindle production repository. The editable chapter sources are Markdown files under `manuscript/`, grouped by destination (currently `02_USA/`, `03_Australien/`, and `05_Neuseeland/`). `notes/` holds editorial and research status; `scripts/` and `lib/` are reserved for production tooling. Root-level DOCX files, cover images, and KDP copy are publication assets. `build/` and `review_render/` contain generated review artifacts and are ignored by Git. `bak/` contains archival material; do not treat duplicate or backup chapters as current source.

## Editing and Style

Write reader-facing manuscript text in German and preserve the existing chapter filenames and numbering (for example, `T06_K26_…md` or `TNZ_K09_…md`). Keep edits focused in the relevant destination folder. Preserve Markdown structure, links, tables, and established terminology. This guide covers immigration, tax, healthcare, and other time-sensitive topics: date claims with the repository’s “Stand” convention, verify them against authoritative current sources, and record research or unresolved checks in `notes/`. Avoid silently changing advice that affects multiple destinations.

## Build, Review, and Tests

No standard build or test command is currently documented in the repository. `node_modules/` is ignored and `.gitignore` notes npm build dependencies, but there is no root `package.json`; do not assume `npm test` or `npm run build` exists. Before delivering manuscript or layout changes, review the edited Markdown and relevant notes, then inspect the generated DOCX/PDF/EPUB only when a project-specific production workflow is available. Do not commit generated files from `build/` or `review_render/` unless explicitly required as publication assets.

## Commits and Pull Requests

Recent history uses short, descriptive subject lines, often prefixed with `Auswandern:` and naming the editorial change. Follow that pattern, e.g. `Auswandern: update New Zealand visa references`. Explain the affected destination or chapters and summarize source checks in the change description. Include before/after page or render evidence when a layout change needs visual review; mention any claims that still need verification.

## Repository Care

Keep publication masters, covers, and KDP listing files consistent with approved manuscript changes. Do not overwrite archival copies or unrelated working-tree edits. Check `git status` before and after work so generated artifacts and unrelated project changes remain identifiable.
