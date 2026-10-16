# Handover

Several agents edit this repository at once. Pull `origin/main` before you start. Run `git status` from `D:\My Books for Amazon`, not from a book folder. A status in the wrong folder has reported a clean tree that was not clean.

If a book’s own note disagrees with this file, the book’s note wins inside that book. If a manuscript file disagrees with a status log, the manuscript wins.

Do not commit another session’s `.docx`. Do not commit `bak\` snapshots, audit scripts, or `relativistic-site\`.

## Where the live notes are

- *Forbidden Offspring* (pen name Genevieve Crisp; new fiction, 12 Oct 2026): `Forbidden_Offspring/notes/HANDOVER.md`, with `Forbidden_Offspring/CLAUDE.md` and `Forbidden_Offspring/AGENTS.md` as pointers for Claude, Codex, Grok and any other assistant. Read it before touching that folder. The manuscript there is generated from `drafts/` by `build_manuscript.py`; edit the drafts, not the manuscript. Reality rule: nothing public before 2029 may contradict real history.
- Look First, *The Universe Has No Now*: `Look First - SERIES/notes/HANDOVER.md`. Book 1 chapters 31 and 32 are full lessons again. The sequel keeps the same subjects as its chapters 25 and 26. There is no Book 3.
- Look First, *A Trip Is Not a New Life*: `Look First - SERIES/A Trip Is Not a New Life - Manuscript/00_Status.md`. Do not restore the deleted Series Plan. Do not renumber the appendix. Popular chapters keep “a landing attempt in the 2030s.”
- Lolly Wren: `Lolly Wren's Curious Science Adventures - SERIES/HANDOVER.md`, plus each book’s manuscript guide.
- Math, Actually (formerly The Mathematics Tower): `Math, Actually - SERIES/notes/CLAUDE.md` (moved up from `Math for HS and College/` on 1 Oct 2026, renamed 2 Oct 2026; the 50 topic outlines are in `Math, Actually - SERIES/planning/`). Floor 6 is trigonometry. Floor 10 is limits. Floor 11 is the derivative.
- *The Dolphins' View of History*: `The Dolphins' View of History/notes/CLAUDE.md`. The folder was `History/` until 1 Oct 2026; it was renamed with `git mv` and holds only this book.
- YouTube companion: `Your First YouTube Channel That Rocks/notes/CLAUDE.md` (renamed from …That Sells and refocused on channel monetization, 2026-10-02). Fifteen chapters. The order is `build_docx.py`. The click chapter is chapter 2.

## Already merged on main

Pull requests #40, #43, and #44 are merged.

- #40 is the Lolly review, not Look First. The reviewed Book 2 draft is the committed file. The old How to Publish folder stays deleted.
- #43 did not replace the RIB manuscript with that branch’s regenerated text. The two sentence fixes on main are “the strange aircraft clock” and “dropped his eyes to himself.” Lesson 6 still points at chapter 7, because that is the chapter the singularities lesson belongs to.
- #44’s syllabus order, the lesson 7 title “Why SR and GR Don’t Fight,” and the five-chair sitting room are on main. The character bible still does not name Julian Barbour as the character’s real name.

## Still being edited on this machine

Leave these for the session that has them open. They are not the shared copy until that session commits them.

**Owner change, 1 Oct 2026, 16:30 PT.** The earlier sessions on RIB Book 1, Protocol Flamingo and the Mathematics Tower are dormant. One session now owns all three books: RIB Book 1 (manuscript, Kindle file, rebuild script, KDP files), Protocol Flamingo (`Protocol_Flamingo_Rev2.docx` and its notes), and the Mathematics Tower volume files. Do not edit them from another session. That session does no git operations; Lothar syncs separately. Backups of every file it changes are in `C:\Users\lomus\OneDrive\My Books for Amazon - session backups\2026-10-01 RIB-Flamingo-Tower\` (Tower backups also go in its `bak\Archive - not for publication` folder).

**Results, 1 Oct 2026, 17:00 PT** (same session; still no git, so these files are changed on disk and uncommitted):
- RIB Book 1: 63,090 → 64,082 words. Chapter 13 rewritten, about 18 broken "Then at…" fragments fixed, `rebuild_kindle.py` now emits real headings, page breaks and a linked TOC, and the Kindle docx is rebuilt. The KDP metadata, checklist and description are finished except the author name and launch date. Details: `_BOOK_SUMMARY.md`, last section.
- Protocol Flamingo: 26,460 → 26,647 words. Continuity, chronology and fact fixes. Details: `Protocol Flamingo/_STATUS.md`.
- Mathematics Tower Volume 2: 175,873 → 178,054 words. Floor 15 on-ramps and a Helmholtz-uniqueness fix in Room 15.7. Details: the Tower's `CLAUDE.md`, section 6.
- Mathematics Tower, second pass, all four volumes (evening, 1 Oct 2026): introductions written for the 14 coldest-opening rooms (3.2, 3.3, 3.7, 6.3, 8.2, 17.1, 17.4, 20.7, 27.4, 27.5, 27.6, 39.2, 42.2, 43.4), plus five accuracy fixes. V1 168,063, V2 179,462, V3 190,831, V4 173,906 words. Backups: `My Books for Amazon - session backups\2026-10-01 Tower pass 2\`. Details: the Tower's `CLAUDE.md`, section 7.
- Mathematics Tower, third pass, all four volumes (late evening, 1 Oct 2026): openings for 12 more rooms (8.3, 11.2, 17.2, 18.3, 25.2, 27.2, 27.3, 39.5, 45.2, 47.2, 48.4, 48.6), accuracy fixes in 25.2, 27.2, 27.3, 39.5, 47.2, 48.4 and 48.6, and Floors 20–21 maths notation converted to typographic form (matrices as [1 2; 3 4]; no Word equations). V1 168,622, V2 180,834, V3 191,501, V4 175,740 words. Backups: `My Books for Amazon - session backups\2026-10-01 Tower pass 3\`. Details: the Tower's `CLAUDE.md`, section 8.
- Mathematics Tower, fourth pass, all four volumes (night, 1 Oct 2026): openings for 12 more rooms (2.8, 7.7, 13.5, 16.4, 18.4, 24.2, 30.4, 30.8, 36.8, 42.7, 48.2, 50.6), accuracy fixes in 13.5, 16.4, 24.2, 30.4, 30.8, 36.8, 42.7 and 50.6, and the rest of V2's notation: Floors 20–21 end matter (missed in pass 3) plus the [[ ]] matrices in 17.3 and Floor 22; V2 has no [[ left. V1 169,209, V2 182,110, V3 192,459, V4 176,544 words. Backups: `My Books for Amazon - session backups\2026-10-01 Tower pass 4\`. Details: the Tower's `CLAUDE.md`, section 9.
- Mathematics Tower, notation sweep, all four volumes (night, 1 Oct 2026): one typed notation across every section ([1 2; 3 4] matrices, Unicode scripts, bracket limits such as ∫[0, π] and lim[x→0], exp(…) in V2–V4, ≥ ≤ ≠, ∗ for convolution); no [[, _{, >= or <= left. About 335 ^ and 915 _ remain where Unicode has no glyph (fractional exponents, f_y, log_b, capital subscripts). V1 169,228, V2 182,245, V3 192,678, V4 176,600 words. Backups: `My Books for Amazon - session backups\2026-10-01 Tower notation sweep\`. Details: the Tower's `CLAUDE.md`, section 10.

- The Relativistic Investigation Bureau Book 1 manuscript, Kindle file, and rebuild script. Owned by the session above.
- Protocol Flamingo (`Protocol_Flamingo_Rev2.docx`, `KDP_LISTING.md`, `notes/_STATUS.md`). **Owner change, 1 Oct 2026, 20:15 PT:** the Protocol / Flamingo / Dolphins session now owns Protocol Flamingo, replacing the session above for this book only, and keeps it synced with git (normal commit and push; no force). Other sessions: do not edit it.
- The Mathematics Tower volume files. Owned by the session above.
- The Lolly Book 2 draft `.docx`. Not owned by that session.
- QED, EE, Physics, RIB Book 2 and Lolly Book 2 are being edited by other workers.
**12 Oct 2026, Wee Scallywag session:** The Wee Scallywag and the Gentle Elf (The Step Stories, Book 1) is now by Anneliese Tauber, the same pen name as Bavarian Cooking. Her Also-by page lists only her books. This session added an "Also by Anneliese Tauber" page to the Scallywag docx that names Bavarian Cooking Made Simple. Whoever owns Bavarian Cooking: please add a matching "Also by Anneliese Tauber" page there listing The Wee Scallywag and the Gentle Elf (Book 1 of The Step Stories). That session has uncommitted changes in `Bavarian  Cooking\`, so this session did not touch that folder. EPUBs are now allowed in the repo (`.gitignore` changed 11 Oct 2026); docx is the working master, EPUB is the upload file.

**13 Oct 2026, Step Stories handover:** The Step Stories (Anneliese Tauber; Books 1 to 3 built, Book 4 planned) have a full handover for Claude, Codex and Grok Bot in `notes/STEP_STORIES_HANDOVER.md`: files and versions, content rules (American edition, ages, Scally's scam rhyme, safety teaching, no copying from Lindgren, Pumuckl or Seuss), build and Kindle Previewer commands, the picture pipeline, git rules, open decisions and to-do list. Books are in `The_Wee_Scallywag_and_the_Gentle_Elf`, `Scally_and_the_Sleepless_Stream` and `Scally_and_the_Hill_with_the_Hanging_Socks`. Do not edit them without reading that file.

**15 Oct 2026, RIB sync:** The Relativistic Investigation Bureau folder on `main` now contains tracked local RIB files plus GitHub-only Book 1 REV17 assets. Earlier GitHub copies with same-name conflicts are preserved under `The Relativistic Investigation Bureau - SERIES/bak/github-pre-sync-2026-10-15/`. Current RIB guidance is in that folder's `AGENTS.md` and `notes/NEXT_BOOK_HANDOFF.md`: Book 1 REV17 candidate, Book 2 REV05 working pair; REV14 and REV04 remain release masters. Keep archived files as reference, not active working copies.
**15 Oct 2026, Holistic Brain Farts:** Retired as a separate active book because the user has dedicated books for its material. The full 17-file PC copy is archived at `SCIENCE  Series\Science Sparks\bak\Lothar's Holistic Brain Farts - 2026-10-15\`. Do not restore or continue the separate book unless asked. Its former GitHub files were removed from `main` in a cleanup PR; Git history retains the previous tracked version. The backup is intentionally local and must not be committed.

**16 Oct 2026, reconciliation resumed:** Filesystem access is enabled. The shared checkout is `pc-checkout-cleanup-2026-10-13`, HEAD `0d423f69`, with 1,271 changed/untracked entries. After fetching, `origin/main` is at `9ed7e1be`; the shared branch differs by 140 local and 576 remote commits. Do not merge that branch wholesale or reset the shared checkout. A clean per-task worktree is at `C:\Temp\book-reconciliation-audit-20261016`, branch `codex/book-reconciliation-audit-20261016`, based on `origin/main`.

The largest concrete path change found so far is Look First: 194 files tracked at `NOVELS\Look First - SERIES` are now present at `SCIENCE  Series\Look First - SERIES`; direct blob comparison finds 138 unchanged and 56 changed. This is a relocation mixed with content edits, not a simple rename. Its existing status/handover notes are stale about the path and do not yet establish that all 56 differences are intended. Do not stage or move this series until those differences are reconciled against its current manuscript/status and any candidate branches.

Current status work is read-only except this handover note and the earlier Poetry book-local note. RIB Book 2 version cleanup was recorded and committed locally as `82d1065` in the nested RIB repository, but its remote URL is invalid; do not push. Poetry REV02 is active; the Word file remains locked, 16 files still match the pushed branch in the latest comparison, and branch content still needs review against `notes/LOTHAR_RULES.md` before merge. The earlier root-level 1,271-entry inventory remains unreconciled. Continue by comparing each book’s handoff/current master to the matching local branch/worktree, then reconcile one book at a time in this clean worktree. Never include `bak\` snapshots or another book’s files in a commit.

**Discovery, 16 Oct 2026:** `.codex-worktrees\` inside the shared checkout is not just 27 small status entries: it contains 28 full nested worktree trees, approximately 94,102 files / 14.3 GB total. These are likely why Git reports only one untracked directory entry per nested worktree; the nested `.git` files stop normal recursive status. Do not delete them or move them as ordinary folders. First match every directory to `git worktree list`, inspect its branch and dirty state, then use `git worktree move` or archive through Codex only when its owner/state is confirmed. Several names correspond to recent Book 3/6/7/9, QED, Physics, Lolly, Bavarian Cooking and Auswandern work, so their content may be current work, not old backups.

The 28 nested worktrees have all been matched to Git's registered worktree list. Status audit: 26 are clean; two carry uncommitted changes and must be preserved exactly—`auswandern-rev118` (4 changed files) and `qed-v2-current-20261015` / branch `codex/qed-v2-status-20261016` (110 changed files). Their tracked branches/commits remain in the shared Git repository. To remove the nested-worktree clutter safely, move all 28 with `git worktree move` to `D:\Offload\.codex\worktrees\repo-reconciliation-2026-10-16\<name>`; do not delete them or discard their dirty files. Recheck each status after moving.


**16 Oct 2026, worktree clutter mitigation:** All 28 nested paths were confirmed as registered worktrees. A Git move attempt on the first worktree was denied by the filesystem, so no worktree was moved. Instead, `.codex-worktrees/` was added to the shared checkout's local `.git/info/exclude`; this reduced its visible status entries from 1,271 to 1,244 without changing the nested worktrees or their individual status. The empty destination directory created during the failed move attempt remains at `D:\Offload\.codex\worktrees\repo-reconciliation-2026-10-16`; no files were placed there. Continue with one-book content reconciliation; do not treat the local exclude as a version cleanup or commit.

**16 Oct 2026, branch state check:** Compared each nested worktree branch with `origin/main`. Of the 28 worktrees, 19 clean branches have zero commits unique to them (their commit history is already contained in `origin/main`), seven clean branches have one or more unique commits, and the two dirty worktrees are not ahead by commits. The two dirty ones remain the Auswandern REV118 working tree and QED Volume 2 current tree noted above. Main-checkout status is now 1,244 after the local exclude.

**Digital Twin duplication found:** `NOVELS\Brave New Times\` is a separate nested Git repository (`Brave-New-Times.git`) containing 3,348 files / about 459 MB. Its Book 1 folder contains `.claude\worktrees\twin-status-594e8a`, a full 3,048-file repository worktree that includes other books. This explains why an “AI fork” can appear to contain the whole collection. It is a nested repository/worktree, not a Book 1 version; do not archive it into a book's `bak\` or remove it as a duplicate without reconciling its unique Book 2–7 material.

Open PR #173 (`claude/twin-status-594e8a`) is a separate main-repository change to `The Digital Twin` (59 files, about 10,241 insertions). It is still open and is not the same path/repository as `NOVELS\Brave New Times\`; keep them distinct during reconciliation. No PR was merged or closed in this audit.

**16 Oct 2026, Digital Twin source comparison:** The tracked main-checkout path `NOVELS\The Digital  Twin\` has 65 deleted files. The parallel nested-repository location `NOVELS\Brave New Times\Book 1 - The Digital Twin\` has only 2 byte-identical counterparts, 41 changed chapter/series files, and 22 missing prior files. The missing set includes source/blueprint files and captured work logs; preserve them. These are not safe to treat as one clean rename. The book's own nested repo and open PR #173 are separate candidate histories; compare their status/handoff and exact chapter files before choosing a master. Do not stage either copy as a wholesale replacement.

**16 Oct 2026, Brave New Times nested repository audit:** `NOVELS\Brave New Times\` is an independent Git repo on `main`, locally one commit ahead and four behind its own `origin/main`. Its Book 1 status still declares REV5 as the master, but the nested repo has 38 modified tracked Book 1 files, two deleted tracked files, and untracked REV5 EPUB/DOCX, cover options, build scripts and the Book 2 head-start files. Treat this as unfinished local Book 1/Book 2 work; preserve it and do not push the nested branch until the status, missing REV4 pair, and complete untracked list are reconciled. Its embedded `.claude\worktrees\twin-status-594e8a` alone accounts for 3,035 untracked entries in the nested repo status and contains a copy of the wider book repository. This is the literal source of the “all books in that fork” appearance. PR #173 remains open as a separate candidate for the same novel; compare its chapter text to the nested repo before choosing a master.


## Auswandern worktree update — 2026-10-16
The user reports checking current `origin/main` in an isolated worktree: the book already has a newer committed REV128 EPUB; an earlier EPUB generated from REV115 was not committed or pushed over it; there was no new book-only change to merge. The latest `main` was fetched and the clean worktree archived; no files were committed, pushed, or merged. This update refers to that isolated clean worktree and does not by itself resolve the separate registered dirty checkout `D:/My Books for Amazon/.codex-worktrees/auswandern-rev118`, whose status still shows four modified files pending owner review.



## Full dirty-worktree sweep — 2026-10-16
Ran `git worktree list --porcelain` and checked each existing registered checkout with `git status --porcelain=v1 --untracked-files=normal`. The following are dirty; counts are status entries, so one untracked directory can contain many files:

- Main shared checkout `C:/Users/lomus/git-dirs/My-Books-for-Amazon.git`: 660 entries.
- `C:/Temp/book-reconciliation-audit-20261016`: 1 modified handover file.
- `C:/Users/lomus/AppData/Local/Temp/bav-main-wt-16499`: 1,030 entries.
- `C:/Users/lomus/AppData/Local/Temp/ee-series-readiness-current-20261013`: 8.
- `C:/Users/lomus/AppData/Local/Temp/ee35/wt`: 1; `.../grokgrav/br-wt9`: 1.
- `C:/Users/lomus/AppData/Local/Temp/grokgrav/main-wt`: 17; `main-wt7`: 212; `main-wt8`: 213; `main-wt9`: 208.
- `C:/Users/lomus/AppData/Local/Temp/hc-rev2`: 2; `lolly1-rev2`: 1.
- `C:/Users/lomus/git-dirs/wt-scallywag`: 4; `wt-sleepless`: 1.
- `C:/Users/lomus/tmp-rules-wt`: 3,355 entries, primarily mass deletions; do not stage or clean without explicit review.
- `C:/Users/lomus/wt-hc13`: 1; `wt-hc8`: 56; `wt-hc9`: 1.
- `D:/My Books for Amazon/.claude/worktrees/youthful-wilson-76f830`: 3,703 entries, extensive deletions and modifications; do not stage or clean without review.
- `D:/My Books for Amazon/.codex-worktrees/auswandern-rev118`: 4 modified files. User separately reports REV115 EPUB work was superseded by the already committed REV128 EPUB on origin/main, and the clean isolated worktree was archived. This report does not identify these four changes, so keep them pending review.
- `D:/My Books for Amazon/.codex-worktrees/qed-v2-current-20261015`: 110 entries.
- `D:/Offload/.codex/worktrees/book4-critical-revision-20261015/My Books for Amazon`: 1 untracked review note.
- `D:/Offload/.codex/worktrees/digital-twin-paths/My Books for Amazon`: 56.
- `D:/Offload/.codex/worktrees/physics-vol2-current-pass/My Books for Amazon`: 92.
- `D:/Offload/.codex/worktrees/protocol-flamingo-version-cleanup/My Books for Amazon`: 1 untracked pacing-readthrough directory.
- `D:/Offload/.codex/worktrees/science-sparks-consolidation/My Books for Amazon`: 1 untracked build directory.
- `D:/Offload/.codex/worktrees/universe-latest-fix-audit/My Books for Amazon`: 5 (REV19 work and REV18 removal).
- `D:/Offload/.codex/worktrees/will-legacy-reconcile/My Books for Amazon`: 1 untracked output directory.
- `D:/Offload/.codex/worktrees/youtube-rev26-description-guidance/My Books for Amazon`: 1 untracked source document.
- Separate nested repository `D:/My Books for Amazon/NOVELS/Brave New Times`, branch main: 38 modified, 2 deleted, 11 untracked path entries; includes a nested Claude worktree.
- Registered RIB Book 1 review path `D:/My Books for Amazon - RIB Book 1 review` is marked prunable because its Git directory points to a missing location; status unavailable.

No entries from this sweep were staged, committed, pushed, merged, cleaned, deleted, or moved. Earlier commit-ahead inventory is distinct and must be reviewed book-by-book before cherry-picking or merging. This note is an inventory, not an ownership determination.



## Branches with commits ahead of fetched origin/main — 2026-10-16
Ran `git rev-list --left-right --count origin/main...HEAD` for registered worktrees. This compares commit ancestry, not book content or whether a PR is merged. Main shared checkout is 140 commits ahead / 576 behind and is not a safe whole-branch push/merge candidate. Other ahead worktrees:

- 1 ahead / 39 behind — `codex/ilwm-own-edition-20261016`.
- 77 ahead / 576 behind — detached `C:/Users/lomus/AppData/Local/Temp/ee35/wt`.
- 24 ahead / 576 behind — detached `C:/Users/lomus/AppData/Local/Temp/grokgrav/br-wt9`.
- 32 ahead / 576 behind — detached `C:/Users/lomus/AppData/Local/Temp/qa1wt`.
- 3 ahead / 30 behind — Auswandern literary pass branch `auswandern-rev129-main-sync-20261016`; user reports the clean isolated worktree has no book-only change to merge because committed REV128 supersedes the earlier REV115 EPUB.
- 1 ahead / 260 behind — Bavarian Cooking reader polish.
- 6 ahead / 95 behind — Book 9 critical revision.
- 1 ahead / 239 behind — EE Book 4 gatedriver/critical reader branch.
- 1 ahead / 39 behind — Giving Birth REV04.
- 1 ahead / 317 behind — Kindle literary review.
- 1 ahead / 158 behind — Physics Volume 1 current.
- 1 ahead / 164 behind — book-location index.
- 1 ahead / 38 behind — Protocol Flamingo REV11 publish.
- 138 ahead / 576 behind — Protocol Flamingo version cleanup.
- 121 ahead / 576 behind — Universe reconcile audit.
- 139 ahead / 576 behind — detached YouTube REV26 description guidance.
- 1 ahead / 20 behind — YouTube REV26 mainline.

Large ahead counts against origin/main often indicate these worktrees are based on a different/stale history; they do not equal that many new book edits and are not approval to push. Before integration, compare each candidate's book-only diff, release/status handover, and remote PR state against current main. No branches were pushed or merged as part of this inventory.



## Review of small ahead branches and live PRs — 2026-10-16
Inspected the commit(s) ahead of origin/main for 1-commit branches and queried GitHub PR state.

- Several commits have the same patch already in origin/main according to `git cherry`: Bavarian Cooking PR #146, Giving Birth PR #217, and YouTube REV26 PR #224 are merged; their local branch divergence is historical, not pending integration. Do not re-merge.
- The current Book 4 review branch commit is unique, but PR #157 remains OPEN while the later Book 4 REV6 release PR #218 is already MERGED. Treat #157 as potentially superseded; do not merge it without checking whether its edits are represented in REV6/current source. The registered worktree also has a separate untracked note outside the PR.
- Protocol Flamingo REV11 PR #223 is CLOSED and not merged. Its diff removes REV10 from active paths and adds REV11, but the associated worktree also has an untracked pacing read-through directory. Confirm current main's active master/status before any replacement PR; do not resurrect PR #223 blindly.
- The open book-location PR #200 changes three index/handover notes only, has no checks, and GitHub reports mergeable UNKNOWN. Review of its diff shows the path update still advertises stale editions (for example Auswandern REV115, Protocol Flamingo REV10, and QED Volume 2 without later release metadata) while moving folder names. It is not a reliable current-master index and should not be merged as-is.
- Unique small commits with no matching merged PR identified in this sweep: alternate edition of In Love with Murder (#branch codex/ilwm-own-edition-20261016), Physics Volume 1 masters (#branch codex/physics-v1-current-20261015), and the location-index branch noted above. These need book-status/current-file review before integration.

PR checks: #157 has validate-docx success but no review decision and mergeable UNKNOWN; #200 has no checks and mergeable UNKNOWN. No PR was merged/closed, branch pushed, or local file staged/committed by this review.



### Correction after inspecting the Book 4 REV6 record
The merged PR #218 revision record explicitly states the delivered 294-page REV6 is a different variant from a separate 295-page REV6 already on main, and that editorial reconciliation is still required before choosing an upload master. Therefore PR #157 cannot be considered superseded just because #218 merged. PR #157's source edits (chapters 1, 43, 51 plus diagram content) are not represented in the current source tree at origin/main; its DOCX and source changes require a three-way editorial comparison against both REV6 variants before deciding whether to integrate. Keep #157 open/pending review; do not close or merge it automatically.



### Protocol Flamingo follow-up
Checked current origin/main's tracked tree and status: REV11 DOCX and EPUB are already present, and the active status explicitly names them as the newest pair, with REV10 preserved in bak. PR #223 was closed without merge and is unnecessary to resurrect for the active release; the desired REV11 pair is already on main. Its old PR diff against the merge base is misleading because the history differs. The separate dirty version-cleanup worktree contains an untracked pacing read-through directory and must be retained for owner review, but it is not needed to publish REV11.



## Book 4 DOCX variant comparison — 2026-10-16
Used Pandoc to extract the three committed DOCX candidates from Git archives into `C:/Temp/book4-docx-compare-20261016`, then compared extracted plain-text lines. This was read-only; no repository manuscript was edited.

- Open PR #157's critical-reader manuscript (`RF_Microwave_and_Transceivers_Book4.docx`): 108,940 extracted words.
- Current origin/main `RF_Microwave_and_Transceivers_Book4_REV6.docx`: 111,234 extracted words.
- Current origin/main `RF_Microwave_and_Transceivers_Book4_REV6_reader_revision.docx`: 111,594 extracted words.
- Text comparison found 65 changed blocks between the PR #157 DOCX and the first REV6; 58 between the two REV6 DOCXs; and 87 between the PR #157 DOCX and the reader-revision REV6. Several are substantive: organization/movement structure, worked examples, cross-volume links, sources, and field-case notes. Extraction counts are approximate and include non-body DOCX text; they are not authoritative Word counts.

This confirms three genuinely distinct manuscripts. The PR #157 changes to sources (Chapter 1 opening, Chapter 43 class E example, Chapter 51 transmitter claim) should not be called superseded solely by filename/version: the newer REV6s differ extensively, and the two REV6 copies also differ. No master can be selected from version number alone. Reconcile chapter-by-chapter against the book owner/editor and verify which REV6 was delivered before promoting any one file to the active master. Keep both current REV6 variants and the open PR intact meanwhile.



## Book 9 critical-revision branch check — 2026-10-16
Branch `codex/book9-critical-revision-20261015` has six commits ahead and modifies the Book 9 source and exports through REV4. GitHub has no PR for this branch. Fetched origin/main already tracks `EE - SERIES/Test_and_Measurement_Instruments_Book9_REV5.docx` alongside the unversioned master and REV4. Thus this branch is historical input, not an unintegrated latest release; do not merge its REV4 export over the newer REV5. The shared checkout separately has uncommitted EE-series trees/files and must remain untouched until that owner reconciles them. No branch or source files changed in this check.



## Physics Volume 1 one-commit candidate check — 2026-10-16
Reviewed `codex/physics-v1-current-20261015` (one commit ahead of origin/main; no PR found). The commit changes only the two KDP DOCX masters and adds Prologue/Chapter 12 opener JPG+PNG assets. Pandoc extraction shows the paperback text has 37 changed blocks, mostly updated TOC page numbers plus small surrounding changes; Kindle extraction has three changed blocks, including opener alt-text and illustration inventory. Extracted word counts: paperback main 51,288 vs branch 51,228; Kindle main 51,269 vs branch 51,239. These small count differences and the absence of a book-level status/handover mean newest/approved release is not confirmed from the commit title alone. Keep the branch as a distinct candidate; do not merge or overwrite the active masters before the book owner confirms these Kindle corrections and checks the illustrations. No source files changed.



## In Love with Murder alternate-edition branch check — 2026-10-16
Reviewed one-commit branch `codex/ilwm-own-edition-20261016`. Its four additions are confined to `In Love with Murder, Actually/Alternate Derailed Edition/`: a Markdown manuscript, generated DOCX fallback, build script, and README. The README explicitly identifies this as an alternate standalone farce, says it is not the parent folder's current master, and says it was recovered from commit 469fbb8. Current origin/main separately contains the canonical parent-folder novel and no alternate-edition folder. No book status/handover under this folder and no PR are present. This is a distinct optional edition, not a newer replacement of the active master and not an old version to move into bak. Keep it isolated pending author's decision on whether to publish the alternate; no files were changed.



## Digital Twin open PR versus Brave New Times current book — 2026-10-16
Checked PR #173 in the parent repository and the independent `NOVELS/Brave New Times` repository. PR #173 is OPEN, mergeable UNKNOWN, with a successful validate-docx check; its latest diff adds the full chapter-source set and series/planning references under a separate legacy `The Digital Twin/` root plus score/rules/index edits. The nested Brave New Times Book 1 status instead names REV5 EPUB/DOCX (about 112,800 words, 35 chapters) as current, with REV4 and earlier in book-local bak. Its Git worktree has 53 porcelain status entries now (modified/deleted/untracked paths), including REV5 exports, review/build/cover files and the embedded `.claude/` worktree. These are separate repositories/histories; the PR source is not the nested repo's active REV5 release and must not replace it wholesale. PR source includes blueprint and session-recovery material that may be unique, so preserve it for source comparison rather than discarding/archiving. No PR merge/close or nested-repo cleanup performed.

The parent repo's PR #173 description says the purpose was to restore missing novel source and keep it synced; the embedded `.claude/worktrees/twin-status-594e8a` inside the nested repo is what makes that fork appear to contain every book. Do not confuse that embedded copy with the current REV5 book directory or with the parent repo PR.



## Shared-checkout uncommitted entries grouped by book — 2026-10-16
Grouped the current 660 porcelain entries in the shared checkout by path. Largest groups:

- `NOVELS/Look First - SERIES`: 194 entries, all deletions at this old location. A relocated `SCIENCE  Series/Look First - SERIES/` tree is untracked and contains a complete copy; earlier comparison found 138 matching/56 different tracked files, so this is not a safe blanket move.
- `EE, Actually  Series/chapters`: 173 entries (166 modifications, 7 untracked groups); plus 51 more entries across root-level export DOCX/EPUB and notes. This is a multi-book series-wide source/export update, not a single-book delta.
- `The Dolphins' View of History/chapters`: 122 entries (75 deletions, 26 modifications, 21 untracked groups); the new REV4 DOCX and chapters are mixed into this area. Requires full release/version review.
- `NOVELS/The Digital  Twin`: 65 tracked deletions; relocated nested Book 1 files and the separate Brave New Times repo exist elsewhere. Prior comparison found substantial mismatch, so do not restore/delete wholesale.
- `SCIENCE  Series/Science Sparks`: 18 entries (including a REV5 candidate).
- `NOVELS/Lolly Wren's Curious Science Adventures - SERIES`: 5; `HOW TO  Series/Your First YouTube Channel That Rocks`: 4; Bavarian Cooking: 2.
- Remaining status entries include direct book exports, series metadata, and added relocated directories. Several root-level REV files may overlap with material already present on origin/main or in book worktrees; status alone cannot decide which copy is newest.

The old-location deletions plus untracked relocated trees explain much of the shared checkout's apparent churn. Do not commit the whole checkout: it mixes at least Look First, the Digital Twin, EE Books 1–9, Dolphins, Science Sparks, Poetry and other books. No moves or staging were made.



## Look First relocation and book-level handovers — 2026-10-16
Read `SCIENCE  Series/Look First - SERIES/notes/HANDOVER.md` and each volume's status before deciding its current file. Book 1 (*The Universe Has No Now*) status names `export/The_Universe_Has_No_Now.docx` as KDP ingest, 112,883-word stamp (1 Oct), and explicitly says docx only/no EPUB. Book 2 (*A Trip Is Not a New Life*) status names `A Trip Is Not a New Life - Kindle.docx` as its 6x9 Kindle file; the status calls the 46-chapter combined manuscript the current book, with source sections in the same folder. The logs date from 1–3 Oct and do not establish which of the later on-disk path copies is authoritative.

The series handover explicitly scopes itself to Book 1 and says leave the sequel, leave `bak/`, unless the author asks for that book; Book 2's separate status also treats it as a distinct current manuscript. Do not move or archive either book's files under the series-level handover alone. The shared checkout has 194 deletions from old `NOVELS/Look First - SERIES` plus a full new `SCIENCE  Series/Look First - SERIES/` tree; 138 old/new files are byte-identical and 56 differ. This combines relocation and content edits, so resolve ownership/current version for each volume before any move. No Look First file changed in this audit.



## Dolphins release reconciliation — 2026-10-16
Fetched `origin/main` contains `The Dolphins' View of History - REV4.docx`, REV4 working Markdown, image set, review, and current status. The current `notes/_STATUS.md` declares REV4 the master; the 16 Oct follow-up review and rendering checks are recorded. In the dirty shared checkout, I hash-compared every modified/untracked file against origin/main: 54 files matched byte-for-byte; the 19 untracked REV4 image files also all matched. The other 76 status entries are deletions of old REV2/legacy chapter DOCX/Markdown paths that are absent from origin/main. Therefore the shared checkout's apparent 131-entry Dolphins change set is a stale-checkout mirror of already committed REV4 plus old-path removals, not an uncommitted newer revision to push. Preserve its old files through the existing book bak/record where present; do not stage this old checkout's whole Dolphins directory. The current remote master is already clear; no file changes made.


## EE series fork-copy spot check — 2026-10-16
Read the copied series' `notes/AGENTS.md` and the Book 5/6/8/9 and Book 4 review notes. Root DOCX files are described as authoritative masters in this copy; chapters are mirrors and `bak/` is retained history. The copied tree contains all nine books and 50+ root DOCX editions, consistent with the concern that a full-series copy was embedded in the AI fork.

Compared selected local root masters to `origin/main:EE - SERIES/` using Git blob hashes. Book 6 REV3 (`984c3282`), Book 8 REV4 (`b4a89a06`), and Book 9 REV5 (`d9c367d6`) are byte-identical to origin/main. They are copies, not fresh pending changes. Book 5 REV3 (`cc7b6f5a`) is present locally but no matching REV3 path exists on origin/main; the dated REV3 note describes it as based on REV2 and reports visual review, while the unnumbered Book 5 master remains unchanged. Treat REV3 as a unique candidate requiring book-specific reconciliation; do not overwrite the unnumbered master or move it to bak based on filename ordering alone.

Book 4 REV6 (`2c291528`) differs from origin/main REV6 (`9188573b`); origin/main also has a separate `REV6_reader_revision` edition. Existing Book 4 review notes say these are different editions (294 vs 295 pages) and require editorial reconciliation before upload. Keep all variants pending that reconciliation. These copied paths appear as untracked in the stale shared checkout, so no whole-series staging is safe. No book content, worktree, branch, PR, or release file changed during this spot check.

## Science Sparks REV5 worktree-copy check — 2026-10-16
The shared checkout has 18 status entries under `SCIENCE  Series/Science Sparks`: the previously tracked `Science Sparks.docx` and base KDP description are deleted at that old path; five existing chapter sources and `scripts/build_almanac.py` are modified; and a REV5 DOCX, REV5 KDP description, five new chapter Markdown files, figures, `notes/00_STATUS.md`, and `notes/CRITICAL_REVIEW_REV5.md` are untracked. The organized folder `D:\My Books for Amazon\SCIENCE  Series\Science Sparks` contains the REV5 outputs and the `bak/2026-10-16-rev5` snapshot. The current status note names REV5 as the active review candidate and says it is not publication-final: full visual page QA, additional diagrams, and other review gates remain. EPUB is explicitly deferred until REV5 settles.

The existing origin/main history has only the initial series-folder organization commit for this path; it does not contain the REV5 status or REV5-named root exports. So this is genuine uncommitted REV5 source/build work, not a byte-identical mirror of origin/main. Preserve the full working set and its existing bak snapshot. Do not move the old DOCX/description to bak or stage a broad tree: the deletion, source edits, and new files form one connected revision candidate. No files were changed or staged in the book folder.
