import sys, re
sys.path.insert(0,r'notes\build')
from lib import Doc
def q(s):
    return s.replace('<<','\u201c').replace('>>','\u201d').replace("'",'\u2019').replace('{em}','\u2014')
class D2(Doc):
    def sub(self,o,n,count=1): Doc.sub(self,q(o),q(n),count)
    def after(self,a,n): Doc.after(self,q(a),q(n))
    def before(self,a,n): Doc.before(self,q(a),q(n))
    def cutp(self,s,n=None): Doc.cutp(self,q(s),None if n is None else q(n).strip())
    def cutrange(self,a,b,n=None): Doc.cutrange(self,q(a),q(b),None if n is None else q(n).strip())
d=D2('The Department of Historical Corrections - REV11.md')

# ---------- CH 13
d.cutrange("Miriam logged the return in the register","Beatrice took the protected case to Records",
"""Miriam logged the return in the register, which now took two figures from each traveller: the department's clock and the traveller's own. She unbuckled Eleanor's left watch, then the right, and wrote both down.

<<Eleven twelve, and seventeen forty-one. Three hours thirty-one of yours against three thirty-two of ours.>> She looked up. <<Is that dilation?>>

<<That's me and a laundry.>> Eleanor shook the watch as if it might confess. <<A minute by speed alone would want a tenth of the speed of light. I was standing still. I set it by eye and I stopped once for a fever.>>

Miriam ruled a second column anyway, with the Operations ruler, in ink. <<The field counts how much of you has happened,>> Eleanor said. <<It's the one thing it can't be lied to about.>>

Beatrice put her head round the door with a form from Pensions about the man in the side room. Was he a member of staff, and if so how old?

<<Three years older than Mr Pembroke,>> she said. <<They say that isn't an age.>>

<<It's the only kind there is,>> said Eleanor.
""")
d.cutrange("Beatrice took the protected case to Records","The omitted sentences said that",
"""Beatrice took the protected case to Records to compare Agnes's certified copy with the suppressed catalogue description. Arthur followed her and began to ask whether the omissions were accidental, and stopped when she looked at him.
""")
d.cutrange("Eleanor spent the afternoon with the original memorandum","At four, Pelling sent a message.",
"""Eleanor spent the afternoon with the original memorandum, the substituted annex and the consequences. The repair could not restore every detail Arthur remembered. Their own witnessed actions, Hester's resistance and the arrival of Miriam and the dead Arthur had all acquired protected evidence. What remained was the fraudulent legal branch, where one open interval still permitted a correction: the duplicate dispatch, provided nobody had copied it outside Glock's control first, and provided it was countersigned. A proof documents what was proposed. It does not certify what was adopted.

Arthur wrote it down. He had learned to distrust rules which appeared only when they became useful. This one was already in the two receipts.
""")
d.cutrange("<<He needs the refusal,>> Arthur said.","The door opened without a knock.",
"""<<He needs the refusal,>> Arthur said. <<While every dispute stays visible, no single witness can settle the country. We want an inquiry where more than one office keeps the evidence and he doesn't choose the witnesses.>>

Beatrice put a copy of the access receipt on the desk, with her signed admission. <<Including this.>>

Pelling read it. His face changed. He did not offer her comfort, which Arthur appreciated on her behalf.

<<Tomorrow morning at nine,>> he said. <<An emergency evidential hearing. I can't promise the result.>>

<<That would spoil the point,>> Arthur said.
""")

# ---------- CH 35
d.cutrange("<<So you're still looking,>> Karim said.","Karim took the report date",
"""<<So you're still looking,>> Karim said. <<Not just keeping the paper.>>

Arthur told him the search had a named person responsible and a date for the next report, and that keeping the paper was how Karim could check whether they did it.
""")
d.cutrange("They went for coffee after work.","She laughed. They spoke about ordinary things",
"""They went for coffee after work. No one was missing, the machine was shut down and neither carried a protected token. Arthur found the absence of contingency planning almost indecent. Eleanor asked what he did when the past behaved itself, and he said he had become suspicious of endings. She told him to try gardening. He said that seemed to involve deadlines too.

He said that seemed to involve deadlines too.""")
d.cutp("<<There isn't. Nobody opened one.>>",
"""<<There isn't. Nobody opened one.>> Eleanor put the magnifier down. <<Dr Rao would call this tunnelling. A wall thick enough to be called closed is still not perfectly closed. The chance falls off very fast with the thickness and never quite reaches nothing. For this wall I wouldn't print the number.>> She looked at the ticket. <<It got through.>>""")
d.cutp("<<No.>> She said it before he had finished.",
"""<<No.>> She said it before he had finished. <<I can't aim it, I can't repeat it and I can't ask it for another. A thing that gets through once by luck isn't a method, and if I build a method I'll have built what Glock built, with better stationery.>>""")
d.cutrange("Karim asked whether he could keep it.","On Sunday he visited his mother.",
"""Karim asked whether he could keep it.

<<Not yet,>> Eleanor said. <<It's the only thing in the building that arrived without a door. It goes into the evidence store with Glock's wiring until the inquiry has closed on it, and I can't tell you when that will be.>>

<<She wrote it to me.>>

<<Yes.>> Beatrice had the custody form out already, and did not make him wait for it. <<A photograph to conservation standard goes home with you. The card stays here. It's the rule that stopped Glock choosing what counts, and it doesn't stop applying because the card is yours.>>

Karim read the form to the end, which Arthur noticed, because nobody had told him to. He signed for the photograph. He did not say thank you. He asked to carry the card down to the store himself, and Beatrice let him, and at the door of the store he stood for a moment longer than the form required before he handed it over.

That evening Arthur wrote a reply, in capitals, in the clerk's way, and signed it with the short flat line. It was addressed to Hall B. Nothing in the building could carry it, and he had told Karim so before he began.

<<Then what's it for?>> Karim had asked.

<<So the file shows that somebody answered.>>

<<That isn't the same as sending it.>>

<<No,>> Arthur said. <<It isn't.>>

Karim had looked at him a moment longer than was comfortable and gone home with the photograph. Arthur filed the reply anyway. He had never been able to leave a receipt unsigned, and he knew that this one was for himself.
""")

# ---------- CH 26
d.cutp("<<There is a fifteenth,>> he added.",
"""The secretary put her head round the door. <<The judges are seated, Receiver.>>

Glock looked at the clock above the shelves, which said eight minutes to four. <<Drink your tea, Mr Pembroke,>> he said, and went out, leaving the door ajar and the book on the desk, which Arthur understood to be the point.

He did not drink the tea. He turned back through the fourteen with the pencil from the grey notebook and added the months in the margins, and stopped at the total, because it was not a number he could write down. He copied *17/114* onto a clean line instead, with the date. His handwriting looked smaller than Glock's. The MAROT file sat on the shelf, thick and old, and he left it alone. It was the one thing in the room he had not been asked to read.

Glock came back at five minutes to four and sat down as if he had not been away.

<<There is a fifteenth,>> he said. <<It isn't in the book. I did not keep it. I used it.>>""")
d.before("Arthur entered the ceremonial room without his coat.","* * *")
d.cutp("<<I do not consent to this office.",
"""<<I do not consent to this office. I do not appoint Mr Glock to determine admissible history on my behalf. I do not waive any person's right to keep or present contradictory evidence. I have signed findings in this department whose consequences I did not follow. Fourteen are in Mr Glock's notebook. A fifteenth is not, because he used it: the assessment stamped on the casualty tables on which Director Fanshawe acted. I did not ask what the first thirty-nine pages said. Let it be recorded that all fifteen are mine. A record that holds my signature has to be one I can be asked about in public. No previous signature of mine is consent to powers concealed from me.>>""")

# ---------- CH 12
d.sub("""<<I know you.>>

<<I have one of those faces.>>

<<From London.>>

<<There are a great many people there.>>""","""<<I know you.>>

<<I have one of those faces.>>""")
d.sub("""<<Your colleague,>> she said, meaning Saye, who was being carried between two of the household men and looking at nothing, <<claims to work for a government that has not happened.>>

<<He does.>>

<<And you oppose him.>>

<<Yes.>>

<<Then perhaps it needn't.>>""","""<<Your colleague,>> she said, meaning Saye, who was being carried between two of the household men and looking at nothing, <<claims to work for a government that has not happened. And you oppose him. Then perhaps it needn't.>>""")
d.sub("""<<Independent of whom?>>

<<You are in no position to be clever.>>

""","")
# ---------- CH 15
d.sub("""<<And if Glock had never touched Belgium?>>

<<You'd have retired in 2051 with a clock, never knowing. And I'd have thought that was a good outcome.>>

""","")
d.sub("I was in the archive. Jon brought me tea. You came down every night","You came down every night")
d.sub("""<<I don't think that's an achievement.>>

<<It's the first thing he should have done,>> said Miriam,""","""<<It's the first thing he should have done,>> said Miriam,""")

# ---------- APPENDIX
d.sub("and three exercises to try, graded Core, Extension and Challenge, each with a full solution and the usual mistake.","one diagram, and three exercises to try, graded Core, Extension and Challenge, each with a full solution and the usual mistake.")
def fig(n,alt,cap): return f"![{alt}](notes/figures/{n})\n\n*{cap}*"
d.after("GPS satellites carry clocks that are corrected",fig("fig1_two_clocks.png",
 "Diagram of two clocks over one journey. A vertical line shows the stay-at-home clock counting 10 years. A red line goes out to 3 light-years and back over 10 home years; the traveller at 0.6 times the speed of light counts 8 years. A dotted line marks the path of light.",
 "Figure 1. Two clocks, one journey. The home clock counts 10 years. The traveller, going out and back at 0.6c, counts 8 (10 \u00d7 0.8). The dotted line is light."))
d.after("Two histories are allowed (3 and 8)",fig("fig2_consistent_loop.png",
 "Diagram with the digits 0 to 9 on top and 0 to 9 below. Grey arrows map each digit N to the last digit of 3N plus 4. Thick blue vertical arrows show that only 3 and 8 map to themselves.",
 "Figure 2. The toy loop. Each digit that arrives sends back the last digit of 3N + 4. Only 3 and 8 map to themselves, so only those letters can exist."))
d.after("A related but separate fact",fig("fig3_looking_at_electron.png",
 "Two sketches of light meeting an electron. Top: short-wavelength light gives a sharp position and a hard kick, drawn as a long arrow. Bottom: long-wavelength light gives a small kick but a blurred position, drawn as a large grey cloud.",
 "Figure 3. Looking at an electron. Light short enough to fix its position gives a hard kick. Light gentle enough for a small kick gives a blurred picture. (Not to scale.)"))
d.after("So entanglement carries no message.",fig("fig4_correlated_tokens.png",
 "Top: a source S sends one member of a pair to Alice and one to Bob; each list on its own is a coin toss and no message passes between them. Bottom: a curve of the share of opposite results against the angle between the axes, falling from 1 at 0 degrees to 0.75 at 60 degrees, 0.5 at 90 degrees and 0 at 180 degrees.",
 "Figure 4. A pair made together. Each list alone is a coin toss. Only when the lists are compared does the share of opposite results follow cos\u00b2(\u03b8/2), where \u03b8 is the angle between the axes."))
d.after("(This is the thick-barrier estimate",fig("fig5_tunnelling.png",
 "A wave arrives from the left and meets a grey barrier. Inside the barrier the wave dies away steeply in red. On the far side a small wave continues, showing a small chance of finding the particle there.",
 "Figure 5. A wave meeting a barrier it cannot climb. It dies away steeply inside but not to zero, so a small wave appears beyond. (Calculated for a rectangular barrier; heights not to scale.)"))
d.sub("Experiments, including Alain Aspect's in 1982 and several loophole-closing ones in 2015, found values above 2.","Experiments, including Alain Aspect's in 1982 (in an equivalent form of the test) and the loophole-closing ones of 2015, violated that bound. The Delft experiment of 2015 found 2.42, give or take 0.20.")
d.sub("These are the standard references behind the lessons. Check them before relying on any figure.","These are the standard references behind the lessons. Each was checked against the publisher's or the Nobel Foundation's own page in October 2026. Titles that contain a person's name are left out.")
d.sub("Living Reviews in Relativity 6 (2003).","Living Reviews in Relativity 6, article 1 (2003).")
d.sub("Physical Review Letters 23 (1969); Aspect, A., Dalibard, J. and Roger, G., Physical Review Letters 49 (1982); Hensen, B. et al., Nature 526 (2015).","Physical Review Letters 23, 880 (1969); Aspect, A., Dalibard, J. and Roger, G., Physical Review Letters 49, 1804 (1982); Hensen, B. et al., Nature 526, 682 (2015). Nobel Prize in Physics 2022: Aspect, Clauser and Zeilinger.")
d.sub("Zeitschrift f\u00fcr Physik 51 (1928); Binnig, G. and Rohrer, H., the scanning tunnelling microscope, Nobel Prize in Physics 1986.","Zeitschrift f\u00fcr Physik 51, 204 (1928); Binnig, G. and Rohrer, H., the scanning tunnelling microscope, Nobel Prize in Physics 1986 (shared with Ernst Ruska).")
print('FAIL',d.fail)
t=d.t.replace('@@KEEP@@','')
open('The Department of Historical Corrections - REV12.md','w',encoding='utf8').write(t)

