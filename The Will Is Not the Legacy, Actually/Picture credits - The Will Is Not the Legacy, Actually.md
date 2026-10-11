# Picture credits: The Will Is Not the Legacy, Actually

Checked 10 Oct 2026 (PT).

## Front and back covers

- **Images:** none from third parties. No photographs and no stock or AI-generated images are used. The illustration (a folded will with a wax seal, a phone showing a play button, a checklist card) is drawn from simple shapes by `src/covers.py` and is original to this book.
- **Fonts** (all from Google Fonts, licensed under the SIL Open Font License 1.1, which permits use in commercial products including book covers):
  - DM Serif Display (title)
  - Lora (subtitle and back-cover text)
  - Inter (author name and small print)
  - Caveat (the handwritten "My Will" on the illustration)
- **People:** none depicted. No real names appear on either cover.

## Interior

- **Five diagrams**, drawn by `src/diagrams.py` from lines, shapes, and text on coloured backgrounds (no photographs, no stock or AI-generated images, no third-party artwork, no people, no names, no brands). Font: Inter (SIL Open Font License 1.1). Each is an 800 px wide palette PNG, inserted inline (not floating):
  1. `src/diagrams/fig2_tod_vs_life_estate.png`: Figure 1, TOD deed vs. life estate deed (Case 11, Chapter 4).
  2. `src/diagrams/fig1_outside_the_will.png`: Figure 2, what passes outside the will (opening of Part Four).
  3. `src/diagrams/fig4_family_list_map.png`: Figure 3, the Family List map (Chapter 23).
  4. `src/diagrams/fig5_video_diary_setup.png`: Figure 4, video-diary setup (Chapter 27).
  5. `src/diagrams/fig3_first_ninety_days.png`: Figure 5, the first ninety days (Chapter 37).
- **Kindle format:** the interior contains no Word tables, text boxes, SmartArt, or columns; all former tables are set as headed lists.
- Rebuild the diagrams with `python3 src/diagrams.py`.

## Rebuilding

Run `python src/covers.py` from the book folder on the box (font paths point to the box's font directory). It writes:
- `The Will Is Not the Legacy, Actually - Front Cover (Kindle).jpg` (1600 x 2560 px, 300 dpi)
- `The Will Is Not the Legacy, Actually - Back Cover.jpg` (1600 x 2560 px, 300 dpi)
