# STATUS — Your First Book That Sells

Last updated: 2026-09-28 (session 2) — **REV3 folded in; title and author confirmed**

## Where this stands

This book did not exist in the repo before session 1. It exists locally at
`C:\Users\lomus\OneDrive\My Books for Amazon\Your First Book That Sells` on the
author's PC, which cloud sessions cannot reach — everything here was built
from `.docx` files the author uploaded directly into chat, across two sessions.

The author has since confirmed, directly in chat: the **book's title is
"Your First Book That Sells"**, and it is published under the **pen name
Kevin Drew Peters** — a deliberate departure from this repo's usual author
(Lothar J. Musiol). See `CLAUDE.md` for the corrected project facts.

Current contents:
- `manuscript/The First-Review Problem.md` — one chapter, ~4,200 words, covering
  why review count and price determine whether a debut Kindle book converts,
  KDP's 70%/35% royalty bands, how to price a standalone vs. a series, who is
  actually eligible to post an Amazon review, Goodreads' separate rules, a
  legal ARC (advance reader copy) pipeline including EPUB delivery and where to
  recruit readers with no existing list, and named case studies.
- `_source/The First-Review Problem (REV1).docx`, `(REV2).docx`, and `(REV3).docx`
  — the author's three original uploads, kept verbatim for provenance.
- `CLAUDE.md` — scope and the house style observed in that one chapter.

## What happened to REV1 vs. REV2

REV2 is a clean superset of REV1: the only content difference is a new
subsection inserted into section VI ("The constraint that keeps the money"),
adding:
- **"Who is allowed to post on Amazon"** — Amazon Community Guidelines require
  $50+ of card spend on that marketplace in the past 12 months before an
  account can leave a rating or review; promo/gift-card spend doesn't count,
  and meeting the bar still isn't the same as a Verified Purchase badge.
- **"Goodreads is a different door"** — no spend minimum there, ratings are
  allowed pre-publication, and advance-copy reviews now carry a source tag
  (author/publisher, Giveaway, NetGalley, other).

`manuscript/The First-Review Problem.md` is built from REV2. Two straight
quote/apostrophe characters that slipped into REV2's new text (inconsistent
with the rest of the chapter's curly-quote typography) were normalized when
transcribing to Markdown. No wording, numbers, or claims were changed
otherwise — this was a typography-only cleanup.

## What happened to REV2 vs. REV3

REV3 is a clean superset of REV2 — purely additive, no deletions, and the
three data tables are byte-for-byte identical to REV2's. Two insertions:

- A new paragraph after the "Convert the Word file to EPUB" line (end of
  section VI), covering the mechanics of emailing an EPUB: it goes to the
  reader's own `@kindle.com` address or opens in the Kindle/Apple Books/Google
  Play Books apps, and BookFunnel/StoryOrigin exist to avoid doing this by hand.
- A new subsection in section VII, **"Who the form is for, and where it goes
  when you have no list"** — two paragraphs on the ARC sign-up form as an
  application (not an open giveaway), and exactly which Facebook groups and
  subreddits (r/ARCReaders, r/AdvanceReaderCopy) to post it in.

Both insertions were already clean of straight quotes, so no typography
normalization was needed this pass. No wording, numbers, or claims were
otherwise changed.

## Open questions for the author

1. **Where does this chapter sit?** There's no outline yet, so the file isn't
   numbered. If more chapters exist locally, the next useful step is getting
   them into this folder (upload them here, or push from the local OneDrive
   folder — see the PR description for git commands) so an outline and
   chapter order can be set.
2. **Is "A working book for authors who want a catalog, not a hobby" the
   book's subtitle**, or just this chapter's running tagline? It's carried
   into the manuscript file as a kicker line above the chapter title either way.
3. No book bible, style guide, or build system exists yet for this title — one
   can be drafted once more chapters (or an intended chapter list) are available,
   following the pattern used by this repo's other multi-chapter books
   (e.g. `Auswandern - Ab in die USA, Kanada, Australien oder Neuseeland/_Konzept/`).
