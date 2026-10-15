# Book 6 Fuse Selectivity Review

**Date:** 13 October 2026  
**Scope:** Chapter 17.6, Worked Example 17.5, Appendix C source note, current DOCX master, extracted mirror, selected PDF pages, and current Kindle package.

## Finding and correction

Chapter 17 gave the 1.6:1 fuse rating rule without naming its applicable fuse category/standard and called the 125 A result "safe." ABB's application guidance specifies the total-selectivity rule for same-type gG fuses compliant with IEC 60269-2. The chapter now states those conditions and directs readers to confirm product/system limits. Worked Example 17.5 computes 1.6 x 63 A = 100.8 A, shows that 125 A is the first standard rating above it and that 100/63 = 1.587, and calls 125 A a rule-based candidate pending product and installation checks. It also explains why a 100 A breaker needs curve and manufacturer coordination data of its own. Appendix C now cites [ABB's fuse selectivity guide](https://new.abb.com/low-voltage/el/our-solutions/selectivity/focus-on/selectivity-with-fuses).

## Verification

- The DOCX package passes ZIP integrity and `python-docx` parsing.
- A fresh extraction matches all 51 current Book 6 text and figure outputs byte for byte.
- The 161-page LibreOffice PDF was rendered; pages 105 and 107 were visually inspected. Worked Example 17.6 now starts on a new page, keeping its ground-electrode/leakage answer together and avoiding a split calculation.
- Kindle Previewer reports Enhanced Typesetting Supported, Success, zero errors, and zero quality issues; its report says no issues found. The embedded `book.docx` SHA-256 matches the current master: `9f655b4885b198658ab69c85eab8374c04a5bfb903dec893b1f023f32f774c52`.

This is a wording and teaching-boundary correction, not a protective-device coordination study. An actual selection still needs the exact fuse/breaker products, manufacturer coordination data, voltage, available fault current, cable protection, and applicable local requirements. Independent power-systems review and site validation remain open; no readiness score is raised.
