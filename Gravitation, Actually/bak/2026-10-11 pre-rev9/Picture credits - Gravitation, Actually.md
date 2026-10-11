# Picture credits: Gravitation, Actually

Recorded 2026-10-10. Every picture in `Gravitation, Actually - Rev8.docx` is listed here. Rev7 added four diagrams on 2026-10-10, and Rev8 replaced the three soft AI paintings the same day.

## Real images (credited, licence checked)

| Picture | Where | Credit line | Licence | Source |
|---|---|---|---|---|
| M87* black hole (first EHT image, 2019) | Chapter 7 | Event Horizon Telescope Collaboration | CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) | https://commons.wikimedia.org/wiki/File:Black_hole_-_Messier_87_crop_max_res.jpg (original release: ESO eso1907a / EHT) |
| Bullet Cluster 1E 0657-56, composite | Chapter 6 | X-ray: NASA/CXC/CfA/M. Markevitch et al.; optical: NASA/STScI, Magellan/U. Arizona/D. Clowe et al.; lensing map: NASA/STScI, ESO WFI, Magellan/U. Arizona/D. Clowe et al. | Public domain (NASA, PD-USGov-NASA) | https://commons.wikimedia.org/wiki/File:1e0657_scale.jpg (NASA release STScI-2006-39) |
| Fruit floating in the ISS (Rick Mastracchio, Unity node, 6 Feb 2014) | Chapter 1 (replaces the AI falling-cabin painting) | NASA | Public domain (NASA media usage guidelines; no endorsement implied) | https://images.nasa.gov/details/iss038e043011 (ISS038-E-043011), 1920×1275 "large" rendition |

All were resized (and M87 cropped) for print at 300 dpi. Licence wording was checked on the Commons file pages and is quoted in the book's caption and on its Picture credits page.

## Diagrams drawn for this book (matplotlib, 300 dpi, `diagrams.py`)

- Light clock (Chapter 2)
- Light cone (Chapter 2)
- Tidal stretching (Chapter 3)
- GPS clock budget (Chapter 3)
- Gravitational lensing (Chapter 6, replaces the murky galaxies picture)
- L-shaped LIGO layout (Chapter 8, replaces the wrong picture)

Added in Rev7 (`diagrams2.py`). These illustrate teaching ideas from Taylor & Wheeler, *Spacetime Physics* (1992), Taylor, Wheeler & Bertschinger, *Exploring Black Holes*, and Misner, Thorne & Wheeler, *Gravitation* (1973). They are drawn new and do not copy any figure from those books:

- Two surveyors / two observers (Chapter 2)
- Gradient as a stack of clock-rate surfaces (Chapter 4)
- Embedding diagram of the Schwarzschild space slice, after Flamm 1916 (Chapter 7)
- Kruskal–Szekeres map (Chapter 7)

Added in Rev8 (`diagrams3.py`):

- Two ants on a flat table and on a curved skin (Chapter 1, replaces the AI apple painting)
- The sheet and the clock-rate curve (Chapter 3, replaces the AI Earth–Moon funnel painting)

## Illustrations (made for this book, not photographs)

- Wormhole flask (`flask.jpg`)

Retired in Rev8, with copies in `bak/old_images/`: the falling cabin, the apple with two ants, and the Earth–Moon funnel. All three were AI paintings that looked soft at print size.

## MediaSearcher

MediaSearcher (D:\My_C#_Apps\MediaSearcher) has no command line; the only program with a `Main` is a self-test. Its sources include the NASA Image Library, Wikimedia Commons, Openverse, and the Smithsonian, so those sources were searched directly instead: the NASA Image and Video Library API, for "floating fruit space station" and "KC-135 weightless".

## Covers

- Front `Gravitation, Actually - Front Cover (Kindle) v2.jpg` and back `Gravitation, Actually - Back Cover v2.jpg`: the existing cover art with the old baked-in lettering painted out and new lettering set with Pillow (Cormorant SC, Source Sans Pro, both under the SIL Open Font License).
