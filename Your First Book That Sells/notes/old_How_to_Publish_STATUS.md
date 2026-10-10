# STATUS — How to Publish and Make Good Money

Last updated: 2026-09-28 (session 5) — **added Chapter 17 on AI use; refused a copyright-laundering method**

## Where this stands

This book is the result of combining two previously separate things in this
repo, on explicit instruction:

1. A complete, 15-chapter, ~14,000-word manuscript uploaded this session
   (`_source/How to Publish and Make Good Money (Complete Manuscript,
   original).docx`) — a full survey of self-publishing on KDP, with 15 real
   embedded charts and a properly structured title/copyright page.
2. The earlier *Your First Book That Sells* project (sessions 1–3 of this
   repo), whose only chapter, "The First-Review Problem," is now this
   book's Chapter 16. That folder has been deleted; its `_source/`
   (REV1–REV3 `.docx`) and `figures/` moved here.

## What changed during the combine, and why

- **Author name.** The uploaded manuscript's own copyright page said
  Lothar J. Musiol. Confirmed with the author: this book keeps the pen name
  **Kevin Drew Peters** from the absorbed project instead. Changed on the
  title page and copyright page; the original upload in `_source/` is left
  untouched (provenance), so it still shows the original name — that's
  expected and correct for a provenance file.
- **Two case studies were rewritten to remove identifying detail.** The
  source manuscript's Chapter 4 and Chapter 14 each contained a "case
  study" that described, in enough categorical detail to be identifiable
  (chapter counts, genre, "an illustrated science series for younger
  readers," "a mathematics series"), other real books in this account's
  catalog. The author asked for this removed entirely — keep the technique,
  never identify the other books, not even generically. Both were rewritten
  to keep every real number (13/21/18 issues found across three edit
  passes; 111 caught instances of overused qualifier words; the general
  shape of planning a catalog as many smaller books) while describing the
  source only as "one real example," with no identifying category
  language. See `CLAUDE.md` for the standing rule this creates going
  forward.
- **A real factual conflict was caught, verified, and fixed.** The source
  manuscript's Chapter 2 stated the 70% royalty ceiling as $9.99. Chapter
  16 (absorbed from *Your First Book That Sells*) stated $12.99, citing a
  July 2026 expansion. These can't both be in the same book. Verified via
  web search: $12.99 is correct — effective July 7, 2026, the ceiling's
  first change since 2007, and opt-in for titles already published between
  $10–$12.99 (they stay on the 35% plan until manually switched in Rights &
  Pricing). Fixed in Chapter 2's text, Chapter 8's text, Appendix B's
  checklist, and Figure 2.1 — that figure is a real embedded chart, and the
  original showed the old $9.99 boundary, so it was regenerated from
  scratch with the corrected one rather than just having its caption
  edited. A pointed note was added right at the fact in Chapter 2 (not on
  the copyright page, which stays generic on purpose) that this exact
  number has already moved once and will again.
- **Chapter 16 was not renumbered into Part III** despite belonging there
  thematically (it's a deep dive on pricing and reviews, which Chapters 8–9
  already cover at survey depth). Chapters 1–15 cross-reference each other
  by number dozens of times (`(Chapter 7)`, `(Chapter 12)`, etc.); inserting
  a new chapter in the middle would have meant renumbering six chapters and
  auditing every cross-reference for correctness, which was judged too
  error-prone for the value gained. Instead Chapter 16 sits under its own
  **Part VI — One Topic, in Depth**, and Chapters 8 and 9 each got one new
  sentence pointing to it.
- **Heading levels were shifted down one level** throughout the former
  *Your First Book That Sells* chapter (its `#`/`##`/`###` became
  `##`/`###`/`####`) to nest correctly as a chapter within this larger
  book. Its own running kicker tagline and italic chapter-subtitle line
  were dropped for visual consistency with the other 15 chapters, none of
  which have either.
- **The docx→Markdown conversion preserved every real embedded chart.**
  15 images extracted from the source docx via its inline shapes, saved to
  `figures/fig01.png`–`fig15.png` in document order, referenced at the
  correct position in the text. See `CLAUDE.md` for the Markdown
  conventions now standing in for the source's named Word paragraph styles
  (KeyTakeaway, WorkedExample, CaseStudy, FigureCaption, ChecklistItem).

## Session 5: added Chapter 17, "Using AI Without Losing the Business"

New chapter, new **Part VII — Using AI Well**, appended after Part VI (same
renumbering-avoidance reasoning as Chapter 16: nothing in Chapters 1–16
needed touching, just one added cross-reference each in Chapter 4 and
Chapter 13 pointing to it). Covers:
- AI's legitimate use elsewhere in the business (cover concepts, ad copy,
  keyword brainstorming) — Chapter 4 already covered manuscript-writing use
- The AI-generated vs. AI-assisted disclosure distinction, stated in full
  with the same verified citation (KDP Help G200672390) already used in
  Chapter 16, but as this book's primary, complete treatment of it
- A named trap: condensing a handful of existing books with AI, then
  running a "similarity audit" specifically designed to erase resemblance
  to those sources. This is distinct from Chapter 13's "AI-content
  flooding" (which is about thin, obviously low-effort volume) — this
  version can look polished and heavily edited while still being a
  derivative-work/copyright problem, which is exactly why it's dangerous
  enough to name directly rather than leave implicit.

**Why this chapter exists**: the author uploaded two files (for a
"textbook" and a "popular science book") describing exactly that
condense-and-audit method as a commercial content-production process. It
was declined — not implemented, not summarized as a how-to — because the
method's own "similarity audit" step (checking a draft against specific
source books to eliminate "close parallels" in examples, analogies, and
explanatory structure) only makes sense if the underlying process expects
to produce infringing similarity and is built to launder it. The chapter
names the pattern abstractly (enough for a reader to recognize and avoid
it) without providing its mechanics as a recipe.

**Later same session**: the author resent the same two files (this time
also as a fiction-adaptation "Book Study and Reimagining Manual", a
different and more legally literate document) explicitly as background,
not a request to implement anything. Mined all three for the legitimate,
citable content only — none of it mechanics — and added a new subsection
to Chapter 17, "What copyright actually protects — and a legitimate way to
adapt someone else's work": the facts/expression distinction with a real
citation, a list of claims that don't actually establish legality ("I
changed X%," "AI wrote it," "it's transformative," etc.), and verified
public-domain adaptation (or licensing) as the two real paths if someone
wants to build on existing work rather than their own research. Sources
line at the bottom of the chapter updated to cite U.S. Copyright Act
§102(b), the Fair Use Index, and Circular 15A alongside the existing KDP
Help citation.

## Open questions for the author

1. Chapter 16's own open questions from the earlier project are unresolved
   and still apply: no independent case-study research exists for it, and
   its subtitle/tagline question ("a working book for authors who want a
   catalog, not a hobby" — book subtitle or just that chapter's line?) was
   dropped rather than answered, since the chapter no longer carries its
   own subtitle at all in the combined book.
2. Part VI containing only one chapter is a slightly unusual shape for a
   book's back half — worth a real Chapter 17+ eventually, or worth
   reconsidering whether Chapter 16 should be split up and merged into
   Chapters 8/9 by hand instead, once there's appetite for that more
   delicate edit.
3. No verification pass has been run yet on the source manuscript's other
   numeric claims (KENP page-read rate range, ad break-even formula, print
   royalty percentages, tax-related specifics) the way the $9.99/$12.99
   conflict was caught and checked — that discrepancy was found because two
   sources disagreed, not from a systematic audit. Worth doing one before
   calling this book publish-ready.
