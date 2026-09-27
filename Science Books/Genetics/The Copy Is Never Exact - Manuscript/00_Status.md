# Status — *The Copy Is Never Exact*

**Started:** 15 September 2026. **Author:** Lothar J. Musiol. **Series:** standalone, first title under Science Books / Genetics.

## What this is

A full first draft of a popular-science genetics book, built to the same Kindle Word
pipeline as the Cosmology titles (`build_docx.py` + python-docx, 6x9in Georgia, one
figure per chapter, hyperlinked TOC).

Lothar's starter list (Watson and Crick, DNA, inheritance, Mendel, methods history,
capabilities today, cloning, food industry, the Human Genome Project, knowing your own
DNA, and DNA correction toward "superhuman") plus his three follow-up requests
(biochemistry, whether quantum effects play a role in mutation, and what life will look
like in 100 years) are all covered — see `00_Chapter_Outline.md` for exactly where.
The plan also added related chapters he did not ask for by name but that the topic
needs to hang together: Franklin and Photo 51, mutation and DNA repair, epigenetics,
the eugenics/Lysenko history, PCR and forensic fingerprinting, ancient DNA and
de-extinction, embryo selection, genetic privacy, and longevity.

## Manuscript (complete)

- Prologue + 46 chapters in eleven parts + appendix, matching `00_Chapter_Outline.md`.
- About 93,000 words of body text (per the built Word file's paragraph text), roughly
  260-300 Kindle pages. Chapter lengths mostly land in the planned 1,900-2,400 word
  band; a few in Part II (chapters 5, 8, 9) run a bit shorter, around 1,500-1,700 words,
  and could be lengthened in a later pass if a fuller book is wanted.
- Voice guide followed throughout: no em-dashes, no bullet lists inside chapters, three
  invented family members (Ruth/Anna/Theo) used only for mechanism, three status words
  (settled/working/speculative) used where a claim's status matters, author's opinions
  marked "I think."
- Parts I (Shape) and II (Molecule) were written directly in this session. Parts
  III-XI were drafted by nine parallel agents against a shared brief
  (`00_Voice_Guide.md` + `00_Chapter_Outline.md` + the prologue as a voice sample), then
  checked for structure (headings, figure lines, word counts) before assembly.
- Each part-writing agent flagged a list of hedged or uncertain facts in its own report
  (dates, dollar figures, exact counts) that were not independently re-verified against
  primary sources in this pass. Before publication, a fact-check pass against the
  `12_Appendix.md` reading list is recommended, the same way the Cosmology books had an
  "error pass" after the first full draft.

## Figures: 47 of 47 filled, 36 real, 11 framed placeholders

- **25 diagrams**: drawn as original line art by `Figures/draw_figs.py` (matplotlib).
  Clean and legible, not gallery art; fine for a Kindle popular-science book.
- **11 real photographs**: fetched from Wikimedia Commons (public domain / CC) by
  `Figures/fetch_photos.py`, credited in `Figures/CREDITS.md`. Two are close-but-not-
  exact stand-ins worth a look: Figure 15 is a botanical painting, not a photo, and
  Figure 28's cave is not verified as the actual Denisova Cave.
- **11 remaining photo slots** are framed grey placeholders (auto-generated, labelled
  "PHOTO" with the caption) exactly like the Cosmology books before their photo pass:
  figures 0, 4, 19, 26, 30, 33, 34, 36, 39, 42, 45, 46. Drop a `figNN.jpg` into
  `Figures/figs/` and rebuild to fill any of them — see `Figures/CREDITS.md` for the
  full list and what each one needs to show.

## On disk for ingest

- Assembled Word file: `export/The_Copy_Is_Never_Exact.docx` (6x9in, Georgia, ~31 MB,
  47 figures embedded, hyperlinked TOC). Opens cleanly in python-docx; a Word/KDP
  previewer pass by Lothar is still needed, as with every prior book in this series.
- No cover has been made. No EPUB has been built (this pipeline, unlike the Cosmology
  one, has not yet had Pandoc wired in — can be added the same way if wanted).
- No `KDP_Description.md` (Amazon sell copy + photo credits block) has been written yet.

## Rebuild

```
python Figures/build_docx.py export/The_Copy_Is_Never_Exact.docx
```

Re-run `Figures/draw_figs.py` or `Figures/fetch_photos.py` only if regenerating figures;
both are idempotent and safe to re-run.

## Still on Lothar

- KDP previewer pass, cover design, `KDP_Description.md`.
- Optional: fill the 11 remaining photo placeholders (real photos or photorealistic
  generation via the xAI Grok Imagine setup used elsewhere in this project).
- Optional: a fact-check/error pass on dates, dollar figures, and specific counts,
  and a length pass on the three shorter Part II chapters.
- No git commit has been made for this book yet.
