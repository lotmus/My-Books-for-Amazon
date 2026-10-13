# Book 3 Technical Review Follow-up (13 Oct 2026)

## Finding and correction

Chapter 26.2 and the Chapter 18 worked solution described efficiency droop in InGaN LEDs as mostly caused by Auger recombination. That wording turns one supported mechanism into a general explanation across devices. Replaced it in both locations: Auger recombination is an observed/contributing mechanism and has an n^3 term in the simple ABC rate model, while carrier leakage, current crowding, localization, and heating may also contribute; their relative importance depends on device structure and operating conditions. The simple model is described as a model, not proof that Auger dominates each LED.

Chapter 26.5 said conventional fluorescent OLED emitters waste the triplet population. Rewrote the paragraph to distinguish phosphorescence from conventional fluorescence and thermally activated delayed fluorescence (TADF), which can recover triplets through reverse intersystem crossing. The blue-emitter difficulty is now expressed as an efficiency/lifetime challenge associated with high-energy excited states, not a universal shortest-lifetime ranking.

## Evidence

- Iveland et al. directly detected Auger electrons in an electrically driven InGaN/GaN LED: [Physical Review Letters 110, 177406 (2013)](https://doi.org/10.1103/PhysRevLett.110.177406).
- A primary study showed that both an Auger fit and a carrier-spillover model could describe measured InGaN blue-LED droop, illustrating why a blanket causal statement is too strong: [Superlattices and Microstructures 47 (2010), 118-122](https://doi.org/10.1016/j.spmi.2009.07.022).
- Uoyama et al. demonstrated efficient delayed-fluorescence OLEDs using singlet and triplet excitons: [Nature 492 (2012), 234-238](https://doi.org/10.1038/nature11687).

## Verification and limits

Updated the authoritative Book 3 DOCX and regenerated the tagged mirror. All 64 mirror files match a fresh extraction byte-for-byte; the DOCX passes ZIP integrity and python-docx parsing. Rendered the current DOCX to a 204-page PDF and visually checked pages 104 (LED worked example) and 155-156 and 159 (Chapter 26 LED and display material); the edited prose is legible and its page break is clean. No numerical result changed. No Book 3 score increase is claimed; broader semiconductor-specialist peer review and device-specific validation remain outside this text edit. The Book 3 KPF built before this master edit is stale and needs regeneration before release.


## Package freshness correction (13 October 2026)

The preceding note that the Book 3 KPF was stale was accurate when written but is superseded. The current package embeds the exact master SHA-256 `44b7da0860e9efddf849baefccc29cb311b548186c0d3c0888b1edc05da975bc`; Previewer reports Supported/Success, zero errors and quality issues, and “No issues found.” This closes package freshness and automated conversion for the current DOCX, not full-device visual QA, semiconductor-specialist peer review, or device validation.
