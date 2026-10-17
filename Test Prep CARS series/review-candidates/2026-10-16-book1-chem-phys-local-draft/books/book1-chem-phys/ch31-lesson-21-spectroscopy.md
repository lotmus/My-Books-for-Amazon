# Lesson 21: Spectroscopy

**What you will be able to do**

- Use infrared (IR) spectra to identify functional groups.
- Use ultraviolet-visible (UV-vis) absorption, color and the Beer-Lambert law.
- Interpret proton NMR spectra: number of signals, chemical shift, integration and splitting.
- Read a mass spectrum for molecular mass and the isotope patterns of chlorine and bromine.
- Combine several kinds of data to identify an unknown compound.

**Why it matters for the exam**

Spectroscopy is how chemists, and the physicians who read their results, see molecules. An MRI scan is NMR; a pulse oximeter is absorption spectroscopy; a clinical lab identifies drugs with mass spectrometry. Categories 4D and 5C list the "molecular structure and absorption spectra" as topics because they combine physics (light interacting with matter, [Lesson 7](chapter:14)) with organic chemistry. Questions usually give you a formula and one or two spectral clues and ask which structure fits. The task is detective work, and the clues are few and very reliable.

Praxis Tip: Always compute the degrees of unsaturation (rings plus π bonds) from the molecular formula first. A formula that implies a C=O or an aromatic ring tells you what to look for in the spectrum.

**Concept Review**

**Light and molecules.** A molecule absorbs a photon when the photon's energy matches a gap between two energy states of the molecule. Different energy gaps mean different regions of the spectrum: radio waves (NMR), infrared (vibrations), visible and ultraviolet (electronic transitions).

**Degrees of unsaturation.** For a formula CₓHᵧNzOw (ignoring halogens, treating each as H), the number of degrees of unsaturation is

    DoU = (2x + 2 + z − y) / 2

Each ring or π bond counts as one. A DoU of 4 or more suggests a benzene ring. A C=O counts as one.

**Infrared (IR) spectroscopy.** IR absorption corresponds to **vibrations** of bonds. The spectrum plots % transmittance against **wavenumber** (cm⁻¹); an absorption is a downward dip. Group frequencies to know:

| Bond | Wavenumber (cm⁻¹) | Appearance |
|---|---|---|
| O–H (alcohol, phenol) | about 3200–3600 | Broad, strong |
| O–H (carboxylic acid) | about 2500–3300 | Very broad, overlapping the C–H region |
| N–H (amine, amide) | about 3300–3500 | Medium; one band for 2° and two for 1° amines |
| C–H (sp³) | about 2850–3000 | Medium to strong |
| C–H of aldehyde | about 2720 and 2820 | Two weak bands |
| C≡N, C≡C | about 2100–2260 | Medium to weak, sharp |
| C=O | about 1670–1780 | **Very strong, sharp** |
| C=C | about 1620–1680 | Weak to medium |

The region below about 1500 cm⁻¹ is the **fingerprint region**, complex and unique to each molecule; it is used for matching but rarely for assigning individual bonds. The C=O stretch is the most useful single peak: its position varies a little with the type of carbonyl (ketones about 1715, aldehydes about 1725, esters about 1735 to 1750, acids about 1710, amides about 1650 to 1690). Treat all of these ranges as approximate; exact values shift with the molecule's environment.

Praxis Tip: Do three scans: the broad O–H region (above 3200), the sharp strong C=O peak (near 1700), and the C–H region (just below and above 3000). Those three answer most IR questions.

**Ultraviolet-visible (UV-vis) spectroscopy.** UV-vis absorption corresponds to the promotion of electrons to higher orbitals, mainly π → π* transitions in double bonds and n → π* transitions in groups with lone pairs, such as C=O. The more extended the conjugation (alternating double bonds), the smaller the energy gap and the **longer the wavelength** of maximum absorption (λ_max). Extended conjugated systems, such as β-carotene (the orange pigment in carrots), absorb in the visible region.

The **color** you see is the **complementary color** of the light absorbed: a compound that absorbs blue light (about 450 nm) looks yellow-orange. Indicators change color when a structural change (protonation or deprotonation) alters the conjugated system ([Lesson 16](chapter:25)).

The **Beer-Lambert law** relates absorbance to concentration:

    A = ε b c

where ε is the molar absorptivity (M⁻¹ cm⁻¹), b the path length (cm), and c the concentration (M). Absorbance is proportional to concentration, which is the basis for measuring the amount of a colored substance in blood or a protein solution.

**Proton NMR (¹H NMR).** Nuclei with spin, such as ¹H, behave as tiny magnets. In a strong magnetic field, they absorb radio-frequency radiation at a frequency that depends on their electronic environment. A ¹H NMR spectrum gives four kinds of information:

1. **Number of signals:** the number of sets of **chemically equivalent** hydrogens. Hydrogens that can be interchanged by symmetry are equivalent.
2. **Chemical shift (δ, in ppm):** where the signal appears. Hydrogens near electronegative atoms or π systems are **deshielded** and appear further downfield (larger δ).
3. **Integration:** the area under a signal is proportional to the number of hydrogens it represents.
4. **Splitting (multiplicity):** a signal is split by hydrogens on neighboring carbons according to the **n + 1 rule**: n equivalent neighbors give n + 1 lines. (Singlet 0 neighbors, doublet 1, triplet 2, quartet 3, quintet 4, septet 6.)

Typical chemical shifts (ppm): alkyl C–H about 0.9–1.5; C–H next to a C=O or on an allylic carbon about 2–2.5; C–H next to an oxygen (alcohol, ether, ester O–CH) about 3.3–4.5; alkene C–H about 4.5–6.5; aromatic C–H about 6.5–8; aldehyde H about 9–10; carboxylic acid O–H about 10–12; O–H and N–H signals are variable and often broad. Treat these ranges as approximate.

Praxis Tip: Build the structure from fragments. Use the splitting to find neighbors (a triplet next to a quartet is an ethyl group) and the integration to count hydrogens in each fragment.

**Mass spectrometry.** In a mass spectrometer ([Lesson 8](chapter:15)) a molecule is ionized and the mass-to-charge ratio (m/z) of the ion and its fragments is recorded. The **molecular ion peak (M⁺)** gives the molecular mass. Fragment peaks show how the molecule breaks. The **base peak** is the most intense peak. Halogens leave a signature: chlorine has two isotopes (³⁵Cl and ³⁷Cl, about 3 : 1), so a compound with one Cl shows peaks at M and M + 2 in a **3 : 1** ratio. Bromine (⁷⁹Br and ⁸¹Br, about 1 : 1) gives M and M + 2 in a **1 : 1** ratio.

**Worked Example 1: IR clues (skill: three scans)**

A compound has the formula C₃H₆O and its IR spectrum shows a strong sharp peak at 1715 cm⁻¹ and no broad band near 3300 cm⁻¹ and no peaks near 2720 cm⁻¹. Which functional group is present?

DoU = (2×3 + 2 − 6)/2 = 1, so one ring or π bond. The strong peak at 1715 cm⁻¹ indicates C=O (using up the unsaturation). No broad O–H band rules out an alcohol or acid; no 2720 cm⁻¹ band rules out an aldehyde. So it is a **ketone**: acetone (CH₃COCH₃).

**Worked Example 2: Building a structure from NMR (skill: fragments)**

A compound C₄H₈O₂ shows: δ 1.2 (triplet, 3H), δ 2.0 (singlet, 3H), δ 4.1 (quartet, 2H); the IR has a strong peak at 1740 cm⁻¹. Identify it.

DoU = (8 + 2 − 8)/2 = 1: one C=O (IR 1740 cm⁻¹, an ester). The triplet (3H) and quartet (2H) together are an ethyl group, CH₃CH₂–; the quartet at 4.1 ppm means the CH₂ is attached to an oxygen. The singlet at 2.0 ppm (3H) is a CH₃ with no neighbors and next to a carbonyl. Fragments: CH₃C(=O)–O–CH₂CH₃, **ethyl acetate**.

**Worked Example 3: Splitting and equivalence (skill: counting signals)**

(a) How many ¹H NMR signals do toluene and p-xylene give? (b) What does an isopropyl group, –CH(CH₃)₂, look like?

(a) Toluene (methylbenzene): CH₃ (1 signal), and the aromatic hydrogens fall into three sets (ortho, meta, para): **4 signals**. p-Xylene (1,4-dimethylbenzene) is symmetric: one set of equivalent CH₃ hydrogens and one set of equivalent aromatic hydrogens: **2 signals**, with integration 6 : 4 = 3 : 2.

(b) The two CH₃ groups are equivalent and each has one neighbor (the CH): a **doublet** integrating for 6H. The CH has six equivalent neighbors: a **septet** integrating for 1H.

**Worked Example 4: Beer's law and color (skill: absorbance)**

(a) A dye has ε = 1.2 × 10⁴ M⁻¹ cm⁻¹. In a 1.0 cm cell at a concentration of 5.0 × 10⁻⁵ M, what is the absorbance? (b) If the concentration doubles, what happens? (c) A solution absorbs strongly near 450 nm (blue). What color does it appear?

(a) A = ε b c = 1.2 × 10⁴ × 1.0 × 5.0 × 10⁻⁵ = 0.60. (b) Absorbance doubles, to 1.2. (c) A solution that absorbs blue light transmits the rest and appears yellow-orange, the complementary color.

**Worked Example 5: Mass spectra and halogens (skill: isotope patterns)**

Bromomethane (CH₃Br) and chloromethane (CH₃Cl) are analyzed. What molecular ion peaks are expected?

CH₃Br: the mass with ⁷⁹Br is 12 + 3 + 79 = 94, and with ⁸¹Br it is 96; the two peaks are about equal in intensity (**1 : 1**). CH₃Cl: masses 50 (³⁵Cl) and 52 (³⁷Cl) in a ratio of about **3 : 1**.

**More Praxis Tips**

Praxis Tip: In NMR, ignore the O–H and N–H signals when you count the splitting of neighbors: they usually do not couple to adjacent hydrogens because of rapid exchange.

Praxis Tip: To count equivalent hydrogens, look for symmetry: a mirror plane or rotation that swaps two hydrogens makes them equivalent.

Praxis Tip: For IR, remember that a strong peak is more informative than a weak one. The C=O stretch is strong; the C=C stretch is often weak.

Praxis Tip: When a UV-vis question asks which compound absorbs at the longest wavelength, pick the one with the most extensive conjugation.

Praxis Tip: For mass spectra, the highest-mass peak that is not part of an isotope pattern is the molecular ion. The M + 2 peak is the telltale for Cl and Br.

**Common Mistakes**

- Counting every hydrogen as a separate NMR signal instead of grouping by equivalence.
- Applying the n + 1 rule to the neighbors' environment instead of the number of adjacent hydrogens.
- Confusing wavenumber with wavelength (higher wavenumber means higher energy and shorter wavelength).
- Reading the color absorbed as the color seen.
- Forgetting the 3 : 1 and 1 : 1 isotope patterns.
- Assigning O–H and C=O peaks without using the sharpness and breadth of the bands.

**Checkpoint Questions**

1. A compound's IR spectrum has a broad, strong absorption near 3300 cm⁻¹ and no strong absorption near 1700 cm⁻¹. The compound most likely contains
   A. a ketone C=O group
   B. an alcohol O–H group
   C. a carbon-carbon triple bond
   D. an ester

2. How many signals would 2-propanol, (CH₃)₂CHOH, show in its ¹H NMR spectrum?
   A. 1
   B. 2
   C. 8
   D. 3

3. In a ¹H NMR spectrum, the hydrogens of a CH₃ group whose only neighboring carbon is a CH₂ group appear as a
   A. singlet
   B. doublet
   C. triplet
   D. quartet

4. In a Beer-Lambert experiment, the concentration of an absorbing solution is doubled while the path length is unchanged. The absorbance
   A. doubles
   B. is halved
   C. is unchanged
   D. is multiplied by four

5. A mass spectrum shows two molecular ion peaks of nearly equal intensity at m/z values that differ by 2. The compound probably contains
   A. one chlorine atom
   B. one fluorine atom
   C. one iodine atom
   D. one bromine atom

6. A compound shows a very strong, sharp IR absorption at 1715 cm⁻¹. This indicates the presence of
   A. a hydroxyl (O–H) group
   B. a carbon-carbon double bond
   C. a carbonyl (C=O) group
   D. an amine (N–H) group

7. Which change in a molecule would shift its UV-visible absorption maximum to a longer wavelength?
   A. Breaking the conjugated system
   B. Extending the conjugated system
   C. Replacing double bonds with single bonds
   D. Cooling the sample

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **B.** A broad band near 3200–3600 cm⁻¹ is characteristic of the O–H stretch of an alcohol; the absence of a C=O band rules out acids, esters and ketones. (A would show a strong sharp band near 1715 cm⁻¹; C would show a weak sharp band near 2100–2260 cm⁻¹; D would show a strong sharp C=O band near 1740 cm⁻¹.)
2. **D.** There are three sets: the six equivalent CH₃ hydrogens, the single CH hydrogen, and the O–H hydrogen. (A treats all hydrogens as equivalent; B ignores the O–H hydrogen; C counts every hydrogen individually.)
3. **C.** By the n + 1 rule, two equivalent neighboring hydrogens split the signal into 2 + 1 = 3 lines (a triplet). (A would require no adjacent hydrogens; B would require one adjacent hydrogen; D would require three adjacent hydrogens.)
4. **A.** A = ε b c, so absorbance is directly proportional to concentration. (B reverses the dependence; C ignores Beer's law; D squares the dependence.)
5. **D.** The two isotopes of bromine (⁷⁹Br and ⁸¹Br) occur in about a 1 : 1 ratio, giving M and M + 2 peaks of equal height. (A would give peaks in a 3 : 1 ratio; B fluorine has only one stable isotope; C iodine has only one stable isotope.)
6. **C.** A strong sharp band near 1700 cm⁻¹ is the signature of the C=O stretch. (A gives a broad band near 3300 cm⁻¹; B gives a weaker band near 1650 cm⁻¹; D gives bands near 3300–3500 cm⁻¹.)
7. **B.** More extensive conjugation lowers the energy gap between orbitals, so the molecule absorbs lower-energy, longer-wavelength light. (A raises the energy gap and shortens the wavelength; C removes the π system that absorbs; D does not change the electronic energy gap significantly.)

Praxis Tip: After the checkpoint questions, look at each wrong choice and name the slip (wrong IR region, miscounted equivalent hydrogens, splitting rule misapplied, complementary color). Log it in your error log ([Strategy: The Question Method](chapter:4)).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "Infrared shows functional groups, with a broad band near 3300 for O–H and a strong sharp band near 1700 for C=O; ultraviolet-visible absorption moves to longer wavelengths as conjugation grows and Beer's law makes absorbance proportional to concentration; proton NMR gives the number of equivalent hydrogen sets, their shifts, their integrations and, by the n plus 1 rule, their neighbors; and mass spectrometry gives the molecular mass, with M and M plus 2 peaks at 3 to 1 for chlorine and 1 to 1 for bromine."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 2 and 3 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set that includes [Lesson 20](chapter:30) carboxylic acid derivatives and [Lesson 7](chapter:14) light), and after 21 days (explain the lesson aloud).

*Interleave:* alternate a spectroscopy problem with a carbonyl problem and an optics problem. [Lesson 22](chapter:32) turns to how compounds are separated before they are analyzed.

Praxis Tip: End each study session by writing, from memory, the degrees-of-unsaturation formula, the main IR bands, the n + 1 rule, and the isotope patterns of Cl and Br.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Verified: DoU values; Beer's law A = 0.60; CH₃Br peaks at m/z 94 and 96 and CH₃Cl at 50 and 52; NMR assignment of ethyl acetate.
- Answer key positions: B, D, C, A, D, C, B.
- Checked: IR ranges and NMR chemical-shift ranges against the fact sheet; the exam usually supplies tables if needed, so quote them as approximate.
- Category 4D and 5C topics covered: molecular structure and absorption spectra (infrared, visible, ultraviolet, NMR), mass spectroscopy. Mass spectrometer physics is in Lesson 8.
