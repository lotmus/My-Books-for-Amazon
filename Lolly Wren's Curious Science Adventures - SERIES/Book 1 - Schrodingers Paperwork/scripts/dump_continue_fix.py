# -*- coding: utf-8 -*-
from pathlib import Path
from lxml import etree
import zipfile
from docx import Document

LIVE = Path(
    r"c:\Users\lomus\OneDrive\My Books for Amazon"
    r"\Lolly Wren's Curious Science Adventures - SERIES"
    r"\Book 1 - Schrodingers Paperwork"
    r"\Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx"
)
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
out = Path(__file__).with_name("dump_continue_fix.txt")
lines = []
d = Document(str(LIVE))

def dump_range(a, b, label):
    lines.append(f"\n===== {label} {a}-{b} =====")
    for i in range(a, min(b+1, len(d.paragraphs))):
        t = d.paragraphs[i].text
        if t.strip():
            lines.append(f"{i}|{t}")

# bookmarks
with zipfile.ZipFile(LIVE) as z:
    xml = z.read("word/document.xml")
    rels = z.read("word/_rels/document.xml.rels")
root = etree.fromstring(xml)
relroot = etree.fromstring(rels)
relmap = {rel.get("Id"): rel.get("Target") for rel in relroot}

paras = root.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p")
lines.append(f"xml paras {len(paras)} docx paras {len(d.paragraphs)}")

# all bookmarks
bms = []
for bm in root.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}bookmarkStart"):
    name = bm.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}name")
    bms.append(name)
lines.append(f"\n=== bookmarks ({len(bms)}) ===")
for name in bms:
    if name and any(k in name.lower() for k in (
        "pointer", "zeno", "phase", "arrow", "feynman", "tunnel", "uncertain",
        "entangl", "clone", "measure", "schrod", "bell", "hawking", "pilot",
        "error", "negentr", "cat", "superpos", "basis", "decoher", "einselect",
        "lesson6", "lesson_6", "lecture6", "glossary"
    )):
        lines.append(f"  {name}")

lines.append("\n=== ALL bookmark names containing glossary-ish ===")
for name in bms:
    if name and not name.startswith("_"):
        lines.append(f"  {name}")

# sample hyperlink that is internal (anchor)
lines.append("\n=== sample internal hyperlinks (first 40 with anchor) ===")
n = 0
for i, p in enumerate(paras):
    for h in p.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hyperlink"):
        anchor = h.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}anchor")
        rid = h.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        htext = "".join(t.text or "" for t in h.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"))
        if anchor:
            lines.append(f"p{i} anchor={anchor!r} vis={htext[:70]!r}")
            n += 1
            if n >= 40:
                break
    if n >= 40:
        break

# novel youtube mapping
lines.append("\n=== novel youtube (p<2100) full ===")
for i, p in enumerate(paras):
    if i >= 2100:
        break
    for h in p.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hyperlink"):
        rid = h.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        tgt = relmap.get(rid, "")
        if tgt and "youtube" in tgt.lower():
            htext = "".join(t.text or "" for t in h.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"))
            lines.append(f"p{i} rid={rid} tgt={tgt}")
            lines.append(f"   vis={htext!r}")

# book entries wrongly youtube
lines.append("\n=== book-looking youtube (p>3060) ===")
for i, p in enumerate(paras):
    if i < 3058:
        continue
    texts = "".join(t.text or "" for t in p.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"))
    for h in p.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hyperlink"):
        rid = h.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        tgt = relmap.get(rid, "")
        htext = "".join(t.text or "" for t in h.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"))
        if tgt:
            lines.append(f"p{i} tgt={tgt[:100]} vis={htext[:60]!r} para={texts[:90]!r}")

dump_range(0, 20, "TITLE")
dump_range(2345, 2395, "LESSON 6")
dump_range(2570, 2635, "LESSON 12")
dump_range(2988, 3010, "GLOSSARY POINTER-ISH")
dump_range(3148, 3175, "ABOUT SERIES")

# find glossary pointer, tunnelling, path integral, phase
lines.append("\n=== glossary / lecture search ===")
keys = [
    "Pointer States", "pointer state", "Quantum Tunnelling", "Tunneling", "tunnelling",
    "Path integral", "Feynman", "Phase ", "Einselection", "Decoherence",
    "Lesson 6:", "Lesson 5:", "Going deeper (skip freely). By the early",
    "de Broglie", "nucleus", "wavelength", "garden square", "How to Read",
    "Further Reading", "Glossary",
]
for i, p in enumerate(d.paragraphs):
    t = p.text
    for k in keys:
        if k in t and (i > 2300 or k in ("garden square", "How to Read", "Glossary", "Further Reading")):
            lines.append(f"{i}|{t[:220]}")
            break

out.write_text("\n".join(lines), encoding="utf-8")
print("wrote", out, "lines", len(lines))
