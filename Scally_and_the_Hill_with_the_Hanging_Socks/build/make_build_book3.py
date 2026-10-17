"""Generate build_book3.py from the Book 2 build script (same layout), with Book 3 text and the picture plan."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(os.path.dirname(HERE)), "Scally_and_the_Sleepless_Stream", "build", "build_book2.py")
s = open(SRC, encoding="utf-8").read()


def rep(a, b, count=1):
    global s
    assert a in s, a[:60]
    s = s.replace(a, b, count)


rep('TITLE1, TITLE2 = "Scally and the", "Sleepless Stream"', 'TITLE1, TITLE2 = "Scally and the Hill", "with the Hanging Socks"')
rep('FULL = "Scally and the Sleepless Stream"', 'FULL = "Scally and the Hill with the Hanging Socks"')
m = re.search(r'STORY_FILE = "Book2_Story_v\d+\.txt"', s)
STORY = sorted(f for f in os.listdir(os.path.join(os.path.dirname(HERE), "Step_Stories_Texts")) if f.endswith(".txt"))[-1]
s = s.replace(m.group(0), 'STORY_FILE = "%s"' % STORY)
rep('"Book 2 of " + SERIES', '"Book 3 of " + SERIES')
rep('Scally_and_the_Sleepless_Stream_Book2_%s.docx', 'Scally_and_the_Hill_with_the_Hanging_Socks_Book3_%s.docx')

# picture anchors from the plan (plus any manual overrides in b3_anchors_extra.json)
plan = json.load(open(os.path.join(HERE, "b3_plan.json"), encoding="utf-8"))
P = os.path.join(os.path.dirname(HERE), "Step_Stories_Pics_Final")
lines = []
for e in plan:
    f = "p%03d_ch%02d.jpg" % (e["n"], e["chap"])
    if os.path.exists(os.path.join(P, f)):
        lines.append("    %r: %r," % (e["key"], f))
i = s.index("place = {")
j = s.index("\n}\n", i) + 3
s = s[:i] + "place = {\n" + "\n".join(lines) + "\n}\n" + s[j:]

# cast
i = s.index("cast = [")
j = s.index("]\nfor n, t in cast:")
cast = '''cast = [
    ("Hal (Halbert) Millersen", "9 and a half. The miller" + A + "s son, with a slate for his notes. Says " + Q + "Acceptable" + R + " when things are bad, and is learning other words."),
    ("Scally, the wee scallywag", "A little devil with pointed ears and a leaf in his hair. He hums a little tune before every trick. His true name is for special occasions."),
    ("Hopsi (Elfie Didlhop)", "An elf with long swept-back ears. She only says what is true, and says so out loud when she is wrong."),
    ("Titch Mitchel", "9 and a half. Red cap, quick fingers and a rope always over her shoulder."),
    ("Tabitha Smoke", "8 and a half. Curly black hair in a bun. Watches carefully and knows her gran" + A + "s stories about the sea."),
    ("Wen Liang", "About 9. New in the village. A careful boy who mends clocks, measures ice, and does not like the dark."),
    ("Dr. Liang", "Wen" + A + "s mother, the new village doctor. Brisk, kind, funny, and never without her black bag."),
    ("Pip", "7 and a half. Titch" + A + "s little brother. He is sure that anything can be tried once."),
    ("Gucci", "A young wolf, now the size of an armchair, who hears things nobody else can."),
    ("Mayor Pomfrey", "The village mayor, with a gold chain, a big mustache and a great love of cheese."),
    ("Mrs. Crumb", "The baker. She has helped half the village into the world."),
    ("Fourpence", "A small brown bird who sings five notes now."),
'''
s = s[:i] + cast + s[j:]
rep("Ages 5–9. Little ones can follow the whole story from the pictures alone.", "Ages 7–10. Younger children can follow the whole story from the pictures alone.")

# guide pages
i = s.index('heading("For Parents and Teachers", 1, "guide")')
j = s.index('toc_link()\npagebreak()\nheading("About the Author"')
guide = '''heading("For Parents and Teachers", 1, "guide")
para("This is a fantasy adventure to read aloud from about age 6 and for children to read themselves at 7 to 10. Younger children can follow the whole story from the pictures alone (a " + Q + "picture walk" + R + ": turn the pages and ask what is happening). Every fact Hopsi states is true, and the magic is marked as magic. The Book 3 gadgets, Wen" + A + "s listener and the scanner with a crank, are storybook machines; real ones use electricity.")
heading("The habits of a scientist in the story", 2, center=False)
for lead, t in [
    (Q + "Check first." + R, "Wen measures the ice before anyone steps on it, and asks whether the Mayor" + A + "s claims about bats are true before the rock goes over the door."),
    ("Say you were wrong.", "Hopsi says " + Q + "I was wrong" + R + " about white ice and about which way the doctor went, and is glad she said it out loud."),
    ("Count and estimate.", "Hal counts a patch of bats and multiplies, and calls it an estimate, not an exact number."),
    ("Honesty.", "Scally hums a little tune before each trick. When a lie hurts someone, he tells the truth, even though it costs him."),
    ("Ask what you cannot hear.", "Gucci can hear sounds people cannot. Wen asks what he is hearing, and builds a way to find out."),
]:
    para(t, lead)
heading("What each chapter teaches", 2, center=False)
for lead, t in [
    ("The First Frost:", "a promise you cannot keep (frost insurance), and safe ladder habits."),
    ("The Doctor" + A + "s Bag:", "how a doctor listens to a heartbeat, why medicine is never candy, and why we do not put our heads into things."),
    ("Ice on the Pond:", "how ice varies, why adults must check conditions, why ice floats, and reach or throw from safety."),
    ("The Hill That Clicks:", "bats, hibernation, why we never wake sleeping animals, and telling a grown-up where you are going."),
    ("The Mayor" + A + "s Cheese Cellar:", "rumors, checking facts, telling the truth when it costs you, and what bats eat."),
    ("Wen" + A + "s Listener:", "sound too high to hear, how bats find their way with echoes, and a scientist" + A + "s " + Q + "I do not know." + R),
    ("The Picture of the Baby:", "how an ultrasound scan works, a baby" + A + "s heartbeat, and a gentle way of knowing a family secret is coming."),
    ("The Sledding Day:", "sledding safety, a fair race, and the difference between a story and a lie."),
    ("The Night of the Big Snow:", "what to do when lost in snow (stop, stay, make noise), staying on the rope, and using sound to find your way home."),
    ("The Baby:", "a welcome, a new brother, and giving a present when words are not enough."),
    ("The First Warm Evening:", "estimating numbers, what bats do for a village, changing your mind, and a new baby in the family."),
]:
    para(t, lead)
heading("Staying safe: what this book models", 2, center=False)
for lead, tx in [
    ("Ice.", "Ice thickness varies, and one measurement cannot prove a pond safe. Four inches is a general guideline for new, clear ice for one person on foot, not a guarantee. Ice may be thinner near shore, over moving water, or under snow. Stay off until an informed adult has checked conditions in several places and says it is safe. Never go alone. If someone falls in, call for help and reach or throw from a safe place; do not go out after them."),
    ("Wild animals.", "Never touch a bat or any wild animal that seems tame or hurt, and tell a grown-up. A few bats carry rabies. Never wake hibernating animals."),
    ("Medicine.", "Never take any medicine unless a grown-up you know well gives it to you. Some medicine tastes sweet on purpose."),
    ("Snow and cold.", "If you are lost in snow, stop, stay where you are, find a fence if you can, and make noise. In a blizzard, stay inside, and use a rope between buildings if you must go out. Tell someone where you are going and go in pairs."),
    ("Sledding.", "Go feet first, down hills that end in a flat open field, away from roads and water. Do not tie sleds together."),
    ("Ladders.", "Somebody holds the bottom, every time."),
]:
    para(tx, lead)
heading("Talk about it", 2, center=False)
for q in [
    "Why does Scally hum a little tune before he tricks someone? How could you tell, if you were Pip?",
    "Wen was afraid of the dark. How did he help himself stay calm while the group watched the cave from a safe distance?",
    "Hopsi says " + Q + "I was wrong" + R + " more than once. Is that easy or hard to do? How did people react?",
    "What do you think a new baby in a family feels like for a big brother or sister? What do you think Pip and Hal feel?",
    "What would you do if you were lost in the snow, or if someone said ice was safe and you were not sure?",
]:
    para(q)
heading("Words to grow", 2, center=False)
para("echo, ultrasound, hibernate, estimate, insurance, friction, scan, heartbeat, pitch, expand.")
heading("A note for adults", 2, center=False)
para("The science is simplified for ages 7 to 10. Bats make very high calls, listen for the echoes, and build a sound picture of the space around them; they can also see. Hibernating bats live on stored fat, and each time one wakes it uses some of it. A medical ultrasound scan uses the same kind of echo to make a picture, and doctors use it to look at an unborn baby; the baby " + A + "s heart beats about twice as fast as an adult" + A + "s. Water expands by roughly one eleventh when it freezes. The book mentions pregnancy lightly and without detail, and a new baby in the family can be a good moment to talk about feelings of being left out. Bats are protected in many places; please never disturb a roost.")
'''
s = s[:i] + guide + s[j:]

# also-by page
i = s.index('heading("Also by Anneliese Tauber", 1, "alsoby")')
j = s.index('centered("Bavarian Cooking Made Simple"', i)
alsoby = '''heading("Also by Anneliese Tauber", 1, "alsoby")
centered("The Wee Scallywag and the Gentle Elf", 15, True, after=4)
centered("The Step Stories, Book 1. Where Scally first met Hal, Hopsi and a ghost in a mill.", 12, italic=True, after=14)
centered("Scally and the Sleepless Stream", 15, True, after=4)
centered("The Step Stories, Book 2. Hal, Scally and Hopsi follow the stream to find where the water goes.", 12, italic=True, after=14)
centered("Book 4 of The Step Stories is coming soon.", 12, italic=True, after=14)
'''
s = s[:i] + alsoby + s[j:]
out = os.path.join(HERE, "build_book3.py")
open(out, "w", encoding="utf-8").write(s)
print("build_book3.py written;", len(lines), "anchors;", STORY)
