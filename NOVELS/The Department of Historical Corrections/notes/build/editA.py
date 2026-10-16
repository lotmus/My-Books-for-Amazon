from lib import Doc
import re
d=Doc('/workspace/histcorr/hc.md')

# ---- title & decoration
d.sub('## 1 The Tuesday That Happened Twice','## 1 A Monday, As Observed')
d.sub('Britain appeared to possess Hawaii. Argentina had become New Wessex, though a marginal note suggested this might be an error in the department’s gazetteer. The Beatles had six members. ','')

# ---- Ch2: clock lag and the load rule, portable frames
d.sub('You enter at nine forty, local time, on June the twenty-second.','You leave us at nine thirty-one and enter at nine forty, local time, on June the twenty-second. The machine always puts nine minutes into the passage. It’s why nobody sees you go.')
d.after('Don’t build a plan around an adverb.','''“Two other things, so that nobody can say I didn’t tell you. Every opening draws on a store of coils, and the store doesn’t count people. It counts kilograms. A window carries two hundred kilograms of protected load, which is you, your coat and whatever you’re holding. It isn’t a rule about how many of you there are. It’s arithmetic about how much of you there is.”

“And the other thing?”

“Portable frames. Bell’s resilience pilot bought three in 2019. One passenger, a hundred-kilo ceiling, a battery in a box, and a key cut to the user’s induction, which means each one will carry the person it was cut for and nobody else. Fanshawe signed the purchase. He thought they were for fire drills.”

“Where are they now?”

“Bell holds the keys. We hold the invoice.”

She gave him the invoice. It was stamped PAID, which in Arthur’s experience was the most alarming word in the language.''')

# ---- Ch6: Reed
d.after('It doesn’t make us independent of the Crown.','''The older of the two escorts, a captain with the stillness of a man who read everything twice, was looking at the warrant in Mrs Crumb’s hand rather than at Bell.

“Captain Reed, Registration Guard. May I have a receipt for this visit, ma’am?”

“You may not,” Bell said.

“For my own file, sir. I like to keep things in two places.”

Mrs Crumb wrote it out and gave it to him. Reed read the date, the time and the line that said no dispatch authorised pending review, then put it in his breast pocket, where Bell could not reach it without a scene.''')

# ---- Ch7: the ratification rule
d.sub('That interval is closed. But the duplicate dispatch tomorrow could carry the original terms. The recommendation isn’t finally settled until the copies agree.”','''That interval is closed, and what I did in it stays done. But a recommendation is not a ruling. The committee ratifies on the twenty-third, at half past ten, when two sealed copies held by separate recipients are found to agree and the clerk enters it in his register. Until then my substitution is a fact and its implementation is a proposal. The machine doesn’t care about law, Pembroke. It cares that the copies were observed to agree.”''')

# ---- Ch9: ledger and clock
d.sub('Eleanor looked at the time. The reconciliation clock had fifty-eight hours left. Outside, Monday evening was settling over an unfamiliar country.','''Eleanor turned the whiteboard over and ruled it into columns: PRESENT, DESTINATION, WHO, KILOGRAMS, RETURN, OUTCOME.

“In ink,” she said. “Nobody rubs anything out. From now on a dispatch is a line, not a feeling.”

Mrs Crumb copied the first rows in her registry hand. It took a quarter of an hour, and the rows were stranger written down than they had been in anyone’s head.

Line one. Fanshawe. Present, Sunday 13 September, 14:05. Destination, 21 June 1815, a desk interval in a committee room, about ten past four. Ninety-one kilograms with kit. Return missed. Outcome: chained to a ring aboard the Mercy.

Line two. Incoming packet. Present, Monday 06:12. Origin, 17 November 2029. Seventy-four kilograms, a body and a photographic packet. Outcome: detected late, because the department’s survey instruments need three hours to describe a change they have already suffered.

Line three. Arthur. Present, Monday 09:31. Destination, 22 June 1815, 09:40. Eighty-six kilograms with coat. Return booked for 10:27 at Pike’s stove, missed. Recovered Monday 15:42 from a cupboard behind an apothecary’s, mid-afternoon, their time.

Line four. Miriam. Present, Monday 09:31 to 09:34, at her own insistence and in her own unobserved gap. Fifty-eight kilograms. She had taken the return reserve to do it, and Eleanor had put the reserve back with forty seconds to spare.

Beatrice wrote the next number and, at the head of the column beside it, in capitals, NO LINE WITHOUT A WEIGHT.

Eleanor looked at the time. It was ten past five. The reconciliation clock had sixty-four hours left, and Bell had said he would be back at six.''')

# ---- Ch10: Bell's flood, two travellers
d.after('By allowing a system to function.','''“I once stood in a records office in Leeds nine days after a flood,” Bell said. “Birth certificates, deeds, compensation files, a century of paper reduced to porridge. People with a cousin at the council had replacements by Friday. Everyone else was asked to produce the documents the office had just drowned. I decided then that a record ought not to be a thing that could be lost.”

It was probably the one true thing he had said all day, and Arthur resented it for that.''')
d.sub('A better return window after dusk. Two travellers.','A better return window after dusk. Two travellers and a bag out, and the window is two hundred kilograms coming back as well.')

# ---- Ch12: Cresswell's token
d.sub('He went through the gate before anyone moved to stop him.','He went through the gate before anyone moved to stop him. Nobody saw him sweep the spare brass slip out of Saye’s case on the way. It was keyed to the hold of the Mercy, ten past nine on the evening of the twenty-second of June, and Cresswell had never in his life been so glad of a procedure.')

# ---- Ch13: return mass; Garrick
d.sub('The return aperture was meant to admit two people. Eleanor sent Arthur first, then Saye, and remained in the laundry while the mass balance reset. For eleven seconds Arthur could see her on the other side, standing very still beside Agnes’s lamp. The light narrowed. He reached towards it.','''The return window was booked for two hundred kilograms. Eleanor had meant it for two people and a bag, and it would carry three people and no bag, but only if the three were Arthur, Saye and herself and she was willing to stand in a cold laundry stripping her kit onto the floor. She sent Arthur first, then Saye, and stayed to unload. The reference reader, the medical kit and her second coat went onto Agnes’s drying rack. Arthur would have called that an anachronism if he had had the breath. For eleven seconds he could see her on the other side, standing very still beside Agnes’s lamp. The light narrowed. He reached towards it.''')
d.sub('She landed awkwardly and caught the console. Miriam shut the circuit with both hands.','She landed awkwardly and caught the console. Miriam shut the circuit with both hands and read the gauge aloud.\n\n“One ninety-eight.”\n\n“Two to spare,” Eleanor said. She was looking at her empty hands. “I left the reader.”\n\n“In 1746?”\n\n“On a drying rack.” She sat down on the nearest crate. “It doesn’t open without the key. I’m told that’s a comfort.”')
d.cutp('Arthur watched Bell’s mechanism encounter an ordinary person willing to be inconvenient.')
d.after('“That would spoil the point,” Arthur said.','''The door opened without a knock. A man in a lanyard the colour of a mild warning stood in it, holding a clipboard as though he had been taught to apologise with it.

“Minister. I’m told there’s been a deviation.”

“Mr Garrick,” Pelling said, in the tone of a man naming a rash. “Area manager, Registration Directorate.”

Garrick looked at the photograph on the desk, then at the paper file Miss Ahmed was holding like a child she had been told to put back.

“Directive fourteen. No record is held outside the central extract. The extract is the record, Minister. Anything else is a rumour with a folder.”

“I am the minister.”

“For Personal Registration, yes, and I’ve a note from the Permanent Secretary’s office to say your instruction takes effect when it’s countersigned by the Receiver’s delegate.”

“Who is that?” Arthur asked.

“There isn’t one yet. That’s why it’s pending.”

Arthur understood the lock then, and admired the workmanship. Nothing had been forbidden. Everything was merely awaiting a signature that did not exist.

Beatrice said quietly, “He’ll bury it.”

Garrick heard. He had the face of a man who had been called a villain once and had not enjoyed it, and what he said next was not for Bell’s benefit.

“If that file goes missing, Miss Ahmed is the one who loses her post. Not me. I’d like that noted.”

“It’s noted,” Arthur said.

“There is a way.” Garrick lowered his voice. “A Form 7B. An identity interview, for a witness to the deviation. Ninety minutes at the Directorate in Victoria Street, thumb on the reader, and I can countersign the file as an exhibit in my own hand. It wouldn’t be mine to refuse then. It would be evidence.”

“Whose thumb?”

Garrick looked at Arthur’s wrist and then, with great tact, at the ceiling.

“Don’t,” Beatrice said. “That reader feeds the central register.”

“I know.”

“Then you’re giving him your signature.”

“I’m giving him a thumb,” Arthur said. “He’ll have it by Thursday anyway. I’d like Miss Ahmed to still have a job on Friday.”

She said nothing. It was the loudest thing she did all day.

It took two hours and ten minutes. The reader was slow, the form had a box for mother’s maiden name that was never going to be right for anyone that week, and a woman in the queue explained to Arthur at length why her daughter’s bicycle licence proved that she was alive. Garrick countersigned at ten to six in blue ink, with the expression of a man doing something brave by accident. By then Pelling’s hearing had slipped from nine in the morning to eleven, because the only room the Directorate would release was booked until then for a tribunal about parking.''')

# ---- Ch14
d.cutp('He had no answer ready, which was the beginning of an honest conversation.')

# ---- Ch15: Reed, Trent, Okafor, frame
d.sub('Bell waited with a woman in uniform and a young man holding a tablet.','Bell waited with an officer in grey whose name tape read REED, and a young man holding a tablet.')
d.sub('“With myself. Yes.”','“With myself. Yes.”\n\nEleanor wrote it on her cuff: two Bells, one frame, neither ever through her machine. It was both the good news and the insult.')
d.before('Eleanor looked at the clock. Six minutes left.','''At the desk behind her, a guard whose badge read L. TRENT looked at the notebook in Arthur’s hand as though it were more alarming than his face. Beyond him a clerk, Ms Okafor by her lanyard, was writing in a pad she kept below the counter and out of the camera’s angle. She did not look up. She did not stop either.''')
d.after('It looked cheaper in person.','''Eleanor’s eyes went to the panelling beside the portrait, where one section had newer screws than its neighbours. She said nothing until they were in the recess.

“A frame,” she murmured. “Single passenger, a hundred kilos, keyed to him. That’s how the younger one goes forward and the older one comes back, and why neither of them needs us.”''')
d.after('“Who defined the threat?”','''By the door, Reed stood with his hands behind him and looked at the floor.''')
d.cutp('That was when Arthur understood the invitation.','That was when Arthur understood the invitation. Bell had not meant to trap him. He had meant to make repair look like demolition, and the clean desks were doing most of the work.')

# ---- Ch16: capacity reconcile, explainers
d.sub('“We have enough capacity for nineteen, in groups,” Eleanor said. “Perhaps twenty-three if we strip the freight allowance.”\n\n“Twenty-seven names,” Miriam replied.\n\n“Eight unlocated.”\n\n“Seven now.”','“The freight window is rated for twenty-one hundred kilograms of protected load,” Eleanor said. “At seventy a head that is thirty people. Allow for bags, chairs and the fact that nobody is a standard adult, and call it twenty-three. Nineteen is the number I’d promise.”\n\n“Twenty-seven names,” Miriam said. “Nineteen inside the complex when I left, Jon among them. Eight elsewhere.”\n\n“Seven, now that we’ve seen Elise,” Arthur said. “Which makes twenty inside.”\n\n“Which makes twenty, if she is where he put her.”')
d.sub('The hearing would begin in forty minutes.','The hearing would begin in twenty-five minutes.')
d.sub(' They were building the kind of record they claimed to want, and it was slower than simply believing their witness.','')
d.sub(' Knowledge of the future was becoming ordinary investigation: witnesses, dates, uncertainties, revision.','')

# ---- Ch17: Hester and Daniel disagree
d.before('Daniel read the sheet, moving his lips.','''Daniel read it through once, and then did something she had not expected. He put it down.

“It doesn’t say who.”

“It says what.”

“It says a gentleman’s secretary left a note. Any lawyer would say the secretary acted alone. I carried that packet. I put it in Bell’s hand. I can say so.”

“And they will know your name and your lodgings.”

“They know both already.”

“They know where you sleep. They don’t know you’ll say it in print.”

Gant, who had been pretending to be deaf, said, “Libel,” to the type.

“A sheet that names a man with a barrister,” Hester said, “is seized by Thursday and burned by Friday. A sheet that quotes his own note and sends him a bill is boring, and boring survives. I want it boring enough to be found in a hundred years.”

“I don’t want it to survive,” Daniel said. “I want it to hurt.”

“Those are two different jobs and I own one press.”

He stood up. He was not a tall young man and the cellar was not a tall cellar, but he stood up as if the roof were optional.

“Then put my name under it. Daniel Wren, deliverer of the packet. Put the address. Then it isn’t a rumour. It’s a man.”

“Mr Ferris holds your indenture.”

“I know who holds it.”

“He’ll read that sheet by nine tomorrow.”

“Then he can read it knowing I didn’t ask his leave.” Daniel took the folded paper out of his coat, the one with the stamp, the one he had carried for three years like a ticket to something. “I’ll take it back to him tonight myself. He can say I’d gone before he knew. That way it’s only me.”

“That is the first sensible thing you’ve said all week,” Hester said, “and I hate it.”

She let him set his own name in type with his good hand, a letter at a time, in the wrong order twice. It was a small line at the bottom of an invoice. He walked out at one in the morning to wake a man who would never forgive him, and came back at two with a sack of his belongings and no indenture, and slept on the floor beside the press as though it were the only bed in London that had not been priced.''')

# ---- Ch18: Dame Judith's interest
d.after('Pelling had appended the objection to all three records.','''Before anyone spoke, Dame Judith North asked that a statement be entered. In the register as it now stood she had never been called to the bar. She sat by courtesy of Mr Pelling’s invitation, and she kept, in the lining of her handbag, a private file of eleven judgments the central extract said she had never given.

“I am not neutral about which record is believed,” she said. “I am merely telling you so. It seems the least a judge can do.”''')

# ---- Ch19
d.sub('That completed the physical verification stage of his machine.','That completed the physical verification stage of his machine, and the thumb Arthur had left on the Form 7B at Victoria had already given him the baseline.')
d.sub('because the distinction was essential and everyone was inclined to panic before hearing it.','because it mattered and everyone was inclined to panic before hearing it.')
d.sub('Their remaining capacity had fallen by a third.','The freight window’s rated load had fallen from twenty-one hundred kilograms to fourteen hundred.')
d.sub('“Nineteen. If we send no freight and use the service lift gap. Twenty at an absolute maximum. No additional induction before the 1815 mission.”','“Twenty at seventy a head. Nineteen once you allow for bags. No freight, no chairs, nobody weighing themselves generously, and the service lift gap or nothing. Twenty is the ceiling and I wouldn’t stand on it.”')
d.sub('Ruth’s family had become impossible within the plan they could physically perform.','Ruth’s family had been outside the plan from the beginning; now they were outside the arithmetic.')

