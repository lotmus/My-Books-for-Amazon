# -*- coding: utf-8 -*-
# Scan a docx for repeated sentences: exact, near-duplicate, and long shared phrases.
import io, sys, re, collections, docx
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def sents(text):
    text = text.replace('\n', ' ')
    parts = re.split(r'(?<=[.!?])["”’)]*\s+(?=["“‘(]?[A-Z0-9“])', text)
    return [p.strip() for p in parts if p.strip()]
def norm(s): return re.sub(r'[^a-z0-9 ]', '', re.sub(r'[’‘“”"\']', '', s.lower())).strip()

def load(path, skip_pred=None):
    ps = docx.Document(path).paragraphs
    items = []   # (para_idx, sentence)
    for i, p in enumerate(ps):
        if p.style.name.startswith('Heading') or p.style.name in ('Title', 'Subtitle', 'Author', 'Source Code'):
            continue
        if skip_pred and skip_pred(i, p): continue
        for s in sents(p.text): items.append((i, s))
    return ps, items

def scan(items, min_exact=4, min_fuzzy=7, thr=0.6, show=True):
    out = []
    occ = collections.defaultdict(list)
    for i, s in items:
        n = norm(s)
        if len(n.split()) >= min_exact: occ[n].append((i, s))
    exact = [(v[0][0], 'EXACT', [i for i, _ in v], v[0][1]) for n, v in occ.items() if len(v) > 1]
    # near duplicates
    grams = {}
    index = collections.defaultdict(set)
    toks = []
    for k, (i, s) in enumerate(items):
        w = norm(s).split()
        toks.append(w)
        if len(w) >= min_fuzzy:
            g = set(tuple(w[j:j+4]) for j in range(len(w)-3))
            grams[k] = g
            for x in g: index[x].add(k)
    seen = set(); near = []
    for k, g in grams.items():
        cand = collections.Counter()
        for x in g:
            for m in index[x]:
                if m > k: cand[m] += 1
        for m, c in cand.items():
            if c < 2: continue
            if norm(items[k][1]) == norm(items[m][1]): continue
            h = grams[m]
            inter = len(g & h)
            cont = inter / min(len(g), len(h))
            if cont >= thr and items[k][0] != items[m][0] or (cont >= thr and items[k][0] == items[m][0]):
                near.append((items[k][0], 'NEAR %.2f' % cont, [items[k][0], items[m][0]], items[k][1], items[m][1]))
    return sorted(exact, key=lambda r: r[0]), sorted(near, key=lambda r: r[0])

if __name__ == '__main__':
    path = sys.argv[1]
    ps, items = load(path)
    exact, near = scan(items)
    print('EXACT repeated sentences (>=4 words):', len(exact))
    for _, tag, idx, s in exact: print('  x%d %s | %s' % (len(idx), idx, s[:160]))
    print('\nNEAR duplicate sentence pairs:', len(near))
    for r in near: print('  %s %s\n     A: %s\n     B: %s' % (r[1], r[2], r[3][:170], r[4][:170]))
