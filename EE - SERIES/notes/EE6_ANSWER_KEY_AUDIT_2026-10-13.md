# Book 6 Answer-Key Audit

Date: 13 October 2026

## Book 6 e-bike range calculation (13 October 2026)

Worked Example 12.7 first converts mechanical motor output to battery input at 80% efficiency, but its final rider-assistance sentence used mechanical Wh/km as though it were battery Wh/km. At 25 km/h, 100 W of rider contribution reduces required motor output from 250 W to 150 W. Battery input falls from 250/0.8 = 312.5 W (12.5 Wh/km) to 150/0.8 = 187.5 W (7.5 Wh/km), saving 5 Wh/km. With 403 Wh usable, the illustrative range becomes 403/7.5 = 53.7 km, compared with 32.3 km without that contribution.

The DOCX master and tagged source were updated. This is a steady-speed arithmetic illustration; real range depends on terrain, rider power profile, drivetrain efficiency, wind, stops, battery condition, and reserve policy. It does not replace a measured range test.

## Follow-up: Book 6 LCL filter and cross-chapter answer integrity (13 October 2026)

Chapter 16 Worked Example 16.6's computed resonance is 2.34 kHz. Its 500 Hz to 5 kHz heuristic check did not establish separation from an actual current-loop bandwidth or stable operation under delay and grid-impedance variation. The master now says so, qualifies ideal high-frequency attenuation, and cites R. Peña-Alzola et al.'s peer-reviewed LCL design study, which ties resonance placement to controller bandwidth, switching frequency, damping, and grid-inductance robustness: [author-hosted paper](https://pure.strath.ac.uk/ws/portalfiles/portal/91561768/Pena_Alzola_etal_IEEE_TOII_2014_Robust_design_of_LCL_filters_for_active_damping_in_grid.pdf).

The full Book 6 DOCX-to-mirror extraction also caught a Chapter 2 Worked Example 2.5 mismatch: the master had a buck Coss problem paired with a PSRR answer, while the source mirror and answer described an LDO-ripple problem. The master question was restored to the PSRR version that matches the calculation. A fresh extraction now matches every Book 6 front matter file, chapter, back-matter file, and figure.

These are targeted corrections, not a full specialist review of either chapter or book. The LCL example is still a textbook calculation, not a stable controller design or grid-connected hardware validation.

## Formatting and Pagination Follow-up (13 October 2026)

A cross-book DOCX scan found four Book 6 problem statements and six worked-example solutions where direct bold formatting extended through the body. In Examples 8.7, 9.1, 9.2, 11.3, 11.6, and 20.6, restored the established bold-label/regular-body format; regenerated the Book 6 source mirror. Example 20.6 had also broken after the words "The resonant" at a page boundary. Kept its heading and problem with the full solution, moving the example to one page with its high-voltage safety note.

Fresh LibreOffice page renders were visually checked at pages 15, 53, 57, 58, 69, 77, 100, and 125. The figure caption remains with Figure 9.1; the PSRR prompt, 5 Wh/km rider-assistance answer, and LCL stability caveat remain legible. This is targeted page inspection, not a full reader-file proof or hardware validation.


## Chapter 17 residual-current protection answer (13 October 2026)

Practice Problem 17.9 asks for a leakage budget below one-third of a 30 mA RCD rating. The former answer did not calculate that budget and said the device could trip randomly at 15 mA, exactly half its rating. The corrected answer shows the strict 10 mA budget and 15 mA total, 5 mA over budget; under the product-standard threshold described by IET, the RCD must not operate at half its rated residual current. It now directs readers to split loads across suitably protected circuits and verify local requirements rather than increase a required 30 mA protection rating. The associated TT installation example retains 1667 ohms as the arithmetic 50 V ceiling but explicitly says it is not an installation acceptance target; it adds the IET UK-specific note that values above 200 ohms may not be stable and calls for measured electrode resistance and required disconnection-time checks. The DOCX master and regenerated mirror agree. Source: [IET TT earthing considerations](https://electrical.theiet.org/wiring-matters/years/2021/87-september-2021/tt-earthing-considerations/).


## Chapter 19/20 answer-boundary correction (13 October 2026)

A chapter-by-chapter comparison caught a displaced answer: Chapter 19 Practice Problem 9 asks for the isolation-barrier capacitance that limits common-mode current to 100 mA at 50 V/ns, but its Appendix B answer had contained the Marx-generator stage-count explanation. The correct result is C = I/(dv/dt) = 0.100/(50e9) F = 2.0 pF. The Marx explanation belongs with Chapter 20 Practice Problem 9. Its answer now calls 25 stages an ideal no-load full-rating lower bound and gives the sizing rule using a verified derated allowable stage voltage, including sharing and transient margins. The DOCX master and regenerated mirrors were checked for both answers. During this edit, repaired question-mark substitutions in recently added source titles. No real pulsed-power hardware validation is implied.


## Chapter 21 cold-string sizing answer (13 October 2026)

Practice Problem 21.2's terse 27 modules now shows the ceiling calculation: floor(1500 V/55.2 V) = floor(27.17) = 27, using the cold module Voc from Problem 21.1. It explicitly labels this the arithmetic limit at the stated -20 C and requires a real design to use the site's minimum design temperature, module voltage tolerance, inverter absolute maximum, and applicable equipment/code margin. The DOCX master and regenerated answer mirror were read back and agree. This is a worked-example correction, not a site-specific PV design review.

Formatting and selected-page check (13 October 2026): normalized the expanded Chapter 20 Problem 9 and Chapter 21 Problem 2 answer entries to the answer-key convention (bold number, regular body), regenerated the mirror, exported the 159-page Book 6 DOCX to PDF with LibreOffice, and inspected page 151. Both answers fit and remain readable; this is selected-page LibreOffice evidence, not full Kindle-device review.


## Chapter 20 solid-state switch tradeoff (13 October 2026)

Practice Problem 20.5 asked why semiconductor stacks were replacing spark gaps and thyratrons, a general claim not supported by the answer. Narrowed it to an IPAC2016 case study of an IGBT replacement project for an SLAC klystron modulator. The answer now explains the reported maintenance motivation (about 10,000 operating hours between thyratron replacements plus reservoir-heater adjustment), the need for series-parallel arrays, and the current-sharing, voltage-sharing, rise-time, parasitic-inductance, cooling, and arc-fault constraints. It distinguishes tested array results from the full replacement, which the paper still described as under development, and labels the vendor-authored paper as a development report rather than independent lifecycle evidence. Added the primary conference paper to Appendix C; DOCX master and regenerated mirror agree. This improves one practice answer but does not close the broader power-electronics fact-read or specialist review. Source: [Roth et al., IPAC2016 MOOCA03](https://proceedings.jacow.org/ipac2016/papers/mooca03.pdf).


## Practice-problem and answer-key numbering check (13 October 2026)

Parsed all 22 current Book 6 chapter Practice sections and the Appendix B answer sections. Every chapter has the same numbered problem set in the questions and answers; no missing or extra numbered answer was found. This structural check does not verify that each answer is correct, sufficiently worked, or safe to apply. The broader solution-depth and independent subject review remain open.


## Chapter 20 capacitor-charging safety answer (13 October 2026)

Practice Problem 20.2 previously gave only the 5 J result. The Appendix B answer now shows `E_cap = 1/2 C V^2 = 5 J`, explains that the 1 kV source supplies 10 J total and the resistor dissipates the other 5 J, and states that the capacitor still stores 5 J after charging. It directs readers to Section 20.4's isolation, discharge, and verification procedure. This improves a worked answer in the high-voltage chapter; it is not a capacitor handling or design procedure. The DOCX master and regenerated mirror match. A fresh 159-page PDF was rendered and page 150 inspected.


## Appendix B answer formatting and pagination (13 October 2026)

A full answer-key style scan found 19 paragraphs where bold formatting covered the answer body, contrary to the book's bold-number/regular-body convention. Split each into a bold problem number and regular-weight explanation. Also kept the long Chapter 12 Practice Problem 12 battery-runtime answer together; it previously broke mid-sentence across pages 146-147. The answer now begins and ends on page 147. The revised 159-page PDF was inspected across pages 141-152 and specifically at pages 146-148; answer text is regular weight and page flow is readable. The regenerated mirror remains text-identical to a fresh extraction; styling and keep-together layout settings are in the DOCX. This selected-range render is not a full-layout or Kindle-device review. A cross-book scan of numbered Appendix B answers found no analogous all-bold-body paragraphs in the other eight current masters.


Chapter 17 breaker-selectivity answer follow-up (13 Oct 2026)

Practice Problem 17.5 previously gave only the purpose of selectivity (keep the rest of the installation energized), not how coordination achieves it. Expanded the answer to explain downstream clearing before the upstream trip point using time-current curves, short-time delay, or zone-selective interlocking; it distinguishes manufacturer selectivity data from current ratings alone and identifies the upstream device's backup role. It directs verification at actual available fault current and checks interrupting/withstand ratings. The DOCX and regenerated mirror agree. A fresh 159-page LibreOffice PDF was rendered and page 149 inspected; the expanded answer fits cleanly. This is a teaching correction, not a protective-device coordination study. The previously verified Book 6 KPF predates this master and needs refresh before release. No score increase.


Chapter 19 isolation-technology comparison (13 Oct 2026)

Chapter 19.4 said digital isolators had largely replaced optocouplers in new designs, and Practice Problem 19.6 asked why this had happened. The claim overgeneralized a technology choice and the former answer treated the optocoupler LED as the only lifetime concern. Revised the section and prompt: some digital isolators offer higher data rates, more consistent timing, or higher CMTI and avoid LED aging, while both technologies remain in use. The answer now directs comparison of insulation class, working-voltage lifetime, surge rating, CMTI, temperature, signal type, and product safety certification. Added TI application brief SLLA426 to Appendix C. The 52-file mirror matches fresh extraction, DOCX ZIP integrity and parsing pass, and a fresh 159-page PDF was rendered; pages 116 and 150 were inspected. The source brief is a vendor comparison, not independent evidence that either technology is best for every application. No score increase. The current Book 6 KPF predates this master change and needs refresh before release.


Chapter 19 safeguard-scope and standards follow-up (13 Oct 2026)

The opening of Section 19.4 had implied that every user-accessible control circuit requires double or reinforced insulation, and named IEC 62368-1 without stating its product scope. Revised the text to describe product-standard safeguards and explain that insulation class depends on the complete equipment's protective architecture. It now treats the isolator as one part of the protection path and calls for checking its certified ratings plus board creepage/clearance under the final product conditions. Appendix C now identifies IEC 62368-1:2023 (corrected 2025) for AV/ICT/office equipment, IEC 61800-5-1:2022 with 2023/2025 corrigenda for adjustable-speed drives, and IEC 60664-1:2020+AMD1:2025 for low-voltage insulation coordination. Primary scope records: [IEC 62368-1](https://webstore.iec.ch/en/publication/69308), [IEC 61800-5-1](https://webstore.iec.ch/en/publication/62103), [IEC 60664-1](https://webstore.iec.ch/en/publication/59671). Regenerated the 52-file mirror and checked fresh extraction; rendered the 159-page PDF and inspected pages 116-117 and 154-155. The paragraph break now separates product-safety scope from isolator technology choice. This is not a product compliance determination. No score increase; the current KPF is stale until regenerated from this master.


## Chapter 13 PMSM current convention (13 October 2026)

Chapter 13 used T = (3/2)p psi_f iq without saying that iq follows an amplitude-invariant Park transform and is a phase-current peak. It also omitted the reluctance-torque term for salient machines. Updated the field-oriented-control explanation to show the general PMSM torque equation, state the reduced surface-PM/id=0 case, and distinguish peak from RMS current. Specified those assumptions in Worked Example 13.3 and Appendix B Problem 7; the latter now gives 333 A peak (about 236 A RMS) and explicitly labels it an ideal model result. Added MathWorks' current torque-estimator and surface-PMSM documentation to Appendix C. Sources: https://www.mathworks.com/help/simscape-electrical/ref/pmsmtorqueestimator.html and https://www.mathworks.com/help/autoblks/ref/surfacemountpmsm.html.

Independent arithmetic gives 333.3 A peak / 235.7 A RMS for Problem 7; Example 13.3 gives 96 N m, 60.3 kW at 6000 rpm, and 141 A RMS at id=0. Regenerated the 52-file Book 6 mirror and verified exact extraction match. Fresh 159-page PDF pages 81-83 were visually checked. Kindle Previewer reports Supported/Success, 0 errors, 0 quality issues; its embedded DOCX hash matches the master. This closes a convention ambiguity in two teaching examples, not a drive design or full answer-key audit. No score increase.

Chapter 21 shading estimate teaching correction (13 Oct 2026): Practice Problem 21.7 now states the equal-substring, conducting-diode, negligible-drop/current assumptions required for the ideal one-third estimate. Its answer separates the ideal voltage/power result from real irradiance, diode, module-curve, and MPPT effects. Regenerated and byte-compared the Book 6 mirror (51 content files, no mismatches/extras); the 160-page PDF was inspected on pages 131 and 152, where the question and expanded answer are legible and the number/body formatting matches neighboring items. Current-master Kindle Previewer conversion reports Supported/Success, zero errors/issues, and “No issues found”; embedded DOCX SHA-256 matches master (f32ae0f69266ac03280043a28b17e74f9f12132d0c010a9693b19a39e097dd77). No readiness-score increase; this closes one answer-key assumption gap, not the broader selected-solution review or external PV specialist review.

Chapter 20 pulse-power problem scope and solution (13 Oct 2026): Practice Problem 20.1 now states that the capacitor is discharged to zero and recharged every 20 ms, making the per-cycle energy assumption behind 50 Hz average power explicit. Appendix B derives 100 J per pulse and 5 kW delivered by the bank, distinguishes this from source input when charging losses are present, and repeats the high-voltage no-construction boundary. The 51 content-file mirror matches extraction with no extras or mismatches; PDF page 151 was inspected and the expanded answer fits cleanly. Current-master KPF reports Supported/Success, zero errors/quality issues, “No issues found”; embedded master hash is 4d2a80c8e138036421f508170fe7f13ef82328faad1245278df119b670d96447. This improves the stated model and safety boundary, not a pulsed-power build qualification or broad specialist review.

Chapter 22 end-to-end efficiency arithmetic correction (13 Oct 2026): Worked Example 22.5 now retains the unrounded product 0.905652 before calculating the 12.146 kW input and 1.146 kW total loss from 11 kW output. The component breakdown is shown explicitly: 0.389 kW in the coil link and 0.757 kW in the other stages. This reconciles the stated 90.6% rounded efficiency with the input/waste figures. Refreshed Book 6 extraction matches its 51 content files with no missing, mismatched, or extra files; inspected the 160-page PDF page 136. Kindle Previewer reports Supported/Success, zero errors/issues, and “No issues found”; embedded DOCX SHA-256 matches master (2b343eb3a3769c96bab508207d8507b8543380b70966908298f9a560299e8e50). No score increase; the correction does not constitute a full independent power-systems review.

## Chapter 1 Practice Problem 5 solution-depth follow-up (13 October 2026)

Expanded the answer from a pair of waste figures to the complete chain: 1 MW delivered output divided by 95% and 97% efficiency, corresponding input and waste at each point, the 21.7 kW reduction, and continuous annual energy savings (21.7 kW × 8760 h ≈ 190 MWh). This makes the assumed output basis and annualization visible so a learner can reproduce the result. The authoritative DOCX and regenerated `src/back.txt` match a fresh 52-file extraction; DOCX ZIP integrity and python-docx parsing pass. The 161-page LibreOffice PDF was inspected on page 141; the new answer remains regular-weight and readable within the answer key. A fresh Kindle Previewer package embeds master hash `9f9a99e358f71e4a539cf51a92cc87319ec9dba9c5caeb0e383384434d1752c6` and reports Supported/Success, zero errors/issues, and “No issues found.” This is one selected answer-depth improvement, not a complete answer-key review or independent power-electronics assessment. No score increase.

## Chapter 7 neutral-harmonic and Chapter 11 burst-loss answer follow-up (13 October 2026)

Two concise answers had omitted reasoning needed to interpret their results. Chapter 7 Practice Problem 3 now explains that a 120° fundamental phase displacement becomes 360° at the third harmonic, so balanced equal third-harmonic components add in phase in the neutral: 3 × 0.20 = 0.60 of the fundamental phase current. It labels this as the third-harmonic component and notes that phase unbalance and other triplen harmonics affect total neutral RMS current. Chapter 11 Practice Problem 3 had incorrectly called a power value a “per-cycle” loss. The revised prompt gives switching loss at 1 MHz, states the constant energy-per-cycle assumption, and excludes quiescent/transition loss. Its answer derives 0.30 µJ per cycle and 6.0 mW at a 20 kHz average switching rate.

The DOCX master passes ZIP integrity and python-docx parsing. Fresh extraction matches all 52 Book 6 mirror files. The updated Book 6 PDF (161 pages) was visually checked at page 144 for the harmonic solution and page 146 for the burst-loss prompt/answer; the Chapter 1 savings expansion remains legible at page 141. A fresh KPF embeds the current master SHA-256 `7ac09ff3331464176dc79276b1a664076e5530f4f24aa0bc87f1ae552e852e6d` and reports Supported/Success, zero errors and quality issues, and “No issues found.” All nine current masters were hash-checked against their KPFs, with clean Previewer reports. These are selected teaching fixes, not a full power-electronics answer-key audit or independent specialist review. No score increase.
