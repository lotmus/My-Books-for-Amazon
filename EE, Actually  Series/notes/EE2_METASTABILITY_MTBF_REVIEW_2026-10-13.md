# Book 2 Metastability MTBF Review

**Date:** 13 October 2026  
**Scope:** Chapter 28.3's common-misconception paragraph in the current DOCX master, its tagged mirror, and selected rendered page.

## Finding and correction

The previous wording said that a design with a 40-minute synchronizer MTBF would fail only occasionally in testing. That reverses the practical interpretation: with a constant failure rate and an exponential time-to-first-failure model, the chance of at least one failure in a one-hour test is `1 - exp(-60/40) = 0.7769`, or about 77.7%. The master now states this probability, makes the model assumptions explicit, and explains that short runs can miss a fault while longer runs can reveal it. It also retains the needed engineering action: use worst-case device parameters and add synchronizer stages to meet the product reliability target.

## Verification

The Book 2 DOCX package passes ZIP integrity and python-docx parsing. The tagged mirror contains the corrected text. A fresh extraction comparison matched all 89 current Book 2 mirror text and figure files. A current 183-page PDF was rendered, and page 144 was visually inspected; the paragraph remains legible and fits with the surrounding Chapter 28 material.

The probability is a reliability-model illustration, not an empirical prediction for every synchronizer: actual failure rate depends on device-specific metastability parameters, clock/data rates, resolution time, voltage, and temperature. No score increase is assigned from this local correction. Product-level MTBF still requires device data and worst-case analysis.
