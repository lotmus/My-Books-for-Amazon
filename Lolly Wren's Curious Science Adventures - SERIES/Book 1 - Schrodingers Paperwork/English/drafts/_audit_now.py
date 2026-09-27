"""Extract and check the live BOOK_1_2 for a shipping audit."""

from __future__ import annotations

import re
import zipfile
from collections import Counter
from pathlib import Path

DOCX = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")
OUT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\English\_audit_extract_2026-09-14.txt")


def para_text(p: str) -> str:
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))


def style_of(p: str) -> str:
    m = re.search(r'<w:pStyle w:val="([^"]+)"', p)
    return m.group(1) if m else "Normal"


def main() -> None:
    with zipfile.ZipFile(DOCX) as z:
        xml = z.read("word/document.xml").decode("utf-8")
        styles = z.read("word/styles.xml").decode("utf-8")
        names = z.namelist()
        bad = z.testzip()
        media = [n for n in names if n.startswith("word/media/")]

    paras = re.findall(r"<w:p\b[^>]*>.*?</w:p>", xml, flags=re.DOTALL)
    texts = [para_text(p) for p in paras]
    words = [w for t in texts for w in t.split() if w]
    h1 = [(i, para_text(p).strip()) for i, p in enumerate(paras) if style_of(p) == "Heading1"]

    lines = []
    lines.append(f"file {DOCX} size {DOCX.stat().st_size}")
    lines.append(f"testzip {bad}")
    lines.append(f"paras {len(paras)} words {len(words)} media {len(media)}")
    lines.append(f"h1 {len(h1)} drawings {xml.count('<w:drawing')} inline {xml.count('<wp:inline')} float {xml.count('<wp:anchor')}")
    lines.append(f"de-DE {'de-DE' in xml} ember {'Amazon Ember' in xml} blue {'2E74B5' in styles}")
    lines.append(f"lastRendered {'lastRenderedPageBreak' in xml}")
    lines.append(f"hard_breaks {xml.count('w:type=\"page\"')}")
    lines.append("")
    lines.append("=== H1 ===")
    for i, t in h1:
        lines.append(f"{i:4d} {t}")

    needles = {
        "ch16_plan": "The plan reached the judge",
        "old_tuesday": "The injunction itself was granted on the Tuesday",
        "notes_continued": "Physics Notes (continued)",
        "back_hook": "Somewhere in a government basement",
        "ten_years": "ten years",
        "forty years": "forty years",
        "eleven minutes": "eleven minutes",
        "S = 2.41": "2.41",
        "Mrs Chain": "Mrs Chain",
        "Gideon": "Gideon",
        "Curious Science": "Curious Science Adventures",
    }
    blob = "\n".join(texts)
    lines.append("\n=== NEEDLES ===")
    for k, n in needles.items():
        lines.append(f"{k}: {blob.count(n)}")

    # Ch15/16 neighborhood
    lines.append("\n=== CH15 TAIL / CH16 HEAD ===")
    for i, t in enumerate(texts):
        if texts[i - 1].startswith("Chapter 16:") if i else False:
            pass
    for i, t in enumerate(texts):
        st = style_of(paras[i])
        if "Chapter 15: Final" in t or "Chapter 16: The Decision" in t:
            for j in range(i, min(i + 12, len(texts))):
                lines.append(f"{j} [{style_of(paras[j])}] {texts[j][:220]}")
            lines.append("---")

    # back cover / about
    lines.append("\n=== LAST 40 NONEMPTY ===")
    nonempty = [(i, t) for i, t in enumerate(texts) if t.strip()]
    for i, t in nonempty[-40:]:
        lines.append(f"{i} [{style_of(paras[i])}] {t[:240]}")

    # duplicate-ish chapter titles
    lines.append("\n=== STYLE COUNTS ===")
    lines.append(str(Counter(style_of(p) for p in paras).most_common()))

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("wrote", OUT, "words", len(words), "h1", len(h1), "testzip", bad)


if __name__ == "__main__":
    main()
