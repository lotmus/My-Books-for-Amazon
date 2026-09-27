"""Promote Physics Notes / Further Reading / Glossary to chapter heading format."""

from __future__ import annotations

import re
import shutil
import tempfile
import zipfile
from pathlib import Path

DOCX = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")

H1_PPR = (
    "<w:pPr>"
    '<w:pStyle w:val="Heading1"/>'
    "<w:pageBreakBefore/>"
    '<w:spacing w:before="400" w:after="240"/>'
    '<w:jc w:val="center"/>'
    "</w:pPr>"
)
HARD = '<w:r><w:br w:type="page"/></w:r>'
H1_RPR = (
    "<w:rPr>"
    '<w:rFonts w:ascii="Amazon Ember" w:hAnsi="Amazon Ember"/>'
    "<w:b/><w:bCs/>"
    "</w:rPr>"
)


def para_text(p: str) -> str:
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))


def should_promote(title: str) -> bool:
    t = title.strip()
    if t in {"Further Reading", "Glossary"}:
        return True
    return t.startswith("Chapter ") and "Physics Notes" in t


def promote(p: str) -> str:
    p = re.sub(r"<w:pPr>.*?</w:pPr>", H1_PPR, p, count=1, flags=re.DOTALL)
    if 'w:type="page"' not in p:
        p = p.replace("</w:pPr>", "</w:pPr>" + HARD, 1)
    # make visible title runs bold Ember
    def fix_rpr(m: re.Match) -> str:
        run = m.group(0)
        if "<w:t" not in run:
            return run
        if "<w:rPr>" in run:
            run = re.sub(r"<w:rPr>.*?</w:rPr>", H1_RPR, run, count=1, flags=re.DOTALL)
        else:
            run = run.replace("<w:r>", "<w:r>" + H1_RPR, 1)
        return run

    return re.sub(r"<w:r\b[^>]*>.*?</w:r>", fix_rpr, p, flags=re.DOTALL)


def main() -> None:
    tmp = Path(tempfile.mkdtemp(prefix="sp_phys_"))
    with zipfile.ZipFile(DOCX) as z:
        z.extractall(tmp)
    xml_path = tmp / "word" / "document.xml"
    xml = xml_path.read_text(encoding="utf-8")
    changed = 0

    def repl(m: re.Match) -> str:
        nonlocal changed
        p = m.group(0)
        if 'w:val="Heading2"' not in p:
            return p
        title = para_text(p)
        if not should_promote(title):
            return p
        changed += 1
        print("promote", title[:80])
        return promote(p)

    xml = re.sub(r"<w:p\b[^>]*>.*?</w:p>", repl, xml, flags=re.DOTALL)
    xml_path.write_text(xml, encoding="utf-8")

    out = DOCX.with_suffix(".docx.next")
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(tmp.rglob("*")):
            if path.is_file():
                z.write(path, path.relative_to(tmp).as_posix())
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        DOCX.unlink()
        shutil.move(out, DOCX)
    except PermissionError:
        raise SystemExit("Close the Word document and run again.")
    print("changed", changed, "wrote", DOCX, "mb", round(DOCX.stat().st_size / 1e6, 2))


if __name__ == "__main__":
    main()
