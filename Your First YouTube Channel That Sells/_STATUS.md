# STATUS — Your First YouTube Channel That Sells

Last updated: 2026-09-28 (session 2) — **second chapter drafted, open as a draft PR**

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
- `_source/` — four author-uploaded files (see below for what each actually
  is). A much larger batch of files uploaded mid-session-2 was *not* added
  here — see "Session 2: a large uploaded-file batch" below for why.
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
- `Teach_German_with_comic-style_news_with_own_text.docx`,
  `Stummfilm_Workflow.docx`, and `Style_Deadpan_cinematic_surreal.txt` —
  read but not used: each reads as a distinct personal channel concept of the
  author's (a German-vocabulary comic-news format, a silent-film restoration
  workflow, a visual style guide), not general craft, and none fit an
  already-planned chapter. Left alone.

Other files in the same batch were general and safe to use the same way the
original `_source/` bookmark list was — free-media site lists (expanding the
footage and music tables), a note on 100%-free-forever AI video tools, a
note on TTS/faceless-channel voice options, and a general chat answer on the
copyright-safe "rewrite it yourself" workflow. These were mined for
technique only, per the author's explicit instruction ("incorporate anything
useful in general ways, not examples") — no scripts, character names, niche
ideas, or pricing decisions from any of these files made it into the
manuscript. None of the ~20 uploaded files were copied into this repo's
`_source/`; they only exist in the chat upload area. Worth asking the author
whether the two generic free-media-list files specifically are worth adding
to `_source/` for future reference.

Two files in the batch were unrelated to this book entirely: a duplicate of
a decades-old, public Microsoft Knowledge Base article on Visual Basic 6
performance, and several YouTube-growth/monetization files (subscriber-
conversion CTAs, affiliate-link placement, a "second channel" YPP-monetization
caveat) that are legitimate general material but belong in the *Build*
chapter, not the just-drafted *Create* chapter — held for later rather than
used now.

## Open questions for the author

1. **Chapter order isn't fixed.** "The Click Is the Whole Business" was
   written first because the character-limit facts were handed over directly
   and needed no research; it doesn't have to be chapter one.
2. **The *Build* chapter still isn't written**, and now has more source
   material queued for it than originally planned: the `YouTube Tricks`
   transcript (second-channel redirect rules), plus the subscriber-conversion,
   affiliate-link, and second-channel-monetization material identified above.
   Also queued: the drawback the author flagged mid-session-2 — each
   additional channel has to separately clear YouTube Partner Program's own
   monetization thresholds; a redirect/placeholder channel doesn't inherit
   the main channel's monetized status.
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
