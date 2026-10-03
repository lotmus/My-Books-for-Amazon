# Handover

Several agents edit this repository at once. Pull `origin/main` before you start. Run `git status` from `D:\My Books for Amazon`, not from a book folder. A status in the wrong folder has reported a clean tree that was not clean.

If a book’s own note disagrees with this file, the book’s note wins inside that book. If a manuscript file disagrees with a status log, the manuscript wins.

Do not commit another session’s `.docx`. Do not commit `bak\` snapshots, audit scripts, or `relativistic-site\`.

## Where the live notes are

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