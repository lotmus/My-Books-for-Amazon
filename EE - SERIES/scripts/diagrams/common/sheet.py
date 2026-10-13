import sys
from PIL import Image
def sheet(files, out, cols=2, w=800):
    t = [Image.open(f).convert('RGB') for f in files]; t = [x.resize((w, int(x.height * w / x.width))) for x in t]
    rows = [t[i:i+cols] for i in range(0, len(t), cols)]; H = [max(x.height for x in r) for r in rows]
    S = Image.new('RGB', (w * cols, sum(H)), 'white'); y = 0
    for r, h in zip(rows, H):
        for k, x in enumerate(r): S.paste(x, (k * w, y))
        y += h
    S.save(out)
if __name__ == '__main__': sheet(sys.argv[2:], sys.argv[1])
