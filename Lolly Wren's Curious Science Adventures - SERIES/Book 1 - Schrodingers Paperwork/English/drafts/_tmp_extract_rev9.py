# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
from docx import Document
from pathlib import Path

path = Path(
    r"D:\My Books for Amazon\The Relativistic Investigation Bureau - SERIES\WORD\REV9_The_Murder_That_Hadnt_Happened_Yet_KINDLE_READY.docx"
)
out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_rev9_extract")
out.mkdir(exist_ok=True)
doc = Document(str(path))

chapters = []
current = None
for i, p in enumerate(doc.paragraphs):
    style = p.style.name if p.style else ""
    text = p.text.strip()
    if style == "Heading 11" and text:
        if text.upper().startswith("APPENDIX") or text == "APPENDIX":
            if current:
                chapters.append(current)
            current = None
            break
        if current:
            chapters.append(current)
        current = {"title": text, "start": i, "paras": []}
    elif current is not None:
        if text:
            current["paras"].append(text)

if current:
    chapters.append(current)

print("CHAPTERS FOUND:", len(chapters))
for c in chapters:
    safe = "".join(ch if ch.isalnum() or ch in " -_" else "_" for ch in c["title"])[:80]
    fpath = out / f"{safe}.txt"
    body = "\n".join(c["paras"])
    fpath.write_text(body, encoding="utf-8")
    print(f"{c['title']} | n={len(c['paras'])} | chars={len(body)} | {fpath.name}")
