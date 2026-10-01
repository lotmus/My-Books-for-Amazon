# -*- coding: utf-8 -*-
import re
import zipfile
from pathlib import Path

ROOT = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First")


def words(text: str) -> int:
    return len(re.findall(r"\S+", text))


def docx_words(path: Path) -> int:
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8", "replace")
    text = re.sub(r"</w:p>", "\n", xml)
    text = re.sub(r"<[^>]+>", "", text)
    return words(text)


def chapter_words(path: Path):
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"(?=^## \d+\. )", text, flags=re.M)
    rows = []
    for part in parts:
        m = re.match(r"## (\d+)\. (.+)", part)
        if not m:
            continue
        rows.append((int(m.group(1)), m.group(2).strip(), words(part)))
    return rows


def docx_text(path: Path) -> str:
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8", "replace")
    text = re.sub(r"</w:p>", "\n", xml)
    text = re.sub(r"<[^>]+>", "", text)
    return text


print("INVOICE SPLIT")
folder = ROOT / "A Longer Life Is Not a New Body - Manuscript"
invoice = next(p for p in folder.glob("*.docx") if "Invoice" in p.name)
text = docx_text(invoice)
# Body starts at the second "1. Her Hands"
starts = [m.start() for m in re.finditer(r"(?m)^1\. Her Hands Still Age\s*$", text)]
print("starts", starts, "docx words", words(text))
body = text[starts[-1]:]
chunks = re.split(r"(?m)^(PART |\d+\. )", body)
# simpler: split on heading lines
lines = body.splitlines()
heads = []
buf = []
cur = None
for line in lines:
    if re.match(r"^\d+\. \S", line.strip()) and len(line.strip()) < 80:
        if cur:
            heads.append((cur, words("\n".join(buf))))
        cur = line.strip()
        buf = [line]
    elif line.strip().startswith("APPENDIX") or line.strip().startswith("Appendix"):
        if cur:
            heads.append((cur, words("\n".join(buf))))
            cur = line.strip()[:40]
            buf = [line]
    else:
        buf.append(line)
if cur:
    heads.append((cur, words("\n".join(buf))))
for title, n in heads:
    print(f"{n:5d}  {title[:70]}")

book = ROOT / "A Trip Is Not a New Life - Manuscript"
print("\nCHAPTERS")
total = 0
for p in sorted(book.glob("0*.md")) + sorted(book.glob("1*.md")):
    if p.name.startswith("00_") or p.name.startswith("11_"):
        continue
    for num, title, n in chapter_words(p):
        total += n
        print(f"{num:3d}  {n:5d}  {title}")
print("main", total)
app = words((book / "11_Appendix.md").read_text(encoding="utf-8"))
front = words((book / "00_Front_Matter.md").read_text(encoding="utf-8"))
print("appendix", app)
print("front", front)
print("all", total + app + front)
