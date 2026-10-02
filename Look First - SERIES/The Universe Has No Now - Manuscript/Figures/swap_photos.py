# Copy drop-in JPEGs onto the live photo slots.
# Contract: figs/figNN.jpg beats figs/figNN_slot.png (see build_docx.py).
# Drop fig00.jpg, fig01.jpg, fig31.jpg, fig32.jpg, fig34.jpg, or fig42.jpg
# into this folder or into figs/. Then run: python swap_photos.py
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
SLOTS = (0, 1, 31, 32, 34, 42)

def main():
    os.makedirs(FIGS, exist_ok=True)
    copied = []
    for n in SLOTS:
        name = "fig%02d.jpg" % n
        src = os.path.join(HERE, name)
        dest = os.path.join(FIGS, name)
        if os.path.isfile(src) and os.path.abspath(src) != os.path.abspath(dest):
            shutil.copy2(src, dest)
            copied.append(name)
        elif os.path.isfile(dest):
            copied.append(name + " (already in figs/)")
    still = ["fig%02d.jpg" % n for n in SLOTS if not os.path.isfile(os.path.join(FIGS, "fig%02d.jpg" % n))]
    print("copied or present:", copied or "(none)")
    print("still needed:", still or "(none — all six photos landed)")

if __name__ == "__main__":
    main()
