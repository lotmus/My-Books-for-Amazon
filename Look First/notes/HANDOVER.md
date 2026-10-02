# Handover — *The Universe Has No Now*

**Scope.** This note is the Look First series only, and this book only: *The Universe Has No Now*. Folder: `The Universe Has No Now - Manuscript`. Author: Lothar J. Musiol. 45 chapters, notes A0–A45. Shared rules for both books: `00_Series_Reference.md`.

The parent repo (`My Books for Amazon`) holds other series. They are not this job. Do not edit them from this handover.

Look First has a sequel, *A Trip Is Not a New Life*, in the folder next door. It is not this book. Leave it, and leave `bak\`, unless the author asks for that book.

Written 30 September 2026, against the files on disk.

The numbered part files in this manuscript are the text. If `00_Status.md` disagrees with a part file, the part file wins. If an older section of the status log disagrees with the current block at the top, the current block wins.

## Git

Repo root is `C:\Users\lomus\OneDrive\My Books for Amazon` (not the Look First folder). Git dir `C:\Users\lomus\git-dirs\My-Books-for-Amazon.git`. Remote `https://github.com/lotmus/My-Books-for-Amazon.git`, branch `book-2-lectures-after-qed`. Look First lives at `My Books for Amazon\Look First` (moved out of `Science Books` on 1 Oct 2026).

Other agents commit on `book-2-lectures-after-qed`, including books outside this series. Run `git status` from the repo root before assuming a file is clean or is yours. A status limited to the wrong path has reported a false clean tree.

**Standing rule (1 Oct 2026): keep GitHub synced with the PC. Commit and do a normal push after every piece of work.** Commit only your own paths (`git commit -- "Look First"`), because other workers stage files in the same index. Never force-push. If the push is rejected, fetch, `pull --rebase` your own commit, and push again. Never commit `.gitmodules`, `How  to  Pubish…`, `relativistic-site/`, or `~$` files. `bak/` is ignored at any depth.

PowerShell does not accept `&&`. Do not pass inline Python that contains a regex; write a `.py` file and run it. The console code page cannot print a curly apostrophe or Greek letters. That is the terminal, not a damaged file.

## This book — current

Chapters 31 and 32 are full lessons in `06_Part_Six_Getting_There.md` (headings at “31. Crews That Do Not Sleep” and “32. A Library of Earth”). Appendix A31 and A32 hold the numbers. Do not shorten them. Do not put back the sentence “The full classroom now lives in…”.

Stamp: **112,883** words in `export\WORD_COUNT.txt` (1 Oct 2026). Docx only; no EPUB is built.

KDP ingest is the docx:

- `export\The_Universe_Has_No_Now.docx`
- Rebuild from the manuscript folder: `python export\assemble_export.py` (docx only; `--with-epub` is ignored)
- Direct docx: `python Figures\build_docx.py "export\The_Universe_Has_No_Now.docx"`
- If that export path is locked, write a side file in `export\` and move it onto the canonical name.

Docx only, standing rule: no EPUB and no PDF. The old EPUB was moved to `bak\export\` on 1 Oct 2026. Ingest is the docx.

Headlines in `Figures\build_docx.py` are navy `0C2D5A`. Link blue stays the Word link color, with an underline. Do not set headlines back to `#0000FF`.

Photograph credits are on the copyright page in `00_Front_Matter.md` and in `KDP_Description.md`.

Kept on purpose:

- The loaf. It is the book’s picture, and it is in the glossary.
- Chapter 30 stays the long chapter. The feast and fake-cue stretch was already cut to a pointer at A30.
- A page break before each part, chapter, and appendix note.
- Standing rule from 25 Sep 2026: every term in the popular text was already built, is built where it is used, or is pointed forward with a chapter number.

Human steps still open: look at `export\cover_typographic.jpg` in the KDP cover tool, and a Kindle previewer pass.

The hostile-review canvas is a review sheet from before chapters 31 and 32 were restored. Its chapter-length chart is historical. Do not rebuild the book from it.

## Cast

`00_Series_Cast.md`, next to `00_Series_Reference.md`, is the shared household. Mara is this book’s woman with the pot holders and the sequel’s woman on Mars. Eli keeps this clock. He does not go. Priya and Rohan belong to the sequel. Do not invent a second Mara, and do not put the Moon classroom in this kitchen.

## Sequel — leave it

*A Trip Is Not a New Life* is the other Look First book. Its chapters 25 and 26 teach the crew and the library again. This book teaches them in chapters 31 and 32. Both stay. Do not cut this book’s chapters because an older line in the sequel’s status or outline called them bridges. Those lines were corrected on 30 Sep 2026. Do not edit the sequel as part of this job.

## Do not undo

- Restoring Book 1 chapters 31 and 32, and notes A31 and A32, as real lessons.
- Teaching e-folds as a factor of about 2.7, fifty to sixty times. Do not teach them as sixty doublings.
- The tilt `n_s ≈ 0.965` (Planck 2018 central value).
- Azotosomes marked cold. Titan’s lake on Arrhenius, not a ten-degree doubling.
- Heat death hot as the track the bombs picked, warm only in the details no one has photographed.
- Row (18) labeled a standing rule, not a formula. Numbered formulas are (1)–(17).
- Photograph credits on Book 1’s copyright page.
- Navy headlines in this book (`0C2D5A`).
