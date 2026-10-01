# Rewrite brief for *The Universe Keeps the Books*

You are line-editing one or more chunks of a popular-science almanac by Lothar J. Musiol (a semiconductor engineer of four decades who studied physics in depth). The almanac is assembled from markdown by a Python builder into a Kindle/print Word file. Chunks live in `_source\_work\`. Untouched originals of every chunk are in `_source\_work\orig\` (same file names). Edit only the chunk files you were assigned, in place. Do not touch any other file.

The folder path contains an apostrophe (`Lothar's`). If you run Python, do not `cd` into it; run from `C:\Users\lomus` and pass full quoted paths, or write a script to `C:\Users\lomus\AppData\Local\Temp\` and run that.

## What to do, in this order of importance

### A. Teach directly. Stop describing a book.
Much of the text narrates a book instead of teaching the reader: "The chapter argues…", "The epilogue draws the arc together…", "Classical mechanics gets a satisfying reframing here", "The central thesis gets restated", "The appendix organizes the volume into four tiers… Then come ten prompts", "is flagged as", "the discussion turns to", "this volume", "the book closes on", "X is covered here". Rewrite every such sentence as the content itself, addressed to the reader. If the text announces content that is not actually present (for example "ten discussion prompts" that are never listed, or "a status check" that is never run), either supply that content briefly and accurately, or delete the announcement. Never leave a promise the page does not keep.

### B. Cut the tics by about two-thirds.
- Self-announced honesty: "honest", "honestly", "to be honest", "it's worth being honest". Show the care; stop saying it.
- "It's worth noting / it's worth stressing / it's worth repeating / worth spelling out".
- "a bit like", and "Picture a…" as the default entry to every analogy. Keep the good analogies; vary or drop the wind-up.
- Analogy-then-disclaimer: the text often offers a picture and then audits it at length ("the picture is honest about X but quiet about Y", "falls short", "runs out", "oversells"). Keep at most one short caveat per chapter, one sentence, placed where the picture genuinely breaks. Delete the rest of the auditing.
- Em dashes: cut by about two-thirds. Use periods, commas, colons or parentheses instead.

### C. Short paragraphs.
No paragraph over about 200 words. Split at natural joints. One idea per paragraph is a good default.

### D. Keep the fun.
The house voice is dry deadpan. Model: "A heavy black hole evaporates with the urgency of a cathedral." "Nature, regrettably, did not take the taxi." "The law is the part that would have filed its paperwork on time." Let jokes land without explaining them. Do not add jokes to every paragraph; one good one per chapter beats five weak ones.

## Hard rules

1. Every line that starts with `#` must stay byte-identical. Do not add, delete, merge, reorder, rename or renumber headings. (The only additions allowed are the Status lines and openers described in your assignment, which are not headings.)
2. Every cross-reference such as "Chapter 15", "Storey 7", "Lesson 23", "Lecture 8", "Appendix 3" must keep pointing at the same number. You may rephrase around it.
3. Keep every fact, number, date and name. Do not introduce new factual claims except where you replace an announcement with the content it announced, and then only claims you are certain of. Never invent quotes, citations, anecdotes, or biographical details about the author.
4. Do not cut whole chapters or sections. Expected length after editing: about 80–100% of the original. The savings come from tics and narration, not from substance.
5. American English. Avoid the contrastive constructions "X, not Y", "isn't X, it's Y", "not X but Y" wherever a plain positive statement works; say what the thing is.
6. Markdown only: paragraphs separated by one blank line; `**bold**` and `*italic*` allowed; keep existing bullet lists; no tables, no HTML, no new headings, no images.
7. Do not write "Part I", "Part II", … to mean a part of an original source book. In this volume "Part N" auto-links to the almanac's own Parts. Use "this book's first half", "the DC chapters", and so on.
8. Do not use the words "almanac", "condensed", "condensation", "highlights", "this volume" or "the full edition" in the text. Readers should not be told about how the book was assembled.

## Certainty labels (only if your assignment says so)
Immediately after each chapter heading named in your assignment, insert one blank line and then exactly one line of this form, then a blank line:

`*Status: Settled.*`

Allowed labels:
- **Settled**: tested repeatedly, textbook physics or biology.
- **Strange but solid**: thoroughly established and still counterintuitive (time dilation, entanglement, the statistical arrow of time, decoherence).
- **Serious but unconfirmed**: mainstream research programs or leading explanations without decisive confirmation (inflation's details, the nature of dark energy, string theory, many origin-of-life scenarios, most quantum-gravity work, forecasts).
- **Speculative**: fringe, untestable as stated, or far beyond evidence (strand model, multiverse claims, Omega Point, ER = EPR as physics of our universe, mind uploading).

For a mixed chapter, name the core and the exception, for example `*Status: Settled; the closing section is Speculative.*` or `*Status: Serious but unconfirmed; the history is Settled.*` Keep it to one line. Judge by the chapter's main claims.

## Book openers (only if your chunk contains a line starting with `# ` and your assignment says so)
Right after that `# ` heading line, before anything else, insert one blank line and a two-sentence deadpan opener of at most 40 words that tells the reader what this book is for and makes them want to read it. It must not mention how the book was assembled.

## When you finish
For each of your chunk files, run a check that compares the list of lines beginning with `#` in your file against the same list in `_work\orig\<same name>` and confirms they are identical. Count words before and after. Then reply with: file names, words before/after, "headings identical: yes/no", how many Status lines you added, and anything you were unsure about (one line each). Keep the reply short.
