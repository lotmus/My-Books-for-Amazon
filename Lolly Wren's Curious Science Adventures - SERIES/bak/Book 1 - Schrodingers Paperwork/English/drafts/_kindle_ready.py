"""Make BOOK_1_2.docx Kindle/KDP-ready and write the live file."""

from __future__ import annotations

import io
import re
import shutil
import tempfile
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork")
LIVE = ROOT / "Schrodingers_Paperwork_BOOK_1_2.docx"
BACKUP = ROOT / "Schrodingers_Paperwork_BOOK_1_Photo_Edition.docx"
FIGS = ROOT / "English" / "_fig_out"

EMU = 914400
MAX_CX = 5486400  # 6.00 in
MAX_CY = 4754880  # 5.20 in — one Paperwhite-ish screen


def source_docx() -> Path:
    for p in (LIVE, BACKUP, ROOT / "Schrodingers_Paperwork_BOOK_1_2.docx.ready"):
        if p.exists() and p.stat().st_size > 200_000:
            return p
    raise SystemExit("no source docx")


def save_clean(src: Path, dest: Path) -> None:
    im = Image.open(src)
    im.load()
    im = im.convert("RGB")
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.suffix.lower() in {".jpg", ".jpeg"}:
        im.save(dest, "JPEG", quality=88, optimize=True)
    else:
        buf = io.BytesIO()
        im.save(buf, "PNG", optimize=True)
        dest.write_bytes(buf.getvalue())


def cap_extent(cx: int, cy: int) -> tuple[int, int]:
    if cx <= MAX_CX and cy <= MAX_CY:
        return cx, cy
    scale = min(MAX_CX / cx, MAX_CY / cy)
    return int(cx * scale), int(cy * scale)


def fix_styles(styles: str) -> str:
    styles = styles.replace('w:val="2E74B5"', 'w:val="000000"')
    styles = styles.replace('w:val="de-DE"', 'w:val="en-GB"')
    # Heading 1: black, bold, page break, outline — no Word blue
    h1 = re.search(r'<w:style w:type="paragraph" w:styleId="Heading1">.*?</w:style>', styles, re.DOTALL)
    if h1:
        block = (
            '<w:style w:type="paragraph" w:styleId="Heading1">'
            '<w:name w:val="heading 1"/>'
            '<w:uiPriority w:val="9"/>'
            "<w:qFormat/>"
            "<w:pPr>"
            "<w:keepNext/>"
            "<w:pageBreakBefore/>"
            '<w:spacing w:before="360" w:after="200"/>'
            '<w:jc w:val="center"/>'
            '<w:outlineLvl w:val="0"/>'
            "</w:pPr>"
            "<w:rPr>"
            "<w:b/><w:bCs/>"
            '<w:color w:val="000000"/>'
            '<w:sz w:val="32"/><w:szCs w:val="32"/>'
            "</w:rPr>"
            "</w:style>"
        )
        styles = styles.replace(h1.group(0), block, 1)
    return styles


def fix_settings(settings: str) -> str:
    settings = settings.replace('w:val="de-DE"', 'w:val="en-GB"')
    if "w:themeFontLang" not in settings:
        settings = settings.replace("</w:settings>", '<w:themeFontLang w:val="en-GB"/></w:settings>')
    return settings


def para_text(p: str) -> str:
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))


def style_of(p: str) -> str:
    m = re.search(r'<w:pStyle w:val="([^"]+)"', p)
    return m.group(1) if m else "Normal"


def fix_document(xml: str) -> str:
    xml = xml.replace('w:val="de-DE"', 'w:val="en-GB"')
    xml = re.sub(r"<w:lastRenderedPageBreak/>", "", xml)
    xml = xml.replace("Amazon Ember", "Georgia")

    def ext_repl(m: re.Match) -> str:
        cx, cy = cap_extent(int(m.group(1)), int(m.group(2)))
        return f'<wp:extent cx="{cx}" cy="{cy}"/>'

    xml = re.sub(r'<wp:extent cx="(\d+)" cy="(\d+)"/>', ext_repl, xml)

    def aext_repl(m: re.Match) -> str:
        cx, cy = cap_extent(int(m.group(1)), int(m.group(2)))
        return f'<a:ext cx="{cx}" cy="{cy}"/>'

    xml = re.sub(r'<a:ext cx="(\d+)" cy="(\d+)"/>', aext_repl, xml)

    # Contents entries: drop list bullets so Kindle does not paint a TOC as a list
    in_contents = False

    def para_repl(m: re.Match) -> str:
        nonlocal in_contents
        p = m.group(0)
        title = para_text(p).strip()
        st = style_of(p)
        if st == "Heading1" and title == "Contents":
            in_contents = True
            return p
        if st == "Heading1" and title != "Contents":
            in_contents = False
        if in_contents and "<w:hyperlink" in p:
            p = re.sub(r"<w:numPr>.*?</w:numPr>", "", p, count=1, flags=re.DOTALL)
            p = p.replace('w:val="ListParagraph"', 'w:val="Normal"')
            if "<w:ind " not in p:
                p = p.replace("</w:pPr>", '<w:ind w:left="360"/></w:pPr>', 1)
        return p

    return re.sub(r"<w:p\b[^>]*>.*?</w:p>", para_repl, xml, flags=re.DOTALL)


def pack(tmp: Path, dest: Path) -> None:
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for f in sorted(tmp.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(tmp).as_posix())
    with zipfile.ZipFile(dest) as z:
        bad = z.testzip()
        names = z.namelist()
        if bad is not None:
            raise SystemExit(f"testzip failed: {bad}")
        if "word/document.xml" not in names:
            raise SystemExit("missing document.xml")
        for n in names:
            if n.startswith("word/media/"):
                Image.open(io.BytesIO(z.read(n))).load()


def main() -> None:
    src = source_docx()
    print("source", src)
    tmp = Path(tempfile.mkdtemp(prefix="sp_kindle_"))
    with zipfile.ZipFile(src) as z:
        z.extractall(tmp)

    media = tmp / "word" / "media"
    for p in sorted(FIGS.glob("image*")):
        save_clean(p, media / p.name)
        print("media", p.name, (media / p.name).stat().st_size)

    doc = tmp / "word" / "document.xml"
    doc.write_text(fix_document(doc.read_text(encoding="utf-8")), encoding="utf-8")
    styles = tmp / "word" / "styles.xml"
    styles.write_text(fix_styles(styles.read_text(encoding="utf-8")), encoding="utf-8")
    settings = tmp / "word" / "settings.xml"
    if settings.exists():
        settings.write_text(fix_settings(settings.read_text(encoding="utf-8")), encoding="utf-8")

    packed = ROOT / "_kindle_build.docx"
    pack(tmp, packed)
    shutil.rmtree(tmp, ignore_errors=True)

    if LIVE.exists():
        LIVE.unlink()
    shutil.copyfile(packed, LIVE)
    shutil.copyfile(packed, BACKUP)
    packed.unlink()
    print("LIVE", LIVE, LIVE.stat().st_size)


if __name__ == "__main__":
    main()
