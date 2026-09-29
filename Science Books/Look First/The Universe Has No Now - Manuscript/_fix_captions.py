from pathlib import Path

root = Path(r"D:\My Books for Amazon\Science Books\Look First\The Universe Has No Now - Manuscript")

# Ch 17 body + captions 17/18
p = root / "04_Part_Four_Missing.md"
t = p.read_text(encoding="utf-8")
t = t.replace(
    "On a Kindle those posters lie. Figure 17 is two stacked gray panels: the slammed gas, then the mass contours, same scale. Look at them one after the other. The contours do not sit on the gas. That is the photograph of “not atoms.”",
    "On a Kindle those posters lie. Figure 17 is one composite: the slammed gas labeled where it piled up, the mass labeled where lensing put it, same scene. The contours do not sit on the gas. That is the photograph of “not atoms.”",
)
t = t.replace(
    "![Figure 17. Two stacked panels of the Bullet Cluster: X-ray gas, then mass contours. The pull did not stay with the gas.](Figures/figs/fig17.png)",
    "![Figure 17. The Bullet Cluster as one composite: hot gas piled in the middle; mass, mapped by lensing, on either side. The pull did not stay with the gas.](Figures/figs/fig17.jpg)",
)
t = t.replace(
    "![Figure 18. A supernova remnant with a bright rim, cropped so the rim survives in gray. Bombs like this, farther off, taught us the stretch is speeding up.](Figures/figs/fig18.png)",
    "![Figure 18. The Crab Nebula, a supernova remnant with a bright rim. Explosions of a related kind, seen much farther off, taught us the stretch is speeding up.](Figures/figs/fig18.jpg)",
)
p.write_text(t, encoding="utf-8", newline="\n")
print("ok part4")

# Fig 31 — honest tractor pixels in a chapter about non-sleeping crews
p = root / "06_Part_Six_Getting_There.md"
t = p.read_text(encoding="utf-8")
t = t.replace(
    "![Figure 31. A machine in flight or on dirt, crisp against a bright ground. The crew that can wait.](Figures/figs/fig31.png)",
    "![Figure 31. A tractor on bright dirt, working a field. The photograph is patient Earth labor; the chapter’s crew that does not sleep is still a machine that can wait.](Figures/figs/fig31.jpg)",
)
p.write_text(t, encoding="utf-8", newline="\n")
print("ok part6")

# Fig 42
p = root / "09_Part_Nine_Filter.md"
t = p.read_text(encoding="utf-8")
t = t.replace(
    "![Figure 42. Two or three birds on a light ground, beaks readable. A filter can look like a craftsman.](Figures/figs/fig42.png)",
    "![Figure 42. One Galápagos finch on a light ground, beak readable. A filter can look like a craftsman.](Figures/figs/fig42.jpg)",
)
p.write_text(t, encoding="utf-8", newline="\n")
print("ok part9")

# Fig 45
p = root / "10_Part_Ten_Future.md"
t = p.read_text(encoding="utf-8")
t = t.replace(
    "![Figure 45. Rover tracks toward a near horizon, or Earth over a dead rim. Meaning is local, on one worldline.](Figures/figs/fig45.png)",
    "![Figure 45. Rover tracks toward a near horizon. Meaning is local, on one worldline.](Figures/figs/fig45.jpg)",
)
p.write_text(t, encoding="utf-8", newline="\n")
print("ok part10")

# Ch 22 egg echo — shorten second occurrence
p = root / "05_Part_Five_Horizons.md"
t = p.read_text(encoding="utf-8")
needle = "Eggs smash. They do not unsmash. Horizons form. They do not, around us, unform into fountains."
first = t.find(needle)
second = t.find(needle, first + 1) if first >= 0 else -1
if second >= 0:
    t = t[:second] + "Same smash. Same refusal of a fountain." + t[second + len(needle) :]
    p.write_text(t, encoding="utf-8", newline="\n")
    print("ok egg")
else:
    print("egg count", t.count(needle))

# Sync FIG dict in builder (Word uses these, not markdown alt text)
bp = root / "Figures" / "build_docx.py"
bt = bp.read_text(encoding="utf-8")
bt = bt.replace(
    '31: ("photo", "A machine on bright dirt. The crew that can wait.", ""),',
    '31: ("photo", "A tractor on bright dirt, working a field. The photograph is patient Earth labor; the chapter’s crew that does not sleep is still a machine that can wait.", ""),',
)
bt = bt.replace(
    '42: ("photo", "Finches on a light ground, beaks readable. A filter can look like a craftsman.", ""),',
    '42: ("photo", "One Galápagos finch on a light ground, beak readable. A filter can look like a craftsman.", ""),',
)
bt = bt.replace(
    '17: ("photo", "The Bullet Cluster, two galaxy clusters that passed through each other. The hot gas (center) piled up in the collision; the mass, mapped by lensing, kept going and sits on either side. The pull did not stay with the gas.", "Credit: NASA/CXC/CfA/M. Markevitch et al.; NASA/STScI; ESO WFI"),',
    '17: ("photo", "The Bullet Cluster as one composite: hot gas piled in the middle; mass, mapped by lensing, on either side. The pull did not stay with the gas.", "Credit: NASA/CXC/CfA/M. Markevitch et al.; NASA/STScI; ESO WFI"),',
)
bp.write_text(bt, encoding="utf-8", newline="\n")
print("ok build_docx")

import subprocess, sys, shutil
r = subprocess.run([sys.executable, str(root / "Figures" / "build_docx.py")], capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
src = root / "Figures" / "The Universe Has No Now - Kindle.docx"
dst = root / "export" / "The_Universe_Has_No_Now.docx"
if src.exists() and dst.parent.exists():
    shutil.copy2(src, dst)
    print("synced export")
