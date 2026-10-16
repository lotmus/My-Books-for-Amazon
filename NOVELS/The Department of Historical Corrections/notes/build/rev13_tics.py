from rev13_view import *
import re,collections
L,ch=chapters()
body='\n'.join(p for n,(i,j,h,ps) in ch.items() for p in ps)
pats=['with the air of','a man who','a woman who','as though','as if','like a ','like an ','did not look up','for a moment','for a long moment','said nothing','looked at him','looked at her','for the avoidance of doubt','which was','a little','slightly','quietly','briefly','politely','dryly','carefully','precisely','exactly','Apparently','as observed','I should like it minuted','nodded','sighed','paused','for a while','the way ','somehow','seemed to','appeared to','in the manner of','There was a ','He did not','She did not','It was not','had the look of','the kind of','that kind of','which meant','he said carefully','a long time','a good deal','rather','perfectly','entirely','absolutely','simply','just ','very ']
for p in pats:
    n=len(re.findall(re.escape(p),body,flags=re.I if p[0].islower() else 0))
    print(f'{n:5d} {p}')
# paragraph openers
op=collections.Counter(' '.join(p.split()[:2]) for p in body.split('\n'))
print(op.most_common(25))
# words
w=collections.Counter(re.findall(r"[a-z’']{5,}",body.lower()))
print([ (k,v) for k,v in w.most_common(150) if k not in ('would','there','could','which','their','about','Arthur','should')][:90])
