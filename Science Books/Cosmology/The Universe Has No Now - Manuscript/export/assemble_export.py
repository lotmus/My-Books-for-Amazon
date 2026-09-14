"""Assemble Book 1 markdown and build Kindle-ingestible files."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys

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


def try_install_pandoc() -> str | None:
    winget = shutil.which("winget")
    if winget:
        print("trying winget install pandoc...")
        r = subprocess.run(
            [winget, "install", "--id", "JohnMacFarlane.Pandoc", "-e", "--accept-source-agreements", "--accept-package-agreements"],
            capture_output=True,
            text=True,
        )
        print(r.stdout[-2000:] if r.stdout else "")
        print(r.stderr[-1000:] if r.stderr else "")
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
        (OUT_EPUB, ["--to", "epub3", "--epub-chapter-level=2"]),
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


def run_build_docx() -> str | None:
    script = os.path.join(SRC, "Figures", "build_docx.py")
    r = subprocess.run([sys.executable, script, OUT_DOCX], capture_output=True, text=True)
    print(r.stdout)
    print(r.stderr)
    return OUT_DOCX if r.returncode == 0 and os.path.exists(OUT_DOCX) else None


def main() -> int:
    os.makedirs(HERE, exist_ok=True)
    text, missing = assemble()
    with open(OUT_MD, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    wc = word_count(text)
    print("assembled", OUT_MD)
    print("words", wc)
    print("missing figure files", missing)

    built: list[str] = []
    docx = run_build_docx()
    if docx:
        built.append(docx)
        print("build_docx wrote", docx, os.path.getsize(docx), "bytes")
    else:
        print("build_docx failed or skipped")

    pandoc = find_pandoc() or try_install_pandoc()
    if pandoc:
        # Prefer python-docx for the 6x9 Word file; still build epub (and docx if the first failed).
        if docx:
            common_epub_only = True
        else:
            common_epub_only = False
        if common_epub_only:
            r = subprocess.run(
                [
                    pandoc,
                    OUT_MD,
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
                    "--to",
                    "epub3",
                    "--epub-chapter-level=2",
                    "-o",
                    OUT_EPUB,
                ],
                capture_output=True,
                text=True,
            )
            print(r.stdout)
            print(r.stderr)
            if r.returncode == 0 and os.path.exists(OUT_EPUB):
                print("wrote", OUT_EPUB, os.path.getsize(OUT_EPUB), "bytes")
                built.append(OUT_EPUB)
        else:
            built.extend(run_pandoc(pandoc, OUT_MD))
    else:
        print("pandoc not found")

    stamp = os.path.join(HERE, "WORD_COUNT.txt")
    with open(stamp, "w", encoding="utf-8") as f:
        f.write(f"{wc}\nmissing={missing}\nbuilt={built}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
