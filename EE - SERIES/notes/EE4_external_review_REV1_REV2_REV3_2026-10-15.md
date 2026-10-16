# Book 4 external review and REV1–REV3 changes — 15 October 2026

## Starting point

The external reader scored the REV1 manuscript 7.4/10. Main concerns were a restrained but underused voice, stakes that sometimes stopped at the calculation, thin measurement-uncertainty and package/via treatment, the length of Parts I and II, and limited visual comparison of ideal and built behavior. The byte-identical REV1 source is retained under `bak/Book4/2026-10-15 pre-external-review/`.

## REV2 work completed

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

The material additions respond to the fixable items in the REV1 review. DOCX ZIP integrity, OOXML validation, chapter extraction, and figure/source-mirror consistency pass. LibreOffice headless conversion failed on this host with “Could not find platform independent libraries <prefix>” and produced no PDF, so the revised pagination has not had a visual render check. These changes do not substitute for an independent RF-specialist review, instrument validation on a physical board, a Kindle Previewer/device check, or a fresh full 14-criterion external review. Verify vendor specifications again at publication.


## REV3 content-gap audit — 15 October 2026

A comparison of REV2 against eleven earlier full-length Book 4 snapshots found one substantive omission: Chapter 48 sections 48.6–48.8 were present in the 11 October candidate/review snapshots but absent from REV2. No other chapter, section, worked example, practice item, or figure title was found missing across those snapshots; apparent text-only differences elsewhere were rewrites or updates. Chapter count and figures remain unchanged.

REV3 restores only those three sections, retaining REV2's current Chapter 48 text and its parser-scope qualification. The restored material covers (1) the relationship among S, Y, and H two-port parameters and conversions, (2) mixing measured linear networks with nonlinear compact transistor models in simulators that support both, and (3) noise-parameter fitting from tuner sweeps, including equations, source-impedance coverage, repeatability, reference-plane control, and limitations. The Chapter 48 takeaway now summarizes these additions, and Appendix C cites Lane's original noise-parameter paper.

Validation: REV3 opens as DOCX; ZIP integrity passes; the Chapter 48 and back-matter tagged mirrors match a fresh extraction exactly. LibreOffice rendered the complete 300-page document. All page thumbnails were reviewed as contact sheets, and pages 226–228 containing Figure 48.1 and the restored material were inspected at full resolution; no clipping, overlap, or section-break defect was found. This was a content-gap repair, not a fresh external score or RF-specialist review.


## Canonical revision numbering

To make the external-review sequence contiguous, filenames have been renumbered: the externally reviewed manuscript formerly named REV5 is REV1; its first revision, formerly REV6, is REV2; and the content-gap correction, formerly REV7, is REV3. Git history preserves the previous filenames.
