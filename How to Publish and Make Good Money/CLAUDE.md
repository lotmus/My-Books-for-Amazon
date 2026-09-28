# How to Publish and Make Good Money — working instructions

## Scope: stay in this folder

This folder is its own book: *How to Publish and Make Good Money — A
Straight, Show-Your-Work Guide to Self-Publishing Profitable Books on
Amazon*. It replaces and absorbs the earlier, narrower *Your First Book
That Sells* project — that folder no longer exists; its one chapter now
lives here as Chapter 16 (see below). Author is the pen name **Kevin Drew
Peters**, consistent with that earlier project — not Lothar J. Musiol,
even though the source manuscript's original copyright page said that
before this session changed it.

**Do not leave this folder.** Don't read, edit, or comment on any other
book, folder, or repo in this account while working on this one, even if a
fix elsewhere looks related. If something outside this folder seems worth
touching, say so and wait to be asked — don't go do it.

**Never name or identify this account's other books in this book's own
text**, even generically enough to be inferable (genre, chapter count, "a
companion book"). This book was assembled by combining sourced material
that originally did exactly that; every instance was rewritten to keep the
technique or lesson while dropping anything that pointed at which other
book it came from. Keep that rule going forward — this book's case studies
either name real, external, checkable people (as Chapter 16's field
reports already do), or they stay generic.

## Project facts

- **Complete, 16-chapter manuscript**, not an early draft: title/subtitle/
  copyright page, six Parts, three appendices, a closing word. Word-style
  structure preserved as a Markdown convention — see "Style conventions"
  below.
- **Chapters 1–15** come from a single complete manuscript upload
  (`_source/How to Publish and Make Good Money (Complete Manuscript,
  original).docx`), covering the full self-publishing landscape: royalties,
  writing/revision, formatting, covers, categories/keywords, pricing,
  launch, ads, taxes, KDP Select vs. wide, scams to avoid, catalog-building,
  and a first-year plan. It came with 15 real embedded charts, extracted to
  `figures/fig01.png`–`fig15.png` and already referenced correctly in the
  manuscript.
- **Chapter 16, "The First-Review Problem,"** is the absorbed *Your First
  Book That Sells* content — a much deeper tactical treatment of reviews
  and pricing specifically than Chapters 8–9 give it. It keeps its own
  established rigor (named field reports, a corrected royalty-table
  derivation, three of its own diagrams in `figures/fig01_launch_timeline.
  png`, `fig02_pricing_decision.png`, `fig03_review_eligibility.png`) and
  sits under its own **Part VI — One Topic, in Depth** rather than being
  renumbered into Part III, specifically so chapters 1–15's many existing
  cross-references (`(Chapter 7)`, `(Chapter 12)`, etc.) never had to be
  touched. Chapters 8 and 9 each carry one added sentence pointing readers
  to Chapter 16 for the deeper version.
- **A real, verified factual conflict was caught and fixed during the
  merge**: the original Chapter 2 stated the 70% royalty ceiling as $9.99;
  Chapter 16's source material said $12.99, citing a July 2026 expansion.
  Verified via web search that $12.99 is correct (effective July 7, 2026,
  the first change to that ceiling since 2007, opt-in for already-published
  titles). Fixed in every location in Chapters 2 and 8, and in Figure 2.1's
  chart, which was regenerated from scratch with the corrected boundary —
  the original chart image showed the old, wrong ceiling. A pointed callout
  was added right at the fact in Chapter 2 (not just the generic copyright-
  page disclaimer) noting that this exact number already moved once and
  will again.
- **Author name was changed from the source file's original text.** The
  uploaded manuscript's title page and copyright page said Lothar J.
  Musiol (this repo's usual author); changed to Kevin Drew Peters
  throughout, per explicit confirmation, to keep continuity with the
  absorbed *Your First Book That Sells* project's pen name.

## Style conventions (Markdown standing in for the source docx's Word styles)

The original manuscript used named Word paragraph styles; this repo's
convention is Markdown, so each maps to a consistent convention. Keep using
these for any new content in this book:
- `# ` — book title (once) and Part-level headings.
- `## Chapter N: Title` — chapter headings.
- `### ` / `#### ` — sections and subsections within a chapter.
- `> **Key takeaway:** …` — a chapter's summary-style callout.
- `> Worked example. …` — a numbers-shown worked calculation.
- `> Case study: …` — a real, generic-but-true illustrative example (see
  the naming rule above — never identifies another of this account's
  books).
- `![figure](../figures/fileName.png)` immediately followed by an italic
  `*Figure N.N — caption.*` line — an embedded chart.
- `- [ ] item` — a checklist item (Appendix A, Appendix B).

## House style

Terse, declarative, second person. Every number shows its arithmetic. Any
claim about Amazon's actual algorithm or ranking behavior is explicitly
labeled as inference or creator/author consensus, never stated as fact —
this book is built specifically around that distinction; see "A Note
Before You Begin." Curly quotes and apostrophes, spaced em dashes.
