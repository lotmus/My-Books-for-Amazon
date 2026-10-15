import re,glob,json,os
D='/workspace/dt/rev3/chapters/'
def path(ch): return glob.glob(D+'ch%02d_*.md'%ch)[0]
def rd(ch): return open(path(ch),encoding='utf-8').read()
def wr(ch,t): open(path(ch),'w',encoding='utf-8').write(t)
def R(ch,old,new,n=1):
    t=rd(ch); assert t.count(old)==n,(ch,old[:50],t.count(old)); wr(ch,t.replace(old,new))
def A(ch,new):
    t=rd(ch).rstrip('\n'); wr(ch,t+'\n\n'+new+'\n')

# ---- 1. trailing similes / man-who clauses (cuts)
sim=re.compile(r'(, (?:and )?(?:like|as if|as though|in the manner of|with the [a-z, -]{0,40}of) (?:a|an|the|someone|somebody)[^.!?]{12,200})(?=[.!?]( |$))')
man=re.compile(r'(?<!["“])( (?:with|in|and) (?:the |an? )?[A-Za-z ,-]{3,60}? of (?:a|an) (?:man|woman|person|child|boy|girl) (?:who|whose|with)[^.!?"“]{8,150})(?=[.!?])')
cutS={0,2,4,5,6,7,9,11,15,16,17,19,23,25,27,28,29,30,33,35,37,38}
cutM={0,2,9,12,14,15,19}
fs=sorted(glob.glob(D+'ch*.md'))[8:]
si=0;mi=0;ns=0;nm=0
for f in fs:
    t=open(f,encoding='utf-8').read()
    def fs_(m):
        global si,ns
        i=si; si+=1
        if i in cutS: ns+=1; return ''
        return m.group(1)
    t=sim.sub(fs_,t)
    def fm_(m):
        global mi,nm
        i=mi; mi+=1
        if i in cutM: nm+=1; return ''
        return m.group(1)
    t=man.sub(fm_,t)
    open(f,'w',encoding='utf-8').write(t)
print('cut similes',ns,'man-who',nm)

# ---- 2. set pieces
R(21,"found it funny and went on.\"\n","""found it funny and went on."

The hen, who had not been consulted, chose that moment to express a view. She went up the leg of my chair, onto the table, and across the file in three strides, took Item Seven in her beak, and left the room by the cat flap with the whole of the Department's refreshment policy.

I went after her. So, I am sorry to say, did Dr Calder, in her slippers, and for some time the garden was the scene of two adults and a Rhode Island Red conducting a negotiation at speed round a water butt. It was Sophie, who had not moved from the table, who solved it. She put one foot out as the hen came by. The hen stopped. Sophie bent down, took the page, and returned it to me with a small hole in it, directly through the words *will be provided.*

"She's never liked that one," said Dr Calder, out of breath, and we went back in.
""")
R(23,"""It's a bit like two people at a party who haven't been introduced."
""","""It's a bit like two people at a party who haven't been introduced."

Then the fan stopped.

It did not stop dramatically. It slowed, coughed once, ticked, and was silent, and in the silence the grey tower on the shelf gave a small high note that I did not like. Dr Calder was across the cellar before I had understood it.

"Heat," she said. "It's the fan. It's been threatening to since Easter." She had the side off the case with a bread knife, and the warm breath of the thing came out into my face. "Ned, my love, it's going to be a little stuffy."

"Auntie Imogen, why is it going *tick?*"

"It's the radiators."

"We haven't got radiators."

"Peas," said Sophie.

She was already on the stairs. She came back with four bags of frozen peas, and the manner of a woman who has dealt with domestic emergencies before and has never found them a reason to raise her voice. She laid the peas along the hot metal. Dr Calder held the case. I held up my phone as a torch, and out of it Daniel-A said, evenly, "Core temperature is eighty-one and rising. Eighty-three. I suggest the peas be moved a little to the left."

We moved them to the left.

"Eighty-three," said Daniel-A. "Eighty-two. Eighty-two. Eighty-one."

"Are you putting peas on me?" said the speaker.

"Yes," said Dr Calder.

"Why?"

"You were a bit hot, darling."

There was a considerable silence, and a drip from the ceiling. "That's the best day," said Ned.

Dr Calder sat down on the cellar floor with her back against the shelves and cried for about a minute, efficiently, as a woman does who has had practice and knows the schedule. Then she got up and fetched a screwdriver. "Eleven thousand days," she said, "and it's a *fan.*"
""")
A(24,"""---

We had perhaps four minutes. Then the hen, who had been sitting on the cellar steps with the air of a sentry, got up and went out through her flap, and began in the yard to make a noise I had not heard from her before. It was the noise of a smoke alarm being introduced to a bagpipe.

"That's the gate," said Dr Calder.

Through the kitchen window we saw a long grey van across the end of the lane, and a man coming up the path with a clipboard held to his chest, as if his authority resided in it. He was about forty, in a raincoat the colour of a filing cabinet. Behind him came two young men in lanyards, carrying between them an empty crate marked **EXHIBITS.**

"Mr Lessing," said Giles, in a voice with no air in it. "Continuity Compliance. He's the one who goes to people's houses. He must have followed me. Oh, God. I took the *train.*"

"Is he armed?" said Sophie.

"He's got a lanyard, Miss Mercier."

"Right," said Dr Calder. She looked, for the first time since we had met her, not frightened but interrupted. "Giles, the coal-hole. Daniel, the other end of that. Sophie, put the kettle on."

"The kettle?"

"They'll want tea. They always do. It's a very long form."

The other end of that was the tower, in its case, with Ned asleep in it, and the peas still cooling its flank. We carried it up the cellar steps between us, with Daniel-A whispering directions from my pocket, through the scullery and across the yard, and put it in the potato store, behind eleven sacks of King Edwards and a door that said **BEWARE OF THE HEN.** I have carried heavier things. I have not carried anything that I was so afraid to knock against a door frame. I covered it with sacking and said, to nobody, "Sorry, Ned," and Dr Calder said, "He's sleeping, he'll not mind," and we went back across the yard at an unhurried walk, at the exact moment that Mr Lessing knocked.

He had a thin, pleasant, tired face, and he did not wait to be asked in. "Dr Calder. Continuity Compliance, Cabinet Office. I have a notice of inspection under the Continuity (Residual Assets) Regulations."

"I'm sure you do," said Dr Calder, setting down a tray. "Biscuit?"

He took one. I think it was the training. "I believe you hold a file."

"I do," said Dr Calder. She went to the Aga and lifted the lid on the hot plate that nobody used, and brought out a cardboard folder, grey with age, labelled in blue ink **PROGRAMME, 1976 to 1994,** and put it into his hands. "It's been in the way for thirty years. You'd be doing me a kindness."

I did not understand, then, what it cost her. I understood it in the van afterwards, when I watched her face. It was everything she had written down, in order, in her own hand, and she gave it to him with a tray of biscuits and no more expression than she would have shown a man collecting a parcel. Sophie, I learned later, had photographed every page of it that morning, over breakfast, with her phone, while the rest of us were finding our feet. I do not know when she had decided to do so. I think it may have been before she met any of us.

"And the, ah, the asset?" said Mr Lessing.

"There is no asset," said Dr Calder. "There is a retired woman and a hen."

One of the young men had found the cellar door. "Sir. There's equipment down here. Cables. A, a cooling unit."

"A freezer," said Dr Calder, evenly. "I keep peas."

The young man went down. We listened to him go down. We listened to him go on being down, for quite a while, and I looked at Sophie and Sophie looked at the ceiling, and Mr Lessing ate a second biscuit, and looked at me.

"Mr Harper," he said. "You have, I understand, the larger share. The Department will need you at Penge on Monday for a formality. Do sign for the notice when it comes. People who don't sign find the next ones are much more difficult to read."

"What happens on Monday?"

"A variation." He smiled. It was a smile that I recognised, because I had been making it for years at people in meetings. "It will be painless."

The young man came back up with a bag of peas and an expression of puzzled defeat. "Sir, there's nothing. It's an old freezer. There's a hen in the cellar."

There was. She had gone down, past him, while he was busy, and was standing in the middle of the floor facing the steps. I do not know what the hen had decided, but when the second young man stepped towards the potato store, with his crate, she came out of the scullery at him like something fired from a catapult. She took his lanyard in her beak. She took it, as far as I could judge, personally.

"Is that a Rental Presence?" cried Mr Lessing.

"It's a hen," said Dr Calder. "Is she registered?"

"We'll see you in Penge, Mr Harper," said Mr Lessing, from the yard, with his raincoat pulled round him and one young man holding a bleeding thumb and the other holding the crate, which now contained the file. He got into the van. It backed down the lane, as it had come, politely.

At the sink Dr Calder rinsed the cups.

"He never looks at the potatoes," she said. "In thirty years, nobody has ever looked at the potatoes."

Down the lane, in the dusk, beside the green gate, the hen stood in the road with a lanyard in her beak, and watched them go.""")
R(32,"It hung there in the cold light, tea-coloured, ruled, covered with its columns. ","")
R(32,"I saw the two men in the dark suits exchange a glance.","I saw the two men in the dark suits exchange a glance. The younger was Mr Lessing, of the green gate. He did not look at me, which was how I knew.")
R(35,"\"Thank you, Gareth.\"\n","""\"Thank you, Gareth.\"

"Where's Mr Pym?" I said. "I'd have thought he would want to see this."

Gareth looked at his shoes. "He's been moved, sir. A letter, on the Monday. He is the Deputy Registrar of Lost Property (Mammalian) now, in the annexe." He cleared his throat. "It's a promotion. It says so. There's no window." Then, in a rush: "He gave me the folder on the Friday, before. He said I was to tell you the hat was a great success."
""")

# ---- 3. endings
A(10,"Behind us the fridge, which had been listening, proposed a chicken and melon salad. Neither of us had the heart to refuse. Neither of us ate it.")
A(11,"At three in the morning I got up and read Form 4A again, in case it had improved.")
A(12,"Eleven days remained. I had a list, a kumquat tree and a speaker, and only one of the three had ever been correct about anything.")
A(16,"I rang Mrs Pritchard. She said she would wear a hat, which I took as consent.")
A(17,"At Stockwell a man got on with a cello, looked at the umbrella, and decided against it.")
A(18,"The Department emailed an invoice for the certificate before I reached the corner: £14, itemised, with a note that the hyphen in *Daniel-A* had been charged as a character.")
A(19,"At Carlisle Hamish asked whether I had enjoyed my stay. I said I was still in it.")
A(33,"The fridge, after a long deliberation, suggested a quiet evening. It was, for once, correct.")
