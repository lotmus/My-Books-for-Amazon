# -*- coding: utf-8 -*-
"""Write manuscript_text.txt from the Word master, so the text and the docx agree.

Run this after anyone edits the master docx directly. rebuild_kindle.py turns the
text back into the same docx. Markup (one paragraph per line, blank line between):
  #### Title      book title (26 pt)        # X   Heading 1 (page break)
  ### X          bold centred subtitle      ## X  Heading 2
  ^ X            centred plain line         **X** Also-by group line
  - X            contents / Also-by entry   [[IMAGE file.jpg | alt text]]
  *x* italic     [text](#bookmark) internal link    [text](https://...) web link
  trailing {#name} sets a bookmark on that paragraph; a leading !! starts a new page.
Images are written to figures/ as rib1_figN.jpg (the bytes already in the docx).
"""
from __future__ import annotations
import re, sys
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MASTER = ROOT / "FINAL_REV11_The_Murder_That_Hadnt_Happened_Yet_KINDLE_READY.docx"
OUT = HERE / "manuscript_text.txt"
FIG = HERE / "figures"


def esc(s: str) -> str:
    return s.replace("*", "\\*")


def inline(p, part) -> str:
    out = []
    for el in p._p:
        tag = el.tag
        if tag == qn("w:r"):
            t = "".join(x.text or "" for x in el.iter(qn("w:t")))
            if not t:
                continue
            rpr = el.find(qn("w:rPr"))
            ital = rpr is not None and rpr.find(qn("w:i")) is not None and rpr.find(qn("w:i")).get(qn("w:val"), "true") not in ("0", "false")
            out.append(f"*{esc(t)}*" if ital and t.strip() else esc(t))
        elif tag == qn("w:hyperlink"):
            t = "".join(x.text or "" for x in el.iter(qn("w:t")))
            a = el.get(qn("w:anchor"))
            target = "#" + a if a else part.rels[el.get(qn("r:id"))].target_ref
            out.append(f"[{esc(t)}]({target})")
    s = "".join(out)
    return s.replace("**", "")  # adjacent italic runs merge


def main(master=MASTER, out=OUT, fig=FIG):
    d = Document(str(master))
    part = d.part
    fig.mkdir(exist_ok=True)
    lines, nimg, section = [], 0, ""
    for i, p in enumerate(d.paragraphs):
        x = p._p.xml
        marks = "".join(f" {{#{b.get(qn('w:name'))}}}" for b in p._p.iter(qn("w:bookmarkStart")))
        if "graphicData" in x:
            nimg += 1
            rid = re.search(r'r:embed="([^"]+)"', x).group(1)
            alt = re.search(r'descr="([^"]*)"', x)
            name = f"rib1_fig{nimg}.jpg"
            (fig / name).write_bytes(part.related_parts[rid].blob)
            alt = (alt.group(1) if alt else "").replace("&quot;", '"').replace("&amp;", "&").replace("&apos;", "'")
            lines.append(f"[[IMAGE {name} | {alt}]]{marks}")
            continue
        text = inline(p, part)
        if not text.strip():
            continue
        st = p.style.name
        runs = p.runs
        bold = bool(runs) and all(r.bold for r in runs if r.text.strip())
        size = next((r.font.size.pt for r in runs if r.font.size), None)
        centred = p.alignment is not None and int(p.alignment) == 1
        sa = p.paragraph_format.space_after.pt if p.paragraph_format.space_after else None
        if st == "Heading 1":
            section = p.text
            line = "# " + text
        elif st == "Heading 2":
            line = "## " + text
        elif bold and size == 26:
            line = "#### " + text
        elif bold and centred:
            line = "### " + text
        elif bold:
            line = "**" + text + "**"
        elif centred:
            line = "^ " + text
        elif sa in (1.0, 2.0) and (section.startswith("Also by") or section == "Table of Contents"):
            line = "- " + text
        else:
            line = text
        if st == "Normal" and p.paragraph_format.page_break_before:
            line = "!! " + line
        lines.append(line + marks)
    out.write_text("\n\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("Wrote", out, len(lines), "paragraphs,", nimg, "images")


if __name__ == "__main__":
    main(*(Path(a) for a in sys.argv[1:]))
