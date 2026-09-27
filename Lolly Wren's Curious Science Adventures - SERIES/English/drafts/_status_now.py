from pathlib import Path

root = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork")
for p in [
    root / "Schrodingers_Paperwork_BOOK_1_2.docx",
    root / "Schrodingers_Paperwork_BOOK_1_2.docx.repack",
    root / "English" / "Schrodingers_Paperwork_BOOK_1_2_BEFORE_FIGURE_FIX_BACKUP.docx",
    root / "English" / "_fig_out",
]:
    if p.is_dir():
        files = list(p.glob("*"))
        print("DIR", p.name, "n=", len(files), [f.name for f in files])
    elif p.exists():
        print("FILE", p.name, p.stat().st_size)
    else:
        print("MISSING", p.name)
