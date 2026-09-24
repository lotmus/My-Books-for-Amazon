# Book summary — The Relativistic Investigation Bureau, Book 1: "The Murder That Hadn't Happened Yet"

Read this first. Only open the full manuscript for things that genuinely need it — continuity checks, exact wording, placing new content. Check `git log` before re-running any mechanical audit; it may already be done.

## Canonical file

`FINAL_REV10_The_Murder_That_Hadnt_Happened_Yet_KINDLE_READY.docx` at the repo root. Git repo, branch `main`, remote `github.com/lotmus/relativistic`. ~6,800 paragraphs, ~60K words (novel + physics appendix).

A separate copy exists under `WORD/` (originally `D:\...\WORD`, its own independent git repo, no remote). **Not canonical.** As of 2026-09-24 everything genuinely valuable there was already superseded by this file — don't merge from it again without checking first.

`bak/` — pre-git backup archive. Do not touch.

## Structure

- Front matter → PROLOGUE → 16 Chapters (fiction) → EPILOGUE
- APPENDIX: 16 Lessons (nonfiction physics course), each paired 1:1 with a fiction chapter via cross-reference links (`-> Lesson for this chapter: N` / `<- Chapter for this lesson: N`)
- Back matter: SUMMARY, Glossary, About the Author, Further Reading, Acknowledgements, Bibliography (9 real, verified books — never fabricate citations). Covers SR/GR/time broadly plus one book per major detour topic (Barbour for relational time, Susskind's *The Black Hole War* for Lesson 11's holography/black-hole-entropy content).
- Companion interactive physics demo site in `demos/` (SR/GR/cosmology), meant for GitHub Pages from the repo root

## Plot (Case 1047)

Derek Gent gets a Bureau email: he'll be murdered tomorrow, timestamped and photographed. Investigation via relativity: SR (Lorentz transform) can't explain the ~2-hour clock discrepancy (would need faster-than-light relative motion) → GR/gravity doesn't fit either → clocks across London and Munich desynchronize anomalously → Julius Barbarian argues time may not be fundamental → holography/multiverse detours → resolution (Ch16, via Sherlock the dolphin): Death, Departure, and Arrival aren't three events, they're **one event under three different coordinate labels** — a filing error ("Pending Geometry"), not a murder. Derek was never going to die. Ends on a cliffhanger for Book 2.

Physics is the literal plot engine throughout, not decoration — the mystery's solution *is* the physics lesson.

## Main cast (+ real-physicist analog — explicit author instruction: "physics is theirs, private lives are wholly invented")

- **Derek Gent** — protagonist, Bureau founder, dry wit, deflects with humor. No driving licence. 23 years in the field (deliberate callback number, used twice — Ch1 and Epilogue). Father to Sophie, cousin to Penny, unresolved romantic tension with Tabitha.
- **Penny Gent** — Derek's cousin. Sharp, impatient, intuitive counterpart to Trevor's literalism.
- **Trevor Boltzman** — junior colleague. Hyper-literal, anxious, genuinely brilliant at maths, comic relief. Sister: Tabitha.
- **Alfred Weinstein** — Einstein analog.
- **Herbert Matkowski** — Minkowski analog.
- **Julius Barbarian** — Julian Barbour analog (relational/timeless physics).
- **Sophie** — Derek's 12-year-old daughter. Kept her own notebook tracking the lying clocks; the surveillance-car/license-plate thread pays off in the Epilogue.
- **Tuppence** — Sophie's mother, Derek's ex. (If "Miranda" ever appears anywhere, that's a leftover bug from an earlier draft — fix it.)
- **Tabitha** — Trevor's sister, introduced late (Ch15). Has a dog, Gucci.
- **Sherlock** — a dolphin, remote Bureau consultant, telepathic. Delivers the Ch16 resolution.
- **Mrs Marsh / Mr Pendleton** — building staff, recurring bureaucratic-comedy bit players ("Pending Geometry is drawer three. Murder is drawer one.").

## Running motifs — don't break these

- **"Pending Geometry"** — the drawer/case-status for a misidentified event; the book's thematic resolution.
- **The "17" motif** — 11:03:17, seventeen seconds, etc. Pays off literally: a brass plate engraved "17" late in the book.
- **LGV** on the mystery clock — red herrings (Local Gravitational Vector, Large Goods Vehicle) before the real answer: *Ligne à Grande Vitesse* (French high-speed rail).
- **"Virtuality" / Open-Door Principle** — closed office door = occupied ("working hard... or shagging, equally hard"); open door = person elsewhere. Paid off for Derek/Tabitha in the Epilogue (Gucci waiting outside Derek's closed door; Trevor applies the rule and doesn't knock) — this is also what the "Coming Next" tease's "Gucci had already worked it out" line refers to.
- **The ordinary cucumber** — Penny's running physics-experiment prop.
- **Trevor's Klein bottle** — a desk ornament (Ch1), a non-orientable surface with no well-defined inside or outside. Paid off in Lesson 11 as an explicit non-example: it's unrelated topology, not holography — the joke is the contrast, not an equivalence.
- **Tea-order callback** — "Yes."/"Milk?"/"No."/"Sugar?"/"One.", identical in Ch1 and Epilogue. Derek changes his order to "Two" in Ch1 (pre-death anxiety); does *not* in the Epilogue (at peace). Keep both instances textually identical if either is ever touched.

## Style rules established this session

- **British spelling throughout** — realise/organise/analyse/coloured/labelled, "lift" not "elevator", maths not math, petrol not gas, biscuits not cookies. Already scrupulously consistent; watch for stray Americanisms in anything new.
- **Dialogue paragraphing**: default is one line per paragraph — the book's dominant investigative Q&A rhythm (~50 runs of 5+ consecutive short lines). This is intentional; don't "fix" it. Exception: warm/intimate short exchanges between characters who know each other well get bundled into a single paragraph with manual line breaks between lines (not merged into flowing prose, no extra paragraph-spacing gap between the lines). Used sparingly — tea order, a couple of Penny/Derek banter beats. Don't apply broadly.
- **Dialogue tags**: "said" is the workhorse (~97 uses). Varied synonyms (queried/opined/affirmed/maintained/stated/etc., ~70 uses) are fine and often deliberately funny — a grandiose verb for a terse one-word answer is this book's dry humor, not a flaw to flatten. Only add a tag where the speaker would genuinely be unclear without one. Don't reuse the exact same tag phrase more than once within a single extended exchange.
- **Speaker attribution risk**: watch for "[Name A] [action]. [Name B] [reaction verb]. '[Quote]'" — the quote can misattribute to whichever name sits immediately before it, even when it actually belongs to the earlier-mentioned character. Verify by content logic, not proximity. (Found and fixed two real instances of this bug this session.)
- **Physics accuracy is load-bearing** — this book had a real error (a gravity-direction sign flip in Lesson 3) that contradicted the very next paragraph in the same lesson. Always sanity-check directional/sign claims, especially gravitational vs. velocity time dilation (they can point opposite ways for the same scenario).
- **Never fabricate bibliography citations** — only add real, independently-verifiable books.
- **Headlines**: all real section headings (chapters, lessons, front/back matter) are uniformly Amazon Ember, 18pt, bold, `#0C447C`, centered — applied as direct formatting, not paragraph style. The Table of Contents listing (which repeats the same titles as small nav entries) is deliberately excluded from this.

## Known-clean state (as of 2026-09-24)

Structural integrity fully verified: 0 duplicate paragraphs, 0 dead cross-reference links, 0 dangling bookmarks, 17/17 images connected, all 49 headlines uniformly styled. Full read-through done on both the novel and the appendix. Check `git log` for the detailed history before assuming any of this needs redoing.
