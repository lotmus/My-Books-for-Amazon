# Figures - Book 1

47 slots: Fig 0 + Fig 1-46. One per chapter plus the prologue. Plus 7 spacetime diagrams (SD1-SD7), added 3 Oct 2026.

Since 3 Oct 2026 (Chapter 30 split into 30 and 31) the printed figure number is the chapter number. File names did not change: `fig31`-`fig45` print as Figures 32-46, and `fig46.png` prints as Figure 31. The mapping is `CHAPTER_FIG` in `build_docx.py`.

Live pixels: `figs/`

```
python draw_figs.py              # 26 diagrams + 20 framed photo slots
python draw_spacetime_figs.py    # 7 spacetime diagrams (figs/sd1_...png to sd7_...png) + fig46.png
python fetch_photos.py           # 14 NASA/ESA/EHT/SDSS JPEGs + 6 Commons/Unsplash earthly JPEGs
python swap_photos.py            # copy any drop-in figNN.jpg into figs/
python build_docx.py             # Kindle 6x9 .docx; uses figNN.jpg if present
```

## Spacetime diagrams (3 Oct 2026)

Placed in the chapter text with Markdown image syntax and full alt text:
`![Spacetime Diagram N. caption](Figures/figs/sdN_name.png "alt text")`. `build_docx.py` sets the alt text as the image description for Kindle accessibility.

| File | Chapter | Shows |
|---|---|---|
| sd1_simultaneity.png | 1 | Two observers, two lines of simultaneity |
| sd2_light_cones.png | 3 | Past and future light cones, elsewhere |
| sd3_twin_proper_time.png | 5 | Twin paths, proper time |
| sd4_flrw_horizons.png | 26 | Expanding-universe light cones, horizons |
| sd5_ctc_vs_delay.png | 36 | Closed timelike curve vs. ordinary time delay |
| sd6_four_elsewheres.png | 38 | Four different "elsewheres" |
| sd7_foliation_worldline.png | 37 | Foliation vs. worldline |
| fig46.png | 31 | Liquid ranges of five solvents at 1 atm (Figure 31) |

## Drop-in contract (all 20 photo slots are filled)

All six earthly slots (00, 01, 31, 32, 34, 42) hold Creative Commons / Unsplash photographs since 14 September 2026. To replace one with your own camera JPEG, put it here:

`Figures/fig00.jpg`  or  `Figures/figs/fig00.jpg`

Same pattern for **01, 31, 32, 34, 42**. Then:

```
python swap_photos.py
python build_docx.py
```

`figNN.jpg` replaces `figNN_slot.png`. No Markdown edit required.

See `CREDITS.md` for every photograph's credit line.
