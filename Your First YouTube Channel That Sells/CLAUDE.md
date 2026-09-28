# Your First YouTube Channel That Sells — working instructions

## Scope: stay in this folder

This folder is its own book: *Your First YouTube Channel That Sells*, a
companion to *Your First Book That Sells* (same repo, separate book — the two
are not chapters of one title, and do not cross-reference each other's
manuscript). Author is the same pen name, **Kevin Drew Peters**, unless told
otherwise.

**Do not leave this folder.** Don't read, edit, or comment on any other book,
folder, or repo in this account while working on this one, even if a fix
elsewhere looks related. If something outside this folder seems worth
touching, say so and wait to be asked — don't go do it.

## Project facts

- **New project, early stage.** One chapter exists so far:
  `manuscript/The Click Is the Whole Business.md`, on titles, descriptions,
  tags, the content-safety category some words trigger, captions, retention,
  and posting cadence. No outline or chapter order is confirmed yet.
- **Two more chapters are planned but not written**, matching a
  Create → Publish → Build arc:
  - *Create*: making videos cheaply with free/low-cost tools (AI text-to-video,
    stock footage/music, FFmpeg-based automation) — source material exists in
    `_source/Making YouTube Videos Cheaply with Online Tools.docx`.
  - *Build*: channel strategy, including running a second channel and what
    that does and doesn't allow — source material exists in
    `_source/YouTube Tricks (chat transcript).docx`.
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

Match the Markdown conventions established in the sibling KDP book, *How to
Publish and Make Good Money* (same repo, its own CLAUDE.md documents these
for that book). Use the same set here so both books convert the same way if
either is ever assembled into a Word/EPUB deliverable:

- `# ` — book title (once) and Part-level headings, if this book ends up
  using Parts.
- `## Chapter N: Title` — chapter headings.
- `### ` / `#### ` — sections and subsections within a chapter.
- `> **Key takeaway:** …` — a chapter's summary-style callout.
- `> Worked example. …` — a numbers-shown worked calculation.
- `> Case study: …` — a real, generic-but-true illustrative example (never
  identifying another book in this account's catalog by name or inferable
  detail — that rule applies account-wide, not just to the KDP book).
- `![figure](../figures/fileName.png)` followed by an italic
  `*Figure N.N — caption.*` line — an embedded chart/diagram.
- `- [ ] item` — a checklist item.

Once this book has enough content (and its own `figures/`), add a checked-in
`build_book.py` that assembles the manuscript into a Word `.docx` the same
way the KDP book's does: plain `python-docx` (no pandoc dependency — not
available in this environment), Heading 1/2 styles set to page-break-before
so chapters start a fresh page, real clickable hyperlinks for inline links,
and GFM tables rendered as real Word tables.

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
