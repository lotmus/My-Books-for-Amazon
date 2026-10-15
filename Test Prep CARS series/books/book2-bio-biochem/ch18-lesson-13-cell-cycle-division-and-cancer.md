# Lesson 13: Cell Cycle, Division and Cancer

**What you will be able to do**

- Order the phases of the cell cycle, name the checkpoints, and explain how cyclins and cyclin-dependent kinases (CDKs) drive the cycle forward.
- Follow chromosome, chromatid and DNA-content (C) numbers through mitosis and through meiosis I and II, and predict what an error such as nondisjunction does.
- Explain how crossing over and independent assortment generate genetic variation.
- Describe apoptosis, and contrast it with necrosis.
- Distinguish proto-oncogenes and oncogenes from tumor suppressors, using p53 and Rb as the central examples, and predict the effect of a mutation.
- Describe potency (totipotent, pluripotent, multipotent), differentiation by differential gene expression, and the broad outline of early embryonic development.

**Why it matters for the exam**

This lesson belongs to category 2C, cell division, differentiation and development. It is a favorite source of passages because it combines counting (chromosomes, chromatids, ploidy), regulation logic (what turns the cycle on, and what stops it), and experiments (flow cytometry histograms, knockouts, drug treatments). It also connects to many neighbors: DNA replication happens in S phase ([Lesson 7](chapter:11)), gene expression decides what a differentiated cell becomes ([Lesson 8](chapter:12)), meiosis is the physical basis of Mendel's laws ([Lesson 10](chapter:14)), the spindle is built from the cytoskeleton ([Lesson 12](chapter:17)), and meiosis in humans is staged across a lifetime in the reproductive system ([Lesson 22](chapter:29)).

Praxis Tip: Almost every question in this lesson is either a counting question or a "what happens if this brake or accelerator is broken" question. Decide which kind it is before you read the answer choices.

**Concept Review**

**The cell cycle.** A dividing eukaryotic cell passes through an ordered cycle.

- **G1 (first gap):** the cell grows, makes proteins and organelles, and decides whether to commit to another division. A cell that leaves the cycle, either temporarily or permanently, is said to be in **G0**. Many mature neurons and cardiac muscle cells are generally in G0 and rarely divide; liver cells can re-enter the cycle after injury.
- **S (synthesis):** DNA is replicated ([Lesson 7](chapter:11)). Each chromosome goes from one chromatid to two identical **sister chromatids**, joined by cohesin proteins and held most tightly at the **centromere**. The centrosome is also duplicated.
- **G2 (second gap):** the cell checks that replication is complete, and makes the proteins needed for mitosis.
- **M (mitosis and cytokinesis):** the nucleus divides (mitosis) and the cytoplasm divides (cytokinesis).

G1, S and G2 together are **interphase**, which in typical cultured cells occupies most of the cycle. M phase is usually the shortest phase, often around an hour or less of a day-long cycle. [VERIFY]

**Checkpoints.** The cycle includes control points at which the cell can stop if conditions are wrong.

- **G1/S checkpoint (the restriction point):** checks cell size, nutrients, growth signals and DNA damage. Passing it generally commits the cell to finish the cycle.
- **G2/M checkpoint:** checks that DNA is fully and accurately replicated and undamaged.
- **Spindle assembly checkpoint (in metaphase):** checks that every chromosome is attached to spindle fibers from both poles. Anaphase is blocked until the last kinetochore is attached.

**Cyclins and CDKs.** The cycle is driven by a family of enzymes called **cyclin-dependent kinases (CDKs)**. A CDK is a protein kinase ([Lesson 12](chapter:17) covers phosphorylation signaling) that is active only when bound to a partner protein, a **cyclin**. Two features explain nearly every question on this topic:

- CDK levels stay roughly constant through the cycle, but cyclin levels **rise and fall**. Cyclins are synthesized at specific times and then destroyed by ubiquitin-mediated proteolysis.
- Different cyclin-CDK pairs act at different points: G1 cyclins with their CDKs push the cell through the G1/S checkpoint, S-phase cyclins promote DNA replication, and the mitotic cyclin with its CDK (often called M-phase promoting factor, or MPF) drives entry into mitosis. [VERIFY specific cyclin letters if you meet them; the exam generally supplies them in the passage.]

Cyclin-CDK activity is also controlled by phosphorylation of the CDK and by **CDK inhibitor proteins** such as p21. At the end of mitosis, a ubiquitin ligase called the **anaphase-promoting complex (APC/C)** tags the mitotic cyclin for destruction and tags a protein (securin) that restrains separase, the enzyme that cuts cohesin. Loss of the cyclin ends the mitotic CDK signal and lets the cell exit mitosis.

**Rb and E2F.** In a resting G1 cell, the **retinoblastoma protein (Rb)** binds a transcription factor called **E2F** and holds it inactive. When growth signals activate G1 cyclin-CDK complexes, they **phosphorylate Rb**. Phosphorylated Rb releases E2F, and E2F turns on the genes needed for S phase. Rb is therefore a **brake**: unphosphorylated Rb stops the cell cycle, and phosphorylation releases the brake.

**p53.** The protein **p53** is a transcription factor that senses cellular stress, especially DNA damage. Normally p53 is kept at low levels because another protein (MDM2) tags it for degradation. DNA damage stabilizes p53, and p53 then activates genes including **p21**, a CDK inhibitor. The result is cell-cycle arrest (commonly at G1/S) that gives time for DNA repair. If the damage is too severe, p53 pushes the cell toward **apoptosis**. Because it protects the genome by stopping or eliminating damaged cells, p53 is often called the "guardian of the genome". A cell without functional p53 can pass damaged DNA to its daughter cells.

Praxis Tip: Tell the story of every cycle protein as accelerator or brake. Cyclin-CDK is an accelerator, Rb and p21 are brakes, p53 is a sensor that applies the brakes, and the APC/C resets the system after mitosis.

**Mitosis.** Mitosis produces two daughter cells genetically identical to the parent (barring mutation). The stages:

- **Prophase:** chromatin condenses into visible chromosomes, each made of two sister chromatids. The mitotic spindle (microtubules) begins forming between the two centrosomes, which move to opposite poles.
- **Prometaphase:** the nuclear envelope breaks down (in animal cells) and spindle microtubules attach to **kinetochores**, protein complexes that assemble on each centromere.
- **Metaphase:** chromosomes line up at the cell's equator (the metaphase plate). The spindle assembly checkpoint operates here.
- **Anaphase:** cohesin is cleaved, sister chromatids separate, and each chromatid is now counted as an independent chromosome. Kinetochore microtubules shorten, and the poles move apart.
- **Telophase:** nuclear envelopes re-form, chromosomes decondense, and the spindle disassembles.
- **Cytokinesis:** in animal cells, a contractile ring of actin and myosin pinches the cell in two (a cleavage furrow). Plant cells build a cell plate.

**Counting rules.** These rules are tested constantly, so memorize the logic rather than the numbers. Use a human cell (2n = 46) as the example. **C** is the DNA content relative to a haploid genome: a haploid gamete is 1C and a diploid G1 cell is 2C.

| Stage | Chromosomes | Chromatids | DNA (C) |
|---|---|---|---|
| G1 | 46 | 46 | 2C |
| G2, prophase, metaphase | 46 | 92 | 4C |
| Anaphase (whole cell) | 92 | 92 | 4C |
| Daughter cell after mitosis | 46 | 46 | 2C |

The rule: **a chromosome is counted by its centromere**. Chromatids are counted only while the sisters are attached. DNA content (C) doubles in S phase and halves at cytokinesis. The number of chromosomes does **not** change in S phase; it doubles transiently in anaphase.

**Meiosis.** Meiosis is two divisions following one round of DNA replication. It converts one diploid cell into four haploid cells that are genetically different from each other.

- **Meiosis I (reductional division):** homologous chromosomes separate. In **prophase I**, homologs pair along their length (**synapsis**) to form a **tetrad** or bivalent (four chromatids), and **crossing over** occurs between non-sister chromatids at points called **chiasmata**. In **metaphase I**, homologous pairs line up at the equator in a random orientation. In **anaphase I**, whole homologs move to opposite poles, but **sister chromatids stay together** (the centromere does not split). Each daughter cell is haploid (n) but each chromosome still has two chromatids.
- **Meiosis II (equational division):** resembles mitosis in a haploid cell. Sister chromatids separate in anaphase II. There is no S phase between meiosis I and II.

| Stage (human) | Chromosomes | Chromatids | DNA (C) |
|---|---|---|---|
| Before meiosis, G1 | 46 | 46 | 2C |
| After S, prophase I | 46 | 92 | 4C |
| After meiosis I (each cell) | 23 | 46 | 2C |
| After meiosis II (each cell) | 23 | 23 | 1C |

The reduction from diploid to haploid happens in meiosis I, not meiosis II. This is why a cell after meiosis I is already called haploid, even though it still has 2C of DNA.

**Sources of variation.** Meiosis generates genetic diversity in three ways.

- **Crossing over** (prophase I) exchanges segments between non-sister chromatids of homologs, producing **recombinant** chromatids that carry new combinations of alleles from the two parents. Genes that are physically farther apart on a chromosome are separated by crossing over more often, which is the basis of linkage maps ([Lesson 10](chapter:14)).
- **Independent assortment** (metaphase I): each homologous pair orients at random, so maternal and paternal chromosomes are distributed independently. With n chromosome pairs, the number of different chromosome combinations in gametes is 2ⁿ (ignoring crossing over). For humans, n = 23, so 2²³ = 8,388,608.
- **Random fertilization:** any sperm can combine with any egg.

**Nondisjunction** is the failure of chromosomes to separate. If it occurs in meiosis I, a pair of homologs goes to the same pole, so all four gametes are abnormal (two with an extra chromosome, two missing one). If it occurs in meiosis II, sister chromatids go to the same pole, so two gametes are normal, one has an extra chromosome and one is missing one. Fertilization with a normal gamete gives a **trisomy** (such as trisomy 21, Down syndrome) or a **monosomy**. Most autosomal monosomies and trisomies are not compatible with live birth.

Praxis Tip: To tell where nondisjunction occurred, look at the alleles in the abnormal gamete. Two different homologs (for example, both A and a) point to meiosis I. Two copies of the same homolog (for example, AA) point to meiosis II, when crossing over near the gene is ignored.

**Mitosis versus meiosis at a glance.**

| Feature | Mitosis | Meiosis |
|---|---|---|
| Divisions, products | 1 division, 2 cells | 2 divisions, 4 cells |
| Ploidy of products | Same as parent | Halved (n) |
| Homolog pairing, crossing over | No | Yes (prophase I) |
| Products identical? | Yes | No |

**Apoptosis.** Apoptosis is programmed, orderly cell death. It sculpts tissues during development (for example, the loss of tissue between developing fingers), removes cells with irreparable DNA damage, and eliminates self-reactive immune cells. The cell shrinks, its chromatin condenses, DNA is cut into fragments, and the cell breaks into membrane-bound fragments that are engulfed by phagocytes. Its contents are not released, so there is generally no inflammation. The central executioners are **caspases**, proteases that are made as inactive precursors and activated in a cascade.

- **Intrinsic (mitochondrial) pathway:** triggered by internal stress such as DNA damage. Pro-apoptotic members of the **Bcl-2 family** make mitochondria leaky, so **cytochrome c** escapes into the cytosol and helps to activate caspases. Anti-apoptotic Bcl-2 proteins oppose this, so overexpression of Bcl-2 can help cancer cells survive.
- **Extrinsic pathway:** triggered when an outside "death signal" binds a death receptor on the cell surface, which activates caspases directly.

**Necrosis**, by contrast, is uncontrolled death from injury (for example, lack of oxygen or toxins). The cell swells and bursts, spilling its contents, and this typically triggers inflammation.

**Cancer: the genetics of runaway division.** Cancer arises from accumulated mutations in genes that control growth, division and death. Two gene classes matter most.

| Feature | Proto-oncogene / oncogene | Tumor suppressor |
|---|---|---|
| Normal role | Promotes growth and division (accelerator) | Restrains division, repairs, or triggers apoptosis (brake) |
| Cancer-causing change | Gain of function | Loss of function |
| Alleles needed | One mutant allele is generally enough | Both alleles generally must be lost |
| Examples | Ras, Myc, growth factor receptors | p53, Rb, BRCA1 and BRCA2 |

A **proto-oncogene** is a normal gene; a mutation, amplification or translocation can convert it into an **oncogene**, whose product is hyperactive or made in excess. For example, a mutant Ras protein that stays locked in its active GTP-bound state keeps sending growth signals ([Lesson 12](chapter:17), G proteins). The effect is **dominant at the cellular level**.

**Tumor suppressors** act as brakes, so cancer requires losing function. The effect is generally **recessive at the cellular level**: a cell with one working copy usually still has enough function. The **two-hit hypothesis** says that both copies must be inactivated. In inherited cancer syndromes (for example, inherited retinoblastoma or Li-Fraumeni syndrome, which involves p53), a person is born with one defective allele in every cell, so only one further "hit" is needed in any one cell, and cancer arises earlier and more often. In sporadic cancer, both hits must occur in the same cell. The *syndrome* is inherited as a dominant trait, but each *cell* becomes cancerous only after the second allele is lost. **BRCA1** and **BRCA2** encode proteins involved in repair of double-strand DNA breaks ([Lesson 7](chapter:11)); their loss raises the mutation rate.

Cancer cells commonly show several features at once: self-sufficient growth signals, insensitivity to stop signals, evasion of apoptosis, unlimited division (often by reactivating **telomerase**; [Lesson 7](chapter:11)), the ability to recruit blood vessels (**angiogenesis**), and the ability to invade and spread (**metastasis**). A **benign** tumor stays local; a **malignant** tumor invades. A **carcinogen** is a substance that raises the probability of cancer, often because it is a mutagen. Cancer is usually the result of several accumulated mutations, which is why its incidence rises with age.

Praxis Tip: For any "this mutation causes cancer" question, ask one thing first: does the mutation make a growth-promoting gene more active (oncogene), or does it make a growth-restraining gene less active (tumor suppressor)? The answer determines the dominance, the number of hits, and the likely treatment strategy.

**Stem cells, differentiation and early development.**

- **Potency** is the range of cell types a cell can become. A **totipotent** cell (the zygote and, generally, cells of the very early embryo) can form the whole organism including placental tissues. A **pluripotent** cell (embryonic stem cells from the inner cell mass) can form every cell type of the body but not the placenta. A **multipotent** cell (for example, a hematopoietic stem cell of the bone marrow) is restricted to a related set of cell types. A **unipotent** cell makes just one type.
- **Stem cells** can both self-renew and give rise to differentiated cells. **Induced pluripotent stem cells (iPSCs)** are made by reprogramming ordinary differentiated cells with a small set of transcription factors, showing that differentiation is generally reversible.
- **Differentiation** occurs by **differential gene expression**. Nearly every cell of an individual carries the same genome; a neuron and a muscle cell differ in which genes are transcribed ([Lesson 8](chapter:12)), not in which genes they contain. Cell fate is directed by transcription factors, by **cytoplasmic determinants** that are unevenly distributed in the egg or dividing cell, and by **induction**, in which signals (including diffusing **morphogens** that form concentration gradients) from neighboring cells change a cell's fate.
- **Early development in outline.** After fertilization, the zygote undergoes **cleavage**, rapid divisions without growth, to make a solid ball (the morula) and then a hollow **blastocyst** in mammals, with an **inner cell mass** (which forms the embryo) and an outer **trophoblast** (which forms the placenta's embryonic part). **Gastrulation** reorganizes the embryo into three **germ layers**: **ectoderm** (skin epidermis, nervous system), **mesoderm** (muscle, bone, blood, heart, kidneys, gonads) and **endoderm** (lining of the gut and respiratory tract; liver and pancreas). **Neurulation** forms the neural tube from ectoderm. Genes such as the **Hox** genes specify position along the head-to-tail axis. Apoptosis and the growth-restraining pathways of this lesson keep the process in order. [Lesson 22](chapter:29) treats human development in more detail.

**Worked Example 1: Counting through the cell cycle (skill: chromosomes, chromatids, C)**

A diploid organism has 2n = 8. Give the number of chromosomes, chromatids and the DNA content (in C) for (a) a G1 cell, (b) a cell in metaphase of mitosis, (c) one cell in anaphase of mitosis, (d) a cell at the end of meiosis I, (e) a gamete.

(a) 8 chromosomes, 8 chromatids, 2C. (b) After S phase: 8 chromosomes, 16 chromatids, 4C. (c) Sister chromatids have separated, so the cell contains 16 chromosomes, 16 chromatids (each is now a chromosome), 4C in total, until cytokinesis. (d) Homologs have separated but sisters have not: each cell has 4 chromosomes, 8 chromatids, 2C. (e) A gamete has 4 chromosomes, 4 chromatids, 1C.

**Worked Example 2: Phase durations from flow cytometry (skill: reading a DNA-content histogram)**

A cell culture is growing asynchronously and steadily, with a total cell cycle of 20 hours. Cells are stained with a dye whose fluorescence is proportional to DNA content, and 1,000 cells are measured: 600 are at 2C, 150 are between 2C and 4C, and 250 are at 4C. In a separate count, 20 of the 1,000 cells are visibly in mitosis. Estimate the time spent in each phase.

The 2C cells are in G1 (or G0): 600/1,000 = 60 percent, so G1 lasts about 0.60 × 20 h = 12 h. The cells between 2C and 4C are replicating DNA (S phase): 15 percent, so S lasts about 3 h. The 4C cells are in G2 or M: 25 percent, so G2 + M lasts about 5 h. The mitotic fraction is 20/1,000 = 2 percent, so M lasts about 0.02 × 20 h = 0.4 h, or 24 minutes. Therefore G2 is about 5 h − 0.4 h = 4.6 h. The assumption is that the cell population is asynchronous and in steady state, so the fraction of cells in a phase approximates the fraction of cycle time spent in that phase.

Praxis Tip: In a DNA-content histogram, the left peak is 2C (G1), the right peak is 4C (G2 and M, which cannot be told apart by DNA content alone), and the valley between them is S phase. A drug that raises the 4C peak and empties the 2C peak blocks the cell after S phase.

**Worked Example 3: Predicting perturbations (skill: brakes and accelerators)**

Predict what happens to the G1/S transition in each case. (a) A mutation that stops Rb from being phosphorylated. (b) A deletion of both copies of the gene for p21 in a cell with DNA damage. (c) A drug that inhibits CDK activity.

(a) Rb stays bound to E2F, so E2F cannot activate S-phase genes: the cell is **blocked in G1**. (b) DNA damage activates p53, but without p21 the CDK complexes are not inhibited, so the cell does **not arrest** and proceeds into S with damaged DNA, increasing the mutation load. (c) Cyclin-CDK cannot phosphorylate its targets, so cells **arrest** at the checkpoint that the inhibited CDK controls (G1/S if a G1 CDK; G2/M if the mitotic CDK). Note the contrast with a mutation that inactivates Rb itself: that releases E2F permanently and removes the brake, which promotes uncontrolled division.

**Worked Example 4: Meiotic variation and nondisjunction (skill: counting gametes)**

(a) An organism has 3 pairs of chromosomes. How many distinct combinations of chromosomes are possible in its gametes, ignoring crossing over? (b) A woman who is heterozygous Aa for a gene near the centromere produces an egg that carries both A and a. Where did nondisjunction occur? (c) What fraction of the gametes from a meiosis II nondisjunction event is normal?

(a) 2³ = 8 combinations. (b) Two different homologs ended up in the same egg, so homologs failed to separate: **meiosis I**. (c) Meiosis II nondisjunction affects only one of the two cells that entered meiosis II, so of the four gametes, **two are normal (one half)**, one has an extra chromosome, and one lacks one. In meiosis I nondisjunction, none of the four gametes is normal.

**Worked Example 5: Classifying a cancer mutation (skill: oncogene or tumor suppressor, two hits)**

In a tumor, the Rb gene has a deletion in both copies. In another tumor, only one of the two alleles of a growth factor receptor gene carries a mutation that makes the receptor signal without its ligand. Classify each, and state why one mutant allele is enough in the second case but not in the first.

The Rb tumor has lost a tumor suppressor: both alleles were lost, consistent with a loss-of-function, recessive-at-the-cell-level mechanism (two hits). The receptor mutation converts a proto-oncogene to an oncogene, a gain of function. The mutant receptor is active regardless of what the normal allele produces, so one mutant allele is dominant at the cellular level. In the Rb cell, one remaining normal allele would still supply enough Rb to restrain E2F.

**Worked Example 6: Apoptosis or necrosis? (skill: mechanism and consequence)**

A cell that has sustained severe DNA damage shows shrinkage, release of cytochrome c from mitochondria, caspase activation, and clean removal by phagocytes without inflammation. Classify the process, and state the role of p53.

This is **apoptosis** by the intrinsic (mitochondrial) pathway. p53, stabilized by the DNA damage, promotes expression of pro-apoptotic Bcl-2 family members, which permeabilize the mitochondria. In contrast, a cell burst by a toxin or lack of oxygen would swell, rupture and cause inflammation (necrosis). A tumor with a p53 mutation would be expected to be resistant to this response.

**More Praxis Tips**

Praxis Tip: For chromosome counting, draw one pair of homologs as two X-shaped objects on scratch paper (one for each homolog after S phase). Then count centromeres for chromosomes and arms-on-a-centromere for chromatids. It takes ten seconds and prevents the commonest error in the lesson.

Praxis Tip: When a passage names an unfamiliar cell-cycle protein, ask whether it behaves as an accelerator or a brake, using the passage's own data (does the cell divide faster or stall when the protein is removed?). You rarely need the protein's real name.

Praxis Tip: A "knockout" of a tumor suppressor makes cells divide more; a knockout of an oncogene (or of an accelerator) makes them divide less. If the result is the opposite, check whether you have reversed the labels.

Praxis Tip: Meiosis I separates homologs and meiosis II separates sisters. Say it as "I is for individuals, II is for identical copies" if that helps. It does not need to be elegant, only reliable.

Praxis Tip: Pay attention to the adjective "haploid". A cell after meiosis I is haploid by chromosome number, yet it still has 2C of DNA because each chromosome has two chromatids.

Praxis Tip: When two answer choices differ only by "dominant" or "recessive", remember the sentence: oncogenes are dominant in the cell, and tumor suppressors are recessive in the cell. Then separately consider whether the question is about the cell or the family.

Praxis Tip: Apoptosis is a tidy dinner party that cleans up after itself. Necrosis is the other kind of party. If the stem mentions inflammation, think necrosis.

**Common Mistakes**

- Saying that the chromosome number doubles in S phase. DNA content doubles; chromosome number does not.
- Counting chromatids as chromosomes before anaphase, or counting a chromosome as one chromatid after replication.
- Calling the product of meiosis I diploid, or placing the reduction in ploidy in meiosis II.
- Forgetting that sister chromatids do not separate in anaphase I.
- Reversing the effect of Rb phosphorylation: phosphorylated Rb releases E2F and lets the cell proceed.
- Saying that p53 is an oncogene because mutations in it are found in cancers. It is a tumor suppressor, lost in cancer.
- Thinking that cancer requires only one mutation, or that every cancer is inherited.
- Treating apoptosis as a failure of the cell. It is an active, regulated process.
- Claiming that differentiated cells have lost genes. They have the same genome but express different genes.

**Checkpoint Questions**

1. A human skin cell has finished S phase but has not yet entered mitosis. How many chromosomes and how many chromatids does it contain?
   A. 92 chromosomes and 92 chromatids
   B. 46 chromosomes and 46 chromatids
   C. 46 chromosomes and 92 chromatids
   D. 23 chromosomes and 46 chromatids

2. Which statement best explains why CDK activity rises and falls during the cell cycle even though the concentration of CDK protein stays roughly constant?
   A. CDKs are active only when bound to cyclins, and cyclin levels rise and fall through synthesis and destruction
   B. CDK genes are transcribed only during M phase
   C. CDKs are active by themselves and cyclins inhibit them
   D. Cyclins are the kinases that phosphorylate Rb directly

3. A drug is added to an asynchronous culture. After 24 hours a DNA-content histogram shows that most cells have 4C DNA and almost none have 2C. The drug most likely blocks the cell cycle
   A. in G1, because cells with 2C DNA accumulate
   B. after S phase, at G2 or in mitosis before cell division
   C. in S phase, because DNA synthesis cannot start
   D. in G0, where cells carry 4C DNA

4. A cell with functional p53 sustains DNA damage. Which sequence is most likely?
   A. MDM2 degrades p53 more rapidly so that the cell can continue dividing
   B. p53 phosphorylates Rb to release E2F and speed entry into S phase
   C. the cell passes the checkpoint at the normal rate so that replication can repair the damage
   D. p53 accumulates, p21 is expressed and inhibits CDKs, and the cell arrests to allow repair or undergoes apoptosis if the damage is severe

5. A woman is heterozygous (Aa) for a gene very close to a centromere. She produces an egg that carries both an A allele and an a allele for this chromosome pair. The most likely explanation is
   A. nondisjunction in meiosis I, because homologous chromosomes failed to separate
   B. nondisjunction in meiosis II, because sister chromatids failed to separate
   C. nondisjunction in mitosis of the egg, because the egg is dividing
   D. normal meiosis, because every egg carries both alleles

6. In a tumor, a mutation in one allele of a gene locks the encoded protein in a permanently active signaling state. Which classification is most appropriate?
   A. a loss-of-function mutation in a tumor suppressor, which requires both alleles to be lost
   B. a silent mutation with no effect on the protein
   C. a loss-of-function mutation in a tumor suppressor, which is dominant
   D. a gain-of-function mutation converting a proto-oncogene into an oncogene, where one mutant allele can be sufficient

7. A neuron and a hepatocyte from the same person have very different structures and proteins. This is best explained by
   A. irreversible loss of the unused genes during differentiation
   B. differential gene expression from essentially the same genome
   C. different numbers of chromosomes in the two cell types
   D. different genetic codes used by the two cell types

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **C.** DNA replication doubles the chromatids but leaves the chromosome number unchanged, because the sisters remain joined at a single centromere. (A counts each sister chromatid as a separate chromosome, which is correct only after sisters separate in anaphase; B is the count for G1, before replication doubled the chromatids; D is the count for a cell after meiosis I, not a diploid cell after S phase.)
2. **A.** Cyclin availability, not CDK abundance, sets the timing of CDK activity. (B contradicts the premise that the CDK level stays constant; C reverses the relationship, since cyclin binding is required for activity; D assigns the kinase activity to the cyclin, when it belongs to the CDK.)
3. **B.** Cells with 4C DNA have completed replication but have not divided. DNA content alone cannot separate G2 from mitosis. (A would produce an accumulation at 2C, the opposite of what is observed; C would leave cells at 2C rather than 4C; D is wrong because G0 cells are diploid and have 2C DNA.)
4. **D.** Damage stabilizes p53, which acts as a sensor that applies the brakes through p21 and, if necessary, triggers apoptosis. (A describes the opposite of p53 stabilization after damage; B confuses the brake with the accelerator, since p53 acts to stop the cycle; C ignores the arrest that gives time for repair, and replication does not repair damage.)
5. **A.** Two different homologs in one gamete indicate that the homologs did not separate in meiosis I. (B would generally give two copies of the same allele, such as AA or aa; C does not apply, since a mature egg is a product of meiosis; D is incorrect, since a normal egg carries one copy of the chromosome and thus one allele.)
6. **D.** A hyperactive growth-promoting protein is an oncogene product, and a single hyperactive allele can drive signaling despite a normal partner allele. (A contradicts the stem, since the protein is hyperactive rather than lost; B is inconsistent with a protein that is permanently active; C fails because a loss of function in a tumor suppressor is generally recessive at the cellular level.)
7. **B.** Differentiated cells carry the same genes but transcribe different subsets of them. (A is generally false, since reprogramming to iPSCs and nuclear transfer show the genes are retained; C is not true, since both are normally diploid with the same karyotype; D is false because the genetic code is essentially universal.)

Praxis Tip: After the checkpoint questions, name the slip behind every wrong choice (counted wrong, reversed brake and accelerator, mixed meiosis I with II, or oncogene with tumor suppressor). Log it in your error log (see Book 1, Strategy: The Question Method).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "The cell cycle runs G1, S, G2 and M, with checkpoints that cyclin-CDK complexes accelerate and that Rb, p21 and p53 restrain; mitosis makes identical diploid cells, while meiosis uses crossing over and independent assortment to make four different haploid cells, with homologs separating in meiosis I and sisters in meiosis II; apoptosis is orderly caspase-driven death; oncogenes are gain-of-function accelerators and tumor suppressors are loss-of-function brakes; and differentiation is differential gene expression from the same genome."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 1 and 4 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set that includes [Lesson 7](chapter:11) replication and [Lesson 10](chapter:14) genetics), and after 21 days (explain the lesson aloud).

*Interleave:* alternate a counting problem with a regulation problem and a genetics problem. Then take the [Cell Biology and Microbiology Set](chapter:20), once [Lesson 14](chapter:19) is also complete.

Praxis Tip: End each study session by drawing, from memory, the cell cycle with its three checkpoints, the stage table for mitosis and for meiosis, and the oncogene versus tumor suppressor table.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Verified by calculation: 2²³ = 8,388,608; 2³ = 8; Worked Example 2 (0.60 × 20 = 12 h; 0.15 × 20 = 3 h; 0.25 × 20 = 5 h; 0.02 × 20 h = 24 min); human chromosome, chromatid and C tables.
- Answer key positions: C, A, B, D, A, D, B.
- Verify with a cell biology reviewer: typical phase durations (M phase "an hour or less"); wording on cyclin-CDK pairings (kept generic on purpose); the statement that totipotency is generally limited to the zygote and very early blastomeres; germ layer derivatives (kidneys and gonads listed under mesoderm); the claim that iPSCs show differentiation is generally reversible; the mention of Bcl-2 and cytochrome c in the intrinsic pathway.
- Category 2C topics covered: cell cycle and checkpoints, regulation (cyclins, CDKs, Rb, p53), mitosis, meiosis and genetic variation, nondisjunction, apoptosis, oncogenes and tumor suppressors, stem cells, differentiation, and an overview of early development.
