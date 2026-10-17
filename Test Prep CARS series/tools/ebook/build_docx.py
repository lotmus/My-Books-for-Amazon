#!/usr/bin/env python3
"""Build a Word (.docx) manuscript from a folder of chapter Markdown files.

Same release rules as build_ebook.py, but Markdown tables stay real Word tables.
  * "Author verification note" blocks are stripped (--release).
  * Equations written as indented lines become centered paragraphs with line breaks.
  * "(chapter:N)" links become internal links.
  * Each answer key starts on its own page.
  * Praxis Tips and equations use the Word styles "Praxis Tip" and "Equation".

Usage:
  python tools/ebook/build_docx.py books/book1-chem-phys --title "..." --author "U. B. Smart" \
      --out Book1.docx [--front front.md] [--cover cover.png] [--release]
Requires: pandoc.
"""
import argparse, glob, os, re, subprocess, sys, tempfile, shutil

def preprocess(text, chnum, existing, release):
    text = text.replace("\r\n", "\n")
    if release:
        text = re.split(r"\n---\n\n\*\*Author verification note", text)[0].rstrip() + "\n"
    lines = text.split("\n")
    out = []
    i = 0
    for k, ln in enumerate(lines):
        if ln.startswith("# "):
            lines[k] = f"{ln} {{#ch-{chnum:02d}}}"
            break
    while i < len(lines):
        ln = lines[i]
        if re.match(r"^ {4,}\S", ln) and (not out or out[-1].strip() == "") and not re.match(r"^\s*([-*+]|\d+\.)\s", ln):
            blk = []
            while i < len(lines) and re.match(r"^ {4,}\S", lines[i]):
                blk.append(lines[i].strip())
                i += 1
            out += ["::: {custom-style=\"Equation\"}", "\\\n".join(blk), ":::"]
            continue
        if ln.startswith("Praxis Tip:"):
            out += ["::: {custom-style=\"Praxis Tip\"}", "**Praxis Tip:**" + ln[len("Praxis Tip:"):], ":::"]
            i += 1
            continue
        m = re.match(r"^\*\*(Answers and (?:reasons|explanations))\*\*\s*$", ln)
        if m:
            out += ["```{=openxml}", "<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>", "```", f"## {m.group(1)}"]
            i += 1
            continue
        out.append(ln)
        i += 1
    res = []
    k = 0
    while k < len(out):
        if re.match(r"^\s{1,3}[A-D]\. ", out[k]):
            if res and res[-1].strip() and not res[-1].endswith("\\"):
                res[-1] += "\\"
            g = k
            while g < len(out) and re.match(r"^\s{1,3}[A-D]\. ", out[g]):
                g += 1
            for t in range(k, g):
                res.append(out[t] + ("\\" if t < g - 1 else ""))
            k = g
            continue
        res.append(out[k])
        k += 1
    text = "\n".join(res)

    def link(m):
        n = int(m.group(1))
        return f"(#ch-{n:02d})" if n in existing else "(#)"
    text = re.sub(r"\(chapter:(\d+)\)", link, text)
    text = re.sub(r"`([^`\n]+)`", r"\1", text)
    return text

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book_dir")
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--author", default="U. B. Smart")
    ap.add_argument("--out", required=True)
    ap.add_argument("--front")
    ap.add_argument("--cover")
    ap.add_argument("--release", action="store_true")
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(a.book_dir, "ch*.md")))
    nums = {int(re.match(r"ch(\d+)", os.path.basename(f)).group(1)) for f in files}
    work = tempfile.mkdtemp(prefix="docx_")
    figdir = os.path.join(a.book_dir, "figures")
    if os.path.isdir(figdir):
        shutil.copytree(figdir, os.path.join(work, "figures"))
    parts = []
    if a.cover:
        shutil.copy(a.cover, os.path.join(work, "cover.png"))
        parts.append("![](cover.png){width=5.5in}\n\n```{=openxml}\n<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>\n```")
    if a.front:
        parts.append(open(a.front, encoding="utf-8").read().replace("\r\n", "\n"))
    for f in files:
        n = int(re.match(r"ch(\d+)", os.path.basename(f)).group(1))
        parts.append(preprocess(open(f, encoding="utf-8").read(), n, nums, a.release))
    full = "\n\n".join(parts)
    if a.release and "[VERIFY" in full:
        print("WARNING: [VERIFY] flags remain", file=sys.stderr)
    md = os.path.join(work, "book.md")
    open(md, "w", encoding="utf-8").write(full)
    meta = os.path.join(work, "meta.yaml")
    open(meta, "w", encoding="utf-8").write(
        f"---\ntitle: \"{a.title}\"\nsubtitle: \"{a.subtitle}\"\nauthor: \"{a.author}\"\nlang: en-US\n---\n")
    cmd = ["pandoc", md, "-f", "markdown+fenced_divs+raw_attribute",
           "--metadata-file", meta, "-t", "docx", "--toc", "--toc-depth=1",
           "--resource-path", work, "-o", a.out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr)
        sys.exit(1)
    if r.stderr.strip():
        print(r.stderr.strip()[:2000], file=sys.stderr)
    print("wrote", a.out)

if __name__ == "__main__":
    main()
