# Canonical build for The Universe, Actually (REV16)

Run from this folder (scripts/rev16), with python-docx and matplotlib installed:

    python figs.py && python figs2.py        # redraw fig/fig1-fig8 (800 px)
    python rev16.py "../../bak/2026-10-11 pre-restructure/The_Universe_Actually__REV15.docx" ../../The_Universe_Actually__REV16.docx
    python tomd.py ../../The_Universe_Actually__REV16.docx > ../../The_Universe_Actually__REV16.md
    cd cover && python backcover.py          # text-only back cover (needs Source Serif Pro; set F to the font path)

ops/b1-b23.py hold every edit as data (sub, replace_p, delp, join, move, image, ...), applied in file-name order to REV15 paragraph indices. Old REV15 build (make.py, structure.txt and helpers) is in bak/2026-10-11 old-build-scripts/.
