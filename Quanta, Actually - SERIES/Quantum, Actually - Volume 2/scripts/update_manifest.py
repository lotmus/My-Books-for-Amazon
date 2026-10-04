"""Refresh scripts/MANIFEST.sha256 and the off-OneDrive backup zip.

Run from anywhere:  python scripts/update_manifest.py
The backup goes to D:\\QED_Course_backup\\QED_Course_sources_latest.zip and holds the
lesson sources, the scripts, the manifest, the Complete docx and every standalone lesson docx.
Every docx is verified with zipfile.testzip() first; if any is damaged the script stops
without touching the manifest or the backup.
"""
import glob
import hashlib
import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
files = (sorted(glob.glob("scripts/lesson*.txt"))
         + ["scripts/build_lesson.py", "scripts/insert_toc.py", "scripts/update_manifest.py",
            "Quantum, Actually - Volume 2.docx"])
bad = [f for f in glob.glob("*.docx") + glob.glob("chapters/*.docx") if zipfile.ZipFile(f).testzip() is not None]
if bad:
    sys.exit("DAMAGED docx files, not updating manifest: %s" % bad)
lines = ["%s  %s" % (hashlib.sha256(open(f, "rb").read()).hexdigest(), f.replace(os.sep, "/"))
         for f in files]
open("scripts/MANIFEST.sha256", "w", encoding="utf-8").write("\n".join(lines) + "\n")
dest_dir = r"D:\QED_Course_backup"
os.makedirs(dest_dir, exist_ok=True)
dest = os.path.join(dest_dir, "QED_Course_sources_latest.zip")
tmp = dest + ".tmp"
with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
    for f in files + ["scripts/MANIFEST.sha256"] + sorted(glob.glob("chapters/Lesson *.docx")):
        z.write(f, f)
assert zipfile.ZipFile(tmp).testzip() is None
os.replace(tmp, dest)
print("manifest entries: %d | backup: %s (%d bytes) | all %d docx OK"
      % (len(lines), dest, os.path.getsize(dest), len(glob.glob("*.docx") + glob.glob("chapters/*.docx"))))
