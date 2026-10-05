import io, sys, re, collections, docx
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
N = int(sys.argv[2]) if len(sys.argv) > 2 else 9
ps = docx.Document(sys.argv[1]).paragraphs
def norm(t): return re.sub(r'[^a-z0-9 ]', ' ', re.sub(r'[’‘“”"\']', '', t.lower())).split()
occ = collections.defaultdict(set)
toks = {}
for i, p in enumerate(ps):
    if p.style.name.startswith('Heading') or p.style.name in ('Title','Subtitle','Author','Source Code'): continue
    w = norm(p.text); toks[i] = w
    for j in range(len(w) - N + 1):
        occ[tuple(w[j:j+N])].add(i)
rep = {g: v for g, v in occ.items() if len(v) > 1}
# merge overlapping grams per paragraph pair into maximal runs
pairs = collections.defaultdict(list)
for g, v in rep.items():
    v = sorted(v)
    for a in range(len(v)):
        for b in range(a+1, len(v)):
            pairs[(v[a], v[b])].append(g)
out = []
for (a, b), gs in pairs.items():
    wa = toks[a]
    starts = sorted(set(next(j for j in range(len(wa)-N+1) if tuple(wa[j:j+N]) == g) for g in gs))
    # extend runs
    runs = []; s = starts[0]; e = s + N
    for st in starts[1:]:
        if st <= e - N + 1 + 0 and st < e: e = max(e, st + N)
        else: runs.append((s, e)); s, e = st, st + N
    runs.append((s, e))
    for s, e in runs:
        out.append((a, b, e - s, ' '.join(wa[s:e])))
out.sort(key=lambda r: -r[2])
print('shared phrases >=%d words between different paragraphs: %d' % (N, len(out)))
for a, b, n, t in out: print('  [%d,%d] %d words: %s' % (a, b, n, t[:200]))
