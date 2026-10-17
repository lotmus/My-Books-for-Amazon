P='../../The Department of Historical Corrections - REV15.md'
b=open(P,encoding='utf-8').read()
def rep(a,c):
    global b
    assert b.count(a)==1,(b.count(a),a[:70]); b=b.replace(a,c)
rep("Garrick, who had been writing, looked up. “May I say that I never heard that.”\n\n“Say what you like.”\n\n“I shall say I took a note of everything, and collected nothing, because there was nothing in the building to collect.” His hand trembled on the clipboard. “It’s a deviation,” he said. “I’ve had two this week. They’re getting easier.”","Garrick, who had been writing, said he would report that he had taken a note of everything and collected nothing, there being nothing in the building to collect. His hand trembled on the clipboard. “It’s a deviation,” he said. “I’ve had two this week. They’re getting easier.”")
rep("“We can’t send the same person everywhere,” Pelling said.\n\n“Thank you,” Eleanor replied. “That is a surprisingly persistent misconception.”","Pelling remarked that they could not send the same person everywhere. Eleanor thanked him; it was a surprisingly persistent misconception.")
rep("Arthur looked at her.\n\n","Arthur looked at her.\n\n") if False else None
open(P,'w',encoding='utf-8',newline='\n').write(b)
