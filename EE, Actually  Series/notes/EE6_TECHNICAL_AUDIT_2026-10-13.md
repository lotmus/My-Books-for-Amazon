# Book 6 Transformer Loading Technical Audit

**Date:** 13 October 2026  
**Scope:** Chapter 17 opening claim, efficiency model, transformer insulation-aging model, Worked Example 17.4, source currency, and the corresponding Appendix C entry.

## Finding and corrections

The opener tied a 45% load point directly to an insulation-aging claim and called a transformer at full load in summer several times shorter-lived without giving the thermal assumptions. The efficiency maximum is determined by the example's core and rated-load copper losses; it does not determine the insulation aging rate. The opener now identifies the 2500 kVA example and separates the loss balance from insulation aging, whose simplified model uses winding hot-spot temperature.

The original Chapter 17.5 called the IEEE C57.91 aging calculation generically, stated a 110 deg C reference, and said utilities use generic 120-150% overloads for a few hours. IEEE's current catalogue identifies **IEEE C57.91-2025** as the active guide and says it supersedes C57.91-2011. The guide's stated scope is mineral-oil-immersed transformers and step-voltage regulators. The manuscript now names the 2011 equation as a historical teaching model, identifies its scope and reference conditions, removes the generic overload percentage/duration claim, and directs actual loading decisions to the current guide and transformer-specific data. The Appendix C citation and front-matter standard list were updated. Figure 17.2 now labels the plotted equation as the 2011 teaching model.

Worked Example 17.4 previously described relative thermal-aging factors as hours of insulation life and used "bank 7.2 hours of life." Its prompt and answer now call these modeled relative-aging comparisons. At 98 deg C, ten hours correspond to about 2.8 equivalent hours at the reference aging rate. At 130 deg C, 24 equivalent reference hours correspond to about 3.4 hours under the simplified model. The answer explicitly says this is not a remaining-life estimate.

## Independent calculation check

For the Chapter 17 example's 5 kW core loss and 25 kW copper loss at rated load:

- Optimum load fraction: sqrt(5/25) = 0.4472, or 44.72%.
- At that load, copper loss is 5 kW, total modeled loss is 10 kW, and output at unity power factor is about 1118.0 kW. Efficiency is 99.1135%, consistent with the text's rounded 99.1%.
- Re-evaluation of the printed Arrhenius equation gives aging factors 0.2817 at 98 deg C, 1.0000 at 110 deg C, 2.7089 at 120 deg C, 6.9842 at 130 deg C, and 17.1995 at 140 deg C. Rounded values in the chapter agree. 24/6.9842 = 3.44 hours; 0.2817 x 10 = 2.82 equivalent reference-aging hours.

## Source and evidence limits

- [IEEE SA, C57.91-2025](https://standards.ieee.org/ieee/C57.91/7163/) lists the active edition, scope, supersession of the 2011 edition, and loading factors including ambient conditions and cooling.
- [IEEE Transformers Committee, IEEE/IEC loading-guide comparison (PDF)](https://grouper.ieee.org/groups/transformers/subcommittees/insulation_life/c57.91/LoadingGuideComparison-IEEE-IEC-R1.pdf) defines the aging acceleration factor by winding hottest-spot temperature and prints the Arrhenius equation with the 110 deg C reference.
- The full text of C57.91-2025 was not inspected in this audit. This report does not claim the 2011 equation is the current edition's equation or validate a real overload plan. Comparing the teaching model with the full 2025 guide and independent transformer-specialist review remain release gates.

## Verification

Updated `Power_and_Energy_Book6.docx` and regenerated `chapters/Book6`. Fresh extraction compared all 52 files (front/chapter/back text and figures) byte-for-byte with the mirror: no missing files, mismatches, or extras. Reconverted the post-edit Book 6 master using Kindle Previewer 3 `-convert -qualitychecks`: Enhanced Typesetting Supported, Conversion Success, 0 errors, 0 quality issues; the per-book report says no issues found. This is automated conversion evidence only, not visual device review or engineering approval. No faculty or series score increase is claimed.

Appendix B wording follow-up (13 Oct 2026): Chapter 17's revised aging discussion was correct, but Appendix B answer 7 retained a residual "hours of reference insulation life" phrase. Updated the answer to describe equivalent hours of modeled thermal aging at the 110 C reference rate and regenerated the Book 6 mirror. This does not change the limits on interpreting the teaching model as a remaining-life estimate.


Chapter 13 800 V architecture and SiC claim refresh (13 October 2026): replaced the broad statement that 2026 premium cars and fast chargers generally use 800 V, the claim that IGBTs lose to SiC, and an unsupported 5-10% range-gain estimate. The revised text explains the same-power current and I^2R relation with its unchanged-cable assumption; states that battery, cable, connector, and charger ratings jointly bound delivered power; names Hyundai IONIQ 5 and Porsche Taycan as specific 800 V-class examples; and identifies ABB Terra 360 CCS output as 150-920 V, rather than suggesting a universal fixed 800 V charger. It frames 1200 V SiC devices and switching-loss benefits as examples/tradeoffs, not universal prescriptions or guaranteed range gain. Primary references: [Hyundai IONIQ 5 specifications](https://www.hyundai.news/uk/articles/press-releases/hyundai-motor-uk-reveals-new-ioniq-5-pricing-and-specification.html), [Porsche 2025 Taycan](https://newsroom.porsche.com/en_US/2024/products/02062024_The_new_2025-_Porsche_Taycan_models.html), [ABB Terra 360](https://new.abb.com/ev-charging/terra-dc-wallbox/terra-dc-wallbox-complying-to-ul-standards), [Infineon 800 V/1200 V SiC reference design](https://www.infineon.com/evaluation-board/REF-CAV280KMSICINV), and [TI 800 V SiC inverter reference design](https://www.ti.com/lit/ug/tiduf23/tiduf23.pdf). Updated Appendix C, regenerated and byte-compared the 52-file mirror, inspected the revised paragraph on PDF page 82, and refreshed the current-master KPF (Supported/Success, zero errors/issues; embedded DOCX hash matches). This narrows a dated market claim; no committee score increase.


Chapter 13 answer-key alignment follow-up (13 Oct 2026): corrected an editing error that had replaced Practice Problem 13.7 with its answer. The problem is restored as a question; Appendix B answer 7 now gives 333 A peak (about 236 A RMS for balanced sinusoids under the stated model) and explicitly limits it to an ideal model result. Revised Problem/Answer 8 to explain conditional partial-load SiC switching-loss benefit and prohibit a universal range estimate. Inspected rendered PDF pages 84 and 147; question and key align and fit cleanly. Fresh extraction comparison: 51 content files, 51 mirror files, 0 mismatches, 0 extras (README is repository metadata). Current-master Kindle Previewer 3 conversion reports Supported/Success, 0 errors, 0 quality issues, and no issues found; embedded DOCX SHA-256 matches master: 93e540c57c60a4d5597274b5c02d1d0b4b55804b86458b9c3e43ed74b3a4ab7d. This supersedes earlier Book 6 KPF hash records. These targeted fixes do not close physical-drive validation or independent specialist review.
