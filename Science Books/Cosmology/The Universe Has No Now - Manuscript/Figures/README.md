# Figures — Book 1

46 slots: Fig 0 + Fig 1–45. One per chapter plus the prologue.

Live pixels: `figs/`

```
python draw_figs.py      # 26 diagrams + 20 framed photo slots
python fetch_photos.py   # 14 NASA/ESA/EHT/SDSS JPEGs + 6 Commons/Unsplash earthly JPEGs
python swap_photos.py    # copy any drop-in figNN.jpg into figs/
python build_docx.py     # Kindle 6x9 .docx; uses figNN.jpg if present
```

## Drop-in contract (all 20 photo slots are filled)

All six earthly slots (00, 01, 31, 32, 34, 42) hold Creative Commons / Unsplash photographs since 14 September 2026. To replace one with your own camera JPEG, put it here:

`Figures/fig00.jpg`  or  `Figures/figs/fig00.jpg`

Same pattern for **01, 31, 32, 34, 42**. Then:

```
python swap_photos.py
python build_docx.py
```

`figNN.jpg` replaces `figNN_slot.png`. No Markdown edit required.

See `CREDITS.md` for every photograph’s credit line.
