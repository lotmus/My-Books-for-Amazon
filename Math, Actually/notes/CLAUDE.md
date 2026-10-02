# Math, Actually — working instructions

This folder holds the manuscripts of *Math, Actually* (Volumes 1–4), the
companion series to *Physics, Actually* and *Life, Actually*. Until 2 Oct 2026
it was *The Mathematics Tower*; see section 0. Read this before editing anything.

What the four volumes contain, and the house facts every volume shares, is in
`Math, Actually - Series Reference.md`. Cite chapters from that file. Do not keep a
second copy of the chapter map here.

---

## 1. How to write — the didactic contract

**`Math, Actually - Didactic Style Guide.md`, in this folder, is the authority on how any
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
   rectangle's area. Could a reader who skipped the previous chapters follow the
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
example and reach the same number.** Section 11.1's on-ramp lands on 6 because 11.2
derives 6; Section 12.1's lands on 3.75 because 12.2's figure already shows 3.75.
When writing a new on-ramp, work backwards from what the next section derives.

Use all seven moves only for a genuinely new kind of object. Technique sections need
moves 6 and 7 only. "Looking Ahead" sections are inventories by design.

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
the author, and the words chapter, section, and series — is in
`Math, Actually - Series Reference.md`. Follow that file.

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
  wholesale** — the book has ~2,200 internal section links and ~350 chapter links, and
  flattening a paragraph to one run destroys them.
- **Prefer styles.xml to touching paragraphs.** Restyling 180 headings is one edit
  there, and safe only when no paragraph carries direct formatting — check first.
- **Verify after every write, before replacing the live file:** `testzip()` clean,
  entry list unchanged, media count unchanged, `document.xml` parses, and every
  replaced image still decodes. Picture counts are in
  `Math, Actually - Series Reference.md`.
- **Verify arithmetic exactly** — as fractions, never floating point. Every table
  in the book should be reproducible by a reader with a pencil.

## 4. Project facts

- **The .docx is the only deliverable. Do not build or rebuild EPUB or PDF, and
  do not offer to.** This is settled; treat it as standing.
- The `.epub` and `.pdf` files (now in `bak\superseded 2026-10-01\`) are **stale and
  superseded** — they predate corrections that are in the .docx. Leave them
  alone, and do not publish from them.
- **Sessions are scoped per volume.** Do not edit other volumes unless asked.
- **Several sessions edit this repo concurrently.** Re-read the file and the git
  log before writing; do not trust a status snapshot from the start of a
  conversation.
- Backups live in `bak\` (the old `Archive - not for publication` folder is now
  `bak\Archive - not for publication\`).

## 5. Where things live

The chapter map, the section pattern, the layout conventions copied from
*Physics, Actually*, and the citations that are easy to get wrong are in
`Math, Actually - Series Reference.md`. That file also records the bookmark
names (`sec_N_M`, `ch_N`, `sec_18_9_tables`). Leave them as they are.


## 0. The rename to Math, Actually (2 Oct 2026)

- Folder `The Mathematics Tower\` → `Math, Actually\`; masters
  `The Mathematics Tower - Volume N.docx` → `Math, Actually - Volume N.docx`.
  Superseded originals are in `D:\bak\2026-10-02 Math Actually\`.
- Vocabulary: Floor N → Chapter N, Room N.M → Section N.M, the Tower → the
  series. No floor/room/storey/Tower wording or lift/staircase/building framing
  in the books. Subtitles kept, without the Floors part (Volume 1 From
  Arithmetic to Calculus, etc.). Chapter 50 is now “Where Mathematics Meets the
  World”.
- Layout copied from *Physics, Actually* (title page, copyright page, Contents,
  Also in This Series, chapter openings with the “Math, Actually” series line,
  Physics heading styles, “A Note Before You Go”). Details and the deliberate
  deviations are in the Series Reference.
- Cross-references inside a volume are hyperlinks named by topic; references to
  another volume are plain “Topic (Volume N)”. Bookmarks are `sec_N_M`, `ch_N`.
- Done once by `scripts\build_math_actually.py` (Python 3 + lxml, see
  `scripts\README_build.md`). It reads the old Tower masters, so do not re-run it
  on the new masters. From now on the masters are edited directly.
- Open: the cover images still show the Tower title; 87 sections still open
  “cold” (under 50 words before the first formula) and need new on-ramps, as
  listed in `Math, Actually - Sections Needing On-ramps.md`.
- **Older sections below are a historical log and keep the old names**
  (Floor = Chapter, Room = Section, Tower = the series).

## 6. Session of 1 Oct 2026 (Volume 2, Floor 15)

One session owns the Tower, RIB Book 1 and Protocol Flamingo, and does no git.
Backup before the edit: `bak\Archive - not for publication\The Mathematics Tower - Volume 2 (backup 2026-10-01, before Floor 15 on-ramps).docx`.

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
- 306 paragraphs changed in the Floor 20–21 rooms. CORRECTION (pass 4): the
  pass-3 claim that nothing was left was wrong. Only the rooms were converted;
  the Floor 20–21 Check Your Understanding, Problems, Answer Key, Solutions and
  glossary entries were missed. Pass 4 converted them (see section 9).
- If Lothar wants real Word equations instead, that is a separate decision.

Word counts (body text): V1 168,063 → 168,622; V2 179,462 → 180,834;
V3 190,831 → 191,501; V4 173,906 → 175,740. About 580 of V2's increase is
the matrix rewrite splitting [[1,2],[3,4]] into separate tokens, not new prose.
Only `word/document.xml` changed; pictures, hyperlinks and bookmarks unchanged.

Next-coldest rooms by the same measure: 18.4, 30.8, 42.7, 7.7, 13.5, 16.4,
24.2, 30.4, 36.8, 48.2, 50.6, 2.8. (27.3 now scores 8 only because its new
opening reaches a display row after one sentence.)

## 9. Session of 1 Oct 2026, night: fourth pass, all four volumes

Backups: `My Books for Amazon - session backups\2026-10-01 Tower pass 4\`.
Scripts on the box: /workspace/books/tower/p4_v1.py … p4_v4.py, run by edit_p4.py.

Openings written (same contract as section 7: a concrete case with real numbers
first, then the name):
- 2.8 milepost road, |x − 3| = 5. 7.7 table of 2ˣ, halving never reaches 0,
  swap the rows to get log₂, x¹⁰ against 2ˣ.
- 13.5 hill z = x² + y² at (3, 4): slopes 6 and 8, five trial directions,
  steepest 10 along ⟨6, 8⟩. 16.4 how a calculator gets e^0.1: 1.1, 1.105,
  1.1051667, 1.1051708. 18.4 y′ + 2y = e⁻ᵗ solved by guessing, then by the
  transform in four rows. 24.2 restaurant (3 × 2 = 6, 3 + 2 = 5, 3 × 4 × 2 = 24)
  and five books (60 ÷ 6 = 10).
- 30.4 well and road x + y = 1. 30.8 sealed box with readings of (x − 3)².
  36.8 ⟨3, 4⟩ measured as 5, 7 or 4; f = x in L¹, L², L∞.
- 42.7 five readings, four trial lines, sums of squared misses 0.2675, 0.14,
  0.11, 0.107. 48.2 saddle x² − y², gradient descent escaping from (0, 10⁻⁶)
  in about 34 steps. 50.6 epidemic generations 1, 3, 9, 27, then 1, 1, 1, 1
  with two-thirds immune.

Accuracy fixes:
- 13.5 example titled "three directions" computed two; added the third,
  ⟨−4/5, 3/5⟩, rate 0, along the level curve.
- 16.4 "a infinite series" → "an"; doubled label "Abstract example — Structural
  example —" → "Abstract example —"; "by roughly a factor of ten" → "by a factor
  of more than ten" (the actual ratios are about 30 to 50).
- 24.2 "the overcounting correction from the previous paragraph" (no such
  paragraph) → "an overcounting correction"; "an n-element subset of size k" →
  "a k-element subset of an n-element set"; stars and bars "choosing which
  k+n−1 positions hold stars" → "which k of the k+n−1 positions"; "the earlier
  list for {a,b,c}" (no earlier list) → "the subsets of {a,b,c}".
- 30.4 "respond by bribery" → "respond with fines".
- 30.8 SGD "still guaranteed to converge" now says "provided its step sizes
  shrink suitably over time"; the "convergence in expectation" sentence replaced
  by the true picture (fixed step 1 keeps bouncing among 1, 3, 5 around the
  average 3; shrinking steps give real convergence).
- 36.8 "an wholly continuous part" → "an absolutely continuous part".
- 42.7 logistic outputs lie in the open interval (0, 1), not on [0, 1].
- 50.6 the 50.3 result came from "dimensional analysis plus a borrowed
  constant", not "dimensional analysis alone".

Notation (V2 only, typographic form as in section 8, no Word equations):
- Floors 20–21 end matter converted in full: CYU, Problems, Answer Key,
  Solutions and glossary entries (40 paragraphs; lambda → λ, 2x3 → 2×3,
  1*(−24) → 1·(−24), d_1 → d₁, A^−1 → A⁻¹, A^T → Aᵀ, a_{ij} → aᵢⱼ, dashes).
- Matrices only: 17.3, 22.6, 22.7 and the Floor 22 Answer Key and Solutions
  (12 paragraphs). V2 now contains no [[ at all. (The "25.9" leftovers named in
  section 8 were these end-matter items after Room 25.9, not Room 25.9 itself.)
- Still [[ ]] elsewhere: V1 4 (4.7, 8.5, 9.9); V3 80 (26.1 15, 34.1 22, 29.5 7,
  Answer Key 7, others); V4 46 (49.4 11, 48.5 5, 48.2 3, 46.3 4, others).
  V2 Floors 23–25 end matter may still carry ASCII maths such as t >= 0, u_1(t).

Word counts (body text): V1 168,622 → 169,209; V2 180,834 → 182,110;
V3 191,501 → 192,459; V4 175,740 → 176,544.
Only `word/document.xml` changed; pictures, hyperlinks and bookmarks unchanged.

## 10. Session of 1 Oct 2026, night: notation sweep, all four volumes

Lothar's decision: keep the typed form (no Word equations) and use it across
the whole Tower, every section (rooms, CYU, Problems, Answer Key, Solutions,
glossary, TOC). Backups: `My Books for Amazon - session backups\2026-10-01 Tower
notation sweep\`. Code on the box: /workspace/books/tower/sweep.py (rules) and
sweep_apply.py (applies them across runs and keeps formatting).
Paragraphs changed: V1 305, V2 597, V3 482, V4 407.

House notation (use it in all new text):
- Matrices [1 2; 3 4]; augmented [1 1 | 6; …]; det [a b; c d].
- Powers and indices as Unicode super/subscripts when every character has one:
  x², e⁻ˢᵗ, eᴬᵗ, aᵐ⁺ⁿ, f⁽ⁿ⁾, Γᵏᵢⱼ, xᵢ₋₁, log₃, pₘ(A).
- If it can't be scripted: e^(…) becomes exp(…) in V2–V4. V1 keeps e^(…),
  because exp is only introduced in 7.6. Other powers stay as base^(…), with
  parentheses, not braces.
- Limits that can't be scripted go in square brackets: ∫[0, π], ∫[−∞, ∞],
  ∫[S²], ∬[D], ∮[C], Σ[n ≥ 0] (an upper limit of ∞), lim[x→0], max[k≤9],
  Res[z=0]. When both limits script, keep ∫₀¹, ∫ₐᵇ, Σₖ₌₁ⁿ.
- ≥, ≤, ≠, ⇔; ℓ∞, L∞, ‖f‖∞; convolution and free product f ∗ g (U+2217),
  Fourier hat (f ∗ g)ˆ(ξ). The plain * stays for duals, adjoints, optima and
  C*, weak*, {*}.
- Inside one paragraph, if one subscript on a letter can't be scripted (f_y),
  its partners stay plain too (f_x), so a formula never mixes fₓ with f_y.
- Markdown leaks *out*, *into*, *out of* in the V4 Answer Key became real italics.

True remaining after the sweep (body, tables and TOC, all four volumes):
- [[ 0, _{ 0, >= 0, <= 0.
- lambda 1: prose, "(the Greek letter lambda)" in 20.7.
- * 360, all genuine notation: V*, T*, x*, C*-algebra, weak*, {*}, f*ω.
- ^ 335: fractional or decimal exponents 187, e.g. a^(1/n), (x² + y²)^(3/2),
  e^(−t/8) in V1; evaluation bars [F]₀^π 38; exponents with no superscript glyph
  47 (π, ∞, ω, ×, as in 3^(2×3), 2^ℵ₀); V1 e^(…) 15; p₁^a₁-type 13; other 35
  (10,000^q, b^(log_b x)).
- _ 915: partial derivatives f_y, u_yy (and f_x kept to match) 329; capital
  subscripts (η_V, χ_A, X_H) 213; other lowercase with no glyph (y_screen, κ_g)
  146; compound _(…) (D_(xy), X_(k+n/2)) 99; Greek, ∞ or ∂ subscripts 90;
  log_b, log_c 38.
Unicode has no glyphs for these, so they stay unless Lothar switches to Word
equations or a font-safe alternative ("log base b", ∂f/∂y).

Word counts (body text): V1 169,209 → 169,228; V2 182,110 → 182,245;
V3 192,459 → 192,678; V4 176,544 → 176,600 (tokens split by spacing).
Only `word/document.xml` changed; pictures, hyperlinks and bookmarks unchanged.
Kindle check still to do: rarer modifier letters (ᶿ, ᶻ, ᴬ, ᵝ) should be
previewed in Kindle Previewer before publishing.

## 11. 1 Oct 2026, late night: folder move, layout, and audit of all four volumes

**Layout.** The Tower now sits at the books root as `The Mathematics Tower\`.
It used to be `Math for HS and College\The Mathematics Tower\`, and that
folder is gone.
- Root: the four volume .docx masters, `KDP_Description.md`, and the cover
  images.
- `notes\`: this file, the series reference, the style guide, and
  `_METHOD - Textbook 3-Source Workflow.md`.
- `planning\Math Books Topics List\`: the 50 topic outlines (Book1–Book50).
  They are plans, not books.
- `scripts\make_epub.py`: moved from `Tools\`. It finds the Tower folder from
  its own location, so no paths had to change. EPUB stays off (section 4).
- `bak\READY (2026-09-26)\`: the old READY copies.
- `bak\superseded 2026-10-01\`: the stale .epub and .pdf files, the two
  `Volume 4.docx.pre-*-backup` files, and the `*.storeys-backup.png` covers.

**Backups before the audit:**
`My Books for Amazon - session backups\2026-10-01 Tower audit\`.
**Code on the box:** /workspace/books/audit/ (`rules.py`, `apply.py`,
`verify.py`, plus the checkers `arith2.py`/`arith3.py` and `poss.py`).
Only `word/document.xml` changed. Pictures, hyperlinks, and bookmarks are
unchanged (97/818/396, 107/906/428, 102/1311/870, 114/980/581).

**Fixes:**
- American spelling, per the series reference: rigour, manoeuvre, flavour,
  humour, relabelling, draught(s), sceptic/scepticism (the ε–δ game's
  “Sceptic” is now “Skeptic”), cheque, kerb, harbour, tumour, instalment,
  totalling, spiralled, -ise/-isable forms, and others. 3 nought → zero /
  none / aleph-null.
- Articles: a entire, a alarming, a unsettling, a infinite(-order,
  -dimensional), a enormous → an; an wholly → a wholly (V1, V3); an
  computable → a computable (V4).
- V3 Problems, Answer Key, and Solutions had lost their possessive
  apostrophes: Green’s, Newton’s, Noether’s, Lagrange’s, Hadamard’s,
  Hadwiger’s, Bessel’s, Riesz’s, Gauss’s, Galois’s, Monte Carlo’s, body’s,
  theory’s, topology’s, and about 20 more. **Other lowercase possessives in
  those V3 sections may still be missing.** A spell checker can't find them,
  so they need a read-through.
- Doubled example labels, 13 in all: V2 “Abstract example — Structural
  example —” ×5; V4 “Abstract example — Illustrative example:” ×6 and
  “Worked example — Synthesis example —” ×1.
- Missing spaces: “floorabove” (V1) and “flooris” (V4).
- Notation: ’’ used as a double prime → ″ (y″, u″, f″, X″, R″). Primes typed
  as apostrophes → ′ (V2 f′ dx, y′, A′, R′, T′; V4 P′ Q′ R′).
  `delta(t − c)` → δ(t − c) (V2 Laplace problem and glossary). The ∬ₛphere
  sweep artifact → ∬[sphere]. “+/-infinity” → ±∞ (V3).
- Maths: the powers of 3 mod 7 tables (V1 Room 7.9, V2 Room 24.9) wrote
  3³ = 3×2 = 6, which is false as written (3³ = 27). They now use ≡ for
  reduction: 3³ ≡ 3×2 = 6 (mod 7), and so on.

**Checked and found clean:** the “Also in This Series” pages (identical in
all four volumes, and they match the title pages and the series reference);
title and subtitle pages; [[ ]], >=, <=, sqrt(, and ASCII Greek. An automated
pass over every pure-number “a = b = c” chain in all four volumes found no
arithmetic errors outside the mod-7 tables. No TODO, TBD, or placeholder text
anywhere. This was not a line-by-line proof read of ~720,000 words.

**Open (Lothar):**
- No Tower KDP description existed. `KDP_Description.md` is a new draft;
  price, categories, and keywords are still to choose.
- This file is now in `notes\`. Tools that load `CLAUDE.md` automatically
  from the Tower root will no longer find it there. This is deliberate: md
  files live in `notes\`, and there is no stub in the root.
- The example count, `boxes.json`/`chapters.png`/`back cover.png` and the
  Archive folder were settled in section 12.

## 12. Round 2, 1 Oct 2026 (all four volumes)

Backup before the edits: `My Books for Amazon - session backups\2026-10-01
Tower audit round 2\` (four volumes, `KDP_Description.md`, this file).

- **Worked-example count recounted:** 430 / 433 / 361 / 349 = **1,573**.
  Only paragraphs starting “Numeric / Abstract / Worked example —” inside the
  shaded example boxes count. Doubled labels were already fixed, and “For
  example —” in running text doesn't count. V2's unlabeled shaded boxes are
  Problems, not examples. Both statements in each volume (“There are … worked
  examples in the Tower, N of them …” and “… the Tower contains … such
  exercises …”) now say 1,573 and the volume's own count, and so does
  `KDP_Description.md`.
- **V3 lowercase possessives:** a read-through of the floor Problems/CYU
  sections, Answer Key and Solutions restored 15 more: algorithm’s,
  cartographer’s (×2), acceleration’s, building’s, needle’s, plane’s,
  definition’s, function’s, subject’s, observer’s, moving frame’s,
  discipline’s, Riemann tensor’s, theorem’s. No lost contractions were found.
- **Archive merged:** all 17 files of `Archive - not for publication` were
  moved with `git mv` to `bak\Archive - not for publication\`, and each
  one's SHA-256 was checked after the move. The old folder is gone.
- **Root files:** `back cover.png` (1024×1536) is the Tower's paperback back
  cover (“Fifty floors. One building. All of mathematics.”), so it stays in
  the root. `boxes.json` was a scratch dump of V3 definition-box openings
  (British spelling, mojibake), and `chapters.png` was a screenshot of
  another series' folder list, identical to the copy in `bak\READY
  (2026-09-26)\`. Nothing referenced either of them, and both are now in
  `bak\superseded 2026-10-01\`.
