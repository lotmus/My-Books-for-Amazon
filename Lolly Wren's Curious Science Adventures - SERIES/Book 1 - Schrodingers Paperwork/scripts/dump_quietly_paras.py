# -*- coding: utf-8 -*-
from pathlib import Path
from docx import Document

LIVE = Path(
    r"c:\Users\lomus\OneDrive\My Books for Amazon"
    r"\Lolly Wren's Curious Science Adventures - SERIES"
    r"\Book 1 - Schrodingers Paperwork"
    r"\Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx"
)
d = Document(str(LIVE))
for i in (216, 365, 532, 746, 847, 1411, 1485, 1572, 1605, 1712, 1940, 1941, 1942, 1943):
    print(f"\n--- {i} ---\n{d.paragraphs[i].text}")
