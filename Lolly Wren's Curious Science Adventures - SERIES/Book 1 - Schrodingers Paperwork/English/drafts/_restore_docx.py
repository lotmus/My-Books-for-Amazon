import shutil
from pathlib import Path

src = Path(
    r"D:\My Books for Amazon\Schrodingers_Paperwork\English"
    r"\Schrodingers_Paperwork_BOOK_1_2_BEFORE_FIGURE_FIX_BACKUP.docx"
)
dst = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")
if not dst.exists():
    shutil.copy2(src, dst)
    print("restored", dst, dst.stat().st_size)
else:
    print("already exists", dst.stat().st_size)
