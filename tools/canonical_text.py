"""Read the canonical back-matter text so build scripts keep no copies of it.

Sources (repo root, notes/):
  ABOUT_THE_AUTHOR - canonical.md   Version A / Version B bios
  ALSO_BY - canonical list.md       the "Also by Lothar J. Musiol" list

To change a bio or the Also-by list, edit those two files; every build picks it up.

    import canonical_text as ct
    ct.about_paragraphs('B')                 # ['Lothar J. Musiol is a graduate ...', 'He writes ...']
    ct.also_by(exclude=['Science Sparks'])   # [('Physics, Actually', ['Physics, Actually, Volume 1: ...']), ...]

`exclude` lists title prefixes to leave out (the book being built); empty groups are dropped.
Build scripts find this module by walking up from their own folder to the first `tools/canonical_text.py`.
"""
import os

ABOUT_FILE = "ABOUT_THE_AUTHOR - canonical.md"
ALSO_BY_FILE = "ALSO_BY - canonical list.md"
ALSO_BY_SECTION = "## Also by Lothar J. Musiol"


def notes_dir():
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "notes")


def _lines(name):
    with open(os.path.join(notes_dir(), name), encoding="utf-8-sig") as f:
        return f.read().splitlines()


def _typo(text, typographic):
    """Books that set curly apostrophes get the canonical straight ones as U+2019."""
    return text.replace("'", "\u2019") if typographic else text


def about_paragraphs(version="B", typographic=False):
    """Paragraphs of the About the Author bio for 'A' or 'B', exactly as written (inline *italic* kept).
    typographic=True turns straight apostrophes into curly ones, for books that use curly quotes."""
    head = "## Version " + version
    out, cur, inside = [], [], False
    for line in _lines(ABOUT_FILE) + [""]:
        if line.startswith("## "):
            if inside:
                break
            inside = line.strip() == head
            continue
        if not inside:
            continue
        if line.strip():
            cur.append(line.strip())
        elif cur:
            out.append(" ".join(cur)); cur = []
    # the file ends with a note about the plain-text copies; it is not part of the bio
    return [_typo(p, typographic) for p in out if not p.startswith("Plain-text copies")]


def also_by(exclude=(), typographic=False):
    """[(group, [title, ...]), ...] from the canonical Also-by list, in order, minus excluded titles.
    typographic=True turns straight apostrophes into curly ones, for books that use curly quotes."""
    groups, group, inside = [], None, False
    for line in _lines(ALSO_BY_FILE):
        if line.startswith("## "):
            if inside:
                break
            inside = line.strip() == ALSO_BY_SECTION
            continue
        if not inside:
            continue
        s = line.strip()
        if s.startswith("**") and s.endswith("**") and len(s) > 4:
            group = (s[2:-2], []); groups.append(group)
        elif s.startswith("- ") and group is not None:
            title = s[2:].strip()
            if not any(title.startswith(x) for x in exclude):
                group[1].append(_typo(title, typographic))
    return [(g, t) for g, t in groups if t]


if __name__ == "__main__":
    for p in about_paragraphs("B"):
        print(p[:90], "...")
    for g, t in also_by():
        print(g, len(t))
