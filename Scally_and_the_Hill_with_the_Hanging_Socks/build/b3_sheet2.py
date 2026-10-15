import sys, os, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
REF = os.path.join(gen.OUT, "sheet_b3_b.jpg")
P = ("Keep this painting exactly as it is, the same nine characters with identical faces, hair, clothes, poses, style and background, with only these corrections: "
     "Pip (the smallest boy) wears a plain red knitted cap that is smooth on top, with NO ear-shaped bumps, NO animal ears at all, and he has small ordinary round human ears and wears small brown boots; "
     "Scally (the little devil on the far left) wears big old brown boots on his feet; "
     "Gucci the wolf is a larger young wolf, as tall as Pip's shoulder, with long legs, thick gray fur, blue eyes and one floppy ear; "
     "Tabitha has small round human ears with no points; every human has round ears and only Scally and Hopsi have pointed ears.")
for n in (sys.argv[1:] or ["sheet_b3_c", "sheet_b3_d"]):
    gen.edit_with(n, REF, P, "3:2")
