from pathlib import Path

root = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork")
for p in sorted(root.glob("*.docx*")):
    print(p.name, p.stat().st_size)
eng = root / "English"
for p in sorted(eng.glob("*BOOK_1_2*")):
    print("ENG", p.name, p.stat().st_size)
