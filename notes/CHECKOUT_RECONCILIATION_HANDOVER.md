# Shared checkout reconciliation handover

Updated 16 Oct 2026, America/Los_Angeles.

## Current snapshot

`D:\My Books for Amazon` is one Git repository. Its checkout is on `pc-checkout-cleanup-2026-10-13`, with `origin/main` at `3d8fdc05`. The expanded `git status --porcelain --untracked-files=all` count is **439 entries**: 87 modified, 8 deleted, and 344 untracked. The checkout is 142 commits ahead and 595 behind `origin/main`. The older report of 1,288 entries is stale. The 29-row increase since the last snapshot is the Book 5 working copy being brought up to date with `main` inside the old path alias; it is not a new independent draft.

The local checkout uses older path prefixes, including `KIDS  books` (two spaces), while current `main` has moved many book folders to the repository root. These are path aliases inside the same repository, not separate repositories. Do not reset, clean, or merge the old branch wholesale: preserve and classify its commits and files book by book.

The first-pass map of the 344 untracked files found 267 content matches to a unique current-main path (including line-ending-normalized text), 4 files with a unique path match but different content, 11 with no path candidate, and 62 ambiguous suffix matches. Treat the ambiguous group as unresolved; a matching basename is not enough to discard or promote a file.

## Completed

- PRs #230 and #231 promoted Step Stories Books 1 v22 and 3 v9. Book 2 v17 is also on `main`.
- PR #232 fixed the Book 3 picture builder. It now retains both illustrations at their shared paragraph anchor, chooses the highest numeric story version, and builds v10 with 119 story images plus the cover.
- PR #233 added the as-built Book 3 outline v2 and corrected the listing to about 23,600 words.
- The D: Book 3 copy under `KIDS  books\Scally_and_the_Hill_with_the_Hanging_Socks` was synced to v10. All 145 active files now match current `main`; its 21 status rows are the old path alias, current files missing from the old branch's index, and v8 files moved into `bak`. The v8/v9 deliverables, prior local text/metadata/build files, 11 changed picture candidates, and duplicate nested fonts are preserved under that book's `bak\2026-10-16 root-sync after v10\`.
- Book 2 is content-aligned with current `main`: all 104 active files in the D: `KIDS  books\Scally_and_the_Sleepless_Stream` folder match the root-level Book 2 paths in `origin/main` (exact bytes or line-ending-normalized text). Its v15 DOCX/EPUB are safely in `bak\2026-10-16_v17_sync\`. The bucket's 105 status rows are explained by the old path alias, current files appearing untracked there, and the two v15 tracked-path deletions; no local content needed promotion or copying.
- The Department of Historical Corrections is also content-aligned: all 85 active files in the D: `NOVELS\The Department of Historical Corrections` folder match current `main`. Its `bak\2026-10-16 REV12`, `REV13`, and `REV14` folders preserve earlier revisions. No local content needed promotion or copying.
- The Dolphins' View of History manuscript is mostly aligned with current `main`: excluding `bak` and `node_modules`, the D: folder has 86 active files versus 88 in `main`; 77 match byte-for-byte and 5 text files match after line-ending/BOM normalization. There are no D-only active paths. Four local variants remain to review (`.gitignore`, `scripts/_generate.js`, `scripts/make_back_cover.py`, and `scripts/make_front_cover.py`); `main` has two additional files (a comedy-draft cover and its generator). The REV4 DOCX and chapter content are already on `main`. The D: book has extensive dated backups, so do not overwrite the four local variants until their changes are reviewed and preserved.
- The EE series folder was renamed on `main` from the D: alias `EE, Actually  Series` to `EE - SERIES`. The D: Book 5 unnumbered DOCX and its 62-file tagged-text mirror were backed up at `bak\EE5\2026-10-16 pre-origin-main-sync\` and synced byte-for-byte to current `main`. The backup also holds a 62-file recovery copy of the main mirror from the safe copy operation.
- The local Book 5 REV3 DOCX and 62-file source mirror remain a newer, reviewed candidate, not the current master. Its unnumbered base predates current `main`: REV3 lacks three current-main paragraphs across Chapters 2 and 8. Its 28 changed text/source files and 34 shared figures are retained locally; do not promote REV3 until it is reconciled with the current master. The five untracked EE notes (Book 4 REV5/REV6, Book 5 REV2/REV3, and Book 6 critical review) also remain to classify. The Book 6 critical-review note already has a same-path counterpart on `main` with a difference; compare before replacing or adding either copy.

## Repository-boundary assessment

The shared repository increases the blast radius: `git status` and commits span unrelated titles, and a single broad commit could mix book work. It did not itself create the 410 status rows. The main source of confusion is that the D: checkout is on a heavily divergent branch (142 ahead and 593 behind current `main`), with historical path aliases and local files mixed together. A clean, series-level repository for each independent publishing workflow would make future status, review, and commits easier to isolate. Keep tightly related books and their shared assets/builders together (for example, the Step Stories books); keep genuinely shared author guidance in a small separate workspace or copy the relevant guidance into each series repo. Do not migrate until this reconciliation is complete and a path/history map is ready. Extract from a clean `main` snapshot with history-preserving path filters, verify each new repo, and retain the current shared repo as a read-only rollback archive until validation is complete.

## Next work

Triage the largest remaining path buckets in this order:

1. Reconcile the Book 5 REV3 candidate with current-main Chapters 2 and 8; classify the local Book 4/6 review notes against current revisions.
2. Review and preserve the four local Dolphins config/build-script variants; then finish its D: sync.
3. `POETRY/Limericks and Nonsense Rhymes` — 17.
4. `KIDS  books/The_Wee_Scallywag_and_the_Gentle_Elf` — 10.
5. `SCIENCE  Series/Science Sparks` — 7.

For each book, compare the local files against current `origin/main` in an isolated worktree. Preserve superseded or unique material in that book's own `bak\` before syncing its D: copy. Promote only reviewed changes through a normal commit, push and PR merge. After each batch, refresh this note with the new counts. Consider splitting repositories by series only after this reconciliation and a file/history map are complete.
