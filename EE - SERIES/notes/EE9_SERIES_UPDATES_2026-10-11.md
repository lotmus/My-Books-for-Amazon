# EE Series updates for Book 9 (proposed, 11 Oct 2026 PT)

Book 9 did not edit these shared files. Apply by hand (or by the agent that owns them).

## 1. notes/ALSO_BY - canonical list.md
Under **Electrical Engineering Series**, after line 57 ("- Firmware and Software for Electronics (Book 8)"), add:

    - Test and Measurement Instruments (Book 9)

## 2. SCORES.md (book table, after the Book 7/Book 8 rows)

    | Test and Measurement Instruments | Electrical Engineering Series, Book 9 | draft | not scored yet (first full build 11 Oct 2026: 38 chapters, 11 parts, ~245 pages, 50 figures, 111 worked examples, 234 problems, 35 listings run, 371 number checks pass) | missing (concept: bench instruments, scope, DMM, SMU, spectrum analyzer, VNA) | missing | poor | est. 3.0 | Strict score read; front/back cover in series trade dress showing instruments; run the ngspice decks of Ch8; re-verify vendor specs and prices at publication; hardware-test the Ch38 mini tracer | after Book 8 |

## 3. Book 8 (Firmware and Software for Electronics)
- Also-by list: add "Test and Measurement Instruments (Book 9)" after Book 8.
- Pointer line where Book 8 talks about instrument control, LabVIEW, or production test, e.g.:
  "Book 9, Test and Measurement Instruments, covers the instruments themselves, SCPI sessions, and LabVIEW/TestStand production test."

## 4. Books 1-7
- Also-by lists: append "Test and Measurement Instruments (Book 9)" after Book 8 in each.
- Book 7 (Packaging, Layout, EMC, and Test): pointer from its EMC pre-scan and production-test chapters to Book 9 Ch33 (EMC pre-compliance) and Ch36 (production test, Cpk, GR&R).

## 5. Cover
The Book 9 cover should show instruments (oscilloscope, DMM, SMU/curve tracer, spectrum analyzer, VNA) in the series trade dress, vendor-neutral, no logos or brand names.

## 6. Files
- EE - SERIES/Test_and_Measurement_Instruments_Book9.docx
- EE - SERIES/kindle_links - Test_and_Measurement_Instruments_Book9.json
- Sources: chapters/Book9/src, scripts/diagrams/b9, scripts/build_b9.py
- Rebuild: python scripts/build_b9.py --chapters 38 (with the Book 5 template and common helpers, as in Book 8)
