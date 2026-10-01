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
- About 95,400 words of prologue and chapter body after the length pass. Later passes stayed inside the bands. A count on 30 September 2026, after the continuity pass below, put the prologue at 938 words and left every chapter that was remeasured inside 1,900 to 2,400. Spot counts from that run: chapter 10, 2,113; chapter 11, 1,940; chapter 18, 2,049; chapter 21, 2,009; chapter 25, 2,096; chapter 32, 2,211; chapter 38, 2,125; chapter 39, 2,167; chapter 43, 2,314; chapter 46, 2,275.
- What that pass added: chapter 4, Griffith's typing work, Avery's May 1943 letter to his brother (paraphrased, not quoted), and the Hershey-Chase blender chemistry with the 1952 paper's sulfur and phosphorus splits. Chapter 8, how the poly-U tape was made, the 27 May 1961 run, the ribosome's three slots, and why several antibiotics jam bacterial ribosomes. Chapter 9, microRNAs, the distant limb enhancer of *SHH*, and the *XIST* RNA that coats one X chromosome. Chapter 17, Bateson and Punnett's sweet peas, coupling, and the reduplication scheme. Chapter 18, salivary-gland chromosome maps and Dobzhansky's seasonal counts on Mount San Jacinto. A later pass removed the bell-curve toy from this chapter, because chapter 10 already teaches the Modern Synthesis. Chapter 30, imprinting slips at *IGF2* and related genes in large-offspring calves, and the mitochondrial mismatch in a clone.
- Continuity pass, 30 September 2026. Milk is one fact in every file: Ruth cannot drink a glass (lactase switches off); Anna inherited the persistence variant from her father and can; Theo inherited Anna's copy and can. The variant sits about fourteen thousand base pairs upstream of *LCT*, in *MCM6*. A line in chapter 22 that had Ruth carrying the variant, and passing it to Anna, was wrong and has been cut. Rio Red is 1984. The fruit Ruth grew up on is Ruby Red, the 1929 bud sport. The FDA animal-cloning risk assessment is dated 15 January 2008 in chapters 30 and 34. That is the date on the FDA risk assessment and the accompanying guidance. The Federal Register notice of availability is 16 January 2008. The book uses the document date in both chapters. No primary source found in this pass gave a different day for the assessment itself.
- Chapter 39 is Ruth, Anna, and Theo at a table, labeled invented once at the start of that part, disagreeing about a spit-kit result. The chip is about 0.02 percent of one parental set. Chapter 11 points forward to the pea garden in Part IV and does not teach the ratios. The prologue keeps one scale picture, a cheek cell, two metres, a handful of mistakes in one division, and does not preview Shenzhen, a prison, or the $2.2 million price. Chapter 18 recalls the Modern Synthesis in two sentences and leaves the lecture in chapter 10. The San Jacinto counts stay. Chapter 43 meets Casgevy, then the edit, then busulfan, then each priced medicine, then the virus envelope, one at a time. Chapter 46's middle is continuous prose. It reminds the reader that the 2020 pathway is the heritable-genome-editing report's requirement for a long medical reason and broad oversight. Gattaca is one clause. The closing sentences, one letter in a billion still wrong, and the refusal to make copying perfect, are still the last words.
- Chapter 10 states the tunnelling claim as a picture of a proton found on the far side of a wall it cannot climb, then the 1963 proposal, then the 2022 calculation, then the missing experiment in a living polymerase. Working, not settled. Parts VI, VIII, IX, and X each have one dry scene: the Santa Pola marshes, the rings of plants around the Brookhaven cobalt source, deCODE's enrolment in Reykjavik, and the kitchen table in chapter 39. Methods (the Sanger ladders), dinner (the seed in the field against the seed in the vault, and the letters already sitting in teosinte), and the biobank chip each say, in that chapter's own material, that the copy is not exact.
- Figure 19 is no longer a library card catalogue. It is the 1912 photograph of the Eugenics Record Office field workers at Cold Spring Harbor, public domain, 1704 by 1174 pixels, from Wikimedia Commons. Figure 17 is the abbatial church of the Augustinian abbey of St Thomas in Old Brno, photographed by Jan Sapák, CC BY-SA 4.0, 5184 by 3456 pixels. The 800-pixel file of the same abbey was replaced. The appendix further-reading note names Judson, Cobb, Maddox, Kevles, and Mukherjee. The glossary is still there. A search after the edits found no remaining "28 January" for the FDA assessment, no line that Ruth drinks milk or carries the lactase variant, and no use of 3.1 billion as the letter count of one cell's forty-six chromosomes. The outline hook that had paired two metres with 3.1 billion was corrected to 6.2 billion for both sets.
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

## Figures: 47 of 47 filled, no grey PHOTO cards

- **25 diagrams**: original line art from `Figures/draw_figs.py`. No credit needed.
- **22 photographs**, including one botanical drawing (Figure 15). All are Wikimedia Commons files under CC0, CC BY, CC BY-SA, or public domain. Credits are in `Figures/CREDITS.md` and in the Photo Credits section of `12_Appendix.md`, which `build_docx.py` already includes, so they reach the docx.
- Captions match the frames. Figure 15 is a drawing of pea flowers. Figure 17 is the abbatial church of the Augustinian abbey of St Thomas in Old Brno, 5184 pixels wide. Figure 19 is the Eugenics Record Office field workers, 1912. Figure 28 is a limestone cave mouth, and the caption says it is not confirmed as Denisova Cave. Figure 29 is a ewe with her lamb in a barn. Figure 31 remains a 1980s electron microscope, because no free photograph of an IVF micromanipulator turned up. Figure 34 is the exterior of a poultry barn. Figure 39 is a consumer saliva tube from a different company than the one chapter 39 discusses, and the caption does not name a company. Figure 45 is a whippet in a show stance, not a dog at full stretch. Figure 46 is a newborn's feet in an adult hand. Bare photo captions now say what to look at.

## On disk for ingest

- Word file: the continuity pass rebuilt cleanly to `export/The_Copy_Is_Never_Exact_new.docx` on 30 September 2026. The builder reported 47 figures and no placeholder slots. The previous attempt to overwrite `export/The_Copy_Is_Never_Exact.docx` failed, so this build was written to the new filename and the old file was left alone. A Word or KDP previewer pass has not been done.
- Front cover: `cover/front_cover.png`, 1800 by 2700 pixels (6 by 9 inches at 300 dpi). Original artwork, title, subtitle, and author set in Georgia. Not a photograph of a person.
- `KDP_Description.md` holds the Amazon sell copy and a short credit list. The description makes no medical promise and quotes no review.

## Rebuild

```
python Figures/build_docx.py export/The_Copy_Is_Never_Exact.docx
```

## Still on Lothar

- A KDP previewer pass. Nothing in this file claims that pass has been done.
- Dollar figures and trial counts that this pass did not reopen against a new source, including the Casgevy list price cited from Vertex's 8 December 2023 announcement, are still the ones already in the chapters. They were not invented in this pass, and they were not re-audited against a fresh download.
- A fact-check pass on dates, dollar figures, and specific counts is still recommended before publication. The haploid and diploid letter counts are consistent: about 3.1 billion in one parental set, about 6.2 billion in a nucleus.
- This manuscript sits in the existing Books for Amazon git repository, which already has commits. The fixes in this pass have not been committed.
