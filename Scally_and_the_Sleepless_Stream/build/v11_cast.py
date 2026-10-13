import os, shutil
R = r"C:\Users\lomus\git-dirs\wt-scallywag"
B1 = os.path.join(R, "The_Wee_Scallywag_and_the_Gentle_Elf")
B2 = os.path.join(R, "Scally_and_the_Sleepless_Stream")
A = "\u2019"; Q = "\u201c"; QQ = "\u201d"


def edit(path, pairs, dst=None):
    t = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert t.count(a) == 1, (path, a[:50], t.count(a))
        t = t.replace(a, b, 1)
    open(dst or path, "w", encoding="utf-8").write(t)


# ---- Book 1 v17 ----
edit(os.path.join(B1, "Step_Stories_Texts", "Book1_Story_v16.txt"), [
    ("and behind her Mrs Crumb the baker and half the village with empty sacks.",
     "and behind her Mrs Crumb the baker and half the village with empty sacks. In front of the crowd, holding Titch" + A + "s hand, was a small boy of six with a crust in each fist: her little brother Pip, who had been told to stay at home and had not."),
], os.path.join(B1, "Step_Stories_Texts", "Book1_Story_v17.txt"))
edit(os.path.join(B1, "build", "build_docx.py"), [
    ('("Hopsi (Elfie Didlhop)", "9. An elf:', '("Hopsi (Elfie Didlhop)", "An elf:'),
    ('("Tabitha Smoke", "8. Curly black hair', '("Tabitha Smoke", "7. Curly black hair'),
    ('    ("Gucci", "A baby wolf with a grumpy face', '    ("Pip", "6. Titch\\u2019s little brother. Small, solemn and always one step behind his sister."),\n    ("Gucci", "A baby wolf with a grumpy face'),
    ("Book1_Story_v16", "Book1_Story_v17"),
])

# ---- Book 2 v11 ----
edit(os.path.join(B2, "Step_Stories_Texts", "Book2_Story_v10.txt"), [
    ("Tabitha Smoke sat with her chin on her knees,", "Tabitha Smoke, nearly eight, sat with her chin on her knees,"),
    ("Before they left, Walt gave out his own rules,",
     "Titch" + A + "s little brother Pip, who was six and three-quarters, had planted himself in front of the donkey with his arms folded. " + Q + "I am coming too," + QQ + " he said.\n\n" + Q + "Six is too small for a bog," + QQ + " said Titch, and crouched, and gave him her last crust and the most important job she could think of. " + Q + "Guard the step. Somebody has to." + QQ + "\n\nPip thought about it, and sat on the step, with the crust, and guarded it.\n\nBefore they left, Walt gave out his own rules,"),
    ("That night every light in the valley went out early",
     "Pip came out of the crowd like a cork out of a bottle and wrapped himself round Titch" + A + "s middle. " + Q + "I guarded the step," + QQ + " he said. " + Q + "Three whole days. Nothing came." + QQ + "\n\n" + Q + "Good," + QQ + " said Titch, and found she had no crust left to give him, so she gave him a very long hug instead.\n\nThat night every light in the valley went out early"),
], os.path.join(B2, "Step_Stories_Texts", "Book2_Story_v11.txt"))
edit(os.path.join(B2, "build", "build_book2.py"), [
    ('"8 and a bit. The miller" + A + "s son,', '"Almost 9. The miller" + A + "s son,'),
    ('("Scally, the wee scallywag", "8. A little devil', '("Scally, the wee scallywag", "A little devil'),
    ('("Hopsi (Elfie Didlhop)", "9. An elf', '("Hopsi (Elfie Didlhop)", "An elf'),
    ('("Titch Mitchel", "8. Red cap', '("Titch Mitchel", "Almost 9. Red cap'),
    ('("Tabitha Smoke", "8. Curly black hair', '("Tabitha Smoke", "Nearly 8. Curly black hair'),
    ('    ("Gucci", "A wolf cub, now', '    ("Pip", "6 and three-quarters. Titch" + A + "s little brother, who guards the mill step while the others are away."),\n    ("Gucci", "A wolf cub, now'),
    ("Book2_Story_v10", "Book2_Story_v11"),
])
print("ok")
