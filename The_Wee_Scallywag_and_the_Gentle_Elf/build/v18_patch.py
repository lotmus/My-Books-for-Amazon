import os, shutil
W = r"C:\Users\lomus\git-dirs\wt-scallywag\The_Wee_Scallywag_and_the_Gentle_Elf"
os.chdir(W)
shutil.copy(r"Step_Stories_Texts\Book1_Story_v17.txt", r"Step_Stories_Texts\Book1_Story_v18.txt")
t = open(r"Step_Stories_Texts\Book1_Story_v18.txt", encoding="utf-8").read()
Q = "\u201c"; R = "\u201d"; A = "\u2019"
miss = []


def sub(a, b, label):
    global t
    if t.count(a) == 1:
        t = t.replace(a, b, 1)
    else:
        miss.append((label, t.count(a)))


# ---- Emil spirit: the butter on the wheel (chapter 2) ----
sub("That evening Hal tried the wheel.",
    "Scally decided to help. He did not say so. He slipped away to Mrs Crumb" + A + "s cool shed, " + Q + "borrowed" + R + " her best crock of butter, and spent the afternoon smearing it on the wheel, the rim, the step and, by accident, himself. " + Q + "It will go easier," + R + " he said, " + Q + "if it is slippery." + R + "\n\n"
    "The wheel did not move. But the step, the yard and the gatepost were now as slippery as a pond in winter. Titch came out with a crust held high, sat down hard, and slid on her bottom halfway to the gate, shrieking with laughter. Hal reached for the wheel and his hand skated straight off it.\n\n"
    + Q + "When two things rub, they pull against each other," + R + " said Hopsi, who had not slipped, because she had looked first. " + Q + "That pull is called friction. Butter makes it smaller, so a squeaky wheel turns more easily. But this wheel is not stuck because it rubs. It is stuck because something is in the way, and butter cannot move that." + R + "\n\n"
    + Q + "So butter is for squeaks," + R + " wrote Hal, " + Q + "and not for jams." + R + "\n\n"
    "Scally spent the rest of the afternoon scrubbing the steps with sand until they squeaked, and Mrs Crumb" + A + "s crock went back to her shed empty, with a message in chalk on the lid: SORRY. I OWE YOU A CROCK. SCALLY. It was the first time he had ever paid for anything, and he did not like how it felt, and he did it anyway.\n\n"
    "That evening Hal tried the wheel.", "butter")

# ---- Bullerby spirit and Pippi spirit: the night in the loft (chapter 8) ----
sub("Later, while Hal paced and Titch counted crusts,",
    "The night before had been the kind you only get once. All of them had slept in the mill loft, in a nest of old sacks, with a lantern turned low and the rain ticking on the roof, and nobody wanted to be the first to sleep. Titch told them that her little brother Pip, who was six, slept with his boots on in case of adventures, and had once been found in the morning wearing the dog. Hal read out a page of his slate where he had written " + Q + "Acceptable" + R + " beside everything. Hopsi told a story, and it was very short, because it was true. " + Q + "Once there was a hop. It grew. That is all, but it was a very good hop." + R + "\n\n"
    "Then Scally sat up with the lantern under his chin. " + Q + "I once ran so fast," + R + " he said, " + Q + "that my shadow got left behind and took three days to catch up. It arrived out of breath, and it had eaten my supper." + R + "\n\n"
    + Q + "That is not true," + R + " said Hopsi.\n\n"
    + Q + "Of course it is not," + R + " said Scally. " + Q + "It is a story." + R + "\n\n"
    "Hopsi thought about that for a long moment. " + Q + "A lie is when you want somebody to believe it," + R + " she said slowly. " + Q + "A story is when everybody knows. I like stories. Tell it again, with the supper." + R + "\n\n"
    "He told it again, with a larger supper, and by the end Titch was crying with laughter, and Gucci had lifted his head to see what the noise was, and Tabitha, on her sacks, had her chin on her knees and her eyes going from face to face, as if she were memorising them. She did not say anything. She did not laugh, not yet. But she did not go to sleep until the lantern did.\n\n"
    "Later, while Hal paced and Titch counted crusts,", "loft")

# ---- True Things: friction ----
sub("Real scientists say it every day, and then they go and find out.",
    "Real scientists say it every day, and then they go and find out.\n\n16. Friction. When two things rub, they pull against each other. That is why your shoes grip and why a slide gets faster when you wax it. Grease makes friction smaller, so it cures a squeak but not a jam. Try it: slide a book across a table, then across a tea towel, then across a sheet of baking paper, and see which is easiest.", "friction")

open(r"Step_Stories_Texts\Book1_Story_v18.txt", "w", encoding="utf-8").write(t)
print("missed:", miss, "| words:", len(t.split()))

bp = r"build\build_docx.py"
s = open(bp, encoding="utf-8").read()
s = s.replace("Book1_Story_v17", "Book1_Story_v18")
k = "    (15, 'That counts'),\n"
assert k in s
s = s.replace(k, k + "    (16, 'When two things rub, they pull against each other'),\n", 1)
k2 = "    'That evening Hal tried the wheel.': 'd02_jamming_the_wheel.jpg',"
assert k2 in s, "place d02"
s = s.replace(k2, "    'Scally decided to help.': 'c02e_butter_slip.jpg',\n" + k2, 1)
k3 = "    'Later, while Hal paced"
if k3 in s:
    pass
s = s.replace("    'She had slept on a pile of sacks", "    'The night before had been the kind you only get once.': 'c08a_loft_stories.jpg',\n    'She had slept on a pile of sacks", 1)
a = "levers, with a seesaw, a fair test, why a trick catches up with you, and why a rainbow needs the sun behind you."
assert a in s
s = s.replace(a, "levers, with a seesaw, a fair test, friction (butter cures a squeak, not a jam), why a trick catches up with you, and why a rainbow needs the sun behind you.", 1)
b = "welcome when the words are not allowed, careful observation, and tides: how the Moon pulls the sea."
assert b in s
s = s.replace(b, "welcome when the words are not allowed, careful observation, the difference between a story and a lie, and tides: how the Moon pulls the sea.", 1)
c = "lever, rainbow, inherit,"
assert c in s
s = s.replace(c, "lever, friction, rainbow, inherit,", 1)
open(bp, "w", encoding="utf-8").write(s)
print("build patched")
