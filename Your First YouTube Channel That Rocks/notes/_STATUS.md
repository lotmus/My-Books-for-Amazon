# STATUS — Your First YouTube Channel That Rocks

## Current state

**Update 2026-10-02 (refocus, supersedes everything below where it disagrees):** Lothar asked for the book to drop everything about selling (one offer, prices, checkout pages, selling videos or books through the channel) and to be about monetizing the channel itself. Title changed to *Your First YouTube Channel That Rocks*, subtitle “Grow Watch Time and Subscribers, Reach the Partner Program, and Earn From Ads, Fans, and Sponsors”; folder and master renamed with `git mv`. Fifteen chapters now (list in `CLAUDE.md`). New chapters: Name the Viewer, Eight Videos Each With One Job, Six Weeks to a Working Channel, Grow Toward the Gate, The Gates and the Review, Ads RPM and the Shorts Pool, Money From the People Who Watch, Sponsors and Affiliate Links, Keep It Paying; rewritten: Read the Count, The Channel Workbook (absorbs the old *Say This* templates); edited: click, production, recording, and rules chapters (rules chapter renamed The Rules That Can Switch Off the Money; adds limited ads and the monetization policies). Retired: Sell One Thing, The Videos That Do the Selling, Where the Money Actually Comes From (split into chapters 8, 9, 13, 14), Six Weeks to a Live Offer, Say This, When Nothing Sells (folded into chapter 14). Abdaal case study dropped (it was about selling a course). Figure 3.1 banner now says “not permission to monetize the result”. New monetization facts checked on YouTube Help/Blog on 2 October 2026 (RPM/CPM, mid-rolls at 8 minutes, Shorts Creator Pool 45% and the 2027 10M floor, Premium/Premium Lite pools, 70% fan-funding shares, membership levels and banned perks, Super Thanks exclusions, Creator Partnerships, Shopping affiliate at 500 subscribers since March 2026). Removed text and originals: `D:\bak\2026-10-02 YouTube book refocus\`. KDP description rewritten. Words (builder count) 29,375 → see commit message.


Last updated: 2026-10-01 — nine chapters, order fixed in `build_docx.py`. The only video load is the eight jobs: four of them have to be long videos (who, problem, method, offer), and the offer is never only a Short. One URL, repeated in the description, the pinned comment, and one profile slot. A subscribe-prompt URL stays out of those three slots. Week two publishes “who” and the offer before the other six, on purpose. The videos chapter says that pair is filming order and the numbered list is watch order. Week five’s path video is the order a stranger should watch, and that video may be a Short. A subscribe line is not spoken in the same breath as the price. The $200 figure is the offer video alone. The other seven videos’ hours go on the money sheet before week six. “Send ten” applies to a thing you ship. A call is judged by the sales that cover the hours. The production figure shows the default stack. Generators are the side door. Brownlee, Rea, and Hart are the film-first path the book declines. Abdaal is the early price on a page you control. Pull request #36 is already merged. Where an older note says the book is three chapters or that chapter order is open, this section wins.

**Update 2026-10-01 (later session):** three chapters appended after chapter 9, without renumbering 1–9: *Record It So They Stay* (scripting for the ear, the 30-second opening, phone audio, light/framing, screen recording, cutting for pace, video chapters, end screens), *Read the Count* (Studio vs. page vs. payment counts, utm link tags as labels on the one URL, impressions/CTR with YouTube’s own 2–10% band and caveats, traffic sources incl. search terms card, retention at the moment the price is said, the 24 Aug 2026 view-counting change), and *The Rules That Can Close the Shop* (warnings/strikes/copyright strikes/Content ID claims, spam/fake-engagement/external-links policies, paid promotion box, AI-use disclosure incl. May 2026 auto-labels, made for kids, license/disclosure/notice logs). Every platform fact is cited to a YouTube help page or blog post checked October 2026. `build_docx.py`: ORDER, START, SOURCES, and GLOSSARY extended; also fixed two builder bugs that printed raw markdown (links inside italic source paragraphs, and links inside bold). Still open: real case-study research pass (open question 3).

**Update 2026-10-01, 19:30 PT (audit session):** facts rechecked on YouTube Help and the YouTube Blog on 1 October 2026. Chapter 5 now states the Partner Program changes that start 1 February 2027 (new-applicant ad gate 8,000 hours or 20M Shorts views; Shorts Creator Pool needs 10M qualified Shorts views in 90 days each month; 55% long-form / 45% Shorts shares; the new activity definition; accept terms by 31 January 2027). Chapter 12 adds what the AI disclosure page now lists (AI music needs it, own-voice clones and AI thumbnails do not, auto-labels via C2PA, penalties for repeated non-disclosure) and the inauthentic-content and AI-persona monetization rules. Chapter 3 points generated music at the AI use setting. Glossary: two new terms, three updated. KDP listing draft: `KDP_Description.md`. Superseded build `…before-more-chapters-20261001-1545.docx`, `_patch_build.py` and `__pycache__` moved to `bak\`. Words 28,520 → 29,363 (body paragraphs).

## History

Last updated: 2026-09-28 (session 2) — **all three planned chapters now drafted, audited, open as a draft PR**

Post-draft audit (session 2) checked all three chapters for: leaked
personal-project terms (clean), balanced markdown tables/links (clean,
one false alarm on my own miscount), and house style. Found and fixed two
real issues: the Build chapter's platform table named seven platforms with
no hyperlinks, inconsistent with the book's link convention (fixed —
added real URLs, only where a search had actually returned one); and all
three chapters, including the already-merged chapter 1, used straight
quotes/apostrophes rather than the curly ones `CLAUDE.md` specifies
(fixed — converted uniformly, including one instance inside
`figures/follower-floor.svg`'s own visible text). PR #36 is currently
clean: mergeable, no CI configured in this repo, no reviews or comments
yet.

## Where this stands

This is a new, separate companion book to *Your First Book That Sells*,
started in session 1. Its title deliberately echoes the Kindle book's, with
"YouTube" kept explicit in the title itself for the same reason a book's
title needs its keyword — search discoverability, on Amazon and on YouTube's
own search once discussed in the book.

Current contents:
- `manuscript/The Click Is the Whole Business.md` — one chapter (~1,900
  words) covering the title/description/tag character limits, why some
  emotionally accurate tags trigger a content-safety category, captions and
  subtitles (viewer controls and the creator upload workflow), retention as
  an unpublished but widely-believed ranking signal, and a Shorts-to-long-form
  posting rhythm.
- `manuscript/Nobody Can Tell What It Cost.md` — the *Create* chapter
  (session 2), on making videos cheaply: AI text-to-video generation, free
  stock-footage/photo libraries with a license/attribution table, free music
  and sound libraries plus mixing ratios, text-to-speech/transcription and a
  hard line on voice-cloning consent, free browser editors and FFmpeg, and a
  closing section on the one production workflow (fully original text, voice,
  and visuals) that never needs a rights check. Opens as a draft PR, not yet
  merged — see below.
- `figures/free-production-pipeline.svg` — a colorful five-stage diagram
  summarizing that chapter, used as its opening visual.
- `manuscript/Where the Money Actually Comes From.md` — the *Build* chapter
  (session 2): YouTube's own two-tier Partner Program thresholds and the
  tactics that actually move subscriber/watch-hour numbers, the second-
  channel-starts-at-zero point (from `_source/YouTube Tricks`), a table and
  chart comparing monetization programs across eight other platforms
  (TikTok, Facebook, Snapchat, X, Rumble, Dailymotion, Instagram, Vimeo,
  Tumblr) with current figures verified via live web search, and affiliate
  links as a revenue stream independent of any one platform's program.
  Notes candidly that two of those programs (Facebook's, X's) were replaced
  entirely within the months before this chapter was written, and that
  Vimeo's On Demand marketplace is being shut down outright — used as the
  chapter's own argument for verifying every number before relying on it.
- `figures/follower-floor.svg` — a bar chart (YouTube highlighted against
  the rest) comparing the follower/subscriber floor across platforms,
  built following the repo-wide dataviz skill (validated palette, emphasis
  form).
- `_source/` — six files (see below for what each actually is). Four are
  from session 1; two more (general free-media/stock-site lists) were added
  in session 2. A much larger batch of files uploaded mid-session-2 was
  *not* added here — see "Session 2: a large uploaded-file batch" below for
  why.
- `CLAUDE.md` — scope, project facts, and house style.

## What's actually in `_source/` — read this before using any of it

- `Making YouTube Videos Cheaply with Online Tools.docx` — a raw bookmark
  list of AI video/image/audio tools and free-stock-media sites, in the
  author's own words. Reusable as-is for research; not written prose.
- `YouTube Tricks (chat transcript).docx` — a short saved chat transcript
  (a different AI assistant) answering one question: can you run a second,
  minimal YouTube channel to redirect traffic, and what does the platform
  allow. General and reusable.
- `YouTube Tips (chat transcript).docx` — **not general teaching material.**
  This is a saved chat transcript of a different AI doing hands-on production
  work for the author's own separate, real video project: a finance/real-estate
  explainer (topic: Home Equity Investments, a named company, two named
  cartoon characters). It contains that project's actual titles, tags,
  thumbnail text, pinned comments, and a 30-day content calendar — none of it
  general-audience teaching content, all of it that specific project's actual
  production assets.
- `Captions and Subtitles (pasted chat content).md` — a pasted answer (same
  kind of source as above) on how caption/subtitle controls and the Studio
  upload workflow work. General and reusable; the content itself is ordinary,
  checkable interface behavior.
- `Free Media (curated shortlist).txt` and `More Free Stock Video and Music
  URLs (pasted chat content).txt` — added session 2. Both are plain lists of
  free/CC-licensed stock-footage and music sites (Pexels, Pixabay, Mixkit,
  Videvo, Life of Vids, Mazwai, Dareful, Uppbeat, Jamendo, Purple Planet
  Music, and others), same kind of source as the bookmark list above.
  General and reusable; several entries are already cited in the *Create*
  chapter's footage/music tables.

## The incident this session's CLAUDE.md rule comes from

The first draft of `manuscript/The Click Is the Whole Business.md` extracted
the *general* principle from `YouTube Tips.docx` correctly (some emotionally
accurate tags trigger a content-safety category; describe the specific
situation instead of the crisis word for it) but illustrated it with that
project's own replacement tags ("struggling homeowner," "cash flow
problems") — not the brand names or characters, but still that specific
project's actual wording, re-purposed as if it were a generic example. The
author caught this and asked for it to not be used at all; the chapter was
rewritten with an unrelated illustrative domain (fitness) instead, and the
rest of `YouTube Tips.docx` was mined only for the transferable structure —
the title formula, the character-limit table, retention and posting-cadence
claims (all labeled as creator consensus, not published fact) — never its
specific example content.

## Session 2: a large uploaded-file batch, and how it was sorted

Mid-session, the author uploaded roughly 20 files with no accompanying
instructions at first, just filenames. Several were immediately recognizable
as the same kind of thing `_STATUS.md` already warns about: real, specific
personal video projects of the author's own, not general teaching material.
Notably:

- `Song_Video_Creation_MANUAL.docx` and `Song_Vidseo_Creation_Info_dump.docx`
  — a personalized "Singsang Production Pipeline" for AI-generated novelty
  song videos, with the author's own recurring bits (chickens, Beyoncé jokes),
  specific tool commitments and prices ("Pika... $10/month... perfect for
  your 200-scene/month singer closeups"), and deep AI-vocal-tuning specifics
  tied to that workflow. Not used at all — narrow to that project and outside
  this book's scope besides.
- `Sound_effects_&_music_plan_.docx` and `Export_settings_for_YouTube.docx`
  — both explicitly built "for your HEI cartoon explainer style," the *same*
  Home Equity Investments / Hometap / named-cartoon-characters project the
  original incident (above) already excluded, just surfacing again from a
  different saved chat. Every scene description, tag, and character reference
  in both was left out. What *was* general and checkable — audio-mixing
  volume ratios, the micro-pause-before-a-punchline technique, and standard
  YouTube export settings (resolution, frame rate, codec, bitrate, audio
  settings) — was extracted with no reference to that project and folded into
  the new chapter.
- `Teach_German_with_comic-style_news_with_own_text.docx` and
  `Stummfilm_Workflow.docx` — read but not used: each reads as a distinct
  personal channel concept of the author's (a German-vocabulary comic-news
  format, a silent-film restoration workflow), not general craft, and neither
  fits an already-planned chapter. Left alone.
- `TTS_-_The_Alien_Genius_of_the_Ocean_-_Octopus.txt` — a finished script for
  what reads as the author's own actual, existing channel ("Planetary
  Knowledge Hub"). Specific real content, not general teaching material —
  excluded the same way the HEI and Singsang material was.

**Two files were excluded for a different reason, and it's worth being
explicit about it rather than filing them next to the merely off-topic
ones.** `Style_Deadpan_cinematic_surreal.txt` is an AI-video prompt built
around a real, named actor's likeness in an invented scene. `high_quality_
clear_cinematic._she.txt` is an explicit sexual AI-image/video prompt, one
variant of which names a real public figure's likeness in a fabricated
sexual scenario. A third file, `workable_free_versions.txt`, otherwise a
normal tool bookmark list, contained one line in the same category (making
a real political figure appear to say fabricated things) that was cut before
anything else in that file was used. None of the three were summarized,
referenced, or mined for "general technique" — a real person's likeness used
without consent isn't a scope problem the way the channel-specific files
above are; it's excluded outright, regardless of context. If either of the
first two files resurfaces in a future session, treat them the same way.

Other files in the same batch were general and safe to use the same way the
original `_source/` bookmark list was — free-media site lists (expanding the
footage and music tables; the two source files are now in `_source/` — see
above), a note on 100%-free-forever AI video tools, more free/near-free AI
avatar and text-to-video tools with their free-tier limits (from the
sanitized remainder of `workable_free_versions.txt`), a note on
TTS/faceless-channel voice options, and a general chat answer on the
copyright-safe "rewrite it yourself" workflow. These were mined for
technique only, per the author's explicit instruction ("incorporate anything
useful in general ways, not examples") — no scripts, character names, niche
ideas, or pricing decisions from any of these files made it into the
manuscript. Other than the two free-media files, none of the ~20 uploaded
files were copied into this repo's `_source/`; the rest only exist in the
chat upload area, and given what turned up in this batch, nothing further
should be copied in without the same read-first triage this batch got.

Two files in the batch were unrelated to this book entirely: a duplicate of
a decades-old, public Microsoft Knowledge Base article on Visual Basic 6
performance, and several YouTube-growth/monetization files (subscriber-
conversion CTAs, affiliate-link placement, a "second channel" YPP-monetization
caveat) that are legitimate general material but belong in the *Build*
chapter, not the just-drafted *Create* chapter — held for later rather than
used now.

## Open questions for the author

1. **Chapter order is fixed** as of 30 September 2026. See the list at the
   top of this file and `build_docx.py`. "The Click Is the Whole Business"
   was written first; it is chapter 2.
2. **The *Build* chapter is now written** (`Where the Money Actually Comes
   From.md`), using the `YouTube Tricks` transcript, the vetted subscriber-
   conversion and affiliate-link material, and the second-channel-
   monetization drawback the author flagged mid-session-2 — all as planned.
   It also grew beyond the original scope into a cross-platform monetization
   comparison (TikTok, Facebook, Snapchat, X, Rumble, Dailymotion, Instagram,
   Vimeo, Tumblr), per the author's session-2 request to expand into "other
   potential places to earn with videos." Worth the author's review
   specifically for accuracy — the platform figures move fast enough that
   two cited programs changed entirely in the weeks around when this chapter
   was drafted, and Dailymotion's own requirements could not be confirmed to
   the same standard as the others (flagged in the chapter's own text).
3. **No case studies exist in this book yet.** The Kindle book leans heavily
   on named, checkable creator case studies; this book doesn't have any yet
   because no session has done that research pass. Worth doing before this
   book is called complete.
4. Author confirmed same pen name (Kevin Drew Peters) applies here; not
   independently reconfirmed for this specific book, carried over from the
   Kindle book's session.
5. Author confirmed (session 2) that this book should match the Kindle
   book's choice of visible, non-cloaked inline hyperlinks and colorful
   workflow diagrams — now used in the *Create* chapter.

## 1 October 2026, evening

- Author set to Lothar J. Musiol on the title page, a new copyright line, and the docx properties (was the pen name Kevin Drew Peters).
- 2026/2027 YouTube Partner Program facts rechecked against YouTube Help and the YouTube blog on 1 October 2026: current gate 1,000 subscribers + 4,000 long-form watch hours in 12 months or 10 million Shorts views in 90 days; from 1 February 2027 new applicants need 8,000 hours or 20 million Shorts views; Shorts revenue sharing from February 2027 needs 10 million Shorts views in the prior 90 days; fan-funding gate (500 subscribers, 3 uploads in 90 days, 3,000 hours or 3 million Shorts views) unchanged; updated terms to accept by 31 January 2027. Chapter 5 already matched; no text change needed.
- Companion book is now the single merged *Your First Book That Sells* (32 chapters). This book stays separate.

