# Electrical Engineering Series: Cautious Buyer Review

**Review date:** 12 October 2026  
**Perspective:** A technically curious buyer deciding whether a book will repay its cost and time. This review uses the repository manuscripts, KDP draft descriptions, and production notes; it is not based on Amazon customer reviews, final Kindle previews, or independent lab testing.

## Buying Verdict

The series has a credible practical identity: it connects equations to parts, measurements, design decisions, and worked examples. Books 1–5 and 7–9 look like the strongest buys for a reader with a defined goal. Book 5’s earlier review warning was stale: its current appendix contains 256 full worked solutions, matching the draft listing. Book 6 has a concise answer key, now disclosed in its preface; its wider fact-read remains unfinished. Books 8–9 need physical hardware validation and release-quality listings/covers. Do not buy all nine at once: choose by topic, and confirm the final listing matches the delivered edition.

Scores below estimate **value to the intended buyer**, not technical correctness alone. The series remains in draft status in the score ledger; covers/listings are incomplete for most volumes.

| Book | Buyer value | Regret risk | Cautious-buyer verdict |
|---|---:|---|---|
| 1. Foundations of Electronics | 8/10 | Medium | Best entry point; buy if you want a structured, equation-based foundation and will solve problems. |
| 2. Circuits, Components, and Control | 8/10 | Medium | Strong practical follow-on for analog, digital, and control design; expect some overlap in components and control examples. |
| 3. Semiconductor Physics and Devices | 8/10 | Medium | Broad and unusually practical device-to-model coverage; buy for device understanding, not a quick circuit cookbook. |
| 4. RF, Microwave, and Transceivers | 8/10 | Medium-high | The most ambitious specialist volume; substantial value for RF learners, but its 52-chapter breadth risks uneven depth. |
| 5. Communications, Wireless, and SDR | 8/10 | Medium | Strong, broad course with 256 fully worked solutions verified in the current source mirror; still use current standards and platform documentation for version-sensitive details. |
| 6. Power and Energy | 7/10 | Medium | Strong project and converter coverage. Appendix B is a concise answer key, now disclosed in the preface; buy if you can work from compact substitutions, and wait if you want tutor-style derivations for every problem. |
| 7. Packaging, Layout, EMC, and Test | 7/10 | Medium-high | Distinctive, practical subject; the documented Book 7/9 TDR/VNA overlap is now scoped, and 227 exercise prompts have matching answer entries. The broader fact-read and solution-depth review remain open. |
| 8. Firmware and Software for Electronics | 8/10 | Medium-high | Strong breadth and exercises; board examples need real-hardware validation, and the final edition/listing is not ready. |
| 9. Test and Measurement Instruments | 8/10 | Medium-high | Potentially the most immediately useful bench reference; check the final specification date and hardware-tested tracer example. |

## What a Buyer Is Paying For

The strongest value proposition is not simply “nine textbooks.” It is the repeated attempt to answer: what should I calculate, what should I build or measure, what usually goes wrong, and how do I check the answer? Books 1–4 and 7 emphasize worked solutions; Books 8–9 also have substantial exercise/example inventories recorded in their review notes. The “What You’ll Actually Use” and “From the Bench” features can help a student distinguish core working knowledge from material included for completeness.

That approach is valuable if you want a guided course and will do the exercises. It is a poor fit if you want a lightweight overview, a quick reference with no prerequisites, or guaranteed plug-and-play projects. Several books assume algebra, circuit familiarity, programming tools, instruments, and/or specific boards. Projects should be treated as learning designs, not as proof that every reader’s particular hardware revision will work unchanged.

## Volume-by-Volume Buyer Notes

### Books 1–3: Foundation, circuits, devices

Book 1 is the clearest starting purchase. Its scope is unusually broad—physics, engineering math, and circuit analysis—and the reader lab ties the ideas together. A buyer should expect equations and practice rather than a gentle popular introduction. Its 38 chapters may feel survey-like in places, so it is not a replacement for a full calculus or electromagnetics course.

Book 2 adds the most recognizable day-to-day design material: op-amps, real components, filters, logic, and control. Its strongest value is the use of real datasheets and bounded SPICE fits. Some overlap with Book 1’s circuit fundamentals and Book 6’s power/control applications is natural; the buyer should expect Book 2 to own component-level circuit design.

Book 3 moves from device physics to usable models, datasheets, and semiconductor technologies. The expanded scope spans manufacturing, sensors, photonics, and ASIC/FPGA decisions, so specialists may find some chapters introductory. Its payoff is connecting physical mechanisms to the models used in design.

### Books 4–7: RF, communications, power, and implementation

Book 4 is a substantial RF reference with broad device and system coverage, examples, and design projects. It is a good match for someone deliberately moving into RF. Its size and breadth increase the chance that some subjects are introductions rather than complete design treatments; buyers should use it alongside current datasheets and vendor application notes.

Book 5 has a compelling communications-to-SDR scope and its current Appendix B says each answer is fully worked. The refreshed source mirror confirms worked reasoning and checks, and the pass-2 note records all 256 solutions expanded from the prior short-answer set. The earlier buyer review incorrectly relied on a stale scorecard entry; the standing author instructions also confirm the biographical detail is correct. The remaining buyer caveat is breadth and date-sensitive wireless standards, which should be checked in the final edition.

Book 6 covers real energy and power projects. Its Appendix B gives concise answers rather than a worked derivation for every problem, and the preface now makes that distinction clear. This suits readers comfortable deriving steps from the chapter examples; readers who want full tutoring should wait for expanded solutions. The broader prose fact-read remains open.

Book 7 fills a useful gap that many electronics series skip: packaging, PCB layout, EMC, and test. The 227 counted practice prompts have 227 numbered answer entries, but that structural match does not grade the reasoning or prove every answer is fully worked. The documented Book 7/9 overlap in TDR/VNA basics and calibration is scoped: Book 7 Chapter 20 centers board coupons, stack-up correlation, and production acceptance, while Book 9 owns instrument operation and calibration. The earlier buyer-review phrase “noted internal repetition” did not identify additional passages; the targeted review records this specific boundary fix, not a claim that every repeated explanation has been eliminated. A broader fact-read remains open. This is a promising specialist purchase, but inspect the table of contents and sample for a narrowly specific topic.

### Books 8–9: Firmware and measurement

Book 8 spans programming, embedded systems, real-time behavior, sensor fusion, edge AI, and HDL. Its review found strong examples and exercises, but this is too much territory for a buyer to expect exhaustive coverage of every platform. The Book 8 checker currently checks 30 of 87 listings; 57 are unavailable through that checker here and none failed. Separate .NET checks build four projects and pass 13 parser/bench tests. Board-dependent examples still lack hardware runs. Buy it as a broad practical guide; verify the target platform and code sample before relying on a project.

Book 9 has the strongest immediate bench-reference promise: instrument selection, safe measurement, uncertainty, characterization, and automation. Safety wording was corrected in the manuscript, but the mini curve tracer still needs a physical hardware run, and vendor specifications/prices need a publication-time recheck. Use the instrument’s own ratings and manual for live work. Buy after those release checks, especially if you need the exact model-specific procedures.

## Overlap and Edition Risks

Some overlap is useful reinforcement: Book 1 introduces fundamentals; Book 2 applies circuit reasoning; Book 3 explains the devices; Book 4 develops RF hardware; Book 5 develops communication signals and systems; Book 7 handles implementation and EMC; Book 8 handles code; Book 9 handles measurement. The sales descriptions and review notes show reasonable boundaries between these homes.

The likely repeat zones are Book 4/5 (radio hardware versus communication/modem theory), Book 2/6 (control and power applications), and Book 7/9 (test methods versus instruments). The buyer should get complementary treatment if each book points clearly to the other and avoids reteaching whole chapters. The current continuity audit confirms the flagged Book 2 section pairs have distinct purposes and cross-references. A Book 7/9 overlap in TDR/VNA fundamentals, calibration, S-parameter definitions, and IF-bandwidth basics has now been reduced by refocusing Book 7 Chapter 20 on board-level coupon design, stack-up correlation, and production acceptance, with reciprocal pointers to Book 9. The broader fact-read remains open before calling the series polished.

A practical risk across the series is version drift: wireless standards, software APIs, prices, and vendor specifications age faster than fundamentals. Date-sensitive claims need visible edition dates and links or references to primary vendor documentation. Covers, descriptions, and the actual downloadable edition must also agree on exercise counts and whether solutions are fully worked.

## Recommendation

For a cautious buyer: start with **Book 1** if you need foundations; choose **Book 2** for circuit design; **Book 3** for semiconductor devices; **Book 4 or 5** only if RF/communications is your target; **Book 7** for PCB/EMC work; **Book 8** for embedded firmware; and **Book 9** for bench measurement. Book 5 is a reasonable buy for its intended reader; the solution discrepancy noted in the first version of this review was already fixed in the current manuscript. Choose **Book 6** if a concise answer key suits your study style; wait if you expect a derivation for every exercise. Its broader fact-read remains incomplete. For Books 8 and 9, wait for physical validation if you need proven, reproducible hardware projects.

Before spending, check the free sample for the level of math, page layout, chapter depth, and solution style you personally want. The current evidence supports a promising technical series, but it does not yet justify treating every volume as a finished, independently validated purchase.

Book 5 Chapter 8 now distinguishes the EU-harmonized 5945–6425 MHz WAS/RLAN allocation from U.S. 6 GHz device rules. It adds LPI, VLP, AFC-controlled standard-power, and GVP device classes, including the GVP rule effective 27 April 2026, and adds FCC 20-51, FCC 24-125, FCC 26-1, and Commission Decision (EU) 2021/1067 to Appendix C. The chapter mirror and source mirror were updated. This corrects an important jurisdiction/snapshot omission; the full standards and vendor fact-refresh remains open, so scores are unchanged.

Book 6's 65-minute rover runtime is now visibly an estimate under constant average load and nominal pack voltage, not an assured run time. The answer identifies voltage sag, cutoff, temperature, aging, converter behavior, and stall current as variables. This improves purchase/use expectation clarity but does not establish field runtime.

The Book 6 quad example's 6-minute figure is now presented as an ideal capacity estimate, with battery, propulsion, current-peak, and operational-reserve factors called out. It cannot guarantee the flight time of a real airframe.


Book 7 buyer-note refresh (13 Oct 2026): corrected the stale instruction to verify a prior, unspecified repetition trim. The documented Book 7/9 TDR/VNA boundary is already revised, and the current structural audit pairs all 227 counted prompts with answer entries. The revised note explicitly limits what answer-count matching proves and leaves broader fact and solution-depth reviews open. The buyer score remains 7/10; no score increase is supported by these structural checks alone.


Book 7 solution-depth follow-up (13 Oct 2026): expanded Chapter 12 Practice Problem 5. With the dielectric constant and other dimensions fixed, the answer explains that a wider trace increases 0.8w + t in the formula denominator, reducing the logarithm and estimated characteristic impedance. The first render exposed unsupported Greek glyphs and body-wide bold; the final answer uses plain-text wording, bolds only the number, and keeps the explanation regular. The DOCX master and regenerated mirror agree. LibreOffice PDF page 166 was inspected and is legible. This local correction does not complete the 227-solution review or change the 7/10 buyer score.


Book 6 solution-depth follow-up (13 Oct 2026): Appendix B Chapter 19 Problems 1-4 now show the gate-current, dynamic-power, bootstrap-capacitance, and Miller-current calculations with units and key limits. The DOCX and regenerated mirror agree; the updated PDF answers are legible on pages 151-152. This makes four answers independently reproducible but leaves the answer key concise overall; the buyer score remains 7/10 because the broader key and power/safety review are still open.
