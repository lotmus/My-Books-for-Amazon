# Kindle file sizes (10 Oct 2026, PT)

Why: on the 70% royalty option KDP charges a delivery fee of about $0.15 per MB of the converted file. Target: about 2-3 MB per ebook.

"Est. MB" = image bytes plus the compressed text of the docx, which is a rough stand-in for KDP's delivered size. The KDP previewer shows the real number after upload.

How the shrink was done: photos became JPEG (q82-85, metadata stripped) at max 1600 px on the long side, or 1200/1000 px where a book was still over 3 MB. Diagrams and line art stayed PNG, palette-quantized (256 colours), max 1600 px (1200 px in The Universe Has No Now). The text, styles, rels IDs and part count are unchanged and checked by script. Every file was also opened and converted in LibreOffice. Separate cover files were not touched. Each original is in the book's bak\ folder as "<name> - 2026-10-10 pre-shrink.docx".

## Shrunk books

| Book | Before MB | After MB | Images | Notes |
|---|---|---|---|---|
| Physics, Actually Vol 2 | 22.44 | 2.03 | 12 | photos 1200 px; interior back cover redrawn as plain text |
| The Universe Has No Now | 14.24 | 4.52 | 54 | photos 1000 px, diagrams 1200 px; STILL OVER |
| Schrodinger's Paperwork (Lolly 1) | 9.97 | 2.81 | 21 | photos 1000 px; front cover 953x1200 JPEG q80 (3,804 KB to 287 KB); back cover redrawn as plain text (2,905 KB to 60 KB) |
| Physics, Actually Vol 1 (Kindle ebook file) | 9.93 | 2.59 | 22 | photos 1200 px |
| Life, Actually | 9.67 | 3.63 | 50 | photos 1000 px; STILL OVER |
| The Murder That Hadn't Happened Yet (RIB 1) | 8.25 | 1.24 | 5 | |
| Math, Actually Vol 4 | 8.18 | 3.04 | 114 | borderline |
| Quantum, Actually Vol 2 | 8.08 | 3.40 | 123 | 1.15 MB of it is text (353k words); STILL OVER |
| Quantum, Actually Vol 1 | 7.84 | 3.04 | 39 | photos 1000 px; borderline |
| Math, Actually Vol 2 | 7.41 | 2.78 | 114 | |
| Math, Actually Vol 3 | 6.96 | 2.62 | 102 | |
| Math, Actually Vol 1 | 5.34 | 2.06 | 97 | |
| Gravitation, Actually Rev8 | 4.23 | 1.62 | 16 | |
| A Trip Is Not a New Life | 3.47 | 2.57 | 46 | |
| Science Sparks | 1.98 | 0.97 | 20 | |
| EE Book 2, Circuits, Components, and Control | 1.80 | 0.62 | 34 | |
| EE Book 1, Foundations of Electronics | 1.69 | 0.59 | 38 | |

No images, already small (MB): EE Books 3-7 0.13-0.15; In Love with Murder 0.19; Permitted Options 0.23; Physics Vol 3 0.14; Protocol Flamingo 0.25; Dolphins 0.17; Warning (RIB 2) 0.16; The Universe, Actually 0.43; The Will Is Not the Legacy 0.19.

## Not modified (audit only)

| Book | Now MB | Possible MB | Why not touched |
|---|---|---|---|
| Auswandern REV115 (published) | 3.30 | 2.09 | published |
| How to Publish Your First Kindle Book REV40 (published) | 2.00 | 1.33 | published; REV40 re-upload pending anyway |
| Your First YouTube Channel REV21 (published) | 1.13 | 0.67 | published; REV21 re-upload pending anyway |
| Bavarian Cooking Made Simple | 5.44 (was 16.9 at audit) | about 5.4 at 1600 px | being worked on elsewhere; 122 recipe photos at about 1000 px already |
| Physics Vol 1 "(KDP UPLOAD)" (paperback file) | 9.93 | 4.19 | print file; keep full resolution for print |

## Still over 3 MB: split proposals (Lothar decides)

| Book | Split point | Half 1 | Half 2 | Suggested titles |
|---|---|---|---|---|
| Quantum, Actually Vol 2 | before Part V (Quantum Field Theory) | Parts 0-IV, about 158k words, about 1.7 MB | Parts V-XI + back matter, about 195k words, about 1.7 MB | Quantum, Actually, Volume 2: A QED Course, Part 1, From Light to Classical Fields / Part 2, From Quantum Fields to Deep QED |
| The Universe Has No Now | before Part VI (Getting There Anyway) | Parts I-V, about 46k words, about 2.4 MB | Parts VI-X + Appendix + Notes, about 62k words, about 2.1 MB | The Universe Has No Now, Book 1: No Now, No Centre / Book 2: Getting There Anyway |
| Life, Actually | before Ch 50 (Cutting and Pasting) | Ch 1-49 (first cell to Mendel and eugenics), about 110k words, about 1.4 MB | Ch 50-84 (biotech, cloning, genomes, editing, life elsewhere), about 86k words, about 2.2 MB | Life, Actually, Vol 1: From the First Cell to Mendel's Peas / Vol 2: From the Edited Genome to Life Elsewhere |

Alternatives to splitting:
- Life, Actually: replacing about 10 decorative photos (listed below) with simple drawings saves about 1.3 MB and gives about 2.3 MB, which avoids the split.
- The Universe Has No Now: the 6 mood photos below save about 0.85 MB and give about 3.7 MB. That's not enough on its own, so it needs those photos plus a split, or it ships at about 4.5 MB (about $0.68 per sale in delivery fees).
- Quantum Vol 2 is mostly text, so pictures can't fix it; it needs the split.

## Prose tightening estimate (no prose edited)

Assumes cutting about 10% of the non-exercise prose (repetition and padding), never exercises or worked solutions.

| Book | Words | Exercise/solution words | Exact repeated sentences (words) | Tightening could cut | MB saved | Avoids split? |
|---|---|---|---|---|---|---|
| Quantum, Actually Vol 2 | 352,862 | about 109,000 | 4,188 | about 25-30k words | about 0.09 | no (3.40 to about 3.31) |
| Life, Actually | 196,429 | about 2,300 | 72 | about 19k words | about 0.05 | no |
| The Universe Has No Now | 107,217 | about 760 | 369 | about 10k words | about 0.03 | no |
| Quantum, Actually Vol 1 | 98,487 | about 1,700 | 23 | about 10k words | about 0.035 | just reaches 3.0 |
| Math, Actually Vol 4 | 240,950 | about 33,800 | 2,904 | about 21-24k words | about 0.08 | reaches about 2.96 (not a split case) |
| The Universe, Actually | 166,213 | about 5,200 | 20,365 | about 20k duplicates plus about 14k | about 0.1 | n/a (0.43 MB); worth doing for length and quality |

The text costs about 3 bytes per word, so the MB problem comes from pictures; tightening shortens the reading, not the file.

## Photoreal and decorative pictures (proposals, not changed)

Physics, Actually Vol 1 (19 chapter openers) and Vol 2 (11 chapter openers): AI-painted infographics, each with a "Key idea" box and a "What we'll explore" list. They teach, so they were kept. Proposal: redraw each as a simple text-only card (title, key idea, bullets on a single colour), which would save about 1.8 MB (Vol 1) and 1.6 MB (Vol 2). Vol 1's card for "Motion Is a Matter of Perspective" has garbled AI text in its first caption.

The Murder That Hadn't Happened Yet: 3 lesson infographics (coordinates, black-hole clue, filing cabinet), which teach. Keep.

Quantum, Actually Vol 1: 14 infographics (prologue crossroads, quantum world, entanglement x2, cat, philosophy, fields, QCD, QED, cryptography, computing, core ideas, simulation, quantum gravity), about 130-165 KB each. They teach; keep or redraw as cards. The prologue "crossroads" image (140 KB) is decorative: proposed for a simple drawing.

Life, Actually (captioned photos, about 90-225 KB each at 1000 px). Proposed for simple drawings (decorative): Fig 15 bare field in winter, Fig 29 limestone cave mouth (the caption says it is not confirmed as the site), Fig 30 ewe with lamb, Fig 31 litter of puppies, Fig 33 ears of corn, Fig 34 tomatoes on a market stall, Fig 35 poultry barn, Fig 43 server racks, Fig 46 whippet, Fig 47 newborn's feet. Keep (they teach or are historical): Fig 1 spit kit, Fig 2 The Eagle pub, Fig 5 bacterial colonies, Fig 16 Mendel's pea drawing, Fig 18 Augustinian abbey, Fig 19 fruit fly, Fig 20 Eugenics Record Office workers, Fig 27 blood tube, Fig 32 electron microscope, Fig 36 Svalbard vault, Fig 37 DNA sequencers, Fig 40 consumer saliva tube.

The Universe Has No Now. Proposed for simple drawings (mood): Fig 0 kitchen clock (141 KB), Fig 1 kitchen (89), Fig 25 Perseverance rover (146), Fig 32 tractor (169), Fig 33 vault door in snow (173), Fig 35 radio dish (209). Keep (astronomy that teaches): Sun, Andromeda, distant galaxies, NGC 4414, sky map, Bullet Cluster, Crab Nebula, M87* ring, M87 jet, Europa, Galapagos finch. This book is built from Figures\ by export\build_docx.py, so any change must also go into the build, or a rebuild restores the big files.

Gravitation, Actually: ISS cabin photo, Bullet Cluster and M87 photos, which teach. Keep.

## Caveat for script-built books

The Universe Has No Now (export/build_docx.py), and possibly Life, Math, Quantum 2 and Science Sparks, are built from scripts. A rebuild re-embeds the full-size source images unless the build also downsizes them.
