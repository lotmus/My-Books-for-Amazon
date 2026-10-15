import sys, re, docx
sys.path.insert(0, __import__('os').path.dirname(__file__))
from eedoc import *
from collections import Counter
T = '\n'.join(ptext(p) for p in body_ps(docx.Document(sys.argv[1])))
pats = r'\b(\w*(colour|behaviour|favour|honour|labour|neighbour|harbour|flavour|vapour|rumour|humour|odour|armour|savour)\w*|\w+(isation|ised|ising)|\w+ise[sd]?|\w+yse[sd]?|centre\w*|metres?|litres?|aluminium|tyres?|grey|whilst|amongst|programme\w*|analogue|catalogue|travell\w+|modell\w+|labell\w+|signall\w+|fibres?|defence|licence|practise\w*|trolley\w*|sulph\w+|learnt|spelt|earthing|earthed|towards|afterwards|judgement|maths|storey|plough|cheque|manoeuvre|mould\w*|artefact\w*)\b'
ok = re.compile(r'(?i)^(\w*wise|precise|concise|noise[sd]?|raise[sd]?|praise[sd]?|promise[sd]?|premise[sd]?|exercise[sd]?|expertise|surprise[sd]?|enterprise[sd]?|advise[sd]?|revise[sd]?|devise[sd]?|supervise[sd]?|comprise[sd]?|compromise[sd]?|franchise|demise|despise|disguise[sd]?|improvise[sd]?|excise|televise[sd]?|poise[sd]?|treatise|paradise|guise|reprise|arise[sd]?|rise[sd]?|advertise[sd]?|exercising|raising|rising|arising|surprising|promising|comprising|advising|revising|supervising|noising|praising|analyse)$')
c = Counter(m.group(0) for m in re.finditer(pats, T, re.I) if not ok.match(m.group(0)))
print(dict(c))
