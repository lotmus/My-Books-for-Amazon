# Book 6 external review response — REV3

Date: 16 October 2026

## Review baseline

The independent review scored REV2 **7.6/10 overall** (recommendation 7.5/10). Its strongest points were the quantitative waste model, conversion-chain arithmetic, and series hand-offs. It identified voice consistency, field consequences, real-world limits, long converter pacing, reliability, and visuals as the main remaining weaknesses. REV3 has not been independently rescored. No score of 10 is claimed.

## Fixes carried into REV3

- Reworked the openings of Chapters 3, 9, and 14 and added restrained observations to selected “From the Bench” notes. The voice remains technical and dry; no punchlines were inserted.
- Added concrete consequences where converter faults reach other systems: rail sag and audio clipping, RF spurs, brown-out resets, thermal overload, early pack shutdown, and data-centre cooling/power costs.
- Added early model-limit notes for buck/boost and magnetic calculations, pointing to parasitics, component operating curves, and later measurement sections.
- Added published-data comparisons with precise limits: the Analog Devices CN0196 inductive-load current-slope example in Chapter 3, and one TI TIDA-00471 reference-board point in Chapter 9. Neither is described as the author's bench measurement, and neither is generalized beyond its stated conditions.
- Added switch-resistance temperature guidance, component-specific capacitor impedance/lifetime caveats, a TDK N87 core-loss point, and a worked magnetic thermal-budget example with explicit assumptions. It is labelled a first-pass estimate, not a universal core-loss rule.
- Expanded measurement uncertainty with instrument/probe limitations and a worked case showing when a small loss cannot be resolved confidently. Release decisions are directed to measured results with a stated uncertainty budget.
- Added a conditional capacitor-drift example for hold-up time and retained manufacturer-specific limits rather than presenting generic lifetime figures as guarantees.
- Added a high-stakes thermal-budget example and matching practice problem/solution, using Idea / Check / Usual mistake.
- Replaced the two requested schematic-only comparisons with bounded published-data plots: CN0196 current slope and the TI reference-board power balance. Other schematic figures remain explanatory illustrations, not measured claims.

## Sources added or used

- Analog Devices, [CN0196 reference design](https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/cn0196.html).
- Texas Instruments, [TIDA-00471 design](https://www.ti.com/tool/TIDA-00471) and [test report](https://www.ti.com/lit/pdf/TIDU926).
- Analog Devices, [MOSFET power dissipation and temperature coefficient note](https://www.analog.com/en/resources/technical-articles/mosfet-power-dissipation-calculation-in-highpower-supply.html).
- TDK Electronics, [N87 ferrite data sheet](https://www.tdk-electronics.tdk.com/blob/528882/download/3/pdf-n87.pdf).
- KEMET, [EDH electrolytic capacitor specification](https://search.kemet.com/component-documentation/download/specsheet/EDH477M035S9RAA).
- Keysight, [U1882B voltage/current probe deskew data sheet](https://www.keysight.com/us/en/assets/7018-01738/data-sheets/5989-7835.pdf).
- Nichicon, [aluminium electrolytic capacitor application guidelines](https://www.nichicon.co.jp/english/series_items/catalog_pdf/e-aluminum.pdf).

## Verification and limits

- REV3 DOCX rendered with LibreOffice to a 533-page PNG proof; all page contact sheets were visually screened, and the two newly plotted figures were inspected at full size.
- REV3 EPUB generated with LibreOffice's EPUB export filter. ZIP container checks passed: `mimetype` is first and uncompressed, all 38 XML-family files parsed, and 29 images are embedded.
- Visual review does not substitute for Kindle Previewer/device testing, an independent power-electronics specialist review, or an independent rescore.
- The published sources are laboratory/reference-design data from their named conditions. They do not create or imply user-owned bench data.

## Revision decision

REV1 and REV2 remain preserved. REV3 is the next manuscript revision, not a claim that every criterion is a 10. Remaining high-value checks are an independent engineer review, Kindle Previewer/device check, and a fresh critical rescore.
