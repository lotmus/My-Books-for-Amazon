# The Digital Twin: handover

Last reconciled: 15 October 2026 (after REV2).

## Current files
- Master docx: `The Digital Twin - REV2.docx` (top of the book folder). Older masters go to `bak\`. The Markdown working copy is `chapters/`. REV1 is in `bak\2026-10-15 REV1\`.
- Cover: `cover/`. KDP package: `KDP_Description.md`. Status and scores: `notes/_STATUS.md`. What is established on the page: `notes/book1_continuity.md` (see "REV2 changes"). Earlier review: `notes/REVIEW_2026-10-15.md` (Codex, manuscript only).
- Planning files (blueprints, Expanded Act I, outline, Novel Bible, Chapters.txt), the session-log copy and the stray RF-IC and empty folders were moved to `bak\2026-10-15 planning files\` on 15 Oct. The Complete Book Blueprint still controls chapter order.
- The `.claude` worktree in the shared checkout was not touched.

## Git
- Branch `digitaltwin-rev1-20261015` (built on `codex/digital-twin-critical-revision`). Normal pushes only; never force-push.
- Build scripts are in `notes/build/` (docx builder, cover, REV2 edit script).

## Rules for this book
- British spelling and British deadpan; Version A About the Author; no paperback; docx only; obey the banned-name rule in notes/LOTHAR_RULES.md and search before every commit.


## REV3 (15 Oct 2026)
- Master is now `The Digital Twin - REV3.docx`; REV2 moved to `bak\2026-10-15 REV2\` (the move is on the D: copy; bak is gitignored).
- REV3 text edits are scripted: `notes/build/rev3_edits.py` then `fix1.py`, run against the REV2 chapters. Do not hand-edit the docx; edit the chapters and rebuild with `notes/build/build_docx.py` (it skips this book's own line in the Also-by list).
- Added: Ch 21 hen steals Item Seven; Ch 23 cooling fan fails, peas on the tower; Ch 24 Compliance raid (Mr Lessing, the Aga file seized, tower hidden in the potato store, Giles away by the loch path); Ch 32 names Lessing in Sir Rupert's party; Ch 35 Pym transferred to Lost Property (Mammalian). Eight chapter endings changed from sentiment to a dry button (Ch 10, 11, 12, 16, 17, 18, 19, 33). 22 trailing similes and 7 "a man who" clauses cut; Ch 32 projection description shortened (the Programme is explained once, in Ch 21).
- Book 2 hook still lands: Ch 35 ends with S2 MERCIER, S. and Sophie's phone dark on the cloth, not ringing.
- Banned-name rule: see notes/LOTHAR_RULES.md; the manuscript and docx were grepped clean.
- Do not touch the Historical Corrections folder (another agent).
