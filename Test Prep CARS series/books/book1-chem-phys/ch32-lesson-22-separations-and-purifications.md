# Lesson 22: Separations and Purifications

**What you will be able to do**

- Explain how extraction, distillation and chromatography separate mixtures, and which property each exploits.
- Design an acid-base extraction to separate an acid, a base and a neutral compound.
- Calculate partition coefficients and compare one large extraction with several small ones.
- Interpret thin-layer chromatography (Rf values) and the elution order in column chromatography.
- Explain how electrophoresis and size-exclusion, ion-exchange and affinity chromatography separate proteins.

**Why it matters for the exam**

Category 5C is all about separating and purifying compounds, because you cannot study what you cannot isolate. Real research passages are full of these methods: a protein purified on a column, a drug measured by HPLC, a DNA fragment sized on a gel. The exam asks you to say what each technique separates on (size, charge, polarity, boiling point, affinity) and what comes out first. Once you have the property, the answer follows. This is a lesson where the vocabulary matters almost as much as the logic.

Praxis Tip: For any separation question, ask "what property differs between these molecules?" and "which technique is built to exploit that property?" The two answers usually give the choice.

**Concept Review**

**Extraction.** Extraction separates compounds by their relative solubility in two **immiscible** solvents, typically water and an organic solvent such as diethyl ether, which are shaken together in a separatory funnel. The more soluble a compound is in a solvent, the more of it goes there. The ratio of the concentrations at equilibrium is the **partition coefficient**:

    K = [solute]_organic / [solute]_aqueous

**Many small extractions beat one large one.** With the same total volume of organic solvent, extracting several times with smaller portions removes more solute than one extraction.

**Acid-base extraction.** Changing the charge of a molecule changes its solubility: ions dissolve in water, neutral organic molecules dissolve in organic solvents. This allows an organic mixture to be separated by washing with aqueous acid or base.

- A **carboxylic acid** is converted to its water-soluble carboxylate by aqueous base (NaHCO₃ or NaOH). Acidifying that aqueous layer later regenerates the neutral acid.
- An **amine** (a base) is converted to its water-soluble ammonium salt by aqueous acid (HCl). Making that aqueous layer basic regenerates the neutral amine.
- A **neutral compound** stays in the organic layer throughout.

Praxis Tip: Use the rule "ionic goes to water, neutral stays in the organic layer." Then ask which reagent turns each compound into its ionic form.

**Distillation.** Distillation separates liquids by differences in **boiling point**. The mixture is heated, the more volatile component vaporizes first, and the vapor is condensed and collected.

- **Simple distillation** works when the boiling points differ by a large amount (a common rule of thumb is more than about 25 °C, and the larger the gap, the cleaner the split).
- **Fractional distillation** uses a column that provides many repeated vaporization-condensation cycles, separating liquids with closer boiling points.
- **Vacuum distillation** lowers the pressure so that liquids boil at lower temperatures, protecting heat-sensitive or high-boiling compounds.
- Some mixtures form **azeotropes**, mixtures with constant boiling composition that cannot be separated by simple distillation.

**Chromatography: the general idea.** In chromatography, a mixture is carried by a **mobile phase** (liquid or gas) over a **stationary phase** (a solid or a coated solid). Components that interact strongly with the stationary phase move slowly; those that interact weakly move quickly, and so the components separate.

- **Thin-layer chromatography (TLC)** and **paper chromatography** use a flat plate or paper as the stationary phase; the solvent climbs by capillary action. The **retention factor** (Rf) of a compound is the distance it traveled divided by the distance the solvent front traveled, a value between 0 and 1. On silica, more polar compounds have *lower* Rf.
- **Column chromatography** packs a column with the stationary phase and passes the mixture through it. On a polar column, less polar compounds elute first.
- **Gas chromatography (GC, gas-liquid)** vaporizes the sample and carries it with an inert gas through a column; compounds separate by volatility and interaction with the column. A detector records the **retention time** and the peak area (proportional to the amount).
- **High-pressure (performance) liquid chromatography (HPLC)** forces a liquid through a column under high pressure, giving fast, high-resolution separations; **reverse-phase HPLC** uses a nonpolar stationary phase, so *polar* compounds elute first.

**Protein separation methods.**

| Method | Separates by | Order or behavior |
|---|---|---|
| **Size-exclusion (gel filtration) chromatography** | Size | The column beads have pores. Large molecules cannot enter and travel only between beads, so they elute **first**; small molecules enter the pores, take a longer path and elute **later**. |
| **Ion-exchange chromatography** | Charge | A cation-exchange resin (negatively charged) binds positively charged proteins; an anion-exchange resin (positively charged) binds negatively charged ones. Bound proteins are released by raising the salt concentration or changing the pH. |
| **Affinity chromatography** | Specific binding | A ligand attached to the resin (an antibody, a substrate analog, a tag such as polyhistidine) binds the protein of interest; everything else washes through, and the target is eluted by adding free ligand or changing conditions. |
| **Gel electrophoresis** | Size and/or charge | An electric field moves charged molecules through a gel. |

**Electrophoresis.** In gel electrophoresis, molecules migrate toward the electrode of opposite charge through a porous gel (agarose for DNA, polyacrylamide for proteins).

- **DNA** is negatively charged (its phosphate backbone), so it migrates toward the positive electrode; shorter fragments move **farther** because they pass through the pores more easily.
- **SDS-PAGE** coats proteins with the detergent SDS, which unfolds them and gives them a uniform negative charge per unit mass, so they separate by **mass** alone, with smaller proteins moving farther.
- **Native PAGE** keeps proteins folded and separates by size, shape and charge.
- **Isoelectric focusing** separates proteins in a pH gradient: each protein migrates until it reaches the pH equal to its **isoelectric point (pI)**, where its net charge is zero, and stops.

**Resolving enantiomers.** Enantiomers have identical physical properties and cannot be separated by ordinary distillation, extraction or achiral chromatography ([Lesson 18](chapter:28)). To separate a **racemic mixture**, react it with a single pure enantiomer of another chiral compound (a **resolving agent**). This converts the pair of enantiomers into a pair of **diastereomers**, which have different physical properties and can be separated (for example by crystallization). The resolving agent is then removed to recover each enantiomer. Chromatography on a chiral stationary phase also works.

**Quantitative analysis.** In GC and HPLC, the area under a peak is proportional to the amount of that compound, and the retention time identifies it (by comparison with standards).

**Worked Example 1: TLC (skill: Rf and polarity)**

A spot travels 3.0 cm while the solvent front travels 6.0 cm on a silica TLC plate. Another spot travels 1.5 cm. (a) Calculate both Rf values. (b) Which compound is more polar?

(a) Rf₁ = 3.0 / 6.0 = 0.50. Rf₂ = 1.5 / 6.0 = 0.25. (b) On silica, the more polar compound is held more strongly and moves less, so the second compound (Rf = 0.25) is more polar.

**Worked Example 2: An acid-base extraction (skill: designing the separation)**

An ether solution contains benzoic acid (an acid), aniline (a base) and naphthalene (neutral). Describe how to separate them.

1. Shake the ether solution with aqueous NaHCO₃. Benzoic acid is converted to sodium benzoate and dissolves in the aqueous layer; separate the layers.
2. Shake the remaining ether solution with aqueous HCl. Aniline is converted to anilinium chloride and dissolves in the aqueous layer; separate.
3. The ether layer now contains only naphthalene; evaporate the ether to recover it.
4. Acidify the first aqueous layer to precipitate benzoic acid; make the second aqueous layer basic to liberate aniline.

**Worked Example 3: One extraction versus two (skill: partition coefficient)**

A solute has K = 4.0 (organic/aqueous). A 100 mL aqueous solution contains 1.00 g of the solute. Compare (a) one extraction with 100 mL of organic solvent, and (b) two extractions with 50 mL each.

(a) Fraction left in water after one extraction = V_aq / (V_aq + K V_org) = 100 / (100 + 4.0 × 100) = 1/5 = 0.20, so 0.20 g remains.

(b) For each 50 mL extraction, the fraction left = 100 / (100 + 4.0 × 50) = 100 / 300 = 1/3. After two extractions: (1/3)² = 1/9 = 0.11 g remains.

Two small extractions leave about half as much solute behind as one big one.

**Worked Example 4: Proteins (skill: choose the method)**

(a) Three proteins of mass 25, 50 and 100 kDa are run on SDS-PAGE and on a size-exclusion column. Give the order of migration/elution. (b) A protein has pI = 9. At pH 7, is it positive or negative? Will it bind a cation-exchange resin? (c) How would you purify a protein that carries a polyhistidine tag?

(a) SDS-PAGE: the smallest (25 kDa) migrates farthest; the largest (100 kDa) the least. Size-exclusion: the largest (100 kDa) elutes first, the smallest (25 kDa) last. The orders are reversed.

(b) pH (7) is below pI (9), so the protein carries a net positive charge. It binds a negatively charged cation-exchange resin.

(c) Affinity chromatography on a nickel-charged resin, which binds the histidine tag; other proteins wash through; elute the tagged protein with a competing ligand (such as imidazole).

**Worked Example 5: Resolving a racemate (skill: diastereomers)**

Explain how to separate the enantiomers of a racemic carboxylic acid using a single enantiomer of a chiral amine.

React the racemic acid (R-acid and S-acid) with pure (R)-amine. The two salts, (R-acid)(R-amine) and (S-acid)(R-amine), are diastereomers and have different solubilities. Separate them by crystallization. Treat each salt with strong acid to liberate each pure enantiomer of the acid, and recover the amine.

**More Praxis Tips**

Praxis Tip: Two orderings that students often confuse are reversed: in size-exclusion chromatography the big molecules elute first, while in gel electrophoresis the small molecules travel farthest. Both follow from the same fact: small molecules access more of the porous material.

Praxis Tip: If a question describes a "stationary phase" that is polar (silica, alumina), predict that polar compounds will be retained longer. Reverse the rule for a nonpolar stationary phase.

Praxis Tip: For extraction problems, write the structure of the neutral and ionic forms of each compound, and mark which layer each is in under the conditions of the question.

Praxis Tip: A question about "which technique separates compounds with very different boiling points" almost never wants fractional distillation. Pick simple distillation unless the boiling points are close.

Praxis Tip: The retention factor Rf has no units and is always between 0 and 1. A value above 1 means you divided the wrong way.

**Common Mistakes**

- Reversing the elution order in size-exclusion chromatography.
- Assuming a more polar compound always has a higher Rf, without checking the stationary phase.
- Forgetting that an extraction with aqueous base moves acids, not bases, into water.
- Using fractional distillation when simple distillation is enough (or the reverse).
- Trying to separate enantiomers with ordinary methods.
- Assigning the direction of DNA migration to the negative electrode.

**Checkpoint Questions**

1. On a silica gel TLC plate (a polar stationary phase), which compound would be expected to have the lowest Rf value?
   A. The least polar compound
   B. A compound of the same polarity as the solvent
   C. The most polar compound
   D. Rf does not depend on polarity

2. Which technique is most appropriate for separating two liquids that have boiling points of 60 °C and 140 °C?
   A. Simple distillation
   B. Recrystallization
   C. Gel electrophoresis
   D. Size-exclusion chromatography

3. In SDS-PAGE, proteins are separated mainly by
   A. charge, with positively charged proteins migrating fastest
   B. mass, with smaller proteins migrating farther
   C. mass, with larger proteins migrating farther
   D. isoelectric point

4. In size-exclusion (gel filtration) chromatography, the first molecules to elute from the column are the
   A. smallest molecules, which travel the shortest path
   B. most positively charged molecules
   C. molecules with the highest affinity for the stationary phase
   D. largest molecules, which cannot enter the pores in the beads

5. An ether solution containing an amine and a neutral compound is shaken with dilute aqueous HCl. Which compound is extracted into the aqueous layer?
   A. The neutral compound, as its hydrochloride
   B. The amine, as its water-soluble ammonium salt
   C. Both compounds equally
   D. Neither compound

6. Why can a racemic mixture of enantiomers not be separated by ordinary distillation or recrystallization?
   A. Enantiomers have identical physical properties such as boiling point and solubility in achiral solvents
   B. Enantiomers have different boiling points but the same melting points
   C. Enantiomers react with each other
   D. Enantiomers are always gases

7. On a TLC plate, a compound travels 2.4 cm while the solvent front travels 8.0 cm. The Rf value is
   A. 3.3
   B. 0.24
   C. 5.6
   D. 0.30

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **C.** Polar compounds adsorb strongly to the polar silica and move slowly, so they have the lowest Rf. (A moves farthest because it interacts weakly with the silica; B moves farther than a strongly adsorbed compound; D contradicts the principle of chromatography.)
2. **A.** A large difference in boiling points (80 °C) allows a clean separation by simple distillation. (B applies to solids; C applies to charged macromolecules; D separates by size, not by boiling point.)
3. **B.** SDS unfolds proteins and coats them with negative charge in proportion to their mass, so migration through the gel depends on size and smaller proteins move farther. (A SDS gives all proteins a similar charge per unit mass; C reverses the order; D describes isoelectric focusing.)
4. **D.** Large molecules are excluded from the pores, so they take a shorter path through the column and emerge first. (A describes the reverse of the true order; B describes ion-exchange chromatography; C describes affinity chromatography.)
5. **B.** The acid protonates the amine to give an ionic ammonium salt, which dissolves in water; the neutral compound stays in the ether. (A a neutral compound has no basic site to protonate; C ignores the difference in basicity; D ignores the acid-base reaction.)
6. **A.** Enantiomers differ only in their interaction with plane-polarized light and with other chiral objects, so a chiral resolving agent is needed. (B enantiomers share all of these properties; C they do not react with each other under these conditions; D they can be solids, liquids or gases.)
7. **D.** Rf = 2.4 / 8.0 = 0.30. (A inverts the ratio; B divides by 10 without reference to the solvent front; C subtracts the distances.)

Praxis Tip: After the checkpoint questions, look at each wrong choice and name the slip (elution order reversed, wrong layer, wrong electrode, polarity of the phase). Log it in your error log ([Strategy: The Question Method](chapter:4)).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "Extraction separates by solubility and acid-base extraction moves ionic forms into water, distillation separates by boiling point, chromatography separates by how strongly each compound sticks to the stationary phase so that on silica the polar compounds move least, size-exclusion elutes the biggest proteins first while gel electrophoresis runs the smallest farthest, and enantiomers must first be turned into diastereomers to be resolved."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 2 and 3 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set that includes [Lesson 20](chapter:30) carboxylic acids, [Lesson 16](chapter:25) acids and bases, and [Lesson 18](chapter:28) stereochemistry), and after 21 days (explain the lesson aloud).

*Interleave:* alternate a separation problem with a spectroscopy problem and an acid-base problem. Then take the [Organic Chemistry Set](chapter:33).

Praxis Tip: End each study session by writing, from memory, the property each separation method uses, the Rf formula, and the elution orders for size-exclusion chromatography and SDS-PAGE.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Verified: Rf = 0.50 and 0.25; 0.20 g after one extraction and 0.11 g after two (1/9); 2.4/8.0 = 0.30.
- Answer key positions: C, A, B, D, B, A, D.
- Verify with a reviewer: the boiling-point difference guidance for simple distillation; reverse-phase HPLC elution order; SDS-PAGE description; polyhistidine-tag affinity detail.
- Category 5C topics covered: extraction, distillation, chromatography (column, GC, HPLC, paper, TLC), peptide/protein separations (electrophoresis, size-exclusion, ion-exchange, affinity chromatography), racemic mixtures and separation of enantiomers, quantitative analysis.
