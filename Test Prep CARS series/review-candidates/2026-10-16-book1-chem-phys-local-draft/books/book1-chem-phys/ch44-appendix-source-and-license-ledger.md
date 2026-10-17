# Appendix: Source and License Ledger

**What this appendix is for**

This ledger records where everything in this book came from and why you may rely on it. For Book 1, the Chemical and Physical Foundations volume, the record is short because almost everything is original. The few outside items are facts about the exam, taken from the exam owner's public pages, and each one is listed below so that a reader (or a reviewer) can see exactly what was relied on.

Praxis Tip: A short ledger is still a ledger. Update it whenever you add a figure, a fact or a quotation, not at the end of the project.

**Independence statement**

This book is independent. It is not affiliated with, endorsed by, or sponsored by the owner of the exam it prepares readers for. The exam's name is used only to say what the book is about. No logos, trademarks or "official" claims are used.

**What was and was not reproduced**

No released exam, no official practice question, and no commercial prep book was reproduced, retyped, summarized in detail or closely paraphrased in this book. Every passage, question, answer choice, explanation and worked example was written by the author for this book. The glossary definitions and the Praxis Tips are also the author's own words.

**Original content, by chapter group**

| Chapter group | Content | Status |
|---|---|---|
| Strategy chapters (1 to 6, 38, 41) | Text, worked examples, checkpoint questions, explanations | Original |
| Lessons 1 to 25 (physics, general chemistry, organic chemistry, biochemistry) | Text, worked examples, checkpoint questions, answer explanations | Original |
| Practice sets (mechanics, physics mixed, chemistry 1 and 2, organic, biochemistry) | Passages, questions, answer choices, explanations | Original |
| Full-length exams 1 and 2, Parts A and B | Passages, questions, answer choices, explanations | Original |
| Appendices (this ledger, the formula sheet and the glossary) | Text and definitions | Original |

Standard scientific facts, constants, equations and conventions (for example, the ideal gas law or the Nernst equation) appear throughout. They are facts and ideas, not protected expression, and are explained in the author's own words.

**Exam-owner facts used**

Each item below is a fact about the exam, described in the book's own words. Each is marked: taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled]. Where this book and the official pages differ, the official pages win.

| Fact used | Where used | Source status |
|---|---|---|
| Section name, position as first of four sections | Chapter 1 | Taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled] |
| Number of questions (59) and time (95 minutes) | Chapters 1, 4, 38 | Taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled] |
| Structure: passage sets plus independent questions | Chapters 1, 4, 38 | Taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled] |
| Section and total score ranges; no penalty for wrong answers | Chapters 1, 38 | Taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled] |
| Field-test (unscored) items; on-screen periodic table; calculator rule | Chapters 1, 5, 38 | Taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled] |
| Content categories 4A to 4E and 5A to 5E, and their foundational concepts | Chapter 1 and lesson openers | Taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled] |
| Four scientific reasoning and problem-solving skills, with approximate shares | Chapters 1, 4, 6, 41 | Taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled] |
| Approximate discipline weights (general chemistry, biochemistry, physics, organic chemistry, biology) | Chapters 1, 3 | Taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled] |
| Mathematics the section expects | Chapter 5 | Taken from the exam owner's public outline/FAQ, facts only, check date: [to be filled] |

Praxis Tip: Fill the check date for every row on the same day you reopen the official pages, and keep a dated copy of each page you relied on.

**Figures**

The book contains 19 original figures, kept in the books/book1-chem-phys/figures/ folder. Each was created by the author with matplotlib (Python), from the author's own data and drawings. None is traced, scanned or adapted from another source.

| Figure file | Subject | Status |
|---|---|---|
| circuit-series-parallel.png | Series and parallel resistor circuit | Original, matplotlib |
| decay-curve.png | Radioactive decay curve | Original, matplotlib |
| dna-base-pairs.png | DNA base pairing | Original, matplotlib |
| energy-bars-track.png | Energy bars along a track | Original, matplotlib |
| enzyme-kinetics-plots.png | Michaelis-Menten and Lineweaver-Burk plots | Original, matplotlib |
| galvanic-cell.png | Galvanic cell diagram | Original, matplotlib |
| glucose-anomers.png | Glucose anomers | Original, matplotlib |
| heating-curve.png | Heating curve with phase changes | Original, matplotlib |
| hydrogen-levels.png | Hydrogen energy levels | Original, matplotlib |
| incline-forces.png | Forces on an incline | Original, matplotlib |
| lens-ray-diagram.png | Lens ray diagram | Original, matplotlib |
| molecular-shapes.png | Molecular shapes (VSEPR) | Original, matplotlib |
| narrowed-tube.png | Flow through a narrowed tube | Original, matplotlib |
| periodic-trends.png | Periodic trends | Original, matplotlib |
| projectile.png | Projectile motion | Original, matplotlib |
| reaction-energy-catalyst.png | Reaction-energy diagram with a catalyst | Original, matplotlib |
| standing-waves-pipes.png | Standing waves in pipes | Original, matplotlib |
| titration-curve.png | Titration curve | Original, matplotlib |
| velocity-time-areas.png | Velocity-time graph with areas | Original, matplotlib |

The scripts that draw the figures are kept with the build tools (tools/ebook/figlib.py and the figures_book1 scripts).

**Kindle build tools**

The ebook is built from the Markdown chapters with a script, tools/ebook/build_ebook.py, which uses pandoc to produce an EPUB for Kindle, the Pillow imaging library, and a Chromium browser binary to render tables as images. The cover is made with tools/ebook/make_covers.py, and the EPUB is checked with tools/ebook/check_epub.py. The fonts and style sheet used are the ones kept in the project. Record the version of each tool, and the license of any font, in the rows below before publishing.

**Rows to fill before publishing**

Use the first table for what the item is, and the second for the rights and the check. Keep the two tables in the same row order.

| Row | Item | Where used | Source and creator |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

| Row | License (with version) | Attribution text | Date checked and by whom |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

If a row cannot be filled completely, the item is not ready to publish. Likely rows: the cover image, the fonts and the style sheet, and the tool versions.

Praxis Tip: Record the license version (for example "CC BY 4.0"), not just the family.

**Before you publish**

- [ ] No released exam, official practice item or commercial prep-book text appears, including paraphrase
- [ ] Every exam-owner fact has a check date filled in
- [ ] Every figure in the folder is listed above and is original
- [ ] The independence statement is on the title page
- [ ] The cover, fonts and tools have complete ledger rows
- [ ] All facts flagged for checking are resolved by a qualified reviewer
- [ ] Every answer key has been independently solved
- [ ] A web search of distinctive phrases found no accidental matches
- [ ] Author verification notes are removed in the release build

Praxis Tip: Run the release build and read the report of leftover flags before you upload anything.

---

**Author verification note (remove before publishing)**

- The exam-owner check dates are intentionally blank. They must be filled by someone who has the official pages open.
- The figure list was made from the folder contents; confirm each figure appears in the chapter you expect.
- Tool versions and font licenses are not yet recorded.
