# Book summary — The Relativistic Investigation Bureau, Book 1: "The Murder That Hadn't Happened Yet"

Read this first. Only open the full manuscript for things that genuinely need it — continuity checks, exact wording, placing new content. Check `git log` before re-running any mechanical audit; it may already be done.

## Canonical file

Working file: `manuscript_text.txt`. Rebuild the Kindle `.docx` with `rebuild_kindle.py` after text edits. Demo URL: `https://lotmus.github.io/relativistic-site/`. Lives in the `lotmus/My-Books-for-Amazon` monorepo at `The Relativistic Investigation Bureau - SERIES/` (branch `main`).

A separate copy exists under `WORD/` (originally `D:\...\WORD`, its own independent git repo, no remote). **Not canonical.**

`bak/` — pre-git backup archive. Do not touch.

`CHARACTER_AND_SETTING_BIBLE.md` — looks/sound/smell/attitude for the main cast and key settings, compiled from what's actually in the manuscript. Check here before writing new descriptive material for an existing character so it stays consistent.

## Structure

- Front matter → PROLOGUE → 16 Chapters (fiction) → EPILOGUE → Coming Next (YESTERDAY sting) → COURSE
- APPENDIX: 16 Lessons. Forward arrows follow the **physics object**, not matching integers (Ch3→L2, Ch5→L3, Ch6→L5 … Ch16→L15; Epilogue has a formal `-> Lesson 16` after the kettle, plus the skip-line after Coming Next). Reverse arrows match the object (L1→Ch1, L3→Ch5, L4→Ch4, L16→Epilogue).
- Back matter: SUMMARY, Glossary, About the Author, Further Reading (start-here list), Acknowledgements, Bibliography (17 real, verified books — never fabricate citations).
- `manuscript_text.txt` — canonical working text. Rebuild the Kindle docx from this file; do not treat the docx as a second original.
- `kdp_description.docx` — the actual Amazon product listing copy. Keep it free of anything but the sales description itself.
- Companion interactive physics demos live at `https://lotmus.github.io/relativistic-site/` (`github.com/lotmus/relativistic-site`). The book's hyperlinks (front matter + Lessons 2, 5, 15) point at that live Pages URL.

## Plot (Case 1047)

Derek Gent gets a Bureau email: he'll be murdered tomorrow, timestamped and photographed. Investigation via relativity: SR (Lorentz transform) can't explain the ~2-hour clock discrepancy (would need faster-than-light relative motion) → GR/gravity doesn't fit either → clocks across London and Munich desynchronize anomalously → Julius Barbarian argues time may not be fundamental → holography/multiverse detours → resolution (Ch16, via Sherlock the dolphin): Death, Departure, and Arrival aren't three events, they're **one event under three different coordinate labels** — a filing error ("Pending Geometry"), not a murder. Derek was never going to die. Ends on a cliffhanger for Book 2.

Physics is the literal plot engine throughout, not decoration — the mystery's solution *is* the physics lesson.

## Main cast (+ real-physicist analog — explicit author instruction: "physics is theirs, private lives are wholly invented")

- **Derek Gent** — protagonist, Bureau founder, dry wit, deflects with humor. No driving licence. Seventeen years in the field (deliberate use of the book's "17" motif, used twice — Ch1 and Epilogue; this note previously said 23, which was stale/wrong — verified against the actual text 2026-09-27). Father to Sophie, cousin to Penny, unresolved romantic tension with Tabitha.
- **Penny Gent** — Derek's cousin. Sharp, impatient, intuitive counterpart to Trevor's literalism.
- **Trevor Boltzman** — junior colleague. Hyper-literal, anxious, genuinely brilliant at maths, comic relief. Sister: Tabitha.
- **Alfred Weinstein** — Einstein analog.
- **Herbert Matkowski** — Minkowski analog.
- **Julius Barbarian** — Julian Barbour analog (relational/timeless physics).
- **Sophie** — Derek's 12-year-old daughter. Kept her own notebook tracking the lying clocks; the surveillance-car/license-plate thread pays off in the Epilogue.
- **Tuppence** — Sophie's mother, Derek's ex. On-page as a 9:16 voicemail overlapping the murder email ("Relativistic, my arse"). (If "Miranda" ever appears anywhere, that's a leftover bug from an earlier draft — fix it.)
- **Tabitha** — Trevor's sister. Seeded Ch1 (unanswered text) and Ch9 (phone face-down); arrives Ch15 with Gucci.
- **Sherlock** — a dolphin, remote Bureau consultant, telepathic. Planted Ch5 as REMOTE CONSULTANT NOTE (Miscellaneous Marine / mackerel) after Trevor asks "Sherlock who?"; delivers the Ch16 resolution.
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
- **Dialogue tags**: as of 2026-09-24, "said" is no longer the default workhorse by explicit user instruction, but it's not banned either — after an initial full-elimination pass, the user clarified "said can be used sometimes," so 13 of the ~65 replaced tags were reverted back to plain "said" (a well-spread sample, picked from the most neutral/interchangeable synonym choices — explained/clarified/suggested/confirmed/stated/reflected/answered/instructed/observed/replied). The remaining ~52 keep their fitted synonym. If more dialogue is added later: don't make "said" the reflexive default the way most fiction does, but it's a legitimate occasional choice, not a word to avoid on principle. Varied synonyms are often deliberately funny — a grandiose verb for a terse one-word answer is this book's dry humor, not a flaw to flatten. Only add a tag where the speaker would genuinely be unclear without one. Don't reuse the exact same tag phrase for the same speaker within one exchange (some reuse across distant scenes is fine and natural).
- **Speaker attribution risk**: watch for "[Name A] [action]. [Name B] [reaction verb]. '[Quote]'" — the quote can misattribute to whichever name sits immediately before it, even when it actually belongs to the earlier-mentioned character. Verify by content logic, not proximity. (Found and fixed two real instances of this bug this session.)
- **Physics accuracy is load-bearing** — this book had a real error (a gravity-direction sign flip in Lesson 3) that contradicted the very next paragraph in the same lesson. Always sanity-check directional/sign claims, especially gravitational vs. velocity time dilation (they can point opposite ways for the same scenario).
- **Never fabricate bibliography citations** — only add real, independently-verifiable books.
- **Headlines**: all real section headings (chapters, lessons, front/back matter) are uniformly Amazon Ember, 18pt, bold, `#0C447C`, centered, as direct formatting. Since 1 Oct 2026 the top-level ones also carry Word's Heading 1 style plus a page break before (Author's Note, Copyright Stuff, Reality Check and the syllabus-page WORKSHOP pointer are Heading 2, no break), so Kindle builds navigation from them. Subtitle lines stay plain. The front Table of Contents entries are plain hyperlinks to section bookmarks, never headings.

## Known-clean state (as of 2026-09-24)

Structural integrity fully verified: 0 duplicate paragraphs, 0 dead cross-reference links, 0 dangling bookmarks, 17/17 images connected, all 49 headlines uniformly styled. Two full read-throughs done on both the novel and the appendix (the second combined with a systematic said-synonym audit), catching ~19 line-level defects the first pass missed: paragraphs missing their quote marks entirely, a couple of genuinely garbled/merged sentences, a duplicated line, a dangling sentence fragment, an Americanized/lowercase "earth", and 2 more dialogue-tag repeats within a single exchange.

**Overused-word pass (2026-09-24)**: a word-frequency audit found several narrative "beat" verbs badly overused with zero internal variety - "nodded" (213 uses), "smiled" (237), "frowned" (81), "pointed" (81), plus body-orientation "turned" (~28 of its uses). Fixed all of them, choosing per-instance replacements for tone/character rather than cycling a word list. **Note for future passes**: the first attempt at both "nodded"→gesture-verbs and "frowned"→"brow furrowed" overcorrected into a *new* single dominant phrase (verified by re-running the frequency check after the edit, not assumed) - both needed a second pass to spread across a genuinely balanced set of alternatives. Always re-check frequency of whatever you just introduced before calling a word-variety pass done. "Looked"/"stared"/"watched"/"glanced" etc. were checked and already have healthy variety (761 uses spread across a 12-word family) - don't "fix" those.

## Physics appendix audit (2026-09-24)

Checked two things that hadn't been specifically verified: (1) whether Lessons 11-12 (holography, "Cinema Interpretation") caveat speculative material as carefully as the rest of the appendix caveats settled physics - they do, arguably better than average pop-physics writing (Lesson 12 opens with an explicit "Optional detour... not evidence on the same footing as the Lorentz transformation," and both lessons repeat "not proof"/"not evidence for a multiverse" throughout). (2) A full equation sweep across the whole appendix - Lorentz transform, both spacetime-interval sign conventions (Lesson 2 uses c²Δt²-Δx², Chapter 7's novel scene uses the opposite convention, and the novel explicitly lampshades this as "depending on sign convention" rather than hiding it), Bekenstein-Hawking entropy scaling, length contraction (exit-ticket numeric answer checks out), the metric tensor, and the Einstein field equation are all standard and correct. No fixes needed from either check.

## Cover byline mismatch - RESOLVED 2026-09-24

Was: `Kindle Front Cover.jpg`/`.png` and the Audible cover read "S.G.R. / Sven Gerald Rupertson" (an earlier candidate pen name, also visible in `bak/junk/SGR_Sven_Gerald_Rupertson_...` filenames) instead of the manuscript's actual developed pen name, Spezala Genara Relavi. User regenerated the front cover and Audible cover with the corrected byline same day - both now read "Spezala Genara Relavi" correctly. Re-verify if either is regenerated again.

## Back-cover pronoun mismatch - RESOLVED 2026-09-24

Was: About the Author blurb on the back cover called Spezala Genara Relavi "He" instead of "She" (manuscript's back matter, paragraph ~6398, is explicit she/her). `Kindle Back  Cover.jpg` was regenerated same day with the fix ("She has no formal qualifications..."), confirmed correct. The stale duplicate `rib back cover.png` (still had the old "He" text, unused) was deleted from the repo.

Check `git log` for the detailed history before assuming any of this needs redoing.

## Keep-and-reassign pass — 2026-09-29

Working file is `manuscript_text.txt`. Rebuild Kindle with `rebuild_kindle.py`.

What moved, not cut:
- How to Read no longer solves the drawer. Sherlock dump left the Prologue; marine/mackerel lives at the Ch5 consultant note after "Sherlock who?"
- Tuppence's "Relativistic, my arse" is a 9:16 voicemail overlapping the murder email. Tabitha seeded Ch1 (unanswered text) and Ch9. Klein bottle on Trevor's desk from Ch1.
- One Munich call (Ch3). Ch4 is the same Wednesday in Schwabing, then joins the call that already happened. Barbarian named on that line.
- The photograph shows three times and no nouns. Penny's margin guesses death, departure, and arrival. The file does not agree until Chapter 16, where one event under three labels is the inference, not a caption they were handed. The wall clock at eleven seventeen is not the brass clock at 11:03:17.
- Ch9 keeps the death-coordinate warning and does not name the triad or call it one structure. Paid in Ch16: Derek almost smashes the brass clock; second hand starts past 11:03; Penny: "Don't complete the coordinate." Derek and Penny close the case there; Sherlock witnesses.
- Ch15 keeps the boarding refusal and does not name the triad.
- YESTERDAY sting is the last page of the novel, before COURSE. The film list lives on the COURSE page, and each lesson ends with that same one-line reminder. Lesson 16's film is Christian Marclay's The Clock. Lesson 16 keeps the office and the platform as two places; 11:03, 11:17, and 12:04 are labels in the file's wrong noun, and Penny's margin nouns are not the file's caption. Lesson 12 is a drill. Lesson 13 is Module B (tides), taught late for Chapter 14. Lesson arrows follow the object. Bibliography 17; Minkowski line unmixed (Perrett–Jeffery Methuen/Dover, not the Calcutta volume). Further Reading is the start-here shelf.
- Chapter 1 does not confirm that the filing joke is the diagnosis. Sherlock does not announce a sequel; he says the drawer is shut and the corridor is not. The epilogue's open questions (Tabitha's text, the note in Derek's hand) stay open inside that week. Trevor does not spend "the rest of his professional life" inside the epilogue. Sophie's brass clock was tested seventeen times, not kept for seventeen weeks. The Greece figure is the flight, about twenty billionths of a second, not a week on a terrace.
- Ch1 Look Inside: email then photograph/Sophie/school/Tuppence, then Bureau rooms. How to Read, Author's Note, and the long copyright joke sit after Chapter 1. Front TOC lists every novel chapter (not a collapsed 3–16 line).
- Apple reconstructed-trajectory teaching lives in Lesson 5. Ch13 is titled The Wrong Kind of Multiverse. Derek and Penny close Case 1047; Sherlock witnesses. Workshop sits after Lesson 2. Julius is not named as Julian Barbour. Demo URL and live Stanford URLs (spacetime2.html, qanda.html) are printed. The old qframe3.html Q&A frameset is dead; do not restore it.
- Places: Barbarian and Weinstein are both in Munich (S-Bahn, not a return from another country). The train that had already arrived takes the Bureau from London-bound-for-Munich to the Louvre. Ch8 tags the return to London. Weinstein has no London door. Coming Next is a *new* file, not a rewrite of Case 1047's LOCALHOST sender. Ch10 `ARRIVAL: YESTERDAY` is a dream plant, not Book 2 already happening.
- `The_Murder_That_Hadnt_Happened_Yet_Additions_Packet.docx` (25 Sep 2026) is fully merged or superseded. Archived to `bak/`. Do not re-apply. Left unused on purpose: YouTube pile (book uses the demo + Norton + Stanford), HTML `toc_lesson_*` anchors (no HTML edition), Sherlock-in-Prologue (moved to Ch5), extra per-chapter glossary arrows (one object-true arrow instead), Lesson 8 Death/Departure spoiler, Ch7 Underground insert (Ch7 is the Louvre), Pound–Rebka “one percent” (1960 result was ~10%). Last leftover used: glossary line for Einstein synchronisation.


## Session of 1 Oct 2026 (one session owns RIB Book 1, Flamingo and the Tower; no git)

Backups of every file changed: `C:\Users\lomus\OneDrive\My Books for Amazon - session backups\2026-10-01 RIB-Flamingo-Tower\` (outside the repo).

- **Chapter 13, The Wrong Kind of Multiverse**, rewritten (about 650 → 1,630 words). Same beats (cinema, *Everything Everywhere All at Once*, texts with Derek, the cucumber, "Investigate the descriptions", the Rule line and arrow). The physics is now exact: real multiverses (beyond our horizon, Everett branches) cannot be visited, and anything you can see is in your universe, so Other-Derek cannot come from another branch. Clock readings at one coincident event are agreed in every frame; distant simultaneity is not. Invariants are the interval and causal order. "Reality should survive a change of stationery" matches Lesson 12 Drill 4. Ends on the ticket stub marked DESCRIPTIONS. It does not name the death/departure/arrival triad (still Chapter 16's to name).
- About 18 broken "Then at the clock." fragments left by the verb-variety pass were repaired (Chs 4, 5, 7, 9, 12, 14). Also: "Penny confirmed. 'Again?'" → "Penny groaned."; "rapped his knuckles against the Bureau's computer" → "checked"; "Weinstein watched the photograph" → "studied". A stray final "." line was removed.
- `rebuild_kindle.py` fixes: real Heading 1/2 styles and page breaks; the 22-entry front TOC is hyperlinked to bookmarks (prologue, chapter_N, how_to_read, interlude, epilogue, coming_next, course); TOC lines are no longer formatted as 18 pt headings; the body sentence "Chapter 16's resolution turns on…" is no longer turned into a heading ("Chapter "/"Lesson " lines are headings only as bare labels); document properties set (title, subject, en-GB, author blank instead of "python-docx"). The pre-fix script is in the backup folder.
- Result: 64,082 words, 48 Heading 1 + 4 Heading 2, 110 hyperlinks (104 internal, 0 dead), 5 images.
- KDP files: `KDP_METADATA.txt` (word count, 3 categories, language, real content note since nobody dies, bio from the book's own About the Author, corrected marketing angles), `KDP_LAUNCH_CHECKLIST.txt` (ticked/annotated; corrected page-break, .mobi, cover-format, ISBN, Countdown-vs-Free advice), `kdp_description.docx` (now only the sales copy).
- Still Lothar's: author name (and matching cover byline), launch date, KDP account/tax/bank, optional 1600×2560 cover re-export, whether the nonfiction "Physics, Actually" series named in One Last Thing exists under that title.
- Do not renumber chapters: RIB Book 2 cites Book 1 chapter numbers.
- Note: `rib back cover.png` (said deleted above, with the old "He" text) is present again in the folder (dated 20 Sep). It is unused; left untouched.
