import re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from lib import Doc
SRC='../../The Department of Historical Corrections - REV12.md'
OUT=sys.argv[1]
d=Doc(SRC)

# ---------- A. repetition / junk cuts ----------
d.sub("a captain with the stillness of a man who read everything twice,","a captain who read everything twice,")
d.sub("with the air of a ceremony that happened to be filmed, stopped at ninety-one per cent","with the dignity of a ceremony that happened to be filmed, stopped at ninety-one per cent")
d.sub("put a lozenge in his mouth with the air of a man making a decision, and asked","put a lozenge in his mouth with some deliberation, and asked")
d.sub("in a dressing gown with a candle, like a man who had been robbed of the right to be asleep and meant to send in a bill.","in a dressing gown with a candle, robbed of the right to be asleep and ready to send in a bill.")
d.sub("It had been built, Arthur thought, by a man who had asked himself the same thing on a staircase and not liked the answer.","It had been built, Arthur thought, by someone who had asked himself the same thing on a staircase and not liked the answer.")
d.sub("For the space of a breath Glock looked like a man who had been given exactly what he asked for, and had read the small print.","For the space of a breath Glock had the look of someone given exactly what he asked for who had then read the small print.")
d.sub("with the look of a man who has taken an unauthorised action and cannot find anything in it to recommend it.","wearing the look of someone who has taken an unauthorised action and cannot find anything in it to recommend it.")
d.sub("with the anxious dignity of a man who has made a single decision and would like not to be asked about it.","with the anxious dignity of the newly decisive.")
d.sub("Mr Hallett came last, in a hackney, breathing hard, a man who had been late once in 1802 and never forgotten it, and carrying a small tin of lozenges which he offered to nobody.","Mr Hallett came last, in a hackney, breathing hard; he had been late once, in 1802, and never forgotten it. He carried a small tin of lozenges which he offered to nobody.")
d.sub("delivered the answer with the relief of a man who had not been required to think.","delivered the answer with great relief at not having been required to think.")
d.sub("“Mrs Crumb,” he said, with the air of a man giving up a small pleasure. “Your note","“Mrs Crumb,” he said, in the tone of someone giving up a small pleasure. “Your note")
d.sub("sat on Glock with the practical decisiveness of a man whose working day had become intolerable.","sat on Glock, his working day having become intolerable.")
d.sub("Eleanor did not look up from the map. “Ask one half","Eleanor kept her eyes on the map. “Ask one half")
d.sub("Miriam did not look up from the gauge. “Don’t.","Miriam kept her eyes on the gauge. “Don’t.")
d.sub("Eleanor said nothing. Silence was kinder than anything she could immediately think of.","Eleanor found that silence was kinder than anything she could immediately think of.")
d.sub("Fanshawe blocked it. For a moment the two men stood face to face,","Fanshawe blocked it. The two men stood face to face,")
d.sub("Miriam lowered her head for a moment. Then she closed the freight aperture.","Miriam lowered her head. Then she closed the freight aperture.")
d.sub("For a moment the yard held perfectly still. The servant began","The yard held still. The servant began")
d.sub("standing very still beside Agnes’s lamp.","standing motionless beside Agnes’s lamp.")
d.sub("Beatrice remained very still.","Beatrice did not move.")
d.sub("Glock stood very still. He had spent years","Glock stood still. He had spent years")
d.sub("Arthur stood very still. Hearing virtues","Arthur did not trust himself to move. Hearing virtues")
d.sub("Fanshawe had listened without accepting any, a considerable professional development.","Fanshawe had listened without accepting any.")
d.sub("“Me.”\n\nHe looked at her.\n\n“I have savings","“Me.”\n\nHe waited.\n\n“I have savings")
# second recap of the very good coat (ch 28 repeats ch 25)
t=d.t
a="refused a seat on the receivership by a man in a very good coat"
i1=t.find(a); i2=t.find(a,i1+10)
if i1>0 and i2>0:
    d.t=t[:i2]+"refused a seat on the receivership by the Receiver’s man"+t[i2+len(a):]
else: d.fail.append(('very good coat',(i1,i2)))

# ---------- B. plants ----------
# T3 village/moss: ch 1, 7, 12
d.sub("because the projected improvement erased an unrecorded village.","because the projected improvement erased an unrecorded village and the moss it burned.")
d.sub("Glock had said it was historical boilerplate. Fanshawe had asked for the original.","Glock had said it was historical boilerplate. Fanshawe had asked for the original; he had a prejudice about estates, which he did not explain.")
d.sub("A Tom Tully was paid fourpence in April for carrying peat.","A Tom Tully was paid fourpence in April for carrying peat off the moss, the only fuel the poorer tenants had. Nan had called the place Tullymoss when she spoke of it, in the voice people use for a parish. No account ever did.")
# T2 Beatrice's dot: ch 6, 9, 15
d.sub("“He said there was a correction which could prevent a railway accident.”","“He said there was a correction which could prevent a railway accident. A round that had been allowed to lapse on the eastern lines, in 1988.”")
d.sub("with a proposal to correct a neglected engineering inspection decades earlier. He had not promised resurrection.","with a proposal to correct a neglected engineering inspection decades earlier. He had named the year, 1988, and the round, an inspector’s on the eastern lines. She had not asked to see the volume. He had not promised resurrection.")
d.sub("“I thought they were something to do with the pencil.”","“The oldest of mine is November 2007. I don’t remember what I was looking at. I was not, that month, looking at much. I thought they were something to do with the pencil.”")
# T1 nurse: ch 7, 9, 15
d.sub("At the top was a hospital name.","At the top was a hospital name: Leeds General Infirmary, Ward 4.")
d.after("I brought a nurse through from the adjacent corridor. She saved you.","“I remember her hands,” Arthur said. “They were cold. She kept saying *stay with me, love*, in the voice you use on someone who has other plans.”\n\n“She was a staff nurse on that ward. She never left her own year: she walked out of her own corridor into a minute that was ours, and back again.” Eleanor looked at the whiteboard, which she had not used. “I didn’t ask her name. By the time I thought to, the ward’s staff roll had gone in a trust merger. I looked in 2012. I looked again in 2014.”")
d.sub("Subject, age 7, to be traced and observed. Do not inform.*","Subject, age 7, to be traced and observed. Do not inform. Leeds General Infirmary, Ward 4. Nurse not traced (staff roll lost in trust merger).*")

# ---------- C. ch 22 split + 22b ----------
B22b='''## 22b Reason for Return

They went to the registry to pack the documents. Arthur followed with Hester’s account. He described the printer carefully: the way she asked for payment before accepting explanations, the damage to Daniel’s hand, her distrust of unsolicited rescue. Beatrice listened with the attention of someone learning the terms of an important appointment.

“Don’t promise to rebuild her shop,” Arthur said. “We need to make actual arrangements, not leave her with gratitude.”

“I’ve included specie and a written authorisation for compensation.”

“From whom?”

“Me.”

He waited.

“I have savings, Mr Pembroke. It has been an uneventful nineteen years in some respects.”

He did not argue. She was paying for a broken press; absolution did not come into it.

At half past ten that night Miriam went down to Records and found Beatrice at the long table with the 2008 register open in front of her. It was open at the same page it had been open at since six. A second volume lay beside it, older, bound in green cloth, with a ribbon marking something.

“You should be eating.”

“So should you.” Beatrice closed the 2008 book on her finger. “I was reading the receipt. It has a box for *reason for return*, and I wrote *personal*. I have been looking at that word for nineteen years.”

Miriam took the chair opposite. She had been two women in two histories, and still did not know which of her was being addressed when her mother looked at her like that.

The receipt was Glock’s, in his small upright hand, for the pages he had taken; the box for the reason was in hers. *Access to the Strath papers, exclusive. Matter: restoration of the Schedule 14 round, Eastern Region permanent way, 1988. Reason for return: personal.*

“I have been doing my dots,” Beatrice said. “A name or nothing, Arthur said, so I have been giving each of them a name. I started with the newest, because it was easiest, and worked backwards. I reached the oldest at half past nine.” She laid a finger on the green volume. “Then I looked across at the receipt, and the receipt said Schedule 14. So does the line.

“I never asked what Schedule 14 was,” she said. “I had read the report. It said a round had lapsed in 1988 and the points under your train had come apart in 2007, and he offered to put the round back. I didn’t ask whose it had been. I think I was afraid it would be somebody’s fault.” She opened the green volume at the ribbon. “This is the oldest of my dots.”

It sat in the margin against line 291. Under it, in the same pencil, very small, was *Nov 07*.

“Two weeks after your funeral, and a year before the report. I was down here because I couldn’t be anywhere else. I read a line, I made a mark and I went home. I thought it was something to do with the pencil.” She turned the book round. “I have just read the line properly. I don’t think I ever did.”

*291. Transfer Schedule 14: Eastern Region, permanent-way inspectors. Forty listed; forty in the covering note. Retained as drafted. B.C. 14 March 1988.* Below it, in the consequence note, typed by a ribbon that had been tired, a little crooked: *Not carried over: CORLEY, A. (Alan), inspector.*

Miriam read it twice. “That’s your hand.”

“I was twenty-five. The schedule agreed with its covering note, so I retained it. Nobody had told me to count the people the note didn’t mention.” Beatrice took off her spectacles. “I have been very careful ever since.”

Miriam did the arithmetic first, because someone had to. “I was born that September.”

“Six months after. I have never once put the two years side by side.”

“And Glock knew.”

“He had the registers. He gave me the year and the round and let me not look.” She almost smiled. “I have been trying all afternoon to find the place where he lied. There isn’t one. He lets people sign.”

“I am not going to tell you it’s all right.”

“I would think less of you.”

“I’m not going to tell you it isn’t, either. I haven’t worked out the proportions.”

“Then put Mr Corley back,” Miriam said. “Correct it.”

“Nineteen eighty-eight is closed. It was witnessed and it was ratified, and a ratified register can be reopened only by a Receiver’s override. That is the lever Glock built, and the one we are going to break in the morning. That is what he sold me, Miriam. A door only he had the key to, into a room I had locked myself.”

“Is he alive?”

“He retired from a signal box in Selby in 2011, if the pension office is right. He was never dead. He was not on the list, and a round that nobody is told to walk doesn’t get walked.”

“Does he know?”

“That he was left out? He wrote to the region twice, in 1989. A clerk told him it had been regularised.” Beatrice put her spectacles back on. “That was a clerk like me.”

“Will you write to him?”

“As a letter or as a correction?”

“Which is the difference?”

“I am told a letter can be declined.”

Miriam looked at the receipt again. “Reason for return. Personal.”

“Yes.”

“It was true twice.”

“Eleanor ruled a column on Monday,” Beatrice said. “I have been through my fifty-three since. Fifty-two I can explain. Strangers, mostly, and a canal. I did not need to be told which one I couldn’t.”

“*Retained as drafted*,” Miriam said. “I have read the constitution of a government that hasn’t happened yet, and that is the most frightening phrase in it.”

“It is a very ordinary phrase. That is what is frightening about it.”

Beatrice did not answer. Neither of them reached for the tea, which had been made for somebody else and gone cold.

“What was it like?” Miriam said at last. “The first morning.”

“Do you want the true answer or the one that sounds well?”

“Both. In order.”

“I held you,” Beatrice said. “And I kept waiting for you to be someone. I had a nineteen-year-old in my arms and I kept waiting to be told she was you.” She looked at the register. “I kept your cardigan. I never let you wear it. I didn’t say.”

“I thought it didn’t suit me.”

“It didn’t. It was never the point.”

Miriam laughed, once, with her whole face. Then she stopped and said, “I’m going to 2029 in a few hours. I’m going to find people I have only ever seen from the corridor. I’m going to ask them to trust a woman they last saw leaving.”

“You’ll do it well.”

“I’ll do it carefully. It isn’t the same.” She took the pen from the table and wrote, in the margin beside the box in her own hand, *Corrected, 16 Sept. Not only personal.* “There. Now it is in two hands.”

Beatrice looked at it for a long while. She did not say anything, which was one of the things she had learnt that week.'''
d.cutrange("They went to the registry to pack the documents.","Before departure, Miriam and Beatrice stood together",B22b)

# ---------- D. ch 31 village ----------
V='''He opened one eye again a minute later. “You’ll want something for the other column,” he said. “I counted mine in the cell, there being nothing else to read. Several approvals I would take back. One refusal I wouldn’t.”

“The drain,” said Eleanor, from the console. She had not turned round.

“I never told you the name.”

“You never told anyone, and nobody could find it, because it was never entered under what its people called it.” She brought a printout across and set it on the crate beside him. “The Strath accounts for 1747 say Strath Moss. Nan Tully called it Tullymoss. The accounts took her word for it once, in April, in a line about peat: fourpence, to a Tom Tully, for carrying it.” She did not look at Arthur. “The correction you stopped would have drained the moss for a profit that was real and small. The peat would have gone, and the nine cottages that burned it. They would never have been listed anywhere. The rent roll for 1761 lists a Thomas Tully, tenant, aged twenty. I don’t know what I did for him in that kitchen. Probably nothing. I know where the roll still has him.”

Fanshawe looked at the printout for a long time. “That is why I asked for the original, when Glock said boilerplate. He said *trust*, and *estate*, and I thought of a place that couldn’t prove it was there. On my last—” He stopped. “It wasn’t a mission. It was a memo, and I was cross.”

Arthur did not forgive him. 1815 was a larger account and it was not his to close. He took out the grey notebook and wrote *Tullymoss. Not drained. H. Fanshawe.* in the column beside the Venetian tariff, which was the first entry he had ever made against Fanshawe’s name that was not a debt.'''
d.after("“Thirty-nine, then,” said Fanshawe, and shut his eyes.",V)

# ---------- E. ch 34 / 34b ----------
d.sub("failing to disclose her personal interest.","failing to disclose her personal interest, which turned out to include her own initials on a line of the 1988 register.")
d.after("failing to disclose her personal interest, which turned out","“And line two hundred and ninety-one?” the chair asked. The page had been exhibited the day before.\n\n“Mine. I retained a schedule that dropped an inspector because it agreed with its covering note. I was twenty-five. I am not offering that in mitigation. It is the particular.”\n\n“Has Mr Corley been informed?”\n\n“I have written to him, as a letter and not a correction. He hasn’t replied. I think that is his right.”")
d.cutrange("Before the final session, the later Glock asked to see Arthur.","The department’s new charter was shorter",None)
B34b='''## 34b Visiting Hours

The later Glock’s letter reached Arthur in the week the finding was published. It asked for fifteen minutes, on lined paper, in the small upright hand Arthur now knew better than his own. Remand visiting hours were Tuesdays and Thursdays, two to four, and Glock had used none of them.

Cole advised that there was no obligation to attend. Arthur went, with the solicitor present and the conversation recorded. He no longer confused listening to a man with granting him control of the room.

The visitors’ room had a vending machine, which offered tea in three varieties of the same tea. Arthur did not press anything. It had been that kind of year.

Glock sat behind a plain table. Without the excellent coat, the private office and the people waiting for his instructions, he looked like an intelligent civil servant who had slept badly. Arthur found this more disturbing than if prison had transformed him into a visibly different kind of person. He did not offer tea. There was none to offer.

“You have won the immediate argument,” Glock said.

“I didn’t come for a concession.”

“No. You came to hear whether I regret it.”

Arthur sat. “I came because you asked. You can decide what you wanted to say.”

Glock looked towards the recorder. “You are making a virtue of machinery again.”

“It helps us remember what was actually said.”

“People will remember what suits them.”

“Some will. That doesn’t require us to help.”

For a while Glock said nothing. Then he said, “Leeds. The third floor,” and Arthur, who had never been to Leeds and had once signed a sentence about it, saw the porridge of paper and the queue outside, and the people asked to produce what the office had drowned.

“I passed the retention,” Arthur said. “I didn’t go.”

“No. The form did not require it.”

“I should like that on the recorder.”

“It is on the recorder.” Glock turned one hand over on the table. “That is what I mean by a record, Mr Pembroke. But I did not mean the records office. I meant the ward.”

Arthur waited.

“You have never asked why you. Everyone else has. You assumed it was the induction, and I let the committee assume it.”

“It was the induction.”

“That made you usable. It was not how I knew your name.” Glock looked at his hand rather than at Arthur. “My mother was a staff nurse on the third floor of Leeds General Infirmary, Ward 4. In October 1991 a woman with a watch on each wrist walked into a treatment room that was supposed to be empty and took her by the sleeve. The doctors had stopped. The woman had not. My mother put her hands on a boy and told him to stay, and he stayed. She told me that story every Christmas until I was thirty, and I believed about half of it. She had written the boy’s name on the back of her hand in biro, because the band had come off in the struggle and she wanted it kept.”

Arthur found that he could no longer see the table.

“In the tenth month, when the book still had not come, she read the name at the foot of the fourth reply and said she had once held a boy of that name. She was in a great deal of pain and had been confused for a week. I looked it up anyway. I look everything up.” Glock turned the hand back over. “Entry one of your file, which Mrs Crumb keeps in a cabinet and believes nobody has read: *Leeds General Infirmary, Ward 4. Nurse not traced.* The entry was initialled EV. The only EV in the building was too young to have been anywhere in 1991, and wore a watch on each wrist. I did not ask her. I traced my mother instead. She was in my kitchen.”

“That’s—” Arthur said, and found the word was not available.

“It isn’t coincidence. Your name was on the band, in her mouth for twenty-seven years and at the foot of the reply. It wanted only one person to read all three, and I read for a living.”

“She saved my life.”

“Yes.”

“And I cost her the last ten months of hers.”

“Ten. The book came in the eleventh.” Glock said it without weight, and Arthur understood that this was not cruelty but accuracy, which was worse. “I am not telling you so that you will be sorry. You will be, and it will be of no use to me. I told you the reason was on the first page. I did not tell you the first page had a nurse in it. You would have been moved, and I needed you signing.”

Cole had stopped writing. He moved his pen to the far side of the notebook, the way one moves a glass out of someone else’s reach.



“She would have told you to forgive me.”

“Very probably. I find I am not my mother’s son in that respect.”

“I should like it on the recorder,” Arthur said, “that in 1991 she kept me alive, and that in 2017 I passed a form that took the end of her life. I should like both.”

“Both are on it.” Glock leaned forward. “I wanted a record that could not be lost. Not a king. A register that nobody could drown.”

Arthur listened. The account was plausible. It did not explain everything, and was not entitled to.

“That was worth wanting.”

Glock leaned back. “You see.”

“I see the beginning.”

That irritated him. “Every copy introduces disagreement. Every independent custodian introduces a different standard. At some point someone must decide.”

“Yes. And someone must be able to question the decision.”

“Forever?”

“When there is evidence.”

“You underestimate the damage people can do with evidence.”

Arthur thought of the selective forecast, the orange bands and the woman in the registration centre whose photograph the system would not scan.

“You’re well placed to explain it.”

Glock looked away. It was not remorse. It might have been anger at finding that the same words could now apply to him.

“Your new office will make mistakes,” he said.

“Yes.”

“People will suffer because you permit uncertainty.”

“People suffered because you prohibited it.”

“You cannot balance a country on an endless appeal.”

As Arthur stood to leave, Glock asked about Ruth.

Cole began to object. Arthur shook his head.

“Her record is being kept,” he said.

“That is very little comfort.”

“I know.”

“You could have kept her alive.”

“By accepting terms which made other families depend on your discretion. You don’t get to turn her into your closing argument. You don’t get to turn your mother into one either.”

Glock said nothing. It was the only time in the conversation that he had not already prepared his answer.

In the corridor Arthur had to stand still for a while while his hands stopped shaking. Cole waited beside him without asking whether the meeting had helped. Then Arthur took out the grey notebook and wrote, because that was what the book was for, *Margaret Glock, staff nurse, Leeds General Infirmary, Ward 4, October 1991. Kept me alive.* He left the line under it empty.

The custody officer asked at the gate whether he had got what he came for.

“No,” Arthur said. “I got what he had been keeping.”

Eleanor was waiting in the car park. She had been told, correctly, that she should not attend, and had come anyway to be somewhere near it. He told her in the order Glock had told him. She listened without interrupting, which she did only when it mattered, and at the end she looked at her wrists.

“I would have said the machine leaves no forwarding address,” she said.

“It doesn’t. A woman does.”

She unbuckled the left watch, looked at it for a moment, and put it in her coat pocket. “I’ll find it a drawer,” she said.'''
d.before("## 35 People with Addresses",B34b)

# ---------- F. ch 37 ----------
d.sub("The first read: *Margaret Glock, Leeds. Eleven months. Retained by A. Pembroke, 12 October 2017. Entered.*","The first read: *Margaret Glock, staff nurse, Leeds General Infirmary, 1991. Eleven months. Retained by A. Pembroke, 12 October 2017. Entered.*")
d.after("Arthur had done his own fifteen at a single sitting","Beatrice made her entries on Thursdays, in pencil first and then in ink, which she described as progress. The first was *Alan Corley, permanent-way inspector, 1988. Left out by B. Crumb, 14 March 1988. Entered.* She had found an address for him in Selby and written a letter, which she posted rather than filed. He had not replied. She had pinned a card to the registry noticeboard saying so, with the date, so that his silence would at least be on the record.")
d.sub("Beside it, the old pencilled registers","Beside it, the old pencilled registers") if False else None

# ---------- G. appendix ----------
d.sub("Chapter 26: “He could not go back and not sign.","Chapter 27: “He could not go back and not sign.")
d.sub("Chapter 35: a Hall B queue ticket","Chapter 37: a Hall B queue ticket")
d.sub("Chapter 31: the tokens “could signal readiness","Chapter 32: the tokens “could signal readiness")
d.sub("the book chooses not to.","the book chooses not to. The later twists keep to it: the chain from a rescue in 1991 to a signature in 2017 to a grudge in 2018 (chapters 9 and 36) runs one way, through records, and nobody in it causes themselves.")

# ---------- H. renumber headings ----------
lines=d.t.split('\n'); n=0
for i,l in enumerate(lines):
    if l.startswith('## Lessons'): break
    m=re.match(r'## (\d+)(b?) (.*)',l)
    if m:
        n+=1; lines[i]=f'## {n} {m.group(3)}'
d.t=re.sub(r'\n{3,}','\n\n','\n'.join(lines))
open(OUT,'w',encoding='utf-8',newline='\n').write(d.t)
print('fails:',d.fail); print('chapters',n)

