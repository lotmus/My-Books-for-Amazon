# Book Writer User Manual

Book Writer is a small, standalone Windows desktop app with two jobs, one per tab:

- **Write a Book** — plan and write a full-length fiction or non-fiction book automatically from
  a title, genre and one-paragraph premise (or from a single starter sentence), then generate
  KDP-sized cover art and export the manuscript as EPUB, Word (.docx) or PDF.
- **Edit a Manuscript** — open an existing manuscript (`.txt`, `.md` or `.docx`) and run
  editorial passes over it: fix bugs, sharpen humor, check the science, add internal and
  external hyperlinks, and tighten the storytelling — chapter by chapter, or the whole book at
  once — then export it the same way.

It was originally a "Book Writer" workspace inside MediaStar.GPT (a video-editing suite) and was
split out into its own app on 2026-09-06, since writing books has nothing to do with editing
video.

## Setting up API keys

Book Writer needs at least one AI provider key to write or edit anything; without one, the Write
tab still runs (every book comes back as a single honest placeholder chapter) and the Edit tab
loads manuscripts but greys out its edit buttons.

1. Copy `config/asset_api.ini.example` to `config/asset_api.ini` (this file is gitignored --
   your real keys never get committed).
2. Fill in whichever of these you have:
   - `anthropic_key` -- Claude, tried first for outline planning, chapter prose and editing.
   - `openai_key` -- OpenAI, a fallback for planning/prose/editing, and the first tier for cover
     art.
   - `gemini_key` -- Gemini, a prose/editing fallback tier, and a cover-art fallback tier.
   - `xai_key` -- Grok, a prose/editing fallback tier.
   - `yandex_api_key` + `yandex_folder_id` -- YandexGPT/YandexART, the last fallback tier for
     planning, prose, editing and cover art. Both must be set together.

You don't need all of them. Each tier is skipped when its key is blank, and every AI call falls
through its configured tiers in order, ending in an honest placeholder or error rather than a
crash if every configured tier fails.

If you already run MediaStar.GPT and have an `asset_api.ini` there, copy the matching lines
straight across -- both apps use the same key names.

## Writing a book

### Starting from a single prompt (optional)

At the top of the **Write a Book** tab is a **Starter prompt** box. Type one or two sentences
describing the book you want -- *"a cosy mystery in a lighthouse, narrator is the new keeper"*,
*"an introduction to tide pools for curious ten-year-olds"* -- and click **Draft setup from
prompt**. Book Writer fills in the Title, Genre, Premise and Chapters fields below with a first
draft. **Every field stays editable** -- change anything before you write. You can also ignore
the starter entirely and fill the Setup fields in by hand.

### Setup and Write

1. Under **Setup**, set a **Title**, pick a **Genre**, set the number of **Chapters**, and
   write a one-paragraph **Premise**.
   - **Fiction** and **Fiction + Science Appendix** carry a "story bible" (characters, setting,
     plot arc) into every chapter so continuity holds. **Fiction + Science Appendix**
     additionally reserves the last chapters as `Appendix:` science explainers about the real
     science behind the story.
   - **Non-Fiction** has no story bible -- each chapter is a self-contained sub-topic.
2. Click **Write Book**. This runs in two phases, fully automatically, with no per-chapter
   review checkpoint:
   - **Outline planning** (one AI call): every chapter's title and a 2-3 sentence summary,
     plus the story bible for the fiction genres.
   - **Chapter writing** (one AI call per chapter): each chapter is written by a separate call
     that sees the whole outline (not the other chapters' prose), so continuity holds.
3. **Cancel** stops a write in progress; whatever's already written stays.
4. A chapter whose every provider tier failed becomes an honest placeholder (starting
   `[This chapter could not be generated: ...]`) explaining why, rather than losing the rest of
   the book -- marked with a `⚠` in the chapter list. See **Retrying a chapter** below to fix it
   without rewriting the whole book.
5. Click a chapter on the left to read it on the right.

### Exam Prep Course genre

Choosing **Exam Prep Course** plans the book as a self-paced course (Strategy, Lesson, Practice and
Appendix units, each with "Praxis Tips") and bakes copyright-safety rules into every outline,
chapter and edit call: no released-exam or commercial prep-book content, original or openly
licensed passages only, no invented citations, and `[VERIFY]` flags for facts a human expert must
check. Chapter titles use the prefixes `Strategy:`, `Lesson N:`, `Practice:` and `Appendix:`. See
`Exam Prep Course Manual.md` in the repository root for the full workflow. AI-written science and
answer keys must be verified by a qualified person before you publish.

### Retrying a chapter

If one or more chapters failed (or you just want a fresh take on one), you don't have to
regenerate the whole book:

- **Retry This Chapter** -- regenerates only the chapter currently selected in the list.
- **Retry All Failed** -- regenerates every chapter still showing its failure placeholder, in
  order, skipping every chapter that already has real text.

Both buttons are enabled once a book exists; a retry runs the same chapter-writing call as the
original Write Book pass and replaces that chapter's text in place, live-updating the chapter
list, the reading pane and the cover/export panel when it finishes.

### Saving and loading your work

A written (or in-progress) book no longer has to live only in memory:

- **Save Project...** saves the current title, genre, premise, story bible, full outline and
  every chapter's text (including cover art path, if generated) to one `.bookproject.json` file
  you choose. Enabled once a book exists.
- **Load Project...** opens a previously saved `.bookproject.json`, filling in Setup and the
  chapter list exactly as they were, ready to keep writing, retry a chapter, edit, or export.

Both remember the last folder you used for project files, separately from the export folder.

## Editing an existing manuscript

The **Edit a Manuscript** tab works on any book -- one you wrote here, or one from anywhere
else.

1. Pick a **Genre** (it affects how the editor treats the text and the exported book's
   subject), then click **Open Manuscript...** and choose a `.txt`, `.md` or `.docx` file.
   Book Writer splits it into chapters on its headings:
   - Markdown `#`/`##` headings, "Chapter N" / "Part N" lines, `Prologue`/`Epilogue`/etc.,
     numbered `1.` headings, `===` underlines, and Word's built-in Title/Heading styles are all
     recognised.
   - If it finds no headings at all, the whole file becomes one chapter -- still fully
     editable. Nothing in the text is ever dropped.
   - A `.docx`'s bold, italic, and bold+italic runs are preserved on import (re-encoded the same
     way the Hyperlinks edit pass and a `.md` import already represent them), as are external
     hyperlinks on real Word hyperlink runs. Formatting that comes from a character/paragraph
     style rather than a direct bold/italic toggle, and a hyperlink whose target can't be
     represented safely, fall back to plain (never dropped) text. Markdown links and emphasis in
     a `.md` file are kept and rendered on export the same way.
2. Tick the **Editorial passes** you want:
   - **Bugs & errors** -- typos, grammar, punctuation, continuity slips, wrong facts.
   - **Humor** -- sharpen wit and comic timing where it fits the voice.
   - **Science accuracy** -- check and correct every scientific/technical claim.
   - **Hyperlinks** -- add internal cross-references to other chapters (`chapter:N` links) and
     external links to authoritative sources, in Markdown syntax.
   - **Storytelling** -- pacing, tension, hooks, show-don't-tell, cut filler.
   All ticked passes run together in one call per chapter (a 3-pass edit is one call, not
   three). Optionally add **Editor notes** -- anything specific you want watched for.
3. Click **Edit This Chapter** (the selected one) or **Edit All Chapters** (every chapter, with
   progress; cancellable). Edits apply straight to the working copy.
4. Review: the right side shows **Original (as imported)** next to **Current**, plus the
   **Editor's log** for that chapter (a short bullet list of what changed and why). A `✎` marks
   edited chapters in the list.
5. **Revert This Chapter** / **Revert All** restore the imported text. Editing again always
   starts from the current text, so you can layer passes.
6. Generate cover art and export exactly as on the Write tab.

## Customizing fonts and colors

Above Cover Art and Export on either tab is a **Style** panel, applied at export time:

- **Headings** -- font name, an optional hex color (blank keeps the default), and a **Bold**
  checkbox (on by default).
- **Body text** -- the same three controls, independently (**Bold** off by default).

The font name falls back through a short chain of common alternatives if the exact name isn't
available on the machine opening the file (e.g. a Georgia heading falls back to Cambria, then
Times New Roman), so a chosen look survives on a reader's device even without that exact font
installed. A link's own color always overrides a chosen body color, so links still read as links.

## Generating cover art

On either tab, once a book is loaded, click **Generate Cover Art**. This produces a KDP-sized
(1600x2560) illustration with the book's title overlaid, tried across up to three AI image
providers (OpenAI images, Gemini, YandexART, in that order) with a real ffmpeg finishing pass.
The status line always explains the real outcome.

Cover art needs a real `ffmpeg.exe` at `Tools\ffmpeg.exe` under this app's own folder -- if it's
missing, generation fails with an honest error naming that path.

## Exporting your book

Three independent export buttons, each enabled once a book is loaded:

- **Export as EPUB...** -- a real, valid EPUB 3 file (chapters, table of contents, cover image
  if one was generated, `dc:subject` from the genre).
- **Export as Word (.docx)...** -- a Word document with real Title/Heading1 styles per chapter,
  plus a real Table of Contents field (right-click it and choose **Update Field**, or press F9,
  to build it) driven off those same heading styles -- so Word's own Navigation Pane shows the
  full outline too. A chapter paragraph that is a single `**bold**` line on its own becomes a
  real Heading2 sub-heading, one level under that chapter's title, in both places.
- **Export as PDF...** -- a 6x9-inch print-trim PDF, same chapter structure.

**Hyperlinks** added by the Hyperlinks edit pass (or already present in an imported `.md`) are
rendered as real links in every format:

- **EPUB / Word** -- both internal (`[text](chapter:N)`) and external
  (`[text](https://...)`) links are clickable. Internal links jump to that chapter; a link to a
  chapter number outside the exported book is shown as plain text rather than a dead link.
- **PDF** -- external links are clickable; internal chapter links are clickable
  section jumps.

`**bold**` and `*italic*` in chapter text are rendered too. Other Markdown (headings, lists,
block quotes) is left as literal text -- Book Writer's chapter model is plain prose plus inline
links and emphasis, nothing heavier.

Each export opens a normal Save dialog defaulting to `Exports\Books` under this app's own folder,
remembers the last folder used, and reports the real outcome -- including a partially-written
book, which still exports but says so.

## Where things live

Book Writer is a fixed local install at `D:\My_C#_Apps\Book Writer`:

- `config\asset_api.ini` -- your API keys (gitignored, never committed).
- `Tools\ffmpeg.exe` -- bundled locally, not committed (copy your own `ffmpeg.exe` here if
  missing).
- `Exports\Books\` -- where exported EPUB/Word/PDF files default to.
- `%LocalAppData%\BookWriter\logs\` -- daily log files.
- `%LocalAppData%\BookWriter\recent-folders.json` -- remembers your last import/export folders.
- `%TEMP%\BookWriter\` -- scratch files used while generating cover art.

## Known limits

- **The editor sees one chapter at a time** plus the list of every chapter's title -- enough for
  continuity checks and `chapter:N` links, but it does not re-read a neighbouring chapter's full
  prose while editing.
- **External links are the model's best effort.** The Hyperlinks pass is told to only link
  stable, authoritative pages and never to guess a URL, but it can still be wrong -- check the
  links it adds before publishing.
- Cover art is a single generated image per book, not multiple variants to choose between.
