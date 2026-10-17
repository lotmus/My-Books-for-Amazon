# Lesson 8: Transcription, Translation and Gene Regulation

**What you will be able to do**

- Trace information from DNA to RNA to protein and name the enzymes and signals at each step.
- Predict an mRNA and a peptide from a DNA template, using the genetic code.
- Describe RNA processing in eukaryotes (cap, tail, splicing) and explain how bacteria differ.
- Explain the lac and trp operons and predict the effect of mutations and conditions.
- Describe eukaryotic gene regulation, including transcription factors and enhancers, epigenetic marks and RNA interference.

**Why it matters for the exam**

Category 1B includes how genes are read and how the reading is controlled. These ideas appear constantly in experiment passages: a reporter gene, a knockdown, a drug that changes chromatin, a mutated operator. Regulation questions are logic questions. If you can state, for each regulator, what it binds, what it does and what turns it on, you can answer almost any variant. This lesson builds on the structure of nucleic acids ([Lesson 3](chapter:6)) and on replication ([Lesson 7](chapter:11)), and it supplies the background for the laboratory methods in [Lesson 9](chapter:13).

Praxis Tip: For every regulatory protein in a passage, fill in a three-part sentence: "It binds ___, so transcription goes ___ when ___." Practicing that sentence beats memorizing operon diagrams.

**Concept Review**

**The central dogma.** Information generally flows from DNA to RNA to protein. DNA is copied to DNA in **replication**, DNA is read into RNA in **transcription**, and mRNA is read into protein in **translation**. There are well-known exceptions: retroviruses (such as HIV) copy RNA into DNA with **reverse transcriptase**, and some viruses copy RNA into RNA. Proteins are not copied back into nucleic acid.

**Transcription.** RNA polymerase reads the **template (antisense) strand** 3′ to 5′ and builds RNA 5′ to 3′, using ribonucleoside triphosphates. The RNA has the same sequence as the **coding (sense) strand**, with U in place of T. Unlike DNA polymerase, RNA polymerase does not need a primer.

- **Promoters** are DNA sequences that tell polymerase where to start. In bacteria the polymerase core enzyme is guided by a **sigma factor** that recognizes promoter elements near the −10 and −35 positions (numbered relative to the start site). In eukaryotes **RNA polymerase II**, which makes mRNA, cannot bind the promoter alone: general transcription factors assemble first, often at a **TATA box** about 25 to 30 bases upstream of the start. RNA polymerase I and III generally make most rRNA and tRNA, respectively.
- **Elongation:** the polymerase unwinds a short bubble and adds nucleotides, with the growing RNA peeling away from the template.
- **Termination:** bacteria use signals in the RNA (a hairpin followed by a run of U residues) or a protein called rho. In eukaryotes the transcript is cut downstream of a polyadenylation signal (AAUAAA) and polymerase falls off farther along.

Praxis Tip: To write an mRNA from a template strand, write the complementary RNA bases, then check the direction. If the template is written 3′-TAC-5′, the mRNA is 5′-AUG-3′, and the mRNA has the same sequence as the coding strand with U replacing T.

**RNA processing in eukaryotes.** The primary transcript (pre-mRNA) is modified in the nucleus before export:

- **5′ cap:** a modified guanine nucleotide (7-methylguanosine) joined to the 5′ end. It protects the RNA from degradation and helps ribosomes bind.
- **3′ poly-A tail:** a string of adenine nucleotides added after cleavage at the polyadenylation signal. It stabilizes the mRNA and helps with export and translation.
- **Splicing:** the spliceosome (small nuclear RNAs with proteins) removes **introns** (intervening sequences) and joins **exons** (sequences that remain in the mature RNA). Introns generally begin with GU and end with AG. Introns are removed in a lariat-shaped intermediate. In **alternative splicing**, different combinations of exons are joined, so one gene can produce several different proteins; this is one reason why the number of human proteins is much larger than the number of genes. Some RNAs, such as certain introns, catalyze reactions themselves (ribozymes).

Bacteria generally do not have introns or caps and do not need a nucleus: their mRNA can be translated while it is still being transcribed, and a single bacterial mRNA often carries several genes (a **polycistronic** mRNA). Eukaryotic mRNA generally encodes one protein, is processed in the nucleus, and is exported to the cytoplasm before translation.

**The genetic code.** The code is read in triplets called **codons**. There are 64 codons: 61 specify amino acids and 3 are stop codons (UAA, UAG, UGA). AUG codes for methionine and is the usual **start codon**. The code is:

- **Degenerate (redundant):** most amino acids have more than one codon, often differing at the third position.
- **Unambiguous:** each codon specifies only one amino acid or a stop.
- **Nonoverlapping and continuous:** it is read without gaps from a fixed starting point, which sets the **reading frame**.
- **Nearly universal:** the same in almost all organisms (mitochondria use a few variations).

A few codons to know by heart appear below; on the exam a codon table is generally provided, so practice using one rather than memorizing it.

| Codon (5′ to 3′) | Amino acid | Codon (5′ to 3′) | Amino acid |
|---|---|---|---|
| AUG | Met (start) | UUU | Phe |
| GAG | Glu | GUG | Val |
| UGG | Trp | CCC | Pro |

**tRNA and the ribosome.** A **transfer RNA** is a short, folded RNA with an **anticodon** that pairs, antiparallel, with the mRNA codon, and an acceptor end (ending in CCA at the 3′ terminus) that carries the amino acid. **Aminoacyl-tRNA synthetases** attach each amino acid to the correct tRNA, using ATP; there is one enzyme for each amino acid, and their accuracy is critical because the ribosome checks only the codon-anticodon match, not the amino acid. Pairing at the third codon position is looser than at the first two (**wobble**), which is why fewer than 61 tRNAs are needed.

**Ribosomes** are made of rRNA and protein, with a small and a large subunit. Prokaryotic ribosomes are 70S (30S + 50S) and eukaryotic ribosomes are 80S (40S + 60S); this difference is a basis for antibiotics that inhibit bacterial ribosomes without much effect on human cytoplasmic ribosomes. The ribosome has three tRNA sites: **A** (aminoacyl; entry), **P** (peptidyl; holds the growing chain) and **E** (exit). The peptide bond is formed by catalytic activity of the large-subunit rRNA (it is a ribozyme).

**Translation steps.**

1. **Initiation.** The small subunit binds the mRNA and the initiator tRNA (carrying methionine; formylmethionine in bacteria) at the start codon AUG. In bacteria the ribosome is positioned by pairing between the mRNA's **Shine-Dalgarno sequence** and the rRNA; in eukaryotes the small subunit generally binds the 5′ cap and scans to the first AUG. Initiation factors help, and GTP is used. Then the large subunit joins.
2. **Elongation.** A charged tRNA enters the A site (an elongation factor with GTP helps), the peptide bond forms (the chain moves from the P-site tRNA onto the A-site amino acid), and the ribosome moves three nucleotides (**translocation**, another GTP). The ribosome reads mRNA 5′ to 3′ and the protein is made from its **N-terminus to its C-terminus**.
3. **Termination.** When a stop codon enters the A site, no tRNA matches it. A **release factor** binds instead, the polypeptide is released and the ribosome subunits separate.

Each amino acid added costs about four high-energy phosphate bonds in total (two to charge the tRNA, two GTP for entry and translocation), which makes protein synthesis a major part of a cell's energy budget [VERIFY].

**Post-translational events.** The polypeptide generally has to be modified or folded further. **Chaperones** assist folding. Proteins may be cleaved (insulin is made as a longer precursor), phosphorylated, glycosylated or tagged with lipids. Disulfide bonds form in the oxidizing environment of the ER and outside the cell. Signal sequences direct proteins to the ER, mitochondria or the nucleus. Proteins marked by **ubiquitin** are degraded by the proteasome, which is a major way of controlling protein levels ([Lesson 1](chapter:4) on folding).

Praxis Tip: Passages that change one amino acid or one step often hinge on the order of events: transcription, then processing, then export, then translation, then folding and modification. A drug or mutation affects that step and everything after it, but nothing before it.

**Gene regulation in bacteria: operons.** Bacteria group related genes into an **operon**: one promoter, an **operator** (a binding site for a repressor) and several structural genes transcribed together. A separate gene encodes the regulatory protein.

*The lac operon (inducible).* The *lac* operon encodes enzymes for using lactose: **lacZ** (β-galactosidase), **lacY** (permease) and lacA. The repressor, encoded by **lacI**, binds the operator and blocks RNA polymerase. When lactose is present, a lactose isomer (**allolactose**, the inducer) binds the repressor and releases it from the operator, so transcription can occur. A second control, by **CAP (catabolite activator protein)** bound to cAMP, switches the operon up when glucose is low. High glucose means low cAMP, so CAP does not activate and expression stays low even with lactose present. The operon is therefore maximally expressed only when lactose is present and glucose is absent.

| Lactose | Glucose | lac expression |
|---|---|---|
| Absent | Present | Off |
| Absent | Absent | Low (repressor bound) |
| Present | Present | Low |
| Present | Absent | High |

*The trp operon (repressible).* This operon encodes enzymes for making tryptophan. The repressor is made in an inactive form. When tryptophan is abundant, tryptophan acts as a **corepressor**: it binds the repressor, which then binds the operator and stops transcription. When tryptophan is scarce, the repressor stays inactive and the operon is transcribed. In inducible systems (lac) the small molecule inactivates the repressor; in repressible systems (trp) the small molecule activates it. Bacteria also have an additional mechanism for the trp operon, **attenuation**, which couples transcription termination to the availability of charged tRNA for tryptophan.

**Mutations in operons.** A mutated *lacI* gene that makes no functional repressor gives high expression whether or not lactose is present (constitutive expression). A mutation in the operator that prevents the repressor from binding gives the same result. A repressor that cannot bind the inducer ("super-repressor") blocks the operon permanently, so it is never induced. A mutation in the promoter generally reduces expression and cannot be rescued by an inducer.

**Eukaryotic regulation.** Eukaryotic genes are controlled by more layers of regulation:

- **Transcription factors** are proteins that bind specific DNA sequences. **Activators** increase transcription and repressors decrease it. Many have a DNA-binding domain (examples include zinc fingers, helix-turn-helix and leucine zippers) and a separate regulatory domain.
- **Enhancers** are DNA sequences, which can be thousands of base pairs from the gene, to which activators bind. DNA looping brings the bound factors, often through a protein complex called Mediator, into contact with the promoter. **Silencers** work similarly to decrease expression. Enhancers function regardless of orientation and often work in a tissue-specific way, which is how different cell types express different genes from the same genome.
- **Combinatorial control:** most genes are regulated by several factors acting together, so a small set of proteins can specify many patterns.
- **Hormone response elements:** steroid hormones diffuse into cells and bind intracellular receptors that act as transcription factors ([Lesson 16](chapter:22) will detail the hormone side).
- **Chromatin structure:** DNA wrapped tightly on nucleosomes (heterochromatin) is generally inaccessible; loosely packed DNA (euchromatin) is generally accessible and transcribed.

**Epigenetics.** Epigenetic marks are chemical changes to DNA or chromatin that alter gene expression without changing the DNA sequence and that can be passed to daughter cells.

- **DNA methylation:** methyl groups are added to cytosine, generally in CpG sequences. Methylation of a promoter is generally associated with silencing.
- **Histone acetylation:** **histone acetyltransferases (HATs)** add acetyl groups to lysine on histone tails, neutralizing positive charge, loosening the grip of the histone on DNA and generally increasing transcription. **Histone deacetylases (HDACs)** remove them, compacting chromatin and generally decreasing transcription.
- **Histone methylation:** its effect depends on which residue is modified; some marks are associated with silencing and some with activation.
- Examples: **X-chromosome inactivation** in female mammals and **genomic imprinting**, in which a gene is expressed depending on the parent of origin. Marks can be reversed, and environmental factors can influence them.

Praxis Tip: For chromatin, think charge. Acetylation removes the positive charge of lysine, so the DNA (negative) is held less tightly, and genes tend to turn on. Methylated DNA at a promoter tends to be switched off.

**RNA interference.** Small RNAs regulate gene expression after transcription. A long double-stranded RNA or a hairpin precursor is cut by the enzyme **Dicer** into short fragments (about 21 to 23 nucleotides). One strand is loaded into a protein complex called **RISC** (with an Argonaute protein). The RNA guides RISC to an mRNA with a complementary sequence. If pairing is nearly perfect, the mRNA is cleaved and degraded (the usual route for **siRNA**). If pairing is imperfect, as with many **microRNAs (miRNA)**, translation is blocked or the mRNA is destabilized. RNAi lowers the level of a protein without altering the gene, so scientists use it for **knockdown** experiments (see [Strategy: Reading Biology Experiments](chapter:3)), and it differs from a knockout, which changes the DNA.

**Worked Example 1: From template to peptide (skill: using the code)**

A template strand reads 3′-TACCGTAGCATT-5′. Write the mRNA and the peptide.

Pair each base: T pairs with A, A with U, C with G, G with C. The mRNA, written 5′ to 3′ alongside the template, is 5′-AUGGCAUCGUAA-3′. Split into codons: AUG, GCA, UCG, UAA. Using the table: Met (start), Ala, Ser, Stop. The peptide is Met-Ala-Ser, three amino acids. The common mistake is to read the template strand directly as if it were the mRNA, which would give UAC, CGU and so on, and the wrong answer.

**Worked Example 2: How long is the protein? (skill: exons, UTRs and codons)**

A pre-mRNA contains three introns. After splicing, the mature mRNA has exons totaling 750 nucleotides (excluding the cap and tail). The 5′ untranslated region is 90 nucleotides and the 3′ untranslated region is 120 nucleotides. How many amino acids does the protein have?

The coding region, including the stop codon, is 750 − 90 − 120 = 540 nucleotides. 540 / 3 = 180 codons. The last codon is the stop, which does not encode an amino acid, so the protein has 180 − 1 = 179 amino acids. The cap and poly-A tail are added without being encoded by the gene, and introns are removed before translation, so none of them contribute. If an intron were wrongly retained, the extra sequence would generally add codons or shift the frame.

**Worked Example 3: Predicting lac operon expression (skill: two-signal logic)**

An *E. coli* culture is moved to each of the four media below. Predict β-galactosidase (lacZ) expression. (a) Glucose only. (b) Lactose only. (c) Glucose and lactose. (d) A strain with no functional lacI repressor, grown with glycerol (no glucose) and no lactose.

(a) Glucose present, no lactose: the repressor is bound to the operator and cAMP is low: **off**. (b) Lactose present, no glucose: allolactose frees the operator and cAMP is high, so CAP activates: **high**. (c) Both: the repressor is released, but high glucose lowers cAMP, so CAP does not activate: **low** expression (the bacteria use glucose first). (d) The repressor is absent, so the operator is open, and with no glucose CAP is active: **high, constitutive**, even though no lactose is present. The general rule: the repressor decides whether transcription is allowed, and CAP decides how much.

**Worked Example 4: A frameshift in translation (skill: reading frame)**

The mRNA 5′-AUGGCAUCGUAA-3′ (Met-Ala-Ser-Stop) has one G inserted after the sixth nucleotide. Describe the result.

The new sequence is AUGGCAGUCGUAA. The first two codons are unchanged (AUG, GCA = Met, Ala). After the insertion the codons read GUC, GUA, A...: Val, Val and so on. The original UAA stop codon is no longer read in frame, so the ribosome continues until it meets some other stop codon, producing a different and probably longer or nonfunctional protein. If instead three nucleotides had been inserted, the downstream frame would be preserved and only one amino acid would be added. This ties directly back to the mutation classes in [Lesson 7](chapter:11).

**Worked Example 5: Reasoning about an epigenetic drug (skill: predicting a perturbation)**

Cells are treated with a histone deacetylase (HDAC) inhibitor. A tumor suppressor gene whose promoter region was silenced in these cells begins to be expressed. Explain, and predict what would happen to histone acetylation and chromatin.

HDACs remove acetyl groups from histone tails. Inhibiting them leaves more histones acetylated. Acetylation neutralizes the positive charge on lysine, loosening histone-DNA contact, so the chromatin around the gene opens, activators and polymerase can reach the promoter, and transcription rises. The DNA sequence has not changed, so the effect is epigenetic and, in principle, reversible when the drug is removed. A good control would be to measure acetylation at that promoter with and without the drug.

**More Praxis Tips**

Praxis Tip: To keep the strands straight, remember that the template strand is the one the polymerase reads, and the mRNA looks like the coding strand. "Coding" refers to the strand with the same sequence, not the strand that is read.

Praxis Tip: The mature eukaryotic mRNA is shorter than its gene (introns are gone) but has a cap and tail the gene did not encode. When a passage compares lengths on a gel, ask which RNA is being measured: pre-mRNA, mature mRNA or protein.

Praxis Tip: When an operon question looks hard, draw two boxes: the repressor (on or off the operator) and the activator (on or off the promoter). The repressor needs lactose to release; the activator needs low glucose to work.

Praxis Tip: Inducible versus repressible comes down to who the small molecule helps. If the ligand inactivates the repressor, the operon is inducible. If the ligand activates the repressor, it is repressible. Bacteria find it perfectly reasonable to run one of each.

Praxis Tip: Knockout versus knockdown: RNAi reduces mRNA, so a leftover signal is expected. A passage that reports partial protein loss after siRNA is not a contradiction.

Praxis Tip: Translation always proceeds N-terminus to C-terminus, and the ribosome moves along the mRNA 5′ to 3′. If you draw an arrow for each on scratch paper, direction questions become almost mechanical.

**Common Mistakes**

- Reading the template strand directly as if it were the mRNA.
- Forgetting that RNA contains uracil, not thymine.
- Counting the stop codon as an amino acid.
- Treating introns and exons as the opposite of what they are: introns are removed, exons stay.
- Saying that glucose directly blocks the lac operator; high glucose acts through lowered cAMP and CAP.
- Mixing up inducible and repressible operons.
- Saying that epigenetic changes alter the DNA sequence, or that they cannot be reversed.
- Describing RNAi as a change to the gene itself.

**Checkpoint Questions**

1. A template DNA strand reads 3′-TACAAAGGG-5′. Which peptide is encoded by the mRNA transcribed from it?
   A. Tyr-Lys-Gly
   B. Pro-Phe-Val
   C. Met-Phe-Pro
   D. Met-Leu-Pro

2. A mutation changes the GU at the 5′ end of one intron to GA, so that the splice site is not recognized. The most likely result is
   A. an abnormal mRNA in which the intron is retained or a neighboring exon is skipped
   B. no effect, because introns are discarded anyway
   C. loss of the promoter, so transcription never begins
   D. a protein with the correct sequence made at a lower rate

3. E. coli with a normal lac operon are grown in medium containing both glucose and lactose. Expression of lacZ is expected to be
   A. high, because the inducer releases the repressor, which is sufficient
   B. zero, because allolactose binds the operator and blocks polymerase
   C. high, because glucose directly activates the promoter
   D. low, because lactose releases the repressor but high glucose keeps cAMP low and CAP inactive

4. A bacterial strain has a mutation in trpR that makes a repressor unable to bind tryptophan but otherwise normal. Compared with a normal strain, when tryptophan is abundant the mutant will
   A. shut off the operon even more strongly
   B. continue to transcribe the trp operon at a high level
   C. transcribe the operon only in the absence of tryptophan
   D. produce more repressor bound to the operator

5. During translation, a ribosome moves a stop codon into the A site. What happens next?
   A. A tRNA with a matching anticodon carries the final amino acid
   B. The ribosome translocates and continues to the next codon
   C. A release factor binds the A site and the completed polypeptide is released
   D. The spliceosome removes the stop codon

6. Cultured cells are treated with a drug that inhibits histone deacetylases. Which result is the most likely?
   A. Increased histone acetylation and increased transcription of some genes, without a change in DNA sequence
   B. Decreased histone acetylation and tighter chromatin
   C. Mutation of the promoters of silenced genes
   D. Loss of all RNA polymerase activity

7. Researchers introduce a short double-stranded RNA complementary to the mRNA of gene X into cells. The expected result is
   A. a permanent deletion of gene X from the genome
   B. increased transcription of gene X
   C. unchanged gene X mRNA and protein, because RNA cannot bind RNA
   D. reduced mRNA and protein for gene X, with no change in the DNA sequence of gene X

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **C.** The mRNA is 5′-AUGUUUCCC-3′, read as AUG (Met), UUU (Phe), CCC (Pro). (A results from reading the template strand itself as if it were the mRNA; B results from reading the correct mRNA backward from 3′ to 5′; D needs a Leu codon, but the second codon UUU specifies Phe.)
2. **A.** Recognition of the splice site is needed to remove the intron and join the exons; if it fails the spliceosome may leave the intron in or skip an exon. (B the intron must be removed correctly for the mRNA to have the right sequence; C the splice site is not part of the promoter; D the sequence itself is altered when splicing fails.)
3. **D.** Expression requires both release of the repressor (lactose present) and activation by cAMP-CAP (glucose absent). (A ignores the need for CAP activation when glucose is high; B reverses the role of the inducer, which binds the repressor rather than the operator; C glucose acts through lowered cAMP and does not activate the promoter directly.)
4. **B.** Tryptophan is the corepressor that activates the repressor; if the repressor cannot bind it, the repressor never blocks the operator. (A the repressor must bind tryptophan to become active and bind the operator; C expression continues regardless of tryptophan in the mutant; D the unliganded repressor does not bind the operator.)
5. **C.** Release factors recognize stop codons, cause release of the polypeptide and allow the ribosome to dissociate. (A stop codons are not read by tRNAs; B the stop codon signals termination; D splicing occurs on pre-mRNA in the nucleus before translation.)
6. **A.** Blocking removal of acetyl groups leaves more acetylated, more open chromatin, which generally favors transcription. (B HDACs remove acetyl groups, so inhibiting them does the opposite; C the drug alters chromatin marks, not the DNA sequence; D the drug does not inhibit the polymerase itself.)
7. **D.** Dicer and RISC use the small RNA as a guide to find and cleave or repress the complementary mRNA, which is a knockdown. (A describes a knockout, whereas RNAi acts on the mRNA; B RNAi lowers expression rather than raising it; C complementary RNA readily base-pairs and guides RISC to the target.)

Praxis Tip: After the checkpoint questions, rewrite any miss as a one-line rule (for example, "template read 3′ to 5′, mRNA written 5′ to 3′") and add it to your error log ([Strategy: The Question Method](chapter:4)).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "RNA polymerase reads the template strand from a promoter and makes RNA 5′ to 3′; in eukaryotes the pre-mRNA is capped, tailed and spliced; ribosomes read codons 5′ to 3′ with tRNAs, building the protein from N to C and ending at a stop codon with a release factor; bacteria control genes in operons with repressors and CAP, eukaryotes use transcription factors, enhancers and chromatin marks such as methylation and acetylation, and small RNAs can silence mRNAs after transcription."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 1 and 3 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (mix with [Lesson 7](chapter:11) on mutations and Book 1, Lesson 23 on protein structure), and after 21 days (explain the lesson aloud and draw both operons).

*Interleave:* alternate a code-reading problem with an operon problem and a replication problem. Then move on to [Lesson 9](chapter:13) to see how scientists measure and manipulate everything in this lesson.

Praxis Tip: End each study session by drawing, from memory, a lac operon with repressor, operator and CAP, and then a eukaryotic gene with enhancer, promoter, exons, introns, cap and tail.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Verified by calculation: template-to-mRNA conversions and codon lookups (Met-Ala-Ser-Stop; Met-Phe-Pro); frameshift sequence; coding length (750 − 90 − 120 = 540 nt = 180 codons = 179 amino acids).
- Answer key positions: C, A, D, B, C, A, D.
- Verify with a molecular biology reviewer: polymerase I/II/III assignments; ATP/GTP cost per amino acid; lac operon table (note the low basal level when glucose is absent and lactose is absent); Shine-Dalgarno and scanning descriptions; Dicer fragment size; statements on histone methylation and heritability of epigenetic marks. Two cross-references ([Lesson 16](chapter:22) for hormones, [Lesson 1](chapter:4) for folding) assume the outline numbering.
- Category 1B topics covered: central dogma, transcription (RNA polymerase, promoters, termination), RNA processing, the genetic code, tRNA and ribosomes, translation steps, post-translational modification, lac and trp operons, eukaryotic regulation (transcription factors, enhancers), epigenetics (methylation, acetylation) and RNA interference.
