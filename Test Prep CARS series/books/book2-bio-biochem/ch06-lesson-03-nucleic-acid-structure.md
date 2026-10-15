# Lesson 3: Nucleic Acid Structure

**What you will be able to do**

- Describe the parts of a nucleotide, the polarity of a strand, and how base pairing, stacking and the antiparallel arrangement build the double helix.
- Apply Chargaff's rules, and recognize when they do not apply (single-stranded genomes and RNA).
- Compare A-, B- and Z-form helices and explain the roles of the major and minor grooves.
- Use linking number, twist and writhe to reason about supercoiling, and predict what topoisomerases and their inhibitors do.
- Describe how DNA is packaged with histones into nucleosomes and chromatin, and how histone charge affects packing.
- Interpret melting curves, melting temperature (Tm), hyperchromicity, GC content and hybridization.
- Match each major class of RNA to its structural features.

**Why it matters for the exam**

This lesson is category 1B, the transmission of genetic information, at the level of structure. Nearly every later lesson in this part of the book (replication, transcription, gene regulation, laboratory techniques) assumes that you can look at a strand and know its polarity, its pairing partner, its shape and its packaging. Lab-technique passages (PCR, blotting, probes) are really melting and hybridization questions in disguise, so Tm and stringency are worth the time.

Book 1, Lesson 25 introduced nucleotides, phosphodiester bonds, base pairing and the idea of melting. This lesson does not repeat that material; it builds on it with helix geometry, topology, packaging and the thermodynamics of melting. If the words "antiparallel", "purine" or "phosphodiester" feel unfamiliar, reread that lesson first. Hydrogen bonding and stacking come from Book 1, Lesson 11, and the free-energy logic of melting from Book 1, Lesson 14.

Praxis Tip: Nucleic acid questions are structure-to-property questions. Whenever a passage describes a change (more GC, less salt, a nick, an acetyl group), ask what it does to charge, pairing or packing, then to stability.

**Concept Review**

**1. Nucleotide anatomy, briefly revisited.** A nucleotide has three parts: a base, a pentose and one to three phosphates. Numbering matters. The ring atoms of the base are numbered plainly (N1, C2, and so on) and the sugar carbons carry primes (1′ to 5′). The base is attached to C1′ of the sugar by an N-glycosidic bond, and the phosphate is attached at C5′. The 3′ carbon carries the hydroxyl that will form the next phosphodiester bond. Nucleosides are named adenosine, guanosine, cytidine, uridine and thymidine (with "deoxy" in front for the DNA versions, except that thymidine is usually written without it because thymine is nearly always found in DNA).

At physiological pH every phosphate in the backbone carries a negative charge. This single fact explains a large share of nucleic acid behavior: DNA is attracted to positively charged histones, repelled by its own other strand unless cations screen the charge, and migrates toward the positive electrode in gel electrophoresis ([Lesson 9](chapter:13)).

**2. What holds the double helix together.** Three kinds of interaction matter, and the exam likes to ask which is which.

- Covalent phosphodiester bonds hold each strand together. Breaking these (a nuclease, strong base for RNA) cuts the strand.
- Hydrogen bonds between complementary bases give specificity: A with T by two, G with C by three.
- Base stacking (van der Waals and hydrophobic contacts between the flat, adjacent base pairs) provides much of the stability. Stacking is also why the helix is stabilized by a nonpolar interior and why melting is accompanied by a change in UV absorbance.

The sugar-phosphate backbones are on the outside and the bases are on the inside. Because the two backbones are not directly opposite each other, the helix has two unequal grooves, the **major groove** and the **minor groove**. In the major groove the edges of the base pairs are more exposed and carry a more distinctive pattern of hydrogen bond donors and acceptors, so sequence-specific DNA-binding proteins generally read the DNA through the major groove. The minor groove is narrower and also carries some sequence information, and several small drug molecules bind there.

**3. Chargaff's rules, and their limits.** In double-stranded DNA, A = T and G = C, so the purines (A + G) equal the pyrimidines (T + C). These rules follow from base pairing and therefore apply only when every base has a partner. They do not hold for single-stranded genomes (some viruses), for single-stranded regions, or for RNA that is not base paired along its length. Chargaff's second observation, that the ratio of (A + T) to (G + C) differs between species but is similar in different tissues of one species, is the reason GC content is a species characteristic.

The practical test: if a sample reports A not equal to T, or G not equal to C, the nucleic acid is not an ordinary fully paired double helix. A viral genome with A = 23, U = 27, G = 26, C = 24 percent contains uracil (so it is RNA) and its percentages do not pair up, so it is presumably single-stranded.

**4. Helix forms: A, B and Z.** The same molecule can take different shapes depending on sequence and conditions.

| Feature | A form | B form | Z form |
|---|---|---|---|
| Handedness | Right | Right | Left |
| Bases per turn | about 11 | about 10.5 | about 12 |
| Shape | Short, wide | Long, narrow | Zigzag backbone |
| When it occurs | Dehydrated; RNA-RNA, RNA-DNA | Hydrated, physiological | Alternating purine-pyrimidine, high salt |

B-DNA is the standard cellular form: right-handed, about 2 nm across, with a rise of about 0.34 nm per base pair, so one turn (about 10.5 base pairs) spans about 3.6 nm. A-form is a shorter, wider right-handed helix. Double-stranded RNA and DNA-RNA hybrids generally adopt A-like geometry, partly because the 2′-OH of ribose favors that sugar pucker. Z-DNA is left-handed with a zigzag backbone and forms most readily in stretches of alternating purines and pyrimidines (for example repeated GC) at high salt or under negative supercoiling; its biological role is less certain than that of B-DNA, and the exam usually asks only for the contrasts above.

Praxis Tip: Handedness is the one place to be strict. A and B are right-handed. Z is the left-handed one (the letter Z zigzags, which helps).

**5. Supercoiling and topoisomerases.** A circular DNA with no free ends (a plasmid, a bacterial chromosome) or a long looped domain held at both ends cannot spin freely, so any over- or under-winding is trapped as strain. The strain is described by three quantities related by one equation.

Lk = Tw + Wr

- **Linking number (Lk):** the number of times one strand crosses the other in a closed molecule. It is an integer and changes only if a strand is broken.
- **Twist (Tw):** the number of helical turns of the strands about each other.
- **Writhe (Wr):** the number of times the helix axis crosses itself, which is the supercoiling.

A relaxed circle has Lk equal to its length in base pairs divided by the helical repeat (Lk₀). Cellular DNA is generally **negatively supercoiled** (underwound: Lk is lower than Lk₀). Underwinding stores energy that makes it easier to separate the strands, which helps replication and transcription. The degree of supercoiling is the superhelical density, sigma = (Lk − Lk₀) / Lk₀, and is typically a few percent and negative in cells.

Overwinding ahead of a replication fork or a transcribing polymerase creates positive supercoils that must be removed. **Topoisomerases** change Lk by cutting and resealing the backbone.

| Enzyme | Cut | ATP needed? | Effect |
|---|---|---|---|
| Type I | One strand | Generally no | Relaxes supercoils |
| Type II | Both strands | Yes | Passes a second duplex through the break |
| Gyrase (bacterial type II) | Both strands | Yes | Introduces negative supercoils |

A type I enzyme generally changes Lk by 1 per cycle through a single-strand break; a type II enzyme changes it by 2 per cycle. The covalent enzyme-DNA intermediate conserves the bond energy, so resealing needs no extra input. Bacterial gyrase is the target of the fluoroquinolone antibiotics, and some anticancer drugs trap eukaryotic topoisomerase II or I in the cut state [VERIFY drug-to-enzyme pairings if a question names one]. Because the cut ends are held by the trapped enzyme, the net effect of such a drug is DNA damage, which is why rapidly dividing cells are most affected.

Praxis Tip: Lk is an integer that cannot change without a break, so a question that changes Lk always involves a topoisomerase. A question that changes only Tw and Wr (for example, ethidium intercalation or histone wrapping) leaves Lk the same.

**6. Packaging: nucleosomes and chromatin.** A human cell's DNA is about 2 meters long and the nucleus is a few micrometers across, so the DNA must be compacted by roughly four orders of magnitude and yet remain accessible.

- The **nucleosome** is the basic unit: about 147 base pairs of DNA wrapped in roughly 1.65 left-handed turns around a **histone octamer** made of two copies each of H2A, H2B, H3 and H4. The wrapping is a form of negative supercoiling.
- Histones are small proteins rich in the basic amino acids lysine and arginine. Their positive side chains neutralize the negative phosphates of DNA, which is why the binding does not depend on sequence.
- Short **linker DNA** (often around 20 to 60 base pairs) connects nucleosomes, producing "beads on a string" about 10 nm across. **Histone H1**, the linker histone, binds near where DNA enters and leaves the nucleosome and helps fold nucleosomes into higher-order fibers.
- Fibers fold further into loops and, at mitosis, into condensed chromosomes.

**Heterochromatin** is densely packed and generally transcriptionally silent; **euchromatin** is more open and more accessible. The N-terminal tails of histones are modified chemically. **Acetylation** of lysine removes its positive charge, weakens the DNA-histone interaction and generally loosens chromatin (more gene expression). **Deacetylation** restores the charge and generally tightens it. Methylation of histones can either activate or repress depending on the residue and degree, and DNA methylation (often at cytosine in CG sequences) is generally associated with silencing. The regulatory consequences are the subject of [Lesson 8](chapter:12).

**7. Melting, Tm and hybridization.** Heating (or high pH, or low salt, or denaturants such as formamide) separates the strands. Single bases absorb UV light near 260 nm, but stacked bases in the helix absorb less, so when the helix melts the absorbance at 260 nm rises, the **hyperchromic effect** (a rise of up to about 30 to 40 percent). The **melting temperature (Tm)** is the temperature at which half the DNA is single-stranded, read off the midpoint of the absorbance versus temperature curve. Melting is cooperative, so the curve is sigmoidal and sharp.

Tm rises with:

- Higher GC content (three hydrogen bonds and strong stacking).
- Longer duplex length.
- Higher concentration of cations (Na⁺, Mg²⁺), which shield the repulsion between backbones.

Tm falls with lower salt, with denaturants (formamide, urea), and with mismatches. Because the thermodynamics is the usual one (ΔG = ΔH − TΔS, Book 1, Lesson 14), melting is favored at high temperature because the entropy of the freed strands wins.

**Annealing and hybridization.** On cooling, complementary strands re-form a duplex (renaturation, annealing). **Hybridization** is annealing between two strands from different sources, such as a labeled probe and a target in a blot or a primer and a template in PCR. Hybrids can be DNA-DNA, DNA-RNA or RNA-RNA. **Stringency** is how demanding the conditions are: high temperature, low salt and formamide favor only perfect (or near-perfect) matches, whereas low temperature and high salt let imperfectly matched strands stay together. Fast renaturation of a DNA sample means it is rich in repeated sequences, a classic result from older experiments.

**8. RNA structure.** RNA is generally single-stranded, but it folds back on itself to form short helices (stems) and unpaired regions (loops, bulges). Those helices are A-form, and in addition to Watson-Crick pairs RNA often contains the G-U **wobble pair**. The 2′-OH makes RNA more susceptible to hydrolysis, especially in base, and it is why RNA is a less stable storage molecule than DNA. Major classes:

- **mRNA:** carries the coding sequence. Eukaryotic mRNA has a 5′ cap (a modified guanine joined 5′ to 5′) and a poly-A tail at the 3′ end ([Lesson 8](chapter:12)).
- **tRNA:** about 76 nucleotides, folded into a cloverleaf in two dimensions and an L-shape in three. It has an anticodon loop that reads the codon and a 3′ CCA end to which the amino acid is attached. It contains many chemically modified bases.
- **rRNA:** the most abundant RNA in a cell; it forms the structural and catalytic core of the ribosome. The prokaryotic ribosome is 70S (30S + 50S) and the eukaryotic ribosome is 80S (40S + 60S).
- **snRNA:** small nuclear RNAs, part of the spliceosome.
- **miRNA and siRNA:** about 21 to 23 nucleotides, double-stranded precursors that guide silencing of complementary mRNA.
- **Ribozymes:** RNA molecules with catalytic activity. The peptidyl transferase activity of the ribosome is carried out by rRNA, and some introns self-splice.

Praxis Tip: Why DNA has thymine and RNA has uracil is a favorite. Cytosine slowly deaminates to uracil. If DNA normally contained uracil, repair enzymes could not tell a mutation from a legitimate base. Using thymine in DNA means any uracil is recognized as damage ([Lesson 7](chapter:11)).

**Worked Example 1: Chargaff and its limits (skill: reasoning)**

(a) A double-stranded DNA sample contains 18 percent thymine. Give the percentages of A, G and C. (b) A sample of nucleic acid isolated from a virus gives A = 31, G = 19, C = 21, T = 29 percent. Is it a double helix?

(a) A = T = 18 percent, so A + T = 36 percent. The other 64 percent is G + C, split evenly: G = C = 32 percent.

(b) A is not equal to T and G is not equal to C, so the sample is not a fully paired duplex. It is probably single-stranded DNA (or contains single-stranded regions). Chargaff's rules are consequences of base pairing; without pairing they do not apply.

**Worked Example 2: Reading a melting curve (skill: data)**

A 40-base-pair DNA solution has A260 = 0.40 at 25 °C. On heating, the reading plateaus at 0.52. (a) What is the hyperchromic increase? (b) At what absorbance is the Tm read? (c) A second DNA of the same length has higher GC content. How does its curve change?

(a) The increase is (0.52 − 0.40) / 0.40 = 0.30, or 30 percent. (b) The Tm is where the strands are half melted: A260 = (0.40 + 0.52) / 2 = 0.46. Find that absorbance on the curve and read the temperature. (c) The curve has the same shape but shifts to the right (higher Tm), because more G–C pairs must be broken.

**Worked Example 3: Supercoiling arithmetic (skill: quantitative reasoning)**

A closed circular plasmid has 4,200 base pairs. Relaxed B-DNA has 10.5 base pairs per turn. The isolated plasmid has Lk = 380. (a) What is Lk₀? (b) What is the superhelical density? (c) How many cycles of a type II topoisomerase (change in Lk of 2 per cycle) would fully relax it?

(a) Lk₀ = 4,200 / 10.5 = 400. (b) ΔLk = 380 − 400 = −20, and sigma = −20 / 400 = −0.05: the plasmid is negatively supercoiled (underwound by 5 percent). (c) To raise Lk from 380 to 400 by 2 per cycle takes 10 cycles. A type I enzyme with a change of 1 per cycle would take 20.

**Worked Example 4: Counting nucleosomes (skill: quantitative reasoning)**

A 10,000-base-pair stretch of chromatin has nucleosomes with 147 bp of wrapped DNA and an average of 53 bp of linker DNA. How many nucleosomes does it contain, and how many core histone proteins?

Each repeat is 147 + 53 = 200 bp. The stretch holds 10,000 / 200 = 50 nucleosomes. Each octamer has 8 core histone proteins (H2A, H2B, H3, H4, two of each), so 50 × 8 = 400 core histone proteins, plus roughly one H1 per nucleosome if it is present.

**Worked Example 5: Designing a probe (skill: research design)**

A researcher wants a probe to detect the sequence 5′-CTGTAATC-3′ in a single-stranded target. Write the probe, state which conditions favor specific binding, and say what happens if a mismatch is present.

The probe must be the reverse complement of the target: complement is GACATTAG written 3′ to 5′, so the probe is 5′-GATTACAG-3′. High stringency (higher temperature, lower salt, or formamide) allows only perfect matches to remain paired. A single mismatch lowers the duplex Tm, so at high stringency the mismatched hybrid is likely to dissociate, which is how a probe can distinguish a single-base difference.

**More Praxis Tips**

Praxis Tip: To write a complementary strand, complement every base and then reverse the whole thing to read 5′ to 3′. Check your answer by pairing the 5′ end of one strand with the 3′ end of the other.

Praxis Tip: "Which melts first?" Count G and C. A short, AT-rich duplex at low salt melts first; a long, GC-rich one at high salt melts last.

Praxis Tip: When a question mentions positive charge on a histone (lysine, arginine), connect it immediately to the negative phosphate backbone. Neutralize the positive charge (acetylation) and the grip loosens.

Praxis Tip: Lk changes only by breaking a strand. If a molecule was nicked in the passage, it can relax; if it is intact and closed, it cannot.

Praxis Tip: Distinguish the three kinds of "bond" in DNA questions: covalent phosphodiester (backbone), hydrogen bonds (between bases, break on melting) and stacking (nonpolar, also lost on melting). Melting breaks the last two and leaves the first.

Praxis Tip: If a question says an RNA is "double-stranded in one region", it is describing a hairpin or stem, and that region is A-form with possible G-U wobble pairs. Do not apply Chargaff to the whole molecule.

Praxis Tip: Many laboratory methods are the same trick: heat to melt, cool to anneal, then ask who finds whom. Keep that sentence in your head when you reach [Lesson 9](chapter:13).

**Common Mistakes**

- Applying Chargaff's rules to single-stranded DNA or to RNA.
- Saying the hydrogen bonds hold the strand together in the backbone, or that melting breaks phosphodiester bonds.
- Calling B-DNA left-handed, or Z-DNA right-handed.
- Thinking that linking number can change without a strand break.
- Forgetting that acetylation removes the positive charge on lysine.
- Predicting that lowering salt raises Tm (it lowers Tm).
- Writing a probe in the same direction as its target instead of the reverse complement.
- Treating the rule "A pairs with T" as true for RNA (A pairs with U).

**Checkpoint Questions**

1. A research team sequences the genome of a newly isolated virus and finds the base composition A = 28 percent, U = 22 percent, G = 31 percent, C = 19 percent. The most reasonable conclusion is that the genome is
   A. double-stranded DNA, because the percentages sum to 100
   B. double-stranded RNA, because A and U are both present
   C. single-stranded RNA, because it contains uracil and its bases are not paired in equal amounts
   D. single-stranded DNA, because G is the most abundant base

2. Which description matches Z-DNA?
   A. A left-handed helix with a zigzag backbone that forms readily in alternating purine-pyrimidine stretches
   B. A right-handed helix that predominates in hydrated cellular DNA
   C. A short, wide right-handed helix typical of RNA-RNA duplexes
   D. A single-stranded coil that has lost its base pairing

3. A closed circular plasmid isolated from bacteria is incubated with a topoisomerase and a trace of ATP is added. A gel shows that the plasmid is now less supercoiled, and the enzyme transiently cut only one strand. The enzyme is most likely
   A. a type II topoisomerase, which cuts both strands in each cycle
   B. DNA ligase, which seals nicks but cannot change linking number by itself
   C. a helicase, which unwinds DNA at a replication fork using ATP
   D. a type I topoisomerase, which relaxes supercoils through single-strand breaks

4. Cells are treated with a drug that inhibits histone deacetylases. Compared with untreated cells, the drug-treated cells will most likely show
   A. fewer acetylated lysines, tighter chromatin and reduced transcription
   B. more acetylated lysines on histone tails, weaker DNA-histone interaction and a more open chromatin state
   C. loss of histones from the DNA, because acetylation breaks the nucleosome into monomers
   D. more negative charge on the histone, tighter binding to DNA

5. A DNA sample shows the following absorbance at 260 nm as it is heated: 0.40 at 60 °C, 0.41 at 70 °C, 0.50 at 75 °C, 0.58 at 80 °C, 0.60 at 90 °C. The melting temperature is closest to
   A. 75 °C, the temperature at the midpoint between the lowest and highest absorbance
   B. 60 °C, where the absorbance is lowest
   C. 70 °C, where the curve first begins to rise
   D. 90 °C, where the curve reaches its plateau

6. Two 30-base-pair DNA duplexes are compared. Duplex X is 70 percent G+C and duplex Y is 30 percent G+C. Which change would make the Tm of duplex X fall below that of duplex Y in the same buffer?
   A. Raising the Na⁺ concentration of X's buffer
   B. Making duplex X longer
   C. Adding a high concentration of formamide to X only
   D. Replacing some A–T pairs of X with G–C pairs

7. Which feature is characteristic of tRNA?
   A. A 5′ cap and a long poly-A tail
   B. A fully double-stranded structure of equal A and U content
   C. A DNA-like backbone lacking the 2′-OH group
   D. A cloverleaf secondary structure with an anticodon loop and a 3′ CCA end that accepts an amino acid

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **C.** Uracil identifies RNA, and the unequal A/U and G/C values show the bases are not all paired. (A a total of 100 percent is true of any complete composition and says nothing about strandedness, and uracil rules out DNA; B if the RNA were fully paired, A would equal U and G would equal C, which they do not; D base abundance does not indicate DNA, and the presence of uracil points to RNA.)
2. **A.** Z-DNA is the left-handed form. (B describes B-DNA; C describes A-form; D describes melted DNA, not a helix form.)
3. **D.** Changing Lk requires a strand to be cut, and a single-strand break with relaxation points to a type I enzyme. (A the observation was a single-strand cut, so a double-strand cutter is not consistent; B a ligase does not cut, so it cannot relax the plasmid; C a helicase separates strands and does not change the linking number of a closed circle by passing a strand through a break.)
4. **B.** Blocking deacetylation raises acetylation, which neutralizes lysine charge and generally loosens chromatin. (A describes the opposite of what blocking a deacetylase does; C acetylation loosens histone contacts but does not dissolve the nucleosome; D acetylation removes positive charge, which weakens attraction to the phosphates.)
5. **A.** The midpoint absorbance is (0.40 + 0.60) / 2 = 0.50, which occurs at 75 °C. (B the lowest absorbance corresponds to fully double-stranded DNA, not to half-melted DNA; C the start of the rise is not the midpoint; D the plateau corresponds to fully melted DNA.)
6. **C.** Formamide destabilizes hydrogen bonding and lowers Tm; the other options raise it. (A higher cation concentration shields the backbone repulsion and raises Tm; B a longer duplex generally has a higher Tm; D more G–C pairs raise Tm.)
7. **D.** tRNA folds into a cloverleaf, reads the codon through its anticodon and carries the amino acid at its 3′ CCA end. (A these are features of eukaryotic mRNA; B tRNA is single-stranded with limited internal pairing, so Chargaff's rules do not apply to the molecule; C tRNA is RNA and has the 2′-OH group.)

Praxis Tip: After the checkpoint questions, name the slip behind each miss (Chargaff misapplied, direction of strand, charge on histones, salt effect) and log it in your error log ([Strategy: Learning Pathways and Systems Without Rote Memory](chapter:2)).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "A nucleic acid is a negatively charged, polar strand of nucleotides whose antiparallel complementary pairs and stacked bases form a right-handed B helix with major and minor grooves; closed circles are supercoiled and topoisomerases change linking number by cutting; histones with positive tails package DNA into nucleosomes unless acetylation loosens them; and the melting temperature, set by GC content, length and salt, tells you how strongly strands hybridize."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 1 and 3 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set that includes [Lesson 1](chapter:4) protein structure and Book 1, Lesson 25), and after 21 days (explain the lesson aloud to a patient friend or a plant).

*Interleave:* alternate a nucleic acid problem with a protein folding problem and a thermodynamics problem (Book 1, Lesson 14). Then go on to [Lesson 4](chapter:7) on bioenergetics.

Praxis Tip: End each session by drawing, on scratch paper, a nucleosome, a melting curve with its Tm marked, and the equation Lk = Tw + Wr, with one sentence explaining each.

---

**Author verification note (remove before publishing)**

- All passages, numbers and questions are original. Arithmetic checked: 4,200 / 10.5 = 400; sigma = −20 / 400 = −0.05; 10,000 / 200 = 50 nucleosomes and 400 core histones; hyperchromic 30 percent; reverse complement of CTGTAATC is GATTACAG.
- Answer key positions: C, A, D, B, A, C, D.
- Verify with a biochemistry reviewer: A/B/Z base pairs per turn; the statement that grooves differ in information content; linker length range; drug-to-topoisomerase pairing (marked); typical hyperchromic percentage; tRNA length; the 5′-5′ cap description.
- Category 1B topics covered: nucleic acid structure and the double helix, Chargaff, A/B/Z forms, grooves, supercoiling and topoisomerases, chromatin and histones, melting and hybridization, RNA classes.
