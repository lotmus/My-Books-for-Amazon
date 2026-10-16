# Strategy: Reading Biology Experiments

**What you will be able to do**

- Read a biology experiment in a fixed order and identify its controls, variables and what the result can and cannot show.
- Interpret gels and blots that are described in text, including loading controls.
- Reason about knockouts, knockdowns, rescue experiments and dose-response data.
- Predict the outcome of a perturbation, and infer pathway order from perturbation data.

**Why it matters**

Experiment passages are the main business of this section. Book 1 gave a general reading order for experiments and graphs (Book 1, Chapter 6; [Core Test Skills, Chapters 17 and 18]). This chapter adds the tools biology uses: gels, blots, gene knockouts, dose-response and signaling pathways. The questions rarely ask for a protocol from memory. They ask what a described result means, what control is missing, or what you would expect if one thing changed.

Praxis Tip: Ask "what would happen if this step were blocked?" for every figure. It converts a figure into a prediction, and a prediction is exactly what the exam asks you to test.

**A reading order for biology experiments**

1. **The question.** What is the experiment trying to find out? Put it in one sentence.
2. **The system.** Cells, tissue, whole organism, purified protein?
3. **The manipulation.** What was changed: a drug, a mutation, a knockout, a dose?
4. **The measurement.** What was read out: growth, band intensity, fluorescence, activity?
5. **The controls.** What comparison tells you the manipulation, and not something else, caused the change?
6. **The result and its pattern.** Say it in words before reading the question.
7. **The limit.** What does this result not show?

**Controls**

- **Negative control.** A condition where no effect is expected (no drug, an inactive version, an empty vector). It shows the background.
- **Positive control.** A condition where an effect is known to occur. It shows the method works; if it fails, a negative result elsewhere is uninterpretable.
- **Vehicle control.** The solvent or carrier alone, given to the control group, to show the solvent has no effect.
- **Loading control.** In blots, a protein expected to be unchanged (often a housekeeping protein), used to confirm equal amounts of sample were loaded.
- **Wild-type comparison.** For mutants, the unmodified organism or cell line studied in parallel.

Praxis Tip: For any "which control is missing" question, find the one thing the experimental group has beyond the manipulation (a solvent, a vector, a handling step) and ask which group would isolate it.

**Gels and blots described in text**

Passages often describe a gel in words: "bands at 50 and 25 kilodaltons" or "fragments of 3,000, 1,200 and 500 base pairs." You need only the logic.

| Method | What it separates | Key point |
|---|---|---|
| Agarose gel | DNA or RNA by size | Smaller moves farther |
| SDS-PAGE | Proteins by size | Smaller moves farther |
| Southern blot | DNA | Probe finds a sequence |
| Northern blot | RNA | Shows mRNA amount |
| Western blot | Protein | Antibody finds a protein |

In all these gels, the sample migrates from the negative electrode toward the positive one because nucleic acids carry negative charge and SDS coats proteins with negative charge in proportion to size, so size, not charge, sorts them. [VERIFY] A thicker band generally means more material, but only compared within a blot and after the loading control is considered. Lane-to-lane comparisons of band intensity make sense only when equal amounts were loaded. Details of the techniques are in [Lesson 9](chapter:13).

**Worked Example 1: Reading a text-described gel**

*Setup.* A circular plasmid of 4,700 base pairs is cut with an enzyme that has three recognition sites on it. The gel shows three bands, at 3,000, 1,200 and 500 base pairs.

*Reasoning.* A circle cut at three sites gives three fragments, and the sizes must add to the plasmid: 3,000 + 1,200 + 500 = 4,700, a match. The smallest fragment (500) migrates farthest from the wells; the largest (3,000) travels least. If the same plasmid were cut at only one site, there would be a single band at 4,700. If a student sees bands totaling more than 4,700, the digest is more likely a mixture of cut and partially cut DNA, or two different plasmids.

*Skill used:* checking that fragment sizes sum to the whole, and ordering them by size.

Praxis Tip: For any digest, add the fragments. If the sum does not equal the starting length, something is wrong with the picture, and that is often the question.

**Worked Example 2: A loading control rescues the interpretation**

*Setup.* Cells are treated with a drug, and a Western blot measures protein X in control and treated cells. Band intensities (arbitrary units): control X = 100, treated X = 60. The loading control (a housekeeping protein) reads control = 100, treated = 50.

*Reasoning.* Raw X fell by 40 percent (100 to 60), but the loading control says half as much sample was loaded in the treated lane. Normalize: control 100 / 100 = 1.0; treated 60 / 50 = 1.2. After correction, protein X rose by about 20 percent: (1.2 − 1.0) / 1.0 = 0.20.

*Reading the result.* The raw band suggested the drug decreased X; the normalized result suggests a modest increase. The loading control reverses the conclusion. It is why every blot question that mentions one is a hint.

*Skill used:* normalizing a band to a loading control before comparing lanes.

**Knockouts, knockdowns, overexpression and rescue**

- **Knockout.** The gene is removed or disrupted, so ideally no functional protein is made.
- **Knockdown.** The amount of the gene product is reduced, often by interfering with its mRNA, so some protein usually remains.
- **Overexpression.** More of the product than normal is made.
- **Rescue.** The missing gene is put back (or a variant is added) in the knockout. If the phenotype returns to normal, the effect was caused by loss of that gene and not by something else.

Two cautions are repeated across experiments. First, a knockdown that reduces protein by 80 percent still leaves 20 percent, so the remaining protein may mask the effect of loss. Second, the gene may affect other things, so a rescue is the best evidence that the phenotype is specific.

**Worked Example 3: A rescue experiment**

*Setup.* Cells lacking gene G (a knockout) grow at half the normal rate. Adding back a normal copy of G returns growth to normal. Adding back a version of G with a mutation that destroys its catalytic site does not restore growth.

*Reasoning.* The slow growth is due to the absence of G, because adding back normal G fixes it. Because the catalytically dead version fails, the catalytic activity of the G protein, and not just its presence as a physical scaffold, appears needed for normal growth. A careful statement: "consistent with G's catalytic activity being required." Not: "G's activity is the only thing G does."

*Skill used:* choosing the conclusion that matches what the rescue shows.

**Dose-response**

A dose-response curve shows an effect against a drug or signal concentration, usually with concentration on a log axis. It generally rises, then levels off at a maximum when all targets are occupied. The **EC50** (or IC50 for inhibitors) is the concentration giving half the maximal effect, and is a measure of potency: lower value, more potent. Maximal effect (efficacy) is a separate property. A reversible competitive inhibitor of a receptor generally shifts the curve to the right, raising the apparent EC50, while the maximum is still reachable at high dose.

**Worked Example 4: Estimating EC50**

*Setup.* A signaling molecule is applied to cells and the response measured as a percent of the maximal response: 1 nM gives 5 percent; 10 nM gives 20 percent; 100 nM gives 50 percent; 1,000 nM gives 90 percent; 10,000 nM gives 100 percent.

*Reasoning.* Half of the maximum is 50 percent, reached at 100 nM, so EC50 is about 100 nM. If an antagonist is added and 50 percent response now needs 1,000 nM, the EC50 increased tenfold while the maximum (100 percent at high dose) is unchanged, consistent with reversible competitive antagonism.

*Reading the curve.* Equal steps on a log axis are equal multiplications, not equal additions. The response rose by about 15 percentage points from 1 to 10 nM but by 30 from 10 to 100 nM: the curve is steepest near the middle.

*Skill used:* reading potency from a log-scale curve.

**Predicting perturbations and ordering a pathway**

When a pathway is a chain (receptor, kinase A, kinase B, transcription factor, gene), perturbation data can tell you the order.

**Worked Example 5: Epistasis in a signaling chain**

*Setup.* A signal normally turns on a reporter gene. Cells lacking kinase A show no reporter even when the signal is present. Cells lacking kinase B also show none. A constitutively active (always on) form of kinase B is introduced. In cells lacking kinase A, the active B gives high reporter signal with no signal added. In cells lacking kinase B, an always-on A gives no reporter.

*Reasoning.* Active B rescues the loss of A, so B acts downstream of A: B can do its job without A. Active A cannot rescue the loss of B, so A requires B. The order is signal, then A, then B, then the reporter. The logic generalizes: a downstream activation overrides an upstream loss, and an upstream activation cannot override a downstream loss.

*Skill used:* ordering a pathway from epistasis data.

Praxis Tip: For a chain question, draw the chain in your notebook, then place each perturbation on it. Everything downstream of a block is lost; everything upstream is unaffected or piles up.

**More Praxis Tips**

Praxis Tip: Say the result aloud in plain English before reading the question: "when X is removed, growth drops by half and returns when X is replaced." If you cannot, you have not yet read the figure.

Praxis Tip: Look for the loading control and ask what the blot looks like if it is corrected for. Many conclusions in a passage are reversed by it.

Praxis Tip: "Consistent with" and "proves" are different words. Choose the answer that stays closest to what was measured.

Praxis Tip: Check the scale on every axis. A log axis turns equal steps into equal ratios, and a drop that looks small can be tenfold.

Praxis Tip: When a result surprises you, check the controls before the biology. Missing, failed or confounded controls explain more surprises than new biology does.

**Checkpoint Questions**

1. On a Western blot, which molecule is detected?
   A. DNA, using a labeled probe
   B. RNA, using a labeled probe
   C. Lipids, using a dye
   D. Protein, using an antibody

2. In an agarose gel, a digest produces fragments of 2,000, 800 and 200 base pairs. Which fragment migrates farthest from the wells?
   A. The 2,000 base pair fragment
   B. The 200 base pair fragment
   C. The 800 base pair fragment
   D. All three migrate the same distance

3. A Western blot shows protein X at 80 units in treated cells and 100 units in control cells, but the loading control is 40 in treated and 100 in control. After normalization, protein X in treated cells relative to control is
   A. 0.8-fold, a 20 percent decrease
   B. 0.4-fold
   C. 2.0-fold higher
   D. unchanged

4. Compared with a knockout, an RNA-interference knockdown that reduces a protein by 85 percent most likely
   A. leaves some protein, so a mild phenotype may reflect residual function
   B. removes the gene from the genome
   C. produces exactly the same result as a knockout in every case
   D. increases the amount of the protein

5. Cells lacking gene G show a defect that disappears when a normal copy of G is added back. This rescue best supports the conclusion that
   A. G is the only gene involved in the process
   B. the defect was caused by an unrelated chemical in the medium
   C. G is dispensable
   D. the defect is caused by the loss of G

6. A drug has an EC50 of 20 nM in the absence of an inhibitor and 200 nM in its presence, with the same maximum response. Which statement is best supported?
   A. The inhibitor reduces apparent potency tenfold without lowering the maximum, consistent with competition
   B. The inhibitor lowers the maximum response
   C. The inhibitor increases potency tenfold
   D. The inhibitor has no effect

7. In a signaling chain, constitutively active kinase B restores reporter expression in cells lacking kinase A, but active kinase A does not restore expression in cells lacking B. What is the order of action?
   A. B acts upstream of A
   B. A acts upstream of B
   C. A and B act in separate, unrelated pathways
   D. The order cannot be inferred from perturbation data

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **D.** Western blots detect proteins with antibodies. (A that describes a Southern blot; B that describes a Northern blot; C lipids are not the target of a Western blot.)
2. **B.** Smaller fragments pass through the gel matrix more easily and travel farther. (A the largest fragment migrates least; C it is intermediate in size and migrates a middle distance; D size determines migration distance.)
3. **C.** Treated: 80/40 = 2.0; control: 100/100 = 1.0; so the ratio is 2.0-fold. (A uses the raw values without normalizing; B uses only the loading control ratio (40/100); D would require equal normalized ratios.)
4. **A.** A knockdown is partial, so the remaining protein can obscure the effect of losing the gene. (B knockdown reduces product; it does not remove the gene; C residual protein can mask effects; D knockdown reduces, not increases.)
5. **D.** Restoring the gene restores normal behavior, which links the defect to G. (A a rescue shows G is required, not that nothing else is; B an unrelated cause would not be corrected by adding G; C the defect appeared when G was missing.)
6. **A.** A tenfold rise in EC50 with unchanged maximum is the pattern expected for reversible competitive inhibition. (B the maximum is stated to be the same; C a higher EC50 means lower potency; D the EC50 changed tenfold.)
7. **B.** A downstream activation rescues an upstream loss, but an upstream activation cannot rescue a downstream loss. (A reverses the order the data indicate; C B bypasses the loss of A, suggesting connection; D this is the standard way to infer order.)

Praxis Tip: When you miss a data question, tag the slip: misread axis, ignored control, direction reversed, or over-concluded. Over-concluding is the most common.

**Common mistakes**

- Comparing band intensity across lanes without checking loading.
- Treating a knockdown as if it were a complete knockout.
- Concluding "proves" from a result that is only consistent with a hypothesis.
- Misreading a log axis as linear.
- Forgetting that a rescue is what shows the phenotype is due to that gene.
- Ordering a pathway backward: upstream and downstream are reversed.

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "I read an experiment by its question, system, manipulation, measurement and controls; I check loading controls before comparing bands; I remember that knockdowns leave some protein and rescues show specificity; I read potency off a log dose-response curve; and I order a pathway by seeing which perturbations override which."

*Review schedule:* redo Worked Examples 2 and 5 with new numbers after 1 day; after 3 days, explain controls from a blank page; after 7 days, apply the reading order to a figure in a later lesson; after 21 days, teach a friend the epistasis logic.

*Interleave:* alternate with [Strategy: Learning Pathways](chapter:2) so that your pathway maps and your perturbation logic reinforce each other, and apply both in [Lesson 9](chapter:13).

**Do this today**

1. Take a figure from any biology source and write the seven-step reading order for it in your notebook.
2. Sketch a gel from a text description of three fragments.
3. Redo Worked Example 2 with different numbers.
4. Draw a three-step pathway and place a knockout on it.

**Recap**

Read the question, system, manipulation, measurement, controls and result before the question. Normalize blots to loading controls, remember that knockdowns are partial and rescues show specificity, read potency from the middle of a log curve, and order pathways by which perturbations override which. Stay close to the data.

---

**Author verification note (remove before publishing)**

- All data, examples and questions are original. Verified: 3,000 + 1,200 + 500 = 4,700; 60/50 = 1.2, 20 percent increase; EC50 shift from 100 to 1,000 nM is tenfold.
- Biology claims to check with a reviewer: gel migration description; SDS-PAGE charge statement; competitive antagonism shifts EC50 to the right with unchanged maximum; knockdown versus knockout definitions; epistasis reasoning.
- Answer key positions: D, B, C, A, D, A, B.
- Category coverage: 1B (techniques), 2A, 2C (signaling); skills 3 and 4.
