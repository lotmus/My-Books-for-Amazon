# Book 4 REV6 — response to external REV3-2 and REV4 reviews

Date: 16 October 2026

## Result

The supplied REV3-2 review scored the book 7.5/10; the REV4 review scored it 7.6/10. Both identified the same work: carry the understated voice and consequence language beyond the opening, break up the amplifier run, quantify environmental and measurement limits, and say what is lost when an ideal calculation fails in a real radio.

REV6 incorporates the fixes that can be supported from available sources and the existing manuscript. It is an internal revision, not a new independent review. My current overall score is **7.9/10**. The book is a useful quantitative middle-ground volume, but its voice, figure set, and prose distinction still do not put it among the strongest specialist RF texts.

## Changes made

- Kept the REV5 consequence-focused openings and bench notes across the amplifier, matching, filter, antenna, and laminate chapters. Examples connect a drifted match to lost link margin, a shifted filter pole to unwanted response, and amplifier nonlinearity to emissions that can fail a report while nominal power appears healthy.
- Preserved the three movements and Contents entries for Chapters 20–41, giving the long run clearer turns between power and linearity, receiving and links, and robustness and measurement.
- Kept the early warning in the load-line chapter that ideal device loads move with package, pad, via, temperature, and manufacturing variation; directs the reader to load-pull and measurement.
- Retained sourced Rogers RO4350B and Murata dielectric temperature data, with limits on what those figures predict. The book does not claim a universal humidity correction or parasitic temperature coefficient.
- Added a KEMET automotive X7R example: the cited family datasheet lists a maximum 3% capacitance loss per decade-hour and says the reference time (48 or 1,000 hours) is part-specific. The text explicitly limits this to that component family and does not turn it into a universal match or efficiency drift rule. [KEMET datasheet](https://content.kemet.com/datasheets/KEM_C1023_X7R_AUTO_SMD.pdf)
- Added a high-stakes, non-efficiency example in Worked Example 23.1. ETSI TS 138 104 V19.6.0 sets a 3.5% EVM limit for PDSCH 256QAM on base-station types 1-C and 1-H. A hypothetical 4.0% specified-test result is 0.5 percentage point over. The passage says this is a waveform-level standard test, not a PA-only verdict, and that CW output power cannot establish compliance. [ETSI TS 138 104 V19.6.0](https://www.etsi.org/deliver/etsi_ts/138100_138199/138104/19.06.00_60/ts_138104v190600p.pdf)
- Revised the Chapter 37 measurement discussion to distinguish absolute level accuracy from ratio uncertainty. A reading 1 dB inside a limit is not decisive when the instrument's absolute level accuracy is ±2 dB; an ACLR ratio needs its own uncertainty analysis, including frequency response, attenuation, noise, and repeatability. Certification still requires the prescribed setup and uncertainty budget.
- Adjusted the Chapter 22 ending so “What You’ll Actually Use” stays together and does not strand its final subheading and bullet across pages.
- Preserved the existing modelled ideal-versus-parasitic comparison in Figure 3.1. The figure is explicitly a model, not measured hardware. No measured-versus-simulated board plot was invented.

## Review against the requested criteria

| Criterion | REV6 score | Current assessment |
|---|---:|---|
| Hidden humor / deadpan British tone | 7.0 | The dry observations now recur in openings and bench notes, but the technical body remains mostly straight exposition. No jokes added. |
| Sharpness vs stakes | 8.0 | Failure consequences are clearer, especially emissions, link margin, and shifted filter response. More of the book could sustain this pressure. |
| Content accuracy and completeness | 8.6 | Source-backed environmental examples and a current standard example improve completeness. Physical component and board behavior remains design- and setup-specific. |
| Section boundaries | 8.5 | The three movements make the lengthy middle more legible; chapter progression and hand-offs remain clear. |
| Images / figures | 6.5 | Relevant figures and the modeled Figure 3.1 help, but much of the set remains schematic. No real hardware data are available for a measured comparison. |
| Reader engagement | 8.0 | Concrete consequences and a standards example improve usefulness; the book remains primarily utilitarian. |
| Structure, pacing, arcs, and information flow | 8.4 | Part II now has explicit turns and Chapter 22's ending reads cleanly. The amplifier material is still long. |
| Prose | 7.7 | Clear, more vivid where outcomes matter, but technical exposition is still often functional. |
| Style | 7.2 | The understated voice is more consistent; template repetition and long explanatory passages remain. |
| Mechanics | 8.7 | No substantive mechanics defect surfaced in the revision and layout review. |
| Insights, wonder, payoffs | 7.8 | The EVM example supplies a practical pass/fail consequence; the larger payoff remains calculation and design judgment rather than narrative discovery. |
| Internal consistency | 8.6 | The text separates screening calculations, component-specific behavior, waveform requirements, and certification claims. |
| Formatting and presentation | 8.2 | Clean render, clear parts, and fixed Chapter 22 break; figure variety remains a limitation. |
| Overall recommendation | 7.9 | Recommendable as an accessible, quantitative middle-ground volume. Not yet among the strongest books on the topics; specialist texts remain deeper. |

Scores are my internal critical assessment after these changes; the two supplied external scores apply to REV3-2 and REV4, not REV6. The REV6 assessment is not an RF-specialist sign-off.

## Not responsibly generalizable or verifiable here

- There is no defensible universal X7R aging rate for every capacitor, nor a universal temperature- or age-driven efficiency degradation multiplier for an RF stage. The cited number is component-specific; designs must use the selected part's datasheet and qualify the assembled network.
- Df, humidity response, package parasitics, and via behavior depend on material, construction, frequency, geometry, and environment. A universal numerical correction would be misleading.
- The book has no measured RF board data. A valid measured-versus-simulated S-parameter figure, load-pull result, or emissions margin requires a specified physical board and calibrated measurement. The existing Figure 3.1 stays identified as modeled.
- The ETSI example illustrates the stated conformance threshold and a hypothetical result; it is not evidence that any particular radio passes or fails certification.
- A specialist RF engineer should still check the design examples, component choices, and standard-specific language. Kindle Previewer inspection and series-cover/listing work remain open.

## Production checks

REV6 was rendered through the installed LibreOffice command-line renderer to 295 pages. All page contact sheets were reviewed; key revised pages were checked at full resolution. After the Chapter 22 pagination fix, the final render remains 295 pages and the revised ending is together. The tagged-text mirror was regenerated from the DOCX. The preserved user delivery-folder REV5 was not overwritten.
