# Lesson 9: Laboratory Techniques in Molecular Biology

**What you will be able to do**

- Explain what PCR, qPCR, gel electrophoresis, blotting, ELISA, cloning, sequencing and CRISPR each do, and the principle behind each.
- Predict and interpret results described in text: how many copies PCR makes, what a lower Ct means, which band is bigger, which blot detects what.
- Choose the right technique for a question (DNA, RNA or protein; presence, size or amount).
- Interpret reporter-gene, knockout and knockdown experiments, including the controls that make the conclusion valid.
- Describe, at concept level, how microarrays and RNA-seq measure gene expression.

**Why it matters for the exam**

This lesson serves category 1B (transmission of genetic information) and is one of the most heavily tested places for skill 3 (research design) and skill 4 (data and graphs). Many passages in the section are built around one of these techniques, and you are rarely asked to perform the technique. You are asked to read what the experiment shows, spot what is missing, or predict what a change would do. The lesson builds on DNA structure ([Lesson 3](chapter:6)), replication ([Lesson 7](chapter:11)) and gene expression ([Lesson 8](chapter:12)), and it supplies the toolkit for the experiment-reading habits in [Strategy: Reading Biology Experiments](chapter:3).

Praxis Tip: For every technique, learn three things: what goes in (DNA, RNA or protein), what the principle is (size, sequence matching, antibody binding), and what a "positive" looks like in words (a band, a color, an earlier cycle). Passages describe the look; you supply the meaning.

**Concept Review**

**1. Amplifying DNA: PCR.** The **polymerase chain reaction** copies a chosen stretch of DNA exponentially in a test tube. The ingredients are template DNA, two **primers** (short single-stranded DNA oligonucleotides), the four deoxynucleotides (dNTPs), a **heat-stable DNA polymerase** (such as Taq polymerase) and buffer with Mg²⁺. The tube is cycled through three temperature steps:

- **Denaturation** (generally about 95 °C): heat separates the two strands.
- **Annealing** (generally about 50 to 65 °C, set by the primers' melting temperature): primers bind their complementary sequences, one on each strand, with their 3′ ends pointing toward each other.
- **Extension** (generally about 72 °C for Taq): the polymerase extends each primer 5′ → 3′, copying the template. [VERIFY typical temperatures]

The primers define the **amplicon**: the stretch between and including them. Each cycle ideally doubles the number of copies, and after the first few cycles the product of defined length dominates. In an ideal reaction:

copies after n cycles = starting copies × 2ⁿ

Real reactions fall short as reagents run out, so the curve eventually plateaus. Primers with more G and C have higher melting temperatures, because G–C pairs have three hydrogen bonds. A **no-template control** (all reagents, no DNA) should give no product; a band there means contamination. If you changed nothing but the primers, the product size would change, because the primers set the ends.

**Reverse transcription.** **Reverse transcriptase** makes a DNA copy (**cDNA**) from an RNA template. **RT-PCR** reverse-transcribes mRNA to cDNA and then amplifies it. Because cDNA is made from mature mRNA, it has no introns. With primers on either side of an intron, the cDNA product is shorter than the product from genomic DNA, which is a standard way to show that a band came from RNA and not from contaminating DNA.

**2. Quantifying DNA: qPCR.** In **quantitative (real-time) PCR** a fluorescent signal (from a dye that binds double-stranded DNA, or from a sequence-specific probe) is read every cycle. The **threshold cycle (Ct)** is the cycle at which fluorescence first rises above background. A reaction that starts with more template reaches the threshold sooner, so:

- **Lower Ct means more starting template.**
- With perfect doubling, a difference of 1 Ct is a 2-fold difference in starting amount; a difference of 3 Ct is 2³ = 8-fold.

To compare gene expression between conditions, the target gene's Ct is normalized to a **reference (housekeeping) gene** that does not change, which corrects for different amounts of starting material. The **ΔΔCt method** is:

ΔCt = Ct(target) − Ct(reference), in each sample
ΔΔCt = ΔCt(treated) − ΔCt(control)
fold change = 2^(−ΔΔCt)

A negative ΔΔCt means more target in the treated sample. A **melt curve** (slowly heating the product while reading fluorescence) checks that a single product was made.

**3. Separating molecules: gel electrophoresis.** An electric field pulls charged molecules through a porous gel.

- **Nucleic acids** carry a negative charge on every phosphate, so they migrate toward the positive electrode (anode). The charge-to-mass ratio is roughly constant, so the gel separates by **size**: smaller fragments move farther and larger fragments stay near the wells. DNA is generally run in **agarose** (larger fragments) or **polyacrylamide** (small fragments, high resolution).
- **Reading size:** run a **ladder** (fragments of known sizes) beside the samples. Over the useful range, the logarithm of fragment size is roughly linear in the distance migrated, so you estimate an unknown band by interpolating between ladder bands, never by simple proportion on the raw sizes.
- **Plasmid forms.** An uncut supercoiled plasmid generally runs faster than the same plasmid when cut once to linear form, and a nicked circle generally runs slowest. So one plasmid sample can give several bands even though it contains one sequence.
- **Proteins** are generally run in polyacrylamide. In **SDS-PAGE** the detergent SDS unfolds proteins and coats them with negative charge proportional to their length, so separation is by **mass** alone. A reducing agent (such as β-mercaptoethanol) breaks disulfide bonds. Thus a protein made of two 30 kDa subunits joined by a disulfide runs at about 60 kDa without a reducing agent and about 30 kDa with one. In **native PAGE** (no SDS) proteins keep their folding, and migration depends on charge, size and shape. **Isoelectric focusing** separates proteins by their pI in a pH gradient (Book 1, Lesson 23).

**4. Detecting one molecule in a mixture: blots.** A **blot** separates molecules on a gel, transfers them to a membrane, and detects one of them with a probe.

| Blot | Target | Probe |
|---|---|---|
| Southern | DNA | Labeled DNA or RNA |
| Northern | RNA | Labeled nucleic acid |
| Western | Protein | Antibody |

Southern and Northern blots use **hybridization**: the labeled probe finds its complementary sequence on the membrane. A Western blot uses an **antibody** that recognizes a particular protein, usually detected with a second, enzyme-linked antibody. Memory aid: the first two named blots point at nucleic acids, and the antibody blot is the protein one.

What each blot answers:

- **Southern:** is a sequence present, how many copies, did a restriction site change (a mutation can change fragment sizes), was a gene deleted?
- **Northern:** is a gene transcribed, how much, how long is the mRNA, are there different sizes (splice variants)?
- **Western:** is the protein present, how big is it, how much, is it modified (a phospho-specific antibody detects only the phosphorylated form)?

Band intensity gives approximate amount, but only after normalizing to a **loading control**, a protein or RNA expected to be constant (such as actin or a ribosomal RNA). If the loading control band is weaker in one lane, less sample was loaded, and the target must be corrected upward.

**5. Measuring protein in a plate: ELISA.** In an **enzyme-linked immunosorbent assay**, an antibody fixed to a plate captures the antigen from a sample. A second antibody carrying an enzyme binds the captured antigen (a "sandwich"), and the enzyme converts a substrate into a colored product. More antigen gives more color. Quantities are read from a **standard curve** made with known amounts. Controls: a blank (no antigen) sets background, and samples above the top standard must be diluted, because the signal saturates. ELISA tells you how much, not how big, and it can measure antibodies (to test for infection) as well as antigens.

**6. Cutting and pasting DNA: restriction enzymes and cloning.** **Restriction enzymes** cut DNA at specific short sequences, usually **palindromes** (the sequence on one strand 5′ → 3′ matches the other strand 5′ → 3′). EcoRI recognizes 5′-GAATTC-3′ and cuts between G and A on each strand, leaving short single-stranded overhangs called **sticky ends**. Any two fragments cut with the same enzyme can anneal at their sticky ends, and **DNA ligase** seals the backbone with phosphodiester bonds.

Cutting counts follow a simple rule:

- A **linear** DNA with n cut sites gives n + 1 fragments.
- A **circular** DNA (plasmid) with n cut sites gives n fragments (for n ≥ 1).

A **plasmid vector** is a small circular DNA that replicates in bacteria. A useful vector has an **origin of replication**, a **selectable marker** (often an antibiotic resistance gene), and a **multiple cloning site** (a cluster of restriction sites). The standard workflow is: cut vector and insert with the same enzymes, ligate, **transform** bacteria, and plate on antibiotic. Only cells that took up a plasmid carrying the resistance gene form colonies. Cutting with two different enzymes forces the insert in one orientation (**directional cloning**); cutting with a single enzyme lets the insert go in either orientation and lets the empty vector re-close on itself.

**Blue-white screening.** Many vectors carry part of the *lacZ* gene (which encodes β-galactosidase) with the multiple cloning site inside it. On plates containing the colorless substrate **X-gal** (and an inducer such as IPTG), cells with an intact *lacZ* make β-galactosidase, which cleaves X-gal to a blue product. If an insert interrupts *lacZ*, no active enzyme forms and the colony is **white**. So on antibiotic plus X-gal:

- no colonies: no plasmid was taken up;
- blue colonies: plasmid present, **no insert** (the vector re-closed);
- white colonies: plasmid present, **insert probably present**. Confirm with a restriction digest or PCR.

**7. Reading the sequence: DNA sequencing.** In **Sanger sequencing**, a reaction copies a template with polymerase, normal dNTPs, and a small amount of fluorescent **dideoxynucleotides (ddNTPs)**, which lack the 3′-OH and so end the chain when incorporated. The result is a set of fragments of every length, each ending in a labeled base. Sorting them by size (generally in a capillary) and reading the color of the end base from smallest to largest gives the sequence of the **newly synthesized** strand, 5′ → 3′. The template is its complement. **Next-generation sequencing** reads millions of short fragments in parallel; the reads are then aligned to a reference or assembled. The number of reads covering a position is the **coverage**, and higher coverage gives more confidence in each base.

**8. Editing genes: CRISPR-Cas9.** In the **CRISPR-Cas9** system, a **guide RNA** (about 20 nucleotides) base-pairs with the matching DNA target, next to a short required sequence called the **PAM**, and the **Cas9** nuclease cuts both strands there. The cell then repairs the break:

- **Non-homologous end joining (NHEJ)** joins the ends imperfectly and often adds or deletes a few bases. A deletion or insertion whose size is not a multiple of three shifts the reading frame, usually destroying the gene: a **knockout**.
- **Homology-directed repair (HDR)**: if the experimenter supplies a **donor template** with homologous ends, the cell copies it into the break, introducing a specific change or inserting a new sequence (a **knock-in**).

Controls include a non-targeting guide RNA and checking for **off-target** cutting at similar sequences. A catalytically "dead" Cas9 (dCas9) can still bind DNA without cutting, and is used to block or recruit regulators to a gene.

**9. Knockout versus knockdown.** A **knockout** removes or disrupts the gene itself, so the product is absent (in every cell for a germline knockout). A **knockdown** reduces expression without altering the gene, most often by **RNA interference**: a short interfering RNA (siRNA) or short hairpin RNA (shRNA) pairs with the target mRNA and directs its degradation or blocks translation ([Lesson 8](chapter:12)). Knockdowns are generally partial and often transient; knockouts of essential genes can be lethal, so **conditional** knockouts (turned on in one tissue or at one time) are used. Both are loss-of-function tools. Two good controls are a **scrambled/non-targeting** construct and a **rescue** experiment: put back a version of the gene that the tool cannot affect, and the phenotype should disappear. If it does not, the original effect may have been off-target.

**10. Reporter genes.** A **reporter** is a gene whose product is easy to measure, used either as a read-out of promoter activity or as a tag.

- **GFP** (green fluorescent protein) fluoresces under blue light without a substrate, so it works in living cells. Fusing GFP to a protein shows where the protein is (localization), though a big tag can disturb function.
- ***lacZ*** gives β-galactosidase, detected by blue color with X-gal (or a yellow product from another substrate).
- **Luciferase** produces light when given its substrate, and is very sensitive for measuring promoter strength.

In a **promoter-reporter** assay the promoter under study drives the reporter. Higher signal means more transcription from that promoter. Deleting or mutating a region of the promoter and finding that the signal falls shows that the region contributes to activity; showing that a protein binds that region needs a different experiment. Include a second, constant reporter to correct for how many cells took up the DNA.

**11. Measuring many genes at once: microarrays and RNA-seq.** A **microarray** is a chip with thousands of fixed DNA probes, one per gene. Labeled cDNA from a sample hybridizes to the probes, and spot brightness reflects how much of that transcript is present. Two samples can be labeled in two colors and compared. **RNA-seq** sequences the cDNA made from all the RNA in a sample and counts how many reads map to each gene. Counts are normalized for gene length and total reads, and the result is a fold change per gene. RNA-seq can detect transcripts you did not know to look for and splice variants; microarrays need known sequences. For both, a change in a transcript level is not proof of a change in protein level ([Lesson 8](chapter:12)), and the comparison needs biological replicates.

**Other techniques you may see described.** Chromatin immunoprecipitation uses an antibody to pull down a DNA-binding protein with the DNA it was bound to, showing where it binds. Co-immunoprecipitation uses an antibody to pull down a protein with the proteins stuck to it, showing interaction. Both are conceptual cousins of the antibody methods above: an antibody finds its antigen, and what comes with it tells you something.

**Reading each technique's result in words**

| Technique | Positive result | Unit of meaning |
|---|---|---|
| PCR | A band of the right size | Presence of the sequence |
| qPCR | Low Ct | Amount of starting template |
| Blot | A band at the probed position | Presence and size |
| ELISA | More color | Amount, via standards |

**Worked Example 1: How many copies? (skill: exponential amplification)**

A PCR starts with 100 copies of the target. How many double-stranded copies would an ideal reaction give after 10 cycles? If each cycle instead increased the amount only 1.9-fold, how many?

Ideal: 100 × 2¹⁰ = 100 × 1,024 = 102,400 copies. At 1.9-fold per cycle: 100 × 1.9¹⁰ ≈ 61,000 copies, about 60 percent of the ideal. A small loss of efficiency per cycle compounds, which is why efficiency matters for qPCR. If a passage reports that adding more cycles no longer increases the product, that is the plateau: reagents are limiting, not a failure of the design.

**Worked Example 2: Comparing expression by qPCR (skill: ΔΔCt)**

A gene's Ct is 24 in control cells and 21 in drug-treated cells. A reference gene has Ct 18 in both. What is the fold change?

ΔCt (control) = 24 − 18 = 6. ΔCt (treated) = 21 − 18 = 3. ΔΔCt = 3 − 6 = −3. Fold change = 2³ = **8-fold increase** in the treated cells. The reference gene having the same Ct in both shows equal input, so the change is due to the drug. Had the reference Ct been 19 in treated cells, the answer would change; always correct for it.

**Worked Example 3: Sizing a band on a gel (skill: log-linear interpolation)**

A DNA ladder runs as follows (distance from the well): 1,000 bp at 40 mm and 500 bp at 49 mm. An unknown fragment migrates 45 mm. Estimate its size.

It lies between the two ladder bands, so interpolate on the log scale. The unknown is (45 − 40)/(49 − 40) = 5/9 of the way from 1,000 toward 500. log₁₀(1,000) = 3.000 and log₁₀(500) = 2.699, a difference of 0.301. So log₁₀(size) = 3.000 − (5/9)(0.301) = 2.833, and size ≈ 10^2.833 ≈ **680 bp**. A plausible answer must lie between 500 and 1,000, and nearer 500, since the band is past the midpoint. (Simple proportion would give 750, which is why the log matters.) On the exam you would pick an answer in the right range, not compute logs.

**Worked Example 4: Restriction digests (skill: counting fragments)**

A circular plasmid of 5,000 bp has EcoRI sites at positions 400 and 2,100, and one BamHI site at position 1,000. Predict the fragments for EcoRI alone, BamHI alone, and both.

EcoRI alone: 2 sites in a circle gives 2 fragments: 2,100 − 400 = 1,700 bp and 5,000 − 1,700 = 3,300 bp. BamHI alone: 1 site gives 1 fragment, the linear 5,000 bp molecule. Both: 3 sites in a circle gives 3 fragments: 400 to 1,000 = 600 bp; 1,000 to 2,100 = 1,100 bp; and the rest, 5,000 − 2,100 + 400 = 3,300 bp. Check: 600 + 1,100 + 3,300 = 5,000. On a gel, the double digest shows three bands and the BamHI-only digest shows one large band that is larger than any other fragment.

**Worked Example 5: Cloning results and a Western blot (skill: reading outcomes and normalizing)**

(a) In a cloning experiment, 2 ng of a ligated plasmid is used to transform bacteria and the antibiotic plate gives 840 colonies. A control plate with no DNA gives none. What is the transformation efficiency, and what do the colors tell you if 780 colonies are white and 60 are blue on X-gal?

Efficiency = 840 colonies ÷ 2 ng = 420 colonies per ng = 4.2 × 10⁵ colonies per μg. The no-DNA plate shows that the antibiotic works (no resistance without the plasmid). Of the 840 colonies, 780 are white (insert probably present, about 93 percent) and 60 are blue (vector without insert).

(b) A Western blot of control and treated cells gives band intensities (arbitrary units): target 4,800 and 1,800; loading control (actin) 2,400 and 2,250, respectively. What is the change in the target in treated relative to control?

Normalize: control 4,800 ÷ 2,400 = 2.0; treated 1,800 ÷ 2,250 = 0.8. The ratio is 0.8 ÷ 2.0 = 0.4. The treated cells have about **40 percent** of the control's target protein, a 60 percent decrease. Looking at the target bands alone (1,800 versus 4,800, a 62.5 percent decrease) would give nearly the same answer here, but the numbers differ and the direction could even flip when loading differs more.

**Worked Example 6: Reading a Sanger result and a reporter experiment (skill: from description to conclusion)**

(a) A Sanger gel read from the smallest fragment to the largest shows end-labels G, A, T, T, C. What is the sequence of the template?

The labeled ends from smallest to largest spell the new strand 5′-GATTC-3′. The template is complementary and antiparallel: 3′-CTAAG-5′, which is written 5′-GAATC-3′.

(b) A promoter fused to GFP gives fluorescence in cells that also express transcription factor T, and 20-fold less in cells given an empty vector. Deleting a 50-bp region of the promoter removes the T-dependent increase. What is the best-supported conclusion?

The factor T increases expression from this promoter, and the deleted 50-bp region is needed for that increase. The experiment does not show that T binds the region directly (it could act through another protein), and it does not show that T acts this way on the native gene in its normal chromosome setting. Controls to look for: empty vector, a constitutive reporter to normalize transfection, and a promoter with an unrelated deletion of the same size.

**More Praxis Tips**

Praxis Tip: Before reading any technique's results, write "DNA, RNA or protein?" on your scratch paper. The choice between Southern, Northern and Western is made entirely by that one word.

Praxis Tip: Lower Ct means more template. Some candidates read "lower" as "less". Draw a small arrow: earlier cycle, more starting material.

Praxis Tip: On any gel question, ask "which way is the positive electrode and which is farther?" DNA is negative, runs toward the anode, and small things go farthest. If you remember only that small runs far, you will still get most questions right.

Praxis Tip: When a band is missing, list the possible causes in order: the sample was not loaded, the target is absent, the probe or antibody failed. Controls decide among them. The passage almost always supplies the control that rules one out.

Praxis Tip: For knockdown versus knockout, ask whether the gene or the transcript was changed. Partial effects, a reduction rather than absence, and reversal within days all point to a knockdown. Permanent, complete absence points to a knockout.

Praxis Tip: A reporter tells you about expression driven by a promoter, not about the protein you care about. If an answer choice says the reporter proves the protein's function, it has probably claimed too much.

Praxis Tip: If a restriction digest question gives you positions, add the fragments. They must sum to the plasmid's total size, and if they do not, you have lost one. A single check removes about half of the arithmetic mistakes.

Praxis Tip: Choose the weakest conclusion that is still supported. Experiments tell you "required" or "sufficient" or "associated", and the answer choices mostly differ in which of those they claim. A knockout that kills the mouse has shown the gene matters, though not subtly.

**Common Mistakes**

- Mixing up Southern, Northern and Western blots (check whether the target is DNA, RNA or protein).
- Reading a lower Ct as less starting material.
- Doubling the wrong thing: using 2n for n cycles instead of 2 raised to the n-th power.
- Estimating a gel band size by simple proportion instead of on the log scale (or, on the exam, outside the range of the ladder).
- Forgetting the loading control when comparing band intensities between lanes.
- Calling white colonies "proof" of the correct insert (they show only that *lacZ* was disrupted).
- Treating a knockdown as if it removed the gene.
- Concluding direct binding from a reporter assay.
- Forgetting that a circular plasmid with n cuts gives n fragments, not n + 1.

**Checkpoint Questions**

1. A reaction begins with 200 copies of a target sequence. Assuming perfect doubling every cycle, how many copies are present after 6 cycles?
   A. 1,200
   B. 12,800
   C. 2,400
   D. 6,400

2. A researcher wants to know whether a mutant cell line still makes the mRNA of gene X, and how long that mRNA is. Which technique best answers both questions?
   A. A Southern blot probed with a labeled sequence from gene X
   B. A Western blot with an antibody to the protein
   C. An ELISA for the protein product
   D. A Northern blot probed with a labeled sequence from gene X

3. In a qPCR experiment with equal input and equal efficiency, sample P reaches the threshold at cycle 20 and sample Q at cycle 23 for the same gene. Which statement is best supported?
   A. Sample P started with about 8 times more template than sample Q
   B. Sample P started with about 8 times less template than sample Q
   C. Sample P started with about 3 times more template than sample Q
   D. The samples started with equal template, and only the primers differ

4. Bacteria are transformed with a ligation mixture of a lacZ-based plasmid and an insert, and plated on ampicillin with X-gal. White colonies are best interpreted as cells that
   A. took up no plasmid
   B. took up a plasmid with an intact lacZ and no insert
   C. took up a plasmid, most likely with an insert that interrupts lacZ
   D. took up a plasmid, and the insert is confirmed to be the correct gene

5. On a Western blot, the target band has the same intensity in the control lane and the treated lane, but the loading-control band is half as intense in the treated lane. The best interpretation is that the treated cells
   A. contain less target protein than the control cells
   B. contain the same amount of target protein
   C. contain no target protein
   D. contain more target protein per unit of total protein than the control cells

6. A purified protein runs at about 60 kDa on SDS-PAGE without a reducing agent and at about 30 kDa when β-mercaptoethanol is added. The protein is most likely
   A. a dimer of two 30 kDa subunits joined by a disulfide bond
   B. a single 60 kDa polypeptide with no disulfide bonds
   C. a single 30 kDa polypeptide that associates only because of SDS
   D. a mixture of 30 kDa and 60 kDa proteins that are unrelated

7. A promoter drives GFP in cells. Cells that also express transcription factor T are 20 times brighter than cells with an empty vector. A constitutive red reporter is equal in the two groups. Which conclusion is best supported?
   A. T binds directly to the promoter
   B. T increases expression from this promoter in these cells
   C. T increases the number of cells that took up the DNA
   D. T is required for all gene expression

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **B.** Copies = 200 × 2⁶ = 200 × 64 = 12,800. (A adds 200 copies per cycle instead of doubling; C multiplies by 2 times 6 instead of raising 2 to the sixth power; D uses only 5 doublings.)
2. **D.** A Northern blot detects RNA by hybridization and shows both presence and size. (A detects DNA, which would be present whether or not the gene is transcribed; B detects protein, not mRNA, and says nothing about mRNA length; C measures protein amount only.)
3. **A.** Each cycle is a doubling, so 3 cycles earlier means 2³ = 8 times more starting template. (B reverses the meaning of a lower Ct; C treats the 3-cycle difference as a 3-fold difference; D the same primers were used for the same gene.)
4. **C.** Ampicillin resistance selects for the plasmid, and the loss of blue color indicates that lacZ is probably interrupted; the insert's identity needs a digest or sequencing. (A cells without the plasmid are killed by ampicillin and would not form colonies; B these would be blue; D white color shows only that lacZ was disrupted, not that the insert is correct.)
5. **D.** Less sample was loaded in the treated lane, so an equal band means the target is relatively enriched (about twofold after normalizing). (A ignores that less sample was loaded in the treated lane; B ignores the normalization; C a band is present.)
6. **A.** Reducing agents break disulfide bonds, and SDS separates the subunits by mass; the size change shows a disulfide-linked pair. (B would run at 60 kDa in both conditions; C SDS disrupts noncovalent association, so a reducing-agent effect points to disulfides; D the shift depends on the reducing agent, not on a mixed sample.)
7. **B.** The equal constitutive reporter excludes differences in uptake, so the higher GFP reflects higher promoter activity; direct binding needs a different experiment. (A the experiment does not test binding, only an effect on expression; C the constitutive reporter is equal, so uptake was similar; D a single promoter was tested.)

Praxis Tip: After the checkpoint questions, name the slip behind each wrong choice (wrong blot, Ct direction, forgotten control, over-reaching conclusion). Log it in your error log (see Book 1, Strategy: The Question Method).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "PCR doubles a primer-defined stretch of DNA each cycle, and qPCR reads the cycle at which it crosses a threshold, with lower Ct meaning more template; gels separate by size with the smallest farthest, blots then find one DNA, RNA or protein with a probe or antibody, ELISA measures amount from a standard curve; restriction enzymes and ligase put inserts into plasmids, selected by antibiotic and screened by blue-white color; Sanger reads the newly made strand, CRISPR cuts DNA and error-prone repair makes knockouts, knockdowns lower the transcript without changing the gene, and reporters read out promoter activity."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 1 and 2 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set that includes [Lesson 8](chapter:12) gene regulation and [Lesson 7](chapter:11) replication), and after 21 days (explain the lesson aloud).

*Interleave:* alternate a technique problem with a gene expression problem and a genetics problem. The next lesson, [Lesson 10](chapter:14), uses probability, and the [Genes and Evolution Set](chapter:16) will test these techniques inside passages.

Praxis Tip: End each study session by writing, from memory, the table of blot types and the three-step PCR cycle, and then predict out loud what a gel would look like for a made-up experiment.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Computed and checked: 100 × 2¹⁰ = 102,400; 100 × 1.9¹⁰ ≈ 61,300; ΔΔCt example gives 8-fold; interpolated band about 680 bp; fragment sums 5,000; 2 ng and 840 colonies give 4.2 × 10⁵ per μg; normalized blot ratio 0.4; checkpoint arithmetic 200 × 2⁶ = 12,800.
- Answer key positions: B, D, A, C, D, A, B.
- Verify with a biology reviewer: typical PCR temperatures; the supercoiled-faster-than-linear statement; the Sanger read-direction description; PAM and guide length wording.
- Category 1B topics covered: PCR, gel electrophoresis, blotting techniques, DNA cloning (vectors, restriction enzymes), sequencing, analysis of gene expression, recombinant DNA, gene editing, knockouts and knockdowns, reporter genes.
