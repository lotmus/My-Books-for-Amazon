# Your First YouTube Channel That Rocks — working instructions

## Scope: stay in this folder

This folder is its own book: *Your First YouTube Channel That Rocks* (titled
*Your First YouTube Channel That Sells* until 2 October 2026), a
companion to *Your First Book That Sells* (same repo, separate book — the two
are not chapters of one title, and do not cross-reference each other's
manuscript). Author is **Lothar J. Musiol** (set 1 October 2026; the earlier pen
name Kevin Drew Peters is retired). This book is not a textbook and not a popular-science book. Do not
apply `COMMERCIAL BOOK METHOD.md` to it.

**Do not leave this folder.** Don't read, edit, or comment on any other book,
folder, or repo in this account while working on this one, even if a fix
elsewhere looks related. If something outside this folder seems worth
touching, say so and wait to be asked — don't go do it.

Before editing, read the **Current state** section at the top of `_STATUS.md`.
If an older paragraph in that file disagrees with it, Current state wins.
That includes any memory that pull request 36 is still open or that this
book has only the first three chapters.

**Git, with other agents in this checkout.** Stage and commit only files
inside this folder. Do not `git add` the parent tree. Other books have
their own uncommitted work. Do not force-push `main`. Do not merge
`claude/youtube-book-create-chapter` again; pull request 36 is already merged.

## Project facts

- **Fifteen chapters, order fixed** in `build_docx.py` (refocus of 2 October
  2026). The book is about monetizing the channel itself — YouTube Partner
  Program thresholds (2026 and the 1 February 2027 changes), ads and RPM/CPM,
  Premium, the Shorts pool, memberships, Super Chat/Stickers/Thanks,
  sponsorships, and affiliate links as income. It is **not** about selling
  your own products, videos, books, or services through the channel; do not
  reintroduce offers, prices for your own products, or checkout pages. The
  arc: setup and quality (1 Name the Viewer; 2 The Click Is the Whole
  Business; 3 Nobody Can Tell What It Cost; 4 Record It So They Stay), growth
  (5 Eight Videos, Each With One Job; 6 Six Weeks to a Working Channel; 7 Read
  the Count; 8 Grow Toward the Gate), eligibility (9 The Gates and the Review;
  10 The Rules That Can Switch Off the Money), monetization streams (11 Ads,
  RPM, and the Shorts Pool; 12 Money From the People Who Watch; 13 Sponsors
  and Affiliate Links), scaling and sustainability (14 Keep It Paying; 15 The
  Channel Workbook). Front matter "Start here" and back matter "The last
  word", Glossary, Sources are in `build_docx.py`. Figures: 3.1
  free-production-pipeline, 14.1 follower-floor. Text removed in the refocus
  is in `D:\bak\2026-10-02 YouTube book refocus\`.
- The click chapter is chapter 2. The cheap-production chapter is chapter 3.
  Eligibility is chapter 9. Use chapter numbers in cross-references.
- **Source material provenance matters here more than usual.** Everything in
  `_source/` except this file and `_STATUS.md` originated as either the
  author's own raw notes (a bookmark list of tools) or a saved chat transcript
  with a *different* AI assistant, doing hands-on production work for the
  author's own separate, real video project (finance/real-estate niche,
  specific brand names and characters). That project's specific content
  (brand names, characters, example tags and titles) **must never appear in
  this book** — the author is producing that video separately, for their own
  channel, not as a book example. Only the *general, transferable principles*
  underneath that transcript belong here, rewritten in this book's own voice,
  with generic or unrelated illustrative examples. See `_STATUS.md` for the
  specific incident this rule comes from.
- Because some source material is another AI's output rather than the
  author's own writing, KDP's AI-content disclosure distinction applies here
  more directly than in the Kindle book: content drafted by **this** session
  from verified facts and interface behavior, in this book's own prose, is
  AI-*assisted* authorship in the normal sense a human editor's use of a tool
  would be; content that would only be a light edit of another AI's own
  phrasing would cross into AI-*generated* territory KDP wants disclosed. Default
  to writing new prose from extracted facts, never lightly editing the source
  transcripts' own sentences.

## Style conventions (Markdown standing in for Word paragraph styles)

The chapters already on disk are the style to match. Each file opens with
the series line, then `# Chapter title`, then an italic job line. Sections
inside a chapter are `## ` with a roman numeral. Do not rename headings to
`## Chapter N:`. *How to Publish and Make Good Money* is not in this repo
anymore; do not restore that folder to copy its style.

- `# Title` — the chapter title in each manuscript file. No “Chapter N” prefix. `build_docx.py` numbers chapters from its `ORDER` list.
- `## I. Section title` — a section. The builder turns this into Heading 2. Do not use `###` for those sections. A `###` line is not a heading in this builder; it would be printed as plain text, hashes included.
- `> **Key takeaway:** …` — a chapter's summary-style callout.
- `> Worked example. …` — a numbers-shown worked calculation.
- `> Case study: …` — a real, generic-but-true illustrative example (never
  identifying another book in this account's catalog by name or inferable
  detail — that rule applies account-wide, not just to the KDP book).
- `![figure](../figures/fileName.png)` followed by an italic
  `*Figure N.N — caption.*` line — an embedded chart/diagram.
- `- [ ] item` — a checklist item.

Rebuild the Word file with `python scripts\build_docx.py` from this folder. It writes `Your First YouTube Channel That Rocks.docx`. It is
plain `python-docx`. Do not add a second builder.

## House style

Match *Your First Book That Sells*'s established voice unless a reason
emerges to diverge: terse, declarative, second person. Capital-roman-numeral
sections, each a complete argument. Concrete numbers over adjectives.
Platform rules are stated as fact only when checkable directly in the
product's own interface or published policy; anything about ranking or the
algorithm's actual behavior is explicitly labeled as inference or creator
consensus, not fact — this platform is if anything more opaque about its own
mechanics than KDP is, so this distinction matters even more here. Curly
quotes and apostrophes, spaced em dashes. A chapter ends with a myths section
and a one-line sources/disclaimer paragraph.
