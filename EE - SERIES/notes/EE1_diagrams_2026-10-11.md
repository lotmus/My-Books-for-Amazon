# Book 1, Foundations of Electronics: diagrams and voice pass (11 Oct 2026)

Old master: bak/2026-10-11 pre-diagrams/Foundations_Book1.docx (MD5 EC15EC72247A01BC8487B810601B8401).

Rebuild (from scripts/diagrams/b1): `python3 figs_b1.py`, then `python3 build_b1.py <old master> t1.docx`, then
`python3 kindle_links.py t1.docx "kindle_links - Foundations_Book1.json" --out Foundations_Book1.docx`.
The docx is the master. Note: chapters/Book1 sources predate this pass and no longer match the master.

What changed
- Smith chart, impedance matching and bias networks moved out of Part II (math) to the end of Part III as Chapter 37; old Chapters 25-37 renumbered 24-36. Every chapter, section, figure, worked-example and § reference renumbered; TOC, Appendix A (Smith formulas now under Part III), Appendix B solutions, Appendix D summaries, preface and part descriptions updated. Odd heading "38.1a" now 38.2.
- 10 new diagrams (matplotlib/schemdraw, shared style scripts/diagrams/common/eestyle.py, 800 px, numbered captions, alt text): 1.1 conductor vs insulator, 7.2 resistor color code, 8.2 LED + series resistor, 9.1 charge circling in B, 12.1 EM plane wave, 19.2 decibel ladder, 30.2 Thevenin source line, 34.1 RL phase lag, 35.1 instantaneous power, 38.1 diode small-signal tangent. Existing 34.1 and 35.1 became 34.2 and 35.2. Every chapter except the short bridge Chapter 25 has at least one figure; 48 in total.
- Every chapter: a hook opener and a "Where you meet this" line; 36 "From the Bench" notes (shaded, before Practice Problems); a closing "What You'll Actually Use" headed list (Everyday working tools / Mostly for exams and deeper study). Exercises and solutions untouched.
- Reading list (12) and Also-by (29) as keyword links with hidden URLs (Open Library / Amazon search).
- American spelling: "shopping trolley" -> "shopping cart".
- KDP_Book1_Foundations.md: description (about 1,900 characters of HTML), 7 keywords, 2 categories.
