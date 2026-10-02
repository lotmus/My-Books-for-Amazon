# build_math_actually.py — the one-time rename build

Turns the four *The Mathematics Tower* masters into the *Math, Actually*
masters. It was run once on 2 Oct 2026. Do not run it on the new masters: it
expects the old names, headings ("Floor N: …", "Room N.M: …") and bookmarks.

    python build_math_actually.py SRC_DIR OUT_DIR

SRC_DIR holds `The Mathematics Tower - Volume 1..4.docx` (the originals are in
`D:\bak\2026-10-02 Math Actually\`). OUT_DIR receives
`Math, Actually - Volume 1..4.docx` and `build_report.json` (link counts,
dangling anchors). Needs Python 3 and lxml.

Files:

- `build_math_actually.py` — the build: cross-volume section index, cross-reference
  rewriting (topic-named hyperlinks inside a volume, plain "Topic (Volume N)"
  across volumes), vocabulary, chapter and section layout in the Physics,
  Actually style, title and copyright pages, the manual Contents, Also in This
  Series, front-matter and epilogue text, Physics heading styles, document
  properties.
- `docxtext.py` — run-aware paragraph editing (keeps formatting, hyperlinks,
  fields and drawings intact).
- `rules.py` — vocabulary rules (floor → chapter, room → section, Tower →
  series, building/lift/staircase phrases) and the protected list (floor
  function, noise floor, room temperature, tower law, Hilbert's hotel …).
- `literal_fixes.py` — one-off sentence rewrites of the old building metaphor.
- `ma_text.py` — the newly written text: volume data, Preface / About This
  Volume, How This Book Is Organized, Where the Foundations Are, epilogues,
  A Note Before You Go.
