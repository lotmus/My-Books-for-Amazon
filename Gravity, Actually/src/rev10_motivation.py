# 11 Oct 2026: Rev10 in place. Adds the author's motivation to "Before you start" (Gravitation by Misner, Thorne,
# and Wheeler is a masterpiece written for graduate students; this book is for everyone else). Page count checked:
# 1,279 numbered pages (WorldCat, Google Books, Wikipedia: li + 1279), so "nearly 1,300 pages".
import sys, os, zipfile, tempfile, xml.etree.ElementTree as ET
p = sys.argv[1]
A = "Their book is a thousand pages and a toolbox. This one is not that book made smaller. It is the same idea, told in ordinary words, and brought up to what we have actually seen:"
B = "Their book, Gravitation, is a masterpiece, written for graduate students: nearly 1,300 pages, built on the tensor mathematics the full theory needs. This book is for everyone else who wants the same ideas. It is not that book made smaller. It tells those ideas in ordinary words, and brings them up to what we have actually seen:"
zin = zipfile.ZipFile(p); x = zin.read("word/document.xml").decode("utf8")
assert x.count(A) == 1, x.count(A); assert "MTW" not in x
x = x.replace(A, B); ET.fromstring(x.encode("utf8"))
fd, tmp = tempfile.mkstemp(suffix=".docx", dir=os.path.dirname(os.path.abspath(p))); os.close(fd)
with zipfile.ZipFile(tmp, "w") as zo:
    for i in zin.infolist(): zo.writestr(i, x.encode("utf8") if i.filename == "word/document.xml" else zin.read(i.filename), compress_type=i.compress_type)
zin.close(); z = zipfile.ZipFile(tmp); assert z.testzip() is None and B in z.read("word/document.xml").decode("utf8"); z.close()
os.replace(tmp, p); print("docx ok")
