import os, re, shutil
W = r"C:\Users\lomus\git-dirs\wt-scallywag\Scally_and_the_Hill_with_the_Hanging_Socks"
os.chdir(os.path.join(W, "Step_Stories_Texts"))
shutil.copy("Book3_Story_v7.txt", "Book3_Story_v8.txt")
t = open("Book3_Story_v8.txt", encoding="utf-8").read()
cut = t.index("Hal\u2019s Slate: What We Found Out")
body, tail = t[:cut], t[cut:]
miss = []


def sub(a, b, label):
    global body
    if body.count(a) == 1:
        body = body.replace(a, b, 1)
    else:
        miss.append((label, body.count(a)))


# 1. timeline: a year passes between Book 2 and Book 3
sub("The stream, which had hummed so loudly in the autumn and slept so peacefully since,", "The stream, which had hummed so loudly the autumn before and slept so peacefully ever since,", "stream")
sub("Pip had turned seven in the summer and mentioned it to everybody.", "Pip had turned seven in the spring and mentioned it to everybody.", "pip birthday")

# 2. trims in chapters 5 to 7
sub("There was a loud, relieved cheer. Several people clapped. A man at the back threw his brown hat into the air, and caught it, and put it on again.", "There was a loud, relieved cheer.", "cheer")
sub("\u201cEvery great cheese town in the world has a cave. Now we shall have one.\u201d", "", "cheese town") if False else None
a = "\u201cWell!\u201d said the Mayor at last. \u201cWell, well. That is a very interesting point.\u201d He went a rich, deep pink, from the collar up. \u201cI am a reasonable man. I am always open to correction. But I have a cellar to fill, and cheeses waiting, and I have announced it to the whole village.\u201d He looked round, and found that he was standing on a barrel in a brown paper hat, in front of two hundred people. He took it off, quite slowly."
sub(a, "\u201cWell!\u201d said the Mayor at last, going a deep pink from the collar up. \u201cI am a reasonable man, and always open to correction. But I have a cellar to fill, and I have announced it to the whole village.\u201d He found he was still wearing a brown paper hat, in front of two hundred people, and took it off slowly.", "mayor reply")
sub("A tuba is low. A whistle is high. A mouse squeak is higher. And above that,", "A tuba is low and a whistle is high. And above that,", "pitch")
sub(" Sound goes out. Sound comes back. And from the time between, you can tell what is there.\u201d", "\u201d", "sound goes out")

# 3. Tabitha and Titch get a moment that matters
sub("We counted all the bats in a square the size of a tablecloth, and then we measured how many tablecloths there were.", "Tabitha\u2019s gran counts seabirds on the cliffs this way, so Tabitha showed us. We counted all the bats in a square the size of a tablecloth, and then we measured how many tablecloths there were.", "tabitha count")
sub("\u201cYes, sir,\u201d said everybody.\n\nThe men went out", "\u201cYes, sir,\u201d said everybody. Titch tied the far end of the rope to the Mitchels\u2019 door post herself, with the knot she used for everything, and it held all night.\n\nThe men went out", "titch knot")

# 4. tighten the ending: Hopsi's speech
i = body.index("\u201cMr. Mayor,\u201d said a small, clear voice.")
j = body.index("Nobody breathed.", i) + len("Nobody breathed.")
body = body[:i] + "\u201cMr. Mayor,\u201d said a small, clear voice. It was Hopsi, standing very straight in front of the whole village. \u201cI have only ever said true things,\u201d she said, \u201cand I have never said I was proud of anyone, because I could not be sure. I am sure now.\u201d She looked along the row of faces. \u201cI am proud of every one of you.\u201d\n\nIt was the longest speech she had ever made. Nobody breathed." + body[j:]

# 5. tics: reduce 'very' and 'quite', vary repeated beats
body = re.sub(r"\bvery (quiet|small|long|slow|slowly|carefully|still|gently|softly|quietly|loud|clear|gentle|careful|close|calm|tired|tight|bright|cold|dark|fast|steady|serious|solemn|good|best|odd|strange|large)\b", lambda m: m.group(1), body, flags=re.I)
body = re.sub(r"\bquite (slowly|suddenly|calmly|still|gently|softly|quietly|steadily|carefully|firmly|helplessly|openly|plainly|clearly)\b", lambda m: m.group(1), body)
alts = ["Nobody spoke.", "Not a word.", "The room held still.", "Silence settled.", "No one answered."]
for phrase in ("Nobody said anything.", "Nobody said anything at all."):
    parts = body.split(phrase)
    out = parts[0]
    for k, p in enumerate(parts[1:]):
        out += (phrase if k == 0 else alts[(k - 1) % len(alts)]) + p
    body = out
for phrase in ("for a long moment", "for a very long moment"):
    parts = body.split(phrase)
    out = parts[0]
    for k, p in enumerate(parts[1:]):
        out += (phrase if k % 3 == 0 else ["for a while", "for a beat", "for a time"][k % 3 - 1]) + p
    body = out

open("Book3_Story_v8.txt", "w", encoding="utf-8").write(body + tail)
print("missed:", miss)
print("words", len((body + tail).split()), "(was", len(t.split()), ")")
bp = os.path.join(W, "build", "make_build_book3.py")
print("anchors need regenerating: run b3_pics.py plan not needed (plan keys unchanged unless paragraphs changed)")
