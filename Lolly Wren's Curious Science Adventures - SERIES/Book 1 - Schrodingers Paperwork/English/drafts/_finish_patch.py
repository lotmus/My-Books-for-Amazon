"""Apply the repaired package and add Kindle-safe Heading 1 page breaks."""

from __future__ import annotations

import re
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork")
LIVE = ROOT / "Schrodingers_Paperwork_BOOK_1_2.docx"
REPACK = ROOT / "Schrodingers_Paperwork_BOOK_1_2.docx.repack"
FIGS = ROOT / "English" / "_fig_out"

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def valid_docx(path: Path) -> None:
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        assert "word/document.xml" in names
        xml = z.read("word/document.xml").decode("utf-8")
        media = [n for n in names if n.startswith("word/media/")]
    print(path.name, "ok", "bytes", path.stat().st_size, "media", len(media))
    print("  ch16_open", "The plan reached the judge" in xml)
    print("  old_injunction", "The injunction itself was granted on the Tuesday" in xml)
    print("  back_live", "Somewhere in a government basement" in xml and "image18" not in "".join(media))
    print("  notes_link", "Physics Notes (continued)" in xml)


def add_style_page_break(styles: str) -> str:
    old = (
        '<w:style w:type="paragraph" w:styleId="Heading1">'
        '<w:name w:val="heading 1"/>'
        '<w:uiPriority w:val="9"/>'
        "<w:qFormat/>"
        "<w:pPr>"
        '<w:outlineLvl w:val="0"/>'
        "</w:pPr>"
    )
    new = (
        '<w:style w:type="paragraph" w:styleId="Heading1">'
        '<w:name w:val="heading 1"/>'
        '<w:uiPriority w:val="9"/>'
        "<w:qFormat/>"
        "<w:pPr>"
        "<w:pageBreakBefore/>"
        '<w:outlineLvl w:val="0"/>'
        "</w:pPr>"
    )
    if old not in styles:
        raise SystemExit("Heading1 style block not found")
    return styles.replace(old, new, 1)


def insert_hard_breaks(xml: str) -> str:
    """Put a real page-break run at the start of each Heading 1 paragraph."""
    hard = '<w:r><w:br w:type="page"/></w:r>'

    def repl(m: re.Match) -> str:
        p = m.group(0)
        if 'w:val="Heading1"' not in p:
            return p
        if 'w:type="page"' in p:
            return p
        # insert after pPr close, before first content
        return p.replace("</w:pPr>", "</w:pPr>" + hard, 1)

    return re.sub(r"<w:p\b[^>]*>.*?</w:p>", repl, xml, flags=re.DOTALL)


def main() -> None:
    source = REPACK if REPACK.exists() and REPACK.stat().st_size > 200_000 else LIVE
    print("source", source)
    valid_docx(source)

    tmp = Path(tempfile.mkdtemp(prefix="sp_finish_"))
    with zipfile.ZipFile(source) as z:
        z.extractall(tmp)

    xml_path = tmp / "word" / "document.xml"
    styles_path = tmp / "word" / "styles.xml"
    xml = xml_path.read_text(encoding="utf-8")
    styles = styles_path.read_text(encoding="utf-8")
    styles = add_style_page_break(styles)
    xml = insert_hard_breaks(xml)
    xml_path.write_text(xml, encoding="utf-8")
    styles_path.write_text(styles, encoding="utf-8")

    # if media missing new figs, copy from _fig_out
    media = tmp / "word" / "media"
    if FIGS.exists():
        for fig in FIGS.iterdir():
            dest = media / fig.name
            if dest.exists() and dest.stat().st_size > fig.stat().st_size * 3:
                shutil.copy2(fig, dest)
            elif not dest.exists():
                shutil.copy2(fig, dest)

    out = LIVE.with_suffix(".docx.next")
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(tmp.rglob("*")):
            if path.is_file():
                z.write(path, path.relative_to(tmp).as_posix())
    shutil.rmtree(tmp, ignore_errors=True)

    try:
        if LIVE.exists():
            LIVE.unlink()
        shutil.move(out, LIVE)
    except PermissionError:
        print("LOCKED: close Word, then I can replace the live file.")
        print("patched copy waiting at", out)
        return
    print("wrote", LIVE, "mb", round(LIVE.stat().st_size / 1e6, 2))
    valid_docx(LIVE)
    print("hard_breaks", zipfile.ZipFile(LIVE).read("word/document.xml").decode("utf-8").count('w:type="page"'))


if __name__ == "__main__":
    main()
