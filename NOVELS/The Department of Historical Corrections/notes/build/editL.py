import sys
sys.path.insert(0,r'notes\build')
from lib import Doc
def q(s): return s.replace('<<','\u201c').replace('>>','\u201d').replace("'",'\u2019')
class D2(Doc):
    def sub(self,o,n,count=1): Doc.sub(self,q(o),q(n),count)
    def cutp(self,s,n=None): Doc.cutp(self,q(s),None if n is None else q(n).strip())
d=D2('The Department of Historical Corrections - REV12.md')
d.sub("Glock came back at five minutes to four and sat down as if he had not been away.","Glock came back at five minutes to four and sat down without apology.")
d.cutp("Karim read the form to the end","Karim read the form to the end, which Arthur noticed, because nobody had told him to. He signed for the photograph and did not say thank you. He asked to carry the card down to the store himself, and at the door he stood a moment longer than the form required before he handed it over.")
d.cutp("Karim had looked at him a moment longer","Karim looked at him until it was uncomfortable and went home with the photograph. Arthur filed the reply anyway. He had never been able to leave a receipt unsigned, and he knew that this one was for himself.")
d.cutp("<<Yes.>> Beatrice had the custody form out already","<<Yes.>> Beatrice had the custody form out already. <<A photograph to conservation standard goes home with you. The card stays here. It's the rule that stopped Glock choosing what counts, and it doesn't stop applying because the card is yours.>>")
d.cutp("The joke was small and belonged to them.")
d.cutp("Arthur watched her sign the requisition.","Arthur watched her sign the requisition. The laboratory meetings were longer. The equipment was becoming safer in ways which would never make a dramatic demonstration.")
d.cutp("The arrivals met weekly in a room above a community centre.","The arrivals met weekly in a room above a community centre. Miss Ahmed had asked the government observers to stop attending unless invited. The people had spent enough time being an administrative event, and needed to complain about one another without it becoming evidence of integration difficulties.")
print(d.fail)
open('The Department of Historical Corrections - REV12.md','w',encoding='utf8').write(d.t)
