# Schrödinger's Paperwork Book 1 — manuscript audit (follow-up)

Audit date: 9 September 2026

Source: `D:/My Books for Amazon/Schrodingers_Paperwork/Schrodingers_Paperwork_BOOK_1.docx`
(last modified 2026-09-06 21:53; 2,376 top-level paragraphs; ~59,000 words)

Prior audit: `English/Schrodingers_Paperwork_BOOK_1_Audit_2026-09-05.md`. This report re-checks
every finding of the 5 September audit against the current file, records which were acted on,
and adds findings that pass missed.

---

## Editorial verdict

The book is very good. The voice is controlled, the comic timing is real, and the
collision between institutional language and personal loss — Mrs Chain and her sister —
carries genuine weight. The physics-teaching layer is technically sound: every "Going
deeper" equation checks out, and the misconception corrections are careful and honest.

> **Status note (10 September).** The paragraphs below describe the file as it stood on
> 9 September. Over 9–10 September the findings were then worked through in a series of
> reviewed, individually-committed passes (git repo initialised; see the dated "Applied"
> sections). As of 10 September the manuscript is **substantially revised**: the corrupt
> image is replaced; the Chapter 13–16 causal chain, the calendar, and the missing setup
> are fixed; the physics overstatements are softened; the continuity slips are closed; the
> appendix teaching lists are broken out; and a Glossary has been added. What remains is
> author's-discretion polish, listed under "Deliberately not done" and "Still open" below.

*(as of 9 September)* It is still not ready to publish, and it is closer to *unchanged*
than the file history suggests. Since the 5 September audit, only nine small copy
corrections have been applied (listed below). **None of the structural findings has been
addressed**: the climax still skips its own causal chain, the calendar still does not
reconcile, several people and losses still arrive without setup, one key line is still
attributed to the wrong speaker, and the physics dialogue still overstates what string
theory has established. In addition, the editing session on 6 September **corrupted the
embedded back-cover image**, which is a new production defect that did not exist in the
August backups.

Priority order for the remaining work: the Chapter 13–16 causal chain first, then the
calendar and the missing setup, then the physics overstatements, then formatting and
production, then the covers.

---

## What changed since 5 September

Comparing `Schrodingers_Paperwork_BOOK_1_BEFORE_AUDIT_FIXES_BACKUP.docx` (the pre-edit
backup) with the current file, exactly nine text changes were made — all from the
"definite copy and notation defects" section of the last audit:

| Para | Was | Now | Prior finding |
| --- | --- | --- | --- |
| 29 | "allegedly.Lothar" | "allegedly. Lothar" | 20 |
| 242 | `\|journey= a\|not yet taken+ b\|already arrived` | ket brackets restored | 21 |
| 318 | "An what." | "A what?" | 20 |
| 581 | `\|street= a\|remembered+ b\|revised` | ket brackets restored | 21 |
| 884 | Beatrix "in the back of an unlicensed grey car" | "in an unlicensed grey car" | 8 |
| 1502 | "enough of the Fecloses" | "enough of the residents" | 20 |
| 1944 | two Physics-Notes links run together | line break inserted | 20 |
| 1950 | "We have three plans … fewer than three" | "four plans … fewer than four" | 12 |
| 2070 | "10^{100} years" (literal) | "10 to the power of 100 years" | 22 |
| 2122 | "DISCREPANCYSUBCATEGORY…SCHEDULEDURGENCY" | fields spaced apart | 20 |

All ten line-level items from the last audit's copy-defect section are therefore resolved
(the appendix superscript `10¹⁰⁰` in para 2335 was correctly left alone — it is a real
formatted run). Everything that required rewriting a scene, a date, or a claim was not
touched.

---

## Applied 9 September (this pass)

The following mechanical corrections were made to `Schrodingers_Paperwork_BOOK_1.docx`
on 9 September. The pre-edit file was saved as
`English/Schrodingers_Paperwork_BOOK_1_BEFORE_MECHANICAL_FIXES_BACKUP.docx`. The document
was re-validated (XSD checks pass, paragraph count unchanged, all 42 cross-references
still resolve).

| # | Location | Change |
| --- | --- | --- |
| N1 | `word/media/image1.png` | Corrupt back-cover image replaced with the clean copy from the 28 Aug backup; ZIP and PNG checksums now valid. |
| N2 | para 227 | "…she might improve her physically." → "…she might improve her, physically." *(minimal repair — confirm this is the intended sense)* |
| K4 | para 135 (cast) | "Dr Stephanie Fainrose — Lolly's mentor." → "…Lolly's mentor, eventually." |
| K5 | para 150 (physicist key) | Keinschein "immaculate, courteous" → "courteous, dishevelled" |
| K6 | para 2204 (Ch 6 notes) | "…he reaches the black-hole information problem" → "she reaches…" |
| K6 | para 2095 | "in the ordinary handwriting of a man who had somewhere to be" → "…of someone who had somewhere to be" |
| P1 | para 2218 (Ch 7 notes) | "experiments beginning with Alain Aspect's 1982 tests" → "experiments — Freedman and Clauser in 1972, then Aspect in 1981–82 —" |
| P1 | Further Reading, Ch 7 entry | Added "Stuart Freedman and John Clauser, the first experimental violation (1972)"; Aspect reworded to "the experiments that closed key loopholes (1981–82)" |
| P5 | "If this made you curious" | Rovelli "forgive him for being right" → "forgive him for being persuasive" |
| F5 | `settings.xml`, `styles.xml` | Default proofing language en-US → en-GB |

## Applied 10 September (Bell-test scene)

Draft "A" from `Schrodingers_Paperwork_BOOK_1_DRAFT_Bell_test_payoff.md` was inserted, plus
the Chapter 16 phrase change. Pre-edit file:
`English/Schrodingers_Paperwork_BOOK_1_BEFORE_BELL_SCENE_BACKUP.docx`. Re-validated (XSD
passes; +19 paragraphs, 2,400 → 2,419; all cross-references still resolve; image intact).

| # | Location | Change |
| --- | --- | --- |
| C1 | Chapter 15, new opening (19 paras, before "Beatrix Sloan won the injunction application…") | The apparatus fault is diagnosed (both stations correlated through the Ministry's own timing/power/randomness), fixed by subtraction (independent clocks, isolated power, decay-source setting-choices, separated stations), re-run clean, and reports **S = 2.41 ± 0.03** against a stated threshold of 2.3 — the number Beatrix takes to court. Bellew present to bind the result. |
| C2 | Chapter 16, para (was 2022) | "the display marked S, which had sat at 1.2 for eleven weeks…" → "the **coherence monitor Fainrose had left running since Sub-District 6** — flat at 1.2 for eleven weeks…" A planted line in the new Ch 15 scene establishes that monitor as a *different* measurement (the district's own internal coherence), so the 1.2 → 2.79 rise on disconnection is now physically correct. |

**C3** was addressed in a later pass — see below.

## Applied 10 September (C3 — missing setup)

Pre-edit file: `English/Schrodingers_Paperwork_BOOK_1_BEFORE_C3_BACKUP.docx`. Re-validated
(XSD passes; +3 paragraphs, 2,420 → 2,423; cross-references and image intact).

| gap | Fix |
| --- | --- |
| **The 411 / "P-9" cohort** arrives unnamed and undefined in Ch 15/16 | New paragraph in **Ch 12** (right after the "woman who had remembered her sister's name" line): Beatrix finds the classification — "P-9, pending status, for a citizen the survey had caught in the middle of something… and then required to sign regardless," with the form's *no action required* field beside it. "The log stood at ninety-one that morning, and was climbing." Ch 15's first use of the number now reads "the four hundred and eleven suppressed states — the P-9 log, closed at last —", so "suppressed states / P-9 states / pending states" are visibly one cohort. |
| **"When Vale froze Sub-District 6"** (Ch 11) referenced as known | New paragraph in **Ch 10** (the drive along the ridge above Sub-District 6): "Sub-District 6… lay under a continuity freeze — Vale's order, to hold the local grid steady while 4C was argued about elsewhere… a grid of windows all lit the same flat yellow, not one of them changing." Keinschein's "He froze it for the grid" now lands on established ground. |
| **Miss Dorothy Kell** (Ch 16) appears with no introduction | Identified in place: "Miss Dorothy Kell — whose brother's apprenticeship was one of the hundred and three, and who had written to the inquiry every week since the freeze —" (ties to the recovered-items list in the previous paragraph and to the Ch 10 freeze). |
| **Vale "ended a paralysis… precisely as Fainrose had told him"** (Ch 16) — an unshown conversation, an unclear "paralysis" | New paragraph in **Ch 12** (right after Vale's suspension): Fainrose predicts to the room that "whoever [stands] up in that inquiry and… say[s] what it did… will be thanked for the disruption and not the truth." Ch 16 para rewritten: Vale "blamed for the disorder the recovery made rather than credited for the eleven days that had made the recovery lawful at all. It was, almost to the word, what Fainrose had said would happen…" — the callback is now earned and the "paralysis" is legible (his testimony against his own directive is what unblocked the inquiry). |

## Applied 10 September (P2–P4 — physics overstatements)

Pre-edit file: `English/Schrodingers_Paperwork_BOOK_1_BEFORE_P234_BACKUP.docx`. Re-validated
(XSD passes; no paragraph-count change — all eight are in-place text edits).

| # | Location | Change |
| --- | --- | --- |
| P2 | Ch 14, von Wittenberg (dialogue) | "the theory has never been tested. **Not once**" → "there has never been a **direct experimental test** of it. **Not one**" |
| P2 | Ch 14, von Wittenberg (dialogue) | dualities "exactly **and provably**" → "exactly … an equivalence **proved in the tractable cases and, in the decades since, contradicted in none**" |
| P2 | Ch 14 Notes, "Going deeper" | "related by **precise mathematical** dualities … it becomes, **exactly**, a different description" → "related by dualities **that are provable in the simplest cases and, so far, consistent everywhere else** … it becomes a different description" |
| P2 | Ch 14 Notes, "What the reader learns" | "removes **the infinities that had always wrecked** attempts" → "removes **the short-distance infinities that had wrecked earlier** attempts — **at least in every calculation anyone has managed to finish**" |
| P3 | Ch 14, von Wittenberg (dialogue) | "That is **the only occasion on which anyone has ever counted** the microscopic states of a black hole and got **the right answer**" → "That is **the first time anyone counted** the microscopic states of a black hole and got **the entropy formula back exactly**" |
| P4 | Physics Prologue (para 124) | "move complexity somewhere you cannot see. Always, **and by law**." → "…Always." (drops the claim that the *institutional* version is a law of physics; keeps the rhetorical beat) |
| P4 | Ch 16, Schrottfinger (dialogue) | "you need not attribute it to me **because Boltzmann said it first and less politely**." → "You need not attribute it to me. **It is the second law with the politics put back in — Boltzmann did the arithmetic and had the sense to stop there.**" |
| P4 | Ch 16 Notes, "Where the popular version goes wrong" | added: the "every institution exports its complexity" line is "**a moral analogy, not a theorem** … administrative complexity, meaning and thermodynamic entropy are three different quantities, and only the last is governed by the second law. Where erasing information does carry an unavoidable physical price, the principle is **Landauer's**." |

The dialogue keeps von Wittenberg's and Schrottfinger's enthusiasm — it is characterisation,
and the Notes already flag it as such — but the flat claims and the false Boltzmann
attribution are gone, and the Notes now carry the correction the audit asked for.

## Applied 10 September (calendar reconciliation, T1–T7)

Pre-edit file: `English/Schrodingers_Paperwork_BOOK_1_BEFORE_CALENDAR_BACKUP.docx`.
Re-validated (XSD passes; +1 paragraph, 2,419 → 2,420; cross-references and image intact).

Working chronology adopted: crisis begins mid-August (Ch 11 "August light"); investigation
runs a handful of days (Ch 12 "three days ago"); injunction **applied for and won on the
Monday, formally granted on the Tuesday** once the Board's demanded plan was filed;
eleven-week repair through **14 November** (coupling cut); districts resolve over December;
the **legal settlement is filed that winter** (not week 9 — it can't carry final recovery
counts before the November recovery); Fainrose chairs the new body in **February**;
Mrs Chain's certificate delivered on a Tuesday in **March**.

| # | Para | Change |
| --- | --- | --- |
| T5 | Ch 6 (~1166) | "the **morning** had become unnaturally bright" → "the **afternoon**…" (Ch 5 already reached afternoon) |
| T4 | Ch 10 (~1562) | "the vertigo she had come, over the **past week**, to recognise" → "…over the **past few days**…" (aligns with Ch 12's three-day span) |
| T4b | Ch 10 (~1568, ~1573) | "**It took** the annex's engineers four days…" → "**It would take**…"; "Lolly opened the green notebook on the drive back." → "**All of that came later. On the drive back that night,** Lolly opened the green notebook." — flags the flash-forward and the return |
| T1 | Ch 16 (~2048) | "The injunction **was granted on the Tuesday** by a judge…" → "The injunction **itself** was granted on the Tuesday, once the plan the Board had demanded on the Monday — as the price of losing the argument — was on the judge's desk. He understood none of the physics…" (Monday = application; Tuesday = the order) |
| T2 / T3 | Ch 15 (~2038) | "when Beatrix filed it **in the ninth week**" → "when Beatrix filed it **that winter**" — the final-count settlement now sits after the November recovery, and para 2039's "over four months" (August → winter) becomes consistent |
| T3b | Ch 16 (~2070) | "the thing she had got, **over four months**, genuinely good at: nothing" → "…**over the winter**…" (removes the second "over four months"; Nov → March) |
| T7 | Ch 16 (~2093) | "a job title she had invented late on a Thursday and **defended for eight months**" → "…and **would spend the next eight months defending**" (makes the eight months explicitly prospective from the February appointment) |
| T6 | Epilogue (after ~2152) | Inserted one line — "**Everything else took the winter.**" — between the "Allegedly./Obviously." exchange and "Mrs Chain was promoted…", so the three-weeks-after statement no longer has to contain the December–February personnel outcomes |

Ch 14's own "three days old" / "In three days" (paras ~1906, ~1915) were left as written —
impressionistic, internally consistent with Ch 12, and not a reader-visible contradiction.

## Applied 10 September (continuity — K1, K2, K7, K8)

Pre-edit file: `English/Schrodingers_Paperwork_BOOK_1_BEFORE_CONTINUITY_BACKUP.docx`.
Re-validated (XSD passes; +1 paragraph).

| # | Fix |
| --- | --- |
| **K2** (Ch 1) | The complaint file "had opened itself on the screen unbidden and had not yet settled on its own fields" *before* Gideon reads it; the third click makes it "resolve itself, all at once, into a shape it had not had a moment before" rather than appear from nothing. |
| **K1** (Ch 3) | Gideon is "folded … into the seat across the aisle" and, when he stumbles, "the bus took a corner" — no kerb, no pavement. He then leaves with a task ("Find out who signed for it" — the requisition archive), which explains his absence from the house and the Fainrose trip and plants the relay-hunt he completes in Ch 15/16. |
| **K7** (Ch 16) | The photograph "had hung on through the whole of it and then been left behind when the old house was condemned"; a man retrieves the physical print — no repeat of the Ch 4 cable-pull. The "burglar" framing (needed for Mrs Chain's inquiry line) is kept. |
| **K8** (Epilogue) | Mrs Chain, a citizen, is "given a seat on the citizens' panel that now had to countersign every continuity order" — not "promoted." The HR joke survives ("tried to process her as a new employee, was corrected at length, and filed the result as a promotion"). |

## Applied 10 September (F1 — appendix teaching lists)

Pre-edit file: `English/Schrodingers_Paperwork_BOOK_1_BEFORE_APPENDIX_LISTS_BACKUP.docx`.
Re-validated (XSD passes; +162 paragraphs, 2,424 → 2,586). Every "The idea, step by step"
and "What the reader learns" block (34 in all) is now a bold label line plus one indented
paragraph per numbered step / bulleted takeaway, with inline term-bolding preserved.
Verified lossless — collapsing the split paragraphs reproduces the original text exactly.

## Applied 10 September (Glossary; front-matter; a pronoun)

Pre-edit file: `English/Schrodingers_Paperwork_BOOK_1_BEFORE_GLOSSARY_FRONTMATTER_BACKUP.docx`.
Re-validated (XSD passes; +46 paragraphs, 2,586 → 2,632; all 43 internal links resolve).

- **Glossary** (new): ~43 alphabetised entries — a crisp definition per term plus the
  chapter that dramatises it — as a reference section after Further Reading. Built from
  the terms the Physics Notes bold on first use; wording consistent with the notes.
- **"A Word on Who Is Who"** moved from front matter to the back (after the Glossary).
  The section already tells the reader to skip it and return after finishing; the move
  makes that structural and keeps first-time reveals intact. TOC updated.
- **Vale** cast entry trimmed: "signs Directive 11-C without reading the second page." —
  the "later suspended / testifies for eleven days" tail was spoiling his arc.
- **K3 (Ch 15):** "She will be recoverable. That is not the same as unharmed." is restored to Fainrose (she says it in Ch 8; unchanged). Ch 15 now has her admit she coined it "week one, in the annex" and then dismissed its weight, while Mrs Chain kept it — a sharper version of the same beat. The notebook page reads "Fainrose's words, jotted the night of the cold vault." Adjacent calendar slip also fixed (de Brévanne's corridor question was Ch 12, not "last month").
- **Ch 3 pronoun:** "Lolly nodded once. She looked at her…" → "Lolly nodded once
  and looked at her. 'That means me,' said Mrs Chain, with a terrible steadiness." (the
  look and the line are now unambiguously attributed).

## Applied 10 September (the two "she" spots + the 78% gloss)

Pre-edit file: `English/Schrodingers_Paperwork_BOOK_1_BEFORE_PRONOUNS_78PCT_BACKUP.docx`.
Re-validated (XSD passes; 3 in-place edits).

- **Ch 4:** "She read the inscription, and for the first time since she had known her, her
  expression shifted…" (three unnamed referents) → "**Beatrix** read the inscription, and
  for the first time since **Lolly** had known her, …" — "her expression" is now
  unambiguously Beatrix's.
- **Ch 12 opening:** the subject slides from Beatrix to Lolly at "By ten she was no use
  to anybody." → "**Lolly**, by ten in the morning, was no use to anybody." (the next
  "she had checked" is then clearly Lolly).
- **Ch 16 (78%):** Mrs Chain's certificate reads 78 %; the district recovered 308 of 411
  (≈ 75 %). Lolly's restraint list now says she is not explaining "that the seventy-eight
  per cent was a figure for her sister and not for the district — arrived at another way,
  and not the three hundred and eight in four hundred and eleven — and that a person was
  in any case a poor thing to render as a fraction." The two numbers can no longer be
  mistaken for the same quantity, and the person-as-percentage reading is refused in the
  narrator's own voice.

## Applied 10 September (author request — Lolly's age)

Not an audit finding. "Forty years in the electronics trade" put Lolly in her
sixties; the character is younger. Changed to **"ten years"** in all eight places it
refers to her (How to Read This Book, Cast, Ch 9, Ch 12 ×3, Ch 13, Ch 16), and the
age-fixing **"in 1983"** physics stint is now circumstantial ("for about eleven minutes,
straight out of university"). Left as-is: Mrs Chain's "forty years of walking" her route
(Ch 8), de Brévanne's / Bellew's "sixty years", and the real author's bio in *A Note on
the Author* ("Mr Musiol spent more than forty years in the electronics industry" — a fact
about Musiol, not Lolly; the author-surrogate wink survives without matching durations).
Pre-edit file: `English/Schrodingers_Paperwork_BOOK_1_BEFORE_LOLLY_AGE_BACKUP.docx`.

## Applied 10 September (author request — Gideon)

Not an audit finding. Following the Lolly-age change, Gideon Wigglesworth is the intended
love interest, so he is anchored as her contemporary and the attraction is made mutual
and visibly pending (Book 1 of a series — a slow burn, kept understated to match the
register):

- **Cast:** "a bench engineer beside her for years before the Ministry claimed them both"
  (his age now tracks Lolly's, and he is, literally, the engineer) + "which Lolly has
  spent years not doing anything about, and Gideon the same years not mentioning."
- **Ch 1:** "They had shared a workbench for the better part of a decade … and had kept
  the habit of each other since" — anchors "for as long as Lolly had known him"; a decade
  matches her ten years in electronics.
- **Ch 3:** as he leaves the bus, "he raised a hand, and held it up a beat longer than a
  wave strictly required" — his side, wordless.
- **Epilogue:** "Gideon's new office was three doors down, a fact Lolly had established on
  the first morning and mentioned to nobody."

Pre-edit file: `English/Schrodingers_Paperwork_BOOK_1_BEFORE_GIDEON_BACKUP.docx`.

## Applied 10 September (whole-manuscript coherence pass — "make it work for the story and the physics")

After a full read of the current manuscript end to end (not just the audit deltas):
narrative, prologue, epilogue, all 17 Physics Notes, Further Reading, Glossary and back
matter. **Verdict: it works.** Both layers hold. The story has a real spine (bureaucratic
premature-resolution = quantum measurement, sustained cleanly across all 16 chapters), a
genuine emotional line (Mrs Chain and her sister), and a deliberate refusal of catharsis
that is earned rather than evasive. The physics is accurate — every "Going deeper"
equation, date and attribution checks out again on this pass — and the "where the popular
version goes wrong" sections remain the strongest thing in the book. This was finishing
work, not a rebuild. Three small committed passes:

### Physics coherence (commit `e64d004`)

| # | Location | Change |
| --- | --- | --- |
| PC1 | Physics Prologue (para ~83) | "This is not the thing hiding its value. There is no value to hide." → "This is not merely the thing hiding an answer it has already picked." The flat version contradicts the sympathetic pilot-wave account in Ch 12 (definite positions, a real guiding wave); the new phrasing matches the hedge the Ch 1 note already uses ("not merely an unknown pre-existing answer"). |
| PC2 | Glossary, *many-worlds* entry | "(Chapter 13)" → "(Chapter 11)". The note that explains many-worlds from nothing is Ch 11's "A closer look" box; Ch 13 only dramatises it mid-argument. Matches the glossary's own practice for every other term. |
| PC3 | Ch 16 (Fainrose reads the monitor) | Added one clause: the coherence number *climbs* to 2.79 because "the houses can finally hold together with one another again — they had been spending all of it on the anchor". A physics-literate reader hits a rising CHSH-type value at the climax and reads it as *more* coupling; this is monogamy of entanglement in plain words. The Ch 15 plant told the reader climbing = success but never why. |

### Prose repairs (commit `392190d`)

| # | Location | Change |
| --- | --- | --- |
| PR1 | Prologue (para ~141) | "Almost anything did, apparently." has had no antecedent since the manuscript arrived — "did" reaches back past an inserted "All was well … Or was it?" aside to "events that had not happened yet" two sentences up. Inserted one deadpan setup line — "The difficulty was deciding what counted as such an event." — so the punchline lands. The "All was well / Or was it?" motif (paired with the epilogue) is untouched. |
| PR2 | Ch 16 (para ~2032) | "Twenty-Two Coldharrow Rise" arrives cold at the top of the certificate scene — the reader last had Mrs Chain at "Equivalent Residence Unit 7B" and does not learn the old house was condemned until 11 paragraphs later (audit finding **N3**, previously flagged, not done). Added one bridging clause: "— where she had been moved when the old house was condemned —". |

### Gideon — close the mid-book gap (commit `7866146`)

Set up in Ch 1 and 3, then absent for eight chapters with no word, then back in Ch 15
doing load-bearing work — so the investigation payoff (he finds the relay) and the
romance payoff (epilogue) both arrived cold.

- **Ch 12:** added Gideon to Lolly's roll-call of where everyone is (he was the one
  omission). Places him in the requisition archive "since the first afternoon", keeps the
  relay hunt warm across the gap, and carries one dry beat of the attraction — she
  rereads his terse notes "once more than its information strictly required".
- **Ch 15:** marked his return from the archive, and made Lolly the one person who never
  stopped noticing him ("everyone except Lolly") — mirrors the epilogue's "mentioned to
  nobody".

The arc is now five understated beats — Cast / shared workbench / the too-long wave / the
reread notes / "except Lolly" / "mentioned to nobody" — rather than a setup and a payoff
with nothing between.

### Looked hard at, left alone (deliberate, not flaws)

- **The four elderly physicists each telling Lolly some version of "you're the outsider."**
  On close reading each has a distinct, speaker-specific angle (de Brévanne: historian
  *and* physicist, never both; von Wittenberg: names the pattern as "not a compliment";
  Bellew → Schrottfinger: the "don't pick until something forces you / you want to know
  what the circuit is" through-line is a deliberate structural rhyme at three load-bearing
  moments). Trimming would cost more than it saves.
- **The library table.** Ch 14 and Ch 16 put von Wittenberg and then Schrottfinger at the
  *same* table by the window over the shut-down carpet showroom. This is deliberate — the
  definite article, and Keinschein sends her there — the spot becomes "where the old
  physicists wait." Ch 12 (de Brévanne) is a different location.
- **The muted climax** (turn the machines off, run the careful boring repair). This is the
  theme, stated outright by Lolly and by the book's refusal of "resolution." Not a
  pacing failure.

### Author decisions (resolved, commit `880e557`)

- **The Heisenberg allusion, Ch 13.** *Decision: soften — keep the weight, drop the
  pointer.* Heitmann's line is untouched ("after everything, it is the only distinction
  I have left that I am still entitled to"); the following sentence loses "box eleven
  about Heitmann's employment between 1939 and 1945" and now reads "Lolly could not read
  it, and thought later that she perhaps could". The shadow survives as suggestion; the
  book no longer makes a checkable claim about the real Heisenberg's wartime record.
- **"One former Ministry official was listed as dead."** (epilogue). *Decision: make it
  Vale, explicitly, with weight.* Rewritten to "Crispin Vale was listed as dead that
  winter … he had testified for eleven days against the directive he had signed, been
  thanked for his candour and blamed for the disorder in the same week … Some time after
  that, he had stopped … a witness who had not been excused." It now closes the thread
  Fainrose plants in Ch 12 and Ch 16 pays off, and the epilogue cutting straight from it
  to Jago's door sign is the chapter's argument in miniature.

## Applied 11 September (epilogue — tonal-balance read-through, commit `b928e9a`)

Full read-through of the epilogue, all 38 paragraphs, for tonal balance. Verdict: the
shape is deliberate and works — comic open → comic pivot → a one-paragraph-per-character
roll-call (mostly comic-to-dry, with a grace note for Pike) → the quiet Lolly/Gideon peak
→ the uncanny thematic coda → the closing joke — with one exception.

The cut from Vale's death (added 10 September) straight into Jago's one-line door-sign
gag had no room between them. The institutional non-pause is already fully made by Vale's
own paragraph ("a witness who had not been excused"); the prose also refusing a beat read
as whiplash rather than a second layer of the same critique — and broke with the book's
own established practice (Ch 16 follows "She did not come back" with a quieter grace note,
not a joke). Added one standalone line: "Nobody minuted that either." — in the book's own
vocabulary (Ch 16 already used "minute" as a verb for the biscuits: "a loss the inquiry
did not minute"), escalating a small joke into something with real weight, and matching
the chapter's existing device for a bare one-line beat between vignettes ("Everything else
took the winter."). No other tonal issues found in the chapter.

## Applied 11 September (appendix — second pass over the Physics Notes, commit `238b122`)

Full re-read of all 17 Physics Notes, the Physics Prologue, Further Reading and the
Glossary, this time checking every equation and citation again with fresh, adversarial
scrutiny and cross-referencing every bolded term against the Glossary entry by entry.
Verdict: the physics itself holds up completely — all 14 equations and every date and
attribution in a "Going deeper" block re-verified correct, with no new factual errors
found. What this pass caught was consistency and completeness, not accuracy:

| # | Location | Finding | Fix |
| --- | --- | --- | --- |
| G1 | Glossary | "black hole" is bolded and formally introduced in Ch 6 but had no headword — only black-hole-*adjacent* entries existed (event horizon, Hawking radiation, information problem, Bekenstein–Hawking entropy). | Added. |
| G2 | Glossary | "entropy" is bolded and defined as step 1 of Ch 16's own numbered sequence, load-bearing for Ch 14b too, but no baseline headword existed (only the black-hole-specific and life-specific variants). | Added. |
| G3 | Glossary | "locality" is bolded and formally introduced as step 3 of Ch 13's numbered sequence; only its opposite, "nonlocality", had an entry. | Added. |
| G4 | Glossary | "syndrome measurement" is bolded in both Ch 8 and Ch 15 as if established vocabulary, with no entry. | Added, pointed at Ch 15 (its clean numbered-step definition, matching how "quantum error correction" itself already points to Ch 15 rather than its first mention in Ch 8). |
| G5 | Glossary | "decoherence" pointed at Chapter 7. Ch 7's own title only claims "the beginning of decoherence"; Ch 10 ("Decoherence and Einselection") is the dedicated account — and, more decisively, the two *later* notes that need to remind the reader what decoherence is (Ch 11, Ch 15) both independently cite Chapter 10, never Chapter 7. | Repointed to Chapter 10 — same principle as the many-worlds fix in the prior pass. |
| N1 | Ch 11, Schrödinger equation | Ch 5 writes the operator with the standard hat, "Ĥ\|ψ(t)⟩". Ch 11 writes the *identical* equation six chapters later as plain italic "H\|ψ⟩", even though its own prose in the same sentence calls H "the system's energy operator". | Added the hat inside the existing run; left the italic styling alone (real textbooks differ on that, and it's a much smaller matter than the missing symbol). |

Also verified directly against the XML (not just the plain-text extraction, which
strips formatting): all 14 equations carry proper OOXML `vertAlign` superscript/
subscript run formatting — T*H*, c³, k*B*, |ψ⟩ etc. all render as real physics notation
in Word/EPUB, not flattened plain text. And every explicit forward/backward chapter
cross-reference within the notes ("next chapter", "Chapter N", "the effect of Chapter
10") was checked and points where it should.

## Applied 11 September (appendix illustrations, commit `c873f49`)

Added one original diagram to each of the 17 Physics Notes (Chapters 1-16, with Chapter
14 split into two), generated with matplotlib rather than sourced stock art (no licensing
question for a commercial book), inserted right after each chapter's "Back to Chapter N"
link and before "In one breath." A consistent palette built from the book's own Heading1
blue (`#2E74B5`); every image carries its own baked-in title and a `docPr` alt-text
description for accessibility; grayscale-safe for e-ink. All 17 were rendered and visually
inspected before embedding, and several went through real fixes on review rather than
being embedded on the first pass: a colinear-arrow bug in the measurement-basis diagram
that made a single incoming beam look like one bidirectional arrow, a "screen" label
colliding with the interference-pattern strip in the superposition and premature-collapse
figures, a missing local-limit/quantum-ceiling bar-chart legend in the Bell/CHSH figure,
and — most substantively — the pilot-wave trajectory diagram initially showing two
highlighted "actual" paths crossing the midline, which is not physically how Bohmian
trajectories behave (they never cross, and there is only ever one actual particle);
redrawn so each slit's fan stays on its own side and exactly one trajectory is bold.
The decoherence figure (Chapter 10) got the most deliberate treatment, at the author's
specific request: an explicit before/after (isolated, still-interfering vs embedded in
environment, one answer settled), titled to tie directly back to the chapter's own Outer
Fenwick moon scene rather than reading as a generic textbook icon.

Validated: XSD passes, +17 paragraphs (one per figure), all 18 image relationships
resolve (17 new plus the original back-cover image), both Chapter 14 images confirmed in
the correct Part One (strings) / Part Two (holography) order.

## Applied 11 September (appendix images — Kindle e-ink grayscale check, commit `d943609`)

The book is bound for Kindle, which for most readers means e-ink: no color at all. The
appendix images (previous entry) were designed and reviewed on a color screen; this pass
checked what they actually look like with the color removed, rather than assuming a
palette that reads fine in color also reads fine in grayscale.

Measured the palette's real grayscale luminance instead of eyeballing it: BLUE (`#2E74B5`)
converts to 102.5 on a 0–255 scale, WARM (`#B5622E`) to 116.9 — only 14 points apart,
close enough that two same-weight solid elements in those two colors can become genuinely
hard to tell apart once desaturated. Converted all 17 images to true grayscale (PIL's `L`
mode, not a resize proxy) and visually inspected every one — not sampled, all 17 — to see
which, if any, relied on that color pair alone to carry a distinction.

**Fifteen of seventeen were already safe**, confirmed by direct inspection rather than
assumption: in each case the color-coded elements also differ in shape (box vs circle,
X-mark vs plain), position (separate labeled subplots), line weight/opacity (one bold
path among many faint ones), or carry a direct text label that disambiguates regardless
of color (bar-chart categories, tile-grid legend).

**Two were not, and both are fixed:**

| # | Location | Problem | Fix |
| --- | --- | --- | --- |
| K1 | Ch 6 (Hawking) | Mass and temperature were two solid, same-weight curves that cross partway through the chart, distinguished only by color — genuinely ambiguous past the crossing point in grayscale. | Made temperature dashed. Color is now a bonus for screen readers; line style carries the distinction on every device. |
| K2 | Ch 16 (long future) | Two of the four era segments (stelliferous / black-hole) landed on nearly identical grays. | Replaced the four-hue fill with a single-hue monotonic ramp (deep blue fading to near-white) — guarantees grayscale separation by construction rather than by luck, and reads better in color too, doubling as "the light going out." |

Both fixes reconfirmed by re-converting to true grayscale after the change (not just
assumed from the code). The other 15 images are pixel-identical to the prior pass.

## Deliberately not done

- **A wholesale rewrite of the Physics Notes prose.** The explanations are already
  accurate and clear (the audit's verdict, unchanged); F1 formatting and the new Glossary
  were the real appendix gains. Rewriting solid teaching prose would be motion, not
  improvement.
- **A broad line-polish / de-repetition pass.** The deadpan agreement-and-correction
  rhythm ("Yes." / "Yes." / "Quite.") is the book's signature; thinning it across 60k
  words risks the voice for little gain. The prose is already tight.
- **F8**: the back-cover blurb embedded as a picture (para 2376). Fine as an external
  cover; if any of that text is meant to be read as back matter, set it live. (F6/F7 —
  heading colour, trim size — are moot: EPUB + audiobook only, no paperback.)

**Correction to F4:** the earlier claim that the document has "one page break" was a
grep miscount (document.xml is a single line). It actually has **27 `pageBreakBefore`,
on 27 of 28 `Heading1` paragraphs** — chapters *do* start on new pages. F3 stands:
`keepNext` is genuinely absent (0 occurrences), so headings can still strand at a page
foot. The single `sectPr` (one section) is normal for a novel and not a problem.

---

## Scope and method

Extracted and read the full narrative, front matter, the physics appendix, the two
character tables, and the embedded image. Parsed `document.xml`, `styles.xml`,
`settings.xml`, `numbering.xml` and the media store directly. Verified all internal
hyperlink/bookmark pairs. Diffed the current file against three prior `.docx` versions.
Spot-checked disputed physics claims against primary sources. This is an editorial and
structural audit, not a full scientific peer review or an exhaustive spelling proof.

No tracked changes and no review comments are present. All 42 internal cross-reference
links resolve to existing bookmarks — **no broken links**. The document has zero external
hyperlinks. Page rendering (pagination, clipping, blank pages) has **not** been visually
certified: no LibreOffice/Word renderer was available in this environment.

---

## NEW findings (not in the 5 September audit)

### N1. The embedded back-cover image is corrupt  ✓ applied 9 Sep

**Priority: High (production).** Location: `word/media/image1.png`, referenced at
paragraph 2376.

The PNG embedded in the current file is damaged. Its ZIP checksum fails, and at the PNG
level one `IDAT` block has a bad CRC and the compressed image stream will not fully
decode (`zlib` error −3, "incorrect data check"). A reader's software will show, at best,
the top band of the image and then breakage; Word may report "unreadable content."

This is a regression introduced on 6 September:

| File | Date | `image1.png` |
| --- | --- | --- |
| `…_BEFORE_PATCH_BACKUP.docx` | 2026-08-28 | **OK** |
| `…_BEFORE_FULL_SYNC_BACKUP.docx` | 2026-08-28 | **OK** |
| `…_BEFORE_AUDIT_FIXES_BACKUP.docx` | 2026-09-06 | corrupt |
| `Schrodingers_Paperwork_BOOK_1.docx` (current) | 2026-09-06 | corrupt (differently) |

The two 6 September files are corrupt in *different* ways, which means whatever tool
edited the document is mangling the binary payload on save. The image is 1318×1977 px.

Recommended action: re-embed the image from a known-good source — either
`word/media/image1.png` extracted from `…_BEFORE_PATCH_BACKUP.docx`, or freshly from
`English/Kindle Back Cover.jpg` (1.6 MB JPEG, intact) — and confirm the CRC is valid
after saving. Whatever process produced the 6 September files should not be used to
write the final manuscript until it stops corrupting media. (This finding is separate
from prior finding 26, which is about whether the back-cover *content* belongs in the
interior at all.)

### N2. Garbled sentence in Chapter 1  ✓ applied 9 Sep (verify wording)

**Priority: Medium.** Location: paragraph 227.

> "Mrs Chain gave her a look which suggested that if she continued in that vein she
> might improve her physically."

"improve her physically" is missing or has lost a word. The intended sense is a dry
threat of violence — e.g. "…she might rearrange her physically" or "…she might have her
improved, physically." Present in all versions back to 28 August; missed by the last
audit's copy-defect table.

### N3. Mrs Chain's address changes without explanation

**Priority: Low–medium.** Locations: Chapter 3, paragraphs 549–552 and 589; Chapter 16,
paragraphs 2027 and 2038.

Mrs Chain's street is "Elm Grove," administratively renamed "Chain Terrace," and her
house is "Equivalent Residence Unit 7B." In Chapter 16 she is at "Twenty-Two Coldharrow
Rise," and the old house is "the scaffolded remains." The move is never shown or
explained, and the reader is left unsure whether Coldharrow Rise is a new house, Elm
Grove restored under yet another name, or an error. One clause bridging this (she was
rehoused while the original was rebuilt / the rename was reversed) would close it.

### N4. Two "other book" pointers sit close together and blur

**Priority: Editorial choice.** Locations: "About the Series" (para 2368) and "If this
made you curious" (para 2370).

"About the Series" promises *Lolly Wren's Curious Science Adventures* Book 2 ("a
different Ministry, in a different country"). Two paragraphs later, "If this made you
curious" points to *The Quantum World* as "the same territory covered by the same
author, at considerably greater length." A reader can reasonably think these are the
same forthcoming book. If both pointers stay, name them so the fiction sequel and the
non-fiction companion are unmistakably distinct.

---

## Re-confirmed open findings (from 5 September, still present)

Numbering follows the 5 September audit. Each item below was checked against the current
file and the quoted text is current. Recommendations there still stand.

### Climax and causal chain

**C1 (prior 1). ✓ applied 10 Sep. The Bell-test result never appears.** Chapter 13 commits the panel to
"a test with a pre-agreed threshold" (para 1832) and Lolly's whole legal theory is: if
the housing-lattice correlation exceeds Bellew's CHSH ceiling of 2, "there were never
nine thousand cases. There was one" (para 1846). Chapter 14 ends on the apparatus fault
— "It's the apparatus measuring itself" (para 1943). Chapter 15 then opens straight into
"Beatrix Sloan won the injunction application on the Monday morning" (para 1946). The
fault is never diagnosed, no valid run is shown, and **no number is ever reported**.
Chapter 16 refers back to "a measurement establishing that they were one act" (para
2005) as something already in the filing system. Even in Chapter 15–16's summary
register, one or two sentences must close this loop: what the fault was, how it was
cleared, what S came back, and that this was the figure Beatrix put in front of Pilbeam.

**C2 (prior 2). ✓ applied 10 Sep. "S" is used in two incompatible senses.** The appendix defines S as the
CHSH quantity with local bound |S| ≤ 2 and quantum maximum 2√2 ≈ 2.83 (para 2288–2289).
The climax has "the display marked S" sit at 1.2 for eleven weeks, then climb to 2.79
after the coupling is cut, which Fainrose reads as "disconnection. Clean disconnection"
(para 2022–2023). As written this is backwards: a CHSH value rising from 1.2 (below the
classical bound) to 2.79 (a strong Bell violation) signals that the parts have become
*more* strongly correlated, not disconnected. Either give the disconnection monitor its
own name and definition, or explain explicitly why a protected pair's S rises once the
unwanted anchor coupling is removed. Right now the book's own appendix contradicts its
climax.

**C3 (prior 5). ✓ applied 10 Sep. Cohort and label arrive undefined.** The suppressed states are "four
hundred and eleven suppressed states" (Chapter 15, para 1958), then "four hundred and
eleven pending states" (Chapter 16, para 2020), then "the four hundred and eleven P-9
states" (para 2007) — three names for one thing, and "P-9" appears with no prior
introduction. Also still unset up: "When Vale froze Sub-District 6" (para 1630, first
mention, treated as known); "Miss Dorothy Kell" (para 2008, no introduction); and Vale
ending the paralysis "precisely as Fainrose had told him he would be" (para 2025 — the
conversation is never shown).

### Calendar

**T1 (prior 3). ✓ applied 10 Sep. Monday vs Tuesday for the injunction.** Chapter 15: "won the injunction
application on the Monday morning" (para 1946). Chapter 16: "The injunction was granted
on the Tuesday" (para 2005), narrated fresh with no signal that this is the same event
seen again or a distinct formal step. Pick one, or distinguish application from order
explicitly.

**T2 (prior 3/4). ✓ applied 10 Sep. The two endings do not nest.** Chapter 15 presents the resolution as
Beatrix's 140-page settlement "filed in the ninth week" (para 1995). Chapter 16 presents
it as the coupling cut on 14 November (para 2020), recovery "over the following month"
(para 2025), and Mrs Chain's certificate delivered "on a Tuesday in March" (para 2026).
These can coexist (a legal settlement of the case vs. individual citizen certificates
months later) but nothing in the text tells the reader that, so Chapter 16 reads as a
second, longer version of an ending Chapter 15 already delivered.

**T3 (prior 4). ✓ applied 10 Sep. "Over four months" does not fit either scene.** The crisis begins in
August (Keinschein in "August light," para 1591). Chapter 15's week-nine scene (para
1996) and Chapter 16's March scene (para 2027) both say Lolly has come to understand
things "over four months" — too long for late October, too short for the following
March.

**T4 (prior 4). ✓ applied 10 Sep. Chapter 10 "the past week" vs Chapter 12 "three days ago."** Para 1538:
Lolly has learned something "over the past week." Two chapters later, para 1676: "Three
days ago I started noticing things in a notebook." The investigation cannot be both a
week old and three days old, and by Chapter 12 it is demonstrably more than a week.

**T5 (prior 4). ✓ applied 10 Sep. Chapter 5 reaches afternoon, Chapter 6 returns to morning.** Para 904:
"The morning had developed into one of those bright English afternoons." Para 1142 (same
continuous day, end of the Fainrose visit): "the morning had become unnaturally bright."

**T6 (prior 4/14). ✓ applied 10 Sep. The epilogue's "three weeks" cannot hold its contents.** "Three
weeks after the incident" (para 2100), the epilogue then reports outcomes that the
narrative dates to January and February — Voller reassigned "in January" (para 2049),
Fainrose appointed and Lolly given her title "In February" (para 2050), Lolly "given a
new desk, the same job title" (para 2120). Place the epilogue after the last dated
events, or drop the "three weeks" anchor.

**T7 (prior 4). ✓ applied 10 Sep. "defended for eight months."** Para 2050: Fainrose is appointed "In
February" and "defended [the job title] for eight months." February + 8 months runs past
the book's own final scene (March). If this is deliberate proleptic narration it still
reads as an error next to a February appointment.

### Continuity and character

**K1 (prior 6). ✓ applied 10 Sep. Gideon's Chapter 3 bus scene is still physically impossible.** They
board the bus (para 563); the bus is moving and the city is changing outside the window
(para 566); Gideon "had joined them by then" (para 568); then Gideon "stepped backwards,
caught his heel on the kerb, and sat down rather abruptly on the pavement" (para 574) —
on a kerb and pavement, from a moving bus; then "they got off at Chain Terrace" (para
589). Put the exchange at the stop before boarding, or after they get off, and give
Gideon a stated reason to peel away (he does not go to the house, and does not reappear
until Chapter 15).

**K2 (prior 7). ✓ applied 10 Sep. Gideon analyses the case file before it appears.** Para 187–189: Gideon
reads "the case file," its field order, and its "present" status. Para 196: "the
appearance of a new case file on the screen" with exactly those fields after "a third
click." Bring the file up before his analysis, or make the third click an update to an
already-visible file.

**K3 (prior 10). ✓ applied 10 Sep. "She will be recoverable" is still attributed to the wrong speaker.**
Chapter 8, para 1365: **Fainrose** says to Mrs Chain, "She will be recoverable. That is
not the same as unharmed." Chapter 15, para 1983–1984: Fainrose says Mrs Chain "told you
that in week one," and the notebook records it as "Mrs Chain's own words." This is a
straight contradiction and one of the clearer errors in the book. Keep Fainrose as the
originator, and if Mrs Chain later adopts the phrase, show her doing so.

**K4 (prior 9). ✓ applied 9 Sep. The cast still calls Fainrose "Lolly's mentor" flatly** (para 135),
although Chapter 5 is unambiguously their first meeting (para 913–938: Fainrose does not
know Lolly and has to deduce she "studied physics once"). "The physicist who becomes
Lolly's mentor" fixes it.

**K5 (prior 28). ✓ applied 9 Sep. The physicist key still calls Keinschein "immaculate"** (para 150
table), but his entrance is "extremely old and radiantly untidy… a great disorganised
nimbus of white hair… a cardigan that had clearly outlived several arguments, and no
shoes" (para 1572–1573). Change the table's adjective (the disguised Heisenberg,
Heitmann, is the "immaculately grey" one, para 1758).

**K6 (prior 11). ✓ applied 9 Sep. Lolly is "he" in the Chapter 6 Physics Notes.** Para 2204: "When Lolly
notices that thermal radiation does not plainly reveal what fell in, **he** reaches the
black-hole information problem." Change to "she." Also para 2095, "in the ordinary
handwriting of a man who had somewhere to be," describing Lolly's hand — defensible as
idiom, but the gendered noun jars; "someone" is safer.

**K7 (prior 13). ✓ applied 10 Sep. The photograph is recovered twice.** Jago's cable-pull restores the
sisters' photograph in Chapter 4 (para 851). In Chapter 16 it "turned up that spring"
via a near-identical cable-pull by an unnamed "man"/"burglar" in "the scaffolded remains
of the old house" (para 2038–2039). No intervening loss is established, and the second
rescuer is left unnamed (presumably Jago). Explain the loss, or make the second recovery
genuinely different.

**K8 (prior 14). ✓ applied 10 Sep. Mrs Chain "was promoted."** Para 2110: "Mrs Chain was promoted. …Human
Resources disagreed." She is established as a citizen, not an employee (para 138). If
this is a deliberate absurdist beat (the Ministry "promoting" a member of the public) it
needs one word of signal; as written it reads as a slip.

### Physics and educational claims

**P1 (prior 15). ✓ applied 9 Sep. Bell-experiment chronology still contradicts itself.** Chapter 7
Physics Notes, para 2218: "experiments beginning with Alain Aspect's 1982 tests found
the quantum correlations instead." Chapter 13 Physics Notes (para 2289) and Further
Reading (para 2352) correctly credit Freedman & Clauser 1972 as the first violation. Fix
the Chapter 7 note to match: "experiments including Freedman and Clauser's 1972 test and
Aspect's later work."

**P2 (prior 16). ✓ applied 10 Sep. Chapter 14 still overstates string theory.** Para 1886: five theories
become one "exactly and provably." Para 2300 (notes): "Replacing points with loops
removes the infinities that had always wrecked attempts to combine gravity with quantum
theory." Para 1878: "the theory has never been tested. Not once." The surrounding prose
is admirably careful ("unconfirmed framework, not an established fact," repeated), which
makes these three absolute phrasings stand out. Soften to: improved short-distance
behaviour; a graviton state that appears unbidden; dualities supported by strong
evidence; and "no direct experimental confirmation" rather than "never tested."

**P3 (prior 17). ✓ applied 10 Sep. "the only occasion."** Para 1902: the Strominger–Vafa count is "the
only occasion on which anyone has ever counted the microscopic states of a black hole
and got the right answer." Unnecessary and unsupported as an absolute historical claim;
the notes (para 2311) already give the correct careful version. Call it a landmark
microscopic calculation for its specified (extremal, supersymmetric) class and drop "the
only occasion."

**P4 (prior 18). ✓ applied 10 Sep. "Always, and by law" / Boltzmann.** Physics Prologue para 124 and
Chapter 16 para 2075 still elevate "any institution promising to make things simpler is
moving complexity somewhere you cannot see" to a law of nature, and para 2075 still tells
the reader to attribute it to Boltzmann. Thermodynamic entropy, semantic complexity, and
the length of an administrative description are not the same quantity. Keep the line as
Schrottfinger's moral argument; in the Chapter 16 notes, add one sentence distinguishing
the metaphor from the second law (and, if you want the information–cost link, name
Landauer's principle rather than Boltzmann).

**P5 (prior 19). ✓ applied 9 Sep (Rovelli line only). Interpretation treated as settled in two places.** Physics Prologue
para 93: "There is no value to hide" — too absolute beside the later, sympathetic
account of definite Bohmian positions. "If this made you curious," para 2370: Rovelli's
*Helgoland* is "prose good enough to make you forgive him for being right" — an
endorsement of one interpretation as true, in a book whose stated discipline is to
declare no winner. "for being persuasive" keeps the joke without the contradiction.

### Formatting and production

**F1 (prior 23). ✓ applied 10 Sep. The appendix's teaching lists are still run-together paragraphs.**
Every "The idea, step by step" block is a single paragraph containing "1. … 2. … 3. …"
(e.g. para 2143, ~710 characters, five steps). Every "What the reader learns" block is a
single paragraph of inline "- " hyphens. That is roughly 32 dense blocks across 16
sections. A list infrastructure already exists in `numbering.xml` (bullet + decimal
formats defined); the steps and takeaways should use it. This is the single biggest
readability problem in the book on a phone or e-reader.

**F2 (prior 25). Title-page spacing is 12+ consecutive empty paragraphs** (paras 10–21,
plus 0, 5, 6). Use real paragraph spacing and page breaks instead.

**F3 (prior 24). Headings have no "keep with next."** Confirmed: zero `keepNext` in the
styles or the document. In any paged output a heading can be stranded at the foot of a
page. Set it on the heading styles.

**F4 (new detail under prior 24). ~~one section with one page break~~ — see the 10 Sep correction above; chapters do start on new pages.**
The entire 59,000-word book contains a single `sectPr`, one manual page break, and one
`pageBreakBefore`. Chapters currently run straight on from one another. For any print
interior, chapters (and the appendix sections) need to start on a new page — set
`pageBreakBefore` on `Heading1` (and decide the rule for `Heading2`). For reflowable
EPUB this matters less, since most converters split on Heading 1, but it should still be
made explicit.

**F5 (prior 24). ✓ applied 9 Sep. Proofing language is US English.** `settings.xml` themeFontLang and the
style defaults are `en-US`, but the prose is British ("colour," "-ise," "whilst,"
"maths"). Set the document default to en-GB so spell-check stops fighting the text.

**F6 (prior 24). Heading colour is blue** (`2E74B5` on `Heading1`). Fine for EPUB;
becomes grey in a monochrome print interior. Decide per output.

**F7 (prior 24). Trim size undecided.** The document is US Letter, 8.5×11, 1-inch
margins — a textbook/manual page, not a novel. If a KDP paperback is planned, choose a
trade size (5×8, 5.25×8, or 6×9) before treating this file as a print interior. If the
product is EPUB + audiobook only (as the folder suggests), this is moot and only F1/F5
and the content findings matter.

**F8 (prior 26). Back-cover marketing copy is embedded as a picture.** Independent of
N1: paragraph 2376 is a ~1300×1980 image carrying substantial readable text (blurb,
character notes, "for readers of Good Omens…"). If any of that is meant to be read as
back matter, set it as live text so it reflows and is accessible; if it is only the
external back cover, decide whether it belongs in the interior file at all.

---

## Recommended revision order

1. **Re-embed a clean back-cover image (N1)** and stop using the tool that corrupted it
   for final output.
2. **Rebuild the Chapter 13–16 spine (C1–C3):** show the Bell fault resolved and the
   number reported; define S once and keep it; introduce the 411/P-9 cohort, Sub-District
   6's freezing, Dorothy Kell, and Vale's decision before they are relied on.
3. **Fix the calendar (T1–T7):** build a private chronology with real dates and elapsed
   days, reconcile the two endings, then replace the relative durations.
4. **Continuity and attribution (K1–K8, N2, N3):** the bus scene, the early case file,
   the "recoverable/unharmed" speaker, the cast's "mentor" and "immaculate," the "he" in
   the Chapter 6 notes, the double photograph, Mrs Chain's promotion and address, and the
   para 227 sentence.
5. **Physics phrasing (P1–P5):** the 1972/1982 chronology, the three string-theory
   absolutes, "the only occasion," "Always, and by law"/Boltzmann, and the two
   settled-interpretation slips.
6. **Formatting and production (F1–F8):** convert the appendix lists, fix the title page,
   enable keep-with-next and chapter page breaks, set en-GB, and settle trim size and
   heading colour against the intended outputs. Then render and inspect.
7. **Covers (prior 27):** decide whether the cover art is literal or symbolic and
   reconcile it with the character descriptions if literal.

The draft does not need its voice touched. It needs the events, the dates, the
attributions and the claims to agree with one another, and it needs a clean image file.
