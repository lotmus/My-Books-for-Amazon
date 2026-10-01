# -*- coding: utf-8 -*-
import subprocess
root = r"C:\Users\lomus\OneDrive\My Books for Amazon"
files = {
    "07": "Science Books/Look First/A Trip Is Not a New Life - Manuscript/07_Part_Seven_Many_Clocks.md",
    "09": "Science Books/Look First/A Trip Is Not a New Life - Manuscript/09_Part_Nine_Not_A_Straight_Line.md",
}
for key, path in files.items():
    t = subprocess.check_output(["git", "show", "HEAD:" + path], cwd=root).decode("utf-8")
    print("====", key, "len", len(t))
    for i, line in enumerate(t.splitlines(), 1):
        if "Appendix A30" in line or "Appendix A32" in line or "Appendix A40" in line or "Appendix A41" in line or "See A30" in line or "see A30" in line or "A30." in line:
            print(f"{key}:{i}: {line[:300]}")
