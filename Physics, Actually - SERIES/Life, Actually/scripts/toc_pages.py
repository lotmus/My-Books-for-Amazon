"""Fill the Contents page numbers without needing Word: render the master to PDF with
LibreOffice, find the page each Contents entry starts on, and write notes/toc_pages.json,
which build_book.py uses as the cached PAGEREF results. Word will still refresh the
numbers itself (updateFields), so small pagination differences correct themselves.
Usage: python toc_pages.py "<built.docx>"   (needs soffice and pdftotext)"""
import os, re, sys, json, subprocess, tempfile
from docx import Document
src = sys.argv[1]; ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tmp = tempfile.mkdtemp()
subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, src], check=True, capture_output=True)
pdf = os.path.join(tmp, os.path.splitext(os.path.basename(src))[0] + ".pdf")
pages = subprocess.check_output(["pdftotext", "-layout", pdf, "-"]).decode("utf-8").split("\f")
def norm(s): return re.sub(r"[^a-z0-9]", "", s.lower())
d = Document(src); entries = []
for p in d.paragraphs:
    if p.style.name == "TOC Entry":
        anc = p._p.xpath(".//w:hyperlink/@w:anchor")
        if anc: entries.append((anc[0], p.text.split("\t")[0]))
start = next(i for i, pg in enumerate(pages) if "Also in This Series" in pg) + 1
out = {}; i = start
for anc, text in entries:
    key = norm(text)[:28]
    for j in range(i, len(pages)):
        head = norm(" ".join(pages[j].strip().splitlines()[:6]))
        if key and key in head:
            out[anc] = j + 1; i = j; break
missing = [t for a, t in entries if a not in out]
json.dump(out, open(os.path.join(ROOT, "notes", "toc_pages.json"), "w"), indent=0)
print("pages found", len(out), "of", len(entries), "missing", missing, "total pages", len(pages) - (1 if not pages[-1].strip() else 0))
