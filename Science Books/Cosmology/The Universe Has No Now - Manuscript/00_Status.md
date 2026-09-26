# Book 1 status — *The Universe Has No Now*

**Kitchen date:** 16 September 2026.  
**Author:** Lothar J. Musiol.  
**Title:** The Universe Has No Now.  
**Series:** Volume 1 of *Look First*. Books 2 and 3 were not opened in this pass.

This file is the close-out checklist after the full-length Book 1 pass.

## Standing policy, from 25 Sep 2026 onward

**Every term used in the popular text must already have been built, be built where it's used, or be explicitly pointed forward with a chapter number, before it's used cold.** This applies to every future editing pass on this manuscript, not just the one that established it. The book already does this well most of the time (see the method and results below) — the job is to keep it that way and catch the exceptions, not to add more machinery.

## Manuscript (closed)

- 45-chapter book in ten part files plus front matter and appendix. Headings match `00_Chapter_Outline.md` (Ch 1–45 / A0–A45). No chapters added. No new part.
- Front-matter order: title (Lothar J. Musiol) → minimal copyright (2026, all rights reserved) → How to Read → series note → Author’s Note → TOC marker → Prologue.
- No acknowledgments, credits, or NASA wall in the book body. Photo credits live only in `KDP_Description.md` for the Amazon field.
- Chapter 30 still includes the 30-centimeter intelligence passage (after the saurian-mind paragraph, before “Civilization is the extra invoice”). Appendix A30 has the matching packing / neuron-count note. Ch 30 was not rewritten.
- In-text figures remapped to Fig 0–45 (one per chapter). No “Chapter 52” leftovers. No film titles.
- Sequel rooms stayed closed: no Moon/Mars Gantt, no Earth-recovery-if-we-leave, no longevity/CRISPR fountain, no 10,000-year tech line, no “full brain” 10% myth.

## Word count

**Before this pass:** 44,172 words (`export\WORD_COUNT.txt`).  
**After this pass:** **112,711 words** in the assembled popular text plus appendix (`export\WORD_COUNT.txt`). That is roughly **320–400 Kindle pages**, in the locked 100–127k band. The integer is a stamp, not an estimate.

Every popular chapter except 30 and 34 was lengthened from outline-thin (~300–1,100 words) into a teaching chapter (~1,800–2,200 words of body). Chapter 30 stayed ~7,500. Chapter 34 stayed a long watchmaker/signal chapter (~2,950). Appendix A0–A45 were thickened to twins, still not a textbook.

## Figures (honest tally)

| | Count |
|---|---:|
| Drawn diagrams (PNG line art) | **26** |
| Real photographs, space (NASA/ESA/EHT/SDSS JPEGs) | **14** |
| Real photographs, earthly (Wikimedia Commons / Unsplash JPEGs, fetched 14 Sep 2026) | **6** |
| Framed placeholders (real PNG files, auto-swap) | **0** |
| Missing slots with no file | **0** |
| **Total** | **46** |

Credits for the store page: `KDP_Description.md`. Author/production ledger: `Figures/CREDITS.md`.  
Pixels: `Figures/figs/`.  
Plan: `00_Figure_Plan.md` (45-chapter remap; old 52-grid retired).

## Kindle-ready vs still a drop-in

**On disk for ingest**

- Assembled markdown: `The_Universe_Has_No_Now.md`
- Word (6×9 in., **KDP ingest file**): `export\The_Universe_Has_No_Now.docx` (rebuilt 16 Sep 2026, ~12.9 MB, 46 figures, 20 real photographs, no placeholders)
- Typographic cover JPEG (no NASA, no sky): `export\cover_typographic.jpg` (1600×2560, KDP 1.6:1). Author should open it before treating it as store-live.
- EPUB: `export\The_Universe_Has_No_Now.epub` (Pandoc, rebuilt 16 Sep 2026, 46 images). Secondary; KDP ingest is the `.docx`.
- Amazon paste: `KDP_Description.md` (sell copy, then Credits).

**Still not upload-ready (human steps only)**

- Final author look at `export\cover_typographic.jpg` in the actual KDP cover tool (rendering can differ slightly from the thumbnail sheet used below).
- Kindle Create / KDP previewer pass (TOC, chapter starts, grayscale figures). Word file's TOC keeps its real internal hyperlinks (111 links) — leave as built; remove later if you want a plain-text TOC instead.
- Optional: replace `fig01.jpg` (empty kitchen) with a licensed two-person still; caption already says “Put two people in it…”. Fig 0 caption matches the wall clock.

## What this pass did

- Lengthened every thin popular chapter so each actually teaches (kitchen scenes, real years/numbers, temperatures).
- Thickened Appendix A0–A45 to match the new claims.
- Rebuilt diagrams (26) and the 6×9 Word file.
- Wrote a typographic cover JPEG. Did not open Books 2 or 3. Did not make a git commit.

## Close-out, 14 Sep 2026 evening

- Filled the last six photo slots from Wikimedia Commons / Unsplash (`Figures/fetch_photos.py`), identified each source and licence, wrote credits into `Figures/CREDITS.md` and the Amazon Credits block.
- Rebuilt `export\The_Universe_Has_No_Now.docx` and `.epub` with all 20 photographs embedded (0 placeholders). Word count unchanged at 112,690.
- Remaining human steps: open the cover JPEG, run the KDP previewer pass, paste `KDP_Description.md`.

## Error pass, 15 Sep 2026

- Word file opens cleanly in Word (361 pages, 46 pictures, 111 TOC links). Rebuilt at 12.9 MB.
- Fixed in `Figures/build_docx.py`: headings now render markdown emphasis (A43 showed literal asterisks in the heading and the TOC); nested exponents such as 10^(10^86) now print as 10 with superscript 10⁸⁶; `g_*` / `z_*` print as a subscript star; the names Sgr A* and Sagittarius A* no longer open a stray italic run (that had leaked asterisks into A2, A9, A18 and A26).
- Photo/caption mismatches fixed: Fig 9 Planck sky re-rendered so warm/cool patches read instead of noise; Fig 14 was an interacting pair, now NGC 4414; Fig 17 Bullet Cluster has *hot gas* / *mass* burned in and a caption that matches the single composite; Fig 18 caption names the Crab Nebula; Fig 24 was a Virgo mosaic, now M87 with its jet; Fig 25 was a rover-less landscape, now the Perseverance selfie. Fig 16 keeps the 2MASS chart with an honest caption and NASA/IPAC credit. Credits updated in `Figures/CREDITS.md` and `KDP_Description.md`.
- Automated text scan: no mojibake, no leftover markdown, no doubled words, no unbalanced quotes or brackets, chapters 1–45 all present, no stale figure numbers. Spell pass: unknown words are all domain terms or hyphenations.

## Rebuild, 16 Sep 2026

- Synced Fig 0 / Fig 1 captions in source markdown and figure plan to the pixels on disk (wall clock; empty kitchen with “put two people in it”).
- Added a one-line photo-credit pointer on the copyright page (Amazon Credits block remains the full ledger).
- Rebuilt `The_Universe_Has_No_Now.md`, `export\The_Universe_Has_No_Now.docx` (~12.9 MB), and `.epub`. Stamp: **112,711** words; 46 images; `photo_placeholders=[]`.
- Remaining: human cover look + KDP previewer. Books 2 and 3 deferred.

## Cover preview pass, 16 Sep 2026

- Problem: the original typographic cover (`Figures/make_cover.py`) read fine at full size but the title thinned out and lost contrast against the black ground once scaled to Amazon's actual tile sizes — the 160×256 search-result thumbnail and the 300×480 product-page tile are where a shopper first sees it, not the 1600×2560 master.
- Fix: rewrote `Figures/make_cover.py` — larger, bolder title type (fills more of the frame), the word "NOW" set in a single warm ochre accent color (the only color on the cover) so the promise reads even at the smallest tile, and a faint clock-face ring behind the title as a quiet kitchen-clock motif tying to the book's own image. Kept the plain black ground, no NASA/no sky, per the locked spine.
- Verified: rendered the new `export\cover_typographic.jpg` (1600×2560, 1.6:1 — matches KDP's expected cover ratio) down to 60×96, 120×192, 160×256, and 300×480 and confirmed the title and author name stay legible at every size. Backed up the old script as `Figures/make_cover.py.bak`.
- Left the Word TOC's real hyperlinks untouched, on request — do not strip them; they can be removed later if a plain-text TOC is wanted instead.

## Cover redesign, 23 Sep 2026

- Author flagged the clock-ring version above as not good enough. Rewrote `Figures/make_cover.py` again, this time drawing the book's own central image instead of decoration: a light cone through one event, with two different observers' "now" lines tilted through it — Mara's level, Eli's tilted, in ochre — the exact picture Chapter 1 and the Prologue argue for. Soft radial glow behind the event, near-black ground, no NASA/no sky, per the locked spine.
- Caught and fixed a real bug before shipping it: the first render of this version clipped "THE UNIVERSE" off both edges of the canvas at full title size. Added an auto-fit loop that shrinks the title font until both title lines fit inside a fixed side margin, so the fix holds even if the title text ever changes.
- Verified at Amazon's real sizes (60×96, 120×192, 160×256, 300×480): title and "NOW" stay legible, the light-cone mark still reads as an X at the smallest tile. 1600×2560, 1.6:1, matches KDP's expected ratio.
- Old versions kept for reference: `Figures/make_cover.py.bak` (original), `Figures/make_cover_v2_clockring.py.bak` and `export/cover_typographic_v2_clockring.jpg` (the clock-ring version superseded by this pass).
- Still needs the one step only the author can do: open the file in KDP's own cover preview tool, since its on-screen rendering can differ slightly from a plain resize.

## Polish pass, 25 Sep 2026

No content changes — every check below came back clean, so nothing needed fixing.

- **False alarm, chased down and closed:** the existing `export\_audit_content.py` script, run fresh, appeared to show `�` replacement characters mangling em dashes, apostrophes, and "Galápagos." Verified at the byte level with `repr()`/`ord()` — the files hold correct Unicode (`—` U+2014, `’` U+2019, `á` U+00E1) throughout. The `�` was only the terminal's font failing to render those glyphs when printing script output, not damage to the files. No fix needed; the manuscript was never corrupted, on OneDrive or otherwise.
- **Cross-reference audit (new, real check):** every in-text "Chapter N" and "Appendix A#" mention across all ten parts and the appendix was checked against the actual 45 chapter headings and 46 appendix notes. All resolve correctly — no leftover references to pre-merge chapter numbers (e.g., no stray "Chapter 47" from the old 52-chapter grid). Clean.
- **Film-title heuristic, verified not just counted:** the audit script's "Contact"/"arrival" hits were manually checked. The one capitalized "Contact" is a technical appendix subheading ("Light-Travel Contact and Information Bounds"), and every "arrival" is lowercase, ordinary usage (arrival times, arrival hall). No film-title leaks.
- **Megaparagraph scan (new):** every paragraph across all ten parts checked for length. Longest is 243 words; nothing near the 260-word flag threshold. No walls of text.
- **Figure caption audit (new):** all 46 captions (0–45, including Fig 0 in front matter) read as intentional short-fragment house style, consistent across the book. Nothing overlong or genuinely run-on.

Net result: Book 1 has no open content defects. Everything still on the list is the same human-only steps above (KDP cover preview, Kindle Create pass, optional Fig 1 photo swap).

## Headline styling + repeated-word pass, 25 Sep 2026

- **Headline style, `Figures/build_docx.py`:** Part headings (Heading 1) and chapter headings (Heading 2) now set font "Amazon Ember," bold, centered, in the author's reference blue (`#0000FF`, sampled from the supplied swatch). Part headings stay larger (20 pt, the "big" headline) and chapter headings were raised from 15 pt to 18 pt (the "small" headline, matching the size given) — both now share the same font/weight/color/alignment treatment. Verified in the rebuilt `.docx` via style inspection (font, size, bold, color, alignment all confirmed correct) before calling it done.
- **Found and fixed in passing:** `Figures/build_docx.py` had `SRC` hardcoded to the old `D:\...` path from before the move to OneDrive. Every rebuild since the move was silently free to pull stale content from the old drive instead of this folder. Changed it to derive from the script's own location, so it always builds from wherever the manuscript actually lives.
- **Repeated-word check:** scanned the whole book for ordinary words (not the book's own house vocabulary — "loaf," "temperature," "honest," "actually," etc. are deliberately recurring) repeating within roughly one page. Found three close pairs; two were deliberate rhetorical repetition ("Was there really a bang? There was really a..." and the three-item "actually infinite / actually ergodic / actually the right count" list) and were left alone — removing them would have flattened intentional prose. Two were genuine accidental repeats in unrelated sentences: "honest courier" / "honest rule" 73 words apart (Ch. 4), and "relativity actually permits" / "the hole we actually have" 72 words apart (Ch. 34/35 boundary). Fixed both with minimal, meaning-preserving edits (first to "faithful courier," second by dropping the redundant "actually"). Re-scanned afterward and confirmed clear.
- Rebuilt `The_Universe_Has_No_Now.md`, `export\The_Universe_Has_No_Now.docx` (12.9 MB), and `.epub` via `export\assemble_export.py`. Stamp: **112,681** words; 46 images; 0 placeholders/missing/broken.

**Follow-up, same day — broader "no word twice on the page" pass, checked and closed.** Author clarified the rule should apply generally, not just to filler words. Ran the check at three tightening levels across the whole book (front matter, all ten parts, appendix):
1. Any content word repeating anywhere within ~300 words (one Kindle page): 7,172 hits across 1,847 words — but the top offenders (leftover, stretch, helium, burst, crunch, vacuum, membrane, block, thread…) are the book's own established technical/thematic vocabulary, not avoidable filler.
2. Tightened to words used ≤12 times total in the whole book, repeating within ~80 words (same paragraph or the next): still 1,231 hits — mostly ordinary words (blood, group, lower, doors) whose local repetition is invisible to a reader, not a real flaw.
3. Tightened further to near-immediate repeats (within 6 words of each other): 1,129 hits, manually read through a large sample. Conclusion: this is where the book's own consistent rhetorical device lives — end a sentence with a term, open the next sentence by repeating it as the subject, for a punchy definition ("The block is time-symmetric…", "The interval is the same for every observer.", "A permit, in this book, is not a city."). It runs through every chapter by design; it's the book's teaching method, not a tic.

Conclusion: beyond the two genuine accidental repeats already found and fixed above ("honest courier"/"honest rule"; doubled "actually"), there is nothing left in Book 1 that is both genuinely avoidable and worth changing. A further mechanical sweep would mean dismantling the book's own definitional-echo device. Not doing that. If the author spots a specific instance that reads badly to them, flag it and it can be fixed surgically — but no further blanket pass is warranted.

## Didactic-guide term-introduction check, 25 Sep 2026

Author pointed at `Physics Didactic Style Guide.md` (`C:\Users\lomus\OneDrive\My Books for Amazon\`), written for a more technical, equation-forward physics course (its own Floor/Room structure, mandatory numeric tables before notation). That literal machinery doesn't fit Book 1's spine-locked, appendix-only-equations design and wasn't applied. But its core instruction — "assume more introduction than seems necessary," never use a word the reader would have to look up without it being built here, earlier, or signposted as coming later — is genre-independent, so it was checked directly.

- Ran the guide's "banned dismissive words at a hinge" list (clearly, obviously, simply, just, of course, easy to see, as you know, recall that) against the full manuscript. Zero hits on the worst offenders. The "obviously" cluster (10 hits) is confined to Chapter 34's uncontroversial-vs-contested rhetorical structure, not physics condescension; the "just/simply/merely" hits (34) are ordinary restrictive-adverb or locative usage. Clean.
- Checked ~30 genuinely technical terms (FLRW, Schwarzschild radius, Kerr, Kruskal, Bekenstein, proper time, worldline, closed timelike curve, foliation, ergodic, chronology protection, cosmological constant, habitable zone, etc.) at their first appearance in the main text. Most are handled well — several are textbook "name it, then translate" (foliation: "the technical name for slicing the loaf into 'nows'"; proper time: "the way a hiking trail has a mileage"; Kruskal: named, admitted it "looks like a secret handshake," then translated to "a drain you cannot climb").
- Found three real gaps — a term used with no gloss, well before the chapter that actually explains it — and fixed each with a short in-line clause or forward pointer, the same move the book already uses elsewhere ("Chapter 33 will pay the bill"):
  - **"singularity"**, Ch. 19 ("Why Forever-Mind Does Not Follow") — used bare, 5 chapters before Ch. 24 defines it ("a ripped place in the loaf"). Added: "a place, Chapter 24's problem, where the equations stop describing what happens next."
  - **"geodesic"**, Ch. 15 ("Bubbles That May Never Stop") — used bare, 9 chapters before Ch. 24's proper gloss. Added: "the straightest path the geometry allows, the trail a free stone or a free clock actually follows."
  - **"decoherence"**, Ch. 6 ("The Block") — used bare in an aside about the evolving-block interpretation, 34 chapters before Ch. 40's real treatment. Added a one-clause plain gloss plus an explicit forward pointer to Ch. 40.

## Full systematic term-gap pass, all 45 chapters, 25 Sep 2026

Author: "make sure it really goes very gentle on the clueless reader... apply it to all chapters." The spot-check above was a sample; this pass was exhaustive. Method:

1. Built a term → "home chapter" map from all ~40 named concepts in the appendix table of contents (`00_Chapter_Outline.md`) — e.g. Schwarzschild radius → Ch. 20, decoherence → Ch. 40, singularity → Ch. 24 — on the theory that the appendix note number marks where the popular text is supposed to properly teach the term.
2. Split all ten part files into their 45 chapter segments programmatically (verified: all 45 present, correctly numbered) and, for every term, found the true earliest chapter it appears in anywhere in the main text, not just a sample.
3. Flagged every term whose earliest appearance falls *before* its home chapter — 24 candidates — and read each one in wide context (not just a keyword hit) to judge it on the merits, the same way the spot-check above did.

**This caught a real bug in the earlier spot-check**: "singularity" was reported there as first appearing in Ch. 19. It actually first appears bare, with no gloss at all, in Ch. 16 — three chapters earlier — inside the BKL/mixmaster passage. The earlier check's script had a loop bug that let one matched term suppress checking the others in the same file. Fixed and re-verified.

Of the 24 candidates, most turned out to already be handled well on close reading — the book already does the guide's job constantly, just not in the exact spot my keyword search first landed on:
- **Deliberate forward references**, already doing exactly what they should ("dark energy, when we get there, is a statement about..."; "the Bekenstein count of Chapter 23 will later make the bit-budget ruder still: shelf space likes area, not volume"; "the anthropic filter of Chapter 41 gets its only real job").
- **Glossed inline already**, just not caught by a narrow context window: Einstein–Rosen ("a pinch in the loaf," same clause), the Omega Point ("a hoped-for final crunch in which life computes forever," same clause), cosmological constant ("to keep the universe static," same sentence), energy conditions ("a rule that energy is not too exotic," next sentence), recollapse (glossed by contrast: "curling closed... nor hinging open"), landscape (glossed two sentences later: "a menu of valleys... is a landscape").
- **A model passage, not a gap**: the horizon problem in Ch. 9 fully explains the underlying observation (two patches, same temperature, never in causal contact) *before* naming it — textbook "explain, then name."
- **"white hole"** in Ch. 7 gets a full plain-language explanation on first mention ("that film run backward: a local fountain no one has seen") even though its home chapter (22) is later — the early mention is the intentional light-touch intro, Ch. 22 is the deliberate deep-dive. Good design, not a defect; it showed the home-chapter method needs a human reading the result, not just the chapter-distance number.
- **One false match from word-sense collision**: "bounce" flagged photons bouncing off free electrons (Ch. 9) as if it were the same concept as a cosmological bounce scenario (home Ch. 43) — same English word, unrelated meaning. Not a real gap.
- **"causal"** and **"wormhole"** are ordinary-enough English / common-enough pop-culture vocabulary that they don't need the same treatment as genuine jargon.

Four were genuine, fixed:
- **"singularity"**, true first use Ch. 16 (not Ch. 19 as first reported) — was bare with zero gloss. Added a full in-line gloss plus forward pointer at Ch. 16, then **lightened** the existing Ch. 19 fix from a full re-explanation into a short callback ("the same wall Chapter 16 named and Chapter 24 properly explains"), so the reader isn't told the same thing twice within a few chapters.
- **"redshift"**, Ch. 5 — used bare in the Pound–Rebka description. Added a ball-thrown-uphill analogy for why climbing out of a well costs a photon energy.
- **"vacuum energy"**, Ch. 15 — used bare. Added: "a hum of energy that empty space carries even with nothing in it."
- **"the block"**, Ch. 3 — used 3 chapters before its home chapter, with no tie back to the already-established "loaf" metaphor. Added: "which is just the loaf's technical name."

Rebuilt `The_Universe_Has_No_Now.md`, `export\The_Universe_Has_No_Now.docx`, and `.epub`. Stamp: **112,801** words; 46 images; 0 placeholders/missing/broken.

## Hostile-referee review + follow-up verification, 26 Sep 2026

Ran a hostile-but-fair adversarial review (false/overstrong claims, missing steps, internal contradictions, padding/AI cadence, promised-depth-delivered-sketch, term sloppiness). Clean results: zero generic AI-cadence phrases (25-pattern scan — "delve," "tapestry," "it's worth noting," etc.); "prove/proof" (44 uses) is unusually disciplined, mostly the book policing its own overclaiming rather than overclaiming itself; force/energy/power show no cross-contamination; core numbers (CMB 2.725 K, age 13.8 Gyr, Y_p ≈ 0.25, H₀ 67–73) are accurate and consistent between rounded popular figures and precise appendix ones.

Four items were flagged for follow-up verification. All four were then checked properly rather than left as assumptions, and none needed a fix:

- **Ch. 30 length** (7,436 words, ~3.7× the chapter average) — read the full chapter. It covers roughly 20 genuinely distinct sub-arguments (metabolism as slope, cannibalism ethics, sex vs. asexuality, reward systems, biosignature detection, DNA universality, alternative minds, alternative body plans, five separate solvent-chemistry cases, population structure, planetary-protection ethics) without restating the same point twice. Its two "Look first. Seed later." lines are the book's own established series-wide refrain, not padding. Splitting it would also violate the project's locked "no chapters added" constraint. Verdict: earned length, not padding. No change.
- **Appendix depth-delivery** — sampled the four forward-references with the longest deferral gaps (Bekenstein/A23 from Ch. 19, dark matter/A17, wormholes/A33 from Ch. 3, anthropic/A41 from Ch. 15) and read the actual appendix payoff against the promise made. All four deliver real formulas, real numbers, and named real results (Morris–Thorne 1988, Alcubierre 1994, Weinberg's 1987 bound, Clowe et al. 2006, current WIMP exclusion limits) — not thin restatements. No change.
- **Title vs. body match, all 45 chapters** — the earlier review only sampled a third. Extracted every chapter's opening and closing ~70 words and checked all 45 against their titles. Zero mismatches — most chapters echo their own title almost verbatim in the closing line (Ch. 20 closes "A horizon is a fact about events"; Ch. 44 opens by asking its own title; Ch. 37's "Four Kinds of Elsewhere" closes on "the four drawers"). No change.
- **Model vs. reality** — read all 19 uses of "model" in the main text. The book consistently keeps model and reality separate, in places explicitly: "The reheating temperature is model-dependent... What is not model-dependent is the order of operations"; "That is a triumph of a model. That space is not our accelerating, leftover-glow space." No change.

Net: the review's clean findings held up, and every flagged item turned out to be a false alarm once actually checked — not manufactured problems, but not fixes either. No manuscript changes this pass; no rebuild needed.

## Format + content pass before Kindle upload, 26 Sep 2026

Author: docx only from here on — no EPUB, no PDF. `export\assemble_export.py` changed accordingly: it now skips the EPUB build by default (pass `--with-epub` to still build one). The old `export\The_Universe_Has_No_Now.epub` is left on disk untouched, stale from before this pass; not deleted without being asked.

**Format audit — real bug found and fixed.** Inspected the built `.docx` directly (paragraph styles, heading structure, hyperlinks, tables, equation runs, images), not just that it opens:
- Paragraph styles, all 45 chapter and all 46 appendix headings present exactly once, no duplicates or gaps — clean.
- TOC: 111 internal hyperlinks, all 111 resolve to a real bookmark — zero broken links.
- The one markdown table in the source (Equations at a Glance) is the one table in the docx — correct, no silent table-to-text-wall failures.
- Equations: sampled all 17 numbered equations' actual Word runs. Subscripts (H₀, Y_p, ρ_c, T_μν) and superscripts (k^μ) are real Word sub/superscript formatting, not leaked `_`/`^` characters. Clean.
- **Bug**: every one of the 45 popular chapters correctly started a fresh page, but all 51 appendix-side headings (the "Contents" page itself, "How to Read These Notes," all 46 numbered appendix notes A0–A45, "Equations at a Glance," "Further Reading," "Glossary") did not — they would have run together as one continuous, unbroken wall of text on Kindle instead of each starting its own page. Root cause in `Figures/build_docx.py`: the page-break call was gated on `b[2] == "chapter"`, but the parser tags appendix notes `"appendix"` and the other headings `"other"` — those tags were silently never checked. Fixed the condition and added the missing break before "Contents." Rebuilt and re-verified: all 112 headings now correctly get a page break.
- Checked for literal `*` leaking into the final docx text (would mean an unclosed emphasis marker somewhere in 112,801 words). Found 16 instances, all legitimate real notation — Sagittarius A*, M87*, and the standard R*/z*/T* variables from the Drake equation and recombination physics — not leaks. Confirms the earlier Sgr A*/M87* stray-italic fix (15 Sep) is still holding.
- Image color: several figures (M87 jet, Bullet Cluster, Crab Nebula, Andromeda, EHT shadow) are genuinely color photographs that will render in grayscale on Kindle e-ink. Not a defect — that's normal for any illustrated Kindle nonfiction, and the one figure where color does real work (Bullet Cluster's hot-gas-vs-mass overlay) already has its regions labeled directly in the pixels, so the distinction survives grayscale.

**Content audit — spell-check and markup-balance, whole manuscript.** Ran a dictionary spell-check across all 12 files with a domain-term allowlist (character names, physicist names, book vocabulary): 404 words flagged. Read through every one — all are units and acronyms (km, Mpc, CMB, BBN, GPS), real physics jargon (timelike, spacelike, comoving, ergodic), proper names split by accented characters my regex didn't catch (Lemaître → "lema"+"tre"; Schrödinger → "schr"+"dinger"), the book's own deliberate coinages (elsehow, nows, rudenesses), and a handful of names/terms verified directly in context (Kade and Sela, a story vignette's two characters; AARO, the real US government anomaly office; Coleman–De Luccia, a real 1980 physics paper; the Egyptian seked and Sopdet, both correctly used and glossed). **Zero genuine typos found.** Also checked emphasis-marker (`**`/`*`), parenthesis, bracket, and curly-quote balance per file — all 12 balance cleanly (the appendix's raw asterisk count looked odd until checked against the actual docx output, which showed it's the legitimate Sgr A*/M87*/R*/z*/T* notation above, not an error).

Rebuilt `The_Universe_Has_No_Now.md` and `export\The_Universe_Has_No_Now.docx` (docx only, per the new default). Stamp: **112,801** words; 46 images; 0 placeholders/missing/broken.
