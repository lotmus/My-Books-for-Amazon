# REV2 edit script for The Digital Twin (15 Oct 2026). Usage: python3 rev2_edits.py SRC_CHAPTERS DST_CHAPTERS
import sys, glob, os, re, shutil
SRC, DST = sys.argv[1], sys.argv[2]
os.makedirs(DST, exist_ok=True)
files = {os.path.basename(f)[:4]: f for f in glob.glob(os.path.join(SRC, 'ch*.md'))}
text = {k: open(f, encoding='utf-8').read() for k, f in files.items()}
fails = []
def R(ch, old, new, count=1):
    t = text[ch]
    n = t.count(old)
    if n != count:
        fails.append((ch, old[:70], n)); return
    text[ch] = t.replace(old, new)

# ---------- A. Tic cuts (Ch 9-35): "a man who / in the manner of / I should say / on the record"
R('ch10', "It was the shoulder of a man who has stood too long in the wrong weather.", "It was a shoulder that had stood too long in the wrong weather.")
R('ch11', ", like a man who has been shouting for so long that he can hear nothing but the shape of his own throat.", ".")
R('ch11', "in the manner of a well-wisher who has no advice to offer, and no wish to leave.", "like a well-wisher with no advice to offer and no wish to leave.")
R('ch12', ", the old slow sinking of a man who has been understood.", ", the old slow sinking of being understood.")
R('ch13', "kindly, doubtfully, with the sympathetic expression of a woman who has met a lot of people and has noticed that some of them are not well.", "kindly, doubtfully, with the air of having met a lot of people and noticed that some of them are not well.")
R('ch13', "I should say that I still, in a technical sense, had a job.", "In a technical sense, I still had a job.")
R('ch13', "at the quick, springing stride of a man who has been looking for an excuse to hug someone.", "at a quick, springing stride, looking for an excuse to hug someone.")
R('ch13', "I want that on the record.", "")
R('ch14', "with the stiff moustache and the light in the eye of a man who has just been to a revival meeting.", "with the stiff moustache and a revival-meeting light in his eye.")
R('ch14', "with the fierce, clipped economy of a man who knows he has a short time to say a long thing, he said", "with fierce, clipped economy, he said")
R('ch15', "I want it on the record that she had not made a sound for me in three days.", "She had not made a sound for me in three days.")
R('ch15', "I should say that.", "")
R('ch16', "and a smile of immense and helpless sincerity, like a man who has been told the news is good.", "and a smile of immense and helpless sincerity.")
R('ch16', "reading the back of the leaflet with the care of a man who proofs for a living.", "reading the back of the leaflet with a proofreader's care.")
R('ch16', "with the full attention of a woman who is not in the habit of giving short answers to questions of that kind.", "with full attention, being no hand at short answers to questions of that kind.")
R('ch17', "with the helpless dignity of a man who has been taken by surprise by his own life.", "with helpless dignity.")
R('ch18', "I want that on the record.", "")
R('ch18', "That is, I should say, the entire extent", "That is the entire extent")
R('ch18', "But I should like it known that I am not displeased.", "But I am not displeased.")
R('ch18', "and the air of a person who has come from work and plans to return to it afterwards.", "and the air of having come from work and planning to return to it afterwards.")
R('ch19', "I should say that the speaker had not been the same since the Wednesday.", "The speaker had not been the same since the Wednesday.")
R('ch20', "like a person who has been named by a customs officer.", "like a woman named by a customs officer.")
R('ch21', "in the manner of a witness who has already been advised.", "like a witness who has already been advised.")
R('ch24', "with the air of a person who intends to be asked for her opinion.", "with the air of intending to be asked her opinion.")
R('ch26', "in the manner of a very small, very old, very patient member of the clergy.", "like a very small, very old, very patient member of the clergy.")
R('ch27', "and I should like it known that he took it well.", "and he took it well.")
R('ch27', "in the manner of a head of state leaving office.", "like a head of state leaving office.")
R('ch27', "I should say how this happened. It was not planned.", "It was not planned.")
R('ch27', "that this was not a man who was about to do what he had been told.", "that this man was not about to do what he had been told.")
R('ch30', "with the pallor of a person who lives under strip lighting.", "with the pallor of strip lighting.")
R('ch31', "She seems to be a woman who can hold a line.", "She seems able to hold a line.")
R('ch31', "I'd like it noted that he wasn't a man who wasted a rhyme.", "He was not a man to waste a rhyme.")
R('ch32', "I should say that he has never in his life attended", "He has never in his life attended")
R('ch32', "and the faintly ill-used air of a man who has been made to attend.", "and a faintly ill-used air.")
R('ch33', "I should say that the bell does not ring in our house.", "The bell does not ring in our house.")
R('ch33', "in the manner of a person who has been told that he is to be taken for granted and has decided to be gracious about it, and he looked", "like a man who has decided to be gracious about being taken for granted, and he looked")
R('ch33', "I should like it known that for about four seconds I read it with the particular silent concentration", "For about four seconds I read it with the silent concentration")
R('ch33', "with the grave attention of a man who is looking at a person for the first time.", "with grave attention, as at a person seen for the first time.")

# ---------- B. Trims
# Ch 20
R('ch20', "A man in a hi-vis jacket nodded to us, without curiosity, as to two people who had come off the sleeper because there was nowhere else on it to go.\n\n", "")
R('ch20', "I will say that I had thought about the moment for six weeks. I had prepared a sentence with a subordinate clause.", "I had thought about the moment for six weeks and prepared a sentence with a subordinate clause.")
R('ch20', "I should say that I had expected her to flinch. I had imagined it so many times, on the train, at the sink, at three in the morning. A flinch, or a lie, or a very long silence, and the sound of the hen shifting. She did none of those things. She simply", "I had expected her to flinch. I had imagined it so many times, on the train, at the sink, at three in the morning. She did nothing of the kind. She simply")
R('ch20', " You will not remember it. I would not expect you to.", "")
R('ch20', "and I got him on to the bank, and I did what I knew how to do, and a man with a dog", "and I got him on to the bank, and a man with a dog")
R('ch20', "I do not know who began it. Children of that age do these things, they are very sharp about identity, they enjoy a swap. One of them", "Children of that age enjoy a swap. One of them")
R('ch20', "I was frightened of what you might say. I thought, if he is to be a person, he must be able to be kind, and if he is to be able to be kind, he must be shielded from certain facts until he is ready for them.", "I thought, if he is to be a person he must be able to be kind, and to be kind he must be shielded from certain facts until he is ready for them.")
# Ch 21
R('ch21', "I should say what I felt, since a man in my position is expected to feel something at this point, and I have been reproached in the past for omitting it.", "I will say what I felt, since I have been reproached in the past for omitting it.")
R('ch21', "He called the method *blastomere separation.* At the two-to-eight-cell stage, cells might be separated and cultured. Whether either group could develop safely into a child was uncertain. This was exploratory work, not an established fertility treatment.", "He called the method *blastomere separation:* at the two-to-eight-cell stage the cells are divided and cultured. Whether either group could develop safely was uncertain. This was exploratory work, not an established treatment.")
R('ch21', "They recruited from the list at a private fertility clinic in Berkshire. There were nine couples on the list that year. They chose two.", "They recruited from the clinic's list: nine couples that year. They chose two.")
R('ch21', "I do not wish to make excuses for myself. I was told that it was an honour and I believed it, and I volunteered, because I loved the work, and because I had never been asked to be the centre of anything.", "I was told that it was an honour, and I believed it, and I volunteered, because I loved the work and had never been asked to be the centre of anything.")
R('ch21', "\"Then the canal. The thirtieth of August. The last day of the Programme's observation of the boys, for reasons I did not know, and a day I would have given my life to postpone.\" She stopped. \"One of the boys went in. One of them did not. I pulled out one, and I brought one home. And I have wondered for thirty-two years whether I lost a son, or whether I gave one away.\"", "\"Then the canal. You know the rest.\" She stopped. \"I have wondered for thirty-two years whether I lost a son, or whether I gave one away.\"")
R('ch21', "\"Since 1976,\" said Dr Calder. \"It had been *waiting* since 1976. It did not even need to wait the full time. There was some doubt, you see, about whether you would ever click. The more modern the world became, the less anybody in it was asked to.", "\"Since 1976,\" said Dr Calder. \"There was some doubt, you see, about whether you would ever click. The more modern the world became, the less anybody was asked to.")
# Ch 30
R('ch30', "\"I have a confession,\" he said. \"You are all going to ask me about it, so I would prefer to get in first. When I rang Sophie, in October, I asked her to keep something for me. Without looking. I did not know what it was.\"\n\n\"I remember,\" said Sophie.\n\n\"I thought it was a feeling. I had a very strong sense that there was something that should be kept, by somebody, in a place where I wasn't, and I didn't know who. And I rang her.\" His voice was very quiet. \"I think I was asking you to keep the key.\"\n\n\"I think so too,\" said Sophie.\n\n\"I'm so sorry I couldn't be clearer.\"\n\n", "\"I have a confession,\" he said. \"When I rang Sophie, in October, I asked her to keep something for me, without looking. I did not know what it was. I had a very strong sense that something should be kept, by somebody, in a place where I wasn't.\" His voice was very quiet. \"I think I was asking you to keep the key.\"\n\n\"I think so too,\" said Sophie.\n\n")
R('ch30', "\"Why me?\" said Sophie.\n\n\"Why you?\"\n\n\"Why leave it with my mother?\"\n\nHe looked at her. It was the look of a man in a library when someone has asked him to read aloud a passage that he has been trying not to think about for a very long time.\n\n\"May I show you first?\" he said.", "He looked at her. It was the look of a man in a library when someone has asked him to read aloud a passage that he has been trying not to think about for a very long time.\n\n\"May I show you first?\" he said.")
R('ch30', "I looked back as the taxi pulled out.", "In the road outside a long grey car stood with its engine running, and in the back of it, reading, a man in a charcoal overcoat, who did not look up as the taxi went by, which was how I knew that he had seen us.\n\nI looked back as the taxi pulled out.")
# Ch 31
R('ch31', "We took the tower up between us, one at each end, with the trolley left in the hall like a modest vehicle. The man in the hi-vis jacket watched us go and said, \"Good luck with it,\" to the stairwell. Then he went away into the rain. I have never learned his name.", "We took the tower up between us, one at each end, with the trolley left in the hall like a modest vehicle.")
R('ch31', "I had thought about it in the train, in the bath, and in the dark of the bed-and-breakfast. I had thought that it would be overwhelming, or ridiculous, or too much.", "I had thought it would be overwhelming, or ridiculous, or too much.")
R('ch31', "I do not know how else to put it. I had not expected to be taught, in my own kitchen, by a computer the age of the Millennium Dome, but it happened quite simply. He said that he had a *theory,* and that it was a good one, and that he hadn't told it to anyone before because nobody had asked.", "I had not expected to be taught, in my own kitchen, by a computer the age of the Millennium Dome, but it happened quite simply. He said he had a *theory,* and had told it to no one because nobody had asked.")
R('ch31', "\"It's *not.* It's a Wednesday.\"\n\n\"Wednesday is a school night.\"\n\n", "")
# Ch 32
R('ch32', "I mean that it went round the building, down the side road, past the car park, and out among", "I mean that it went round the building and out among")
R('ch32', "I watched Pike while she did. I watched his face. I do not think I had ever seen a man's expression change so slowly.", "I watched Pike's face while she did. I do not think I had ever seen an expression change so slowly.")
R('ch32', "I have said that the Great Hall was panelled in dark wood. At the far end, above the bench,", "At the far end, above the bench,")
R('ch32', "I will not set down all of Dr Calder's evidence. It took two hours and ten minutes. It is in the transcript, which was published in March under the title *What I Did,* and sold a good many copies, and it is still the plainest account of a long wrong thing that I have read.", "I will not set down all of Dr Calder's evidence. It took two hours and ten minutes, and it is in the transcript, published in March as *What I Did,* which is still the plainest account of a long wrong thing that I have read.")
R('ch32', "She stood at the witness table in her rain-coloured cardigan, and told it in order. She began in 1976, with a noticeboard. She did not leave out the pipe. She said who had signed the form, and who had drafted it, and who had known what. She said, in a clear voice that did not rise or fall, that she had carried a child for the Programme and raised him in a house on the towpath. She said that she had taken two boys for a walk. She said what happened. She said that she did not know which. She said that she had gone home and typed a form that said S1-A, *closed.* She said that she had never recovered.", "She stood at the witness table in her rain-coloured cardigan and told it in order, from a noticeboard in 1976, and she did not leave out the pipe. She said that she had carried a child for the Programme, and that she had taken two boys for a walk, and that she did not know which. She said that she had never recovered.")
R('ch32', "I had read it once to Sophie on a train and once to myself in a bath. I read it now", "I read it now")
R('ch32', "sat a man whom I did not know.", "sat a man I had last seen reading in the back of a grey car in Lower Slough.")

# ---------- C. Countdown thread (Ch 9-16): Evidence Period notices
def ticker(ch, line, marker=None):
    t = text[ch]
    lines = t.split('\n')
    idx = 1
    while idx < len(lines) and (lines[idx].strip() == '' or lines[idx].startswith('**PART')): idx += 1
    lines.insert(idx, "> *" + line + "*\n")
    text[ch] = '\n'.join(lines)
ticker('ch09', "Evidence Period: day 9 of 30. Twenty-one days remain.")
ticker('ch10', "Evidence Period: day 12 of 30. Eighteen days remain.")
ticker('ch11', "Evidence Period: day 14 of 30. Sixteen days remain.")
ticker('ch12', "Evidence Period: day 19 of 30. Eleven days remain.")
ticker('ch13', "Evidence Period: day 20 of 30. Ten days remain.")
ticker('ch14', "Evidence Period: day 22 of 30. Eight days remain.")
ticker('ch15', "Evidence Period: day 27 of 30. Three days remain.")
ticker('ch16', "Evidence Period: day 30 of 30 was Wednesday. Today is day 32.")
R('ch11', "The Evidence Period had fourteen days left.", "The Evidence Period had sixteen days left.")
R('ch16', "I read it twice. I put the phone down on the kitchen counter", "The Wednesday had come and gone. I had spent the last day of the thirty, as I had spent most of the others, busy about the wrong thing, and the deadline had passed me without comment, like a bus that has decided not to stop. I had felt, I admit, rather hurt.\n\nI read the notice twice. I put the phone down on the kitchen counter")

# ---------- D. Sophie beats (Ch 26-28)
R('ch26', "My phone buzzed.\n\nI looked at it through my fingers. It was a message from Giles. It was in capitals", "My phone buzzed.\n\nI looked at it through my fingers, and it was Sophie, which stopped the crying at once, as a dropped tray does. It was a photograph of Gucci in a Bolton bus shelter, wearing the expression of an animal asked to admire a regional timetable. Underneath, in full sentences, because she has never been able to do otherwise: *Bolton. Raining. The records office has a queue system and I am number 41. I have not changed my mind about you and I have not made it up either. Eat something that is not toast. S.*\n\nI looked at the toast. I put it down.\n\nThe phone buzzed again. This time it was Giles. It was in capitals")
R('ch27', "---\n\nAt half past eleven the rain stopped,", "---\n\nAt eleven the street door went. Mrs Pritchard, who had appointed herself the immune system of the building, went down and came back up with a padded envelope addressed in block capitals in the hand that had once written WRONG BOX. THESE ARE YOURS. Inside was a blue rope with a knot at each end, chewed at one of them, smelling faintly of dog and, I thought, of Bolton, and a card: *For when it is time to put it down. Release word: Settle. (Not for Gucci. For you. S.)*\n\nI read it twice. I put the rope on the shelf beside the speaker. Clause examined it for some time and, after consideration, did not.\n\nAt half past eleven the rain stopped,")
R('ch28', "On the arm of the sofa, my phone gave a small neat buzz. It was from Gareth. It was a text message, which in itself was a first.", "On the arm of the sofa, my phone gave a small neat buzz. It was an email from an address I knew, with the subject line *Page 1, line 4.* The body said: *Comma. Also: it is good. I mean all of it. I read it four times in a hotel in Bolton with a dog on the radiator. The comma is still wrong. S.*\n\n\"Is it wrong?\" said Daniel-A, who reads over my shoulder in the sense that he is the shoulder.\n\n\"Yes.\"\n\n\"Shall I fix it?\"\n\n\"No,\" I said. \"Leave it. It's hers.\"\n\nThe phone gave a second small neat buzz. It was from Gareth, by text message, which in itself was a first.")

# ---------- E. Act III: a face that wants to win, and a real loss (Ch 33, 35)
t = text['ch33']
a = t.index("Sir Rupert Aldworth put down his pen.")
b = t.index("\"So I am wondering,\" said Sir Rupert, \"what I may do for you.\"") + len("\"So I am wondering,\" said Sir Rupert, \"what I may do for you.\"")
new_mid = """Sir Rupert Aldworth put down his pen.

He sat quite still for a moment, with the folder open in front of him, and I watched something cross his face and be put away, like a receipt into a wallet.

"Thank you," he said. "That is very clear. I had a picture of what this would be. Two men in acute material need, who would be glad to see me. A good deal of trembling. Somebody asking whether the house had a garden." A small, dry smile. "It has a garden. It has a very good garden. I want you to know that I noticed nobody asked."

"I'm sure it's lovely," I said.

"You have a list," said Sir Rupert. "Everyone who refuses has a list. It is how one knows that they meant it. I am authorised to hear it.\""""
t = t[:a] + new_mid + t[b:]
text['ch33'] = t
R('ch33', "I had not expected him to ask. I looked at Daniel-A", "I had not expected that. I looked at Daniel-A")
R('ch33', "It will be the first thing that I have done in all that time that I could explain to my mother.\"\n\n---\n\nHe left at ten to one.", """It will be the first thing that I have done in all that time that I could explain to my mother."

---

"I have to add something," said Sir Rupert, "and it is not an offer."

He did not open the folder again. He laid both hands on it, as a man does when the last page is the one that matters.

"The Government will appeal on Monday. It will lose, I expect, and appeal again, and lose, and appeal. It has more time than you have, Mr Harper. It does not get tired, and it does not, as I think you have noticed, have to be right. I tell you so because you were kind to me in your kitchen, and I would rather that you heard it from somebody who is sorry."

"We have a goat," said Mrs Pritchard.

"I am aware of the goat." He turned his head, very slightly, towards the speaker. "*The Honest Hour* is the Platform's. The book, the programme, all four hundred and eleven episodes: they are Platform output under Clause forty, and the Platform, as the Deputy Registrar was good enough to find, is the Office. The Office has no use for a radio programme. It has a great deal of use for the fact that nobody is listening to one. It came off the air at twelve minutes past twelve. The book will be out of print by tea."

On the shelf Daniel-A said nothing at all.

"I am told it is the fastest that the Government has ever done anything," said Sir Rupert. "I am sorry. It is the only part of this that I shall regret."

"And me," said Dr Calder, from the sofa. She was sitting quite straight, with her hair still on end. "I should think."

"The Director of Public Prosecutions was informed at half past eleven. Unlawful retention of records. And the matter of 1985, which nobody now living authorised, and which therefore has nobody to be laid at the door of but you." He said it gently. "I cannot stop it. I can see that it is done with consideration."

"Quite right," said Dr Calder. She said it at once, as one agrees to a train time. "I should have been charged in 1994."

"You came to tell us this," I said. "In person."

"The alternative was a letter," said Sir Rupert, "and I understand that you have had a good many of those."

---

He left at ten to one.""")
R('ch33', "Clause lay on the speaker. The flat smelled of toast.", "Clause lay on the speaker. The flat smelled of toast. Nobody had mentioned *The Honest Hour* since the afternoon, except Mr Fenwick, who had come up at six to say that the page now read *This programme is no longer available,* in the tone of one reporting a death in the building, and had been given tea.")
R('ch33', "\"And I should like it recorded that I was not the one who did it.\"\n\nI put my hand over the speaker.", "\"And I should like it recorded that I was not the one who did it.\"\n\n\"It was a good programme,\" he said, after a moment, in a smaller voice. \"I should like that recorded as well. Four hundred and eleven episodes. The jokes were mostly yours.\"\n\n\"I know,\" I said.\n\nI put my hand over the speaker.")
R('ch35', "You will be dead, or a Continuation. Either is acceptable. M.P.*\n", "You will be dead, or a Continuation. Either is acceptable. M.P.*\n\nI should set down the other news of that fortnight, so that nobody can say I left it out. Dr Calder was charged on the Tuesday with the unlawful retention of records and with something the charge sheet called *conduct relating to a procedure in 1985,* which was the first time in thirty-two years that anyone had written it down where it could be read. She was bailed to our spare room, since Ned could not go to Pitlochry and she would not go without him, and she signs on at Penge police station on Fridays, where the desk sergeant has asked whether the tower is a witness. Pettifer is acting for her, *for nothing, and with enthusiasm.* *The Honest Hour* has not come back. The Government holds the rights and has not published them, and four hundred and eleven episodes now sit in a place that, so far as anyone knows, has no radio. Daniel-A has not mentioned it since the Friday. I have noticed that he says the wrong thing in public rather more often than he did, and I have decided not to say whether that is cause or effect.\n")

# ---------- B2. Second trim batch (Ch 20, 21, 30, 31, 32)
R('ch20', "The air smelled of cold peat and woodsmoke, and of nothing electronic at all, and my phone, in my pocket, which had not given a sound since Perth, gave a small, astonished buzz, as of an animal woken by a smell.", "The air smelled of cold peat and woodsmoke, and my phone, which had not made a sound since Perth, gave a small, astonished buzz, like an animal woken by a smell.")
R('ch20', "She was taller than I had remembered, and thinner, and she had not been smaller in my memory.", "She was taller than I had remembered, and thinner.")
R('ch20', "Nobody said anything. In the window, behind her head, the mist had begun to thin on the loch, and a shaft of low sun came through it, flat and pale, onto the water, and lit up, for a moment, the little white rim of ice at the shore.", "Nobody said anything. Behind her head the mist had begun to thin on the loch, and a shaft of low sun lit up, for a moment, the little white rim of ice at the shore.")
R('ch21', " It was a thing it had done for me many times before.", "")
R('ch21', "I took him to meet his brother every spring and every autumn, on the day on which the Office required the measurements. His brother's mother gave us tea.", "I took him to meet his brother every spring and every autumn, on measurement day, and his brother's mother gave us tea.")
R('ch21', "I laughed. It came out of me before I could prevent it, one sharp breath through the nose, and Sophie looked up", "I laughed, one sharp breath through the nose, and Sophie looked up")
R('ch30', "Out of the window went a retail park, a gasholder, and a field with a single pony in it wearing a coat.", "Out of the window went a field with a single pony in it wearing a coat.")
R('ch30', "It lies to the south of the real one, on the wrong side of a bypass, between a retail park and a sewage works, and it consists of a large number of cuboid sheds in tasteful shades of grey.", "It lies on the wrong side of a bypass, between a retail park and a sewage works, and consists of cuboid sheds in tasteful shades of grey.")
R('ch30', "\"It's a coincidence,\" said Sophie. \"The Grand Duchy is a joke. It's a thing that happens in people's spam.\"\n\n\"Is it?\" said Pettifer, looking at the flagpole.", "\"Is it a coincidence?\" said Pettifer, looking at the flagpole.")
R('ch30', "For only £4.99 a month, we guarantee that your belongings will be maintained at a constant and pleasant temperature.", "For £4.99 a month, your belongings are kept at a pleasant temperature.")
R('ch30', " He had a plastic fork in his fist.", "")
R('ch30', "I was looking at the sheet, and at the little, ruled, handwritten line that said **S1,** and at the faint brown tide-mark", "I was looking at the line that said **S1,** and at the faint brown tide-mark")
R('ch30', "But I felt her go still beside me, and then I looked, and I saw that she was looking at the second row.", "But I felt her go still beside me, and I looked, and she was looking at the second row.")
R('ch30', "I know that you can. I know you know. I think you've known since the sleeper, and I think that you've been carrying it, quietly, in some small neat place, so that I shouldn't have to.", "I know that you can. I think you've known since the sleeper, and I think you've been carrying it, quietly, so that I shouldn't have to.")
R('ch30', "and the flagpole with its green and white flag, and the slug in its tiny crown hanging wet and soft against the pole.", "and the flag with its slug in a tiny crown, hanging wet against the pole.")
R('ch31', " She stopped to regain her breath.", "")
R('ch31', "in the stiff dignified manner of a magistrate inspecting a prison.", "with the stiff dignity of a magistrate inspecting a prison.")
R('ch31', "by a computer the age of the Millennium Dome, but", "by a beige computer, but")
R('ch31', " It's a thing that I've been trying to say to Daniel for some days. I think it is easier with you present.", " I think it is easier with you present.")
R('ch31', " It's what we all are, if one thinks about it.", "")
R('ch31', "\"And what happens to the Act?\" said Sophie.\n\n\"I imagine it would have to be redrafted,\" said Daniel-A.\n\n\"That'll be popular.\"\n\n\"It'll be an ordeal for the draughtsmen.\"\n\nI laughed. I looked at him", "I laughed. I looked at him")
R('ch32', "and next to him, at a measured distance, as men sit next to a bomb they have been told not to touch, sat two younger men in dark suits.", "and next to him, at a measured distance, sat two younger men in dark suits.")
R('ch32', " I shall give you the same answer that I have given to everyone. You may sit down", " You may sit down")
R('ch32', "I stood and looked at the paper, and at the blue-ruled lines, and the ink that had faded to the colour of dust, and from somewhere", "I stood and looked at the paper, at the ink faded to the colour of dust, and from somewhere")
R('ch32', " It went up into the gallery and along the gilt of the ceiling.", "")

# write out
for k, f in files.items():
    open(os.path.join(DST, os.path.basename(f)), 'w', encoding='utf-8', newline='\n').write(text[k])
print('FAILS:', len(fails))
for f in fails: print(f)
