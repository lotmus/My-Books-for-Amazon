# Repository Guidelines

Read `notes/STEP_STORIES_HANDOVER.md` first: it holds the content rules, the build commands, the picture pipeline, the git rules and the open decisions for The Step Stories (children's books by Anneliese Tauber).

## Project Structure & Module Organization

The story master is `Step_Stories_Texts/Book1_Story_v*.txt`; the docx and EPUB in the folder root are deliverables; pictures are in `Step_Stories_Pics_Final/`; `build/` holds the Python build and picture scripts.

## Build, Test, and Development Commands

`cd build && python build_docx.py`, then pandoc for the EPUB as in `build/README.md`.

Convert new text to American spelling with `Scally_and_the_Sleepless_Stream/build/us_spelling.py`. After a build, check the EPUB with Kindle Previewer 3 (`Kindle Previewer 3.exe book.epub -convert -output <dir>`); errors and quality issues must both be 0.

## Coding Style & Naming Conventions

Python scripts, four-space indentation, UTF-8. File names carry the version (`..._v20.docx`); move older versions to `bak/` and rejected pictures there too (neither is committed). American spelling, no repeated sentences inside a book, only Scally and Hopsi have pointed ears, no PDFs, no Word tables, no floating images.

## Commit & Pull Request Guidelines

Use short imperative subjects that start with the book (for example, `Wee Scallywag: ...`). Work in a git worktree, `git fetch` and merge `origin/main` first, commit only this book's folder and the notes you touched, and push normally with `git push origin HEAD:main HEAD:scallywag HEAD:sleepless-stream`. Never force-push and never print or commit the xAI image key.
