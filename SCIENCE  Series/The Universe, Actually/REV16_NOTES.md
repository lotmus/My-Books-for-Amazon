# The Universe, Actually — REV16 notes (11 Oct 2026, PT)

Master: `The_Universe_Actually__REV16.docx`. Markdown working copy: `The_Universe_Actually__REV16.md` (generated from the docx; the docx is the master). REV15 is in `bak/2026-10-11 pre-restructure/`. Build: `python scripts/rev16/rev16.py REV15.docx REV16.docx` (edit layer in `scripts/rev16/ops/b1-b23.py`, then part order, renumbering, Contents, links, figures). This is the only build; the REV15-era `scripts/make.py`, `structure.txt` and helpers are in `bak/2026-10-11 old-build-scripts/`.

## New arc: small to large, then life to knowledge
Introduction: Why Any of This Matters (old chapter 1, now unnumbered, includes the scale interlude and Figure 1).

- Part I, The Rules of Motion and Energy: 1 Motion, Force and Energy; 2 Heat and Disorder; 3 Waves, Sound and Light; 4 Electricity, Magnetism and Fields
- Part II, The Quantum World: 5 Quantum Rules and Quantum Matter (new opening primer: quanta, matter waves, wave function and Born rule, superposition, uncertainty, spin and statistics); 6 Measurement, Decoherence and Interpretations; 7 Entanglement and Bell's Theorem; 8 Quantum Information and Computation; 9 Quantum Field Theory and Electrodynamics
- Part III, Particles, Nuclei and Atoms: 10 Standard Model (Figure 2); 11 Beyond the Standard Model; 12 Dense Matter and the Strong Force; 13 Nuclei, Fission and Fusion; 14 Neutrinos; 15 Atoms and the Periodic Table; 16 Chemistry of Bonds and Reactions; 17 Solids, Soft Matter and Plasma
- Part IV, Space, Time and Gravity: 18-24 (special relativity, curved spacetime, relativity at work, gravitational waves, black holes, Hawking radiation, information question)
- Part V, Planets, Stars and Galaxies: 25 Solar System; 26 Small Bodies; 27 Planets Around Other Stars; 28 Stars and Stellar Remnants; 29 Fast Radio Bursts and High-Energy Messengers; 30 Galaxies and the Large-Scale Universe
- Part VI, The Universe as a Whole: 31 Expanding Universe; 32 A Universe With a Birthday (Figure 3); 33 Dark Matter and Dark Energy; 34 Quantum Gravity, Strings and the Multiverse; 35 Arrow of Time; 36 What Is Time?
- Part VII, Life: 37-47 (origin of life, cell, evolution and genetics, quantum biology, genome, CRISPR, synthetic biology, deep time, extremes, life elsewhere, human evolution)
- Part VIII, The Human Body and Mind: 48-55 (body, disease, microbiome, precision medicine, aging, brain, consciousness, other minds)
- Part IX, Earth, the Living Planet: 56-62 (structure of the Earth, climate, ecology, biodiversity, oceans, renewable energy, sustainability)
- Part X, Technology: 63-68 (information theory, codes, AI, robotics, biotechnology, space exploration)
- Part XI, How We Know, and What Comes Next: 69-76 (history of scientific thought, Four Maxes, method, mathematics, knowing and doubting, future challenges, possible futures, what would change in the guides)

77 numbered chapters became the Introduction plus 76 chapters; 544 sections became 508.

## Repetition merged (nothing lost; unique facts moved to the surviving copy)
Expansion (Hubble law twice, conflicting acceleration dates), relativity/GR record, black-hole thermodynamics and Hawking radiation, Unruh, AdS/CFT, Omega Point, string/M-theory, action principle (three sections), Casimir, neutrino mass, BEC, superconductivity, topological phases, quantum optics, Bell's theorem (four overlapping sections), Standard Model (four overlapping sections), Higgs, materials/soft matter/plasma, fast radio bursts (three sections), stellar vs nuclear nucleosynthesis, baryogenesis vs leptogenesis, pulsar timing arrays, black-hole imaging (moved into Black Holes), icy moons (life chapter now points to the Solar System chapter), habitable zone, human evolution, Neanderthals, Homo floresiensis, Reichenbach (five 'Further Integration' stubs folded in), EM waves, DNA pairing, periodic table history, twin paradox. Twenty 'Further Aspects' headings retitled by content or folded in. Thirty-odd cross-references are now live links ('Chapter N').

## Accuracy fixes
Scale interlude (grape/genome/universe comparisons were wrong); Friedmann equation (curvature term); dark-energy domination vs onset of acceleration; Hubble tension now ~5 sigma; Hawking temperature/lifetime example; GW catalog size; neutrino-mass bound (0.07-0.12 eV); NIF ignition 2022; Bell tests (2015 loophole-free, 2022 Nobel); PTA evidence 2023; Homo floresiensis dates and brain size; Shannon source-coding statement; Reichenbach common-cause paragraph (was self-contradictory); 'third-generation star'; Ganymede, Io, Enceladus details; Europa Clipper/JUICE dates.

## Other
- American spelling sweep extended (-ise/-isation stems, litre, catalyse, flavour, tunnelling, analogue).
- Bibliography: all 52 entries bookmarked; every title is a keyword link (Wikipedia, Open Library or publisher), no visible URLs; 15 in-text title mentions link to their entries.
- External Resources: 66 links de-duplicated and regrouped under the eleven parts.
- Seven diagrams, 800 px (see Fix pass below), inline, with captions and full alt text (Figure 1 two arcs; Figure 2 Standard Model chart, a picture of the table with the table text in the alt text; Figure 3 cosmic timeline).
- Contents rebuilt and fully linked (Note, Preface, Introduction, parts, chapters, Epilogue, every appendix item, About the Author, More Actually Books). Also-by unchanged (already has Gravity, Actually). Review line and bio unchanged.
- Words: 130,782 (REV15) -> 129,233 (REV16), after adding a ~550-word quantum primer and figure captions.

## Fix pass (11 Oct 2026, same day; closes the five open items)
1. Back cover redrawn, text only, single navy background (scripts/rev16/cover/backcover.py): new blurb in American spelling describing the eleven parts as two ladders; old cover in `bak/2026-10-11 pre-fixes/`.
2. `KDP_Description.md`: 2,600-character KDP HTML description (honest positioning against Bryson: findings rather than anecdotes, denser and more current, less comedy), 7 non-overlapping keywords that avoid title words, 2 categories plus alternatives.
3. Close fact read of the ~60% previously only scanned (ops b8-b18, 126 edits). Examples: Andromeda merger now ~50% in 10 Gyr (2025 Gaia/Hubble); KM3NeT 220 PeV neutrino; TXS 0506+056 and NGC 1068; cosmic-ray ankle 5 x 10^18 eV and suppression ~4 x 10^19 eV with the dipole; FitzGerald; neutron-star diameter (~25 km); Higgs fine-tuning 10^34; process-node names vs feature sizes; Ge band gap; PDB >200,000; Asgard archaea and two-domain tree; McClintock dates; Paulinella; end-Permian 80-90% marine species; cloned rhesus 2024; Casgevy and 2025 personalized base editor; ~100 trillion synapses; Jupiter ~95 moons and Red Spot record; lunar recession 3.8 cm/yr; Moon formation timescale; Late Heavy Bombardment and early instability; three interstellar objects incl. 3I/ATLAS; >6,000 exoplanets and the 1992 pulsar planets; AlphaFold Nobel 2024; Google 2024 below-threshold error correction; >1,000-qubit devices; Microsoft topological claim disputed; photosynthetic coherence downgraded; avian magnetoreception; Bohr effect wording; Penzias-Wilson and Alpher-Herman 1948. Unverifiable or wrong lines removed (e.g. 'no healthy primate from somatic cell', 'sterilized the surface', 'five octaves', Huygens even-dimension statement corrected). One earlier misaimed rewrite in Synthetic Biology fixed (the parts-registry paragraph is back).
4. Rhythm and tightening: about 140 staccato paragraphs rewritten into varied sentences with every fact kept (ops b8-b23). Paragraphs with runs of three or more very short sentences: 444 (REV15) -> 425 (REV16 first pass) -> 308; share of sentences under 8 words 28.7% -> 24.7%; mean sentence 11.7 -> 12.5 words. Four new teaching diagrams (scripts/rev16/figs2.py, drawn in matplotlib, 800 px, inline, captions and full alt text): Figure 2 electromagnetic spectrum (Light, ch. 3), Figure 4 stellar life cycle (ch. 28), Figure 6 tree of life (ch. 39), Figure 7 plate tectonics (ch. 56). Existing figures renumbered in reading order (Standard Model now 3, cosmic timeline 5); scales of the universe stays Figure 1.
5. Build: `scripts/rev16` is canonical (README there). Old REV15 build moved to bak.

Words: 130,782 (REV15) -> 129,233 (REV16 first pass) -> 128,791 (this pass), with four captions and rewrites added; no exercise or worked solution touched.

## Still open
- The short, declarative house style is deliberate in places (Epilogue, chapter codas); about 300 paragraphs still have a run of three short sentences. Another rhythm pass would help, but with diminishing returns.
- Categories: KDP may now allow three; the listing file names two as asked.
