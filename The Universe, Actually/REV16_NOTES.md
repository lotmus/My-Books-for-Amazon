# The Universe, Actually — REV16 notes (11 Oct 2026, PT)

Master: `The_Universe_Actually__REV16.docx`. Markdown working copy: `The_Universe_Actually__REV16.md` (generated from the docx; the docx is the master). REV15 is in `bak/2026-10-11 pre-restructure/`. Build: `python scripts/rev16/rev16.py REV15.docx REV16.docx` (edit layer in `scripts/rev16/ops/b1-b7.py`, then part order, renumbering, Contents, links, figures).

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
- Three diagrams, 800 px, inline, with captions and full alt text (Figure 1 two arcs; Figure 2 Standard Model chart, a picture of the table with the table text in the alt text; Figure 3 cosmic timeline).
- Contents rebuilt and fully linked (Note, Preface, Introduction, parts, chapters, Epilogue, every appendix item, About the Author, More Actually Books). Also-by unchanged (already has Gravity, Actually). Review line and bio unchanged.
- Words: 130,782 (REV15) -> 129,233 (REV16), after adding a ~550-word quantum primer and figure captions.

## Open
- Back cover: garbled AI-generated lines in the third paragraph, 'reating', British 'behaviour', and 'seven connected worlds' (book now has eleven parts). Needs a redraw.
- No KDP description/keywords file in the folder.
- Only about 40% of the text was reread closely for facts; the rest was checked by similarity scans only.
- scripts/structure.txt and make.py still describe the REV15 build; REV16 builds from scripts/rev16.
