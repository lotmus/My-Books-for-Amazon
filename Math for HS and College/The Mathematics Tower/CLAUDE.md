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

## 6. Session of 1 Oct 2026 (Volume 2, Floor 15)

One session owns the Tower, RIB Book 1 and Protocol Flamingo, and does no git.
Backup before the edit: `Archive - not for publication\The Mathematics Tower - Volume 2 (backup 2026-10-01, before Floor 15 on-ramps).docx`.

Floor 15 was the thinnest floor and its rooms opened cold with definitions.
Volume 2 went from 175,873 to 178,054 words (body text). Only `word/document.xml`
changed; 107 pictures, 906 hyperlinks and 428 bookmarks are unchanged.

- 15.1: weather-map opening before the definition, bridging from Room 14.4.
- 15.2: full seven-move on-ramp for divergence (shop-door count; boxes around
  (1,1,1) in ⟨x²,y²,z²⟩ give exactly 6; ⟨x³,0,0⟩ at (1,0,0) gives 3 + h²/4:
  3.25, 3.0625, 3.0025, 3.000025, never arriving at 3). Curl on-ramp as
  circulation ÷ area: the rotation field gives 2 for every square, matching
  the room's ⟨0,0,2⟩; ⟨0,x³,0⟩ gives the same table, heading for 3. The formal
  examples that follow reach 6 and 2. "Partial derivatives introduced in the
  last floor" now says Room 13.4 (they are Floor 13, not 14).
- 15.4: work-as-trolley opener (50 J, 25 J at 60°, 0 J), and the hill-climb
  case for path independence.
- 15.5: rain-through-a-hoop opener (10, 5, 0 liters per hour), landing on the
  room's 2π disc and the tilted-plane result of 1.
- 15.7: accuracy fix. The worked Helmholtz example does not decay at infinity,
  so its split is not unique. A second, verified split is added:
  ∇(x²+y²+z²+xy) + curl⟨0,0,−y²⟩. The text explains why decay restores uniqueness.
- Hinge words removed ("simply gathered", "it just spins", "just this constant",
  "simply a choice"). Answer to Floor 15 Problem 12 now points to Room 15.4.

Candidates for a later pass (not done): other rooms that open cold, e.g. 6.3,
3.2, 17.1; rooms 15.6 and 15.8 are still under 900 words.

## 7. Session of 1 Oct 2026, evening: cold-opening pass, all four volumes

Same owner session, no git. Backups of all four volumes, this file and the root
HANDOVER.md are in
`C:\Users\lomus\OneDrive\My Books for Amazon - session backups\2026-10-01 Tower pass 2\`.

Method: for every room except Looking Ahead, count the prose words before the
first display line or worked example, and read the first sentence. Rooms that
began with a bare definition or formula were ranked weakest. The x.1 "What … Is"
rooms already have on-ramps. Floor 1's zero scores are a quirk of the
measurement (no subtitle line), not cold openings.

New on-ramps, each sharing its numbers with the room's own examples, and every
figure checked as exact fractions:
- V1: 3.2 (calculator error; 1/(x − 3), √(x − 5)); 3.3 (taxi 2x + 1, patio
  squares, second differences of x² − 4x + 3); 3.7 (folding paper; log₂32 = 5;
  log₂10,000 bracketed and shown irrational); 6.3 (Ferris-wheel seat at 0°, 30°,
  90°, 150°, 180°, 210°, −30°); 8.2 (café prices; the room's two systems).
- V2: 17.1 (metronome comb, spacing 1/T, T·cₙ = 0.9003 at T = 4, 8, 16);
  17.4 (rain gauge [1,2,3] * [1,1] = [1,3,5,3]; box-on-box overlaps); 20.7
  (photo stretch; A = [[4,1],[2,3]] on five trial arrows).
- V3: 27.4 (heat vs string at x = π/2: e^(−t) sin x against sin x cos 2t;
  Newton's acceleration rule); 27.5 (ink drop; kernel peaks 0.5642, 0.2821, 0.1410);
  27.6 (soap film; four-point averages of x² − y²).
- V4: 39.2 (average surprise 0.469; best block codes 1, 0.645, 0.533, 0.493 bits
  per flip, never reaching 0.469); 42.2 (weighted average 3.5, loaded die 4.5,
  35/12); 43.4 (doubling system; five-bet cap gives average exactly 0).

Accuracy and presentation fixes:
- 17.1: Poisson summation does not need non-overlapping copies; cₙ = (1/T) f̂(n/T) always.
- 27.4: Huygens' principle holds in odd dimensions from three up, not "any odd"
  (one dimension leaves a wake from initial velocity). The wave equation is not
  "the reason the speed of light is a limit"; reworded to light obeying wave equations.
- 27.5: the maximum principle now says "unless the solution is constant".
- 39.2: 0.469 bits is a little under half of a fair coin's bit, not "a fifth".
- 20.7: ASCII math (lambda, *, ^2, ^T, x_1, " - ") is now λ, ·, ², ᵀ, x₁, em dash.
  "lambda" → λ also in 20.8, 20.9 and the 25.9 glossary.
- Hinge words removed in 3.2, 3.7 and 17.4.

Still open: Floor 20–21 write matrices as [[a,b],[c,d]] and 20.8 still uses
d_1, ^2 and "plus or minus" (house style or not: Lothar's call). Next-coldest
rooms by the same measure: 48.6, 25.2, 27.2, 45.2, 8.3, 18.3, 27.3, 11.2, 39.5,
48.4, 17.2, 47.2.

Word counts (body text): V1 166,215 → 168,063; V2 178,054 → 179,462;
V3 189,786 → 190,831; V4 172,679 → 173,906. Only `word/document.xml` changed
in each; pictures 97/107/102/114, hyperlinks and bookmarks unchanged.

## 8. Session of 1 Oct 2026, late evening: third pass, all four volumes

Same owner session, no git. Backups of all four volumes, this file and the root
HANDOVER.md are in
`C:\Users\lomus\OneDrive\My Books for Amazon - session backups\2026-10-01 Tower pass 3\`.

New openings, same method as section 7 (each uses the room's own numbers,
every figure checked exactly):
- V1: 8.3 (room corner and Toblerone faces; elimination of the room's system to
  3y + z = 9, y − 2z = −4, point (1, 2, 3)); 11.2 (11.1's table 7, 6.5, 6.1,
  6.01 redone with h as a letter: slope = 6 + h).
- V2: 17.2 (test-wave areas for the unit pulse: 1, 2/π ≈ 0.6366, 0);
  18.3 (un-adding 1/2 + 1/3; (3s + 5)/((s − 1)(s + 2)) = (8/3)/(s − 1) +
  (1/3)/(s + 2), checked at s = 2); 25.2 (choir {1,2,3,4} and chess club
  {3,4,5,6} in a class of 8).
- V3: 27.2 (moving walkway, u = f(x − 2t)); 27.3 (B² − 4AC for circle,
  hyperbola, parabola, then Laplace, wave, heat).
- V4: 39.5 (bad phone line: 0.531, 0.278, 0 bits against the naive 0.9, 0.8,
  0.5); 45.2 (two carts; Euler steps 2.25, 2.375, 2.45, 2.495 → 2.5);
  47.2 (thrown ball, action (4a² − 40a)/3 minimal at the true 5 m arch);
  48.4 (data 1, 3, 8: SVRG corrections all give −4); 48.6 (GDA arrows are the
  rotation field of Room 15.1; distance grows by √(1 + η²) every step).

Accuracy and presentation fixes:
- 27.2: the wave equation is in Room 27.4, not "the next room".
- 27.3: Hadamard's example is in Room 27.1, not "the previous room".
- 48.4: RMSProp's 0.3425 is the actual update, not the "effective step"
  (the comparison with AdaGrad's 0.0995 update was right; the label was wrong).
- 48.6: min_x max_y means y responds to x, not "each after seeing the other's move".
- 25.2: "just what was just defined here" → "the set of equivalence classes
  defined above"; stray full stop after "relation?".
- 39.5: doubled label "Abstract example — Illustrative example"; mismatched
  quote around the erasure symbol.
- 47.2: x’’ → x″. 18.3: "simply" removed. 20.4: "a elegant" → "an elegant".

Notation, Floors 20–21 (all rooms, including 20.7's matrices):
- Word equations (OMML) were NOT used. No volume contains any, and KDP's
  docx-to-Kindle conversion does not render them reliably, so matrices use the
  clean typographic form already used in Volume 4 (Room 45.2): [1 2; 3 4] —
  rows separated by semicolons, entries by spaces, compound entries in
  parentheses ([(4−λ) 1; 2 (3−λ)]), augmented blocks as [2 1 | 1 0; 1 1 | 0 1].
- Also: x_1, a_{ij}, d_1 → x₁, aᵢⱼ, d₁; ^2, ^3, ^T, ^−1 → ², ³, ᵀ, ⁻¹;
  R^n → ℝⁿ; "plus or minus 1" → ±1; * → · (Floor 20 only; the * in Floor 21
  is the adjoint and stays); spaced hyphens → em dashes (one real minus in
  20.4); m x n, 2x3 → ×; <=> → ⇔; ... → ⋯ or …; ∫_{−π}^{π} → ∫[−π, π]
  (as in 47.2); A_x, A_y in Cramer's rule → A₁, A₂ (matching xᵢ = det(Aᵢ)/det(A));
  A^p A^q = A^(p+q) → AᵐAⁿ = Aᵐ⁺ⁿ (no superscript q exists, and p is p(A) there).
- 306 paragraphs changed. No [[, ^, _{ or "plus or minus" remains in Floors 20–21.
  Other floors (17.3, Floor 22, 25.9) still have some [[ ]] matrices.
- If Lothar wants real Word equations instead, that is a separate decision.

Word counts (body text): V1 168,063 → 168,622; V2 179,462 → 180,834;
V3 190,831 → 191,501; V4 173,906 → 175,740. About 580 of V2's increase is
the matrix rewrite splitting [[1,2],[3,4]] into separate tokens, not new prose.
Only `word/document.xml` changed; pictures, hyperlinks and bookmarks unchanged.

Next-coldest rooms by the same measure: 18.4, 30.8, 42.7, 7.7, 13.5, 16.4,
24.2, 30.4, 36.8, 48.2, 50.6, 2.8. (27.3 now scores 8 only because its new
opening reaches a display row after one sentence.)
