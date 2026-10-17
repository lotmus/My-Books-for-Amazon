# Shared checkout reconciliation handover

Updated 16 Oct 2026, America/Los_Angeles.

## Current snapshot

`D:\My Books for Amazon` is one Git repository. Its checkout is on `pc-checkout-cleanup-2026-10-13`, with `origin/main` at `af4df10d`. The expanded `git status --porcelain --untracked-files=all` count is **410 entries**: 58 modified, 8 deleted, and 344 untracked. The checkout is 142 commits ahead and 587 behind `origin/main`. The older report of 1,288 entries is stale.

The local checkout uses older path prefixes, including `KIDS  books` (two spaces), while current `main` has moved many book folders to the repository root. These are path aliases inside the same repository, not separate repositories. Do not reset, clean, or merge the old branch wholesale: preserve and classify its commits and files book by book.

The first-pass map of the 344 untracked files found 267 content matches to a unique current-main path (including line-ending-normalized text), 4 files with a unique path match but different content, 11 with no path candidate, and 62 ambiguous suffix matches. Treat the ambiguous group as unresolved; a matching basename is not enough to discard or promote a file.

## Completed

- PRs #230 and #231 promoted Step Stories Books 1 v22 and 3 v9. Book 2 v17 is also on `main`.
- PR #232 fixed the Book 3 picture builder. It now retains both illustrations at their shared paragraph anchor, chooses the highest numeric story version, and builds v10 with 119 story images plus the cover.
- PR #233 added the as-built Book 3 outline v2 and corrected the listing to about 23,600 words.
- The D: Book 3 copy under `KIDS  books\Scally_and_the_Hill_with_the_Hanging_Socks` was synced to v10. Its v8/v9 deliverables, prior local text/metadata/build files, 11 changed picture candidates, and duplicate nested fonts were preserved under that book's `bak\2026-10-16 root-sync after v10\`. Its remaining 21 status rows are mostly the old path alias and the current v10 files.

## Next work

Triage the largest remaining path buckets in this order:

1. `KIDS  books/Scally_and_the_Sleepless_Stream` — 105 status rows.
2. `NOVELS/The Department of Historical Corrections` — 85.
3. `The Dolphins' View of History/chapters` — 65.
4. `EE, Actually  Series/chapters` — 62.
5. `KIDS  books/Scally_and_the_Hill_with_the_Hanging_Socks` — 21.

For each book, compare the local files against current `origin/main` in an isolated worktree. Preserve superseded or unique material in that book's own `bak\` before syncing its D: copy. Promote only reviewed changes through a normal commit, push and PR merge. After each batch, refresh this note with the new counts. Consider splitting repositories by series only after this reconciliation and a file/history map are complete.
