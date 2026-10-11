# Picture credits: Gravitation, Actually

Recorded 2026-10-11. Every picture in `Gravitation, Actually - Rev9.docx` and both covers are listed here. Rev7 added four diagrams on 2026-10-10, Rev8 replaced three soft AI paintings the same day, and Rev9 (2026-10-11) replaced the last AI painting (the wormhole flask) with a drawn diagram and replaced both covers.

## Real images (credited, license checked)

| Picture | Where | Credit line | License | Source |
|---|---|---|---|---|
| M87* black hole (first EHT image, 2019) | Chapter 7 | Event Horizon Telescope Collaboration | CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) | https://commons.wikimedia.org/wiki/File:Black_hole_-_Messier_87_crop_max_res.jpg (original release: ESO eso1907a / EHT) |
| Bullet Cluster 1E 0657-56, composite | Chapter 6 | X-ray: NASA/CXC/CfA/M. Markevitch et al.; optical: NASA/STScI, Magellan/U. Arizona/D. Clowe et al.; lensing map: NASA/STScI, ESO WFI, Magellan/U. Arizona/D. Clowe et al. | Public domain (NASA, PD-USGov-NASA) | https://commons.wikimedia.org/wiki/File:1e0657_scale.jpg (NASA release STScI-2006-39) |
| Fruit floating in the ISS (Rick Mastracchio, Unity node, 6 Feb 2014) | Chapter 1 | NASA | Public domain (NASA media usage guidelines; no endorsement implied) | https://images.nasa.gov/details/iss038e043011 (ISS038-E-043011), from the 1920×1275 rendition, scaled to 1200 px in Rev9 |

The M87 and Bullet Cluster photos are 800 px wide (photo rule). License wording was checked on the Commons file pages and is quoted in the captions and on the book's Picture credits page, where the Commons pages are linked.

## Diagrams and tables drawn for this book (matplotlib / Pillow)

Rev9 rule: pictures that must be read (diagrams, tables) are exempt from the 440 px photo rule. All diagrams are 1,100–1,600 px wide; the three tables are 1,600 px.

- `diagrams.py`: light clock, light cone, tidal stretching, GPS clock budget, gravitational lensing, LIGO layout
- `diagrams2.py` (Rev7): two surveyors, stack of clock-rate surfaces, embedding diagram, Kruskal map. These illustrate teaching ideas from Taylor & Wheeler, *Spacetime Physics* (1992), Taylor, Wheeler & Bertschinger, *Exploring Black Holes*, and Misner, Thorne & Wheeler, *Gravitation* (1973), drawn new, not copied.
- `diagrams3.py` (Rev8): two ants, the sheet and the clock-rate curve
- `diagrams4.py` (Rev9): surveyors redrawn (book's sign convention, −16; "5 km" on the distance line), embedding diagram (labels clear of the rings), Kruskal map (labels clear of the curves), and the new wormhole slice that replaces the AI flask
- `tables.py` (Rev9): the three number tables of Appendix B at 1,600 px

## AI images

None remain in Rev9. Retired, with copies kept: the falling cabin, the apple with two ants, the Earth–Moon funnel (Rev8, in `bak/old_images/`), the wormhole flask (Rev9, `bak/old_images/flask.jpg`), and the v2 covers built on AI art (Rev9, in `bak/`).

## Covers

- Front `Gravitation, Actually - Front Cover (Kindle) v3.jpg` (1600×2560) and back `Gravitation, Actually - Back Cover v3.jpg`: drawn from scratch by `src/cover9.py` (Pillow, NumPy): a falling apple strobed along a straight line on a spacetime grid with a light cone. No rubber sheet, no photographs, no AI image generator. Fonts: Cormorant SC, Cormorant Garamond, Source Sans Pro (SIL Open Font License). Title and author checked at 100 px wide.

## MediaSearcher

MediaSearcher (D:\My_C#_Apps\MediaSearcher) has no command line; its sources (NASA Image Library, Wikimedia Commons, Openverse, Smithsonian) were searched directly in Rev8.
