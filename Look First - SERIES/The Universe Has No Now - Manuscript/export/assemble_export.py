"""Assemble Book 1 markdown and build Kindle-ingestible files."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
FIGS = os.path.join(SRC, "Figures", "figs")
OUT_MD = os.path.join(SRC, "The_Universe_Has_No_Now.md")
OUT_DOCX = os.path.join(HERE, "The_Universe_Has_No_Now.docx")
OUT_EPUB = os.path.join(HERE, "The_Universe_Has_No_Now.epub")

PARTS = [
    "00_Front_Matter.md",
    "01_Part_One_No_Now.md",
    "02_Part_Two_Past.md",
    "03_Part_Three_Burst.md",
    "04_Part_Four_Missing.md",
    "05_Part_Five_Horizons.md",
    "06_Part_Six_Getting_There.md",
    "07_Part_Seven_Loops.md",
    "08_Part_Eight_Copies.md",
    "09_Part_Nine_Filter.md",
    "10_Part_Ten_Future.md",
    "11_Appendix.md",
    "12_Notes_and_Sources.md",
]

YAML = """---
title: The Universe Has No Now
subtitle: Time, Origins, and Whether We Can Get Somewhere Else
author: Lothar J. Musiol
lang: en-US
rights: Copyright © 2026 Lothar J. Musiol. All rights reserved.
---

"""

FIG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HEAD_RE = re.compile(r"^(#{1,2})\s+")


def resolve_fig(n: int) -> tuple[str, bool]:
    for name in (
        f"fig{n:02d}.jpg",
        f"fig{n:02d}.jpeg",
        f"fig{n:02d}.png",
        f"fig{n:02d}_slot.png",
    ):
        path = os.path.join(FIGS, name)
        if os.path.exists(path):
            return f"Figures/figs/{name}", True
    return f"Figures/figs/fig{n:02d}_slot.png", False


def rewrite_images(text: str) -> tuple[str, list[int]]:
    missing: list[int] = []

    def repl(m: re.Match) -> str:
        cap, _old = m.group(1), m.group(2)
        num = re.match(r"Figure\s+(\d+)", cap or "")
        if not num:
            return m.group(0)
        n = int(num.group(1))
        rel, found = resolve_fig(n)
        if not found:
            missing.append(n)
        return f"![{cap}]({rel})"

    return FIG_RE.sub(repl, text), missing


def assemble() -> tuple[str, list[int]]:
    chunks: list[str] = [YAML]
    missing: list[int] = []
    for i, name in enumerate(PARTS):
        raw = open(os.path.join(SRC, name), encoding="utf-8").read()
        raw = raw.replace("%%TOC%%\n\n", "").replace("%%TOC%%\n", "").replace("%%TOC%%", "")
        body, miss = rewrite_images(raw)
        missing.extend(miss)
        lines = body.splitlines()
        out_lines: list[str] = []
        for line in lines:
            if HEAD_RE.match(line) and (
                line.startswith("# PART")
                or line.startswith("# APPENDIX")
                or line.startswith("## ")
            ):
                out_lines.append("\\newpage")
                out_lines.append("")
            out_lines.append(line)
        chunks.append("\n".join(out_lines).rstrip() + "\n\n")
        if i < len(PARTS) - 1:
            chunks.append("\\newpage\n\n")
    text = "".join(chunks)
    # collapse accidental triple pagebreaks
    text = re.sub(r"(\\newpage\n\n){2,}", r"\\newpage\n\n", text)
    return text, sorted(set(missing))


def word_count(text: str) -> int:
    # Strip YAML, markdown chrome, image lines
    body = re.sub(r"^---.*?---\s*", "", text, count=1, flags=re.S)
    body = re.sub(r"!\[.*?\]\(.*?\)", " ", body)
    body = re.sub(r"\\newpage", " ", body)
    body = re.sub(r"[#>*_`|]", " ", body)
    words = re.findall(r"[A-Za-z0-9’']+", body)
    return len(words)


IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")


def inventory_from_text(text: str) -> dict[str, object]:
    """Classify assembled markdown image links against files on disk."""
    drawn: list[int] = []
    photos: list[int] = []
    slots: list[int] = []
    broken: list[tuple[int, str]] = []
    for cap, rel in FIG_RE.findall(text):
        num = re.match(r"Figure\s+(\d+)", cap or "")
        if not num:
            continue
        n = int(num.group(1))
        abs_path = os.path.join(SRC, rel.replace("/", os.sep))
        if not os.path.isfile(abs_path):
            broken.append((n, rel))
            continue
        base = os.path.basename(rel).lower()
        if base.endswith("_slot.png"):
            slots.append(n)
        elif base.endswith(".jpg") or base.endswith(".jpeg"):
            photos.append(n)
        else:
            drawn.append(n)
    return {
        "md_images": len(drawn) + len(photos) + len(slots),
        "drawn": drawn,
        "photos": photos,
        "slots": slots,
        "broken": broken,
    }


def count_zip_images(path: str, folder_prefix: str | None = None) -> tuple[int, list[str]]:
    if not os.path.isfile(path):
        return 0, []
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
    except zipfile.BadZipFile:
        return 0, []
    hits: list[str] = []
    prefix = (folder_prefix or "").replace("\\", "/").lower()
    for name in names:
        low = name.replace("\\", "/").lower()
        if not low.endswith(IMAGE_EXTS):
            continue
        if prefix and prefix not in low:
            continue
        hits.append(name)
    return len(hits), hits


def find_pandoc() -> str | None:
    exe = shutil.which("pandoc")
    if exe:
        return exe
    for candidate in (
        r"C:\Program Files\Pandoc\pandoc.exe",
        r"C:\Users\{}\AppData\Local\Pandoc\pandoc.exe".format(os.environ.get("USERNAME", "")),
    ):
        if os.path.exists(candidate):
            return candidate
    return None


def find_winget() -> str | None:
    exe = shutil.which("winget")
    if exe:
        return exe
    for candidate in (
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "WindowsApps", "winget.exe"),
        r"C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\winget.exe",
    ):
        if os.path.isfile(candidate):
            return candidate
    return None


def try_install_pandoc() -> str | None:
    winget = find_winget()
    if winget:
        print("trying winget install pandoc...")
        r = subprocess.run(
            [winget, "install", "--id", "JohnMacFarlane.Pandoc", "-e", "--accept-source-agreements", "--accept-package-agreements"],
            capture_output=True,
            text=True,
        )
        print(r.stdout[-2000:] if r.stdout else "")
        print(r.stderr[-1000:] if r.stderr else "")
    else:
        print("winget not found")
    return find_pandoc()


def run_pandoc(pandoc: str, text_path: str) -> list[str]:
    built: list[str] = []
    common = [
        pandoc,
        text_path,
        "--from",
        "markdown+raw_tex+tex_math_dollars",
        "--toc",
        "--toc-depth=2",
        "--resource-path",
        f"{SRC}{os.pathsep}{FIGS}",
        "--metadata",
        "title=The Universe Has No Now",
        "--metadata",
        "author=Lothar J. Musiol",
        "--metadata",
        "lang=en-US",
    ]
    for dest, extra in (
        (OUT_DOCX, ["--to", "docx"]),
    ):
        cmd = common + extra + ["-o", dest]
        print("running", " ".join(cmd))
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0 and os.path.exists(dest):
            print("wrote", dest, os.path.getsize(dest), "bytes")
            built.append(dest)
        else:
            print("pandoc failed for", dest)
            print(r.stdout)
            print(r.stderr)
    return built


def _write_text(path: str, text: str) -> str:
    """Write text. If OneDrive locks the canonical path, write beside it and replace."""
    try:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        return path
    except OSError as err:
        side = path + ".rebuilt"
        print("locked", path, err, "->", side)
        with open(side, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        try:
            os.replace(side, path)
            return path
        except OSError:
            return side


def run_build_docx() -> str | None:
    script = os.path.join(SRC, "Figures", "build_docx.py")
    dest = OUT_DOCX
    r = subprocess.run([sys.executable, script, dest], capture_output=True, text=True)
    print(r.stdout)
    print(r.stderr)
    if r.returncode != 0 or not os.path.exists(dest):
        side = os.path.join(HERE, "The_Universe_Has_No_Now_rebuilt.docx")
        r = subprocess.run([sys.executable, script, side], capture_output=True, text=True)
        print(r.stdout)
        print(r.stderr)
        if r.returncode == 0 and os.path.exists(side):
            try:
                os.replace(side, dest)
                return dest
            except OSError:
                return side
        return None
    return dest


def build_epub(pandoc: str, md_path: str = OUT_MD) -> bool:
    cmd = [
        pandoc,
        md_path,
        "--from",
        "markdown+raw_tex+tex_math_dollars",
        "--toc",
        "--toc-depth=2",
        "--resource-path",
        f"{SRC}{os.pathsep}{FIGS}",
        "--metadata",
        "title=The Universe Has No Now",
        "--metadata",
        "author=Lothar J. Musiol",
        "--metadata",
        "lang=en-US",
        "--to",
        "epub3",
        "--epub-chapter-level=2",
        "-o",
        OUT_EPUB,
    ]
    print("running", " ".join(cmd))
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.stdout:
        print(r.stdout)
    if r.stderr:
        print(r.stderr)
    if r.returncode == 0 and os.path.exists(OUT_EPUB):
        print("wrote", OUT_EPUB, os.path.getsize(OUT_EPUB), "bytes")
        return True
    print("pandoc epub failed")
    return False


def write_stamp(
    wc: int,
    inv: dict[str, object],
    missing: list[int],
    built: list[str],
    docx_n: int | None,
    epub_n: int | None,
    skip_docx: bool,
) -> None:
    photos = inv["photos"]
    slots = inv["slots"]
    drawn = inv["drawn"]
    fetched = ",".join(f"fig{n:02d}" for n in photos)
    if docx_n is None:
        docx_line = "docx_images=not inspected"
    elif skip_docx:
        docx_line = f"docx_images={docx_n} (inspected, not rebuilt)"
    else:
        docx_line = f"docx_images={docx_n}"
    epub_line = (
        "epub=export\\The_Universe_Has_No_Now.epub"
        if epub_n
        else "epub=not built"
    )
    stamp = os.path.join(HERE, "WORD_COUNT.txt")
    with open(stamp, "w", encoding="utf-8") as f:
        f.write(
            f"{wc}\n"
            f"docx=export\\The_Universe_Has_No_Now.docx\n"
            f"{epub_line}\n"
            f"md_images={inv['md_images']}\n"
            f"epub_images={epub_n if epub_n is not None else 'n/a'}\n"
            f"{docx_line}\n"
            f"drawn_diagrams={len(drawn)}\n"
            f"fetched_photos={fetched}\n"
            f"photo_placeholders={slots}\n"
            f"missing={missing}\n"
            f"broken={inv['broken']}\n"
            f"built={built}\n"
            "cover=export\\cover_typographic_v2_clockring.jpg\n"
        )


def main() -> int:
    skip_docx = "--skip-docx" in sys.argv
    build_epub_too = False  # docx only, standing rule (1 Oct 2026): no epub, no pdf; --with-epub is ignored
    if "--with-epub" in sys.argv:
        print("--with-epub ignored: docx only")
    os.makedirs(HERE, exist_ok=True)
    text, missing = assemble()
    md_path = _write_text(OUT_MD, text)
    wc = word_count(text)
    inv = inventory_from_text(text)
    print("assembled", md_path)
    print("words", wc)
    print("missing figure files", missing)
    print("md_images", inv["md_images"], "drawn", len(inv["drawn"]),
          "photos", len(inv["photos"]), "slots", inv["slots"],
          "broken", inv["broken"])

    built: list[str] = []
    if skip_docx:
        print("skipping build_docx (--skip-docx); Word file left untouched")
        if os.path.isfile(OUT_DOCX):
            built.append(OUT_DOCX)
    else:
        docx = run_build_docx()
        if docx:
            built.append(docx)
            print("build_docx wrote", docx, os.path.getsize(docx), "bytes")
        else:
            print("build_docx failed or skipped")

    epub_ok = False
    if not build_epub_too:
        print("skipping epub (docx only)")
    else:
        pandoc = find_pandoc() or try_install_pandoc()
        if pandoc:
            # Never let pandoc overwrite a sibling-owned python-docx Word file.
            if skip_docx or os.path.isfile(OUT_DOCX):
                epub_ok = build_epub(pandoc, md_path)
                if epub_ok:
                    built.append(OUT_EPUB)
            else:
                built.extend(run_pandoc(pandoc, md_path))
                epub_ok = os.path.isfile(OUT_EPUB)
        else:
            print("pandoc not found")

    docx_n, _docx_hits = count_zip_images(OUT_DOCX, "word/media/")
    epub_n, epub_hits = count_zip_images(OUT_EPUB) if os.path.isfile(OUT_EPUB) else (None, [])
    if epub_n is not None:
        print("epub image files", epub_n)
        for h in epub_hits:
            print(" ", h)
    if os.path.isfile(OUT_DOCX):
        print("docx media images", docx_n)

    write_stamp(
        wc,
        inv,
        missing,
        built,
        docx_n if os.path.isfile(OUT_DOCX) else None,
        epub_n if epub_ok or os.path.isfile(OUT_EPUB) else None,
        skip_docx,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
