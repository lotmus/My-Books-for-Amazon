# Quantum, Actually, Volume 1: status

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
