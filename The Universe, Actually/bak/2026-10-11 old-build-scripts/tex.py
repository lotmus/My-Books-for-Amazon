# -*- coding: utf-8 -*-
# Convert the light LaTeX used in the manuscript into runs: list of (text, kind) with kind in '', 'sup', 'sub'.
import re
GREEK = {'alpha':'α','beta':'β','gamma':'γ','delta':'δ','epsilon':'ε','varepsilon':'ε','zeta':'ζ','eta':'η','theta':'θ','kappa':'κ',
 'lambda':'λ','mu':'μ','nu':'ν','xi':'ξ','pi':'π','rho':'ρ','sigma':'σ','tau':'τ','phi':'φ','chi':'χ','psi':'ψ','omega':'ω',
 'Gamma':'Γ','Delta':'Δ','Theta':'Θ','Lambda':'Λ','Xi':'Ξ','Pi':'Π','Sigma':'Σ','Phi':'Φ','Psi':'Ψ','Omega':'Ω'}
SYM = {'hbar':'ħ','times':' × ','approx':' ≈ ','cdot':' · ','pm':' ± ','sim':' ~ ','ll':' ≪ ','gg':' ≫ ','ge':' ≥ ','geq':' ≥ ','le':' ≤ ','leq':' ≤ ',
 'to':' → ','rightarrow':' → ','propto':' ∝ ','infty':'∞','partial':'∂','nabla':'∇','circ':'°','odot':'⊙','cup':' ∪ ','sum':'∑','int':'∫',
 'uparrow':'↑','downarrow':'↓','rangle':'⟩','langle':'⟨','ldots':'…','dots':'…','neq':' ≠ ','equiv':' ≡ ','hbar':'ħ','ell':'ℓ',
 'sin':'sin ','cos':'cos ','tan':'tan ','ln':'ln ','log':'log ','max':'max ','min':'min ','exp':'exp ',
 ',':' ',';':' ',' ':' ','quad':' ','qquad':'  ','!':'','left':'','right':'','bigl':'','bigr':'','Big':'','big':'','{':'{','}':'}'}
SKIP_GROUP = {'mathrm','text','mathbf','mathcal','mathbb','mathit','operatorname','textrm','boldsymbol'}
WARN = set()

def _group(s, i):
    """s[i]=='{' -> (content, index after)"""
    depth = 0; j = i
    while j < len(s):
        if s[j] == '{': depth += 1
        elif s[j] == '}':
            depth -= 1
            if depth == 0: return s[i+1:j], j+1
        j += 1
    return s[i+1:], len(s)

def _atom(s, i):
    while i < len(s) and s[i] == ' ': i += 1
    if i >= len(s): return '', i
    if s[i] == '{': return _group(s, i)
    if s[i] == '\\':
        m = re.match(r'\\([A-Za-z]+|.)', s[i:])
        return m.group(0), i + len(m.group(0))
    return s[i], i + 1

def parse(s):
    runs = []
    def add(t, k=''):
        if t: runs.append((t, k))
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            m = re.match(r'\\([A-Za-z]+|.)', s[i:])
            cmd = m.group(1); i += len(m.group(0))
            if cmd in GREEK: add(GREEK[cmd])
            elif cmd == 'frac':
                a, i = _atom(s, i); b, i = _atom(s, i)
                ra, rb = parse(a), parse(b)
                ta, tb = ''.join(t for t, _ in ra), ''.join(t for t, _ in rb)
                wa = len(ta.strip()) > 1 and not re.fullmatch(r'[\w.]+', ta.strip())
                wb = len(tb.strip()) > 1 and not re.fullmatch(r'[\w.]+', tb.strip())
                if wa: add('(')
                runs.extend(ra)
                if wa: add(')')
                add('/')
                if wb: add('(')
                runs.extend(rb)
                if wb: add(')')
            elif cmd == 'sqrt':
                if i < len(s) and s[i] == '[':
                    j = s.index(']', i); i = j + 1
                a, i = _atom(s, i); ra = parse(a)
                ta = ''.join(t for t, _ in ra)
                add('√')
                if len(ta) > 1: add('(')
                runs.extend(ra)
                if len(ta) > 1: add(')')
            elif cmd in SKIP_GROUP:
                a, i = _atom(s, i); runs.extend(parse(a))
            elif cmd in ('dot', 'ddot', 'hat', 'bar', 'vec', 'tilde'):
                a, i = _atom(s, i); ra = parse(a)
                mark = {'dot':'̇','ddot':'̈','hat':'̂','bar':'̄','vec':'⃗','tilde':'̃'}[cmd]
                runs.extend(ra)
                if runs: runs[-1] = (runs[-1][0] + mark, runs[-1][1])
            elif cmd in SYM: add(SYM[cmd])
            else:
                WARN.add(cmd); add(cmd)
        elif c in '^_':
            a, i = _atom(s, i + 1)
            k = 'sup' if c == '^' else 'sub'
            inner = parse(a)
            for t, kk in inner: runs.append((t, k if kk == '' else kk))
        elif c in '{}':
            i += 1
        elif c == '~':
            add(' '); i += 1
        else:
            add(c); i += 1
    # merge adjacent same-kind
    out = []
    for t, k in runs:
        if out and out[-1][1] == k: out[-1] = (out[-1][0] + t, k)
        else: out.append((t, k))
    # tidy spaces: collapse doubles, fix minus signs
    res = []
    for t, k in out:
        t = re.sub(r' {2,}', ' ', t)
        if k in ('sup', 'sub'): t = t.replace('-', '−')
        res.append((t, k))
    # trim leading/trailing spaces overall
    if res:
        res[0] = (res[0][0].lstrip(), res[0][1]); res[-1] = (res[-1][0].rstrip(), res[-1][1])
    return [(t, k) for t, k in res if t]

def plain(s):
    return ''.join(t for t, _ in parse(s))

if __name__ == '__main__':
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    for t in [r'T_2 = T_1(V_1/V_2)^{\gamma-1} = 300\times 2^{0.4} \approx 396', r'F/A = -\frac{\pi^2\hbar c}{240 d^4}', r'E_n = -13.6\,\mathrm{eV}/n^2',
              r'c = 1/\sqrt{\mu_0 \epsilon_0}', r'\mathcal{N}=4', r'|\uparrow\rangle', r'\dot{x}']:
        print(parse(t))
    print(WARN)
