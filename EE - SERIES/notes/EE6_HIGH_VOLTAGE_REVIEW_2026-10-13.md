# Book 6 High-Voltage Insulation Review

**Date:** 13 October 2026  
**Files:** `Power_and_Energy_Book6.docx`, `chapters/Book6/src/ch08.txt`, and `chapters/Book6/src/back.txt`.

## Finding and correction

Chapter 8.6 gave a 5 mm creepage example for “a common board material” and made clearance sound as though the same inputs determine it. This left the material assumption ambiguous and blurred the distinction between air clearance and surface creepage.

The master and tagged mirror now state that creepage is selected from steady-state working voltage, pollution degree, and CTI-derived material group, while clearance is selected separately from rated impulse voltage, overvoltage category, field conditions, and altitude. The 5 mm illustration is explicitly tied to IEC 60664-1:2020+AMD1:2025 Table F.5, 1000 V RMS, pollution degree 2, and the printed-wiring-material column excluding material group IIIb. Reinforced insulation is stated as 10 mm. The text says this example does not establish clearance or qualify a PCB, and requires applicable product-standard review, material verification, and compliant slot geometry.

Appendix C now cites the consolidated editions: IEC 60664-1:2020+AMD1:2025 CSV and IEC 61010-1:2010+AMD1:2016 CSV, with official IEC catalogue links. IEC identifies the former as valid Edition 3.1, published 6 May 2025; its scope includes equipment rated up to 1,000 V AC or 1,500 V DC, and its 2025 changes include an updated altitude-correction table. IEC identifies the latter as the consolidated general safety requirements for measurement, control, and laboratory equipment.

## Verification and remaining limits

The current Book 6 DOCX opens in Word; the revised Chapter 8.6 and Appendix C wording was read back from the saved master and compared with the tagged-text mirror. The DOCX document XML parses. This check did not render pages or validate a real PCB design. The 5 mm value is a standards illustration, not a general layout recommendation; product-specific and installation-specific review remains necessary.

Sources: [IEC 60664-1:2020+AMD1:2025 CSV](https://webstore.iec.ch/en/publication/107319); [IEC 61010-1:2010+AMD1:2016 CSV](https://webstore.iec.ch/en/publication/59769).

## Residual-current protection wording follow-up (13 October 2026)

Chapter 17.7 previously said 30 mA RCDs and 4-6 mA North American GFCIs were fast enough to prevent ventricular fibrillation. That wording overstated a risk-reduction device as a guaranteed outcome. The master now identifies 30 mA RCDs as additional protection and Class A GFCI operating current as 4-6 mA, states that these devices reduce risk but do not make contact safe or guarantee injury prevention, and names current path, duration, protective earthing/bonding, and correct device selection. Appendix C now points to the IET guidance on current-duration effects and RCD additional protection, plus OSHA GFCI guidance. The regenerated Book 6 mirror and saved master were checked for the updated wording. This editorial source check does not constitute installation design advice or independent electrical-safety review.

A second sentence in 17.7 now says an RCD operates when residual imbalance reaches its operating threshold, rather than only after it exceeds the marked rating. This agrees with the chapter's answer-key note that devices may trip below IΔn and with IET's discussion of actual trip behavior.

Threshold detail: for North American Class A GFCIs, the final text states the UL 943 boundary precisely: the device must trip at or before 6 mA and must not trip below 4 mA. Appendix C now cites UL Solutions' current marking/application guide in addition to OSHA material.


## OSHA source precision follow-up (13 Oct 2026)

Replaced the misidentified OSHA publication link in Appendix C with OSHA's Electrical safety training material, specifically its section "Classes of Ground-Fault Circuit-Interrupters." It gives a Class A specification of 5 mA +/- 1 mA. The book labels this as training guidance, not a current regulation, and retains UL 943 as the product-standard reference for the Class A boundary. The current master and regenerated mirror contain the corrected citation. This source correction does not alter the Chapter 17 safety score or replace an independent electrical-safety review.
