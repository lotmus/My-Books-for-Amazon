# -*- coding: utf-8 -*-
from docx import Document
import re, json, os
from collections import defaultdict, Counter

path = r'D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1.docx'
out_dir = r'D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_audit_10'
doc = Document(path)
paras = [(i, (p.style.name if p.style else ''), p.text or '') for i, p in enumerate(doc.paragraphs)]

# Narrative range only
narrative_end = 2104
narrative = [(i, s, t) for i, s, t in paras if i < narrative_end]

patterns = {
    'Tegner': re.compile(r'Tegn[eé]r', re.I),
    'Tegmark': re.compile(r'Tegmark', re.I),
    'Peck': re.compile(r'\bPeck\b'),
    'Voss': re.compile(r'\bVoss\b'),
    'eighth_week': re.compile(r'eighth week|eight weeks|8th week', re.I),
    'von_Wittenberg': re.compile(r'von Wittenberg', re.I),
    'Witten\b': re.compile(r'\bWitten\b'),
    'Tuesday_afternoon': re.compile(r'Tuesday afternoon', re.I),
    'Rules_for': re.compile(r'Rules for', re.I),
    'Physics_Notes': re.compile(r'Physics Notes', re.I),
    'injunction': re.compile(r'injunction', re.I),
    'Fenwick': re.compile(r'Fenwick', re.I),
    'Monday|Tuesday seal': re.compile(r'(Monday|Mon\.?).{0,40}(hearing|seal)|seal.{0,40}(Tuesday|Tue)', re.I),
    'double_the_the': re.compile(r'\bthe the\b', re.I),
    'double_words': re.compile(r'\b(\w+)\s+\1\b', re.I),
}

hits = defaultdict(list)
for i, s, t in narrative:
    if not t.strip():
        continue
    for name, rx in patterns.items():
        for m in rx.finditer(t):
            hits[name].append((i, m.group(0), t[max(0, m.start()-40):m.end()+60].replace('\n', ' ')))

# Broader rule-block search
ruleish = []
for i, s, t in narrative:
    ts = t.strip()
    if re.search(r'^(Rule|Rules|What this chapter|One-line|Remember:|Do not |Never )', ts):
        ruleish.append((i, s, ts[:140]))
    if 'Rules for' in ts or ts.startswith('•') or (ts.startswith('-') and len(ts) < 120):
        ruleish.append((i, s, ts[:140]))

# Chapter map from meta
with open(os.path.join(out_dir, '_meta.json'), encoding='utf-8') as f:
    meta = json.load(f)

def chap_of(idx):
    for m in meta:
        if m['start'] <= idx < m['end']:
            return m['title']
    return '?'

report = []
report.append('=== PATTERN HITS (narrative only) ===')
for name in sorted(hits.keys()):
    report.append(f'\n## {name}: {len(hits[name])}')
    for i, g, snip in hits[name][:40]:
        report.append(f'  p{i} [{chap_of(i)}] {g!r} :: {snip[:140]}')
    if len(hits[name]) > 40:
        report.append(f'  ... +{len(hits[name])-40} more')

report.append('\n=== RULE-ISH PARAS ===')
for i, s, ts in ruleish[:100]:
    report.append(f'p{i} [{s}] {ts}')

# Also scan closing paras for physics pointers more loosely
report.append('\n=== CHAPTER CLOSING + OPENING SNIPS ===')
for m in meta:
    report.append(f"\n#### {m['title']} ({m['words']}w) paras {m['start']}-{m['end']}")
    report.append('OPEN:')
    for i, t in m['opening'][:3]:
        report.append(f'  p{i}: {t[:220]}')
    report.append('CLOSE:')
    for i, t in m['closing'][-4:]:
        report.append(f'  p{i}: {t[:220]}')
    # look for Rules / Physics in last 15 non-empty
    last_nonempty = []
    for i in range(m['end'] - 1, m['start'], -1):
        t = paras[i][2].strip()
        if t:
            last_nonempty.append((i, t))
            if len(last_nonempty) >= 12:
                break
    for i, t in last_nonempty:
        if re.search(r'rule|physics|appendix|lecture|remember', t, re.I):
            report.append(f'  HINT p{i}: {t[:200]}')

outp = os.path.join(out_dir, '_scan.txt')
with open(outp, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report))
print('wrote', outp)
print('hit counts:', {k: len(v) for k, v in hits.items()})
print('ruleish count', len(ruleish))
