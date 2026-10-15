# Lesson 5: The TCA Cycle and Oxidative Phosphorylation

**What you will be able to do**

- Describe the pyruvate dehydrogenase reaction, its cofactors and its regulation.
- Trace the TCA cycle from acetyl-CoA to oxaloacetate, naming the steps that make NADH, FADH₂, GTP and CO₂, and state the yield per turn and per glucose.
- Explain how the electron transport chain builds a proton gradient and how ATP synthase uses it.
- Estimate ATP yield from glucose with P/O ratios, and explain why textbook numbers differ.
- Predict the effect of inhibitors and uncouplers on oxygen use, ATP synthesis, and the redox state of the carriers.
- Describe mitochondrial structure and the shuttles that move NADH equivalents and ATP across the inner membrane.

**Why it matters for the exam**

Category 1D is one of the most heavily tested areas of the section, and oxidative phosphorylation is its favorite hard topic. Passages here almost always give you an experiment (an oxygen electrode trace, an inhibitor, a mutant enzyme) and ask what happens next. You will rarely need to recite the cycle; you will often need to say which carriers pile up when something is blocked. This lesson builds on [Lesson 4](chapter:7) (ATP, free energy, glycolysis) and on the redox and free-energy ideas of Book 1, Lessons 14 and 17. The control logic of these pathways, and how they fit with fat and amino acid metabolism, continues in [Lesson 6](chapter:9).

Praxis Tip: Think of this lesson as one story: carbon is burned to CO₂ in the matrix, the electrons are handed to carriers (NADH, FADH₂), and the carriers pay the electrons into a chain that runs downhill to oxygen and builds a gradient that makes ATP. Every question is about one link of that story.

**Concept Review**

**Pyruvate dehydrogenase (PDH).** Pyruvate from glycolysis enters the mitochondrial matrix (via a carrier in the inner membrane) and is converted to acetyl-CoA:

pyruvate + CoA + NAD⁺ → acetyl-CoA + CO₂ + NADH

This is an oxidative decarboxylation catalyzed by the **pyruvate dehydrogenase complex**, a large assembly of three enzymes (E1, E2, E3) with five cofactors: thiamine pyrophosphate (TPP), lipoic acid, CoA, FAD and NAD⁺. Vitamin links: thiamine (B₁), riboflavin (B₂, for FAD), niacin (B₃, for NAD⁺) and pantothenate (B₅, for CoA). The reaction is essentially **irreversible** in cells. Consequence: animals cannot convert acetyl-CoA back to pyruvate, so **fatty acids (which give acetyl-CoA) cannot be turned into net glucose** ([Lesson 6](chapter:9)).

PDH is regulated in two ways. First, **product inhibition**: acetyl-CoA and NADH inhibit the complex directly. Second, **covalent modification**: PDH kinase phosphorylates (and inactivates) the complex and is stimulated by ATP, acetyl-CoA and NADH, and inhibited by pyruvate and ADP. PDH phosphatase removes the phosphate and activates the complex; it is generally stimulated by Ca²⁺ and by insulin. [VERIFY] In plain language: when the cell is energy-rich, PDH is switched off; when pyruvate is plentiful and energy is needed, it is switched on. A deficiency of thiamine or poisoning by arsenic (which binds lipoic acid) causes pyruvate and lactate to accumulate. [VERIFY]

**The TCA cycle (citric acid or Krebs cycle).** The cycle runs in the **mitochondrial matrix**. Acetyl-CoA (2 carbons) condenses with oxaloacetate (4 carbons) to make citrate (6 carbons). Two carbons are then lost as CO₂, and oxaloacetate is regenerated. The steps, in order:

| Step | Enzyme | What is made |
|---|---|---|
| Acetyl-CoA + OAA → citrate | Citrate synthase | Citrate |
| Citrate → isocitrate | Aconitase | Isocitrate |
| Isocitrate → α-ketoglutarate | Isocitrate DH | NADH, CO₂ |
| α-Ketoglutarate → succinyl-CoA | α-KG DH complex | NADH, CO₂ |
| Succinyl-CoA → succinate | Succinyl-CoA synthetase | GTP (or ATP) |
| Succinate → fumarate | Succinate DH | FADH₂ |
| Fumarate → malate | Fumarase | none |
| Malate → oxaloacetate | Malate DH | NADH |

**Yield per turn (per acetyl-CoA):** 3 NADH, 1 FADH₂, 1 GTP (or ATP, by substrate-level phosphorylation) and 2 CO₂. Because one glucose gives **two** acetyl-CoA, the cycle turns twice per glucose, so PDH plus the cycle together give, per glucose, 6 CO₂ (2 from PDH and 4 from the cycle), 8 NADH (2 from PDH and 6 from the cycle), 2 FADH₂ and 2 GTP. The cycle itself makes almost no ATP directly; its job is to load electron carriers. It needs oxygen only indirectly, because the carriers must be reoxidized by the electron transport chain; without O₂ the NADH backs up and the cycle stalls.

Two details are often tested. First, **succinate dehydrogenase** is the only cycle enzyme embedded in the inner membrane, and it is also **Complex II** of the electron transport chain. Second, the two carbons lost as CO₂ in a given turn come from the oxaloacetate part of citrate, not from the acetyl group that just entered; the acetyl carbons are lost in later turns. A carbon-labeling question can hinge on this.

**Regulation of the cycle.** Control is mostly by energy state and by the supply of NAD⁺. **Isocitrate dehydrogenase** is inhibited by ATP and NADH and activated by ADP and Ca²⁺. The **α-ketoglutarate dehydrogenase complex** is inhibited by its product succinyl-CoA and by NADH, and activated by Ca²⁺. **Citrate synthase** is inhibited by citrate and ATP, and also depends on the supply of oxaloacetate and acetyl-CoA. [VERIFY] The big picture: a high NADH/NAD⁺ ratio (energy and electrons plentiful) slows the cycle; a high ADP/ATP ratio speeds it up. Because the cycle is cyclic, its intermediates are used as building blocks (citrate for fatty acids, α-ketoglutarate and oxaloacetate for amino acids, succinyl-CoA for heme). Replenishing them is called **anaplerosis**; the main route is **pyruvate carboxylase**, which makes oxaloacetate from pyruvate (biotin-dependent, activated by acetyl-CoA).

Praxis Tip: When an intermediate is removed for biosynthesis, the cycle slows unless oxaloacetate is replenished. If a question mentions biotin deficiency or a pyruvate carboxylase defect, think "low oxaloacetate."

**The electron transport chain (ETC).** The chain is a set of protein complexes and two mobile carriers in the **inner mitochondrial membrane**. Electrons pass from carriers of low reduction potential to carriers of higher reduction potential, ending at O₂, which is reduced to water. Each step releases free energy, and at three steps the energy is used to pump protons out of the matrix.

| Complex | Reaction | Pumps H⁺? | Inhibited by |
|---|---|---|---|
| I (NADH dehydrogenase) | NADH → CoQ | Yes | Rotenone, amytal |
| II (succinate DH) | FADH₂ → CoQ | No | Malonate (at succinate DH) |
| III (cytochrome bc₁) | CoQH₂ → cyt c | Yes | Antimycin A |
| IV (cytochrome c oxidase) | cyt c → O₂ → H₂O | Yes | Cyanide, azide, CO |

The mobile carriers are **coenzyme Q (ubiquinone)**, a lipid-soluble molecule that diffuses within the membrane and collects electrons from Complexes I and II, and **cytochrome c**, a small soluble protein in the intermembrane space that carries electrons from III to IV. The complexes use iron-sulfur clusters, flavins and heme groups (cytochromes) to pass single electrons. Only Complex IV reacts with O₂, taking four electrons to reduce one O₂ to two H₂O. Oxygen is the **final electron acceptor**; this is why oxygen is needed for the whole pathway.

A common estimate is that about 10 protons are pumped per NADH (Complexes I, III and IV) and about 6 per FADH₂ (III and IV only, since Complex II pumps none). [VERIFY] Because FADH₂ enters after Complex I, it drives less pumping and yields less ATP than NADH.

The free energy available follows from the difference in reduction potential (Book 1, Lesson 17):

ΔG°′ = −nFΔE°′

with n = 2 electrons and F = 96.5 kJ/(V·mol). For NADH to O₂, ΔE°′ is about 0.82 − (−0.32) = 1.14 V, so ΔG°′ is about −220 kJ per mole of NADH. [VERIFY] That is far more than the roughly 30 kJ needed to make one ATP, which is why the energy is released in small steps and captured as a proton gradient.

**Chemiosmosis and ATP synthase.** The proton pumping makes the intermembrane space more acidic and positive relative to the matrix. This **proton motive force** has two parts: a chemical part (a pH difference, ΔpH) and an electrical part (a membrane potential, Δψ, matrix negative). Protons flow back through **ATP synthase** (Complex V), down their gradient. ATP synthase has two parts: **F₀**, the proton channel embedded in the membrane with a rotating ring of c subunits, and **F₁**, the catalytic head in the matrix. Proton flow turns the ring and a central stalk, and the rotation forces conformational changes in three catalytic sites (the **binding-change mechanism**), driving ATP formation and release. Importantly, the energy input is used mainly to release the tightly bound ATP, not to form the bond itself.

Oxidation and phosphorylation are **coupled**: electron transport proceeds only if protons can return, which usually means only if ADP is available to be phosphorylated. This is **respiratory control** (acceptor control). A resting cell with high ATP and low ADP has a steep gradient and slow electron flow; a working cell with high ADP drains the gradient and speeds up the chain and oxygen consumption.

**Uncouplers and inhibitors.** These are classic passage material.

| Agent | Target | O₂ use | ATP made |
|---|---|---|---|
| Rotenone, antimycin A, cyanide, CO | ETC complex | Falls | Falls |
| Oligomycin | ATP synthase (F₀) | Falls | Falls |
| 2,4-Dinitrophenol (DNP) | Carries H⁺ across membrane | Rises | Falls |
| UCP1 (thermogenin) | Natural H⁺ leak | Rises | Falls |

An **ETC inhibitor** stops electron flow: carriers upstream of the block become fully reduced, carriers downstream become oxidized, the gradient collapses, and ATP synthesis stops. **Oligomycin** blocks the proton channel of ATP synthase; the gradient builds up until it opposes further pumping, so electron flow and O₂ use also fall (respiratory control). An **uncoupler** such as DNP is a lipid-soluble weak acid that shuttles protons across the membrane, bypassing ATP synthase. The gradient is dissipated, so the chain runs faster and O₂ consumption rises, but little ATP is made and the energy is released as **heat**. **Brown fat** uses the protein **UCP1** to do the same thing on purpose, producing heat in newborns and in cold adaptation. Cyanide and azide bind the heme iron of Complex IV, and carbon monoxide also inhibits it; the cell cannot use oxygen even though oxygen is present, so cells shift to glycolysis and lactate rises. [VERIFY]

Praxis Tip: For any inhibitor question, ask three things in order. Where is the block? What piles up before it (reduced carriers) and what runs short after it (oxidized carriers)? Does the gradient rise or fall? Oxygen consumption follows from the gradient.

**ATP yield and P/O ratios.** The **P/O ratio** is the number of ATP made per oxygen atom reduced, i.e., per pair of electrons. Using about 4 protons per ATP (3 through ATP synthase and 1 to import phosphate and exchange ATP for ADP), 10 protons per NADH give about 2.5 ATP (P/O about 2.5), and 6 per FADH₂ give about 1.5 ATP. [VERIFY] Older textbooks use 3 and 2, giving totals of 36 to 38 per glucose; modern estimates give about 30 to 32. Exam questions normally supply the values they want, so use the numbers in the passage if they are given. Using 2.5 and 1.5, the per-turn yield of the cycle is 3(2.5) + 1.5 + 1 = 10 ATP per acetyl-CoA.

Glucose yield (aerobic, malate-aspartate shuttle): glycolysis nets 2 ATP and 2 NADH; PDH makes 2 NADH; the cycle makes 6 NADH, 2 FADH₂ and 2 GTP. That is 10 NADH, 2 FADH₂ and 4 ATP-equivalents made by substrate-level phosphorylation. Total: 10(2.5) + 2(1.5) + 4 = 32 ATP. [VERIFY]

**Mitochondrial structure and transport.** The **outer membrane** is permeable to small molecules through porins. The **inner membrane** is highly folded into **cristae** (which increase the surface area for the ETC), is rich in the lipid cardiolipin, and is impermeable to most ions and polar molecules, which is what lets it hold a gradient. The **intermembrane space** is where protons accumulate and cytochrome c sits. The **matrix** holds PDH, the TCA enzymes, fatty acid oxidation enzymes, mitochondrial DNA and ribosomes (consistent with the endosymbiotic origin; [Lesson 12](chapter:17)). Cytochrome c released into the cytosol also helps trigger apoptosis ([Lesson 13](chapter:18)).

Transport across the inner membrane needs carriers. The **ADP/ATP translocase** exchanges matrix ATP for cytosolic ADP, and a phosphate carrier brings in Pi along with a proton; these two processes use part of the proton motive force (hence the "1" in the 4 protons per ATP above). NADH made in the cytosol by glycolysis cannot cross the inner membrane, so its electrons enter by **shuttles**:

- **Malate-aspartate shuttle** (liver, heart): cytosolic NADH reduces oxaloacetate to malate, which enters the matrix and regenerates **NADH** there. About 2.5 ATP per cytosolic NADH.
- **Glycerol-3-phosphate shuttle** (skeletal muscle and brain; [VERIFY]): cytosolic NADH reduces DHAP to glycerol-3-phosphate, which is oxidized by an enzyme in the inner membrane that reduces **FAD to FADH₂**, entering at coenzyme Q. About 1.5 ATP per cytosolic NADH.

Using the glycerol-3-phosphate shuttle, the two glycolytic NADH count as FADH₂ equivalents and the glucose total becomes 8(2.5) + 4(1.5) + 4 = 30 ATP.

**Worked Example 1: Counting per glucose (skill: bookkeeping)**

How many NADH and FADH₂ are made from one glucose between glucose and CO₂, and how many CO₂ are released?

Glycolysis: 2 NADH. PDH (twice): 2 NADH and 2 CO₂. TCA (two turns): 6 NADH, 2 FADH₂, 2 GTP and 4 CO₂. Totals: 10 NADH, 2 FADH₂ and 6 CO₂. The six carbons of glucose are all released as CO₂, as expected for complete oxidation.

**Worked Example 2: ATP yield with an altered shuttle (skill: assumptions)**

A passage states that each NADH yields 2.5 ATP, each FADH₂ yields 1.5 ATP, and substrate-level phosphorylation gives 4 ATP per glucose. Compare muscle (glycerol-3-phosphate shuttle) with liver (malate-aspartate shuttle).

Liver: 10(2.5) + 2(1.5) + 4 = 25 + 3 + 4 = 32 ATP. Muscle: the two cytosolic NADH count as 1.5 each, so 8(2.5) + 4(1.5) + 4 = 20 + 6 + 4 = 30 ATP. The difference is only the shuttle.

**Worked Example 3: Free energy from reduction potentials (skill: Book 1 link)**

Compute ΔG°′ for transfer of two electrons from NADH (E°′ = −0.32 V) to O₂ (E°′ = +0.82 V). Is the process spontaneous?

ΔE°′ = 0.82 − (−0.32) = 1.14 V. ΔG°′ = −nFΔE°′ = −(2)(96.5 kJ/(V·mol))(1.14 V) = about −220 kJ/mol. The sign is negative, so the process is spontaneous; the large magnitude is why the chain is divided into several steps.

**Worked Example 4: Reading an oxygen electrode experiment (skill: data reasoning)**

Isolated mitochondria are given succinate and ADP, and oxygen consumption is recorded. Adding oligomycin sharply decreases the rate. Adding DNP afterward restores a high rate. What is the interpretation?

With ADP present, electron flow is coupled to ATP synthase. Oligomycin blocks the F₀ channel, so protons cannot re-enter; the gradient builds and slows the chain, and oxygen consumption falls. This shows that the electron transport was tightly coupled to ATP synthase. DNP provides a different route for protons, so the gradient collapses despite the blocked synthase; the chain, free of back-pressure, runs fast again. The rate recovers although no ATP is made. (Also notice that succinate feeds Complex II, so rotenone, a Complex I inhibitor, would not have stopped this experiment.)

**Worked Example 5: Predicting redox state after a block (skill: perturbation)**

Cyanide is added to cells in oxygen. What happens to cytochrome c, to the NADH/NAD⁺ ratio in the matrix, to the TCA cycle, and to lactate?

Complex IV is blocked, so electrons stop at cytochrome c, which becomes mostly reduced. Complexes upstream also back up, and coenzyme Q and NADH become more reduced. NAD⁺ is therefore in short supply, so PDH and the TCA dehydrogenases slow (they need NAD⁺ and are inhibited by NADH). ATP from oxidative phosphorylation falls, so the cell relies on glycolysis, regenerating NAD⁺ by making lactate, and lactate rises.

**More Praxis Tips**

Praxis Tip: Write the carrier tally per glucose on the first line of scratch paper: 10 NADH, 2 FADH₂, 4 substrate-level ATP-equivalents. Then plug in whatever P/O values the passage offers.

Praxis Tip: Oxygen consumption tracks the gradient, not the presence of oxygen. Inhibit the synthase and it drops; leak the membrane and it rises.

Praxis Tip: FADH₂ bypasses Complex I. If Complex I is blocked (rotenone), succinate can still feed the chain, but NADH-linked substrates cannot.

Praxis Tip: Name the cycle's electron-rich products in order: isocitrate, α-ketoglutarate and malate give NADH; succinate gives FADH₂. Three, then one.

Praxis Tip: A rolling trick for the cycle's carbons: 2 in as acetyl, 2 out as CO₂ over the turn, and the 4-carbon acceptor comes back.

Praxis Tip: The inner membrane is the barrier that makes the gradient possible; any agent that makes it leaky (uncouplers, detergents, membrane damage) lowers ATP yield.

**Common Mistakes**

- Saying the TCA cycle consumes oxygen directly, or that it makes most of the ATP.
- Forgetting that glucose gives two acetyl-CoA, so the cycle turns twice.
- Saying oligomycin raises oxygen consumption (it lowers it; an uncoupler raises it).
- Placing Complex II in the proton-pumping group.
- Treating the older figure of 36 to 38 ATP as the only correct answer instead of using the passage's values.
- Letting cytosolic NADH cross the inner membrane without a shuttle.
- Thinking cyanide kills by blocking the delivery of oxygen rather than its use.

**Checkpoint Questions**

1. A patient with severe thiamine deficiency would be expected to have elevated blood levels of
   A. acetyl-CoA, because its production is increased
   B. oxaloacetate, because the TCA cycle runs faster
   C. pyruvate and lactate, because TPP is needed by pyruvate dehydrogenase
   D. ATP, because glycolysis is blocked

2. Which statement about one complete turn of the TCA cycle, starting from one acetyl-CoA, is correct?
   A. It produces 3 NADH, 1 FADH₂, 1 GTP or ATP and releases 2 CO₂
   B. It produces 1 NADH, 3 FADH₂ and 1 GTP
   C. It produces 2 NADH, 2 FADH₂ and 2 CO₂ but no GTP
   D. It consumes O₂ directly and releases 4 CO₂

3. Which TCA cycle enzyme is also a component of the electron transport chain and is bound to the inner mitochondrial membrane?
   A. Isocitrate dehydrogenase
   B. Succinate dehydrogenase
   C. Malate dehydrogenase
   D. Citrate synthase

4. Isolated mitochondria with ADP and succinate consume oxygen at a steady rate. Adding oligomycin decreases the rate; subsequently adding 2,4-dinitrophenol raises it above the starting rate. The best interpretation is that
   A. oligomycin blocked Complex IV and DNP bypassed it
   B. DNP restored ATP synthesis, which restored oxygen consumption
   C. oligomycin caused the oxygen electrode to fail and DNP repaired it
   D. oligomycin blocked ATP synthase so the gradient rose and slowed the chain, while DNP dissipated the gradient and removed that back-pressure

5. A worker exposed to cyanide has a severe drop in ATP production. Which change is expected in mitochondria?
   A. Complex I becomes more oxidized because electrons are removed faster
   B. Cytochrome c and coenzyme Q become more reduced, and the proton gradient collapses
   C. Oxygen consumption rises because the gradient is steeper
   D. The TCA cycle speeds up because less NADH is available

6. Assume 2.5 ATP per NADH, 1.5 ATP per FADH₂ and 4 ATP from substrate-level phosphorylation per glucose. In a tissue using the glycerol-3-phosphate shuttle, how many ATP are made from one glucose oxidized completely?
   A. 32
   B. 26
   C. 30
   D. 36

7. Brown adipose tissue expresses UCP1. Compared with a tissue lacking UCP1, brown fat during cold exposure will show
   A. lower oxygen consumption and more ATP made per oxygen
   B. higher ATP made per oxygen, because protons are conserved
   C. unchanged oxygen consumption, because UCP1 affects only the matrix pH
   D. higher oxygen consumption and heat output, and less ATP made per oxygen consumed

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **C.** Thiamine pyrophosphate is a cofactor of PDH (and of α-ketoglutarate dehydrogenase). With PDH impaired, pyruvate accumulates and is diverted to lactate. (A acetyl-CoA production by PDH would fall, not rise; B the TCA cycle would slow, not speed up; D glycolysis is not blocked, and ATP supply would fall.)
2. **A.** The three NADH come from isocitrate DH, α-KG DH and malate DH; FADH₂ from succinate DH; GTP from succinyl-CoA synthetase. (B reverses the NADH and FADH₂ counts; C miscounts carriers and omits the substrate-level phosphorylation; D the cycle does not use O₂ directly, and a turn releases only 2 CO₂.)
3. **B.** Succinate dehydrogenase is Complex II, which passes electrons from FADH₂ to coenzyme Q. (A is a matrix enzyme and not part of the chain; C is a matrix enzyme that makes NADH; D is a matrix enzyme and does not oxidize anything.)
4. **D.** Oxygen consumption is limited by the proton gradient. An uncoupler removes the limit even when ATP synthase is blocked. (A a Complex IV block would not be reversed by a proton carrier; B DNP uncouples; it lowers ATP synthesis; C ignores the biological explanation and has no support.)
5. **B.** Cyanide blocks Complex IV. Electrons back up through the chain, upstream carriers are reduced, pumping stops and the gradient dissipates. (A electrons accumulate behind the block; C a blocked chain consumes less oxygen and the gradient falls; D NADH accumulates, and the cycle slows.)
6. **C.** Eight NADH (20) plus four FADH₂ (6; the two cytosolic NADH enter as FADH₂ equivalents) plus 4 gives 30 ATP. (A is the yield with the malate-aspartate shuttle; B drops both the FADH₂ and substrate-level contributions; D is the older textbook estimate with different P/O ratios.)
7. **D.** UCP1 lets protons leak back across the inner membrane, so the chain runs faster, the energy is released as heat and the P/O ratio falls. (A UCP1 increases oxygen use and lowers the yield per oxygen; B protons return without driving ATP synthase; C UCP1 changes the gradient and therefore the oxygen use.)

Praxis Tip: After the checkpoint questions, check each wrong choice and name its slip (wrong direction of change, wrong complex, wrong tally). Log it in your error log, then go to the [Practice: Biomolecules and Metabolism Set](chapter:10) when you have finished [Lesson 6](chapter:9).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "Pyruvate becomes acetyl-CoA in the matrix, the TCA cycle burns acetyl-CoA to CO₂ and loads three NADH and one FADH₂ per turn, those carriers feed an electron chain that pumps protons across the inner membrane and ends at oxygen, and ATP synthase uses the returning protons to make ATP, so inhibitors of the chain or synthase stop ATP and uncouplers burn the gradient as heat."

*Review schedule:* revisit this lesson after 1 day (redraw the TCA cycle with the NADH, FADH₂, GTP and CO₂ steps marked), after 3 days (redo Worked Examples 2 and 4 on a blank page), after 7 days (do the checkpoint questions mixed with [Lesson 4](chapter:7) glycolysis questions), and after 21 days (explain an oxygen electrode trace aloud).

*Interleave:* alternate a TCA question with a glycolysis regulation question and an enzyme inhibition question from Book 1, Lesson 24.

Praxis Tip: End each session by drawing the inner membrane with the four complexes, Q, cytochrome c and ATP synthase from memory, marking where protons go and where each inhibitor acts.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Arithmetic verified in code: ΔG°′ about −220 kJ/mol from 1.14 V; 10 NADH, 2 FADH₂, 4 substrate-level ATP-equivalents give 32 ATP (malate-aspartate) and 30 ATP (glycerol-3-phosphate); 10 ATP per turn.
- Answer key positions: C, A, B, D, B, C, D.
- Verify with a biochemistry reviewer: protons pumped per complex and per NADH/FADH₂; 4 H⁺ per ATP; modern 30 to 32 ATP yield; PDH kinase and phosphatase regulators; citrate synthase regulation; which tissues use the glycerol-3-phosphate shuttle; E°′ values; cyanide and CO wording; arsenic and lipoic acid.
- Category 1D topics covered: PDH and regulation, TCA cycle and regulation, ETC, chemiosmotic coupling, ATP synthase, P/O ratios, uncouplers and inhibitors, mitochondrial structure and shuttles.
