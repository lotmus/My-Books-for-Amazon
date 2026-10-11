# -*- coding: utf-8 -*-
import io, sys, re, json, zipfile
from lxml import etree
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
z = zipfile.ZipFile('../The_Universe_Actually__REV11.docx')
root = etree.fromstring(z.read('word/document.xml'))
body = list(root.find(W + 'body'))
def xml(el):
    s = etree.tostring(el, encoding='unicode')
    return re.sub(r'\sxmlns:\w+="[^"]*"', '', s)
def text(el): return ''.join(t.text or '' for t in el.iter(W + 't'))
T = [text(e) for e in body]
pool = {s['id']: s for s in json.load(open('pool.json', encoding='utf-8'))}

fb = {}
fb['title_xml'] = [xml(e) for e in body[0:9]]
fb['note'] = {'title': 'A Note on This Book', 'paras': T[10:14]}
fb['preface'] = {'title': 'Preface', 'paras': T[15:33]}
fb['epilogue'] = {'title': 'Epilogue: Actually', 'paras': T[3594:3607]}
fb['sources'] = {'title': 'A Note on Sources', 'paras': T[3608:3610]}
fb['bibliography'] = {'paras': T[3611:3641]}
fb['appendix'] = {'review': T[3642], 'author': T[3645:3647]}
fb['alsoby_xml'] = [R for R in [xml(e) for e in body[3016:3026]]]
fb['alsoby_title'] = 'Also by Lothar J. Musiol'

# merge the five link pages by topic
URL = re.compile(r'https?://[^\s)]+')
topics = {}; order = []
intro = []
for sid in (2893, 2903, 2918, 2936, 2951):
    for t in pool[sid]['paras']:
        m = re.match(r'\*\*(.+?)\*\*\s*(.*)', t)
        if not m: continue
        name, rest = m.group(1).strip(), m.group(2)
        key = re.sub(r'[^a-z]', '', name.lower().replace('&', 'and'))
        if key not in topics: topics[key] = {'name': name, 'items': []}; order.append(key)
        # split rest into (label, url) pairs
        pos = 0
        for u in URL.finditer(rest):
            label = rest[pos:u.start()].strip().rstrip(':').strip()
            pos = u.end()
            url = u.group(0).rstrip('.,;')
            if url not in [x[1] for x in topics[key]['items']]: topics[key]['items'].append((label, url))
res = ['The links below point to reliable outside material for the main subjects in this book. They are starting points, not endorsements of every claim on the pages they lead to. The addresses are written out in full so that Kindle and other readers make them tappable.']
for key in order:
    d = topics[key]
    parts = []
    for label, url in d['items']:
        parts.append((label + ': ' if label and not label.startswith('(') else '') + url)
    res.append('**%s** ' % d['name'] + '  '.join(parts))
fb['resources'] = {'paras': res}
json.dump(fb, open('frontback.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print({k: (len(v) if isinstance(v, list) else len(v.get('paras', []))) for k, v in fb.items()})
print(len(order), 'resource topics')
for r in res[:6]: print(r[:200])
