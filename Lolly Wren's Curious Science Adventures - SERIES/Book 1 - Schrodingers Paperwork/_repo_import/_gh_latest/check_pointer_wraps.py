# -*- coding: utf-8 -*-
from pathlib import Path
from lxml import etree
import zipfile

LIVE = Path(
    r"c:\Users\lomus\OneDrive\My Books for Amazon"
    r"\Lolly Wren's Curious Science Adventures - SERIES"
    r"\Book 1 - Schrodingers Paperwork"
    r"\Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx"
)
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

with zipfile.ZipFile(LIVE) as z:
    root = etree.fromstring(z.read("word/document.xml"))

print("=== all glPointer wraps ===")
for i, p in enumerate(root.findall(f".//{W}p")):
    for h in p.findall(f".//{W}hyperlink"):
        if h.get(f"{W}anchor") == "glPointer":
            vis = "".join(t.text or "" for t in h.findall(f".//{W}t"))
            t = "".join(x.text or "" for x in p.findall(f".//{W}t"))
            print(f"p{i} vis={vis!r}")
            print(f"   ctx=...{t[max(0,t.lower().find('pointer')-40):t.lower().find('pointer')+50]!r}")
