# Book 7 REV4 external-review response — 2026-10-16

Source draft: `Packaging_Layout_EMC_and_Test_Book7_REV3.docx`. New master: `Packaging_Layout_EMC_and_Test_Book7_REV4.docx`.

## Changes

- Split the former 20-chapter Part I into Part I (Chapters 1–10) and Part II (Chapters 11–20); EMC is now Part III and the robot is Part IV. Updated the contents, chapter transitions, and in-text part references.
- Reworked the openings of Chapters 3, 11, and 21 and the bench guidance in Chapters 5, 10, 22, and 28 to make the dry voice more consistent.
- Added consequences for rail droop, a broken return path, solder fatigue, and common-mode cable current, including cross-series links checked against the current Books 4, 5, 6, 8, and 9 outlines.
- Added named, condition-specific laminate values, SAC305 expansion data, and a warning that moisture reliability does not have one universal humidity coefficient.
- Added a load-step charge example and a VNA reconnect-repeatability example. Both use stated assumptions and distinguish a screening estimate from a complete model or uncertainty budget.
- Expanded the fatigue discussion with an explicit mission-profile count and model limitations; illustrated Black-law scaling from a declared measured baseline rather than presenting an unsupported universal lifetime.
- Matched Appendix B's introductory working/usual-mistake wording to Book 8. Regenerated `chapters/Book7_REV4/` from the REV4 DOCX.

## Limits retained

- The near-field probe remains a source-finding tool unless its transfer function is calibrated; there is no universal dB uncertainty that applies to every probe and setup.
- The numerical CTE and moisture data are specific to the named material, alloy, and test conditions. Certification still follows the governing test method, test configuration, and applicable decision rule.
- A universal fatigue life or electromigration lifetime cannot be specified without the actual geometry, materials, stress profile, failure mechanism, and sample statistics. REV4 gives conditional model scaling and a declared baseline.
- Existing schematic figures were retained. The new worked examples add quantitative consequences, but this pass does not add a new comparative ideal-versus-measured emissions plot.

## Sources used

- Rogers Corporation, [RO4000 Series High Frequency Circuit Materials Data Sheet](https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4000-laminates-ro4003c-and-ro4350b---data-sheet.pdf).
- Liu et al., [SAC305 solder-joint thermal response study](https://doi.org/10.3390/mi13060908), *Micromachines* 13(6), 908 (2022).
- IPC, [IPC-9701B contents](https://www.ipc.org/TOC/IPC-9701B_TOC.pdf), thermal-cycling test method and statistical life concepts.
- NIST, [VNA receiver-nonlinearity uncertainty study](https://www.nist.gov/publications/quantifying-receiver-nonlinearities-vna-measurements-wr-15-waveguide-band), [noise effects in S-parameter measurements](https://www.nist.gov/publications/noise-influence-scattering-parameter-measurements), and [Microwave Uncertainty Framework](https://www.nist.gov/services-resources/software/wafer-calibration-software).
