# Book 6 External Link Audit

**Audit date:** 13 October 2026  
**Scope:** HTTP(S) links in the current Book 6 tagged source mirror, including Appendix C. This is a reachability check, not claim-by-claim source validation.

## Results

All 14 current external-reference URLs in the Book 6 mirror opened successfully. The list covers the YHDC SCT-013-000 datasheet, two Espressif ESP32-S3/ADC sources, IEC 60664-1 and IEC 61010-1 catalogue records, Microchip AN1471, Infineon AN2025-10, the Strathclyde-hosted LCL-filter paper, UL Solutions' GFCI marking guide, three IET pages, OSHA electrical-safety training material, and the IPAC2016 primary paper on an IGBT thyratron-replacement project. Book 8's two HTTP URLs are XAML namespace identifiers, not reader-facing citations.

The previous Book 6 OSHA URL resolved to an older publication whose title did not match the cited title. The master now links directly to OSHA's Electrical safety training material, which identifies the Class A specification as 5 mA +/- 1 mA. Appendix C labels it training guidance, not a current regulation; UL 943 remains the applicable product-standard reference. The master and regenerated mirror now agree on this citation.

No dead external URL remains in the current Book 6 mirror. Reachability does not establish that each source supports every nearby statement, that a standard edition applies to a particular design, or that component specifications remain unchanged at publication.


Chapter 20 source follow-up (13 Oct 2026): added the IPAC2016 paper "Thyratron Replacement" as a primary source for the scoped accelerator-modulator case. Its proceedings PDF opened successfully. The current Book 6 mirror now has 14 reader-facing external URLs.
