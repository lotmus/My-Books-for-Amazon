import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
files = sorted(root.glob("0*_Part_*.md")) + [root / "11_Appendix.md"]
text = "\n".join(p.read_text(encoding="utf-8") for p in files)
parts = re.split(r"(?m)^(?=## )", text)
rows = []
for part in parts:
    m = re.match(r"##\s+(\d+|A\d+)\.\s+(.+)", part)
    if not m:
        continue
    body = re.sub(r"!\[.*?\]\(.*?\)", " ", part)
    body = re.sub(r"^##.*$", " ", body, flags=re.M)
    words = re.findall(r"[A-Za-z0-9'’]+", body)
    rows.append((m.group(1), len(words), m.group(2).strip()[:60]))
rows.sort(key=lambda r: (0 if r[0][:1].isdigit() else 1, r[1]))
out = Path(__file__).with_name("_ch_words.txt")
lines = [f"{n:5}  {num:>4}  {title}" for num, n, title in rows]
out.write_text("\n".join(lines), encoding="utf-8")
