from pathlib import Path
import subprocess, sys

pairs = [
(
Path(r"D:\My Books for Amazon\Science Books\Look First\A Trip Is Not a Settlement - Manuscript\02_Part_Two_The_Moon_First.md"),
[
(
"Rohan, on the other side of Mara’s tin, used to work payloads. He is invented. He still flinches",
"Rohan, on the other side of Mara’s tin, used to work payloads. He still flinches",
),
(
"Suit gloves have a designer who is invented. The dust is not. She has a box of lunar simulant that is not the Moon and is still rude to bearings. She can tell you, at a table, why a glove that works in a clean room fails after an hour of glass. She is the long pole that photographs badly.",
"Suit gloves have a designer. The dust is not invented. A box of lunar simulant that is not the Moon is still rude to bearings. A clean-room glove fails after an hour of glass. That failure is the long pole that photographs badly.",
),
(
"Nandita Rao drafts the fight for a living. She is invented. She has a wall of versions. Version 3 had a habitat the size of a bus. Version 6 shrank it. Version 8 added a partner’s module that then slipped a year. Version 9 asked whether the landing needed the handshake. She does not hate any version. She hates the sentence “the architecture is settled.” Settled is what you say about a house you are no longer allowed to improve. Camps should not be settled. Camps should be honest about being camps.",
"The station fight has a wall of versions. Version 3 had a habitat the size of a bus. Version 6 shrank it. Version 8 added a partner’s module that then slipped a year. Version 9 asked whether the landing needed the handshake. Nobody hates any version. Everybody should hate the sentence “the architecture is settled.” Settled is what you say about a house you are no longer allowed to improve. Camps should not be settled. Camps should be honest about being camps.",
),
],
),
(
Path(r"D:\My Books for Amazon\Science Books\Look First\A Trip Is Not a Settlement - Manuscript\04_Part_Four_Who_Stays.md"),
[
(
"Rohan’s mother lives in a city that floods in the ugly years. She is invented. The flood is not a metaphor.",
"Rohan’s mother lives in a city that floods in the ugly years. The flood is not a metaphor.",
),
],
),
(
Path(r"D:\My Books for Amazon\Science Books\Look First\A Trip Is Not a Settlement - Manuscript\01_Part_One_Dirt_Delay_Dates.md"),
[
(
"Tom Brennan writes dates for a living. He is invented. His job is real and has a nicer name on the org chart. He sits in the review lead’s reviews with a spreadsheet that has three columns: *announced*, *internal*, *what I would bet*. He is not allowed to show the third column. The third column is why he still has a conscience.",
"Dates get written for a living. The job is real and has a nicer name on the org chart. The review has a spreadsheet with three columns: *announced*, *internal*, *what I would bet*. The third column is not allowed on the screen. The third column is why a conscience still fits in the room.",
),
],
),
]

n = 0
for p, reps in pairs:
    t = p.read_text(encoding="utf-8")
    for a, b in reps:
        if a in t:
            t = t.replace(a, b)
            n += 1
            print("ok", p.name)
        else:
            print("MISS", p.name, repr(a[:60]))
    p.write_text(t, encoding="utf-8", newline="\n")
print("done", n)
r = subprocess.run(
    [
        sys.executable,
        r"D:\My Books for Amazon\Science Books\Look First\A Trip Is Not a Settlement - Manuscript\Figures\build_book.py",
        "permit",
    ],
    capture_output=True,
    text=True,
)
print(r.stdout)
print(r.stderr)
