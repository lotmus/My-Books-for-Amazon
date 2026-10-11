# -*- coding: utf-8 -*-
# Scan the model (not the docx) for repeated / near-repeated sentences, reporting section ids.
import io, sys, collections, re
from model import build_model, all_sections
from uscan import sents, norm
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def run(min_exact=4, min_fuzzy=7, thr=0.6, front=True):
    parts, fr, log = build_model()
    items = []   # (order, chapter#, chapter title, sid, section title, sentence)
    for n, ct, s, lead in all_sections(parts):
        for t in s['paras']:
            if t.startswith('**Topics'): continue
            for st in sents(re.sub(r'\*\*', '', t)): items.append((n, ct, s['id'], s['title'], st))
    if front:
        for key in ('epilogue', 'note', 'preface', 'sources'):
            for t in fr[key]['paras']:
                for st in sents(t): items.append((99, key, key, key, st))
    return items, log
def exact_dups(items, m=4):
    occ = collections.defaultdict(list)
    for k, it in enumerate(items):
        n = norm(it[4])
        if len(n.split()) >= m: occ[n].append(k)
    return [v for v in occ.values() if len(v) > 1]
def near_dups(items, mf=7, thr=0.6):
    grams = {}; index = collections.defaultdict(set)
    for k, it in enumerate(items):
        w = norm(it[4]).split()
        if len(w) >= mf:
            g = set(tuple(w[j:j+4]) for j in range(len(w)-3)); grams[k] = g
            for x in g: index[x].add(k)
    out = []
    for k, g in grams.items():
        cand = collections.Counter()
        for x in g:
            for m in index[x]:
                if m > k: cand[m] += 1
        for m, c in cand.items():
            if c < 2 or norm(items[k][4]) == norm(items[m][4]): continue
            h = grams[m]; cont = len(g & h) / min(len(g), len(h))
            if cont >= thr: out.append((k, m, cont))
    return out
if __name__ == '__main__':
    items, log = run()
    for l in log: print('LOG', l)
    ex = exact_dups(items); nr = near_dups(items)
    words = sum(len(items[k][4].split()) for v in ex for k in v[1:])
    print('EXACT groups', len(ex), 'repeat words', words, '| NEAR pairs', len(nr))
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    loc = lambda it: '%s/%s[%s]' % (it[0], it[3][:34], it[2])
    if mode in ('all', 'exact'):
        for v in sorted(ex, key=lambda v: v[0]):
            print('EXACT x%d: %s' % (len(v), items[v[0]][4][:140]))
            for k in v: print('     ', loc(items[k]))
    if mode in ('all', 'near'):
        for k, m, c in sorted(nr):
            print('NEAR %.2f' % c); print('   A', loc(items[k]), items[k][4][:150]); print('   B', loc(items[m]), items[m][4][:150])
