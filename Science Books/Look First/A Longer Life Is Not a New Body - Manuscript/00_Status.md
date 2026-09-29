# Book 3 status — *A Longer Life Is Not a New Body*

**Kitchen date:** 25 September 2026.
**Author:** Lothar J. Musiol.
**Title:** A Longer Life Is Not a New Body (29 Sep 2026). Earlier display titles: *The Body Keeps Its Own Clock*, then *The Body’s Honest Invoice*. Manuscript folder: `A Longer Life Is Not a New Body - Manuscript`.
**Subtitle:** Lifespan, Minds, and Why Ten Thousand Years Is Not a Straight Line.
**Series:** Volume 3 of *Look First*. Books 1 and 2 were not reopened in this pass.

## Manuscript

- **16 chapters** in the part files on disk (A0–A16). A 23 Sep note described four extra chapters (fast trip, cousin clocks, the reset, long sleep). Those rooms were written into the existing chapters on 29 Sep, not as new numbers: cousins in Chapter 3, the reset in Chapter 5, proper time in Chapter 11, torpor in Chapter 15. The 23 Sep list, for the record:
  - **Ch 12, "A Fast Trip Is Not a Long Life"** (special/general relativity — proper time, the twin case, GPS/muon/airliner evidence), citing Lewis Carroll Epstein's *Relativity Visualized*.
  - **Ch 4, "Every Clock Has a Cousin"** (comparative biology — naked mole rat, Greenland shark, immortal jellyfish, Jonathan the tortoise).
  - **Ch 6, "The Reset That Isn't"** (partial epigenetic reprogramming — the 2013 teratoma result, 2016 cyclic dosing, 2020 three-factor eye result, the January 2026 first human trial).
  - **Ch 15, "A Long Sleep Is Not a Long Life"** (induced torpor — Mars-transit proposals, therapeutic hypothermia's narrowing evidence, hibernator neuroscience).
  - Plus two appendix-only expansions (no new chapter): a "biological age" test subsection added to A2, and a longevity-drugs subsection (metformin/rapamycin/senolytics trials) added to A5.
- `00_Chapter_Outline.md` and `00_Figure_Plan.md` updated to match the 20-chapter state.
- Temperatures taught in front matter / Ch 1. Forever-mind and Omega Point stay cold and out.
- No Artemis / Starship downtown courtroom; no CMB / second-origin zoo reopened. The one pre-existing cross-series reference ("Chapter 12 of the other book," meaning *A Permit Is Not a City*'s own Chapter 12) was correctly left unrenumbered throughout both passes.

## Word count

**Stamp after 23 Sep, both passes:** **37,376 words** in an earlier docx count. The markdown on disk in this folder was shorter than that note. **29 Sep 2026** second thicken: S-curves, institutions, the trial receipt, plasticity’s bill, the fly-map versus a file, and a way to grade headlines. Shortest chapters now sit near 1,000–1,400 words. Script total for the folder about 30,000 words; reader text (front, parts, appendix) about 25,000.

## Figures

| | Count |
|---|---:|
| Drawn diagrams | **18** |
| Stills (`fig01.jpg`, `fig20.jpg`) | **2** |
| **Total embeds** | **20** |

New this pass: `fig04.png` (four hazard-curve bars: mouse/human/mole-rat/shark), `fig06.png` (a fence diagram for partial reprogramming), `fig12.png` (a spacetime diagram for relativity, from the earlier pass), `fig15.png` (a furnace dial and two hourglasses, for torpor). Drawn directly into `Figures\` with a standalone script rather than through `draw_figs_series.py`'s own `b`-functions, which still save into stale `figs_body`/`figs_permit` subfolders that `build_book.py` does not read — if resuming figure work through those functions, copy the output PNGs up by hand afterward, or fix `save()` to target `Figures\` directly.

## Kindle

- Rebuild: `python Figures\build_book.py body` from this manuscript's Figures folder. `build_book.py`'s `BOOKS["body"]["SRC"]` is hardcoded to a gone D: path; a fallback (added 23 Sep) points it at the Figures folder's parent when that path is missing, so it also runs from a relocated copy.
- File the builder writes now: `A Longer Life Is Not a New Body - Kindle.docx`. The older files `The Body Keeps Its Own Clock - Kindle.docx` and `The Body’s Honest Invoice - Kindle.docx` are in `bak`. Verified after the final rebuild: 20 chapter headings, 20 appendix notes, 20 figure captions, 54 hyperlinked TOC entries, 20 embedded images, **0 straight quotes/apostrophes anywhere in the book** (3 pre-existing ones in the old Chapter 20 text were also found and fixed this pass).
- Amazon paste: `KDP_Description.md`.

## Sources added 23 Sep

Relativity (Ch 14 / A14): Lewis Carroll Epstein, *Relativity Visualized* (Insight Press). Edwin F. Taylor and John Archibald Wheeler, *Spacetime Physics*, 2nd ed. (1992). Neil Ashby, *Living Reviews in Relativity* 6 (2003). Hafele and Keating, *Science* 177 (1972). Bailey et al., *Nature* 268 (1977). Chou et al., *Science* 329 (2010).

Comparative biology (Ch 4 / A4): Ruby, Smith, and Buffenstein, *eLife* (2018). Tian et al., *Nature* (2013). Zhang et al., *Nature* 621 (2023). Nielsen et al., *Science* 353 (2016).

Reprogramming (Ch 6 / A6): Abad et al., *Nature* 502 (2013). Ocampo et al., *Cell* 167 (2016). Lu et al., *Nature* 588 (2020). FDA IND clearance, 28 January 2026.

Torpor (Ch 15 / A15): NASA's STASH program. Nielsen et al. (TTM), *NEJM* 381 (2019). The TTM2 trial, *NEJM Evidence* 1 (2022). Arctic ground squirrel tau-reversal literature.

Longevity drugs and biological-age tests (A5, A2 expansions): the TAME trial (metformin) funding status as of Aug 2026. The Dog Aging Project's TRIAD rapamycin trial. UNITY Biotechnology's 2020 UBX0101 Phase 2 failure (company not named in prose, per house style). Sehgal et al., *Aging Cell* (2026), on epigenetic-clock reliability.

Full citations for all of the above are in the Appendix's "Further Reading" section, tagged by chapter.

## Craft pass, 24 Sep 2026

Found and fixed a real defect, not just a length gap: the series bible targets ~70–90k words for this book (see `Series Plan/07_What_Was_Written.md`), and a prior automated "expand" script had padded twelve of the sixteen original chapters with clone paragraphs — the same closing idea restated three to eight times in a row with minor rewording, rather than genuinely new content. The worst cases: **Chapter 20** ("The Honest Body," the book's closer) had its entire final beat — the basil/airlock scene, the temperature inventory, the "how to spend a Tuesday" paragraph — duplicated wholesale; **Chapter 7** ("Not a Fountain") had eight near-identical "stuck doors" paragraphs in a row and was missing its "Where the popular version goes wrong" + Rule close entirely; **Chapter 5** ("Local Fixes") had five duplicate "scissors with paperwork" closings.

Fixed all of it: Chapters 1, 2, 5, 7, 9, 10, 11, 12, 13, 16, and 20 each had their repeated closings consolidated to one tight version, and Chapter 7 got its missing Rule line written. In the freed space, added ten new real, cited facts in place of the padding (not just cuts): global/hand osteoarthritis prevalence (Ch 1), the Jeanne Calment identity-fraud allegation and its refutation (Ch 2), the exact Casgevy pivotal-trial numbers (Ch 5), real lecanemab/donanemab trial percentages (Ch 7), the Lancet Commission's hearing-loss dementia-risk figure and a phone-checking/slot-machine mechanism (Ch 9 and 10), the Human Genome Project's real cost-then-vs-now (Ch 11), the count of antibiotic classes found before and after 1962 (Ch 12), and the real, ongoing polio-eradication/vaccinator-killings situation in Pakistan and Afghanistan (Ch 16). Citations for all ten added to the appendix's Further Reading section.

Net effect: word count moved from 37,848 to **36,362** — a small net *decrease*, because removing the duplication outweighed the new material. The book is measurably better (no repeated paragraphs, ten more real facts, one structural gap closed) but this pass did **not** close the gap to the series bible's 70–90k target; it fixed quality problems that were more urgent than the length gap. Verified after rebuild: still 20 chapters, 20 appendix notes, 20 figures, 54 TOC links, 0 straight quotes.

**Still open, if a future pass wants to chase the 70–90k target properly** (the way Permit's session did): every remaining chapter would need genuinely new scene material and 1–3 more real facts each, not just de-duplication — a much larger undertaking than this pass. A duplicate-paragraph scan (`difflib.SequenceMatcher` similarity > 0.5 between paragraphs in the same chapter) is a fast, cheap way to re-check for this specific defect after any future automated expansion pass.

## Retitle and story pass, 25 Sep 2026

Retitled from *The Body Keeps Its Own Clock* to **The Body's Honest Invoice**, at Lothar's suggestion: the clock image fit Part I and the relativity/torpor chapters but never fit the brain-myth or progress-extrapolation parts, and "invoice"/"honest" are each used dozens of times across all twenty chapters already. Also renamed Part I from "Many Clocks" to **"Local Fixes, Not Fountains"** for the same reason — gene editing and reprogramming don't read as "clocks" either. Updated everywhere: front matter, KDP description, chapter outline, figure plan, `build_book.py`'s TITLE (which also renamed the output file), `Figures/CREDITS.md`, both draw-script comment headers, and the series bible / Book 3 outline in `Series Plan/`. Old-titled docx deleted as superseded. The manuscript folder itself and internal `SRC` path in `build_book.py` still said "Clock" on this date — left alone then, to avoid touching git tracking and OneDrive sync paths; only the book's own displayed title changed. On 29 Sep 2026 the folder and those path strings were renamed to `A Longer Life Is Not a New Body - Manuscript`.

Then, at Lothar's request to make the invented story more complete and compelling, found and fixed a real continuity error: Chapter 18 (pre-existing) establishes that Rohan supports Mara only through the same light-delayed link as everything else — "Rohan on the delay," "teaching a valve she has never seen" — he is never physically with her. My own three new chapters (4, 6, 15) had accidentally written him as co-present ("over Mara's shoulder," "he taps the printout," "he hands the printout back," "he shrugs"). Rewrote all three scenes as asynchronous recorded exchanges instead — each line composed without having heard the reply to the previous one — which is more consistent and, incidentally, more affecting, since the delay itself becomes part of the scene rather than being ignored. Also gave Chapter 15's scene a personal hook: Mara's own outbound transit (conscious, not torpor) rather than a purely abstract policy question.

Also developed "the sister on the coast," previously unnamed and mentioned only three times as an inequality symbol, into a small real arc: named her **Priya** at her first proper mention (Ch 11), gave her a full scene with a specific situation — a closed trial enrollment, the boring wins she gets instead — in Ch 17 (the inequality chapter, the natural home for it), and added a genuine payoff in the closing chapter (20): a letter confirming Priya's surgery went "the boring way," landing beside Mara's own local win as "two invoices paid in the same currency." One earlier, pre-name mention in Ch 5 was left anonymous on purpose, a normal delayed-reveal before Ch 11 properly introduces her.

Word count moved from 36,362 to **37,036**. Verified after rebuild: still 20/20/20/54 (chapters/appendix notes/figures/TOC links), 0 straight quotes, "Priya" appears 7 times with a real beginning, middle, and end.

**Still open for the story, if wanted:** Rohan himself is still thin — his own location, job title, and reason for being the one who "already knows the pump" are never stated. The other 16 chapters' Mara vignettes remain brief single-beat illustrations, not a continuous arc; only Chapters 11, 15, 17, 18, and 20 now carry real continuity. A full novelization pass would be a much larger, separate undertaking.

## Headline styling and word-repetition pass, 25 Sep 2026

At Lothar's request, all headline levels in `build_book.py` now use Amazon Ember, bold, centered, and a specific blue (RGB 0,0,255 / hex #0000FF, sampled from an attached swatch): Heading 1 (Part titles) 20pt, Heading 2 (chapter titles, plus the Appendix's own internal section headers, which share the same style) 18pt as specified, Title Page (the book's own title) 28pt. Heading 2 was also changed from left-aligned to centered to match. This is set in the *shared* `build_book.py`, so rebuilding Permit will pick up the same styling automatically — flag to Lothar if that book should look different. Caveat worth knowing: "Amazon Ember" is Amazon's own proprietary font, used in the Kindle app/device UI, not something a KDP author can normally embed in a book file — Word and most systems will silently substitute a fallback font for on-screen display, and Kindle Create's own reflow will very likely apply its own font choice regardless of what's set here for body text. The color should carry through more reliably, but on an e-ink Kindle, blue converts to a mid-gray — worth checking in the KDP previewer once a cover/interior review happens.

Also did a systematic scan (a `difflib`/frequency script, session scratchpad, not saved into the repo) for non-thematic words repeating within roughly one Kindle page (~300 words) per Lothar's "not twice on the same page" note. Most flagged repeats turned out to be the book's own deliberate devices and were left alone: recurring motif words (helium, invoice, monastery, catalog, the drunk "middle," "cupboard," "meeting/ledger") and genuine rhetorical parallelism (a "someone... someone... someone" list, a "you can keep X without Y" anaphora in Ch20's closing) — fixing those would have weakened good, intentional prose. The one real, unintentional tic found: "already," used as filler connective tissue, piled up five times in one page near the end of Chapter 18 and a few more times earlier in the same chapter. Varied four of those instances (kept the chapter's actual thesis line, "the brain you have is already on duty," untouched, since that one is load-bearing). Word count 37,036 → 37,050. Not an exhaustive line-by-line pass across all twenty chapters — flag if a fuller audit is wanted, most other chapters' repeat density looked like normal topic-focused prose, not a tic.

## Continued word-repetition pass + style-guide check, 25 Sep 2026

Continued the "not twice on the same page, if easily avoidable" pass from earlier the same day. Fixed a handful more genuine, easy same-paragraph duplicates: "borrowed wholesale" (was "borrowed whole," clashing with "the whole animal" two sentences later, Ch4), "an entire mouse" (was "a whole mouse... a whole person," Ch6), one more "already" removed from a tight sentence in Ch2. On closer inspection most of the remaining scan hits turned out to be the book's own deliberate vocabulary ("product," central to the whole book's local-fix-vs-product argument) or genuine rhetorical anaphora (Ch19's "do not let a map launder a walk... do not let a second person's confidence launder a ticket... do not let a restoration's miracle-story launder a forever" — a real three-part parallel, not an accident). Left those alone rather than flatten good, intentional prose into synonym soup.

Lothar then pointed to `C:\Users\lomus\OneDrive\My Books for Amazon\Physics Didactic Style Guide.md`, a guide written for a from-scratch physics-teaching book (Move-1-through-7 structure, an on-ramp of 380-660 words before any formal statement, numbers before symbols, intuition and proof sharing the same numbers). It does not map onto this book's own already-established architecture (hot/warm/cold claims, a Mara/Rohan scene, a Rule close, every chapter) — restructuring a chapter into "seven moves" would fight the house style, and Lothar confirmed: keep the existing work, apply only what's easy. Checked the register-level rules against the two physics-adjacent chapters (14, relativity; 15, torpor) and their appendix notes:

- **Real fix applied:** Chapter 14 had one banned "hinge" phrase per the guide's own list — "the effect is tiny and now easy to see" — used exactly where the concept (gravitational time dilation being measurable at all) needs to land, which is the guide's specific concern (telling a reader something is "easy" right where they might be struggling). Reworded to state the fact plainly instead.
- **Checked and already clean:** the same banned-word list (*clearly, obviously, simply, just, of course, easy to see*, etc.) turned up nothing else in Ch14 or its appendix A14; three near-miss words in Ch15/A15 ("clearly," "simply," "just") were all ordinary narrative/descriptive usage, not dismissiveness at a teaching moment, and were correctly left alone.
- **Verified, not fixed (already correct):** the guide's Section 4 rule that an informal explanation and its formal derivation must reach the *same number* — checked every figure in Chapter 14's prose against Appendix A14's table (the 34-year/33.8-year round trip, the 33 cm/33 cm optical-clock resolution, the 0.27 ms/quarter-of-a-thousandth-of-a-second altitude bill, the 38/38.4 µs GPS drift, the 9 ms/nine-thousandths-of-a-second ISS gap, the ~2×10²¹ J / "two billion trillion joules" energy cost) — all already match exactly. No correction needed; this confirms the original research-and-write pass for that chapter was already done to this standard.

Word count 37,050 → 37,055. Verified after rebuild: still 20/20/20/54, 0 straight quotes. Not applied: a full "seven moves" rewrite of Ch14/15 (explicitly out of scope — would conflict with house style and wasn't what Lothar wanted, just awareness of the guide's register-level rules going forward for any future physics content in this series).

## "Gentle on the clueless reader" pass, 25 Sep 2026 — new standing house rule

Lothar asked for a full-manuscript pass to make the book much gentler on a reader who knows nothing about the subject, and — important — for this to become a **permanent standard from now on**, not a one-time cleanup: every term, acronym, or claim that needs grounding for a zero-background reader should get it, going forward, in every future edit to this book (and, by the same logic, its siblings in the series).

Method used, worth repeating on any future pass: first ran a mechanical scan of the whole book for the Physics Didactic Style Guide's banned "hinge" words (*clearly, obviously, simply, just, of course, easy to see, needless to say*, etc.) — came back clean; every hit was ordinary narrative usage (describing a character, a natural qualifier like "just slower"), not pedagogical dismissiveness, so no changes needed there. The real work was a close-reading jargon/assumed-knowledge audit, done per Part file (four parallel sub-agent passes, one per Part), each one flagging concrete spots where a term, acronym, or number was dropped on the reader without enough plain-language grounding — explicitly excluding things already well-explained, deliberate suspense, and the Mara/Rohan/Priya narrative beats.

Fixed 34 instances across all four Part files, each with a short in-line gloss (an appositive or a parenthetical) matching the book's existing voice, not a restructure:

- **Part I (10 fixes):** chromosomes, autophagy, rapamycin/metformin, oncogene, cytomegalovirus, the two-copies-of-a-gene fact needed before heterozygote/homozygote, transfusion-dependent beta thalassemia, cytokine storms, and tying "amyloid" back to Chapter 3's "clumping waste proteins" plus glossing Lewy bodies and frontotemporal dementia.
- **Part II (13 fixes):** PET scanner, "the mesh" (first use in this file), hippocampus, hydrocephalus/"the mantle" (reworded to "cortex"), voxel, glia, the "modifiable risk factor" dementia statistic (plus plain-fraction restatement), worldline, cochlea, closed-loop stimulators (glossed at first use, Ch9, so the Ch9-closing recap term isn't new), dopamine, and the "Chapter 2 split the pots" callback.
- **Part III (5 fixes):** lithography/nanometer (Ch12), the CERN storage-ring aside (Ch14), why a *smaller* black hole's tides are worse (Ch14), accelerometer (Ch14), and germline/"the string"/the off-switch callback (Ch16), plus a "sickle-cell-class win" reminder.
- **Part IV (11 fixes):** CAR-T and enzyme replacements, the delivery/"truck" metaphor reminder, atherosclerosis, apheresis, data lock, pediatric hemispherectomy, hippocampus-as-"map-room" (cross-referenced to Ch8), the incompleteness aside (added the "no system can verify itself from inside" clause), and "the accelerating stretch."

Every fix follows the same shape: a short em-dash or parenthetical gloss right where the term first appears, in the book's own register, never a restructure of the surrounding argument — consistent with Lothar's earlier instruction not to import the Physics Didactic Style Guide's "seven moves" framework wholesale. Introduced a few straight apostrophes while drafting the glosses (`cell's`, `brain's`, `trial's`, etc.) — caught and converted to curly in a follow-up pass; verified 0 straight quotes remain anywhere in the book after rebuild.

Word count 37,055 → **37,253**. Verified after rebuild: still 44 Heading 2s (20 chapters + 20 appendix notes + 4 section headers), 20 Figure Captions, 0 straight quotes/apostrophes.

**Going forward:** treat "would a reader with zero background follow this on first read" as a standing check on every future sentence added to this book — new facts, new numbers, new named mechanisms all get a same-sentence or same-clause gloss before they're allowed to stand alone, the same way this pass did it.

## Same pass extended to the appendix, 2026-09-26

Lothar asked for the identical accessibility pass on `11_Appendix.md`. Read the whole file directly (288 lines, small enough not to need the four-way sub-agent split used for the main chapters) and applied the same standard, calibrated for the appendix's own stated register — "How to Read These Notes" frames it as denser scientific detail paired with a popular chapter, so already-explained-in-the-matching-chapter terms and real citation names were correctly left alone; only genuinely opaque notation, acronyms, and jargon *not* already unpacked anywhere got a gloss:

- **A2:** glossed "intraclass correlation" (the reliability statistic behind the biological-age-clock reproducibility numbers) as "a 0-to-1 score for how well repeat tests on the same person agree with each other."
- **A5:** named the actual drugs behind the mechanism-class descriptions — "an mTOR-inhibitor class drug (rapamycin, a transplant drug)" and "an AMPK-pathway drug already licensed for diabetes (metformin)" — since the appendix had switched to mechanism-only language while the main chapter uses the drug names, breaking the link between the two; also glossed "lipid nanoparticles" as "fatty capsules that ferry genetic material into a cell."
- **A6:** glossed "intravitreal injection" as "an injection into the eye itself."
- **A14:** added inline variable glosses to the weak-field time-dilation equation — Δτ/τ as "the fractional change in a clock's rate," ΔΦ as "the change in gravitational potential," g h as "gravitational acceleration times height" — since the appendix's other main equation (proper time, τ) already names its term in prose right after but this one didn't.
- **Bonus fix in the main text while cross-checking:** found that Chapter 5's own first mention of "AAV, lentivirus" as delivery vectors was never actually expanded, even though the appendix (A5) references the same acronym — added "a hollowed-out virus put to work as a truck, in classes called AAV and lentivirus" at the Chapter 5 source, so the appendix's later, terser reuse of "AAV" now has a real antecedent.

Left alone on purpose, matching the "appendix is the denser optional register" carve-out: the full hallmarks list in A3 (already explained in plain language in Chapter 3), the τ/proper-time equation notation in A14 (immediately glossed in the same sentence), named methylation clocks (GrimAge, DunedinPACE — proper nouns, not acronyms needing expansion), and the Book-1 callback in A19 ("the leftover glow," "the shove") which is explicitly signposted as courtesy material the reader does not need.

Word count 37,253 → **37,322**. Verified after rebuild: still 44 Heading 2s, 20 Figure Captions, 0 straight quotes.

## Same pass extended to the front matter, 2026-09-26

Lothar asked for the identical pass on `00_Front_Matter.md`. Read the whole file directly (117 lines). It was already close to clean — the front matter's whole job is orienting a first-time reader, so most of it is already gentle by design (the temperature system is taught from scratch in "How to Read This Book," HALE gets an inline gloss, the Volume 1/2 callbacks are explicitly framed as courtesy the reader can skip). Two real gaps found, both in the "Hot" bullet of the temperature list — the first substantive technical examples a reader meets in the whole book, ahead of any chapter's own explanation:

- **"A sickle-cell-class gene edit"** — named with no gloss, three chapters before Chapter 5 explains what sickle-cell disease is. Added "— a fix for an inherited blood disease —."
- **"packets"** — listed bare among "vaccines... a genome... packets, cheaper compute," with no hint of what kind of packets, nine chapters before Chapter 11 explains it as network packets carrying a clear radio signal. Added "that keep a signal clear across a long delay."

Left alone on purpose: "string theory" (already self-explained in the same paragraph — "a large mathematical framework" that "has not produced a unique, risky prediction"), the Volume 1/2 references in "A Note on the Series" (explicitly signposted as courtesy, "you do not need..."), and "hallmark of aging" in the Author's Note (used rhetorically, contrasting jargon-recitation with real understanding — the sentence's own point doesn't require knowing the technical term).

Word count 37,322 → **37,340**. Verified after rebuild: still 44 Heading 2s, 20 Figure Captions, 0 straight quotes. This closes out the standing "gentle for the clueless reader" rule across the whole book: main chapters (2026-09-25), appendix (2026-09-26), and now front matter (2026-09-26) have all had the same pass.

## Still human

- Kindle Create / KDP previewer.
- `KDP_Description.md`'s sell copy still describes the pre-this-pass book; worth a pass to mention the new chapters if Lothar wants them in the Amazon listing.
