# 11 Oct 2026: Rev10 in place. The book is no longer titled after MTW's Gravitation, so the clause
# "the large 1973 textbook this book takes its title from" becomes "the large 1973 textbook whose spirit this book borrows".
import sys, os, zipfile, tempfile, xml.etree.ElementTree as ET
p = sys.argv[1]
A = "the large 1973 textbook this book takes its title from."; B = "the large 1973 textbook whose spirit this book borrows."
zin = zipfile.ZipFile(p); x = zin.read("word/document.xml").decode("utf8")
assert x.count(A) == 1, x.count(A); n0 = x.count("Gravitation")
x = x.replace(A, B); assert x.count("Gravitation") == n0; ET.fromstring(x.encode("utf8"))
fd, tmp = tempfile.mkstemp(suffix=".docx", dir=os.path.dirname(os.path.abspath(p))); os.close(fd)
with zipfile.ZipFile(tmp, "w") as zo:
    for i in zin.infolist(): zo.writestr(i, x.encode("utf8") if i.filename == "word/document.xml" else zin.read(i.filename), compress_type=i.compress_type)
zin.close(); z = zipfile.ZipFile(tmp); assert z.testzip() is None and B in z.read("word/document.xml").decode("utf8"); z.close()
os.replace(tmp, p); print("ok")
