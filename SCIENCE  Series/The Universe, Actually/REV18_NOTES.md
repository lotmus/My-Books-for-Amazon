# REV18 notes (11 Oct 2026)

Master: `The_Universe_Actually__REV18.docx` (5.3 MB, about 147,000 words, about 391 pages when rendered, 0 repeated sentences of five or more words, 140 internal links and none dead). REV17 and REV16 are kept in `bak/`.

## What changed since REV17
- **Photographs.** 17 real NASA images (public domain), placed beside the text they illustrate and credited in each caption: the Sun, the Southern Ring and Crab nebulae, an aurora from the Space Station, Jupiter, Saturn, Pluto and Charon, a gravitational lens, the Hubble eXtreme Deep Field, Andromeda, the galactic center, the Pillars of Creation, the Cosmic Cliffs, Europa, Earth, Perseverance, and the Apollo 11 flag. Figures are now numbered 1–64 in reading order. `A Note on Sources` carries a photograph-credits paragraph. Files, sources and credits: `scripts/rev17/photos/` (originals, `meta.json`), `getphotos.py`, `photos_reg.py`.
- **Further reading.** A paragraph at the end of each of the eleven Parts, drawn from the bibliography, and nine new bibliography entries (Kuhn, Lane, Popper, Ritchie, Russell, Seth, Shannon and Weaver, Singh, Weart).
- **Thin chapters expanded.** About 5,100 new words in new sections: Ch 51 Precision Medicine, 52 Aging, 66 Robotics, 67 Biotechnology, 68 Space Exploration (rocket equation, trajectories, space telescopes, what space does to a body), 70 Four Maxes (one new section per Max), 74 Future Challenges (open numbers in cosmos and life, how long problems take). Facts checked against what I know; none of them is from the Asimov PDFs.
- **Rhythm pass.** 313 staccato runs (three or more consecutive sentences of nine words or fewer) merged into flowing sentences, keeping every fact. 16 deliberate rhetorical runs were left (the "We do not know" list in the Introduction, the closing lines of the Epilogue, the hook triplet in Chapter 1, question lists, and the like). The scan is `rhythm_scan.py`; the fixes are in `rhythm_fix_01..08.py`.
- US spelling swept (analyzers, kilometers, program, metric tons).

## Rebuild
Figures once: `python figs_a.py` ... `figs_e.py` (in `scripts/rev17`). Then `sh build18.sh`, which runs `rev17.py` (REV16 to figures, hooks, questions, photos), `extras18.py` (Further Reading, bibliography, credits), `expand18.py` (new sections) and `rhythm_tools.py apply` (all `rhythm_fix_*.py`). Needs `bak/The_Universe_Actually__REV16.docx`.

## Open
- Photos are all NASA; no ESA or Commons pictures were added, so no attribution license needs tracking.
- The strict four-angle score of 8.9 was not re-run for REV18; pictures, depth and prose rhythm should move up.
- Other candidates for expansion: Chapters 12, 14, 23, 49, 50, 58–60 (about 1,000–1,100 words each).
- Cover and KDP description were not changed; KDP_Description.md could mention the NASA photographs.
