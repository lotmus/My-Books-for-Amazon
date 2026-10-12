import os, shutil
W = r"C:\Users\lomus\git-dirs\wt-scallywag\Scally_and_the_Sleepless_Stream"
os.chdir(os.path.join(W, "Step_Stories_Texts"))
shutil.copy("Book2_Story_v3.txt", "Book2_Story_v4.txt")
t = open("Book2_Story_v4.txt", encoding="utf-8").read()
Q = "\u201c"; R = "\u201d"; A = "\u2019"
miss = []


def sub(a, b, label):
    global t
    if a in t:
        t = t.replace(a, b, 1)
    else:
        miss.append(label)


# Hopsi can be wrong too
sub("He wrote on the slate, WRONG, in capitals.\n",
    "He wrote on the slate, WRONG, in capitals.\n\n" + Q + "I thought it would sink as well," + R + " said Hopsi. " + Q + "I was wrong too. That is what a test is for." + R + "\n", "hopsi wrong")

# the children work things out before Walt confirms
sub("\n\n" + Q + "Ah," + R + " said Walt, smiling slowly. " + Q + "That one" + A + "s fresh from the mountain.",
    "\n\nHal turned the two stones over in his hands. " + Q + "I think the round one has been rolled," + R + " he said. " + Q + "Like a biscuit crumb that has been in my pocket all week." + R + "\n\n" + Q + "Ah," + R + " said Walt, smiling slowly. " + Q + "You have it already. That one" + A + "s fresh from the mountain.", "hal guess")

# safe after the whirl: Titch did not go in
sub("Gucci was sodden, grey as a rat, and furious. He sneezed twice. Then he put his head in Titch" + A + "s lap and shook all over.",
    "Gucci was sodden, grey as a rat, and furious. He sneezed twice. Then he put his head in Titch" + A + "s lap and shook all over.\n\n" + Q + "You went to the very edge," + R + " said Walt, and his voice was not quite steady. " + Q + "That is the thing I told you never to do. You lay flat, you held on, and the others held you. That is the only reason this ended well. Next time, shout for the rope first, and let the rope go in, not you." + R + "\n\n" + Q + "I know," + R + " said Titch, very small. " + Q + "I did not think. He is my Gucci." + R + "\n\n" + Q + "That is a good reason," + R + " said Walt, " + Q + "and still not an excuse. But nobody is hurt, and we all know it now." + R + " Tabitha put her coat round Titch" + A + "s shoulders and sat there until the shaking stopped.", "whirl safe")

# flood: Walt also tells Scally the safe way
sub(Q + "She did," + R + " said Walt, " + Q + "and so did you." + R,
    Q + "She did," + R + " said Walt, " + Q + "and so did you. Next time, throw the rope and stay on the bank. But I thank you, and I mean it." + R, "flood safe")

# Slate intro: take your time
sub("Where Hopsi is not sure, she says, " + Q + "I think." + R,
    "Where Hopsi is not sure, she says, " + Q + "I think." + R + " You do not have to read them all at once: one a night is plenty.", "slate")

open("Book2_Story_v4.txt", "w", encoding="utf-8").write(t)
print("missed:", miss, "| words:", len(t.split()))

bp = os.path.join(W, "build", "build_book2.py")
s = open(bp, encoding="utf-8").read().replace("Book2_Story_v3.txt", "Book2_Story_v4.txt")
open(bp, "w", encoding="utf-8").write(s)
