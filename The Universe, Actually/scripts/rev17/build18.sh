#!/bin/sh
# Full REV18 rebuild: figures first (python figs_a.py ... figs_e.py, once), then from scripts/rev17:
set -e
OUT=../../The_Universe_Actually__REV18.docx
python rev17.py ../../bak/The_Universe_Actually__REV16.docx $OUT
python extras18.py $OUT
python expand18.py $OUT
python rhythm_tools.py apply $OUT
