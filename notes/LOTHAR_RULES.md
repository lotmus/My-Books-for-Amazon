# Lothar's standing rules for every book

This is the handbook for any assistant working on Lothar J. Musiol's books, on any account. Read it before you edit. Prefer this file over memory, chat history, or an older book note when they disagree. Book-specific notes (each book's `notes/` or `CLAUDE.md`) still win for details that apply only inside that book. Canonical bio and Also-by text live in the sibling files named below; do not invent a second copy.

Repo root on the PC: `D:\My Books for Amazon`. Git directory: `C:\Users\lomus\git-dirs\My-Books-for-Amazon.git`. GitHub: `lotmus/My-Books-for-Amazon`.

---

## Identity

- Author name is always **Lothar J. Musiol** (with the J.).
- Household facts: Lothar has four children, a wife, and a grumpy Teacup Pomeranian named **Gucci**. When the published bio wording needs to change, edit `notes/ABOUT_THE_AUTHOR - canonical.md` first, then propagate.
- Pen-name rules:
  - **Kevin Drew Peters** alone (no real name anywhere on the book, listing, or Also-by): *How to Publish Your First Kindle Book* (also known under the older title *Your First Book That Sells*) and *Your First YouTube Channel That Rocks*. A Kevin Drew Peters Also-by page lists only Kevin Drew Peters books. Never put those titles on a Lothar J. Musiol Also-by page.
  - **Lothar J. Musiol writing as Spezala Genara Relavi (S.G.R.)**: The Relativistic Investigation Bureau books.
  - **Lothar J. Musiol writing as Quentin Edmund Darling (Q.E.D.)**: Lolly Wren's Curious Science Adventures books.
  - **Lothar J. Musiol writing as Romuald Livingston**: *In Love with Murder, Actually*.
  - **Lothar J. Musiol writing as George Herbert Fontaine**: *Protocol Flamingo*.
  - **Anneliese Tauber** (a Bavarian mother of four): *Bavarian Cooking Made Simple*. Never list it in Lothar's Also-by. It has no Also-by page of its own.
- Do not bring back retired titles or series names on any Also-by page. The retired list lives in `notes/ALSO_BY - canonical list.md`.

---

## Bio and Also-by

- There are two About the Author versions. Canonical text: `notes/ABOUT_THE_AUTHOR - canonical.md`. Use it exactly (italicize the two film titles in Version A).
  - **Version A** (with the *Love Actually* "Colin" line): British-English novels — RIB Books 1–2, Lolly Wren Books 1–2, *Protocol Flamingo*, *In Love with Murder, Actually*. Keep each book's own pen-name paragraph(s) first, then Version A.
  - **Version B** (without Colin): every other book under Lothar's name. Both versions mention Gucci.
  - **Never** put either version on the Kevin Drew Peters books, on Auswandern, or on Bavarian Cooking.
- Placement: replace an existing About the Author section; otherwise add one just before the Also-by page. If a book has no back matter, put About the Author at the end.
- Every book gets a nice, inviting review line and an Also-by page, except where Identity forbids it (Bavarian Cooking; Kevin Drew Peters books use only their own short list).
- Canonical Also-by list and order: `notes/ALSO_BY - canonical list.md`. Every Lothar-name book's Also-by page uses that list, leaves out the book itself, and keeps that book's own layout. Keep "Also in This Series" pages separate. Auswandern is listed under In German; its own docx has no Also-by page.

---

## Files and folders

- Deliverable format is **docx only**. Markdown working copies are fine. Never build, offer, or ship PDF or EPUB.
- Never delete anything. Move old files into the book's `bak\` subfolder, or into a dated folder under `D:\bak\`.
- Only the current master, its md working copy, and notes stay at the top of each book folder. Older versions go into that book's `bak\`.
- Do not commit `bak\` snapshots, audit scripts, or `relativistic-site\`.
- Stay inside the book folder you were asked to work on. If something outside it looks worth touching, say so and wait to be asked.
- If a book's own note disagrees with `notes/HANDOVER.md`, the book's note wins inside that book. If a manuscript file disagrees with a status log, the manuscript wins.
- Run `git status` from `D:\My Books for Amazon`, not from a book folder.

---

## Git

- After every piece of work: commit and do a **normal push**. Never force-push.
- Keep GitHub and the PC in sync.
- Before any git command: clear `GIT_DIR` and `GIT_WORK_TREE`, then check `git rev-parse --show-toplevel`. A global `core.worktree` once caused damage; do not rely on leftover environment variables.
- On this PC the usual setup is: work tree `D:\My Books for Amazon`, git dir `C:\Users\lomus\git-dirs\My-Books-for-Amazon.git`.
- Several agents may edit at once. Stage and commit only the files for the book you are working on. Re-read the file and the git log before writing; do not trust a status snapshot from the start of a conversation.
- Pull `origin/main` (or the branch you were told to use) before you start shared work. Do not commit another session's `.docx`.
- Heavy or parallel work: use a **temp git worktree**. Never `reset --hard` (or otherwise reset) the `D:\My Books for Amazon` checkout while other jobs may have uncommitted edits there; sync that checkout with a fast-forward only.

---

## Content

- Never write the name **Trump**. The topics are fine without the name (for example "the president", "Washington", "the US government"). Search for the name before every commit.
- How-to books use generic example people, not real names. Case studies that need a real, checkable source may name a channel or brand; lead with the channel brand where it differs from a person. Never use Lothar's own titles as examples inside a how-to book.
- Remove unverifiable facts without asking. Keep only claims checked against official or reliable sources (publisher pages, Crossref, Open Library, government statistics, the product's own policy pages). Never invent a source.
- Use concise wording with no content lost. Cut repetition and padding; do not cut teaching substance.
- In teaching books, exercises with worked solutions are the backbone and are **never cut**. Prefer "Try it now" plus graded Core / Extension / Challenge, each showing the usual mistake. Trim prose instead of trimming exercises.
- Never use cryptic abbreviations such as "MTW". Write full titles.
- The "Actually" books share formatting conventions (title page layout, series line, heading styles, linked contents, review line, About the Author, Also-by). Match the sibling volumes.
- Spelling: **American** for science and nonfiction; **British** for the British novels (RIB, Lolly Wren, Protocol Flamingo, In Love with Murder, Actually).
- Voice for the British novels: British deadpan, wry, not anarchic absurdism unless a book's own note asks for it.
- Math / teaching on-ramps: never define a thing before the reader has felt the need for it, and never use a symbol before the arithmetic has already made the point. Tone treats the reader as an intelligent adult; pace assumes nothing has been met before. Banned at a hinge: clearly, obviously, simply, just, of course, it is easy to see.
- Do not restore deleted series plans, retired folder names, or withdrawn Also-by pairings.

---

## Kindle and layout

- **Headings** (Lothar, 2026-10-11, applies to every book): bold, 16pt, dark-to-medium blue, centered, in a font that is Kindle-compatible and survives an EPUB import (Amazon Ember where already in use; otherwise a standard embedded font Word/KDP ships natively — Georgia, Bookerly, Caecilia, or similar; never a system font that gets substituted silently). Each chapter (and any other top-level heading: Prologue, Epilogue, appendices, Notes and Sources, Further Reading, Also-by) starts at the top of a fresh page — insert a page break before the heading, not just extra blank lines. Page setup should match a Kindle device's effective screen shape (portrait, no fixed print trim size) rather than a US Letter or A4 layout. This is a standing formatting rule for all 30+ books, not a one-off for any single title; apply it the next time a book's layout is touched rather than as its own dedicated pass across the whole catalog at once.
- Images inline only. No text boxes, no floating images.
- Photos about **440 px** wide, JPEG, with a gentle warm colour boost so dishes and subjects look inviting. Crop to the subject. Replace dull, blurry, or unappetising photos.
- Diagrams with small labels about **800 px**.
- Embedded front cover about **1000×1600** (separate KDP cover files may be larger, for example 1600×2560).
- Back covers are **text-only on a single colour**. No barcode on the ebook back cover art unless a print wrap needs it.
- Contents page: list and link everything (every appendix item, About the Author, Also-by). **No page numbers** on the contents page.
- Bibliographies and external sources use keyword hyperlinks with hidden URLs. In-text citations link to their bibliography entries.
- Keep files small (KDP delivery fee on the 70% royalty option). Target roughly 2–3 MB per ebook. See `notes/FILE_SIZES.md` for the current size table and shrink method.
- For Math and similar Word masters edited as zip/XML: preserve run structure and hyperlinks; verify `testzip()`, parse, and media counts after every write.

---

## Pictures and licences

- Replace weak pictures with better, legally licensed ones. One tool for that search is the MediaSearcher app at `D:\My_C#_Apps\MediaSearcher`.
- Record credits and licences for every photo. Put credits under the figure or on a credits page in the book (do not defer them only to an Amazon description).
- Avoid photoreal images that do not teach. Prefer a simple diagram or drawing when a photo is only decorative.
- Do not paste AI tool names into the reader's book as credits or as "written with" lines.

---

## Scoring

- Score strictly and critically. Track everything in `SCORES.md` at the repo root.
- Four angles for a general book: target reader, harsh critic, subject expert / fact-checker, Amazon market. Give each a score out of 10 and an issue list; put the overall score last; also give a sellability score out of 10.
- For science books the score areas are: physics (or subject) accuracy, exercises and solutions, clarity for non-physicists, structure and pacing, prose, pictures, sources and licences, Kindle formatting, KDP listing, and covers.
- Covers are judged from the files in the book folder. A file that exists only under `bak/` counts as draft.
- Status labels in `SCORES.md`: published = live on Amazon; ready = manuscript closed with an upload package or KDP description; draft = still being written or fixed.

---

## Working style

- Make fixes directly rather than leaving them for Lothar to remember.
- Give short, answer-first replies. Report results, not promises.
- When Lothar approves a wording change, put it in the manuscript in the same session.
- Prefer rewriting from verified facts over lightly editing another session's or another tool's prose, especially in how-to books that started from mixed source notes.

---


## Working efficiently (coach Lothar on this)

When you see Lothar falling into these patterns, remind him gently — once, briefly, without lecturing:

- **Batch asks.** Put several decisions or fixes in one message instead of a stream of small follow-ups. Each extra turn costs context and RAM.
- **Settle decisions first.** Pen names, taglines, cover style, and similar choices should be fixed before a job starts, not changed mid-job.
- **Rescore after a big pass.** Do a full critical rescore only after a substantial edit pass, not after every small tweak.
- **At most two heavy jobs at a time** on this low-RAM PC. Queue the rest.
- **Rely on this file.** Point at `notes/LOTHAR_RULES.md` instead of repeating standing rules in chat.
- **Ship before polishing.** Get books to *ready* and uploaded before chasing higher 9.x scores.

For assistants: do heavy or parallel work in temp worktrees, and never reset the `D:\My Books for Amazon` checkout while other jobs may have uncommitted edits there.

---
## Job management

Assistants follow this, and gently coach Lothar when the pattern slips.

- **At most two heavy book jobs at once** on LOTHAR-HP (low RAM). Queue everything else.
- When Lothar asks for **more than two heavy jobs at once**, hold the extras in the Job queue, tell him plainly what is queued, and start them as slots free up. (Lothar approved this rule.)
- Keep a short **Job queue** at the top of `SCORES.md` (book, task, status, who). Update it when a job starts, finishes, or is blocked.
- **Never run two jobs on the same book**, or on the same `SCORES.md` rows, at the same time.
- Each job works in its **own temp worktree**, commits in small batches, pushes normally, and **fast-forwards** the `D:\My Books for Amazon` checkout only — never resets it.
- Each job edits **only its own book** and **only its own SCORES row**.
- Give a job **one complete brief up front** (all fixes, decisions settled). Do not redirect it mid-run.
- **Finish and report one job** before starting the next on the same book.
- After a job, record the outcome in `SCORES.md` (score before and after, open items).
- Clean up temp worktrees and transfer folders afterwards by **moving them to `D:\bak`**, never deleting them.
- If a job stalls or the connection drops, **resume from its last pushed commit** instead of starting over.

---

## Compacting and saving usage

Keep chats and tokens cheap without losing the thread.

- When a chat gets long, **first save the current state** (job queue, open items, decisions) into `SCORES.md` and this rules file, **then** compact or start a fresh chat that begins by reading `notes/LOTHAR_RULES.md` and `SCORES.md`.
- Keep `SCORES.md` and this rules file **short**: move finished jobs and old notes to `notes/ARCHIVE.md`.
- After each job, move temp worktrees and transfer folders to `D:\bak`, never deleting them.
- **Read only the parts of files you need** instead of whole books when that is enough.
- **Reuse existing scripts** instead of rewriting them.
- Keep reports short: **results and open items only**.

---

## Published books

- Live on KDP and **do not edit unless asked**:
  - *Auswandern – Ab in die USA, Kanada, Australien oder Neuseeland?*
  - *How to Publish Your First Kindle Book* / *Your First Book That Sells* (REV41 pending re-upload)
  - *Your First YouTube Channel That Rocks* (REV22 pending re-upload)
- Pending re-uploads are still "published": do not open a rewrite; only apply the pending package if Lothar asks.

---

## Where else to look

| Need | File |
|---|---|
| About the Author text | `notes/ABOUT_THE_AUTHOR - canonical.md` |
| Also-by titles and order | `notes/ALSO_BY - canonical list.md` |
| Multi-agent ownership / do-not-touch | `notes/HANDOVER.md` |
| Kindle MB targets and shrink log | `notes/FILE_SIZES.md` |
| Scores, covers, release order | `SCORES.md` |
| Book-specific method | that book's `notes/` or `CLAUDE.md` |

If this handbook and a book note conflict on a global rule (pen names, Trump, docx-only, no force-push, scoring method), this handbook wins. If they conflict on a detail inside one book (chapter order, build script, local voice), the book note wins.
