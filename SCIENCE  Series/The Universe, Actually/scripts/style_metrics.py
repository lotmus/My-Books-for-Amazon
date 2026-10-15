# -*- coding: utf-8 -*-
import io, sys, re, collections
from model import build_model, all_sections
from uscan import sents
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
parts, front, log = build_model()
STOCK = [r'remains? (an )?open', r'is not (yet )?(established|confirmed)', r'has not been (confirmed|observed|detected)', r'No (such )?\w+( \w+)? (has|have) (yet )?been', r'remains? (unresolved|unknown|uncertain|incomplete)', r'it is not a', r'is (therefore|thus) ', r'The (result|framework|theory|model|process) is']
rows = []; stock = collections.Counter(); tot = 0
chap = {}
for n, ct, s, lead in all_sections(parts):
    for t in s['paras']:
        if t.startswith('**Topics') or t.startswith('\\['): continue
        ss = sents(re.sub(r'\*\*', '', t))
        c = chap.setdefault((n, ct), {'sent': 0, 'words': 0, 'short': 0, 'long': 0})
        for x in ss:
            w = len(x.split()); c['sent'] += 1; c['words'] += w
            if w <= 6: c['short'] += 1
            if w >= 28: c['long'] += 1
            for p in STOCK:
                if re.search(p, x, re.I): stock[p] += 1
            tot += 1
print('sentences', tot)
for p, k in stock.most_common(): print(k, p)
print()
res = []
for (n, ct), c in chap.items():
    res.append((c['short'] / c['sent'], c['words'] / c['sent'], n, ct, c['words']))
res.sort(reverse=True)
print('most staccato (share of sentences <=6 words, mean length):')
for sh, m, n, ct, w in res[:30]: print('%.2f %.1f %2d %s (%d words)' % (sh, m, n, ct, w))
print('mean share', sum(r[0] for r in res) / len(res))
# spelling variants
txt = ' '.join(t for n, ct, s, l in all_sections(parts) for t in s['paras'])
for a, b in [('color', 'colour'), ('center', 'centre'), ('kilometers', 'kilometres'), ('organize', 'organise'), ('analyze', 'analyse'), ('behavior', 'behaviour'), ('meter', 'metre'), ('realize', 'realise'), ('favor', 'favour')]:
    print(a, len(re.findall(r'\b%s\w*' % a, txt)), b, len(re.findall(r'\b%s\w*' % b, txt)))
