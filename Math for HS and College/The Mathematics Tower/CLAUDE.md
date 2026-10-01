# The Mathematics Tower — working instructions

This repository holds the manuscripts of *The Mathematics Tower* (Volumes 1–4)
and their derived editions. Read this before editing anything.

What the four volumes contain, and the house facts every volume shares, is in
`Tower - Series Reference.md`. Cite floors from that file. Do not keep a second
copy of the floor map here.

---

## 1. How to write — the didactic contract

**`Tower - Didactic Style Guide.md`, in this folder, is the authority on how any
new idea is introduced. Read it in full before writing or rewriting prose, and
follow it.** It is not a suggestion; it is the house method, and the book's
teaching quality depends on it.

The single sentence it rests on:

> **Never define a thing before the reader has felt the need for it, and never use
> a symbol before the arithmetic has already made the point.**

**Who the reader is — formally an equal, in practice somebody who does not yet
know anything.** Tone treats them as an intelligent adult; pace assumes nothing
has been met before. These do not conflict: respect is tone, slowness is pace.

Everything in these books is hard to understand without a long run-up, so give
one. The writer already understands the material and therefore cannot feel where
it is hard — the sense that *this is surely enough introduction* is the opinion
of the one person who cannot be confused by it. So work by rule instead:

- If a passage feels slightly too slow to you, it is about right. If it feels
  exactly right, it is already too fast.
- Assume more introduction than seems necessary. The on-ramps that work run
  380–660 words before the formal statement.
- One new idea per paragraph wherever it is hard.
- Nothing assumed in silence: every term is built here, built earlier, or
  signposted as coming later. When you write *recall that*, check it was ever
  actually said.
- "Equal" rules out the dismissiveness, never the explaining. No *as you know*,
  no *needless to say*, and no apologising for going slowly.

Being told something you already knew costs a reader four seconds. Being hurried
past something you did not know costs them the chapter.

The seven moves, in order, for the first encounter with any genuinely new object:

1. **Start from something the reader already owns** — a road sign's gradient, a
   rectangle's area. Could a reader who skipped the previous floors follow the
   first paragraph?
2. **Let the familiar thing break** — visibly, not by assertion. This creates the
   need; machinery introduced before the need reads as arbitrary.
3. **Change the question out loud**, in one short sentence. It is the hinge.
4. **State the obstacle so it can be felt** — "the run is zero and the climb is
   zero, and zero divided by zero tells you precisely nothing." The most-skipped
   move, and skipping it is why limits read as ritual rather than rescue.
5. **Offer the trick, admitting it looks like cheating.**
6. **Numbers before symbols** — a short table the reader can check by hand — and
   then say plainly **what the numbers never do**. Concealing non-attainment is a
   false economy that costs you at every later ε–δ argument.
7. **Name it only once it exists, then translate the reader's own notation**
   (Δy/Δx ↔ the book's *h*).

Structural rule: **the informal table and the formal derivation must share an
example and reach the same number.** Room 11.1's on-ramp lands on 6 because 11.2
derives 6; Room 12.1's lands on 3.75 because 12.2's figure already shows 3.75.
When writing a new on-ramp, work backwards from what the next room derives.

Use all seven moves only for a genuinely new kind of object. Technique rooms need
moves 6 and 7 only. "Looking Ahead" rooms are inventories by design.

Two standing cautions:

- **Banned at a hinge:** *clearly, obviously, simply, just, of course, it is easy
  to see.* Each tells a struggling reader the fault is theirs.
- **Parallelism is an asset, not repetition to be edited out.** "A positive
  discriminant means… a negative discriminant means…" is doing work. Only remove a
  repeated word when it carries two *different* senses with no parallel structure
  to justify the echo.

---

## 2. House style

House style — American English, curly quotes, spaced em dashes, a proper minus,
the author, and the words Floor, Room, and Tower — is in
`Tower - Series Reference.md`. Follow that file.

---

## 3. How to edit a .docx safely

The manuscripts are Word files; edits are made to `word/document.xml` inside the
zip. Hard-won rules:

- **Word enforces child order.** In `w:pPr`: … spacing, ind, **jc**, …, outlineLvl.
  In `w:rPr`: **rFonts**, b, color, sz, szCs. Out-of-order children make Word
  refuse the file.
- **Text is split across `w:r` runs.** A string that appears literally in
  `document.xml` is necessarily inside one `w:t`, so a plain replace is safe. If it
  does not appear, it spans runs and needs a run-aware edit.
- **Paragraphs containing hyperlinked cross-references cannot be rebuilt
  wholesale** — the book has ~818 hyperlinks and 700 `Room X.Y` references, and
  flattening a paragraph to one run destroys them.
- **Prefer styles.xml to touching paragraphs.** Restyling 180 headings is one edit
  there, and safe only when no paragraph carries direct formatting — check first.
- **Verify after every write, before replacing the live file:** `testzip()` clean,
  entry list unchanged, media count unchanged, `document.xml` parses, and every
  replaced image still decodes. Picture counts are in
  `Tower - Series Reference.md`.
- **Verify arithmetic exactly** — as fractions, never floating point. Every table
  in the book should be reproducible by a reader with a pencil.

## 4. Project facts

- **The .docx is the only deliverable. Do not build or rebuild EPUB or PDF, and
  do not offer to.** This is settled; treat it as standing.
- The `.epub` and `.pdf` files sitting beside the manuscripts are **stale and
  superseded** — they predate corrections that are in the .docx. Leave them
  alone, and do not publish from them.
- **Sessions are scoped per volume.** Do not edit other volumes unless asked.
- **Several sessions edit this repo concurrently.** Re-read the file and the git
  log before writing; do not trust a status snapshot from the start of a
  conversation.
- Backups live in `Archive - not for publication`.

## 5. Where things live

The floor map, the room pattern, and the citations that are easy to get wrong
are in `Tower - Series Reference.md`. That file also records the Floor 18
bookmark names. Leave them as they are.
