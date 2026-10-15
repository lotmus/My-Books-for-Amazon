# The Universe, Actually - REV15 (2026-10-10)

Master: `The_Universe_Actually__REV15.docx` (REV14 moved to `bak\`).

## What changed from REV14
- **Near-duplicate chapters merged** (81 -> 77 chapters, 8 parts unchanged):
  - 29 Quantum Information + 30 Quantum Computation + 70 Quantum Computing -> **29. Quantum Information and Computation** (Part III). The plain-language opening of the old ch. 70 now opens the chapter; the rest of it closes the chapter as "Building One, and What It Is For". Quantum Error Correction and its "Further Aspects" section are one section. Part VII (Technology) keeps AI, Robotics, Biotechnology, Space Exploration, Secrets and Codes.
  - 39 Evolution and Genetics + 40 Evolution -> **38. Evolution and Genetics**: selection first, then the genetics from Mendel to DNA, imprinting and gene transfer, population genetics with its worked examples, speciation, the tree of life, sex, behavior, social insects, and "The Map That Contains Itself" as the close. Merged section pairs: Natural Selection (+ Without a Designer), Mendel and the Chromosomes (+ Mendelian Inheritance), Classification and the Tree of Life (+ The Tree of Life).
  - 51 The Nervous System and the Brain + 52 Neuroscience -> **49. The Brain and Nervous System**; the old ch. 52 opening is the section "What Neuroscience Knows"; Systems Neuroscience absorbs its "Further Aspects" section.
  - Chapters renumbered 1-77, bookmarks `ch_1`..`ch_77`, linked Contents rebuilt (0 dead links). No sentence-level near-duplicates in the merged chapters beyond deliberate parallels.
- **American spelling** in the main text (color, behavior, center, meter, -ize, program, signaling, hemoglobin...); 287 runs. Bibliography and External Resources titles are left as published.
- The three leftover "In this section:" outline lines are gone.
- **Back matter**: the catch-all "Appendix" heading is replaced by real headings, **About the Author** and **Also by Lothar J. Musiol**, both in the Contents; the review invitation sits just before About the Author.
- **Links**: `kindle_links.json` re-applied (REV14 had lost them): 99 external links, no visible URLs.
- Typography: curly apostrophes and quotes, prime marks, true minus signs in the equations.

## Rebuilding
REV15 is REV14 plus three docx-level passes, in this order:
1. `python scripts/rev15_structure.py The_Universe_Actually__REV14.docx tmp.docx`
2. `python tools/kindle_links.py tmp.docx "The Universe, Actually/kindle_links.json" --out tmp2.docx`
3. `python scripts/rev15_typo.py tmp2.docx The_Universe_Actually__REV15.docx`

`scripts/make.py` (pool + `structure.txt` + `ops/`) still produces the REV14 layout; run the three passes after it, or port the merges into `structure.txt` before the next pool rebuild.
