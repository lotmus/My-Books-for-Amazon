import os, shutil
W = r"C:\Users\lomus\git-dirs\wt-scallywag\The_Wee_Scallywag_and_the_Gentle_Elf"
os.chdir(os.path.join(W, "Step_Stories_Texts"))
shutil.copy("Book1_Story_v10.txt", "Book1_Story_v11.txt")
t = open("Book1_Story_v11.txt", encoding="utf-8").read()
Q = "\u201c"; R = "\u201d"
miss = []
def sub(a, b, l):
    global t
    if a in t: t = t.replace(a, b, 1)
    else: miss.append(l)
sub(Q + "Give me my bag," + R + " it said, but not so softly now.",
    Q + "Give me my bag," + R + " it said, but not so softly now.\n\nThe pond went dark. The ghost" + "\u2019" + "s lantern guttered and went out, and in the black the voice came up through the water, as cold as a cellar. " + Q + "Boots, Sparefunk. Proper ones, that go where you like. Only give me the bag." + R + "\n\nScally" + "\u2019" + "s arms tightened round it. Everyone heard the little clink of the sweets inside. Nobody breathed.\n\n" + Q + "He tells you what you want," + R + " said Hopsi, very steadily, " + Q + "so that you will forget what he wants." + R + "\n\nScally shut his eyes. " + Q + "I want to stay," + R + " he said, and the lantern flared back on.", "dark")
sub("Nobody heard the end of the sentence. The fog went with it. The air smelled faintly of boiled sweets for about a minute, and then of rain.",
    "Nobody heard the end of the sentence. The fog went with it. The air smelled faintly of boiled sweets for about a minute, and then of rain.\n\nNobody was hurt. Titch" + "\u2019" + "s knees shook for a good while, and Tabitha held her hand until they stopped. " + Q + "Being frightened is not the same as being wrong," + R + " said Hopsi. " + Q + "You were frightened, and you said no anyway. That is what brave is." + R, "after")
open("Book1_Story_v11.txt", "w", encoding="utf-8").write(t)
print("missed", miss)
bp = os.path.join(W, "build", "build_docx.py")
s = open(bp, encoding="utf-8").read().replace("Book1_Story_v10.txt", "Book1_Story_v11.txt")
open(bp, "w", encoding="utf-8").write(s)
