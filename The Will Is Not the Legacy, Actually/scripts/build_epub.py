"""Build a reflowable EPUB 3 edition for Kindle from the Markdown source."""

from __future__ import annotations

import json
import posixpath
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out" / "The_Will_Is_Not_the_Legacy_Actually_Kindle.epub"
TITLE = "The Will Is Not the Legacy, Actually"
AUTHOR = "Lothar J. Musiol"
IMAGE = re.compile(r"!\[([^]]*)\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
LINK = re.compile(r"\]\(#([^)]+)\)")


def main() -> None:
    files = sorted((ROOT / "md").glob("*.md"))
    if not files:
        raise SystemExit("No Markdown chapters found in md/.")

    headings: dict[str, str] = {}
    rows: list[tuple[Path, list[str]]] = []
    heading_number = 0
    for path in files:
        lines = path.read_text(encoding="utf-8").splitlines()
        updated: list[str] = []
        for line in lines:
            match = HEADING.match(line)
            if match:
                heading_number += 1
                title = match.group(2).strip()
                anchor = f"_sec{heading_number:04d}"
                headings.setdefault(title, anchor)
                line = f"{match.group(1)} {title} {{#{anchor}}}"
            # The manuscript's !> syntax marks shaded takeaway boxes in the print build.
            # In a reflowable EPUB, blockquotes provide a clean accessible equivalent.
            elif line.startswith("!>"):
                line = ">" + line[2:]
            updated.append(line)
        rows.append((path, updated))

    unresolved: set[str] = set()
    for _, lines in rows:
        for line in lines:
            for target in LINK.findall(line):
                if target not in headings:
                    unresolved.add(target)
    if unresolved:
        raise SystemExit("Unresolved internal EPUB links: " + ", ".join(sorted(unresolved)))

    rules_path = ROOT / "kindle_links.json"
    rules = json.loads(rules_path.read_text(encoding="utf-8")).get("rules", [])
    with tempfile.TemporaryDirectory(prefix="will_epub_") as temp_name:
        temp = Path(temp_name)
        for rel_dir in ("src/diagrams",):
            shutil.copytree(ROOT / rel_dir, temp / rel_dir)

        inputs: list[Path] = []
        for source, lines in rows:
            text = "\n".join(lines) + "\n"
            for target, anchor in headings.items():
                text = text.replace(f"](#{target})", f"](#{anchor})")
            for rule in rules:
                text = text.replace(rule["find"], rule["to"])
            dest = temp / source.name
            dest.write_text(text, encoding="utf-8", newline="\n")
            inputs.append(dest)

        about = (ROOT / "about.md").read_text(encoding="utf-8")
        author_text = about.split("## Version B", 1)[1].split("Plain-text copies", 1)[0].strip()
        author_file = temp / "about_author.md"
        author_file.write_text("# About the Author\n\n" + author_text + "\n", encoding="utf-8")
        inputs.append(author_file)

        also = (ROOT / "alsoby.md").read_text(encoding="utf-8")
        also_text = also.split("## Also by Lothar J. Musiol", 1)[1].split("## Also by Kevin Drew Peters", 1)[0].strip()
        also_file = temp / "also_by.md"
        also_file.write_text("# Also by Lothar J. Musiol\n\n" + also_text + "\n", encoding="utf-8")
        inputs.append(also_file)

        copyright_file = temp / "copyright.md"
        copyright_file.write_text(
            "# Copyright and Use\n\n"
            "Copyright © 2026 Lothar J. Musiol. All rights reserved.\n\n"
            "No part of this book may be reproduced or transmitted without written permission, "
            "except for brief quotations in reviews and the worksheets and checklists in the "
            "appendices, which readers may copy for personal use.\n\n"
            "This book is educational, not legal, tax, financial, or medical advice. It does not "
            "create a lawyer-client relationship. Legal rules and figures change; the jurisdictional "
            "figures in this edition were checked against official sources in October 2026. All "
            "people and families in the examples are fictional.\n\n"
            "First edition, 2026.\n",
            encoding="utf-8",
        )
        inputs.insert(0, copyright_file)

        css = temp / "kindle.css"
        css.write_text(
            "body { line-height: 1.35; }\n"
            "h1, h2, h3 { line-height: 1.2; break-after: avoid; }\n"
            "blockquote { margin: 1em 0.5em; padding: 0.5em 0.8em; border-left: 0.2em solid #68758b; }\n"
            "img { max-width: 100%; height: auto; }\n"
            "p { widows: 2; orphans: 2; }\n",
            encoding="utf-8",
        )

        OUT.parent.mkdir(parents=True, exist_ok=True)
        command = [
            "pandoc",
            "--from=markdown+header_attributes",
            "--to=epub3",
            "--output", str(OUT),
            "--metadata", f"title={TITLE}",
            "--metadata", f"author={AUTHOR}",
            "--metadata", "lang=en-US",
            "--metadata", "rights=Copyright © 2026 Lothar J. Musiol",
            "--metadata", "date=2026",
            "--toc", "--toc-depth=2",
            "--split-level=2",
            "--epub-cover-image", str(ROOT / "The Will Is Not the Legacy, Actually - Front Cover (Kindle).jpg"),
            "--css", str(css),
            *[str(path) for path in inputs],
        ]
        subprocess.run(command, cwd=temp, check=True)

    validate_epub(OUT)
    print(f"Built {OUT}")
    print(f"Chapters: {len(files)}; heading anchors: {heading_number}; internal links checked: {sum(1 for _, lines in rows for line in lines for _ in LINK.findall(line))}")


def validate_epub(path: Path) -> None:
    with zipfile.ZipFile(path) as archive:
        bad_member = archive.testzip()
        if bad_member:
            raise SystemExit(f"Corrupt EPUB member: {bad_member}")
        names = set(archive.namelist())
        if "mimetype" not in names or "META-INF/container.xml" not in names:
            raise SystemExit("EPUB container files are missing.")
        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = next(el for el in container.iter() if el.tag.endswith("rootfile"))
        opf = ET.fromstring(archive.read(rootfile.attrib["full-path"]))
        manifest = [el for el in opf.iter() if el.tag.endswith("item")]
        spine = [el for el in opf.iter() if el.tag.endswith("itemref")]
        missing = [item.attrib["href"] for item in manifest if item.attrib.get("href") and
                   not item.attrib["href"].startswith(("http:", "https:")) and
                   str((Path(rootfile.attrib["full-path"]).parent / item.attrib["href"]).as_posix()) not in names]
        if missing:
            raise SystemExit("EPUB manifest entries missing from archive: " + ", ".join(missing))
        if len(spine) < 5:
            raise SystemExit("EPUB spine is unexpectedly short.")
        docs = [name for name in names if name.endswith((".xhtml", ".html"))]
        markup = {name: archive.read(name).decode("utf-8") for name in docs}
        all_markup = "\n".join(markup.values())
        if "The Will Is Not the Legacy, Actually" not in all_markup or "About the Author" not in all_markup:
            raise SystemExit("Expected title or author back matter is missing.")
        if "!&gt;" in all_markup or "src/diagrams/" in all_markup:
            raise SystemExit("Unconverted callout marker or source image path remains.")
        ids = {name: set(re.findall(r'\bid="([^"]+)"', text)) for name, text in markup.items()}
        broken = []
        for name, text in markup.items():
            for href in re.findall(r'\bhref="([^"]+)"', text):
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc or not parsed.fragment:
                    continue
                target = unquote(parsed.path)
                target = posixpath.normpath(posixpath.join(posixpath.dirname(name), target)) if target else name
                fragment = unquote(parsed.fragment)
                if target not in ids or fragment not in ids[target]:
                    broken.append(f"{name} -> {href}")
        if broken:
            raise SystemExit("Broken EPUB navigation/link targets: " + "; ".join(broken[:12]))
        nav = next((item.attrib.get("href") for item in manifest if item.attrib.get("properties") == "nav"), None)
        nav_path = posixpath.normpath(posixpath.join(posixpath.dirname(rootfile.attrib["full-path"]), nav)) if nav else None
        if not nav_path or nav_path not in names or 'epub:type="toc"' not in archive.read(nav_path).decode("utf-8"):
            raise SystemExit("EPUB 3 table-of-contents navigation document is missing.")


if __name__ == "__main__":
    main()
