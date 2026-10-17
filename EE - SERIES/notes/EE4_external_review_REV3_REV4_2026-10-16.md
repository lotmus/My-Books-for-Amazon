# Book 4 external review of REV3 and REV4 response — 16 October 2026

## Review result

The external review of `RF_Microwave_and_Transceivers_Book4_REV3.docx` scored the manuscript 7.4/10. It praised the technical core, the Chapter 1 capacitor example, internal consistency, and the series hand-offs. It asked for more restrained voice, consequences that reach the field, quantified laminate and measurement limits, earlier ideal-versus-built warnings, stronger amplifier pacing, and more useful temperature/lifetime treatment.

## REV4 changes

- Reworked the openings of Chapters 11, 23, and 30, plus the From the Bench passages in those chapters, to carry a quiet, dry voice without adding punchlines.
- Made the consequences explicit for the already-present cases: a capacitor above SRF can put RF on a bias rail; a design beyond its Bode–Fano limit gives up link margin; missed Doherty load modulation removes the intended back-off efficiency peak; and a 30 dB fade takes the worked link below sensitivity. Chapter 10 now warns against carrying a 2.45 GHz line model unchanged to 28 GHz and quantifies one RO4350B loss example.
- Added a specific RO4350B example: the Rogers 10 GHz Dk and loss figures, a first-order dielectric-loss estimate for the existing line geometry, the 8–40 GHz design-Dk range, moisture absorption, and the manufacturer's circuit/lifetime qualification caveat.
- Expanded Chapter 37's instrument limits with the NanoVNA V2 calibrated S11 noise floor and the tinySA Ultra's specified absolute-power and frequency-linearity limits. The text treats these as model-specific capability limits, not a universal uncertainty for all units.
- Kept Chapter 3's existing early ideal-versus-built notice and added one near the start of Chapter 21. The existing Figure 3.1 already compares ideal matches with a modeled ground-via effect; the Doherty and 30 dB fade examples already supply high-stakes numerical payoffs, so no unsupported measured curve or new duplicate example was invented.
- Replaced a vague promise about decades of GaN life with a device-specific Qorvo temperature example and a clear rule: RF drift is not a lifetime multiplier; use the part's junction-temperature and qualified life data. The book now distinguishes a representative measured slope from a universal coefficient.
- Kept Appendix B's existing Idea / Check / usual-mistake solution format and the established Key idea, From the Bench, and What You'll Actually Use structures. The chapter divisions and movement headings already break the long amplifier stretch.
- Regenerated the Book 4 tagged-text mirror from the REV4 master and updated the Book 4 score record. The revision sequence remains contiguous: REV1 was the initially reviewed manuscript; REV2 was the first fix pass; REV3 restored omitted Chapter 48 material; REV4 responds to the new review of REV3.

## Sources consulted

- Rogers Corporation, *RO4000 Series High Frequency Circuit Materials Data Sheet* (RO4350B), https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4000-laminates-ro4003c-and-ro4350b---data-sheet.pdf
- NanoRFE, *NanoVNA V2 User Manual*, https://nanorfe.org/nanovna-v2-user-manual.html
- tinySA, *TinySA4 Specification*, https://tinysa.org/wiki/pmwiki.php?n=TinySA4.Specification
- Qorvo, *GaN Power Amplifier Design Solutions*, representative 150 W GaN temperature-slope example.
- Analog Devices, AN-2591, *When It Comes to Long-Term Reliability of RF Amplifier ICs, Focus First on Die Junction Temperature*, https://www.analog.com/en/resources/app-notes/an-2591.html

## Review limits

REV4 has not received a new independent score or specialist RF review. The additions are source-backed examples and design checks, not a substitute for measurements on a built board. The complete 294-page DOCX was rendered and every page was visually reviewed; the new Appendix C source entries were checked again after removing their inherited page breaks.
