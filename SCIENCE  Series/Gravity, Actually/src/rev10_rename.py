# Rev10 (11 Oct 2026): rename the book from "Gravitation, Actually" to "Gravity, Actually" and change the subtitle
# to "Einstein's Relativity in Plain Words: ...". Text of Rev9 otherwise unchanged. Misner, Thorne and Wheeler's
# "Gravitation" (a real book title) is left as is. Usage: python rev10_rename.py <Rev9.docx> <Rev10.docx>
import sys, zipfile, xml.etree.ElementTree as ET
src, dst = sys.argv[1], sys.argv[2]
EDITS = {
  "word/document.xml": [("<w:t>GRAVITATION, ACTUALLY</w:t>", "<w:t>GRAVITY, ACTUALLY</w:t>", 1),
                        ("Einstein\u2019s Gravity in Plain Words", "Einstein\u2019s Relativity in Plain Words", 2),
                        ("<w:t>Gravitation, Actually: Einstein", "<w:t>Gravity, Actually: Einstein", 1)],
  "word/header1.xml": [("Gravitation, Actually  \u00b7  Lothar J. Musiol", "Gravity, Actually  \u00b7  Lothar J. Musiol", 1)],
  "docProps/core.xml": [("<dc:title>Gravitation, Actually: Einstein\u2019s Gravity in Plain Words", "<dc:title>Gravity, Actually: Einstein\u2019s Relativity in Plain Words", 1)],
}
zin = zipfile.ZipFile(src); out = {}
for part, reps in EDITS.items():
    x = zin.read(part).decode("utf8"); before = x.count("Gravitation")
    for a, b, n in reps:
        assert x.count(a) == n, (part, a, x.count(a)); x = x.replace(a, b)
    assert "Gravitation, Actually" not in x and "GRAVITATION, ACTUALLY" not in x and "s Gravity in Plain" not in x, part
    print(part, "Gravitation count", before, "->", x.count("Gravitation"))
    ET.fromstring(x.encode("utf8")); out[part] = x.encode("utf8")
with zipfile.ZipFile(dst, "w") as zout:
    for info in zin.infolist():
        zout.writestr(info, out.get(info.filename, zin.read(info.filename)), compress_type=info.compress_type)
z = zipfile.ZipFile(dst); assert z.testzip() is None
for n in z.namelist():
    if n.endswith(".xml"): assert "Gravitation, Actually" not in z.read(n).decode("utf8", "ignore"), n
print("wrote", dst)
