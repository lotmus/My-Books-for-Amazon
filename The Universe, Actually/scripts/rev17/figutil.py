import os, json
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from PIL import Image
os.makedirs('fig', exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Serif', 'font.size': 9, 'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.titlesize': 10.5, 'axes.titleweight': 'bold', 'axes.labelsize': 9})
NAVY = '#1f4e79'; RED = '#c0392b'; GREEN = '#2e7d32'; GOLD = '#d4a017'; GREY = '#666666'; PURPLE = '#6a3d9a'
kB = 1.380649e-23; h = 6.62607e-34; c = 2.99792458e8
REG_FILE = 'fig/registry.json'
def new(w=8, h_=4.4): return plt.subplots(figsize=(w, h_), dpi=100)
def rk4(f, y0, t):
    y = np.zeros((len(t), len(y0))); y[0] = y0
    for i in range(len(t) - 1):
        dt = t[i + 1] - t[i]; k1 = np.array(f(t[i], y[i])); k2 = np.array(f(t[i] + dt / 2, y[i] + dt / 2 * k1))
        k3 = np.array(f(t[i] + dt / 2, y[i] + dt / 2 * k2)); k4 = np.array(f(t[i] + dt, y[i] + dt * k3))
        y[i + 1] = y[i] + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y
def save(fig, name, chapter, anchor, caption, alt):
    path = 'fig/%s.png' % name
    fig.tight_layout(); fig.savefig(path, dpi=100); plt.close(fig)
    im = Image.open(path).convert('RGB').quantize(colors=128, method=Image.MEDIANCUT, dither=Image.NONE)
    im.save(path, optimize=True)
    reg = json.load(open(REG_FILE, encoding='utf-8')) if os.path.exists(REG_FILE) else {}
    reg[name] = {'file': path, 'chapter': chapter, 'anchor': anchor, 'caption': caption, 'alt': alt}
    json.dump(reg, open(REG_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(name, os.path.getsize(path) // 1024, 'KB')
