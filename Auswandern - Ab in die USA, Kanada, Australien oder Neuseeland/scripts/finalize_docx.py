"""Updates the TOC and all fields in a DOCX (so page numbers are real) via a
running headless LibreOffice instance, then saves it back to the same path.

Start LibreOffice first, then run this script:
    soffice --headless --invisible --nocrashreport --nodefault --norestore \
        --nofirststartwizard --nologo \
        --accept="socket,host=localhost,port=2002;urp;" \
        -env:UserInstallation=file:///tmp/lo_profile &
    python3 finalize_docx.py <path-to-docx>

Requires libreoffice-writer + python3-uno (apt install libreoffice-writer
python3-uno if `import uno` fails).
"""
import sys
import urllib.parse
import uno
from com.sun.star.beans import PropertyValue


def make_prop(name, value):
    p = PropertyValue()
    p.Name = name
    p.Value = value
    return p


def main():
    if len(sys.argv) != 2:
        print("usage: python3 finalize_docx.py <path-to-docx>", file=sys.stderr)
        sys.exit(1)
    path = sys.argv[1]

    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_context)
    ctx = resolver.resolve(
        "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)

    url = "file://" + urllib.parse.quote(path)
    doc = desktop.loadComponentFromURL(url, "_blank", 0, (make_prop("Hidden", True),))
    try:
        indexes = doc.getDocumentIndexes()
        for i in range(indexes.getCount()):
            indexes.getByIndex(i).update()
        doc.getTextFields().refresh()
        doc.storeToURL(url, (make_prop("FilterName", "MS Word 2007 XML"),))
    finally:
        doc.close(False)

    print(f"Aktualisiert: {path}")


main()
