# Book 4 external review and REV6 changes — 15 October 2026

## Starting point

The external reader scored the REV5 manuscript 7.4/10. Main concerns were a restrained but underused voice, stakes that sometimes stopped at the calculation, thin measurement-uncertainty and package/via treatment, the length of Parts I and II, and limited visual comparison of ideal and built behavior. The byte-identical REV5 source is retained under `bak/Book4/2026-10-15 pre-external-review/`.

## REV6 work completed

- Kept the established understated openings while adding consequences where failure reaches the hardware or link: bypass-capacitor operation above SRF, a bad match stressing a PA or triggering transmitter power reduction, a link falling below sensitivity, and compression creating adjacent-channel energy when DPD is absent.
- Added early ideal-versus-built notices in the lumped-match, distributed-match, and filter chapters, with pointers to later package/via and layout material.
- Added model-specific measurement limits for NanoVNA V2 and tinySA Ultra, and clarified that noise floor, instrument model, calibration plane, and repeatability limit confidence in a result.
- Quantified an example 1.6 mm through-via at about 0.75 nH (about 11.5 Ω at 2.45 GHz) and one LFCSP package extraction at about 0.42–0.49 nH; both are geometry-specific examples, not universal constants. Added RO4350B dielectric/temperature and ceramic timing-resonator drift examples, explicitly distinguishing timing resonators from microwave dielectric pucks.
- Added a 30 dB fade case to the link-budget example and the resulting mode fallback or packet loss.
- Added internal movement headings in the unusually long Parts I and II. The existing 915 MHz / 20 mm Chu-limit example already gave a numerical bandwidth limit; it was retained and not needlessly duplicated.
- Reworked Figure 3.1 to place the ideal L and pi matches beside a modeled L-match with a 0.75 nH series ground via. The caption and image description label the via value as illustrative and geometry-dependent.
- Added source links in Appendix C and retained Appendix B's full Idea / Check / usual-mistake solution structure.

## Sources for new technical values

- Rogers, [RO4000 Series data sheet](https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4000-laminates-ro4003c-and-ro4350b---data-sheet.pdf).
- Analog Devices, [Power Supply and Ground Design for a WiFi Transceiver](https://www.analog.com/en/resources/technical-articles/power-supply-and-ground-design-for-a-wifi-transceiver.html); [AN-772 package extraction](https://www.analog.com/en/resources/app-notes/an-772.html).
- [NanoVNA V2 manual](https://www.nanorfe.com/nanovna-v2-user-manual.html); [tinySA Ultra specifications](https://tinysa.org/wiki/pmwiki.php?n=TinySA4.Specification).
- Murata, [CERALOCK temperature characteristics](https://www.murata.com/en-global/products/timingdevice/ceralock/overview/basic/summary).

## Review limits / next checks

The material additions respond to the fixable items in the REV5 review. DOCX ZIP integrity, OOXML validation, chapter extraction, and figure/source-mirror consistency pass. LibreOffice headless conversion failed on this host with “Could not find platform independent libraries <prefix>” and produced no PDF, so the revised pagination has not had a visual render check. These changes do not substitute for an independent RF-specialist review, instrument validation on a physical board, a Kindle Previewer/device check, or a fresh full 14-criterion external review. Verify vendor specifications again at publication.
