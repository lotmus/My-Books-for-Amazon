Science Sparks - source files

The .md files are the text of the book (edit these, not the .docx).
Needs Python with python-docx and matplotlib; the print edition also needs Microsoft Word and pywin32.

    python make_figures.py                                              redraw figures/ (only after changing a figure)
    python build_almanac.py "..\Science Sparks.docx"                    Kindle edition
    python build_almanac.py --print "Science Sparks - Print.docx"
                                                                        6x9 print edition with page numbers, index and PDF
    python build_almanac.py --volume 1 "Science Sparks - Volume 1.docx"
                                                                        one volume of the three-volume set (1 to 3; add --print if wanted)

Sections (restructured 2 Oct 2026; superseded per-book sources are in D:\bak\2026-10-02 Science Sparks restructure):
    10_mathematics.md               Mathematics
    20_physics_and_cosmos.md        Physics and the Cosmos
    30_quantum_physics.md           Quantum Physics
    40_biology.md                   Biology
    50_science_in_the_novels.md     Science in the Novels
    90_glossary.md                  back glossary

Chapters are "## N. Title" and are numbered continuously through the whole book; "Chapter N"
anywhere in the text (and in the glossary) becomes a link to that chapter. If you insert or remove
a chapter, renumber the headings and the "Chapter N" references after it.

Section order and blurbs, front and back matter, figure placement (by chapter number), heading
style (centered, medium blue 1F4E9F) and the Also By list live in build_almanac.py.
Every chapter has a status line. The section files and build_almanac.py were generated from the
old per-book sources by a one-off restructure (2 Oct 2026); from now on edit them directly.

Status lines: a line "*Status: Settled.*" right under a chapter heading is styled as the
chapter's certainty label (Settled / Strange but solid / Serious but unconfirmed / Speculative).
