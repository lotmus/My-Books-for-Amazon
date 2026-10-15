# Lesson 7: DNA Replication and Repair

**What you will be able to do**

- Explain why replication is semiconservative and predict the outcome of a density-labeling experiment.
- Name the enzymes at the replication fork, state what each does, and explain why the lagging strand is made in fragments.
- Compare prokaryotic and eukaryotic replication, including origins, polymerases and the end-replication problem.
- Explain proofreading, telomeres and telomerase.
- Match a type of DNA damage to the repair pathway that fixes it, and classify point mutations by their effect on a protein.

**Why it matters for the exam**

Category 1B asks you to reason about how genetic information is copied, protected and changed. Passages in this area often describe an enzyme that has been deleted or inhibited and ask what happens to the new DNA. The knowledge you need is small and highly connected: one direction of synthesis (5′ to 3′), one requirement (a free 3′-OH), and a handful of enzymes with clear jobs. This lesson builds on the structure of DNA in [Lesson 3](chapter:6) and on enzyme logic from Book 1, Lesson 24. The lessons that follow use it: [Lesson 8](chapter:12) covers how the information is read, and [Lesson 9](chapter:13) covers the laboratory methods (such as PCR) that borrow the replication machinery.

Praxis Tip: Almost every replication question can be answered from two facts: DNA polymerase adds nucleotides only to a free 3′-OH, and it reads the template 3′ to 5′ while building the new strand 5′ to 3′. Write those two facts at the top of your scratch paper before you start.

**Concept Review**

**Semiconservative replication.** Each daughter double helix contains one old (parental) strand and one newly made strand. This was shown by the Meselson-Stahl experiment: bacteria grown for many generations in heavy nitrogen (¹⁵N) were moved to light nitrogen (¹⁴N), and the DNA was separated by density in a centrifuge. After one generation all DNA had an intermediate density (hybrid, one heavy and one light strand). After two generations half the DNA was hybrid and half was fully light. Conservative replication (the parental double helix stays intact and an all-new copy is made) predicts a heavy band and a light band after one generation, which was not seen. Dispersive replication (mixed segments in every strand) predicts a single band that gets lighter each generation, and it does not predict the persistent hybrid band that was seen.

**Origins and the replication fork.** Replication begins at specific sites called **origins of replication**. Bacterial chromosomes are generally circular and have a single origin (**oriC** in *E. coli*). Eukaryotic chromosomes are linear and very long, so each has many origins, which fire at different times during S phase. At an origin the DNA opens into a **replication bubble** with a **replication fork** at each end. Replication is **bidirectional**: two forks move away from each origin in opposite directions. The bacterial chromosome is therefore copied by two forks that travel around the circle until they meet.

**The enzymes at the fork.**

| Protein | Job |
|---|---|
| Helicase | Unwinds the double helix (uses ATP) |
| Single-strand binding proteins | Keep the separated strands from re-pairing |
| Topoisomerase (gyrase in bacteria) | Relieves supercoiling ahead of the fork |
| Primase | Makes a short RNA primer |

| Protein | Job |
|---|---|
| DNA polymerase III (bacteria) | Main enzyme that extends new DNA |
| DNA polymerase I (bacteria) | Replaces RNA primers with DNA |
| Sliding clamp | Holds the polymerase on the template |
| DNA ligase | Seals nicks in the sugar-phosphate backbone |

**Why a primer?** DNA polymerases cannot start a new chain. They can only add a nucleotide to an existing 3′-OH. **Primase**, an RNA polymerase, lays down a short RNA **primer**, and the DNA polymerase extends it. Each new nucleotide arrives as a deoxynucleoside triphosphate (dNTP). The polymerase joins its α-phosphate to the 3′-OH of the growing strand and releases pyrophosphate; the hydrolysis of that pyrophosphate pulls the reaction forward ([Lesson 4](chapter:7) on coupling).

**Leading and lagging strands.** The two parental strands are antiparallel, but the polymerase can only build 5′ to 3′. At each fork:

- The **leading strand** uses the template that is read 3′ to 5′ in the direction the fork is moving. It is built continuously, toward the fork, from a single primer.
- The **lagging strand** uses the other template. It must be built away from the fork in short pieces called **Okazaki fragments**, each needing its own primer. Each fragment is roughly 1,000 to 2,000 nucleotides in bacteria and roughly 100 to 200 in eukaryotes [VERIFY].
- After a fragment is made, DNA polymerase I (bacteria) removes the RNA primer ahead of it, using its 5′ to 3′ exonuclease activity, and fills the gap with DNA. **DNA ligase** then forms the final phosphodiester bond between neighboring fragments.

Because the lagging strand needs a new primer for every fragment, it uses far more primers than the leading strand.

**Prokaryotic and eukaryotic replication.**

| Feature | Prokaryote | Eukaryote |
|---|---|---|
| Origins per chromosome | One | Many |
| Main polymerases | Pol III (and Pol I) | Generally pol delta, epsilon, alpha |
| Okazaki fragments | Longer | Shorter |
| Chromosome ends | Circular, no ends | Linear, telomeres |

In eukaryotes the DNA is wrapped on histones, so replication also requires new histones and re-forming chromatin. In eukaryotes the polymerase that works with primase to start fragments is generally pol alpha, while pol delta and pol epsilon are generally the main extending enzymes for the lagging and leading strands [VERIFY]. Mitochondria have their own DNA polymerase and their own small circular genome.

Praxis Tip: When a passage describes a mutant lacking one fork enzyme, ask what the fork would look like. No helicase: no bubble. No primase: no starting point. No ligase: the lagging strand stays in unjoined fragments. No topoisomerase: the DNA ahead of the fork over-twists and the fork stalls.

**Fidelity and proofreading.** DNA polymerase is selective: the correct base fits the active site by size and hydrogen bonding, and a wrong base is added only about once in 10⁴ to 10⁵ nucleotides [VERIFY]. Replicative polymerases also have a **3′ to 5′ exonuclease** activity: when a wrong nucleotide is added, the polymerase pauses, backs up, removes the mismatched 3′ nucleotide and tries again. This **proofreading** improves accuracy roughly a hundredfold. After replication, the **mismatch repair** system (below) removes most remaining errors. The overall error rate after all these steps is roughly one per 10⁹ to 10¹⁰ nucleotides copied [VERIFY]. RNA polymerases make more errors than DNA polymerases, which is tolerable because RNA is temporary.

**Telomeres and telomerase.** The ends of linear chromosomes are protected by **telomeres**: many repeats of a short sequence (TTAGGG in humans) that end in a single-stranded 3′ overhang. The **end-replication problem** is that the lagging strand cannot be completed to the very end: after the last primer at the 5′ end of the new strand is removed there is nothing to extend, and a short stretch of the template is left unreplicated. With every division telomeres therefore tend to shorten. Short telomeres signal damage and trigger senescence or apoptosis, a built-in limit on the number of divisions.

**Telomerase** is a ribonucleoprotein: a reverse transcriptase protein component that carries its own RNA component. The RNA contains a sequence complementary to the telomere repeat, and it serves as a template to extend the 3′ overhang of the template strand. Primase and DNA polymerase can then fill in the complementary strand. Telomerase is generally active in germ cells, early embryonic cells and many stem cells, and is generally low or absent in most somatic cells. Most cancer cells reactivate telomerase, which helps them divide without limit.

**DNA damage and repair.** DNA is damaged constantly, both by normal chemistry (for example, cytosine slowly deaminates to uracil) and by agents such as ultraviolet (UV) light, ionizing radiation and chemicals. The cell has several repair systems, and the choice depends on the type of lesion.

| Pathway | Lesion it fixes | Key idea |
|---|---|---|
| Mismatch repair | Mispaired bases after replication | Cuts out the new strand |
| Base-excision repair | One damaged base (e.g., uracil) | Glycosylase removes the base |
| Nucleotide-excision repair | Bulky lesions (e.g., thymine dimers) | Cuts out a stretch of strand |
| Double-strand break repair | Both strands cut | Join ends or copy from a partner |

- **Mismatch repair.** Proofreading misses a few errors. Mismatch repair proteins scan newly made DNA, detect distortions from a mismatch, and remove a stretch of the strand containing the error. To fix the right strand the system must tell new from old: in *E. coli* the parental strand is marked by methylation that has not yet been added to the new strand, and in eukaryotes nicks and other features of the newly made strand serve as markers. A repair polymerase fills the gap and ligase seals it. Defects in human mismatch repair genes are linked to hereditary colorectal cancer.
- **Base-excision repair (BER).** For small, nondistorting damage to a single base, such as uracil from cytosine deamination. A **DNA glycosylase** recognizes the abnormal base and cuts the bond between the base and the sugar, leaving an **apurinic or apyrimidinic (AP) site**. An AP endonuclease cuts the backbone at that site, a polymerase fills in the missing nucleotide, and ligase seals the nick. Uracil in DNA is easy to spot because DNA normally contains thymine, not uracil. This is one reason thymine, rather than uracil, is used in DNA: deaminated cytosine can be detected and fixed.
- **Nucleotide-excision repair (NER).** For bulky lesions that distort the helix, such as the **thymine dimers** formed when UV light joins adjacent thymines. A complex of proteins recognizes the distortion, cuts the damaged strand on both sides of the lesion, removes a stretch of roughly 25 to 30 nucleotides [VERIFY], and a polymerase refills the gap using the intact strand as template. Defects in NER cause **xeroderma pigmentosum**, with extreme sensitivity to sunlight and high rates of skin cancer.
- **Double-strand break repair.** A break in both strands is among the most dangerous lesions. There are two main routes. **Non-homologous end joining (NHEJ)** joins the broken ends directly. It works at any stage of the cell cycle but may lose or add a few nucleotides, so it is error-prone. **Homologous recombination** uses an undamaged homologous copy (generally the sister chromatid, available after replication in S and G2) as a template to restore the original sequence accurately. Mutations in the genes for homologous recombination (for example *BRCA1* and *BRCA2*) raise cancer risk.

Praxis Tip: Pick the repair pathway by asking two questions. Is the damage in one strand (so the other strand can serve as the template) or both? Is it one base or a bulky distortion? One base: BER. Bulky: NER. Replication error: mismatch. Both strands: break repair.

**Mutations.** A **mutation** is a heritable change in DNA sequence. If it arises in a germ cell it can be passed on to offspring; a **somatic** mutation affects only that cell and its descendants and is not inherited by children. Mutations arise from replication errors that escape repair, from chemical or radiation damage, or from mobile DNA elements.

| Type | Change in DNA | Effect on protein |
|---|---|---|
| Silent | Codon changes, same amino acid | None |
| Missense | One amino acid changes | Varies, from none to severe |
| Nonsense | Codon becomes a stop | Protein cut short |
| Frameshift | Insertion or deletion not a multiple of 3 | Every downstream codon changes |

An insertion or deletion of a multiple of three nucleotides (an **in-frame** change) adds or removes whole amino acids but keeps the downstream frame. Sickle cell disease is a classic missense example: a single nucleotide change in the gene for the beta chain of hemoglobin replaces glutamate with valine at one position, and the altered protein polymerizes when deoxygenated. Other mutations can change splice sites, promoters or regulatory sequences without altering the coding sequence directly. Larger changes include duplications, deletions, inversions and translocations. Many mutations are neutral. A mutation in a gene can cause **loss of function** (the usual result) or, less commonly, a **gain of function**; both ideas return in [Lesson 13](chapter:18) on oncogenes and tumor suppressors.

Praxis Tip: To classify a point mutation, write the old and new codons side by side and look up both. Same amino acid: silent. Different amino acid: missense. Stop: nonsense. Never decide from the DNA alone, because the code is degenerate.

**Worked Example 1: Meselson-Stahl (skill: predicting a labeling experiment)**

Bacteria grown for many generations in ¹⁵N medium are moved to ¹⁴N medium and allowed to divide three times. Assuming semiconservative replication, what fraction of the DNA molecules is hybrid (one heavy and one light strand), and what fraction is fully light?

Start with one fully heavy double helix. Semiconservative replication keeps each old heavy strand paired with a new light strand, so the two heavy strands are always found in hybrid molecules, and only two hybrid molecules exist in any later generation. After n generations there are 2ⁿ molecules. After 3 generations there are 2³ = 8 molecules: 2 hybrid and 6 fully light. The hybrid fraction is 2/8 = 1/4 (25 percent) and the fully light fraction is 6/8 = 3/4 (75 percent). Check with the earlier generations: after 1, all (2 of 2) are hybrid; after 2, 2 of 4 (half) are hybrid, matching the experimental result.

**Worked Example 2: How long does a bacterial chromosome take to copy? (skill: bidirectional replication)**

A circular bacterial chromosome of 4.8 million base pairs has one origin. Each fork moves at 800 nucleotides per second. How long does replication take, assuming that both forks start together and never stall?

Bidirectional replication means each fork copies half of the chromosome, 2.4 million base pairs, and the two forks meet opposite the origin. Time = distance divided by speed = 2,400,000 / 800 = 3,000 seconds = 50 minutes. If only one fork were working, the time would double to 100 minutes. This also explains why eukaryotes use many origins: with a genome roughly a thousand times larger and slower forks [VERIFY], one origin would take far too long.

**Worked Example 3: Following one fork (skill: leading versus lagging)**

At a fork moving to the right, the parental strand running 3′ to 5′ left to right is the template for one new strand. Which new strand is leading and which is lagging, and why?

The polymerase builds new DNA 5′ to 3′, reading the template 3′ to 5′. The template that runs 3′ to 5′ in the direction the fork moves (left to right) lets the polymerase follow the fork and synthesize continuously: that new strand is the **leading strand**. The other template runs 5′ to 3′ in the direction of fork movement. The polymerase must work away from the fork, backward relative to the fork's travel, in segments: that new strand is the **lagging strand**, made as Okazaki fragments, each needing a primer. If DNA ligase is missing, the lagging strand is made but remains in fragments with nicks between them, while the leading strand is mostly unaffected.

**Worked Example 4: Telomere shortening (skill: modeling a limit)**

A somatic cell begins with a telomere of 10,000 base pairs and loses 100 base pairs per division. Senescence is triggered when the telomere falls below 4,000. How many divisions can the lineage complete? What changes if the cells express telomerase?

The telomere can lose 10,000 − 4,000 = 6,000 base pairs before the threshold. At 100 per division, 6,000 / 100 = 60 divisions. With telomerase, repeats are added back to the 3′ overhang, so the net loss per division can be reduced or eliminated, and the cell is no longer limited by telomere length. This is why high telomerase activity is a feature of germ cells, stem cells and most tumors, and why a passage that "immortalizes" cultured cells by adding telomerase makes biological sense.

**Worked Example 5: Classifying mutations (skill: codon comparison)**

In one mRNA the codon GAG (glutamate) is changed in three different alleles to GAA, GUG and UAG. Classify each. Then say what happens if a single nucleotide is inserted early in the coding region.

GAA also codes for glutamate: **silent**. GUG codes for valine: **missense** (the sickle cell change). UAG is a stop codon: **nonsense**, which truncates the protein, and often leads to a nonfunctional product. A single-nucleotide insertion is not a multiple of three, so it shifts the reading frame: every codon downstream changes and a premature stop codon is likely. Insertion of three nucleotides would instead add one amino acid and keep the frame. The earlier in the gene a frameshift or nonsense mutation occurs, the more severe it usually is.

**More Praxis Tips**

Praxis Tip: In the Meselson-Stahl problems, count molecules, not strands. The two original heavy strands never disappear, they just get diluted among 2ⁿ molecules.

Praxis Tip: If a question asks which strand is lagging, find the direction of fork movement first. Arrows on scratch paper, drawn with the 5′ and 3′ labels, beat memory every time.

Praxis Tip: Remember that primers are RNA, and that is why a replacement enzyme (DNA polymerase I in bacteria) is needed. DNA does not contain stray RNA bits for very long, which is fortunate for everyone involved.

Praxis Tip: Proofreading is the polymerase's own 3′ to 5′ exonuclease. Mismatch repair is a separate system that works after replication. A mutant lacking proofreading and one lacking mismatch repair both raise mutation rates, but the second can be distinguished by errors persisting in the new strand after the polymerase has moved on.

Praxis Tip: Telomerase is a reverse transcriptase that carries an RNA template. If a passage says that an enzyme "uses an internal RNA template to make DNA", it is describing telomerase.

Praxis Tip: For any damage question, read what the lesion looks like. A single odd base points to BER; a pair of fused bases points to NER; a clean break across both strands points to end joining or recombination.

**Common Mistakes**

- Saying DNA polymerase can start a chain without a primer.
- Reversing the direction of synthesis, or saying a strand is made 3′ to 5′.
- Confusing proofreading (during replication, by the polymerase) with mismatch repair (after replication, by separate proteins).
- Saying the leading strand has no primer; it has one primer per fork, and it is the lagging strand that needs many.
- Treating all repair as one process; the pathway depends on the lesion.
- Classifying a mutation as silent or missense from the DNA change alone, without checking the codon table.
- Saying that telomerase is active in all somatic cells.

**Checkpoint Questions**

1. Bacteria grown for many generations in ¹⁵N medium are transferred to ¹⁴N medium and allowed to replicate DNA three times. Assuming semiconservative replication, what fraction of the DNA molecules is hybrid (one ¹⁵N strand and one ¹⁴N strand)?
   A. 1/2
   B. 1/4
   C. 1/8
   D. 3/4

2. Which statement about the lagging strand is correct?
   A. It is synthesized in the 3′ to 5′ direction
   B. It is made continuously from a single primer
   C. It requires no primer because ligase supplies the 3′-OH
   D. It is made discontinuously as Okazaki fragments, each starting from an RNA primer

3. A mutant DNA polymerase lacks its 3′ to 5′ exonuclease activity but is otherwise normal. Compared with the normal enzyme, the mutant would most likely
   A. leave more mismatched nucleotides in the newly synthesized strand
   B. be unable to add any nucleotides at all
   C. synthesize DNA in the 3′ to 5′ direction
   D. no longer require a primer

4. Telomerase differs from conventional DNA polymerase because telomerase
   A. is highly active in most mature somatic cells
   B. adds nucleotides to a 5′ end
   C. carries its own RNA that serves as the template for adding repeats to the chromosome end
   D. is needed to replicate circular bacterial chromosomes

5. A skin cell is exposed to ultraviolet light, which fuses adjacent thymine bases on one strand into a bulky dimer that distorts the helix. Which pathway is the main route for repairing this damage?
   A. Mismatch repair
   B. Nucleotide-excision repair
   C. Base-excision repair
   D. Non-homologous end joining

6. The mRNA codon UAC (tyrosine) is changed by a single nucleotide substitution to UAA. This is best described as a
   A. silent mutation, because the codon changes without altering the protein
   B. missense mutation, in which tyrosine is replaced by another amino acid
   C. frameshift mutation, because the reading frame is altered
   D. nonsense mutation, producing a shortened protein

7. An electron micrograph shows a single linear DNA molecule from a growing cell with several replication bubbles along its length. These data are most consistent with
   A. a eukaryotic chromosome with multiple origins of replication
   B. a bacterial chromosome, which generally replicates from a single origin
   C. a DNA molecule that has no origin
   D. a cell in which helicase is inactive

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **B.** After three generations there are 8 molecules, of which exactly 2 are hybrid and 6 are fully light. (A is the hybrid fraction after two generations, not three; C would mean only one hybrid molecule in eight, but both parental strands end up in separate hybrid molecules; D is the fully light fraction after three generations, not the hybrid fraction.)
2. **D.** The lagging strand template runs the wrong way for continuous synthesis at the fork, so the polymerase works backward in pieces, each needing a primer. (A no DNA polymerase extends a chain in the 3′ to 5′ direction; B describes the leading strand; C ligase seals nicks but cannot start a new chain.)
3. **A.** The 3′ to 5′ exonuclease is the proofreading function that removes wrongly added nucleotides. (B polymerase activity is separate from exonuclease activity; C direction of synthesis is determined by the polymerase active site, not the exonuclease; D a primer is still required.)
4. **C.** Telomerase is a reverse transcriptase with an internal RNA template, and it extends the 3′ overhang of the chromosome end. (A is generally low or absent in most somatic cells; B like every polymerase it extends a 3′ end; D circular chromosomes have no ends and so do not need it.)
5. **B.** Nucleotide-excision repair removes a stretch of the damaged strand, and the intact strand is used as a template for filling the gap. (A corrects mispaired bases in newly synthesized DNA, not bulky dimers; C generally handles small single-base lesions removed by a glycosylase; D rejoins double-strand breaks, and here only one strand is damaged.)
6. **D.** UAA is a stop codon, so translation ends at that position and the protein is truncated. (A UAA is a stop codon, so the protein is changed; B UAA specifies no amino acid; C a substitution keeps the frame.)
7. **A.** Several bubbles on one linear molecule reflect multiple origins firing during S phase, a eukaryotic feature. (B would show a single bubble, not several; C without an origin no bubbles can form; D without helicase the strands do not separate and no bubbles form.)

Praxis Tip: After the checkpoint questions, sort each miss into one of three bins: wrong direction, wrong enzyme job, or wrong repair pathway. Log the bin in your error log ([Strategy: The Question Method](chapter:4)), and the pattern will tell you what to review.

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "Replication is semiconservative and bidirectional from origins, with helicase opening the fork, primase making RNA primers, polymerase extending 3′-OH ends 5′ to 3′ with proofreading, a continuous leading strand and a lagging strand in Okazaki fragments joined by ligase; telomerase uses its own RNA template to protect linear ends; and different lesions go to different repair pathways, while mutations are classified by what they do to the codon."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 1 and 3 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (mix with [Lesson 3](chapter:6) on nucleic acid structure and Book 1, Lesson 24 on enzymes), and after 21 days (explain the lesson aloud and draw a fork with both strands).

*Interleave:* alternate a replication problem with a nucleic acid structure problem and an enzyme problem. Next, move on to [Lesson 8](chapter:12) to see how the sequence you have just learned to copy gets read.

Praxis Tip: End each study session by drawing a replication fork from memory with all eight proteins, 5′ and 3′ labels on every strand, and an arrow for the direction of fork movement.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Verified by calculation: Meselson-Stahl fractions (2 of 8 hybrid, 6 of 8 light after three generations); fork time (2.4 million bp / 800 per second = 3,000 s = 50 min); telomere divisions (6,000 / 100 = 60).
- Answer key positions: B, D, A, C, B, D, A.
- Verify with a molecular biology reviewer: eukaryotic polymerase roles (alpha, delta, epsilon); Okazaki fragment sizes; polymerase and overall error rates; NER excision length; the uracil-in-DNA rationale for thymine; statements on telomerase activity.
- Category 1B topics covered: DNA replication (semiconservative, origins, enzymes, leading and lagging strands, prokaryotic and eukaryotic differences, proofreading, telomeres and telomerase), DNA repair (mismatch, base-excision, nucleotide-excision, double-strand break), and mutation types and consequences.
