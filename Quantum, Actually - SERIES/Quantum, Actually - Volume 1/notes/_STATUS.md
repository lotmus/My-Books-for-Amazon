# Quantum, Actually, Volume 1: status

## 11 Oct 2026, full read-through and exercises, REV03: 8.7 -> 9.1 (strict)

Master is now `Quantum, Actually - Volume 1_REV03_2026-10-11.docx`; REV02 is in `bak/2026-10-11 pre-exercises/` (and in git history). Built by `scripts/exercises_2026-10-11/engine.py` from REV02 with `batch1.py` ... `batch5.py` (set QA1_SRC to the REV02 path); `verify.py` checks the package.

Exercises (Vol 2 format: "Try it now n" label in blue bold inside the chapter; at the chapter end Heading 2 Exercises, the Core/Extension/Challenge intro, numbered exercises, Heading 2 Solutions, Heading 2 Answers to Try it now):
- 62 Try it now checks (2 per chapter) and 189 graded exercises (4-7 per chapter, every chapter 1-31), each solution worked through and naming the usual mistake. Every number recomputed. How to read this book now explains the exercises; the end blurb mentions them. The TOC is unchanged (Vol 2 does not list exercise sections).

Full read (no sampling), fixes:
- Physics: GPS clocks (rubidium or cesium, not "every satellite timed against rubidium"); Einstein's dice line attributed to the 1926 Born letter; BIG Bell test no longer claims a stronger later reanalysis; cosmic Bell test: Vienna with MIT, quasars in 2018 at 7.8 and 12.2 billion years; doubled phrase in the 2026 network-nonlocality sentence; a cat is a few times 10^26 atoms; Higgs boson is a ripple in the field, and the field sets the elementary masses; neutrino-in-lead softened; Millennium Prize "only one with a claim on matter" removed; QCD "one of the two gauge theories" corrected; "no other theory tested so precisely" -> few predictions; OTOC name; Collective Electrodynamics not "the book this one grew out of"; flux quantum is a few billionths of a fridge magnet's flux (twice); field-tensor sentence (observers do not get the identical E/B split; E^2 - c^2B^2 is invariant); laser: stimulated emission copies phase; radiation-resistance analogy; g-2 "ten digits" -> one part in a trillion; drift speed a fraction of a mm/s; "a meter of household wire"; QED "more closely than any other theory" softened; circuit QED "one and the same" -> meet in one device; Appendix 1 summary: strong force couples to colour charge, "Black holes are real." removed; Appendix 3 relativity date; Bostrom "then at" Oxford.
- Typography: the Greek mu and nu in the QED Lagrangian, covariant derivative, interaction term, Glossary and Equations Decoded had become u and v (and a stray subscript psi); restored.
- Leftovers from earlier titles: "Parts One through Three", "Parts Eight through Ten", "every remaining Part", "midpoint of this book", "this book's own title", "on the first page", "where this book started", "Chapter Three", "earlier in this chapter" (Appendix 3), Chapter 5 "a chapter" -> four chapters.
- Back to Contents added at the ends of Chapters 3 and 6. Nadella source is a LinkedIn post; Theoretical Minimum no longer "gentlest" next to "advanced".
- kdp_description_QA1.txt: one paragraph on the exercises.

Checks: 0 Word tables, no visible URLs, 935 hyperlinks (933 + 2), package entries and relationships unchanged, 2.11 MB, about 120,500 words (98,600 before; the growth is exercises and solutions). LibreOffice render: 478 pages, exercise pages and the Lagrangian checked by eye.

Scores (strict): physics 9.4, exercises 9.4, clarity 9.0, structure 9.2, prose 8.7, pictures 9.0 (not re-audited), sources 9.2, Kindle 9.2, KDP listing 9.2, covers 8.8; overall 9.1. Sellability 6.5 (long subtitle, niche Part Two; the exercises are now a selling point).
Still open toward 9.5: a prose-tightening pass on Part Two (Chapters 13-31 repeat their own conclusions and run long; this pass trimmed only where a sentence was wrong); an outside physicist's check of the exercise solutions; the Gravitation, Actually entry in Also-by still uses the old subtitle "A Short Book on Gravity", as in every other book (its new subtitle is in Gravitation's KDP_Description.md), so update all Also-by lists together.

## 10 Oct 2026, strict rescore from a careful sampled reread: 8.1 -> 8.7

Sampled: front matter and Prologue, Chapter 6 opening, all of Chapter 13, the Part One question box, Epilogue opening, Notes on Sources, Further Reading, Bibliography, back matter. Not a full read-through.
Prose 8.4 (Part One leans on one-line paragraphs; Part Two is strong but wordy), structure 8.6, facts 9.1, formatting/KDP 9.0, covers 8.5 (new).

Covers (the old ones still said The Quantum World and Science for Everyone; the back carried an endorsement attributed to Carlo Rovelli that nothing in the repo supports, a printed ISBN barcode, and a Collective Electrodynamics feature the merge removed):
- New front and back, 2202 x 3520, by `scripts/make_qa1_covers.py` in Volume 2's trade dress (star field, double gold frame, Cinzel gold title, feature box, badge). Back quote is from the Prologue; no barcode (KDP adds one). Old covers in `bak/2026-10-10 old covers/`.

Text fixes (`scripts/rescore_2026-10-10.py`):
- Prologue: "That is where Quantum World begins" (old title, no full stop) -> "That is where the quantum world begins."; the sentence about "that assumption" now follows the assumption.
- Road map step 7 is a Heading 2 like steps 1-6; wrong opening quote in the "ONE PART IN A TRILLION" box head.
- Chapter 13: the (r) in e^{i theta(r)} is now in the exponent; SQUID sensitivity is "a tiny fraction of one flux quantum" (it was "measured in single flux quanta"); two overlong sentences split.
- Questions This Book Answers: "Chapter N  Why..." -> "Chapter N: Why..."; Q./A. boxes single-spaced; 502 trailing spaces removed.
- Notes on Sources: 8 doubled full stops; Peskin and Schroeder 1995 is Addison-Wesley (as in the Bibliography); note 12 now says the one-part-in-a-billion figure is for ae and one part in a trillion for g/2, so Parts One and Two agree.
- 25 empty hyperlinks unwrapped (no visible change).
- Link rule: 39 more sources linked by title (Open Library for books, DOI, arXiv or the archive PDFs for papers), each checked to resolve; the BB84 paper links to its 2014 reprint, now named in the entry. Rules added to kindle_links.json; rerunning the tool changes nothing.

Exercises: this volume has none to cut; nothing was cut.
Still open: Part One's one-line-paragraph rhythm (author's style, left alone); a full read-through.
