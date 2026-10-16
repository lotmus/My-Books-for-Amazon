# Foundations of Electronics — external review response and REV2 scorecard

Date: 15 October 2026

## Source review

The external reader scored the book 7.1/10. The most actionable points were a flatter voice than the later series volumes, insufficiently quantitative figures, weak practical consequences for common errors, an unclear analog-first rule, thin measurement-uncertainty guidance, and too few numerical bridges between Parts I, II and III. The claims that Chapter 15 only handled significant figures and that uncertainty was largely absent were already stale against the current REV1 text: it contained uncertainty propagation, worked DMM examples, and a full ESP32-S3 ADC error budget. REV2 makes that material easier to locate and extends it with a named instrument/probe budget.

## Changes in REV2

- Added a quantitative Coulomb-force versus gravity figure in Chapter 1, with the one-metre comparison and its ratio.
- Replaced the Chapter 19 time-response figure with a dimensioned RC plot using the chapter's 47 kΩ and 10 µF example; added a concrete consequence for a tenfold resistance error.
- Added a quantitative resonance phasor figure in Chapter 36, tied to the existing RLC example and showing equal, opposite reactive voltages whose magnitudes exceed the source.
- Added a Chapter 15 subsection on reading actual meter and probe specifications, with a Fluke 117 worked accuracy calculation, probe-loading limits, and the ESP32-S3 ADC test conditions.
- Clarified that “analog first” is a teaching order, then named the measurements for which sampling, calibrated conversion, timing, logging, I²C, radio, or display make the ESP32-S3 appropriate.
- Added numerical transitions from Part I to later RF work (Chapter 12) and from Part II to a sensor divider and ADC range check (Chapter 25). Chapter 38 already had a numerical hand-off.
- Added concrete outcomes for unit-prefix confusion, wrong feedback sign, supernode setup, power calculation, RMS-versus-peak confusion, and component tolerance.
- Added a checked supernode example to Chapter 28, placed after its other worked examples and before the bench note.
- Sharpened several chapter openings and explanatory passages without adding jokes or changing the book to a British comic register.

## REV2 scorecard

Scores are a strict editorial reassessment after the changes, not a claim of independent subject-matter certification. The book has not yet had an independent EE solution audit or Kindle Previewer check.

| Criterion | Score / 10 | Assessment |
|---|---:|---|
| Hidden humor / deadpan British tone | 4.0 | The revision adds dry restraint (“the sign mistakes are not”; “The notation is small. The consequence is not”), but the manuscript is not distinctly British and should not pretend otherwise. Humor remains occasional. |
| Sharpness vs stakes | 7.0 | Unit, feedback-sign, RMS, ADC, supernode, and resonance errors now have tangible outcomes. Some warnings elsewhere remain generic and the power-factor stakes are not yet tied to a Book 6 design example. |
| Content accuracy and completeness | 8.0 | The core foundation is broad and coherent; the new calculations were checked. A systematic independent technical audit of all worked solutions and claims is still outstanding. |
| Section boundaries | 8.5 | Parts and chapter hand-offs remain easy to follow; Chapters 12 and 25 now make their numerical links explicit. |
| Images / figures | 6.5 | Three quantitative figures improve the standard. The field and potential sketches and Smith-chart constructions remain mostly schematic; REV2 does not repair every figure criticized. |
| Reader engagement | 7.5 | Reader Lab framing and consequential examples make the calculations more useful. Some chapters remain exposition-first, with little direct lab follow-through. |
| Structure, pacing, information flow | 8.0 | The physics-to-mathematics-to-circuits sequence works, and the Part II bridge is stronger. The middle preparation still feels long before the circuit payoff. |
| Prose | 7.0 | Clear, technically controlled prose with several more memorable transitions. Much of the book remains functional rather than vivid. |
| Style | 6.5 | A restrained series voice is emerging, though it is not yet consistent across 38 chapters and should not be sold as a comic or specifically British voice. |
| Mechanics | 8.5 | No new mechanical defect was found in the changed material; the tagged source mirror was regenerated. |
| Insights, wonder, payoff | 7.5 | The force ratio, ADC resolution-versus-error figure, and resonance voltages deliver stronger numerical payoffs. Wonder is still episodic rather than a through-line. |
| Internal consistency | 8.5 | The analog-first rule now has limits, and the new values agree with the stated examples and component values. Later-book claims still merit a series-wide cross-reference audit. |
| Formatting and presentation | 7.5 | All 202 rendered pages were contact-sheet scanned; changed figure and chapter pages were inspected at full resolution. New material is legible and no clipping or overlap was found. Existing sparse pages and some dense example pages remain. |
| Overall recommendation | 7.8 | Recommendable as a quantitative starting volume for the series. It is still not among the strongest introductory texts in physics or circuit analysis; a full solution audit, Kindle-device check, and more complete visual redesign are needed for that claim. |

## Remaining work

- Independent electrical-engineering review of worked solutions, hardware claims, and the complete series hand-offs.
- Kindle Previewer/device check.
- Series cover and KDP description.
- A later visual pass for field, potential, and Smith-chart figures, plus consistent treatment of pedagogical boxes.

Do not raise the score above 7.8 until those checks are complete. This is an editorial score, not a publish-ready or expert-verified score.
