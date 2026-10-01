import json, os, re, sys

W = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(W)
MAN = json.load(open(os.path.join(W, 'manifest.json'), encoding='utf-8'))
EXTRA = ['04_quantum_lectures.md', '11_novel_narrative_science.md']


def read(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8').replace('\r\n', '\n')


def texts():
    out = {}
    for m in MAN:
        out[m['file']] = '\n\n'.join(read(os.path.join(W, p)).strip('\n') for p in m['parts']) + '\n'
    for e in EXTRA:
        out[e] = read(os.path.join(SRC, e))
    return out


def books(text):
    cur, buf = None, []
    for line in text.splitlines():
        if line.startswith('# '):
            if cur:
                yield cur, buf
            cur, buf = line[2:].strip(), []
        elif cur:
            buf.append(line)
    if cur:
        yield cur, buf


NUM_H = re.compile(r'^#{2,4} (?:(\d+)\.|(?:Chapter|Storey|Lesson|Lecture) (\d+)\b)')
APP_H = re.compile(r'^#{2,4} Appendix (\d+)\b')
RANGE_H = re.compile(r'^#{2,4} (?:Chapters|Lessons|Lectures) (\d+)\s*[–-]\s*(\d+)')
REF = re.compile(r'\b(Chapter|Storey|Lesson|Lecture|Appendix) (\d+)\b')

PATTERNS = {
    'below/above': r'\b(?:see|shown|listed|described|given|set out|summari[sz]ed) (?:below|above)\b|\b(?:table|figure|diagram|chart|list|box|sidebar|illustration) (?:below|above)\b|\bthe following (?:table|figure|diagram|chart)\b',
    'promise': r"\b(?:as (?:we|you)(?:'ll| will) see|we(?:'ll| will) (?:return|come back|see)|more on (?:this|that) later|later in (?:this|the) (?:book|volume|series)|in a later chapter|a later chapter)\b",
    'production': r'\b(?:almanac|condensed|highlights|this volume|full edition|abridged|excerpt(?:ed)?|digest|in this collection|this compilation|the original book|the source book)\b',
    'partref': r'\bPart (?:I|II|III|IV|V|VI|VII|VIII|IX|X)\b',
    'volume/book N': r'\b(?:Volume|Vol\.?|Book) \d\b',
    'series': r'\bseries\b',
    'tics': r"\bhonest(?:ly)?\b|\bit(?:'s| is) worth\b|\bworth (?:noting|stressing|remembering|saying|pointing out)\b",
    'todo': r'\b(?:TODO|TBD|XXX|FIXME|placeholder|lorem)\b|\[\?\]|\?\?',
    'exercise': r'\b(?:exercise|answer key|answers at the end|solutions? (?:at|in) the back)\b',
}


def main():
    t = texts()
    print('=== dangling numbered references ===')
    for fname, text in t.items():
        for title, lines in books(text):
            nums, apps = set(), set()
            for l in lines:
                m = NUM_H.match(l)
                if m:
                    nums.add(int(m.group(1) or m.group(2)))
                m = APP_H.match(l)
                if m:
                    apps.add(int(m.group(1)))
                m = RANGE_H.match(l)
                if m:
                    nums.update(range(int(m.group(1)), int(m.group(2)) + 1))
            body = '\n'.join(l for l in lines if not l.startswith('#'))
            bad = {}
            for m in REF.finditer(body):
                word, n = m.group(1), int(m.group(2))
                ok = (n in apps) if word == 'Appendix' else (n in nums)
                if not ok:
                    ctx = body[max(0, m.start() - 70):m.end() + 30].replace('\n', ' ')
                    bad.setdefault(m.group(0), ctx)
            for k, ctx in bad.items():
                print(f'[{title[:30]}] {k}: ...{ctx}...')
    for name, pat in PATTERNS.items():
        rx = re.compile(pat, re.I)
        print(f'=== {name} ===')
        for fname, text in t.items():
            for title, lines in books(text):
                for l in lines:
                    if l.startswith('#'):
                        continue
                    for m in rx.finditer(l):
                        ctx = l[max(0, m.start() - 80):m.end() + 60]
                        print(f'[{title[:26]}] {ctx}')
    print('=== em dashes outside headings, per file ===')
    for fname, text in t.items():
        n = sum(l.count('\u2014') for l in text.splitlines() if not l.startswith('#'))
        print(fname, n)


main()
