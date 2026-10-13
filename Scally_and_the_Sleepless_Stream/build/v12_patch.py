import os, shutil
W = r"C:\Users\lomus\git-dirs\wt-scallywag\Scally_and_the_Sleepless_Stream"
os.chdir(W)
shutil.copy(r"Step_Stories_Texts\Book2_Story_v11.txt", r"Step_Stories_Texts\Book2_Story_v12.txt")
t = open(r"Step_Stories_Texts\Book2_Story_v12.txt", encoding="utf-8").read()
Q = "\u201c"; R = "\u201d"; A = "\u2019"
miss = []


def sub(a, b, label):
    global t
    if t.count(a) == 1:
        t = t.replace(a, b, 1)
    else:
        miss.append((label, t.count(a)))


# Pip's password gag at the homecoming (Emil and Bullerby spirit)
sub(Q + "Good," + R + " said Titch, and found she had no crust left to give him, so she gave him a very long hug instead.",
    Q + "Good," + R + " said Titch, and found she had no crust left to give him, so she gave him a very long hug instead.\n\n"
    + Q + "Except the Mayor," + R + " Pip added, in a carrying voice. " + Q + "He did not know the word. I made him stand on one leg until Mrs Crumb told him." + R + "\n\n"
    "At the front of the crowd the Mayor went pink to the tips of his ears. " + Q + "It was," + R + " he said, with great dignity, " + Q + "a very good password." + R + "\n\n"
    + Q + "Marmalade," + R + " said Pip, with deep satisfaction.", "pip password")

# The walnut-boat picnic for Walt (Bullerby spirit; floating revisited)
sub("Old Walt took on an apprentice.",
    "On the last Sunday of October the village held a picnic on the bank for Old Walt, and it ended, as these things do, in a boat race. Every child made a boat from half a walnut shell, a matchstick mast and a leaf for a sail, and the whole valley lined up along the water to watch. Hal" + A + "s sank at once, because he had tested it with one pea too many, and he wrote WRONG on his slate and tried again with none. Titch" + A + "s went straight and fast, and Gucci jumped in after it. Pip entered a single wooden clog, and was disqualified, and was awarded a bun for effort. Scally" + A + "s boat won by a whole length, because Fourpence landed on the mast and sang.\n\n"
    + Q + "Is that cheating?" + R + " said Scally, before anybody could say it for him.\n\n"
    + Q + "I do not think so," + R + " said Hopsi, after a very long think. " + Q + "You did not ask the bird. It was luck. But next year we will write the rules down first." + R + "\n\n"
    "The Mayor, who had come to give out the prizes, stepped back to admire the winner and fell in up to the knees. Nobody dived in. Old Walt, who was sitting down, simply held out his pole without getting up. " + Q + "Reach," + R + " he said, " + Q + "not throw. The water is shallow and the Mayor is near." + R + "\n\n"
    "Old Walt took on an apprentice.", "boats")

open(r"Step_Stories_Texts\Book2_Story_v12.txt", "w", encoding="utf-8").write(t)
print("missed:", miss, "| words:", len(t.split()))

bp = r"build\build_book2.py"
s = open(bp, encoding="utf-8").read().replace("Book2_Story_v11", "Book2_Story_v12")
new = {
    "On the last Sunday of October the village held a picnic": "b83_walnut_boats.jpg",
    "Pip came out of the crowd like a cork": "b84_pip_homecoming.jpg",
}
i = s.index("place = {") + len("place = {\n")
s = s[:i] + "".join("    %r: %r,\n" % (a, b) for a, b in new.items()) + s[i:]
open(bp, "w", encoding="utf-8").write(s)
print("build patched")
