Science Sparks - source files

The .md files are the text of each book (edit these, not the .docx).
Needs Python with python-docx and matplotlib; the print edition also needs Microsoft Word and pywin32.

    python make_figures.py                                              redraw figures/ (only after changing a figure)
    python build_almanac.py "Science Sparks.docx"          Kindle edition
    python build_almanac.py --print "Science Sparks - Print.docx"
                                                                        6x9 print edition with page numbers, index and PDF
    python build_almanac.py --volume 1 "Science Sparks - Volume 1.docx"
                                                                        one volume of the four-volume set (1 to 4; add --print if wanted)

Part order, bridges, front and back matter, figure placement, full-edition pointers and the
Also By list live in build_almanac.py. 12_glossary.md is the back glossary; references in it
("Physics 14", "Quantum Lectures 7") become links.

Status lines: a line "*Status: Settled.*" right under a chapter heading is styled as the
chapter's certainty label (Settled / Strange but solid / Serious but unconfirmed / Speculative).
