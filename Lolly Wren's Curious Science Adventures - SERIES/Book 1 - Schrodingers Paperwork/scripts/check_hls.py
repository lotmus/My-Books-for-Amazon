# -*- coding: utf-8 -*-
from pathlib import Path
from lxml import etree
import zipfile

LIVE = Path(
    r"D:\My Books for Amazon"
    r"\Lolly Wren's Curious Science Adventures - SERIES"
    r"\Book 1 - Schrodingers Paperwork"
    r"\Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx"
)
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

with zipfile.ZipFile(LIVE) as z:
    xml = z.read("word/document.xml")
    rels = z.read("word/_rels/document.xml.rels")
root = etree.fromstring(xml)
relroot = etree.fromstring(rels)
relmap = {rel.get("Id"): rel.get("Target") for rel in relroot}
paras = root.findall(f".//{W}p")

needles = [
    "There is a vulgar public explanation",
    "Those relations have a name",
    "Now you are asking the interesting question",
    "Somewhere else, a physicist would eventually explain why",
    "The usual tale says that a pair",
    "De Broglie’s 1924 doctoral thesis",
    "Lolly Wren’s Curious Science Adventures",
    "If a demo is down, the lecture still stands",
    "A barrier, she thought, was only ever a classical promise",
    "On the wavelength of a proton",
    "Once, a tutor had told her",
    "Quantum tunnelling",
]

for i, p in enumerate(paras):
    t = "".join(x.text or "" for x in p.findall(f".//{W}t"))
    for n in needles:
        if n in t:
            hls = []
            for h in p.findall(f".//{W}hyperlink"):
                a = h.get(f"{W}anchor")
                rid = h.get(R + "id")
                vis = "".join(x.text or "" for x in h.findall(f".//{W}t"))
                hls.append(f"anchor={a} rid={rid} tgt={relmap.get(rid,'')} vis={vis[:50]!r}")
            print(f"p{i} hls={len(hls)} | {t[:90]!r}")
            for h in hls:
                print("   ", h)
            break
