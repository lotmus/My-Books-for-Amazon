# WORK QUEUE - The Dolphins' View of History

**Status: complete, Codex (15 Oct 2026). Job: REV4.**
Written 15 Oct 2026 by Grok Bot from REVIEW_REV3_2026-10-15.md, _STATUS.md and the previous WORK_QUEUE.md (old queue moved to bak\2026-10-15 old work queue\ on D:).

Read first: notes/LOTHAR_RULES.md (repo root notes/), SCORES.md (Job queue), then this folder's notes\REVIEW_REV3_2026-10-15.md, notes\_STATUS.md, notes\PICTURE_CREDITS.md, notes\Held Back - Sections Written but Not in the Build.md.

## Starting point
Master: `The Dolphins' View of History - REV3.docx` (commit a967bb6b on main; 40 chapters, about 66,414 words, 19 images, 1.25 MB). Scores: overall 9.1, sellability 6.2 (Grok's own estimates, no outside reader, no Previewer check). Output the new master as `The Dolphins' View of History - REV4.docx` and move REV3 to bak\2026-10-15 pre-REV4\.

## Goal
Make the book a faster, sharper read without losing what works: a REAL 15-25 percent compression of the survey chapters, plus the two missing vignettes, less formulaic verdicts and the loose ends from REV3.

## Steps, in priority order
1. **Compress the survey chapters by about 8,000-10,000 words** (target body about 56,000-58,500 words; REV3 managed only -0.6 percent because additions offset cuts, so count words per chapter before and after and keep a table in your review note). Work chapter by chapter, longest survey chapters first. Cut: repeated explanations, secondary country/ruler detours, second and third examples where one carries the point, stacked similes, restated theses, sentences that only announce what the next sentence says. Keep: the dolphin frame and voice, the thesis ("capability compounded, judgment did not"), historiography notes, global non-Eurocentric coverage, the bridge sentences added in REV3, all pictures and their lead-in sentences, all exercises (if any chapter has them), all existing vignettes (Agnolo di Tura, Benin plaque, Equiano, Nanni/Ea-nasir, Jerome, Afonso I, Yang Jisheng). Do not net-add words anywhere except the two new vignettes (step 2), which must be paid for by extra cuts elsewhere.
2. **Two new vignettes** (each 150-300 words, primary-source or concrete scene, with a Notes and Sources entry and a link where one exists): (a) the Neolithic transition (for example a Catalhoyuk house, Gobekli Tepe, or skeletal evidence of early farmers; choose what you can source reliably); (b) the digital/climate present (a concrete, checkable moment: for example a named dataset, the Keeling curve, a documented outage or a documented flood/heat event; no speculation, no modern-politics jabs).
3. **Vary the dolphin verdicts**: several survey-chapter verdicts are still formulaic. Make lengths and shapes differ (from one line to a short paragraph); remove any verdict that only repeats the chapter's last paragraph; keep the strongest in full. Keep the heavy chapters (slave trade, genocides, Great Leap, Rwanda, Congo) sober: no jokes.
4. **Afonso I's Notes entry has no link**: find a reliable online source (an edition of the 1526 letters to the King of Portugal, a museum or university page) and add a keyword hyperlink with hidden URL; if none can be verified, say so in the Notes entry and in the report. Do not invent a source.
5. **Resync the .md chapter working copies with the docx** (docx is the source of truth; regenerate chapters\*.md from REV4, keep the chapter numbering after the REV3 merges: 40 chapters). Do not commit stale md.
6. **Back cover** as the last page per the rule: Kindle back cover text-only on the front-cover colour (existing files KINDLE_BACK_COVER_2560.jpg and scripts\make_back_cover.py are the starting point; make a text version for the docx last page: blurb from notes\KDP_Description.md, three or four hook lines from the book itself (no invented reviews), "Lothar J. Musiol" line with Version B bio sentence from notes\ABOUT_THE_AUTHOR - canonical.md (no Colin line), the Also-by list from notes\ALSO_BY - canonical list.md without this book).
7. **Re-check automatically**: zero sentences over 300 characters (REV3 got to zero; keep it), banned name zero hits, "Xi" never in prose, the Notes bibliography title with the real Economy title stays, contents rebuilt and fully linked (about 51 entries), page size 3.6 x 4.8, 0 tables, images inline and within 3.0 in, American spelling, no "Colin" line, no AI-tool names as credits. Update PICTURE_CREDITS.md if any picture changes.
8. **Kindle Previewer check** (installed on LOTHAR-HP; REV3 was only rendered in LibreOffice): open the built file, check the merged chapters, the contents links, the strips/figures, and the new back cover; record the result. If Previewer cannot be run, say so plainly and do not claim a pass.
9. Update notes\_STATUS.md, write notes\REVIEW_REV4_<date>.md (what changed, per-chapter word counts before/after, scores, honest gaps), update this book's row and Job queue row in SCORES.md (repo copy), push, copy to D:.

## Do NOT change
The dolphin frame, global non-Eurocentric coverage, historiography notes, the thesis, the popular-history register, the cover design (cover is separate; do not redraw it).

## Done criteria
- Body words down at least 8,000 (target 8,000-10,000) from 66,414, shown by a before/after table.
- Both new vignettes present with Notes entries; Afonso entry linked or honestly flagged.
- Verdicts visibly varied; heavy chapters still sober.
- md resynced; back cover last page; contents linked; checks in step 7 all clean; Previewer result recorded.
- Rescored honestly (four angles; Grok's REV3 reference: overall 9.1, sellability 6.2). A rise in sellability beyond about 6.5 is not credible without a cover and listing change; do not claim one.

## Report back
Words before/after, chapters affected, the two vignettes (titles and sources), verdict changes, Afonso link result, Previewer result, scores per angle vs REV3, commit hash, file paths, open items for Lothar (cover decision, outside reader, KDP upload).
## Standing constraints (from notes/LOTHAR_RULES.md; the rules file wins on any conflict)

- Format: **EPUB is the upload format**; docx is kept only as a fallback for manual issues Lothar cannot resolve in his epub editor (changed 2026-10-15); no PDF; md working copies are fine. Docx layout rules still apply to the docx and epub content: Word page size 3.6 x 4.8 in with 0.3 in margins; every image fits inside the 3.0 in text width; Heading 1 (chapter, appendix, back matter) starts on a new page via page-break-before; headings bold, 16 pt, dark-to-medium blue, centered, Kindle-safe font. No Word tables, no text boxes, no floating images (inline pictures only). Linked contents page, no page numbers, every appendix item, About the Author and Also-by linked. No PDF, no paperbacks.
- Names: the author is always "Lothar J. Musiol" (with the J.) unless the book's pen-name rule says otherwise. Never write the banned name (the surname of the former US president) anywhere, in any file, notes and scores included; search every changed file for it before every commit. "Xi" is only ever "Pooh" in prose. No cryptic abbreviations such as the three-letter short form of a long title; write full titles.
- Back cover (Lothar, 15 Oct 2026, every Amazon book): the LAST page is a back cover in the style of the front cover, text instead of pictures, as on a paperback: blurb or tagline, a few review-style hook lines or selling points, a short author line (pen-name rules apply), the Also-by list, the series line where relevant. No barcode, no price, no ISBN box. Kindle-friendly: page size 3.6 x 4.8 in, styled text on the cover colour or one inline image of the styled page; no tables. Never invent quotes or endorsements.
- Files: never delete anything. When you create a new version (REVn+1), move the previous master to this book's own bak\ (for example bak\2026-10-15 pre-REVn+1\), never to a common folder. Only the current master, its md copy and notes stay at the top of the folder. Do not commit bak\ snapshots or audit scripts. Commit only this book's files; do not commit another session's docx.
- Git: before any git command clear GIT_DIR and GIT_WORK_TREE and check git rev-parse --show-toplevel. Work in your own temp worktree (repo git dir C:\Users\lomus\git-dirs\My-Books-for-Amazon.git), merge origin/main first, commit in small batches, normal push to your branch AND to main, never force-push, no git inside D:. Copy the finished files into the D: folder by plain copy. Never reset the D: checkout.
- Job rules: one job per book; at most two heavy jobs at once on this low-RAM PC; edit only this book and only its own SCORES.md row and Job queue row (repo copy; D:'s SCORES.md differs, leave it alone).
- If the PowerShell tool throws an intermittent parse error, retry; for docx edits use python-docx or zip/XML with run structure and hyperlinks preserved; verify testzip(), XML parses, media count, hyperlink count after every write.
- Scoring (honest, no inflation): four angles each with a score out of 10 and an issue list: target reader, harsh critic, subject expert / fact-checker, Amazon market; overall last, plus sellability out of 10. For science books use the science score areas in the rules file. Score only what you checked. Do not give 10s. Say plainly what was not checked (no outside reader, no cold read, Kindle Previewer run or not).
- Reporting: short, answer-first: what changed (with before/after numbers: words, chapters, images), the new scores per angle and overall vs. before, what was NOT done and why, the commit hash, the exact file paths written, and what only Lothar can do.

## Completion record — 15 October 2026

REV4 is complete and is the current master. Body count: 50,051 → 41,500 words (−8,551; 17.1%); whole document: 66,518 → 58,211. Per-chapter counts, sources, and QA are recorded in `REVIEW_REV4_2026-10-15.md`. Both new vignettes are sourced and linked; the Afonso I source is linked; verdicts are varied; the final page is a text-only back cover; active Markdown copies are synced. Repeat scan is clean, with 51 Heading 1 paragraphs, 19 inline images, 363 hyperlinks, no tables, valid DOCX XML/ZIP, and successful 420-page LibreOffice render.

Kindle Previewer was not run because desktop control is unavailable in this session. An outside reader has not reviewed REV4. These two checks remain before a KDP upload decision.
