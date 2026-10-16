# Lesson 4: Bioenergetics and Glycolysis

**What you will be able to do**

- Distinguish ΔG from ΔG°′, use ΔG = ΔG°′ + RT ln Q, and decide the direction of a reaction in the cell.
- Explain why ATP is a useful energy currency and how coupling drives unfavorable reactions.
- Describe the roles of NAD⁺, NADH, FAD and FADH₂ and connect reduction potential to free energy.
- Walk through the ten steps of glycolysis, naming the committed step, the irreversible steps and the net yield.
- Predict how allosteric regulators and hormones adjust hexokinase or glucokinase, PFK-1 and pyruvate kinase.
- Explain fermentation, the Cori cycle and why some tissues depend on anaerobic glycolysis.

**Why it matters for the exam**

This lesson opens category 1D, bioenergetics and fuel-molecule metabolism. Passages in this category rarely ask you to recite the pathway. They show a perturbation (an inhibitor, a mutant enzyme, a hormone, a tissue with no mitochondria) and ask what happens to the substrates, the products and the energy balance. The concepts you need come largely from Book 1. Free energy and equilibrium come from Book 1, Lesson 14 (thermodynamics) and Lesson 15; reduction potentials and ΔG = −nFE come from Book 1, Lesson 17 (electrochemistry); regulation, Km and Vmax, competitive and allosteric control come from Book 1, Lesson 24 (enzymes). This lesson applies them rather than repeating them.

Praxis Tip: In metabolism passages, find the question the passage is really asking: is it about energy (ΔG), about flow (which enzyme is limiting and how it is regulated), or about redox balance (is NAD⁺ available)? Most items answer to one of the three.

**Concept Review**

**1. ΔG versus ΔG°′.** The standard free energy change ΔG°′ is defined for a reference state (1 M for solutes, pH 7, usually 25 °C; the prime tells you the pH is 7) and tells you about the position of equilibrium. The actual free energy change ΔG depends on the real concentrations in the cell.

ΔG = ΔG°′ + RT ln Q
ΔG°′ = −RT ln K′eq

where Q = [products] / [reactants] at the actual concentrations. At 298 K, RT is about 2.48 kJ/mol and at 310 K about 2.58 kJ/mol. The sign of ΔG, not of ΔG°′, decides the direction. A reaction with a positive ΔG°′ can run forward in the cell if the product is removed fast enough to make Q small. A reaction with ΔG = 0 is at equilibrium. Cells are not at equilibrium; they are in a **steady state**, and keep Q for key reactions far from K′eq by supplying substrates and removing products.

This is why glycolytic steps fall into two classes. Most are **near equilibrium** (ΔG close to zero), so they run in either direction depending on concentrations. A few are **far from equilibrium** (large negative ΔG) and therefore irreversible in the cell. The latter are the regulated steps, which is no coincidence: control is exerted where the flux can be set, and a reaction at equilibrium has no "push" to modulate.

Praxis Tip: ΔG°′ answers "where does this reaction end up if left alone under standard conditions?" ΔG answers "which way is it going right now in this cell?" The exam will try to swap them.

**2. ATP and coupling.** The hydrolysis of ATP to ADP and inorganic phosphate has ΔG°′ of about −30.5 kJ/mol (about −7.3 kcal/mol). In the cell, ATP is held at a very high ratio to ADP, so the actual ΔG is more negative, often in the range of −50 to −65 kJ/mol [VERIFY range].

ATP is "high energy" for specific reasons, not because the phosphoanhydride bond is unusually strong. Hydrolysis relieves electrostatic repulsion among the closely spaced negative charges of the triphosphate, the products ADP and Pi are better stabilized by resonance and by solvation, and entropy increases when one molecule becomes two. The phrase "energy stored in the bond" is a mistake; breaking any bond requires energy, and the favorable hydrolysis comes from the stability of the products.

ATP is also in the middle of a scale of phosphoryl transfer potential. Compounds whose hydrolysis is more favorable than ATP's can phosphorylate ADP; ATP can phosphorylate compounds that are less favorable.

| Compound | ΔG°′ of hydrolysis (kJ/mol) |
|---|---|
| Phosphoenolpyruvate | about −62 |
| 1,3-Bisphosphoglycerate | about −49 |
| ATP (to ADP) | −30.5 |
| Glucose 6-phosphate | about −14 |

[VERIFY the rounded table values if a question depends on them.]

**Coupling.** A thermodynamically unfavorable reaction can be driven by pairing it with a favorable one through a shared intermediate, so that the overall ΔG is the sum.

glucose + Pi → glucose 6-phosphate + H₂O: ΔG°′ = +13.8 kJ/mol
ATP + H₂O → ADP + Pi: ΔG°′ = −30.5 kJ/mol
glucose + ATP → glucose 6-phosphate + ADP: ΔG°′ = −16.7 kJ/mol

The enzyme does not "pay" ATP to the reaction; the phosphoryl group is transferred through a covalent or tightly bound intermediate, so the two reactions are truly coupled. Free energies add; equilibrium constants multiply.

**Two ways to make ATP.** **Substrate-level phosphorylation** transfers a phosphate directly from a high-energy substrate to ADP (two steps of glycolysis do this). **Oxidative phosphorylation** uses a proton gradient generated by the electron transport chain ([Lesson 5](chapter:8)). In glycolysis the second type is not involved; the NADH produced is reoxidized by the mitochondria or by fermentation.

**3. Redox carriers.** Oxidation is loss of electrons (or loss of hydrogen from a carbon); reduction is gain. Catabolism of fuels is overall oxidation, and the electrons are collected by carriers.

- **NAD⁺ / NADH.** NAD⁺ accepts a hydride ion (two electrons plus one proton) from a substrate and becomes NADH. It is derived from the vitamin niacin (B₃). The carrier is soluble and diffuses between enzymes; dehydrogenases in catabolic pathways use it, and NADH delivers electrons to the electron transport chain. The related **NADPH** (carrying an extra phosphate) is generally the reductant for biosynthesis and for protecting against oxidative damage, and is made largely in the pentose phosphate pathway ([Lesson 6](chapter:9)). A rough rule: NAD⁺ for catabolism, NADPH for anabolism.
- **FAD / FADH₂.** FAD (from riboflavin, B₂) accepts two hydrogen atoms (two electrons and two protons) and is generally a tightly bound prosthetic group of its enzyme, a flavoprotein, rather than a freely diffusing carrier. Succinate dehydrogenase, which is in the electron transport chain as well as in the TCA cycle, contains FAD.

Electron transfer follows the thermodynamics of Book 1, Lesson 17. The standard reduction potential of the NAD⁺/NADH couple is about −0.32 V (low, so NADH is a strong reductant), and that of O₂/H₂O is about +0.82 V [VERIFY]. The free energy for transferring n electrons across a potential difference is

ΔG°′ = −nF ΔE°′

with F = 96.485 kJ/(V·mol). For NADH reducing O₂ (n = 2), ΔE°′ = 0.82 − (−0.32) = 1.14 V, so ΔG°′ is about −220 kJ/mol. This is why NADH is a rich source of energy and why the electron transport chain can power ATP synthesis ([Lesson 5](chapter:8)).

Praxis Tip: Think of NAD⁺ as a reusable cart. If it is not returned (reoxidized from NADH) the dehydrogenase has nothing to load onto, and the pathway stops. This idea explains fermentation.

**4. Glycolysis: ten steps in the cytosol.** Glycolysis converts one glucose (6 carbons) into two pyruvate (3 carbons each), a net of 2 ATP and 2 NADH, with no oxygen required. It is split into an investment phase (spending ATP) and a payoff phase (collecting ATP and NADH).

| Step | Reaction | Notes |
|---|---|---|
| 1 | Glucose → glucose 6-P | Hexokinase or glucokinase; uses ATP; irreversible |
| 2 | Glucose 6-P → fructose 6-P | Phosphoglucose isomerase; near equilibrium |
| 3 | Fructose 6-P → fructose 1,6-bisP | PFK-1; uses ATP; committed step |
| 4 | Fructose 1,6-bisP → DHAP + G3P | Aldolase; cleavage into two 3-carbon pieces |
| 5 | DHAP ⇌ G3P | Triose phosphate isomerase |
| 6 | G3P + NAD⁺ + Pi → 1,3-BPG + NADH | G3P dehydrogenase; oxidation |
| 7 | 1,3-BPG → 3-phosphoglycerate | Phosphoglycerate kinase; makes ATP |
| 8 | 3-PG → 2-phosphoglycerate | Phosphoglycerate mutase |
| 9 | 2-PG → phosphoenolpyruvate | Enolase; removes water |
| 10 | PEP → pyruvate | Pyruvate kinase; makes ATP; irreversible |

[VERIFY enzyme names against the course reference; the intermediates are the important part.] Several points repay attention.

- After step 4, everything is doubled: DHAP is converted to glyceraldehyde 3-phosphate (G3P), so one glucose gives two G3P, and steps 6 to 10 happen twice.
- Steps 1 and 3 each spend one ATP (the investment, 2 ATP). Steps 7 and 10 each yield one ATP per G3P, so 4 ATP are made. The **net is 2 ATP** per glucose.
- Step 6 is the only oxidation. It makes 1 NADH per G3P, so 2 NADH per glucose. The Pi incorporated here is why the product has a high-energy acyl phosphate.
- Steps 7 and 10 are substrate-level phosphorylation. PEP donates its phosphate because its hydrolysis (about −62 kJ/mol) is much more favorable than ATP's.
- The **irreversible steps** are 1, 3 and 10. In gluconeogenesis these are bypassed with different enzymes ([Lesson 6](chapter:9)).
- The **committed step** is generally taken to be step 3 (PFK-1). Glucose 6-phosphate can still go to glycogen or the pentose phosphate pathway, but fructose 1,6-bisphosphate is committed to glycolysis.

Net equation:

glucose + 2 NAD⁺ + 2 ADP + 2 Pi → 2 pyruvate + 2 NADH + 2 ATP + 2 H⁺ + 2 H₂O

**5. Regulation of glycolysis.** Regulation is exercised at the three irreversible steps, according to the cell's energy state and the body's hormonal state.

| Enzyme | Activated by | Inhibited by |
|---|---|---|
| Hexokinase | Substrate (glucose) | Glucose 6-P (product) |
| PFK-1 | AMP, ADP, fructose 2,6-bisP | ATP, citrate |
| Pyruvate kinase | Fructose 1,6-bisP | ATP, alanine; glucagon in liver |

- **Hexokinase** is inhibited by its own product, glucose 6-phosphate. If downstream steps back up, glucose 6-phosphate accumulates and phosphorylation of new glucose slows.
- **PFK-1** is the main control point. It is inhibited by high ATP (the cell has enough energy; ATP binds an allosteric site and lowers the affinity for fructose 6-phosphate) and by citrate (a signal that biosynthetic precursors and TCA intermediates are plentiful). It is activated by AMP and ADP (the cell needs energy). The most powerful activator is **fructose 2,6-bisphosphate**, a signaling molecule rather than a pathway intermediate. In liver, high insulin (or low glucagon) raises its concentration, which stimulates glycolysis and inhibits gluconeogenesis; glucagon lowers it [VERIFY details of the bifunctional enzyme PFK-2/FBPase-2].
- **Pyruvate kinase** is activated by fructose 1,6-bisphosphate (a **feed-forward** activation: an earlier intermediate speeds up a later enzyme) and inhibited by ATP and alanine. In the liver, glucagon (through phosphorylation) inactivates it, which spares glucose when the body is fasting.

Praxis Tip: To predict regulation, ask what the cell needs. High ATP, high citrate or high product means slow glycolysis. High AMP or ADP, or a fed state with insulin, means fast glycolysis. The correct answer is nearly always the one that matches that logic.

**6. Hexokinase versus glucokinase.** Most tissues phosphorylate glucose with hexokinase, which has a low Km (high affinity; roughly 0.1 mM [VERIFY]), is saturated at normal blood glucose and is inhibited by glucose 6-phosphate. This lets muscle and brain take glucose for their own needs. The liver and the pancreatic beta cell use **glucokinase** (hexokinase IV), which has a much higher Km (roughly 5 to 10 mM [VERIFY]) and high Vmax, and is not inhibited by glucose 6-phosphate. Its rate therefore tracks blood glucose. When glucose rises after a meal, the liver takes more up, stores it as glycogen and converts it; when glucose is low, the liver does not compete with the brain for it. In the beta cell, glucokinase works as a glucose sensor that sets insulin secretion ([Lesson 6](chapter:9)). Glucokinase kinetics are somewhat sigmoidal, and its activity is also controlled by a regulatory protein and by insulin [VERIFY]. For exam purposes, the contrast is high affinity and product inhibition (hexokinase) versus lower affinity, high capacity and sensing (glucokinase).

**7. Fates of pyruvate and fermentation.** Aerobically, pyruvate enters mitochondria and is converted to acetyl-CoA ([Lesson 5](chapter:8)). Without oxygen (or in cells that lack mitochondria), NADH cannot be reoxidized by the electron transport chain and the pool of NAD⁺ would run out, stopping step 6. **Fermentation** solves this: it reduces pyruvate (or a derivative) with NADH, regenerating NAD⁺ so glycolysis can continue. It makes no extra ATP; the ATP yield stays at 2 per glucose.

- **Lactate fermentation:** pyruvate + NADH + H⁺ → lactate + NAD⁺, catalyzed by lactate dehydrogenase. This occurs in working muscle at high demand, in red blood cells and in some microorganisms.
- **Alcoholic fermentation (yeast):** pyruvate is decarboxylated to acetaldehyde (releasing CO₂; thiamine pyrophosphate is the cofactor), and acetaldehyde is reduced to ethanol by NADH, regenerating NAD⁺.

**Cori cycle.** Lactate produced by muscle (or red cells) enters the blood, travels to the liver, and is converted back to pyruvate and then to glucose by gluconeogenesis; glucose returns to the muscle. The cycle moves the metabolic burden of regenerating glucose from the muscle to the liver, using ATP and GTP in the liver (roughly 6 ATP equivalents per glucose made [VERIFY]) while the muscle gains only 2 ATP per glucose, so the cycle as a whole costs energy. It also keeps the lactate from building up and acidifying the muscle, and lets the muscle keep working anaerobically when oxygen is limited.

**Tissue dependence.** Red blood cells have no mitochondria and therefore depend on glycolysis and lactate formation for ATP. Tissues with high demand and an interrupted blood supply, such as a muscle during sprint exercise, rely on fermentation. The brain generally depends on a steady supply of glucose.

Other sugars enter glycolysis by conversion. Galactose is converted to glucose derivatives in the liver. Dietary fructose in liver is generally phosphorylated and cleaved to triose phosphates, entering below PFK-1 [VERIFY], which is one reason fructose is metabolized without the major PFK-1 control.

**Worked Example 1: Coupling (skill: quantitative reasoning)**

Phosphorylation of glucose by inorganic phosphate has ΔG°′ = +13.8 kJ/mol. ATP hydrolysis has ΔG°′ = −30.5 kJ/mol. (a) What is the ΔG°′ of the coupled reaction? (b) Estimate its equilibrium constant at 298 K.

(a) ΔG°′ = +13.8 + (−30.5) = −16.7 kJ/mol. (b) K′eq = exp(−ΔG°′ / RT) = exp(16,700 / (8.314 × 298)) = exp(6.74), which is roughly 850. The coupled reaction goes strongly forward, whereas K′eq for the uncoupled reaction is very small (exp(−5.57), about 0.004).

**Worked Example 2: ΔG in the cell (skill: reasoning)**

In a cell at 310 K, [ATP] = 3.0 mM, [ADP] = 0.30 mM and [Pi] = 2.0 mM. Using ΔG°′ = −30.5 kJ/mol, calculate ΔG for ATP hydrolysis. Why does it differ from ΔG°′?

Q = [ADP][Pi] / [ATP] = (0.00030 × 0.0020) / 0.0030 = 2.0 × 10⁻⁴. RT at 310 K is 2.58 kJ/mol, and ln Q = −8.52, so RT ln Q = −21.9 kJ/mol. ΔG = −30.5 − 21.9 = about −52 kJ/mol. It is more negative than ΔG°′ because the cell keeps ATP high and ADP and Pi low, so Q is far below 1.

**Worked Example 3: Energy from redox (skill: connect Book 1, Lesson 17)**

Use E°′ = −0.32 V for NAD⁺/NADH and +0.82 V for O₂/H₂O. Calculate ΔG°′ per mole of NADH oxidized by O₂ (n = 2) and comment on the sign.

ΔE°′ = 0.82 − (−0.32) = 1.14 V. ΔG°′ = −nFΔE°′ = −(2)(96.485)(1.14) = about −220 kJ/mol. The sign is negative because electrons flow from the low-potential couple to the high-potential couple: the reaction is spontaneous. About 220 kJ/mol is more than seven times the free energy of ATP hydrolysis, which is why one NADH can support the synthesis of several ATP.

**Worked Example 4: Glycolysis bookkeeping (skill: pathway reasoning)**

Compute the net ATP and NADH when (a) glucose is converted to lactate; (b) one glucose unit from glycogen enters glycolysis as glucose 1-phosphate, which is converted to glucose 6-phosphate.

(a) ATP: 2 used, 4 made, so net 2. NADH: 2 made at step 6, 2 consumed by lactate dehydrogenase, so net 0 NADH; the end products are 2 lactate. (b) Glycogen phosphorylase cleaves a glucose unit with Pi, giving glucose 1-phosphate without spending ATP ([Lesson 6](chapter:9)), and the isomerization to glucose 6-phosphate costs no ATP. The hexokinase step (1 ATP) is skipped, so the net is 4 − 1 = 3 ATP per glucose unit.

**Worked Example 5: Why glucokinase tracks blood glucose (skill: Km, link to Book 1, Lesson 24)**

Treat hexokinase (Km 0.1 mM) and glucokinase (Km 8 mM) as simple Michaelis-Menten enzymes. Compare each enzyme's fraction of Vmax at blood glucose of 5 mM (fasting) and 10 mM (after a meal).

v/Vmax = [S] / (Km + [S]). Hexokinase: 5 / 5.1 = 0.98 and 10 / 10.1 = 0.99, effectively saturated, so a doubling of glucose changes its rate by about 1 percent. Glucokinase: 5 / 13 = 0.38 and 10 / 18 = 0.56, an increase of about 44 percent. The low-Km enzyme is insensitive to glucose in the physiological range, while the high-Km enzyme follows it, which fits a role as a sensor and a disposal pathway after a meal. (The real glucokinase curve is sigmoidal, so its response is, if anything, steeper.)

**More Praxis Tips**

Praxis Tip: The name of the enzyme often gives the job. A kinase transfers phosphate from ATP, a phosphatase removes it, a mutase moves a group within the molecule, an isomerase rearranges it, and a dehydrogenase removes hydrogen (hydride) to NAD⁺ or FAD.

Praxis Tip: Count carbons. Six carbons before step 4 and three carbons after it, which means that everything from step 5 on is doubled when counted per glucose.

Praxis Tip: Do the ledger the same way every time: ATP spent (2), ATP made (4), NADH made (2). Then adjust for the question, such as glycogen as the starting material or an inhibitor of a given step.

Praxis Tip: An enzyme that is inhibited by its own product is a local feedback loop (hexokinase and glucose 6-phosphate). An enzyme activated by an earlier intermediate is feed-forward (pyruvate kinase and fructose 1,6-bisphosphate).

Praxis Tip: If a poison blocks the electron transport chain, mitochondria can no longer reoxidize NADH. Cells that can ferment (via lactate dehydrogenase) keep glycolysis going at 2 ATP per glucose and lactate rises; cells that cannot ferment run out of NAD⁺ and glycolysis stalls. Keep asking where the NAD⁺ comes from.

Praxis Tip: "Spontaneous" means ΔG is negative; it says nothing about speed. A reaction with a very negative ΔG can still be slow without its enzyme (Book 1, Lesson 24).

**Common Mistakes**

- Using ΔG°′ to decide the direction of a reaction in the cell instead of ΔG.
- Saying that ATP has a "high-energy bond", as if breaking the bond released energy.
- Counting 4 ATP as the yield of glycolysis (that is the gross yield; the net is 2).
- Forgetting that two G3P are made per glucose.
- Saying that fermentation makes ATP beyond glycolysis, or that its purpose is to make lactate (its purpose is to regenerate NAD⁺).
- Confusing hexokinase and glucokinase: the liver enzyme is the high-Km one without product inhibition.
- Saying that PFK-1 is activated by ATP and citrate.
- Forgetting that NADPH, not NADH, is the main biosynthetic reductant.

**Checkpoint Questions**

1. A student states that ATP hydrolysis releases a large amount of energy because the terminal phosphoanhydride bond is exceptionally strong. Which correction is most accurate?
   A. The bond is exceptionally weak, and breaking it releases energy
   B. Hydrolysis is favorable mainly because charge repulsion is relieved and the products ADP and Pi are better stabilized by resonance and solvation
   C. ATP hydrolysis is unfavorable under cellular conditions and requires a coupled reaction to proceed
   D. The energy is stored in the adenine ring and released when it is removed

2. Reaction A → B has ΔG°′ = +6.0 kJ/mol. In a cell at which RT is 2.5 kJ/mol, [A] = 1.0 mM and [B] = 0.010 mM. In which direction does the reaction proceed under these conditions?
   A. Backward (B to A), because ΔG°′ is positive
   B. It is at equilibrium, because ΔG°′ is small
   C. Backward, because ΔG is about +17.5 kJ/mol
   D. Forward (A to B), because ΔG is about −5.5 kJ/mol

3. A liver cell contains abundant ATP and citrate. Which effect on glycolysis is expected?
   A. Inhibition of PFK-1, slowing the conversion of fructose 6-phosphate to fructose 1,6-bisphosphate
   B. Activation of PFK-1, because ATP is a substrate
   C. Activation of pyruvate kinase by citrate
   D. No effect, because regulation occurs only at the level of transcription

4. A cell extract is supplied with glucose, ATP, NAD⁺, ADP, Pi and all glycolytic enzymes. What is the net yield per glucose after the pathway runs through pyruvate?
   A. 2 pyruvate, 4 ATP and 4 NADH
   B. 1 pyruvate, 2 ATP and 1 NADH
   C. 2 pyruvate, 2 ATP and 2 NADH
   D. 2 pyruvate, 2 ATP and 2 FADH₂

5. Cells in an oxygen-free chamber are given glucose and an inhibitor of lactate dehydrogenase. Compared with untreated anaerobic cells, ATP production from glycolysis in the treated cells will fall because
   A. lactate is required as a substrate for step 1 of glycolysis
   B. pyruvate cannot be formed because pyruvate kinase requires lactate
   C. ADP can no longer be phosphorylated by the electron transport chain
   D. NADH cannot be reoxidized, so NAD⁺ is depleted and the glyceraldehyde 3-phosphate dehydrogenase step stalls

6. A researcher compares the uptake of glucose by liver and muscle cells at glucose concentrations of 5 mM and 15 mM. Muscle uptake is nearly the same at both, while liver uptake rises sharply. The most consistent explanation is that
   A. the liver lacks any enzyme to phosphorylate glucose
   B. muscle phosphorylates glucose with a low-Km hexokinase that is saturated at both levels, whereas the liver uses high-Km glucokinase
   C. muscle hexokinase has a high Km and responds to glucose
   D. glucokinase is inhibited by its own product glucose 6-phosphate, which accumulates in the liver

7. During a sprint, a muscle releases lactate into the blood. Which statement about its fate and the energy balance is correct?
   A. The liver can convert lactate to glucose, which consumes more ATP equivalents than the 2 ATP the muscle gained, so the cycle has a net energy cost
   B. Lactate is converted to glucose in the muscle, because muscle contains the full gluconeogenic pathway
   C. The cycle generates a net gain of ATP for the body, because the liver makes ATP during gluconeogenesis
   D. Lactate is exhaled in the breath as lactic acid

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **B.** The favorable ΔG arises from properties of the reactants and products, not from the strength of a single bond. (A breaking any bond requires energy, so this repeats the misconception; C hydrolysis of ATP is favorable in the cell and is what drives coupled reactions; D the adenine ring is not altered by hydrolysis.)
2. **D.** Q = 0.010 / 1.0 = 0.010, so ΔG = 6.0 + 2.5 ln(0.010) = 6.0 − 11.5 = −5.5 kJ/mol, which is negative. (A the sign of ΔG°′ does not decide direction when concentrations are far from standard; B the reaction is at equilibrium only if ΔG equals zero; C inverts Q (using reactant over product); the correct ratio is 0.010, not 100.)
3. **A.** High ATP and citrate signal an energy-rich, precursor-rich cell, so PFK-1, the main control point, is inhibited. (B ATP is a substrate but at an allosteric site it inhibits; C citrate does not activate pyruvate kinase, and the energy state argues for slowing glycolysis; D PFK-1 is allosterically regulated on a short time scale.)
4. **C.** The investment phase spends 2 ATP and the payoff phase makes 4 ATP, giving a net of 2, plus 2 NADH at step 6. (A the gross ATP is 4, but 2 are spent, and the NADH count is 2 not 4; B one glucose gives two pyruvate because the six-carbon molecule is split into two three-carbon molecules; D glycolysis uses NAD⁺, not FAD, at its single oxidation step.)
5. **D.** Fermentation exists to regenerate NAD⁺, and without it step 6 runs out of its oxidizing cofactor. (A lactate is a product, not a substrate of step 1; B pyruvate kinase does not use lactate; C the electron transport chain is not required for the substrate-level steps and is not active anaerobically in any case.)
6. **B.** Low-Km hexokinase is already near Vmax at 5 mM, while high-Km glucokinase tracks glucose. (A the liver does phosphorylate glucose, using glucokinase; C a high Km would make the enzyme respond strongly to glucose, as in the liver; D this is a property of hexokinase, not glucokinase.)
7. **A.** Gluconeogenesis in the liver costs about 6 ATP equivalents per glucose, more than the 2 ATP gained by muscle glycolysis. (B this is not generally the case; the Cori cycle depends on the liver; C gluconeogenesis consumes ATP and GTP rather than producing them; D lactate is not removed by respiration; the carbon returns to glucose or is oxidized.)

Praxis Tip: After the checkpoint questions, write one sentence for each miss in the form "I confused X with Y because...". Log it in your error log ([Strategy: Learning Pathways and Systems Without Rote Memory](chapter:2)).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "The direction of a reaction in the cell is set by ΔG, which is ΔG°′ plus RT ln Q, and cells use ATP, whose hydrolysis is favorable because of charge relief and product stabilization, to drive unfavorable reactions by coupling; glycolysis turns glucose into two pyruvate with a net of 2 ATP and 2 NADH, is controlled at hexokinase, PFK-1 (the committed step) and pyruvate kinase by energy-state signals and hormones, and depends on fermentation to regenerate NAD⁺ when mitochondria cannot."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 1 and 4 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set that includes Book 1, Lessons 14, 17 and 24 and [Lesson 1](chapter:4)), and after 21 days (draw the pathway with regulators from memory).

*Interleave:* alternate a free-energy calculation with a pathway-regulation question and an enzyme kinetics question. Then move to [Lesson 5](chapter:8), the TCA cycle and oxidative phosphorylation.

Praxis Tip: End each study session by drawing the ten intermediates of glycolysis on scratch paper, marking the three irreversible steps, the two ATP investments, the two ATP-yielding steps and the NADH step.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Arithmetic checked in Python: 13.8 − 30.5 = −16.7 kJ/mol; K′eq about 850; ΔG of ATP hydrolysis at the example concentrations about −52.4 kJ/mol (RT 2.58 kJ/mol at 310 K); ΔG°′ for NADH oxidation about −220 kJ/mol; sigmoid-free Michaelis-Menten fractions 0.98, 0.99, 0.38, 0.56.
- Answer key positions: B, D, A, C, D, B, A.
- Verify with a biochemistry reviewer: ATP in-cell ΔG range; phosphoryl-transfer table values; hexokinase and glucokinase Km values; details of the fructose 2,6-bisphosphate system (PFK-2/FBPase-2 and hormones); glucagon and liver pyruvate kinase; Cori cycle ATP-equivalent cost; fructose entry below PFK-1; enzyme names for steps 2 to 9.
- Category 1D topics covered: principles of bioenergetics (free energy, ATP, coupling, redox carriers), glycolysis (steps, regulation, net yield, fermentation, tissue-specific hexokinase and glucokinase), Cori cycle.
