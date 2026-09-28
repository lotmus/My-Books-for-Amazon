# How to Publish and Make Good Money — Book Plan

_Started 2026-09-27. New book — no prior draft existed anywhere this session could
reach (checked the whole `my-books-for-amazon` repo; nothing under "publish" or
"money" existed before this). Folder name corrected from the working title's
"Pubish" typo to "Publish." Built from scratch on branch
`claude/book-publishing-guide-arqfkm`, matching the repo's convention of one
top-level folder per book._

## The premise

A straight, mechanically accurate, no-guru guide to self-publishing on Amazon
KDP and actually making money at it — royalty math, categories and keywords,
pricing, launch, ads, taxes, and the scams to dodge along the way. Aimed at
someone who has a manuscript (or the will to write one) and wants the business
side explained by someone who will show the arithmetic instead of promising a
lifestyle.

Differentiator: most KDP guides are either recycled blog-post advice or a
guru's funnel for a $997 course. This one shows its work — real royalty
formulas, a real break-even ACOS calculation, a real keyword-slot count — and
where it uses an illustrative model instead of a disclosed Amazon statistic
(pricing curves, launch-concentration effects, backlist compounding), it says
so on the chart itself. A few chapters also draw a "Case Study" box from the
actual production discipline used elsewhere in this catalog (the EE series'
3-source method and multi-pass audit habit, the History book's repetition
sweeps) as a worked example of what real editorial rigor looks like, rather
than a generic "edit your book" bullet point.

## Format decisions

- **Kindle ebook + paperback**, matching this catalog's default. No hardcover
  chapter content changes if hardcover is added later — KDP hardcover uses the
  same interior file as paperback.
- Kindle edition needs no ISBN (ASIN only), no index, and no page-numbered
  TOC — same reasoning already established for the EE series: KDP builds its
  Kindle "Go to" navigation from Heading 1/Heading 2 styles. A **plain-text
  Contents listing** (titles only, no dot leaders, no page numbers) sits in the
  front matter for readers, not for navigation.
- Paperback uses KDP's free assigned ISBN unless the user later wants
  publisher-of-record control (Appendix C covers the tradeoff).
- Every Part and Chapter heading forces a fresh page (`pageBreakBefore` on the
  Heading 1/2 styles in the reference doc), same fix already proven on the EE
  series' pagination pass — cheaper to build in from the start than to patch
  later.
- **`cover.png` is a standalone file for KDP's separate cover-upload slot, not
  embedded on page 1 of the manuscript** — KDP shows the uploaded cover on its
  own; repeating it inside the interior file would show the cover twice.

## Toolchain (this session, Linux container — no Word/PowerShell COM available here)

- Markdown source chapters → **pandoc** (`chapters/*.md` → docx), styled via a
  `reference.docx` built with **python-docx** (Heading 1/2/Title styles, page
  breaks, accent color).
- Illustrations via **matplotlib**, using the validated categorical/sequential/
  status palette from the `dataviz` skill (`#2a78d6` blue accent throughout, so
  body headings and charts share one color language). Charts built on an
  illustrative model (not a disclosed Amazon statistic) are labeled as such
  directly in the caption.
- `figures/make_figures.py` regenerates every chart from one script — matches
  this repo's existing pattern of a checked-in generator script (`_generate.js`
  in `History/`) rather than hand-edited images with no source.
- Source of truth stays in `chapters/*.md` (readable in git diffs); the shipped
  `.docx` is a build artifact regenerated from it, same "keep sources, ship the
  merged doc" split the EE series uses for its Drafts.

## Structure

**Front matter**: title page, copyright page, Contents, "A Note Before You Begin."

- **Part I — The Landscape**
  1. Why Self-Publish
  2. How Amazon Actually Pays You
- **Part II — Writing and Producing the Book**
  3. Choosing What to Write
  4. From Draft to Manuscript
  5. Formatting That Doesn't Break Kindle
  6. Covers That Sell in a Thumbnail
- **Part III — Getting Discovered**
  7. Categories, Keywords, and Your Product Page (expanded 2026-09-28 to fold
     in book-description/A+ Content copywriting alongside categories/keywords —
     see status log)
  8. Pricing for Profit
  9. Launching Without an Audience
  10. Amazon Ads Without Wasting Money
- **Part IV — The Business Side**
  11. Getting Paid: Taxes, Payments, and Reporting
  12. KDP Select vs. Going Wide
  13. Avoiding the Traps
- **Part V — Playing the Long Game**
  14. From One Book to a Catalog (expanded 2026-09-28 with an audiobooks/ACX
      section — see status log)
  15. A Realistic First-Year Plan

**Back matter**: Appendix A (Launch Checklist), Appendix B (Royalty Quick
Reference), Appendix C (ISBN/Wide-Distribution Notes + Further Reading), A
Closing Word.

## Illustrations (16 total, `figures/`)

1. `cover.png` — title art (standalone, for KDP cover upload)
2. `fig01_publishing_workflow.png` — the whole book as one 8-stage pipeline (Ch1)
3. `fig02_royalty_cliff.png` — the 70%/35% royalty curve across price points (Ch2)
4. `fig04_editing_workflow.png` — the 4-pass editing pipeline, draft to ready manuscript (Ch4)
5. `fig05_ebook_vs_print.png` — a branching workflow: manuscript splits into the Kindle path vs. the print path (Ch5)
6. `fig06_thumbnail_test.png` — a cover mockup at full size vs. actual thumbnail size (Ch6)
7. `fig07_keyword_funnel.png` — title words → 7 backend slots → categories → search match (Ch7)
8. `fig07b_product_page_anatomy.png` — the 5-stage anatomy of a converting book description (Ch7)
9. `fig08_pricing_sweet_spot.png` — illustrative price-vs-take-home curve (Ch8, labeled illustrative)
10. `fig09_launch_concentration.png` — same sales spread out vs. concentrated (Ch9, labeled illustrative)
11. `fig10_acos_breakeven.png` — break-even ACOS worked example, good/critical zones (Ch10)
12. `fig10b_ad_workflow.png` — auto campaign → search term report → harvest → manual, with the ongoing-refinement loop (Ch10)
13. `fig12_select_vs_wide.png` — a decision workflow: enroll → track page-reads → renew or go wide (Ch12)
14. `fig13_red_flags.png` — scam warning-sign checklist graphic (Ch13)
15. `fig14_catalog_compounding.png` — illustrative backlist income compounding (Ch14, labeled illustrative)
16. `fig15_first_year_roadmap.png` — 12-month phase timeline (Ch15)

Two figures (`fig05`, `fig12`) were redesigned from static two-column
checklists into branching workflow/decision diagrams after the user flagged
the original set as "too generic" and asked for something about workflows
— see status log.

## Status log

- 2026-09-27: Book plan written; folder, chapters/, figures/ scaffolding created
  on `claude/book-publishing-guide-arqfkm`.

- 2026-09-27 (same day): First complete draft finished end to end. All 15
  chapters + front/back matter written (~12,500 words, front matter through
  Appendix C). All 12 illustrations generated via `figures/make_figures.py`
  using the validated dataviz-skill palette; a full visual QA pass caught and
  fixed 8 real layout bugs before shipping (an arrow rendering backwards on
  the cover, a legend colliding with axis labels, a stray debug mark, a
  cover-mockup caption overlapping the image it described, a funnel's bottom
  segment too narrow for its own label, a warning-icon glyph landing mid-
  sentence instead of beside it, and a Gantt chart whose 1-month-wide bars
  couldn't fit their labels — fixed by switching that one to a standard
  left-labeled `barh` layout instead of in-bar text).
  Final manuscript assembled via `build_book.py` (python-docx reference
  doc + pandoc), matching the EE series' pagination fix from day one
  (`pageBreakBefore` set on the Heading 1/2 *styles*, not patched per-heading
  later). One real assembly bug found and fixed: passing `--metadata
  title=/author=` to pandoc made it auto-generate a second, duplicate title
  block (its own built-in Title/Author styles) on top of the hand-authored
  title page — fixed by dropping those flags and setting the docx's core
  properties directly via python-docx after conversion instead. Verified via
  zip integrity, XML well-formedness, and a full python-docx read-back
  (heading outline, image count, word count) — this container has no
  Word/PowerShell COM and headless LibreOffice fails to load even a
  trivial one-line docx (confirmed environment limitation, not a content
  bug), so no rendered-PDF visual pass was possible this session; that
  would be a good next step wherever Word or a working LO install is
  available. `cover.png` is deliberately NOT embedded in the manuscript —
  it's for KDP's separate cover-upload slot.
  NOT YET DONE: no external review pass of the kind the EE series and
  History book each got (multiple independent re-reads hunting for
  factual/numeric errors); no reader has verified the KDP policy specifics
  (price bands, keyword-slot count, royalty formulas) against KDP's current
  live help pages, which the book itself repeatedly tells readers to do.

- 2026-09-27 (later): user feedback — several figures read as generic
  (static two-column checklists) where the underlying content was actually
  a process. Added three new workflow diagrams (the whole book as one
  8-stage pipeline for Ch1, the 4-pass editing pipeline for Ch4, the ad
  auto-to-manual cycle with its ongoing-refinement loop for Ch10) and
  redesigned `fig05` and `fig12` from static comparisons into a branching
  formatting workflow and a Select-vs-Wide decision flow, respectively.
  One layout bug caught on the first render and fixed before shipping: the
  curved connector arrows from "Finished Manuscript" into each column in
  the new `fig05` crossed directly through the "EBOOK PATH"/"PRINT PATH"
  header text — shortened the arrows to stop at the column's top edge
  instead of continuing down into the header's vertical space. 14
  illustrations total after this pass. Pushed as a second commit to the
  same PR (#18) rather than amending.

- 2026-09-28: user said "continue writing." Rather than pad existing
  chapters or insert new numbered chapters mid-book (which would force a
  renumbering cascade across every later chapter heading, every figure
  caption, and every prose cross-reference like "Chapter 9" or "Ch 11" —
  exactly the bug class the EE series' and History book's own status logs
  describe fixing repeatedly after their renumbering passes), filled two
  genuine content gaps by folding them into the most thematically-fitting
  existing chapter, so no other chapter's number, figure number, or
  cross-reference needed to change:
    - Chapter 7 (renamed "Categories, Keywords, and Your Product Page")
      gained a full section on writing the Amazon book description itself
      — the hook/promise/bullets/proof/CTA structure, a before-and-after
      worked example, and Author Central vs. A+ Content — since the
      description is a real, previously-missing third pillar of "the
      product page" alongside the cover (Ch6) and categories/keywords.
    - Chapter 14 gained an audiobooks/ACX section (DIY narration vs.
      royalty share vs. pay-per-finished-hour vs. the newer AI/"Virtual
      Voice" option, the exclusivity trade-off vs. going wide, a worked
      cost example, and a note on which books suit audio at all) — a
      second-format revenue lever that fits the chapter's existing
      "extend a catalog's earning power" theme exactly.
  One new figure added (`fig07b_product_page_anatomy.png`, a 5-stage
  workflow reusing the same `_vertical_workflow` helper the Ch1/Ch4/Ch10
  diagrams already use) — correctly numbered Figure 7.2 since Chapter 7
  already had a Figure 7.1 (the keyword funnel). Deliberately did NOT add
  a figure to the audiobooks section: its three routes are a menu of
  parallel options, not a sequence, and the worked-example box already
  gives it the concrete treatment without forcing a diagram where the
  content doesn't call for one. Also updated `fig01_publishing_workflow`'s
  "Set Metadata" stage label to "Set Metadata & Listing Copy" to reflect
  Chapter 7's wider scope — no chapter numbers in that figure needed to
  change, since none of the chapters they reference were renumbered.
  16 illustrations total after this pass; word count ~13,600.
