# -*- coding: utf-8 -*-
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn

LIVE = Path(
    r"D:\My Books for Amazon"
    r"\Lolly Wren's Curious Science Adventures - SERIES"
    r"\Book 1 - Schrodingers Paperwork"
    r"\Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx"
)
d = Document(str(LIVE))
out = Path(__file__).with_name("continue_scan.txt")
lines = []

lines.append(f"paragraphs {len(d.paragraphs)}")
lines.append("=== youtube / http in body ===")
for i, p in enumerate(d.paragraphs):
    t = p.text
    if "youtube" in t.lower() or "http://" in t.lower() or "https://" in t.lower() or "youtu.be" in t.lower():
        lines.append(f"{i} {t[:400]}")

lines.append("\n=== pointer state ===")
for i, p in enumerate(d.paragraphs):
    t = p.text
    if "pointer" in t.lower() and ("state" in t.lower() or "st" in t.lower()):
        if "pointer" in t.lower():
            # show around pointer
            idx = t.lower().find("pointer")
            snippet = t[max(0, idx - 40): idx + 80]
            rels = []
            for rel in p._p.findall(".//" + qn("w:hyperlink")):
                rels.append(rel.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"))
            lines.append(f"{i} rels={rels} ...{snippet}...")

lines.append("\n=== title page / series ===")
for i in range(0, 20):
    t = d.paragraphs[i].text.strip()
    if t:
        lines.append(f"{i} {t[:200]}")

lines.append("\n=== rotating arrow / Feynman ===")
for i, p in enumerate(d.paragraphs):
    t = p.text
    if "rotating arrow" in t.lower() or "small rotating" in t.lower() or "turning arrow" in t.lower() or "spinning arrow" in t.lower():
        lines.append(f"{i} {t[:280]}")

lines.append("\n=== garden square / tunnelling ===")
for i, p in enumerate(d.paragraphs):
    t = p.text
    if "garden square" in t.lower() or "tunnel" in t.lower() and "grass" in t.lower():
        lines.append(f"{i} {t[:300]}")

lines.append("\n=== Lesson 12 going deeper ===")
for i, p in enumerate(d.paragraphs):
    if p.text.strip().startswith("Lesson 12:"):
        for j in range(i, min(i + 40, len(d.paragraphs))):
            if "Going deeper" in d.paragraphs[j].text or "wavelength" in d.paragraphs[j].text.lower():
                lines.append(f"{j} {d.paragraphs[j].text[:350]}")
            if d.paragraphs[j].text.strip().startswith("Lesson 13:"):
                break
        break

lines.append("\n=== grey counts in novel-ish range ===")
# just list paragraphs with grey/gray in first 2000 paras
count = 0
for i, p in enumerate(d.paragraphs[:2100]):
    if " grey" in p.text.lower() or " gray" in p.text.lower() or p.text.lower().startswith("grey"):
        count += 1
        if count <= 25:
            lines.append(f"{i} {p.text[:160]}")
lines.append(f"total grey mentions in first 2100: {count}")

out.write_text("\n".join(lines), encoding="utf-8")
print("wrote", out, "lines", len(lines))
