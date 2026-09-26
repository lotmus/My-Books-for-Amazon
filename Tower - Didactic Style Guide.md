# The Mathematics Tower — Didactic Style Guide

How every new idea in the Tower should be introduced. Derived from the two
passages that work best — the opening of Room 11.1 (the derivative) and the
opening of Room 12.1 (the integral) — and generalised so the same shape can be
applied to any room in any volume.

---

## 1. The principle, in one sentence

**Never define a thing before the reader has felt the need for it, and never use
a symbol before the arithmetic has already made the point.**

Everything below is a consequence of that sentence.

The failure mode this guards against is the one Room 11.1 originally had: an
epigraph, then straight into *"the instantaneous rate of change of f at that
point"*. That sentence is correct, and it is useless to someone meeting calculus
for the first time, because it answers a question the reader has not yet been
made to ask.

---

## 2. The seven moves

Use these in order. Each move has a job, and skipping one is what makes an
explanation feel like it started in the middle.

### Move 1 — Start from something the reader already owns

Open with a thing the reader could have done at primary school, or can see out
of a window. Not a recap of an earlier floor: an actual possession.

> *Derivative:* a road sign warns of a 10% gradient. For every 100 metres
> forward, you climb 10. That fraction is the slope.
>
> *Integral:* the area of a rectangle is width times height. You have known this
> since you were small.

The test: could a reader who skipped the previous eleven floors still follow the
first paragraph? If not, it is not move 1 yet.

### Move 2 — Let the familiar thing break

Show the possession working, then show it failing. The failure must be visible,
not asserted.

> *Derivative:* on a straight road, one number describes the whole hill — 10% at
> the bottom, 10% at the top. Now bend the road. "Ask how steep that hill is and
> there is no longer a single answer."
>
> *Integral:* the region under a straight line is a triangle, and school gave you
> that formula. Put a curve on top and school gave you nothing.

This move creates the need. Machinery introduced before the need is felt reads as
arbitrary; the same machinery after it reads as a rescue.

### Move 3 — Change the question, out loud

Say explicitly what the new question is. Do not let the reader infer it.

> "Not 'how steep is the hill', but 'how steep is the hill right here, at this one
> spot'?"
>
> "Not how much area lies between here and there, but what function reports the
> area accumulated so far?"

One sentence. It is the hinge of the whole passage, and it should be short enough
to be remembered.

### Move 4 — State the obstacle so it can be *felt*

Name the reason the new question cannot be answered directly, in concrete terms,
and do not hurry past it.

> "At a single spot you have not gone forward at all. The run is zero and the
> climb is zero, and zero divided by zero tells you precisely nothing."

This is the move most often skipped, and skipping it is expensive. A resolution is
only satisfying in proportion to how real the problem felt. If the reader does not
feel the 0/0 wall, the limit looks like a ritual instead of a rescue.

Signal it. A phrase like *"and it is worth feeling this properly before we get rid
of it"* tells the reader the discomfort is intentional.

### Move 5 — Offer the trick, and admit it looks like cheating

Give the idea in plain words before any notation.

> "The way round it looks like a cheat and turns out not to be one. Do not try to
> measure at the spot. Measure from the spot to somewhere a little further along,
> where there is a real climb and a real run to divide."
>
> "Stop attacking the thing you cannot do, and replace it with a great many things
> you can."

Naming the apparent cheat disarms the reader's suspicion instead of leaving it to
fester.

### Move 6 — Numbers before symbols

A short table the reader can verify by hand. Five lines is plenty. The arithmetic
must do the persuading; the notation arrives later only to record what was already
believed.

```
h = 1      slope = 7          4 rectangles      3.75
h = 0.5    slope = 6.5        8 rectangles      3.1875
h = 0.1    slope = 6.1        20 rectangles     2.87
h = 0.01   slope = 6.01       100 rectangles    2.7068
h = 0.001  slope = 6.001      1000 rectangles   2.670668
```

Then — and this is not optional — **say what the numbers never do**:

> "Notice what they never do: they never arrive. Every one of those slopes was
> measured across a real stretch of road, so every one of them is the steepness of
> a stretch, not of a spot. Yet 6 is plainly the number they are aiming at."

Concealing non-attainment to keep things simple is a false economy. It is the
conceptual core, and a reader who is not told now will be confused later by
asymptotes, by improper integrals, and by every ε–δ argument in the book.

### Move 7 — Name it, then translate the notation

Name the object only once it exists, and keep the naming flat.

> "That is the derivative, and nothing more alarming is going on. It is a slope —
> the same rise over run you have used since school — with one extra move at the
> end."

Then translate into whatever the reader arrived with. Most readers were taught
Δy/Δx and have never been told it is the same thing as the book's `h`:

> "The shrinking run, which school calls Δx, is written h from here on — so Δx → 0
> and h → 0 are two names for the same instruction."

---

## 3. The structural rule: intuition and proof must share numbers

The informal table and the formal derivation that follows **must use the same
example and reach the same number.**

- Room 11.1's on-ramp gets **6** for `x²` at `x = 3` by watching a table.
  Room 11.2 then derives `f′(3) = 6` from the definition.
- Room 12.1's on-ramp gets **3.75** for four rectangles and heads toward **8/3**.
  Room 12.2's figure already shows 3.75, and derives the rest.

This costs nothing and buys a great deal: the reader meets the answer twice, once
as a belief and once as a proof, and the two rooms lock together instead of each
starting cold. When writing a new on-ramp, **look at what the next room derives
and work backwards from its numbers.**

Verify the arithmetic exactly — as fractions, not floating point — before it goes
in. Every table in the Tower should be reproducible by a reader with a pencil.

---

## 4. Forward references

When a passage hand-waves, say so and say where the rigour lives.

> "Room 12.2 does this properly, allowing the strips to be uneven."
>
> "Room 11.2 does this properly, and gets 6 again."

This converts a gap into a promise. It also means the informal passage can stay
informal without apology, which keeps it readable.

Cross-references must point at rooms that exist and contain what is claimed. A
reference to a proof the book never gives is worse than no reference — the Tower
had one of these: a line calling the Euclidean algorithm *"the same machinery
again"* when the algorithm had never been shown.

---

## 5. Register

- **Short sentences at the point of difficulty.** Long ones are fine for scenery,
  never for the hinge.
- **One new idea per paragraph** wherever the material is hard.
- **Concrete nouns.** Hills, roads, rectangles, staircases, ladders, cans of drink.
  Abstraction is what the reader is trying to reach, not what they should wade
  through to get there.
- **Dry humour is welcome; it must never be at the reader's expense.** "Arriving
  early and out of uniform" is fine. "Obviously" is not.
- **Banned words at a hinge:** *clearly, obviously, simply, just, of course, it is
  easy to see*. Every one of them tells a struggling reader the fault is theirs.
- **Address the reader as an equal.** Second person is good; the Tower's rate
  drifts from about 10 uses per thousand words on Floor 1 to about 3 by Floor 8,
  and the upper floors are colder for it. Aim to keep it steady.
- **Parallelism is an asset, not repetition to be edited out.** "A positive
  discriminant means… a negative discriminant means…" is doing work. Only remove a
  repeated word when it carries two *different* senses with no parallel structure.

---

## 6. When to use the full seven moves — and when not

Use all seven for the **first encounter with a genuinely new kind of object**:
the derivative, the integral, the limit, the vector, the logarithm, the complex
number, the matrix, the group.

Do **not** use them for:

- an idea that extends one already built (the quotient rule, after the product
  rule — the need is already felt);
- routine technique rooms, where the reader wants the method, not a story;
- "Looking Ahead" rooms, which are inventories by design.

A rough guide: if the room's title contains *"What … Is"*, it needs all seven. If
it names a technique, it needs moves 6 and 7 only — a worked number, then the
notation.

---

## 7. Checklist before a room is finished

1. Could a reader who skipped the previous floors follow the first paragraph?
2. Does something familiar visibly **break** before new machinery appears?
3. Is the new question stated in one short sentence?
4. Is the obstacle stated concretely enough to be felt?
5. Do numbers appear **before** notation?
6. Is it said plainly what the numbers never do?
7. Is the object named only after it exists?
8. Is the reader's own notation (Δx, rise over run) translated explicitly?
9. Does the next room derive the same example and reach the same number?
10. Does every forward reference point at a room that exists and delivers?
11. Has every figure in the table been checked exactly, not numerically?
12. Are *clearly*, *obviously*, *simply* and *just* absent from the hinge?

---

## 8. The two reference passages

When in doubt, read these and copy the shape, not the words:

- **Room 11.1**, from *"Begin with something you can already do"* to
  *"Room 11.2 does this properly, and gets 6 again."*
- **Room 12.1**, from *"That worked because the region happened to be a triangle"*
  to *"the number is what the machine hands over once you nail down two ends."*

Both run about 500 words and both do all seven moves in order. That length is a
reasonable target: long enough to build the need, short enough that a reader in a
hurry can still reach the formal statement on the same spread.
