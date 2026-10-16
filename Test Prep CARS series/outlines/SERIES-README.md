# Series plan

**Series author (byline for every book):** U. B. Smart

| Order | Outline | Role |
|---|---|---|
| 0 | `Core-Test-Skills-Outline.md` | Shared, exam-agnostic skills. **Drafted** in `books/core-test-skills/` (36 chapters), pending expert review |
| 1 | `MCAT-Book1-Chemical-and-Physical-Foundations-Outline.md` | Chem/Phys section |
| 2 | `MCAT-Book2-Biological-and-Biochemical-Foundations-Outline.md` | Bio/Biochem section |
| 3 | (not yet written) Psychological, Social and Biological Foundations | |
| 4 | (not yet written) Critical Analysis and Reasoning | |
| 5 | (not yet written) Full-length practice exams | |

## Byline notes

- Book Writer currently has no author field, so the byline must be added by hand in the exported EPUB/Word/PDF (title page and file metadata) until the app supports it.
- "U. B. Smart" is used as a series pen name. Check it is not already used by another author or imprint before publishing, and keep a record of who actually wrote and verified each book (see the ledger appendix) for your own files and any rights or tax questions.
- Disclose AI assistance wherever the retailer or publisher requires it.
- Add the independence disclaimer (not affiliated with or endorsed by any exam owner) to every title page and product description.

## Voice guide (whole series)

- **Dry, deadpan British humor, used lightly.** Understatement, mild exasperation, the occasional well-placed aside. Roughly one dry line per section, never in the middle of a derivation, never at the learner's expense.
- **Clarity first.** The joke goes *after* the explanation, never instead of it. Remove any line that makes a step harder to follow.
- **No jokes in answer keys, formulas, or the Fact Sheet.** Humor stops where exactness starts.
- **Spelling:** US spelling throughout (decided). Humor is British in flavor only: understatement and dry asides, not spelling.
- **In Book Writer:** put "dry, deadpan British humor, light touch" in each book's premise so the generator follows it.

## Format: Kindle ebooks (reflowable EPUB)

Every book in the series is published as a Kindle ebook (reflowable EPUB). Consequences already identified:

- **Book Writer's own EPUB export does not render Markdown tables or indented equation blocks** (it supports only paragraphs, bold, italic and links). Because the manuscripts use tables heavily, the plan is to build the Kindle files from the Markdown with pandoc, with a stylesheet and a pre-processing step, rather than through the app's exporter. Book Writer remains useful for drafting and editing.
- **Keep tables narrow.** On phone-sized and e-ink screens, tables with more than four columns are hard to read. Wide tables in the lessons should be converted to lists or split before release. New content should use at most four columns.
- **Equations** are written as indented lines; the build step turns them into centered, non-wrapping lines (or images for anything complex).
- **Internal links** use the `(chapter:N)` convention; the build step maps them to the generated chapter files.
- **Cross-book references** ("Core Test Skills, Chapter N") are plain text and should be rewritten as "see the companion book" or a series link once the books have retail pages.
- **Kindle Direct Publishing requirements to handle at upload:** disclose AI-generated content as the platform requires, provide a title, subtitle and author name exactly as on the cover, keep the independence disclaimer on the copyright page, and make sure the book description does not imply endorsement by the exam owner.
