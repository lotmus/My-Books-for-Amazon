import zipfile
from pathlib import Path

docx = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")
out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\English\_fig_out")
out.mkdir(exist_ok=True)
with zipfile.ZipFile(docx) as z:
    for n in z.namelist():
        if n.startswith("word/media/"):
            dest = out / Path(n).name
            dest.write_bytes(z.read(n))
            print(dest.name, dest.stat().st_size)
