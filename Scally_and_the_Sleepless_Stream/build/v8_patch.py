import os, shutil
W = r"C:\Users\lomus\git-dirs\wt-scallywag\Scally_and_the_Sleepless_Stream"
os.chdir(os.path.join(W, "Step_Stories_Texts"))
shutil.copy("Book2_Story_v7.txt", "Book2_Story_v8.txt")
t = open("Book2_Story_v8.txt", encoding="utf-8").read()
miss = []


def sub(a, b, label):
    global t
    if a in t:
        t = t.replace(a, b, 1)
    else:
        miss.append(label)


# 1a. the echo trick backfires: Titch outwits Scally
i = t.index("“Scally,” said Hopsi, without moving.\n\n“Yes, Hop?”")
j = t.index("“That’s the first sensible thing you’ve said this week,” said Titch.") + len("“That’s the first sensible thing you’ve said this week,” said Titch.")
t = t[:i] + (
    "Titch said nothing at all. She walked round a different rock, out of sight, cupped her hands and took a deep breath. “SCALLY OWES TITCH TWO CRUSTS!”\n\n"
    "There was a pause. “Scally owes Titch two crusts… crusts… crusts,” said the cliff, in a voice that was most definitely not the cliff’s, and rather better than his.\n\n"
    "“That’s not fair!” said Scally, coming out with a crust-shaped hole in the air where his plan had been.\n\n"
    "“The cliff said so,” said Titch. “It’s a magic cliff. You have to pay.” She held out her hand, and after a long moment, grinning in spite of himself, he put two crusts in it.\n\n"
    "“It was a good trick,” said Scally. “Yours was better. Mine was only a trick. Yours was funny.”\n\n"
    "“A cliff can only say what you say,” said Hopsi to Hal, who was watching with his mouth open. “It repeats. It cannot make anything up.”"
) + t[j:]

# 1b. Tabitha asks the question about the box; Titch spots the apple swap
sub("It was Hopsi, behind him. She had not said a word, but she had heard. She was not looking cross. She was looking at him with a sort of patient interest.\n\n“What happens to the ten pounds,” she said, “when the hum is still there?”",
    "It was Tabitha, behind him. She had not said a word, but she had heard. She was not looking cross. She was looking at him with a sort of patient interest.\n\n“What happens to the ten pounds,” she said, “when the hum is still there?”", "tabitha asks")
sub("“Yes,” said Hopsi.\n\n“Right,” said Scally. “Forget the box.”\n\n“I thought you might,” said Hopsi, and went back to her hops.",
    "“Yes,” said Tabitha.\n\n“Right,” said Scally. “Forget the box.”\n\n“I thought you might,” said Tabitha, and went back to counting the hum.", "tabitha end")
sub("She had been listening with one eyebrow up. Hopsi, on her stone, was not looking at anything. And when Scally went to the water’s edge with something red in his fist and a small, thoughtful smile, she said, in her ordinary voice, without turning her head, “That is not Tabitha’s apple.”",
    "She had been listening with one eyebrow up, and she had watched Scally’s hands the whole time. When he went to the water’s edge with something red in his fist and a small, thoughtful smile, she said, in her ordinary voice, “That is not Tabitha’s apple. I saw you swap it.”", "titch sees")
sub("“It is a stone,” said Hopsi, “painted red. You swapped it behind your back. It is going to sink, and you are going to win a penny,",
    "“It is a stone, painted red,” said Titch. “He swapped it behind his back.”\n\n“It is going to sink,” said Hopsi, from her stone, “and you are going to win a penny,", "stone")
sub("“You always know.”\n\n“I only say what I see,” said Hopsi. “You did the rest.”",
    "“Somebody always catches me.”\n\n“Titch did,” said Hopsi. “I only asked what you had won. You did the rest.”", "somebody catches")

# 3. the ending is an idea about evidence, not a proverb
sub("“Shortcuts that worked: none. I’ve looked, and I can’t find one.”",
    "“Shortcuts that worked: none. Four tries is not many, so I cannot say never. But I have looked, and I can’t find one.”", "hal data")
sub("“I think,” said Scally, “that the long way always gets you home.”",
    "“I think,” said Scally, “that when you can’t tell if a shortcut works, you should take the way you can check.”", "scally line")
sub("“A shortcut is only quicker if it works. And the long way always gets you home.”",
    "“A shortcut is only quicker if it works. And if you can’t tell, take the way you can check.”", "scally repeat")
sub("15. A shortcut is only quicker if it works. Hal looked at all the shortcuts on the journey and found that none had saved time. That is data. A scientist looks, counts, tests, and says, “I think.”",
    "15. A shortcut is only quicker if it works. Hal looked at all the shortcuts on the journey and found that none had saved time. That is data, but four tries is a small sample, so a scientist says “I think” and not “always”. If you cannot tell whether a shortcut works, take the way you can check.", "slate 15")

# 4. a quiet, funny moment between the storm and the flood
sub("The sun came out with a bang, and the whole gorge steamed like a boiled pudding.",
    "The sun came out with a bang, and the whole gorge steamed like a boiled pudding. For a minute it was almost funny. Dumpling sat down in a puddle and refused to get up. Gucci shook himself all over Walt, who said it was the first bath he had had since spring. Titch wrung out Tabitha’s plait like a dishcloth, and Scally, who had a whole oak leaf stuck to his forehead, announced that he was now an official stream-keeper.", "funny")

# 6. why the children can walk on no sleep
sub("All morning the stream hummed beside them, louder than in the night.",
    "Nobody had slept for three nights, and yet nobody fell asleep on the path, which Hopsi thought was the strangest part. Walt said the hum kept you awake the way a hand keeps a kite up, that it was no kindness, and that it would not last. All morning the stream hummed beside them, louder than in the night.", "sleep")

# 5. the mirror-world tease gets a small answer
sub("“It stopped saying UP,” said Hal.\n\n“It’s got where it wanted to go,” said Tabitha.",
    "“It stopped saying UP,” said Hal.\n\nFar behind his reflection, very faintly, a second mill turned the wrong way round, and a thin old man in a flour-sack cloak, with his hat on straight, touched it to the pond and was gone. Hal did not say anything. It seemed like a thing to keep.\n\n“It’s got where it wanted to go,” said Tabitha.", "mirror")

# slate: the hum is magic
sub("16. “I think” is a scientist’s sentence.",
    "16. The hum is magic. No real stream hums like that, though real streams do make many sounds, from a gurgle over stones to a roar in a flood.\n\n17. “I think” is a scientist’s sentence.", "slate 16")

open("Book2_Story_v8.txt", "w", encoding="utf-8").write(t)
print("missed:", miss, "| words:", len(t.split()))

bp = os.path.join(W, "build", "build_book2.py")
s = open(bp, encoding="utf-8").read().replace("Book2_Story_v7.txt", "Book2_Story_v8.txt")
open(bp, "w", encoding="utf-8").write(s)
