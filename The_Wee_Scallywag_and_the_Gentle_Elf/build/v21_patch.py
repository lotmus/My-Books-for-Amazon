import os, re, shutil
W = r"C:\Users\lomus\git-dirs\wt-book1\The_Wee_Scallywag_and_the_Gentle_Elf"
os.chdir(W)
shutil.copy(r"Step_Stories_Texts\Book1_Story_v20.txt", r"Step_Stories_Texts\Book1_Story_v21.txt")
t = open(r"Step_Stories_Texts\Book1_Story_v21.txt", encoding="utf-8").read()
cut = t.index("Hopsi\u2019s True Things")
body, tail = t[:cut], t[cut:]
A = "\u2019"; Q = "\u201c"; R = "\u201d"
miss = []


def sub(a, b, label):
    global body
    if body.count(a) == 1:
        body = body.replace(a, b, 1)
    else:
        miss.append((label, body.count(a)))


# ---- continuity: days, the mother, sleeping places ----
sub("His mother had gone to the village to borrow flour, and had left Hal in charge of the step.",
    "His mother had gone to her sister" + A + "s, two villages over, to borrow flour, and would not be back until Sunday, and she had left Hal in charge of the step.", "mother away")
sub("Next morning two messengers in blue and purple coats", "That afternoon two messengers in blue and purple coats", "ch2 opening")
sub(Q + "I have, Father," + R + " said Hal.", Q + "I am telling them, Father," + R + " said Hal.", "ch2 father")
sub("hung it on the door where his mother would see it:", "hung it on the door where anyone would see it:", "slate door")
sub("Mrs. Crumb gave everyone a bun, and walked them all the way back to the mill.", "Mrs. Crumb gave everyone a bun, walked them all the way back to the mill, and stayed to look after the miller" + A + "s kitchen until his wife came home.", "crumb stays")
sub("Behind him came Hal" + A + "s mother with a basket,", "Behind him came Hal" + A + "s mother, home early from her sister" + A + "s, with a basket,", "mother returns")
sub("And you may sleep on the sacks by the stove.", "And you may sleep on the sacks in the loft with the others.", "loft sleep")
sub("listening to the stove tick. When he slept, he dreamed that every single person he knew was standing safely outside.",
    "listening to the rain tick on the roof. When he slept, he dreamed that every single person he knew was standing safely outside. It was the second night. Tomorrow at midnight the third day would close, and nobody knew the name.", "second night")
sub("They went in single file, in pairs, with the lantern in front,", "They went in single file, with the lantern in front,", "single file")
sub("Then I got here, and Hal pushed the porridge across.", "I jammed it on Monday, and I did not mean your father to fall. I hid. Then on Thursday I came back to see whether you were selling, and Hal pushed the porridge across.", "monday jam")
sub("Scally came out of the dark at a run, shrieked with delight, and chased the ghost twice round the mill.",
    "Scally came out of the dark at a run, with Titch, who had been invited to sleep on the sacks and had decided it was an adventure, close behind. He shrieked with delight, and chased the ghost twice around the mill.", "titch at night")
sub("Sparefunk got up with the bird still on his head", "Scally got up with the bird still on his head", "name end 1")
sub(Q + "It" + A + "s on me," + R + " said Sparefunk, with great dignity", Q + "It" + A + "s on me," + R + " said Scally, with great dignity", "name end 2")
sub("sat down on Sparefunk" + A + "s head, and stayed there.", "sat down on Scally" + A + "s head, and stayed there.", "name end 3")

# ---- plant the warning rhyme ----
sub("He did not say so. He slipped away to Mrs. Crumb", "He did not say so. He hummed under his breath, a little tune with words in it: Just a little, just a bit, who will ever notice it? Then he slipped away to Mrs. Crumb", "hum butter")
sub("Then he had an idea. He picked up a round brown stone,", "Then he had an idea, and hummed, under his breath: Just a little, just a bit, who will ever notice it? He picked up a round brown stone,", "hum toad")
sub("Nobody noticed that he had his fingers crossed behind his back.", "Nobody noticed that he had his fingers crossed behind his back. Nobody except Hopsi, who heard him humming.", "hum fire")

# ---- setup for the fire payoff, and a livelier pike ----
sub(Q + "Somebody must put the fire out," + R + " said Hopsi, when the pike was gone.", Q + "Fire needs fuel, heat and air," + R + " said Hopsi, when the pike was gone. " + Q + "Take one away and it goes out. Somebody must put this one out." + R, "fire setup")
sub("They caught the pike at dusk. Titch threw her cloth over its head,", "The pike was cleverer than any of them. It took Hal" + A + "s bait three times and gave it back each time with a look of deep disappointment, as if it had been served cold soup. At dusk Titch lost patience, threw her cloth over its head,", "pike clever")
sub("and landed on Scally. They roasted it", "and landed on Scally. It looked at him. He looked at it. " + Q + "I am sorry," + R + " said Scally, to the pike, which seemed only fair. They roasted it", "pike sorry")

# ---- the king's men ----
sub(Q + "It is a great deal of flour," + R + " said the second, " + Q + "for a boy." + R + " They stamped a paper, and nobody was mad at all,",
    Q + "It is a great deal of flour," + R + " said the second, " + Q + "for a boy." + R + " " + Q + "And whom shall we tell the king made it?" + R + " asked the first, writing. " + Q + "The wheel," + R + " said Hal. They wrote that down, since it was the only honest answer, and it was the first time the king" + A + "s men had ever heard of a mill taking the credit. They stamped the paper, and nobody was mad at all,", "king's men")

# ---- American spelling and words ----
for a, b in (("tunnelling", "tunneling"), ("Tunnelling", "Tunneling"), ("moustache", "mustache"),
             ("twice round the mill", "twice around the mill"), ("the wrong way round", "the wrong way around"),
             ("which Titch said was unnatural", "which Titch said was unnatural")):
    body = body.replace(a, b)
body = re.sub(r"\bround (by the firm path|the corner|the long way)\b", lambda m: "around " + m.group(1), body)
body = re.sub(r"\bswings round\b", "swings around", body)
body = re.sub(r"\bturned round\b", "turned around", body)
body = re.sub(r"\barms round it\b", "arms around it", body)
tail = tail.replace("Tunnelling", "Tunneling").replace("tunnelling", "tunneling")

# ---- tics ----
body = re.sub(r"\bvery (quiet|small|long|slow|slowly|carefully|still|gently|softly|quietly|loud|clear|gentle|careful|close|calm|tired|tight|bright|cold|dark|fast|steady|serious|solemn|odd|strange|large)\b", lambda m: m.group(1), body, flags=re.I)
body = re.sub(r"\bquite (slowly|suddenly|calmly|still|gently|softly|quietly|steadily|carefully|firmly|helplessly|openly|plainly|clearly)\b", lambda m: m.group(1), body)
for phrase, alts in (("for a long moment", ["for a while", "for a beat", "for a time"]),):
    parts = body.split(phrase)
    out = parts[0]
    for k, p in enumerate(parts[1:]):
        out += (phrase if k % 3 == 0 else alts[k % 3 - 1]) + p
    body = out

open(r"Step_Stories_Texts\Book1_Story_v21.txt", "w", encoding="utf-8").write(body + tail)
print("missed:", miss)
print("words", len((body + tail).split()), "(was", len(t.split()), ")")

# ---- build script ----
bp = r"build\build_docx.py"
s = open(bp, encoding="utf-8").read()
s = s.replace("Book1_Story_v20", "Book1_Story_v21")
for a, b in (("tunnelling", "tunneling"), ("Tunnelling", "Tunneling"), ("moustache", "mustache")):
    s = s.replace(a, b)
a = '"Next morning two messengers"'
if a in s:
    s = s.replace(a, '"That afternoon two messengers"')
elif "Next morning two messengers" in s:
    s = s.replace("Next morning two messengers", "That afternoon two messengers")
else:
    print("anchor key for messengers not found")
k = 'centered(AUTHOR, 18)\npagebreak()\nheading("Contents", 1, "toc")'
if k in s:
    s = s.replace(k, 'centered(AUTHOR, 18, after=30)\ncentered("For everyone who has ever called a stone a fly.", 13, italic=True)\npagebreak()\nheading("Contents", 1, "toc")', 1)
else:
    print("dedication spot not found")
open(bp, "w", encoding="utf-8").write(s)
print("build patched")
