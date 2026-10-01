import pathlib
import re

root = pathlib.Path(r"A Trip Is Not a New Life - Manuscript")
files = sorted(root.glob("0*.md")) + sorted(root.glob("1*.md"))
text = "\n".join(
    p.read_text(encoding="utf-8")
    for p in files
    if p.name not in {"00_Chapter_Outline.md", "00_Status.md", "00_Front_Matter.md"}
)
parts = re.split(r"\n## ", text)
rows = []
for part in parts:
    match = re.match(r"(\d+)\.\s+([^\n]+)", part)
    if not match:
        continue
    words = len(re.findall(r"[A-Za-z0-9']+", part))
    rows.append((int(match.group(1)), words, match.group(2).strip()[:60]))
rows.sort()
for number, words, title in rows:
    print(f"{number:02d} {words:5d} {title}")
print("count", len(rows))
