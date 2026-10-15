# Status: *Life, Actually* (2 October 2026)

- Master: `Life, Actually.docx`, built by `scripts/build_book.py` from `chapters/*.md`.
- 11 Parts, 84 numbered chapters, Prologue, Epilogue; 50 figures; about 195,000 words; 718 pages at 6 × 9 in (LibreOffice render).
- Contents page numbers are pre-filled from a LibreOffice render (`scripts/toc_pages.py` → `notes/toc_pages.json`). Word refreshes them on opening (answer Yes to the update-fields prompt), because Word's pagination differs slightly.
- Part XI (chapters 77–84) is new, current to October 2026. Facts that are still moving and should be re-checked before publication: Mars Sample Return funding, Tianwen-3 and Rosalind Franklin dates, TRAPPIST-1 e and K2-18 b reanalyses, Venus phosphine, exoplanet count, Europa Clipper and Dragonfly schedules, mirror-life policy.
- Open decisions for Lothar: see the final report and the "Deliberate deviations" list in `00_Plan.md`.

## Rebuild

    python scripts/build_book.py              # writes Life, Actually.docx
    python scripts/toc_pages.py "Life, Actually.docx" && python scripts/build_book.py   # refresh Contents page numbers (needs LibreOffice)
    python scripts/draw_new_figs.py           # only if Figures 48–50 change

## Fact re-check, 2 October 2026 (PT)

Checked by web search against the sources below. Changes went into `chapters/11_Part_XI_Life_Elsewhere.md`, `chapters/12_Back_Matter.md` and, as text-only edits, into `Life, Actually.docx` (so a rebuild from the Markdown gives the same text).

| Fact (chapter) | Verdict | Change | Source |
|---|---|---|---|
| Mars Sample Return: FY2026 budget passed January 2026 without MSR; money moved to a future-Mars-missions line (Ch. 79) | Correct. House 8 Jan, Senate 15 Jan 2026; report: "does not support the existing MSR program"; $110M for Mars Future Missions. FY2027 request also ends MSR. | Cost of NASA's two January 2025 options corrected from "roughly 6 to 7" to "roughly 6 to 8 billion dollars" ($5.8–7.1B and $6.6–7.7B). | https://spacenews.com/congress-passes-minibus-spending-bill-that-rejects-proposed-nasa-cuts/ ; https://www.livescience.com/space/mars/nasas-mars-sample-return-is-dead-leaving-china-to-retrieve-signs-of-life-from-the-red-planet ; https://www.nasa.gov/news-release/nasa-to-explore-two-landing-options-for-returning-samples-from-mars/ |
| Tianwen-3: launch around 2028, samples around 2031 (Ch. 79) | Correct; sharpened. Targets the Dec 2028–Jan 2029 window, two Long March 5 launches, return 2031. | "around 2028" → "in late 2028" | https://spacenews.com/chinas-tianwen-3-mars-sample-return-mission-moves-into-spacecraft-construction-phase/ ; https://www.china-in-space.com/p/tianwen-3-mars-sample-return-mission |
| Rosalind Franklin: launch 2028 (Ch. 79) | Correct; sharpened. ESA: late 2028 on a NASA-provided Falcon Heavy, landing at Oxia Planum in 2030. | "planned for launch in 2028" → "planned for launch in late 2028 and landing in 2030" | https://science.nasa.gov/blogs/mars-rosa/2026/04/16/nasa-begins-implementation-for-esas-rosalind-franklin-mission-to-mars/ ; https://explorationscience.esa.int/project/exomars-rosalind-franklin-rfm/ |
| TRAPPIST-1 e: four transits (2025) rule out H2-dominated air, CO2-thick air unlikely, bare rock vs N2 air undecided; longer program running (Ch. 81) | Correct. 15-transit TRAPPIST-1 e/b program's first results (2026) do not change this. | None | https://iopscience.iop.org/article/10.3847/2041-8213/adf62e ; https://iopscience.iop.org/article/10.3847/1538-3881/ae28cb |
| K2-18 b: April 2025 MIRI claim ~3 sigma; AJ 2025 "does not meet the standards of evidence"; joint analysis, ~25 more MIRI transits; DMS not detected as of 2026 (Ch. 81) | Correct, except the last reanalysis sentence ("a 2026 reanalysis found the DMS signal largely disappeared once the data were processed differently"), which could not be matched to a 2026 paper, and "ethane" (the papers name ethylene and propyne). | Rewritten: hydrocarbons such as ethylene and propyne; 2026 Nature Astronomy analysis (Welbanks et al.) finds many such gases fit as well as DMS or better; binning of the MIRI data matters (Stevenson et al. 2025). | https://iopscience.iop.org/article/10.3847/1538-3881/ae0338 ; https://www.aanda.org/articles/aa/full_html/2025/08/aa55580-25/aa55580-25.html ; https://ui.adsabs.harvard.edu/abs/2026NatAs..10..234W/abstract |
| Venus phosphine: neither confirmed nor ruled out; further campaign approved for 2026 (Ch. 84) | Correct. JCMT-Venus fifth campaign approved for July 2026; no independently validated result; IR/occultation upper limits stand. | None | https://meetingorganizer.copernicus.org/EPSC2026/EPSC2026-1119.html ; https://arxiv.org/html/2409.13438 |
| Bibliography, 2025 papers | Titles and years all correct (checked against Crossref). Five were cited as online-only and now have volume and pages. Gori et al. is in print in 2026. Glavin, Madhusudhan and Wolfe-Simon (retracted 24 July 2025) already complete and correct. | Gori: NEJM 394(12) (2026): 1195–1203; Hurowitz: Nature 645 (2025): 332–340; Khawaja: Nat. Astron. 9 (2025): 1662–1671; Musunuru: NEJM 392(22) (2025): 2235–2243; UK Biobank: Nature 645 (2025): 692–701. Each keeps its online date. | https://api.crossref.org/works/10.1056/NEJMoa2509807 (and the DOIs 10.1038/s41586-025-09413-0, 10.1038/s41550-025-02655-y, 10.1056/NEJMoa2504747, 10.1038/s41586-025-09272-9); https://www.science.org/doi/10.1126/science.adu5488 |

Not re-checked in this pass: exoplanet count, Europa Clipper and Dragonfly schedules, mirror-life policy.
