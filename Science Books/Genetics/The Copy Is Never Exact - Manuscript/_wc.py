import re
import pathlib

root = pathlib.Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Genetics\The Copy Is Never Exact - Manuscript")

def wc(text):
    lines = []
    for line in text.splitlines():
        if line.startswith("#"):
            continue
        if line.startswith("!["):
            continue
        if line.strip() == "---":
            continue
        lines.append(line)
    body = "\n".join(lines)
    words = re.findall(r"[A-Za-z0-9']+", body)
    return len(words)

fm = (root / "00_Front_Matter.md").read_text(encoding="utf-8")
idx = fm.find("## Prologue")
want = {"4.", "5.", "7.", "8.", "9.", "17.", "18.", "30."}
idx = fm.find("## Prologue")
print(f"{wc(fm[idx:]):5d}  PROLOGUE")
files = [
    "01_Part_One_Shape.md",
    "02_Part_Two_Molecule.md",
    "04_Part_Four_Monk.md",
    "07_Part_Seven_Copies.md",
]
for f in files:
    text = (root / f).read_text(encoding="utf-8")
    parts = re.split(r"(?=^## )", text, flags=re.M)
    for p in parts:
        m = re.match(r"## (\d+)\.", p)
        if not m:
            continue
        key = m.group(1) + "."
        if key not in want:
            continue
        title = re.match(r"## (.+)", p).group(1)
        print(f"{wc(p):5d}  {title}")
