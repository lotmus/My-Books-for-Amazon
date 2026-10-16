# Appendix: Error Log Template and Analysis Sheet

Use this with Chapter 9. Set it up once, then fill one row per wrong answer or lucky guess.

Praxis Tip: The log works only if it is quick to use. Keep the columns short and resist adding more.

**1. Log columns**

| Column | What to write |
|---|---|
| Date | When you answered it |
| Source | Which set or test |
| Q# | Question number |
| Topic | From your content outline |
| Chose / Correct | What you picked and what was right |
| Why I chose it | One honest sentence, written before reading the explanation |
| Cause code | CG, MR, RU, TC or CS |
| Confidence | High, medium or low at the time |
| Fix | One concrete action |
| Redo date | When to try a similar question |
| Redo result | Right, wrong, or pending |

**2. Cause codes**

| Code | Meaning | Typical fix |
|---|---|---|
| CG | Content gap | Short lesson, flashcards, redo in 2 and 7 days |
| MR | Misread | Note the qualifiers and the final line; restate the question |
| RU | Rushed | Practice with checkpoints; flag-and-move |
| TC | Trap choice | Name the misconception; make a card |
| CS | Calculation slip | Estimate first; check units; recompute a different way |

**3. Spreadsheet setup**

If you use a spreadsheet, place the cause codes in a column (say column G). Then, in a summary area:

- Count of each cause: `=COUNTIF(G:G,"CG")`, and the same for MR, RU, TC and CS.
- Total errors: `=COUNTA(G:G)-1` (subtract the header row).
- Share of each cause: the count divided by the total.
- Share of errors that need no new content: `=(MR+RU+TC+CS)/total`, using the cell references for your counts.

Filter by Topic to find the weakest areas, and by Confidence = High to find false beliefs.

Praxis Tip: Add a "Week" column. Weekly counts let you see whether your fixes are working.

**4. Weekly analysis sheet**

| Item | This week | Last week |
|---|---|---|
| Total errors | | |
| CG | | |
| MR | | |
| RU | | |
| TC | | |
| CS | | |
| High-confidence errors | | |
| Biggest cause | | |
| Fix I will focus on | | |
| Redo questions due | | |

**5. Worked Example: Filling one row**

| Field | Entry |
|---|---|
| Date | 2026-03-02 |
| Source | Mixed set 4 |
| Q# | 7 |
| Topic | Percent change |
| Chose / Correct | B / C |
| Why I chose it | I took 25% for both steps; assumed they cancel |
| Cause code | TC |
| Confidence | High |
| Fix | Make a card: "Percent change uses the starting value of that step as base." |
| Redo date | 2026-03-05 |
| Redo result | Pending |

This row shows a trap choice made with high confidence, the most valuable kind to log.

**More Praxis Tips**

Praxis Tip: Log immediately after each set while the reasoning is fresh.

Praxis Tip: Sort by redo date each morning and do the due items first.

Praxis Tip: Archive a row after two correct redos in a row, separated by several days.

Praxis Tip: Once a month, read the whole log from the top. Patterns that hide week to week are visible at a glance.

---

**Author verification note (remove before publishing)**

- Spreadsheet formulas assume a layout with cause codes in column G; adjust to the actual layout and test them.
- The example row is invented.
