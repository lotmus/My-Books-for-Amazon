#!/usr/bin/env python3
"""Sanity-check .docx files changed in a PR.

Hard failures (non-zero exit): the file isn't a valid zip, or python-docx
can't open it at all — both mean the manuscript is corrupt.

Warnings (posted as annotations, don't fail the build): a paragraph carries
a Heading style but reads like body text (too long, or empty). That pattern
has caused real bugs in this repo (headings bleeding into story paragraphs),
and it's a style any book in here could hit, not just one.
"""
import subprocess
import sys
import zipfile

import docx

HEADING_LEN_LIMIT = 150


def changed_docx_files(base):
    out = subprocess.run(
        ["git", "diff", "--name-only", "-z", "--diff-filter=ACMR", base, "HEAD", "--", "*.docx"],
        capture_output=True, check=True, text=True,
    ).stdout
    return [p for p in out.split("\0") if p]


def check(path):
    hard_failures = []
    warnings = []

    try:
        zf = zipfile.ZipFile(path)
        bad = zf.testzip()
        if bad:
            hard_failures.append(f"corrupt zip entry: {bad}")
            return hard_failures, warnings
    except zipfile.BadZipFile as e:
        hard_failures.append(f"not a valid zip/docx: {e}")
        return hard_failures, warnings

    try:
        d = docx.Document(path)
    except Exception as e:
        hard_failures.append(f"python-docx failed to open: {e}")
        return hard_failures, warnings

    for i, p in enumerate(d.paragraphs):
        style = (p.style.name if p.style else "") or ""
        if not style.lower().startswith("heading"):
            continue
        text = p.text
        if len(text) > HEADING_LEN_LIMIT:
            warnings.append(
                f"paragraph {i} is styled '{style}' but has {len(text)} characters "
                f"(looks like body text, not a heading): {text[:60]!r}..."
            )
        elif text.strip() == "":
            warnings.append(f"paragraph {i} is styled '{style}' but is empty")

    return hard_failures, warnings


def main():
    if len(sys.argv) != 3 or sys.argv[1] != "--base":
        print("usage: validate_docx.py --base <git-ref>", file=sys.stderr)
        sys.exit(2)
    base = sys.argv[2]

    paths = changed_docx_files(base)
    if not paths:
        print("No changed .docx files.")
        return

    failed = False
    for path in paths:
        print(f"::group::{path}")
        hard_failures, warnings = check(path)
        for problem in hard_failures:
            print(f"::error file={path}::{problem}")
        for problem in warnings:
            print(f"::warning file={path}::{problem}")
        if hard_failures:
            failed = True
            print(f"{len(hard_failures)} hard failure(s)")
        elif warnings:
            print(f"{len(warnings)} warning(s)")
        else:
            print("OK")
        print("::endgroup::")

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
