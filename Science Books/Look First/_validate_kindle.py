"""Validate Kindle docx files for Create-ready ingest."""
import zipfile, re, os
from pathlib import Path
from xml.etree import ElementTree as ET
from docx import Document
from docx.shared import Inches

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

FILES = [
    Path(r"D:\My Books for Amazon\Science Books\Look First\A Permit Is Not a City - Manuscript\A Permit Is Not a City - Kindle.docx"),
    Path(r"D:\My Books for Amazon\Science Books\Look First\The Body Keeps Its Own Clock - Manuscript\The Body Keeps Its Own Clock - Kindle.docx"),
    Path(r"D:\My Books for Amazon\Science Books\Look First\The Universe Has No Now - Manuscript\Figures\The Universe Has No Now - Kindle.docx"),
    Path(r"D:\My Books for Amazon\Science Books\Look First\The Universe Has No Now - Manuscript\export\The_Universe_Has_No_Now.docx"),
]


def validate(path: Path):
    print("====", path.name, "====")
    if not path.exists():
        print("MISSING"); return
    doc = Document(str(path))
    sec = doc.sections[0]
    w, h = sec.page_width.inches, sec.page_height.inches
    print(f"page {w:.2f}x{h:.2f} in  margins LRTB "
          f"{sec.left_margin.inches:.2f}/{sec.right_margin.inches:.2f}/"
          f"{sec.top_margin.inches:.2f}/{sec.bottom_margin.inches:.2f}")
    h1 = h2 = pics = credits = 0
    md_leaks = []
    for p in doc.paragraphs:
        style = p.style.name if p.style else ""
        if style == "Heading 1":
            h1 += 1
        elif style == "Heading 2":
            h2 += 1
        if style == "Figure Credit":
            credits += 1
        t = p.text or ""
        if re.search(r"\*\*[^*]+\*\*|!\[[^\]]*\]\(|%%TOC%%|^#\s", t):
            md_leaks.append(t[:80])
        for r in p.runs:
            pass  # image count comes from zip media below
    # count images via relationships
    img_count = 0
    with zipfile.ZipFile(path) as z:
        media = [n for n in z.namelist() if n.startswith("word/media/")]
        img_count = len(media)
        doc_xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
        breaks = doc_xml.count('w:type="page"')
        bookmarks = len(re.findall(r"w:bookmarkStart", doc_xml))
        hyperlinks = len(re.findall(r"w:hyperlink", doc_xml))
    print(f"H1={h1} H2={h2} images={img_count} page_breaks~={breaks} bookmarks={bookmarks} toc_links~={hyperlinks}")
    print(f"figure_credit_paras={credits}  md_leaks={len(md_leaks)}")
    if md_leaks:
        for m in md_leaks[:5]:
            print("  leak:", repr(m))
    ok = (
        abs(w - 6) < 0.05 and abs(h - 9) < 0.05
        and h2 >= 16
        and img_count >= 16
        and breaks >= 20
        and hyperlinks >= 10
        and credits == 0
        and len(md_leaks) == 0
    )
    print("KINDLE_CREATE", "READY" if ok else "NEEDS_FIX")
    print()


for f in FILES:
    validate(f)

# sync B1 export from Figures build if export exists and Figures is newer
src = Path(r"D:\My Books for Amazon\Science Books\Look First\The Universe Has No Now - Manuscript\Figures\The Universe Has No Now - Kindle.docx")
dst = Path(r"D:\My Books for Amazon\Science Books\Look First\The Universe Has No Now - Manuscript\export\The_Universe_Has_No_Now.docx")
if src.exists() and dst.parent.exists():
    import shutil
    shutil.copy2(src, dst)
    print("synced B1 export from Figures build")
