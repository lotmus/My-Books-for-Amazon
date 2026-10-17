from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree

HERE = Path(__file__).resolve().parent
BOOK = HERE.parent
SERIES = BOOK.parent
SOURCE = BOOK / "The_Murder_That_Hadnt_Happened_Yet_REV19_REVIEW_CANDIDATE.docx"
COVER = BOOK / "Kindle Front Cover.jpg"
CSS = SERIES / "scripts" / "kindle-reflowable.css"
METADATA = SERIES / "scripts" / "kindle-metadata.yaml"
OUTPUT = BOOK / "The_Murder_That_Hadnt_Happened_Yet_REV19_Kindle_Reflowable.epub"


def main() -> None:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise SystemExit("pandoc was not found on PATH")
    with tempfile.TemporaryDirectory() as temp:
        raw = Path(temp) / "raw.epub"
        subprocess.run([pandoc, str(SOURCE), "--output", str(raw), "--to", "epub3", "--standalone", "--toc", "--toc-depth=2", "--split-level=1", "--css", str(CSS), f"--epub-cover-image={COVER}", "--metadata-file", str(METADATA), "--metadata", "title=The Murder That Hadn't Happened Yet"], check=True)
        with ZipFile(raw) as source, ZipFile(OUTPUT, "w") as target:
            target.writestr("mimetype", source.read("mimetype"), compress_type=0)
            found = False
            for item in source.infolist():
                if item.filename == "mimetype":
                    continue
                data = source.read(item.filename)
                if item.filename.endswith((".xhtml", ".html")):
                    try:
                        root = etree.fromstring(data)
                    except etree.XMLSyntaxError:
                        target.writestr(item, data, compress_type=ZIP_DEFLATED)
                        continue
                    for image in root.xpath("//*[local-name()='img' and starts-with(@alt, 'Back cover:')]" ):
                        paragraph = image.getparent()
                        paragraph.set("style", "break-before: page; page-break-before: always; text-align: center; margin: 0; padding: 0;")
                        image.set("style", "width: 100%; height: auto; max-width: 100%; max-height: 100vh; object-fit: contain;")
                        found = True
                    if found:
                        data = etree.tostring(root, encoding="utf-8", xml_declaration=True)
                target.writestr(item, data, compress_type=ZIP_DEFLATED)
        if not found:
            OUTPUT.unlink(missing_ok=True)
            raise SystemExit("Back-cover image was not found in the generated EPUB")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
