import json, os, re, sys

W = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(W)
MAN = json.load(open(os.path.join(W, 'manifest.json'), encoding='utf-8'))


def read(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8')


def norm(t):
    return t.replace('\r\n', '\n')


def joined(folder):
    out = {}
    for m in MAN:
        pieces = [norm(read(os.path.join(folder, p))) for p in m['parts']]
        pieces = [p.strip('\n') for p in pieces]
        out[m['file']] = '\n\n'.join(pieces) + '\n'
    return out


def ws(t):
    return re.sub(r'\s+', ' ', t).strip()


def cmd_test():
    for name, text in joined(os.path.join(W, 'orig')).items():
        cur = norm(read(os.path.join(SRC, name)))
        print(f"{name:28} exact={text == cur} ws_equal={ws(text) == ws(cur)}")


def cmd_check():
    for m in MAN:
        for n in m['parts']:
            a = norm(read(os.path.join(W, n)))
            b = norm(read(os.path.join(W, 'orig', n)))
            ha = [l.rstrip() for l in a.splitlines() if l.startswith('#')]
            hb = [l.rstrip() for l in b.splitlines() if l.startswith('#')]
            paras = [p for p in re.split(r'\n\s*\n', a) if not p.lstrip().startswith(('#', '-', '*  ', '1.'))]
            longp = sum(1 for p in paras if len(p.split()) > 200)
            st = len(re.findall(r'(?m)^\*Status: .+\*\s*$', a))
            print(f"{n:34} {len(b.split()):6} -> {len(a.split()):6} "
                  f"{'HEAD_OK' if ha == hb else 'HEAD_DIFF'} status={st} "
                  f"emdash={a.count(chr(0x2014))} long={longp} "
                  f"{'UNCHANGED' if a == b else ''}")
    print('glossary exists:', os.path.exists(os.path.join(SRC, '12_glossary.md')))


def cmd_join():
    for name, text in joined(W).items():
        orig_raw = read(os.path.join(SRC, name))
        nl = '\r\n' if '\r\n' in orig_raw else '\n'
        with open(os.path.join(SRC, name), 'wb') as f:
            f.write(text.replace('\n', nl).encode('utf-8'))
        print('joined', name, len(text.split()), 'words')


{'test': cmd_test, 'check': cmd_check, 'join': cmd_join}[sys.argv[1]]()
