
## Book 6 Switching-Loss Review (13 October 2026)

The earlier buck-converter examples counted output-capacitance loss for only one switch and treated a single constant Coss as generic. The revised text now accounts for both high-side and low-side devices in the synchronous buck, explicitly labels constant Coss as a first-order approximation, and directs real-device estimates to datasheet Eoss or integration of vCoss(v). Worked examples, practice answers, Appendix B, Appendix C, and both figures now use the corrected model.

Corrected worked-example totals are 2.552 W (88.7%) at 500 kHz, 4.204 W (82.6%) for silicon at 1 MHz, and 1.974 W (91.0%) for the deliberately controlled GaN comparison at 1 MHz. At 0.2 A, Chapter 11's model gives 50.4% forced-PWM efficiency and 87.4% burst/PFM efficiency at a 50 kHz average switching rate. These remain illustrative estimates; device curves, parasitics, controller behavior, thermal effects, and hardware measurements are outside the model.

The saved DOCX captions and embedded image bytes were inspected; embedded images match `fig9_1.png` and `fig11_1.png`. Source equations and worked values were checked against manufacturer application notes: [Infineon CoolSiC datasheet application note, §4.3.8](https://www.infineon.com/assets/row/public/documents/60/42/infineon-an2025-10-understanding-and-interpreting-the-coolsic-mosfet-1200v-datasheet-applicationnotes-en.pdf) and [Microchip AN1471](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ApplicationNotes/ApplicationNotes/01471A.pdf). The figures were visually inspected. This is not bench validation or a full chapter audit.


Figure 9.1 accessible-description correction (13 Oct 2026): a line-by-line comparison found stale approximate totals (2.52 W, 4.13 W, 1.90 W) in the figure's alt description although the caption, plot, and worked examples reported 2.552 W, 4.204 W, and 1.974 W. Updated the embedded DOCX image description to the exact worked totals and clarified the common 0.90 W conduction segment; regenerated Book 6's mirror. The saved master contains one updated description, the mirror contains the new values with all three stale totals absent, and the embedded chart asset is unchanged and visually shows the exact values. This corrects accessible text; it does not verify screen-reader usability.


Post-accessibility-edit conversion: the current Book 6 master (including the corrected Figure 9.1 description) was included in a fresh all-nine Kindle Previewer 3 batch. Its row reports Supported, Success, zero errors, and zero quality issues; its individual report says no issues found. This confirms conversion, not screen-reader or device-layout usability.


Synchronization verification: a fresh extraction of the updated master matches all 52 files in the Book 6 mirror byte-for-byte. The embedded Figure 9.1 image bytes match ig9_1.png; only the image description changed.


Chapter 9.7 cooling-claim correction (13 Oct 2026): replaced the unsupported universal statement that every high-power converter/accelerator above a wattage cutoff uses forced air or liquid cooling, and removed a claimed factor-of-two-to-four airflow reduction as a general rule. The revision now ties the cooling choice to losses, power density, enclosure, airflow, acoustics, reliability, and service constraints; it describes TI's about-50% reduction only as a specific 100 LFM power-tool example and says cold-plate ratings need matching flow, coolant, interface, and temperature boundary. Added TI's SLVA462 heatsink report and its power-tool thermal-design article to Appendix C. The current DOCX exports to a 159-page PDF; page 60 was inspected, and the revised paragraph remains legible with Worked Example 9.5 on the page. A fresh extraction matches all 51 content/figure files in the mirror byte-for-byte. No overall score change: this fixes one overgeneralized explanation and is not a whole-book thermal-design validation.
