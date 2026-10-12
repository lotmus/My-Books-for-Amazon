import os, shutil
W = r"C:\Users\lomus\git-dirs\wt-scallywag\Scally_and_the_Sleepless_Stream"
os.chdir(os.path.join(W, "Step_Stories_Texts"))
shutil.copy("Book2_Story_v5.txt", "Book2_Story_v6.txt")
t = open("Book2_Story_v6.txt", encoding="utf-8").read()
miss = []
n0 = len(t.split())


def cut(a, b="", label=None):
    global t
    if a in t:
        t = t.replace(a, b, 1)
    else:
        miss.append(label or a[:40])


cut("There was a murmur. A lot of people had had no sleep for two nights. It was a murmur of people thinking that two hundred sandbags did not sound too bad.",
    "There was a murmur of people who had not slept for two nights, thinking that two hundred sandbags did not sound too bad.")
cut("It curled one way, and then the other, like a dropped rope, in great lazy bends, so that the path beside it followed along, and along, and along, and never seemed to get anywhere.",
    "It curled one way, and then the other, like a dropped rope, in great lazy bends, and the path beside it followed along and never seemed to get anywhere.")
cut("Hopsi’s face had gone white as paper. Hal, who had once stood on the mill step and been spoken to by it in the fog, felt his scalp tighten from the top of his head to the base of his spine. Gucci growled, low, like a kettle, at the water.",
    "Hopsi’s face had gone white as paper. Hal felt his scalp tighten. Gucci growled, low, like a kettle, at the water.")
cut("It was a voice, but it was no longer a stranger’s voice. It was worn down, and thin, and stuck like a needle in a groove. It was the voice of one sentence, said ten thousand times. And under it, in the water, you could hear the stream, straining at the leash, to be allowed to go on.",
    "It was a voice, but no longer a stranger’s. It was worn thin, and stuck like a needle in a groove, the voice of one sentence said ten thousand times.")
cut("They had been there since dawn. They had not slept. They had not needed to. The Mayor was at the front,",
    "They had been there since dawn. The Mayor was at the front,")
cut("And Scally, who had been given a pair of boots and a life and a gift, was crouching over the board with a brush, quite happily, with his tongue between his teeth.",
    "And Scally was crouching over the board with a brush, quite happily, with his tongue between his teeth.")
cut("It was not much. It was a small thing. But the water, which had turned for fifty years without a rest, hesitated,",
    "It was not much. But the water, which had turned for fifty years without a rest, hesitated,")
cut("It did not stop all at once. It slowed, and slowed, and eased, like a great wheel that has been pushed for fifty years, and at last has been allowed to rest. The funnel in the middle filled. The black water went smooth.",
    "It did not stop all at once. It slowed, and eased, like a great wheel that has been pushed for fifty years and at last allowed to rest. The funnel in the middle filled. The black water went smooth.")
cut("It was the quietest thing any of them had ever heard. It was a silence like a long breath let go. They sat in it. Nobody could speak. Then, slowly,",
    "It was the quietest thing any of them had ever heard, a silence like a long breath let go. Then, slowly,")
cut("Hal went to the pond, to think. He knelt on the bank, and his reflection looked up at him from the water. It had dark rings under its eyes, and its hair stood up like a hedge. It looked as tired as he felt.",
    "Hal went to the pond, to think. He knelt on the bank, and his reflection looked up at him, with dark rings under its eyes and its hair standing up like a hedge.")
cut("It had not winked since the summer. It winked, and its mouth shaped one word, over and over, in a way that Hal could read quite well, because it was the same word in either direction.",
    "It had not winked since the summer. Its mouth shaped one word, over and over, that Hal could read quite well, because it was the same word in either direction.")
cut("Nobody in the valley slept that night.\n\nIn the morning, the miller fell asleep",
    "Nobody in the valley slept that night.\n\nIn the morning, the miller fell asleep")
cut("The village cockerel crowed at midnight, at two, at half past three, and then gave up and sat on a wall looking offended.",
    "The village cockerel crowed at midnight, at two, and at half past three, and then gave up and sat on a wall looking offended.")
cut("“It is stream water, with mud in it,” said Hopsi, “and nothing in it that makes anybody sleep. Hops can help a little, if you are already tired, and you have put in a pinch. It will not cure the hum.” She did not raise her voice. She never did. “Mrs Crumb has paid a penny for a cup of mud, because she thought it was medicine.”",
    "“It is stream water, with mud in it,” said Hopsi, “and it will not cure the hum.” She did not raise her voice. She never did. “Mrs Crumb has paid a penny for a cup of mud, because she thought it was medicine.”")
cut("There was a short, loud argument. Hal’s mother said no. Mrs Crumb said certainly not. The Mayor said he forbade it. Old Walt waited until they were done and then said one thing.",
    "There was a short, loud argument. Hal’s mother said no, Mrs Crumb said certainly not, and the Mayor said he forbade it. Old Walt waited until they were done and then said one thing.")
cut("All morning the stream hummed beside them. It had grown louder in the night. Sometimes it sounded like a word and sometimes like a cat in a barrel.",
    "All morning the stream hummed beside them, louder than in the night. Sometimes it sounded like a word and sometimes like a cat in a barrel.")
cut("Hal looked at the bank. “How do we know what will float?”\n\nHopsi sat down on a stone. “Guess first,” she said. “Then test.”",
    "Hal looked at the bank. “How do we know what will float?”\n\nHopsi sat down on a stone. “Guess first,” she said. “Then test.”")
cut("For one long, awful second there was only a hole in the water.\n\n", "For one awful second there was only a hole in the water.\n\n")
cut("Scally began to laugh, and could not stop. After a minute, all of them were laughing, even Walt, even Dumpling, who gave a low hee-haw. It was the shaky laughing of people who have been frightened and found it was all right.",
    "Scally began to laugh, and could not stop. After a minute, all of them were laughing, even Walt, even Dumpling, who gave a low hee-haw. It was the shaky laughing of people who have been frightened and found it was all right.")
cut("“Cold water,” said Walt, when the laughing had run out. “That is what takes the breath out of a person. It squeezes the chest and you gasp before you know it. A strong swimmer drowns that way. You do not go in alone. You do not go in at all, if you can reach or throw. Do you see why?”",
    "“Cold water,” said Walt, when the laughing had run out, “squeezes the chest and you gasp before you know it. A strong swimmer drowns that way. You do not go in at all, if you can reach or throw. Do you see why?”")
cut("They stood up. They did not shout, because shouting does nothing. They followed, along the edge, along the firm bank, the long way round. At the second bend the grass came up high, and a mist rose off the wet ground, and it turned, in the space of a few minutes, into a white, soft, thick fog.",
    "They stood up. They followed along the firm bank, the long way round. At the second bend a mist rose off the wet ground and turned, in a few minutes, into a thick white fog.")
cut("They found him. He was in clay, up to the knees, in the middle of the neck, and the other boot was gone. The soil had held him for six steps and let go on the seventh. He had stopped struggling, which was clever, because struggling sinks you. He was standing perfectly still, in the fog, with his arms out. He was green about the face.",
    "They found him in clay up to the knees, in the middle of the neck, and the other boot was gone. The soil had held him for six steps and let go on the seventh. He had stopped struggling, which was clever, because struggling sinks you. He stood perfectly still in the fog, with his arms out, green about the face.")
cut("Nobody said anything for a long time.\n\nWalt sat down on the grass beside him. He was rubbing his bad leg, absently, in the way of a man who has done it for fifty years. “I know that neck,”",
    "Nobody said anything for a long time.\n\nWalt sat down on the grass beside him, rubbing his bad leg. “I know that neck,”")
cut("They ate Titch’s crusts, and apples, and a hard yellow cheese, and Walt’s stew, which was mostly turnip. Gucci lay with his chin on Hal’s knee, trying to look as though he was not watching the cheese. Dumpling stood behind them, chewing, with one ear turned toward the stream.",
    "They ate Titch’s crusts, and apples, and a hard yellow cheese, and Walt’s stew, which was mostly turnip. Gucci lay with his chin on Hal’s knee, trying to look as though he was not watching the cheese.")
cut("Nobody moved.\n\nHopsi’s face", "Nobody moved.\n\nHopsi’s face")
cut("They lay down in their blankets. They did not talk much. The stream sang on in the dark, “A shortcut is only…” and nobody slept, and nobody expected to.",
    "They lay down in their blankets. The stream sang on in the dark, “A shortcut is only…” and nobody slept, and nobody expected to.")
cut("The Falls were a wall of grey water, as high as a church, coming down from a lip of black rock into a pool that boiled white. The air around them was full of fine wet spray. It roared so loudly that a person could not hear himself think. And, under the roar, the hum went on.",
    "The Falls were a wall of grey water, as high as a church, coming down from a lip of black rock into a pool that boiled white. The air was full of fine wet spray, and the roar was so loud that a person could not hear himself think. Under it, the hum went on.")
cut("“Oh, does she,” said Titch, narrowing her eyes.\n\n“The cliff said so,” called Scally’s voice, with enormous innocence. “It’s a magic cliff. You have to pay.”\n\n",
    "“Oh, does she,” said Titch, narrowing her eyes.\n\n“The cliff said so,” called Scally’s voice, with enormous innocence. “It’s a magic cliff. You have to pay.”\n\n")
cut("It happened quickly. One minute there was a bright blue lid over the gorge. The next, a dark wall of cloud had slid over it from the west, and the spray at the Falls turned from white to grey, and the first big drops fell, one by one, with a thump, on the stones.",
    "It happened quickly. One minute there was a bright blue lid over the gorge. The next, a dark wall of cloud had slid over it from the west, and the first big drops fell, one by one, with a thump, on the stones.")
cut("There was a long, long silence, full of ringing.", "There was a long silence, full of ringing.")
cut("It was the longest minute of Hal’s life. The path up the side of the gorge was steep and slick with rain. Titch went first,",
    "It was the longest minute of Hal’s life. The path was steep and slick with rain. Titch went first,")
cut("The next minutes were a blur of brown water and shouting. Hal sat down hard on a boulder with the rope round his middle and dug in his heels. The rope ran down to Scally, who ran down the bank to the very edge of the rising water, where the path was already a river, and held out his hand.",
    "The next minutes were a blur of brown water and shouting. Hal sat down hard on a boulder with the rope round his middle and dug in his heels. Scally ran down the bank to the very edge of the rising water and held out his hand.")
cut("They watched the flood. It was brown and ugly and roaring, and it swept away the lower path, the place where they had been, the stones, the whole of the grass they had crossed that morning. Where the Falls had been a column, there was now a tower of foam. And far under the thunder,",
    "They watched the flood. It was brown and ugly and roaring, and it swept away the lower path and the whole of the grass they had crossed that morning. And far under the thunder,")
cut("It turned slowly, in one great smooth spiral, so slowly it seemed like a dream. In the centre there was a deep, dark funnel, and a faint sucking noise. From the whirl there rose a pale thin mist, shaped, if you did not look straight at it, like a very tall man in a long coat.",
    "It turned slowly, in one great smooth spiral. In the centre there was a deep, dark funnel, and a faint sucking noise. From the whirl rose a pale thin mist, shaped, if you did not look straight at it, like a very tall man in a long coat.")
cut("The water ran up the bank. It slapped at their feet. The stream, which had been talking quietly in the dark, roared. Fourpence flew up from Dumpling’s ear, singing four notes, wildly, and fluttered back.",
    "The water ran up the bank and slapped at their feet. The stream roared. Fourpence flew up from Dumpling’s ear, singing four notes, wildly, and fluttered back.")
cut("They held. Titch, on her stomach, with Gucci’s scruff in her fist, was sliding inch by inch to the edge. Hal, at the end of the line, felt the rope burn through his palms. His arms were turning to wood.",
    "They held. Titch, on her stomach, with Gucci’s scruff in her fist, was sliding inch by inch to the edge. Hal felt the rope burn through his palms.")
cut("Titch was wrapping Gucci in her coat. Tabitha held a canteen to Walt’s lips. Dumpling lay with her knees folded and her nose in Hal’s pocket, looking for the last apple. And Scally sat apart, with his arms round his knees and his hair in his eyes, as quiet as a stone.",
    "Titch was wrapping Gucci in her coat. Tabitha held a canteen to Walt’s lips. Dumpling lay with her nose in Hal’s pocket, looking for the last apple. And Scally sat apart, with his arms round his knees, as quiet as a stone.")
cut("“We went the long way round the bend,” said Hal. “Along the bank. Safe. We built a raft, and crossed the long way, with a rope. Safe. We climbed the Falls on the rope. Safe. We got through the bog on the green path, in single file, and nobody put a foot wrong.” He looked at his slate.",
    "“We went the long way round the bend,” said Hal. “We crossed the pool on a raft, with a rope. We climbed the Falls on the rope. We got through the bog on the green path, in single file. All safe.” He looked at his slate.")
cut("Tabitha said it again, half to herself, in her slow way. “A shortcut is only quicker if it works. If it doesn’t, you’re lost. And then it’s the slowest way of all.”\n\nThere was a long silence. The whirlpool went round in the dusk, turning, with its mist like a coat on a nail, and as they listened, it said, in a low, uncertain voice:",
    "Tabitha said it again, half to herself. “If it doesn’t, you’re lost. And then it’s the slowest way of all.”\n\nThere was a long silence. The whirlpool went round in the dusk, with its mist like a coat on a nail, and as they listened, it said, in a low, uncertain voice:")
cut("He had not spoken for a long time. He had sat with his chin on his knees, looking at his hands. He stood now, in his two socks, on the bank, with the wind in his black hair. He did not look clever. He did not look sly. He looked like a boy who has been very frightened, and has just been told it is all right, and has found out that it is true.",
    "He had not spoken for a long time. He stood now, in his two socks, on the bank, with the wind in his black hair. He did not look clever. He did not look sly. He looked like a boy who has been very frightened, and has just been told it is all right, and has found out that it is true.")
cut("Nobody was watching. Hopsi was away in the garden. Hal was inside.\n\n", "Nobody was watching.\n\n")
cut("They were nothing to do with him. They were not his. They were not for sale. He had found a penny in them, that was all, as he had found a penny in Mrs Crumb’s hands, and in the Mayor’s ten pounds, and in a box of moss. He held the brush for a long moment, dripping.",
    "They were not his, and they were not for sale. He had only found a penny in them, as he had in Mrs Crumb’s hands, and in the Mayor’s ten pounds, and in a box of moss. He held the brush for a long moment, dripping.")
cut("He set off down the lane, in the big brown boots, with the goose behind him, and did not look back. They watched him go. The long road bent, and the willow showed gold at the end of it. And above them, very slowly, the grey sky had begun to come down.\n\nHopsi had her head tilted back. She was looking at the cloud, and at the line of the hills, and at a small bird that was flying low over the mill roof. She had her needle in her hand, and a bowl of hops in her lap.\n\nShe was quiet for a while. Then she said it,",
    "He set off down the lane, in the big brown boots, with the goose behind him, and did not look back. The long road bent, and the willow showed gold at the end of it. And above them, very slowly, the grey sky had begun to come down.\n\nHopsi had her head tilted back, looking at the cloud, and at the line of the hills, and at a small bird flying low over the mill roof.\n\nShe was quiet for a while. Then she said it,")
cut("In the village, everybody slept soundly too, for the first time in weeks, and woke each morning rather surprised. Mrs Crumb’s buns came out golden.",
    "In the village, everybody slept soundly too, and woke each morning rather surprised. Mrs Crumb’s buns came out golden.")

open("Book2_Story_v6.txt", "w", encoding="utf-8").write(t)
print("missed:", miss)
print("words", n0, "->", len(t.split()))
bp = os.path.join(W, "build", "build_book2.py")
s = open(bp, encoding="utf-8").read().replace("Book2_Story_v5.txt", "Book2_Story_v6.txt")
open(bp, "w", encoding="utf-8").write(s)
