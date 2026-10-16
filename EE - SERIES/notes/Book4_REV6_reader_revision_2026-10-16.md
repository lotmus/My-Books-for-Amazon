# Book 4 REV6 revision record — 16 October 2026

REV6 starts from REV5. REV1–REV5 remain unchanged.

## Substantive changes

- Rewrote the openings of Chapters 3, 8, 11, 17, 20, 21, 23, and 30 around concrete field failures and their mechanisms.
- Divided Part II into three movements: Chapters 20–27 build the radio chain; 28–34 cover field behavior and system blocks; 35–41 design and verify the transmitter. The movement map appears in both the reading guide and contents, and the page dividers stay with the first chapter of each movement.
- Marked Chapters 21 and 23 with a dagger in the contents and added field cases. Chapter 21 calculates hot-case junction temperature from declared assumptions (100 W RF, 60% drain efficiency, 1.5 °C/W junction-to-ambient, and a selected 150 °C design ceiling); the text explicitly says these are illustrative, not universal device ratings. Chapter 23 replaces its routine Worked Example 23.2 with the numerical NR 256QAM EVM pass/fail case: 4.0% exceeds the cited 3.5% test limit by 0.5 percentage point.
- Added cross-volume consequence sentences to the existing bench notes in Chapters 3, 5, 7, 18, 21, 23, 30, and 37. These tie matching, antenna, environmental, waveform, link-budget, and measurement outcomes to Books 5, 7, and 9.
- Varied selected Key idea, From the Bench, On the Job, and What You’ll Actually Use passages to make the practical guidance less mechanically uniform.
- Kept Appendix B answers unchanged; the prior audit found all 319 preserve the Idea / Check / usual mistake pattern.

## Sources

- Rogers RO4000 Series materials data sheet: https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4000-laminates-ro4003c-and-ro4350b---data-sheet.pdf
- KEMET C1100 SMD MLCC data sheet: https://content.kemet.com/datasheets/KEM_C1100_CAS_SMD.pdf
- KEMET F3113 ceramic capacitor characteristics: https://content.kemet.com/datasheets/F3113_Mil_CE_High_Rel.pdf
- Keysight FieldFox handheld analyzers data sheet: https://www.keysight.com/zz/en/assets/3123-1696/data-sheets/FieldFox-Handheld-Analyzers.pdf
- ETSI, 3GPP TS 38.104 V18.9.0, NR base-station transmission and reception: https://www.etsi.org/deliver/etsi_ts/138100_138199/138104/18.09.00_60/ts_138104v180900p.pdf

Cross-referenced Book 3, 5, 6, and 7 chapter titles were checked against the latest outlines available during this revision.

## Verification and limits

The REV6 DOCX opened and passed ZIP integrity validation. LibreOffice rendered it to a 294-page PDF; every page was rendered to an image and reviewed in contact sheets, with the new field cases, contents, movement breaks, and revised examples also inspected at full size.

The thermal case is an explicitly assumed design scenario, not a universal lifetime or temperature rule. Analyzer uncertainty is configuration-dependent; use the exact instrument, antenna/cable setup, calibration state, and applicable certification procedure. The EVM threshold is tied to the cited TS 38.104 revision; confirm the applicable release and test conditions before certification.


## Repository integration

The delivered 294-page REV6 is preserved as RF_Microwave_and_Transceivers_Book4_REV6_reader_revision.docx. The main branch already contained a different 295-page REV6 from a separate review pass. This commit adds the delivered manuscript under a distinct filename and preserves that existing REV6 and its chapter mirror. The reader revision starts from the delivery-folder REV5; it does not supersede or incorporate every change in the other REV6. These two variants require editorial reconciliation before selecting an upload master. Only Book 4's manuscript and this revision record are included in this integration.
