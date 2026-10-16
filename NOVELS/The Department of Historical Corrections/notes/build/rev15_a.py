import re
P='../../The Department of Historical Corrections - REV15.md'
b=open(P,encoding='utf-8').read()
def rep(a,c):
    global b
    assert b.count(a)==1,('cnt',b.count(a),a[:70]); b=b.replace(a,c)
# --- 1. split ch 19
end=b.index('## Lessons')
head,tail=b[:end],b[end:]
head=re.sub(r'^## (\d+) (.+)$',lambda m:'## %d %s'%(int(m.group(1))+(1 if int(m.group(1))>=20 else 0),m.group(2)),head,flags=re.M)
b=head+tail
rep("## 19 The Printer Keeps a Copy","## 19 Written Down")
rep("“It will be when he hears my name.”\n\nThe knock came at eleven at night,","“It will be when he hears my name.”\n\nNed went, at a run, which in his case was a form of respect.\n\nHester swept the glass into the corner of the window frame, wrote CLOSED PENDING on a half-sheet and pinned it where the pane had been. It was the first honest notice the shop had displayed all week.\n\n## 20 The Printer Keeps a Copy\n\nThe most important refusal of the week was made by a man holding a pie.\n\nThe knock came at eleven at night,")
# appendix refs
rep("Chapter 27: “He could not go back","Chapter 28: “He could not go back")
rep("(chapters 9 and 36)","(chapters 9 and 37)")
rep("Chapter 32: the tokens","Chapter 33: the tokens")
rep("Chapter 22: Dr Rao","Chapter 23: Dr Rao")
rep("Chapter 37: a Hall B queue ticket","Chapter 38: a Hall B queue ticket")
# --- 2. ch 21 (Evidence in Person)
rep("The usher, who had a lanyard appeal booked for half past twelve, announced the time at intervals, and nobody thanked him.","The usher, who had a lanyard appeal booked for half past twelve, announced the time at intervals, and nobody thanked him. Rain had started on the high windows. The room smelled of damp coats and of the municipal polish used on every room in which people are made to wait.")
rep("Fanshawe admitted his intervention. Cole asked whether he had sought an independent assessment of Glock’s casualty forecast.\n\n“No.”\n\n“Why not?”\n\n“The forecast was classified.”\n\n“You were director of the department.”\n\n“Yes.”\n\n“Could you have required an assessment?”\n\nFanshawe looked at the table.\n\n“Yes.”","Fanshawe admitted his intervention. Cole asked whether he had sought an independent assessment of Glock’s casualty forecast. He had not; the forecast was classified. Cole observed that he had been director of the department. He agreed that he had.\n\n“Could you have required an assessment?”\n\nFanshawe studied the table, which was veneer over chipboard and had nothing to offer him.\n\n“Yes.”")
rep("Dame Judith made a note. Arthur saw her underline something once.\n\nMiriam entered carrying no papers.","Dame Judith made a note. Arthur saw her underline something once. He found that he was gripping the edge of his chair, and made his hand let go.\n\nMiriam entered carrying no papers. Cole offered her a chair; she stood behind it instead and put both hands on its back.")
rep("Dame Judith asked whether immediate suspension of the future reference sealing was physically possible. Eleanor said yes, if Glock cooperated. Glock said cooperation required recognition of the existing authority. Cole asked whether this meant Arthur’s signature. Glock did not answer directly.","Dame Judith asked whether suspending the future sealing was physically possible. Eleanor said yes, if Glock cooperated. Glock said cooperation required recognition of the existing authority. Cole asked whether he meant Arthur’s signature, and he did not answer directly.")
rep("Pelling’s face had grown pale.\n\nGlock did not lean towards the camera. He waited for the room to finish, as one waits for a train already booked.","Pelling had gone pale and was turning his pen end over end on the blotter, a quarter-turn at a time.\n\nGlock did not lean towards the camera. He waited for the room to finish, as one waits for a train already booked.")
# --- 3. ch 23 (Case for Refusal)
rep("“He can turn off the transmission,” Cole said.\n\n“He can turn off his,” Eleanor replied. “We use the service line Miriam opened. It carries very little. Voice and a time mark.”\n\n“And if he takes that away?”\n\nArthur put the grey notebook on the table.\n\n“Then witnesses carry the record.","Cole asked what happened if Glock cut the transmission. Eleanor said he could cut his own; they would use the service line Miriam had opened, which carried very little, voice and a time mark. And if he took that away?\n\nArthur put the grey notebook on the table.\n\n“Then witnesses carry the record.")
rep("“I’m directed to collect, by nine tomorrow, all material held outside the central extract in connection with this week’s hearing. There’s a van. It leaves Victoria Street at a quarter past eight.” He consulted the clipboard. “I’ve also got Minister Pelling’s instruction, which I can sign, if I choose, before the van goes, and which would make it the Receiver’s delegate’s own order that the evidence is to be kept. I’ve got two instructions and one signature. I thought you should know the time of the van.”","“I’m directed to collect, by nine tomorrow, all material held outside the central extract in connection with this week’s hearing. There’s a van. It leaves Victoria Street at a quarter past eight.” He consulted the clipboard. “I’ve also got Minister Pelling’s instruction, which I can countersign before the van goes, and which would make it the delegate’s own order that the evidence is kept. Two instructions and one signature. I thought you should know the time of the van.”")
rep("Pelling pressed the button and the line went dead. The guard studied the ceiling, which had not been so thoroughly examined since the building was put up.","Pelling pressed the button and the line went dead. The guard studied the ceiling, which had not been so thoroughly examined since the building was put up. Arthur found that he had picked up Garrick’s pen from the plinth and was clicking it, and put it down.")
rep("Fifteen envelopes went out of the building by eleven. Arthur sat watching the registry clock.","Fifteen envelopes went out of the building by eleven. The toaster ticked as it cooled. Arthur sat watching the registry clock.")
open(P,'w',encoding='utf-8',newline='\n').write(b)
print('ok')
