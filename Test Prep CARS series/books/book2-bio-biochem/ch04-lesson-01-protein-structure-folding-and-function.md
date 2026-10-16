# Lesson 1: Protein Structure, Folding and Function

**What you will be able to do**

- Connect each level of protein structure to the interactions that stabilize it and the treatments that destroy it.
- Explain how proteins reach their native fold, what chaperones do, and how misfolding causes disease.
- Compare myoglobin and hemoglobin, read an oxygen-dissociation curve, and predict shifts caused by pH, carbon dioxide, 2,3-bisphosphoglycerate and fetal hemoglobin.
- Relate the structures of collagen and keratin to their roles, and describe how motor proteins, transport proteins and antibodies use binding and shape change.
- Predict the effect of a single amino acid substitution on folding, binding or assembly.

**Why it matters for the exam**

This lesson belongs to category 1A, the structure and function of proteins. Passages in this area rarely ask you to recite a definition. They give you a mutation, a curve, a denaturing treatment or a gel result, and ask what changed and why. Book 1, Lesson 23 taught the amino acids, the peptide bond, the four levels of structure and the basics of denaturation. Book 1, Lesson 24 taught enzymes, kinetics, inhibition and allostery. This lesson does not repeat those. It asks what those rules predict when a whole protein folds, misfolds, binds oxygen cooperatively, builds a tissue or moves a cargo. Hemoglobin is the star: it ties together the Bohr effect, allostery, acid-base balance ([Lesson 18](chapter:24)) and one of the best-known single-residue diseases.

Praxis Tip: For every protein you meet, ask three questions in order: what is its shape, what does that shape let it bind, and what changes when it binds? Most 1A questions are one of those three in disguise.

**Concept Review**

**Levels of structure: what holds each one, what breaks it.** The four levels are familiar. What the exam rewards is knowing the stabilizing forces and the reagent that defeats each one.

| Level | Main stabilizing forces | Disrupted by |
|---|---|---|
| Primary | Peptide bonds | Strong acid and heat (hydrolysis), proteases |
| Secondary | Backbone hydrogen bonds | Heat, urea, extreme pH |
| Tertiary | Hydrophobic core, ionic and H bonds, disulfides | Heat, urea, SDS, reducing agents |
| Quaternary | Same noncovalent forces between subunits | Dilution, pH, salt, detergents |

Notice that denaturation, by definition, leaves the primary structure alone. A protein that has been boiled still has its sequence. That is why some small proteins can refold, and why the primary sequence is said to contain the instructions for the fold.

Two structural vocabulary items extend Book 1. A **domain** is a compact, independently folding region of a polypeptide, often with its own function (a binding domain, a catalytic domain). A **motif** is a small recurring pattern of secondary structure, such as a helix-turn-helix that binds DNA. Many proteins are built from several domains, and large changes in function can come from swapping a domain.

Secondary structure also has tendencies you can use. Proline lacks a free backbone N-H and has a rigid ring, so it generally breaks α-helices and puts bends in chains. Glycine, with only a hydrogen as its side chain, is flexible and fits into tight turns. A stretch of mostly hydrophobic residues about 20 amino acids long is the classic signature of a helix that spans a membrane, because the helix hides its backbone hydrogen bonds internally while its side chains face the lipid.

**Folding.** In the 1950s and 60s, experiments on the small enzyme ribonuclease showed that a protein unfolded with urea and a reducing agent regained activity when both were removed slowly. The sequence alone was enough to specify the fold in a test tube. This is the principle behind the idea that folding is driven toward the lowest free-energy state. A useful picture is a **folding funnel**: the unfolded chain has many high-energy, high-entropy conformations, and as the chain collapses and forms contacts the number of available shapes narrows toward one low-energy native state. The hydrophobic effect (Book 1, Lesson 23) provides the main push. The folded state is only marginally more stable than the unfolded state, generally by a few tens of kJ/mol, so small changes in sequence or environment can tip the balance.

The cell speeds up and protects folding:

- **Chaperones** (such as the Hsp70 family) bind exposed hydrophobic stretches of newly made or stressed polypeptides, prevent them from clumping together, and release them in cycles powered by ATP hydrolysis. Many chaperones are **heat shock proteins**, made in larger amounts when the cell is stressed.
- **Chaperonins** (such as the bacterial GroEL/GroES system) are barrel-shaped complexes that enclose a single unfolded protein in a protected chamber, again using ATP. [VERIFY] Eukaryotes have a related chaperonin of their own.
- **Protein disulfide isomerase** helps the correct disulfide bonds form in the oxidizing environment of the endoplasmic reticulum. **Peptidyl prolyl isomerase** speeds the slow interconversion of cis and trans peptide bonds before proline.

The most important thing a chaperone does not do is supply information. It does not change the final fold; it only keeps the chain out of trouble while it finds that fold.

**Misfolding and disease.** If the quality-control system is overwhelmed, misfolded proteins are tagged with ubiquitin and degraded by the proteasome, or they aggregate. Aggregates rich in β-sheets, called **amyloid**, accumulate in several neurodegenerative diseases. **Prions** are a special case: a misfolded form of a normal cell protein that can convert its properly folded counterparts into the misfolded form, so the "infectious agent" is a protein conformation rather than a nucleic acid. The same amino acid sequence can therefore have two stable shapes with different consequences.

**Post-translational modification.** Many proteins are altered after synthesis. Common examples are phosphorylation of serine, threonine or tyrosine (reversible regulation, Book 1, Lesson 24), attachment of sugars (glycosylation, [Lesson 2](chapter:5)), attachment of lipids that anchor a protein to a membrane, and **proteolytic cleavage**, as when proinsulin is trimmed to insulin. Each modification adds a chemical group the 20 amino acids lack, or changes the protein's location or lifetime.

**Myoglobin and hemoglobin.** Both bind oxygen at a **heme** group: a flat ring with an iron atom in the Fe²⁺ (ferrous) state. Oxygen binds to iron reversibly. If the iron is oxidized to Fe³⁺ the protein (now methemoglobin) generally cannot carry oxygen. Carbon monoxide binds the same iron with far greater affinity than oxygen, which is why it poisons the system: it occupies the sites and also shifts the remaining sites toward holding on to the oxygen they have.

- **Myoglobin** is a single polypeptide with one heme, found in muscle, where it stores oxygen and releases it when the muscle is working hard. Its binding curve is **hyperbolic**, like a simple enzyme saturation curve.
- **Hemoglobin** is a tetramer of two α and two β chains (α₂β₂), each with one heme, in red blood cells. It transports oxygen from lungs to tissues, and it also carries some carbon dioxide and buffers protons. Its binding curve is **sigmoidal**.

The sigmoidal shape is the signature of **cooperativity**. Hemoglobin exists in two broad forms: the **T (tense)** state, with low oxygen affinity, favored when no oxygen is bound, and the **R (relaxed)** state, with high affinity, favored when oxygen is bound. Binding oxygen at one heme shifts the subunit interfaces toward R, so each successive oxygen binds more easily. A convenient way to describe this is the **Hill coefficient**, n. A protein with independent sites has n = 1 (myoglobin). Hemoglobin has n of about 2.8, which is close to but less than the number of sites, 4. A Hill coefficient can never exceed the number of binding sites.

The result is physiologically useful. Over the pressure range found between lung and tissues, the steep middle of the hemoglobin curve means a small fall in oxygen pressure releases a large fraction of the oxygen. Myoglobin, which has a much lower **P₅₀** (the oxygen pressure at which the protein is half saturated), holds on to oxygen at pressures at which hemoglobin is already giving it up. Roughly: P₅₀ of myoglobin is about 3 mmHg, and that of adult hemoglobin about 26 mmHg. [VERIFY approximate values] The exact numbers matter less than their order of magnitude: myoglobin is far more oxygen-hungry than hemoglobin, so oxygen flows from blood to muscle.

An equation used for simple modeling is the Hill equation. If it appears on the exam it will be given to you. In fractional saturation Y:

Y = pO₂ⁿ / (P₅₀ⁿ + pO₂ⁿ)

With n = 1 this reduces to the myoglobin curve, Y = pO₂ / (P₅₀ + pO₂).

**Factors that shift the hemoglobin curve.** The oxygen-dissociation curve of hemoglobin plots percent saturation against oxygen pressure.

| Change | Direction of shift | P₅₀ and affinity |
|---|---|---|
| Lower pH, higher CO₂ (Bohr effect) | Right | P₅₀ up, affinity down |
| Higher 2,3-BPG | Right | P₅₀ up, affinity down |
| Higher temperature | Right | P₅₀ up, affinity down |
| Fetal hemoglobin (α₂γ₂) | Left | P₅₀ down, affinity up |

A **right shift** means that more oxygen is released at a given tissue pressure; a **left shift** means hemoglobin holds oxygen more tightly. Working muscle is warm, acidic and rich in CO₂, so it pulls oxygen off hemoglobin where it is most needed. This is the **Bohr effect**: protons (and CO₂) bind to hemoglobin, favoring T and releasing oxygen. The reverse is true in the lungs, where CO₂ is exhaled, pH rises, and oxygen binding is favored. The **Haldane effect** is the mirror image: oxygenated hemoglobin binds less CO₂ and H⁺, helping unload CO₂ in the lungs.

**2,3-Bisphosphoglycerate (2,3-BPG)**, a by-product of glycolysis in red cells, binds in the central cavity of deoxygenated hemoglobin, whose positive charges attract its negative charges, and stabilizes the T state. [VERIFY] With less oxygen supply (high altitude, chronic lung disease) red cells make more 2,3-BPG, which shifts the curve right and helps unload oxygen. **Fetal hemoglobin** has γ chains in place of β chains; it binds 2,3-BPG less strongly and therefore has higher oxygen affinity, which lets oxygen move from maternal to fetal blood across the placenta.

Hemoglobin also illustrates what a single substitution can do. In **sickle cell disease** a glutamate in the β chain (position 6) is replaced by valine. The new surface hydrophobic patch fits into a pocket on another hemoglobin in the deoxygenated state, so deoxygenated molecules polymerize into fibers that distort the red cell. One residue changed, so the disease arises from altered quaternary interactions, not from a change in the heme.

Praxis Tip: A "right shift" is always the answer to "what helps tissues take oxygen?" Remember the shift triggers as the conditions in a working muscle: acid, carbon dioxide, heat, and extra 2,3-BPG.

**Structural proteins.** Fibrous proteins give cells and tissues strength and shape.

- **Collagen**, the most abundant protein in animals, forms a **triple helix** of three left-handed polyproline-type chains wound into a right-handed rope. Every third residue is **glycine**, the only one small enough to sit in the crowded core, giving a repeating Gly-X-Y pattern, where X and Y are often proline and **hydroxyproline**. Hydroxylation of proline requires **vitamin C** (ascorbic acid) as a cofactor; its deficiency weakens collagen and produces scurvy. Collagen fibers are then cross-linked for strength. Replacing a core glycine with any larger residue disrupts the helix and causes brittle bone and other connective tissue disorders.
- **Keratin** forms intermediate filaments of coiled coils of α-helices in hair, nails and skin. Disulfide bonds between cysteines add strength; hair is made curly or straight by breaking and re-forming them.
- **Cytoskeletal proteins** such as actin filaments, microtubules (tubulin) and intermediate filaments set cell shape and provide tracks for movement; they are covered with the cell in [Lesson 12](chapter:17).

**Motor proteins.** Motor proteins convert the chemical energy of ATP into directed movement by cycling between conformations.

- **Myosin** binds actin, pivots in a power stroke, and is released when a new ATP binds. It drives muscle contraction ([Lesson 20](chapter:27)).
- **Kinesin** walks toward the plus end of a microtubule, which generally carries vesicles outward from the cell body toward the periphery. **Dynein** walks toward the minus end, generally carrying cargo inward.

**Transport and binding proteins.** Hemoglobin is a carrier in the blood; **albumin** carries fatty acids, hormones and drugs; **transferrin** carries iron. Channels and carrier proteins in membranes move ions and solutes ([Lesson 12](chapter:17)). All share one principle: a specific binding site with an affinity tuned to the job, so the carrier binds where the ligand is plentiful and releases where it is scarce.

**Antibodies.** An **antibody** (immunoglobulin) is a Y-shaped protein of **two identical heavy chains and two identical light chains** held together by disulfide bonds and noncovalent forces. The tips of the arms (Fab regions) contain **variable regions** that form the antigen-binding sites; the stem (Fc region) is constant within a class and triggers immune effector functions. Because each Y has two arms, one antibody generally has **two** antigen-binding sites. Genetic recombination generates a vast number of variable regions ([Lesson 21](chapter:28)).

Praxis Tip: Tie each fibrous protein to one residue clue. Collagen: glycine every third residue plus hydroxyproline (vitamin C). Keratin: cysteine and disulfides. Antibodies: disulfide-linked heavy and light chains with variable tips.

**Worked Example 1: Reading oxygen binding (skill: using the saturation equations)**

Model myoglobin with Y = pO₂ / (3 + pO₂) and hemoglobin with the Hill equation using P₅₀ = 26 mmHg and n = 3 (a simplification of the real value). Lungs: pO₂ = 100 mmHg. Resting muscle: pO₂ = 40 mmHg. How much of hemoglobin's oxygen is delivered, and how saturated is myoglobin at 30 mmHg?

Hemoglobin in the lungs: Y = 100³ / (26³ + 100³) = 1,000,000 / 1,017,576, which is about 0.98 (98 percent). In the muscle: Y = 64,000 / (17,576 + 64,000) = 0.78 (78 percent). Delivery is about 98 − 78 = 20 percentage points of saturation, so roughly one fifth of the capacity. Myoglobin at 30 mmHg: Y = 30 / 33 = 0.91, about 91 percent saturated. Myoglobin is still nearly full at a pressure where hemoglobin has released oxygen, which is exactly the direction that moves oxygen from blood to muscle. In hard exercise the muscle pressure falls further and the Bohr shift adds to delivery, so a much larger share is released.

**Worked Example 2: Predicting shifts (skill: reading a curve)**

A runner's leg muscle has lower pH, a higher temperature and higher CO₂. Predict the effect on hemoglobin's curve and on oxygen delivery. A mother living at altitude has higher 2,3-BPG in her red cells. What is the consequence for her fetus?

For the runner, every change shifts the curve to the right: P₅₀ increases and hemoglobin releases more oxygen at the same pressure. The curve still reaches full saturation in the lungs because the lung pressure is high, so loading is little affected while unloading improves. For the mother, higher 2,3-BPG shifts her own curve right, which helps her tissues unload oxygen. Fetal hemoglobin, with less affinity for 2,3-BPG, remains to the left of the mother's curve, so the gradient for oxygen transfer to the fetus is maintained.

**Worked Example 3: One residue (skill: from substitution to mechanism)**

In the β chain of hemoglobin, Glu6 is replaced with Val. A different mutation replaces a surface lysine, far from any interface, with arginine. Which is most likely to affect polymerization, and why?

Replacing glutamate (negative, polar) with valine (nonpolar) at the surface creates a sticky hydrophobic patch that can fit into a complementary pocket on another molecule in the deoxy state: this generates polymers.The lysine to arginine change on the surface, far from interfaces, keeps a positive charge and is likely to be nearly silent. The general rule: the effect of a substitution depends on the location (core, surface, interface, active site) and the chemical difference (size, charge, polarity).

**Worked Example 4: An unfolding experiment (skill: interpreting a refolding result)**

A small enzyme with four disulfide bonds is treated with 8 M urea plus a reducing agent, and its activity falls to zero. In experiment A the urea and reducing agent are removed together by dialysis and the enzyme is left in air: activity returns to 90 percent. In experiment B, the reducing agent is removed while urea remains. Disulfides are allowed to form, and the urea is then removed. Activity returns to only about 1 percent. What do these results show?

Experiment A shows that the sequence alone can specify the fold, because activity returns with no cell machinery. The loss of activity shows that activity depends on the folded form, not just the primary structure. In experiment B the disulfides formed while the protein was unfolded and linked the wrong cysteines (scrambled pairings), and removal of urea left the chain locked in a nonnative arrangement. The lesson is that cells use protein disulfide isomerase and an ordered folding pathway to avoid this; disulfides stabilize a fold, they do not generally direct it.

**Worked Example 5: Counting and connecting (skill: structure to function)**

(a) An IgG antibody is incubated with a reducing agent and then run on a denaturing gel. How many bands are expected, and how many distinct polypeptide types? (b) A kinesin motor attached to a vesicle is watched in an axon moving toward the terminal. Which end of the microtubule does the terminal face? (c) A mutation replaces a glycine in a collagen Gly-X-Y repeat with arginine. Why is the effect severe?

(a) The reducing agent breaks the disulfide bonds and the denaturing detergent breaks the noncovalent ones, so the Y falls apart into its four chains: two identical heavy chains and two identical light chains, which gives two types of polypeptide (two bands, heavy and light). (b) Kinesin generally moves toward the plus end, so the terminal faces the plus end. (c) Glycine sits in the crowded center of the triple helix, where no side chain larger than hydrogen fits, so a bulky arginine disrupts packing of the entire rope, and because the helix zips up from one end the defect has consequences along the whole fiber.

**More Praxis Tips**

Praxis Tip: When the stem says "heat" or "urea," think noncovalent interactions break and peptide bonds survive. When it says "reducing agent," think disulfides.

Praxis Tip: A Hill coefficient above 1 means cooperativity and below the number of sites. If an answer choice gives a coefficient larger than the number of binding sites, discard it.

Praxis Tip: Do not say hemoglobin "has a higher affinity for oxygen" without saying which state. T is low affinity and R is high affinity, and the curve is the average of the population.

Praxis Tip: For any mutation question, locate the residue first (core, surface, interface, active site), then ask what physical property changed. Charge-to-hydrophobic on a surface is a classic recipe for aggregation.

Praxis Tip: Chaperones are not enzymes of folding in the sense of supplying shape. If a choice says a chaperone "determines" the fold, it is probably wrong. If it says it "prevents aggregation," it is probably right.

Praxis Tip: Draw the sigmoidal and hyperbolic curves on scratch paper together, with P₅₀ marked, in the first minute of any oxygen-binding passage. Eight seconds of drawing saves three minutes of confusion. (British restraint is not a virtue when a curve shifts.)

Praxis Tip: When the stem says "fetal," think left shift and weak 2,3-BPG binding, so the fetus wins the tug of war for oxygen without any dramatic fuss.

**Common Mistakes**

- Saying denaturation breaks peptide bonds.
- Reversing the direction of shift: acid, heat and CO₂ move the curve to the right, not the left.
- Treating a right shift as a stronger hold on oxygen. It is a weaker hold.
- Saying chaperones tell a protein what shape to take.
- Forgetting that the Hill coefficient of a cooperative tetramer is below 4.
- Thinking the Bohr effect changes the heme chemistry. It changes the protein's conformational equilibrium (T versus R).
- Confusing antibody variable regions (the arms) with the constant stem.

**Checkpoint Questions**

1. A patient with a collagen disorder is found to have a glycine in a Gly-X-Y repeat replaced by arginine. The most likely reason this disrupts the tissue is that
   A. arginine is negatively charged and attracts water
   B. glycine forms disulfide bonds between chains
   C. glycine is the only residue small enough to fit in the crowded core of the triple helix
   D. arginine cannot be incorporated by ribosomes

2. Myoglobin shows a hyperbolic oxygen-binding curve and hemoglobin shows a sigmoidal curve. The best explanation is that
   A. hemoglobin has multiple subunits whose affinities change as oxygen binds, while myoglobin has a single heme
   B. myoglobin contains no iron
   C. hemoglobin binds oxygen at non-heme sites
   D. myoglobin is a tetramer with a Hill coefficient of 4

3. During intense exercise, a muscle becomes more acidic and warmer and its CO₂ level rises. Compared with resting conditions, hemoglobin passing through this muscle will
   A. hold oxygen more tightly, because the curve shifts to the left
   B. release the same oxygen, because the Bohr effect acts only in the lungs
   C. lose its heme iron, because acid removes the metal
   D. release more oxygen at a given oxygen pressure, because the curve shifts to the right

4. Which statement best describes the role of molecular chaperones such as Hsp70?
   A. They supply the information that specifies the final fold
   B. They bind exposed hydrophobic regions of unfolded chains to prevent aggregation, often using ATP
   C. They hydrolyze peptide bonds in misfolded proteins
   D. They add phosphate groups to the folded protein to activate it

5. Two purified proteins were tested for oxygen binding. Protein X was 33 percent saturated at 2 mmHg, 50 percent at 4, 67 percent at 8 and 88 percent at 30. Protein Y was 4 percent saturated at 10 mmHg, 27 percent at 20, 55 percent at 30, 74 percent at 40 and 91 percent at 60. The data are best explained if
   A. protein X is cooperative because it saturates at low pressure
   B. both proteins bind oxygen independently at identical sites
   C. protein Y has a lower P₅₀ than protein X
   D. protein Y is cooperative and protein X binds with a hyperbolic curve and a P₅₀ near 4 mmHg

6. A protein is heated until it loses activity and forms a cloudy precipitate. Which of the following is most likely to be true?
   A. Noncovalent interactions were disrupted and exposed hydrophobic regions aggregated, while the peptide bonds remained intact
   B. The peptide bonds were hydrolyzed into free amino acids
   C. The primary structure changed to a new sequence
   D. Only the quaternary structure was lost

7. Fetal blood has a higher oxygen affinity than maternal blood, mainly because fetal hemoglobin
   A. binds 2,3-BPG more strongly, shifting its curve to the right
   B. binds 2,3-BPG less strongly than adult hemoglobin, shifting its curve to the left
   C. lacks heme groups and binds oxygen directly
   D. is a monomer like myoglobin

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **C.** Every third position lies in the center of the helix where only hydrogen fits. (A is wrong because arginine is positively charged, and charge is not the central issue; B is wrong because glycine has no sulfur and forms no disulfide bonds; D is wrong because arginine is one of the standard 20 amino acids.)
2. **A.** Cooperativity needs interacting sites; a single-site protein follows simple saturation binding. (B is wrong because myoglobin has a heme with iron; C is wrong because each hemoglobin subunit binds oxygen at its own heme; D is wrong because myoglobin is a monomer with a Hill coefficient of about 1.)
3. **D.** The Bohr effect plus heat favors the T state and lowers oxygen affinity. (A is wrong because acid, heat and CO₂ shift the curve right; B is wrong because the Bohr effect acts mainly in tissues; C is wrong because the iron stays bound to the heme at these conditions.)
4. **B.** Chaperones assist but do not instruct folding. (A is wrong because the amino acid sequence specifies the fold; C is wrong because that is the job of proteases and the proteasome; D is wrong because phosphorylation is carried out by kinases, not chaperones.)
5. **D.** X follows Y = p/(4 + p). Y rises slowly then steeply, the S shape of cooperativity, with half saturation near 28 mmHg. (A is wrong because saturating at low pressure shows high affinity, not cooperativity; B is wrong because protein Y shows a steep, S-shaped rise; C is wrong because Y reaches half saturation near 30 mmHg compared with 4 for X.)
6. **A.** Denaturation unfolds the protein without breaking covalent backbone bonds, and exposed hydrophobic regions stick together. (B is wrong because ordinary heating does not hydrolyze peptide bonds at these temperatures; C is wrong because the sequence is unchanged by denaturation; D is wrong because secondary and tertiary structure are lost as well.)
7. **B.** Less 2,3-BPG stabilization of the T state means higher affinity and a left-shifted curve. (A is wrong because stronger 2,3-BPG binding lowers affinity; C is wrong because fetal hemoglobin contains heme; D is wrong because fetal hemoglobin is a tetramer (two α and two γ chains).)

Praxis Tip: After the checkpoint questions, sort each wrong choice into a slip (direction of shift, level of structure, which bond breaks) and log it in your error log, see [Strategy: Learning Pathways and Systems Without Rote Memory](chapter:2).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "A protein's sequence directs its fold, chaperones keep the chain from aggregating while it finds that fold, and denaturation breaks noncovalent forces but not peptide bonds; myoglobin binds oxygen in a hyperbolic curve while hemoglobin's cooperative T-to-R switch gives a sigmoidal curve that shifts right with acid, carbon dioxide, heat and 2,3-BPG and left in the fetus; collagen, keratin, motors and antibodies show how a specific residue pattern and shape yield a specific job."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 1 and 2 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set including Book 1, Lesson 24 enzyme kinetics), and after 21 days (explain the lesson aloud).

*Interleave:* alternate a hemoglobin curve problem with an enzyme inhibition problem and a buffer problem. The [Biomolecules and Metabolism Set](chapter:10) will test these together.

Praxis Tip: End each study session by drawing from memory both oxygen-binding curves, labeling P₅₀ and the four shift factors, and listing one residue clue for each structural protein.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Arithmetic verified in the generator script: myoglobin Y at 30 and 3 mmHg (91 and 50 percent); simplified Hill model (n = 3, P₅₀ = 26) gives 98 percent at 100 mmHg and 78 percent at 40 mmHg.
- Answer key positions: C, A, D, B, D, A, B.
- Verify with a biochemistry reviewer: P₅₀ values; Hill coefficient of hemoglobin (about 2.8); 2,3-BPG binding site description; the eukaryotic chaperonin statement; the claim about CO shifting remaining sites.
- Category 1A topics covered: structure and function of proteins (levels of structure, folding, chaperones, denaturation, hemoglobin, cooperativity, Bohr effect, structural proteins, motor proteins, transport proteins, antibodies).
