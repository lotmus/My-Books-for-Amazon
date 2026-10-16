# Book 6 critical revision and review — 15 October 2026

Scope: *Power and Energy*, Electrical Engineering Series, Book 6. The authoritative DOCX was edited and its tagged-text mirror regenerated. A 523-page interim DOCX proof was inspected page by page; the final 525-page proof was rechecked at the revised Chapter 8, Chapter 11, title, and back-matter pages. The EPUB package was checked for XML validity, internal targets, media, and container requirements. This is an editorial review, not an independent engineering certification or complete external fact-check.

## Changes made

- Chapter 3, Worked Example 3.2: identifies 93.3% as the result for only three modeled losses and names omitted loss terms. This prevents a partial model from being presented as full-converter efficiency.
- Chapter 7: corrected the scope of IEC 61000-3-2; removed the universal 75 W threshold and the claim that the rule forced PFC into every PC and television. The standard applies within its specified product and test scope. Source: [IEC 61000-3-2 consolidated edition](https://webstore.iec.ch/en/publication/28164).
- Chapter 8: restored the matched PFN/load equivalent resistance for pulse-top droop, corrected Worked Example 8.4 to 97.5 µH primary (9.75 mH secondary), and keyed Practice 8.5 to the 25 Ω matched equivalent resistance (2.5 mH). The worked solutions now agree with their stated circuits.
- Chapter 11: repaired Exercise 11.3 so switching loss is dimensionally expressed in watts and the constant-energy-per-cycle assumption is explicit; the solution key remains 6 mW. Kept the full question together across the page break.
- Chapter 16: distinguishes grid-following from grid-forming control and states that virtual inertia, frequency response, and black-start capability depend on implementation and system conditions.
- Chapter 17: replaced casual panel-opening advice with a qualified-person safety frame covering isolation, stored energy, proving the tester before and after, absence-of-voltage checks, site arc-flash assessment, and PPE. Added a linked safe-isolation source: [Electrical Safety First, Best Practice Guide 2](https://www.electricalsafetyfirst.org.uk/media/btoiv1h5/best_practice-guide-2_issue-4-2.pdf).
- Back matter: moved the review request beside the author bio rather than leaving it isolated on a mostly blank page.
- DOCX page setup follows the series ebook fallback specification: 3.6 × 4.8 in with 0.3 in margins. Regenerated the Book 6 source mirror.

## Scores

Scores are candid, not targets. The earlier “zero images / missing covers / missing description” row was factually stale: this manuscript contains 27 figures, draft cover files, linked contents, and a KDP description. The updated row records that evidence.

| Criterion | Score | Specific assessment |
|---|---:|---|
| Hidden humor / deadpan British tone | 2/10 | Almost absent. That is a poor fit for the requested literary criterion but a reasonable choice for serious electrical-engineering instruction. If adding it, use occasional dry asides in low-stakes “On the Job” passages; never in isolation or arc-flash guidance. |
| Sharpness vs stakes | 8/10 | Generally clear and direct. Chapters 17 and 20 discuss severe hazards; the revised safety language is more responsible, though a book cannot substitute for training or applicable codes. |
| Content accuracy and completeness | 7.5/10 | Corrections remove several consequential overclaims. The worked problems and 22-chapter range are useful; specialist coverage is necessarily selective, and an independent engineer must still verify calculations, standards interpretation, and safety advice before publication. |
| Section boundaries | 8/10 | Parts and chapter transitions are explicit; practice and “What You’ll Actually Use” recaps give readers clear stopping points. |
| Images / figures | 8/10 | 27 relevant authored figures support circuits, waveforms, curves, and systems. They are generally placed near their discussion and remain visible in the proof; some technical graphs carry small labels at the narrow trim size. |
| Reader engagement | 7.5/10 | Worked examples, job context, and practical recaps make the material usable. The breadth and density can still overwhelm a new reader. |
| Structure | 7.5/10 | The progression from converter basics through grid, facility, specialized converters, and wireless power is coherent. Twenty-two chapters span a very broad field, and later chapters sometimes read as compressed surveys. |
| Prose | 7/10 | Mostly intelligible and economical, but functional rather than literary; some passages rely on dense technical shorthand and repeated explanatory patterns. |
| Style | 6.5/10 | The practical teaching voice is consistent but not highly distinctive. “From the Bench” and “On the Job” help, though repeated chapter templates can feel mechanical. |
| Mechanics | 8/10 | No conspicuous proof-stage defects appeared in the full visual pass. This does not replace a dedicated line-by-line copyedit of equations, units, and references. |
| Insights / wonder / payoff | 7.5/10 | Connects component-level losses to grids, data centers, batteries, and energy systems. The payoff is practical more often than surprising. |
| Internal consistency | 8/10 | The known efficiency, standards, grid-forming, and safety statements were clarified. Cross-references and terminology mostly hold; external review should still check the many assumptions across examples. |
| Formatting / presentation | 7.5/10 | Full 523-page interim proof inspected page by page; the final 525-page proof was checked at revised sections and back matter; chapter openings, figures, appendices, and links render cleanly. The small fallback trim yields a very high page count and the long Also-by list spans several screens/pages. EPUB structure has 68 internal links, 27 images, valid XML, and no broken targets or fragments. A Kindle Previewer/KDP device preview is still outstanding. |
| Overall recommendation | 7.5/10 | Recommend to technically curious readers who want a broad, calculation-rich introduction and will check the limits of simplified examples. Not yet among the strongest books on the subject: its breadth and useful scaffolding do not compensate for the need for independent technical review, more distinctive prose, and device-preview validation. |

## Release gates still open

- Independent power-electronics engineer review of equations, solved answers, standards claims, and safety content.
- Kindle Previewer or KDP preview on actual device profiles; the EPUB package check does not establish that Amazon will render every font, image, and link ideally.
- Decide whether the 3.6 × 4.8 fallback layout and 525-page print-style proof are acceptable for the intended upload workflow. EPUB is reflowable, so those printed page breaks do not represent Kindle screen pages.
- Covers and listing exist as drafts; no live listing or market evidence was checked. The “Also by” page now matches the current canonical list, including *The Digital Twin*.

## EPUB package check

Exported with LibreOffice from the revised DOCX. Checked 67 archive entries, XML parsing, 68 internal links, all linked targets and fragments, 27 image references, first-entry `mimetype`, and stored (uncompressed) `mimetype`. No structural errors found. Kindle Previewer/KDP validation was not established by this check.
