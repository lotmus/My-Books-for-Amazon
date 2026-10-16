# Book 4: critical review and revision record — 15 October 2026

Reviewed the current Book 4 master after a critical read and a focused second review of revised material. The file is a tutorial and broad survey, not a complete reference for professional RF design. Scores below use the requested 0–10 scale; the humor criterion is scored for fit to this technical book, not against a fiction standard.

## Scores

| Criterion | Score | Critical assessment |
|---|---:|---|
| Hidden humor / deadpan British tone | 2/10 | The book is not written in a British comic voice, and almost no humor is present. That is acceptable for the subject; inserting jokes into safety or design material would distract. A few dry, understated observations could fit low-stakes transitions, but this is not a substantive defect. |
| Sharpness vs. stakes | 7/10 | The technical voice is generally controlled. Revised safety and design passages now distinguish simplified models from compliance or fabricated performance. Some chapter introductions still announce scope in a predictable, textbook cadence. |
| Content accuracy and completeness | 7/10 | The book is unusually broad and contains substantial worked material, but several earlier claims needed correction: microwave open/short measurement, filter stopband behavior, antenna matching, array steering, narrow-strip microstrip equations, and the scope of exposure assessment. Those are now corrected or qualified. The breadth still forces simplification, and a qualified RF specialist has not independently checked the full manuscript. |
| Section boundaries | 8/10 | Parts and chapter divisions are easy to follow. The Chapter 18 title now reflects the actual coupling-design deliverable; its added workflow identifies the missing substrate, EM, layout, and prototype steps. Cross-book signposts are useful. |
| Images and figures | 7/10 | The 54 figures are relevant and generally support the examples; computed plots make several numerical relationships legible. The book still leans on plots and block diagrams where a few detailed test setups, circuit layouts, or annotated field diagrams would teach more. |
| Reader engagement | 7/10 | Hooks, practical contexts, examples, bench notes, and exercises give the reader repeated ways into the material. The 52-chapter span can feel like a reference survey, and some topics receive only an introductory treatment. |
| Structure | 7/10 | The four-part progression from passive networks through active devices to technologies and applications is sound. The later parts expand the book substantially; transitions help, but a few sections feel adjacent rather than causally developed. |
| Prose | 7/10 | Usually clear and concise, with useful numerical specificity. It is readable technical prose rather than literary prose; some explanations repeat a claim in the chapter overview, section text, key idea, and closing list. |
| Style | 6/10 | The voice is practical and consistent but not highly distinctive. Repeated chapter devices are helpful scaffolding, yet they make the book's rhythm predictable across 52 chapters. |
| Mechanics | 8/10 | The master is mechanically clean in the inspected passages, with consistent units and terminology. Numerical and parser checks pass. A full copyedit remains useful after subject-matter review because the book is long and dense. |
| Insights, wonder, and payoffs | 7/10 | The examples make important scale changes tangible: mismatch, Q, radar range, phase noise, and device limits. The book has satisfying engineering payoffs, though its survey breadth sometimes substitutes a map of the field for deeper design insight. |
| Internal consistency | 8/10 | Cross-references and chapter ownership are mostly coherent. The current parser scope is explicitly limited to legacy Touchstone 1.x; date-sensitive satellite details are qualified. The exposure chapter now separates FCC and ICNIRP quantities and avoids treating a screening calculation as certification. |
| Formatting and presentation | 7/10 | The 293-page PDF render has stable pagination, readable headings, equations, figures, and exercise pages in the reviewed render. A 293-page contact-sheet pass and full-resolution inspection of changed Chapter 33 pages found no clipping or flow defects. The current master also changes one Chapter 33 bench-note sentence and the front-matter description of worked-example inputs; those final changes were not rerendered as a separate full-book PDF after LibreOffice stalled at shutdown. Kindle-device/Previewer review remains outstanding. |
| Overall recommendation | 7/10 | Recommend it as a broad, worked introduction for technically literate readers who want one route through RF, microwave, and transceiver topics. I would not call it one of the strongest books on the topic yet: its range is a strength, but depth varies, some visuals could teach more, and specialist review plus a final Kindle check are still absent. |

## Changes made

- Applied edits to the current tracked `EE - SERIES` Book 4 master, retaining its newer HF-propagation qualification and cited ARRL source that were absent from the local untracked snapshot.
- Replaced the front-matter overclaim that every worked-example number was computed rather than estimated; it now says examples state their inputs and calculations and warns that modeled or typical values are not device guarantees.
- Rewrote Chapter 5's S-parameter introduction to explain why ideal open/short terminations are difficult at microwave frequencies and why traveling-wave reference impedances are used.
- Qualified Chapter 6's filter stopband description, Chapter 7's antenna/matching distinction, Chapter 8's phase steering and beam squint, Chapter 11's bandwidth estimate, and Chapter 13's Chu-bound and single-resonance assumptions.
- Added the narrow-strip Hammerstad branch to Chapter 10 and stated the model's assumptions and limits.
- Renamed Chapter 18 to “A Bandpass Filter from Specification to Coupling Design” and added the missing path from coupling values through EM extraction, complete-layout simulation, and prototype tuning.
- Replaced editorial filler in Chapter 41 with comparison criteria and a caveat on practical class-performance ranges.
- Rewrote Chapter 33 to distinguish screening estimates from compliance assessment, separate FCC requirements from ICNIRP's local absorbed-power-density method above 6 GHz, and avoid implying that proximity sensing is universal.

## Verification and remaining work

- Recomputed 87 printed-value assertions against the revised master: pass.
- Re-ran 24 legacy Touchstone 1.x format/unit combinations: pass.
- Pre-review history (legacy filenames): the 293-page REV4 PDF was rendered and inspected, including full-resolution checks of revised Chapter 33 pages. The next draft, now the externally reviewed REV1, changed one additional sentence on the Chapter 33 bench note; a whole-book REV1 render was not confirmed at that stage because LibreOffice hung during shutdown. The later canonical REV3 has since rendered as a complete 300-page document.
- The FCC rules and KDB procedures are jurisdiction- and device-specific; ICNIRP 2020 uses different local exposure quantities above 6 GHz. Consult the current [FCC rule](https://www.ecfr.gov/current/title-47/section-1.1310), [FCC portable-device guidance](https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=20676&switch=P), and [ICNIRP 2020 guidelines](https://www.icnirp.org/cms/upload/publications/ICNIRPrfgdl2020.pdf) for an actual assessment.
- Remaining before publication: independent RF-specialist review, current product/specification checks where date-sensitive, Kindle Previewer/device inspection, and finished cover files.
