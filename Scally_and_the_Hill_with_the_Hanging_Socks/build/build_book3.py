import re, io, os, datetime
from PIL import Image
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(B, "Step_Stories_Pics_Final")
TITLE1, TITLE2 = "Scally and the Hill", "with the Hanging Socks"
FULL = "Scally and the Hill with the Hanging Socks"
SERIES = "The Step Stories"
AUTHOR = "Anneliese Tauber"
STORY_FILE = "Book3_Story_v8.txt"
VERSION = re.search(r"_(v\d+)\.txt$", STORY_FILE).group(1)
STORY = os.path.join(B, "Step_Stories_Texts", STORY_FILE)
Q = "“"; R = "”"; A = "’"

raw = open(STORY, encoding="utf-8").read()
body = raw[raw.index("Chapter 1."):]
blocks = [b.strip("\n") for b in re.split(r"\n\s*\n", body) if b.strip()]

place = {
    'Hal Millersen woke to find his window furred ': 'p001_ch01.jpg',
    'Downstairs the kitchen smelled of porridge an': 'p002_ch01.jpg',
    'The cart stopped in the yard. The woman jumpe': 'p003_ch01.jpg',
    'The boy, Wen, had not said anything. He had c': 'p004_ch01.jpg',
    'It took a long time. A bit of old oil dripped': 'p005_ch01.jpg',
    'It was the first thing Wen had said. Hal, at ': 'p006_ch01.jpg',
    'Nobody explained it to him. Hal put it on the': 'p007_ch01.jpg',
    'Titch’s mother, who was as round as a barrel ': 'p008_ch01.jpg',
    'Everybody turned. Scally looked at him. He ha': 'p009_ch01.jpg',
    'Hopsi had unwrapped one of her scarves to loo': 'p010_ch01.jpg',
    '“I have not got a mother like that,” said Sca': 'p011_ch01.jpg',
    'But beside Hal, the great gray wolf had gone ': 'p012_ch01.jpg',
    'He did not howl like a wolf in a story, with ': 'p013_ch02.jpg',
    'Dr. Liang’s house stood by the bridge, a smal': 'p014_ch02.jpg',
    'Inside, the house smelled of soap and woodsmo': 'p015_ch02.jpg',
    'Thump-thump. Thump-thump. Thump-thump. It was': 'p016_ch02.jpg',
    'Gucci had never in his life been asked to sta': 'p017_ch02.jpg',
    'While all this was going on, Pip had been goo': 'p018_ch02.jpg',
    '“It was only going to be a little bit,” said ': 'p019_ch02.jpg',
    '“You never take any medicine, or any pill, or': 'p020_ch02.jpg',
    'It had been standing by the back door the who': 'p021_ch02.jpg',
    'He had been standing still. Now he put down h': 'p022_ch02.jpg',
    'It took a whole pat of butter and a long, qui': 'p023_ch02.jpg',
    'When they had cleaned up the kitchen, and was': 'p024_ch02.jpg',
    'Scally had been standing a little apart, with': 'p025_ch02.jpg',
    '“Thank you,” he said. “It is the best one. I ': 'p026_ch02.jpg',
    'By the end of the week the mill pond had froz': 'p027_ch03.jpg',
    'He was kneeling on the bank, at the very edge': 'p028_ch03.jpg',
    '“It is the weak kind,” said Wen, without look': 'p029_ch03.jpg',
    'Scally had been quiet for a while. He had bee': 'p030_ch03.jpg',
    'Scally opened his mouth, and found that there': 'p031_ch03.jpg',
    'Pip said it, too. He said it with his best fa': 'p032_ch03.jpg',
    'He did not run. He walked, carefully, with hi': 'p033_ch03.jpg',
    'The whole bank was moving at once. Hal’s moth': 'p034_ch03.jpg',
    '“Throw it low,” said Wen. “So it slides. Not ': 'p035_ch03.jpg',
    'Pip lay down on the ice. He did it so slowly ': 'p036_ch03.jpg',
    'They all pulled. Hal and Tabitha and Titch, w': 'p037_ch03.jpg',
    '“I did not test it,” said Scally. He said it ': 'p038_ch03.jpg',
    'For a moment nobody moved. Then Hal’s mother ': 'p039_ch03.jpg',
    'Dr. Liang looked at her son. She did not say ': 'p040_ch03.jpg',
    'The ice melted, and froze again, and melted a': 'p041_ch04.jpg',
    '“I did. All eleven. And the church tower, fro': 'p042_ch04.jpg',
    '“Just a little, just a bit,” said a small voi': 'p043_ch04.jpg',
    'First, Hal asked his mother. She was at the k': 'p044_ch04.jpg',
    'It was a long hill, and a cold one. The sun, ': 'p045_ch04.jpg',
    '“I am not,” said Wen, “a person who likes the': 'p046_ch04.jpg',
    'The passage opened out suddenly into a chambe': 'p047_ch04.jpg',
    'She had said it softly, with her face tipped ': 'p048_ch04.jpg',
    'He took it out, slowly. It was not easy for h': 'p049_ch04.jpg',
    'It did it slowly. A small black wing opened, ': 'p050_ch04.jpg',
    'It was just past two in the afternoon. They w': 'p051_ch04.jpg',
    'By the next morning the whole village knew ab': 'p052_ch05.jpg',
    'It was the first thing Hopsi had said all mor': 'p053_ch05.jpg',
    '“As you know,” said the Mayor, “this village ': 'p054_ch05.jpg',
    '“Ah,” said the Mayor. “Yes. The bats.” He low': 'p055_ch05.jpg',
    'Scally was standing still. All the color had ': 'p056_ch05.jpg',
    'For a long moment, Scally did not move. Then ': 'p057_ch05.jpg',
    '“They do not,” said Scally. “I made it up. I ': 'p058_ch05.jpg',
    '“The boy is right,” said Dr. Liang. “I am a d': 'p059_ch05.jpg',
    '“Well!” said the Mayor at last, going a deep pink': 'p060_ch05.jpg',
    'It was the third night after the village meet': 'p061_ch06.jpg',
    '“Sound has a pitch,” said Wen. “High or low. ': 'p062_ch06.jpg',
    'It was the strangest thing Hal had ever seen.': 'p063_ch06.jpg',
    '“I should say,” said Hopsi, slowly, “that I d': 'p064_ch06.jpg',
    'They stopped a good way from the cave mouth. ': 'p065_ch06.jpg',
    'He held out the funnel, and all of them liste': 'p066_ch06.jpg',
    'Over the hill, against the last green light, ': 'p067_ch06.jpg',
    'Scally, kneeling in the bracken with his arms': 'p068_ch06.jpg',
    'It was a gray Saturday in the middle of Janua': 'p069_ch07.jpg',
    '“It is a listening lantern,” said Dr. Liang. ': 'p070_ch07.jpg',
    'Titch’s mother had been sitting in the best c': 'p071_ch07.jpg',
    'And from the box, very faintly, there came a ': 'p072_ch07.jpg',
    'Titch’s mother was crying a little, in an ext': 'p073_ch07.jpg',
    '“I do not tell people what they are having,” ': 'p074_ch07.jpg',
    'They all had a turn at the window, to look at': 'p075_ch07.jpg',
    'Her voice was light and ordinary. But Hal, lo': 'p076_ch07.jpg',
    'They went. The kitchen was warm and small and': 'p077_ch07.jpg',
    '“Everything is perfectly fine,” she said. “I ': 'p078_ch07.jpg',
    'The big snow came the first week of February,': 'p079_ch08.jpg',
    'The long hill behind the mill was the best in': 'p080_ch08.jpg',
    '“Hmm,” said Dr. Liang, from her other side. S': 'p081_ch08.jpg',
    'It was a long, low, handsome sled, made of pa': 'p082_ch08.jpg',
    'It was the first time anyone had ever heard h': 'p083_ch08.jpg',
    'They went again. Scally, on the baker’s tray,': 'p084_ch08.jpg',
    '“You are going to go over the little bump,” s': 'p085_ch08.jpg',
    'The rest of the morning went by in a happy bl': 'p086_ch08.jpg',
    '“It is the best one so far,” said Hopsi. “I d': 'p087_ch08.jpg',
    '“Right now,” said Dr. Liang, and stood, and p': 'p088_ch08.jpg',
    'Hal always said that the first flake fell jus': 'p089_ch09.jpg',
    'She had come over from the hill at a run, wit': 'p090_ch09.jpg',
    'She went out into the white. The door shut. A': 'p091_ch09.jpg',
    'The men went out in a chain, tied together by': 'p092_ch09.jpg',
    '“A person who is lost in snow should stop,” s': 'p093_ch09.jpg',
    'It was the strangest scene any of them ever r': 'p094_ch09.jpg',
    '“She says it is where the wind was coming fro': 'p095_ch09.jpg',
    '“No,” said Hal’s father. “Not you. Not the ro': 'p096_ch09.jpg',
    'It was a long ten minutes. Nobody spoke. Wen ': 'p097_ch09.jpg',
    '“I stopped,” said Dr. Liang. She was shaking ': 'p098_ch09.jpg',
    'Dr. Liang ran. She ran across the yard, along': 'p099_ch09.jpg',
    'Mrs. Crumb came out of the little front room ': 'p100_ch10.jpg',
    'Pip had gone to sleep on the floor under the ': 'p101_ch10.jpg',
    '“I have got Pip, and Little Man, and Pipsquea': 'p102_ch10.jpg',
    'Pip climbed up onto the bed. He put his elbow': 'p103_ch10.jpg',
    '“Swish,” said Wen, in a whisper. “Swish-swish': 'p104_ch10.jpg',
    'Scally sat. He held out his arms, rigidly, th': 'p105_ch10.jpg',
    'She had thought about it all evening, in the ': 'p106_ch10.jpg',
    'Outside the wind had begun to drop. The storm': 'p107_ch10.jpg',
    'It ran off the roofs in little silver waterfa': 'p108_ch11.jpg',
    'They had brought blankets. They had brought t': 'p109_ch11.jpg',
    'Hal cleared his throat. “We went into the cav': 'p110_ch11.jpg',
    '“The cabbage moth is the worst pest in this v': 'p111_ch11.jpg',
    'It came out low, and quick, and so small that': 'p112_ch11.jpg',
    'He stood in the grass, with his wheel of chee': 'p113_ch11.jpg',
    '“There is another cellar,” he said. “It has b': 'p114_ch11.jpg',
    '“Mr. Mayor,” said a small, clear voice.': 'p115_ch11.jpg',
    'Hal sat at the kitchen table with his slate i': 'p116_ch11.jpg',
    '“I did not know,” said Hal. “But I wrote it d': 'p117_ch11.jpg',
    '“No,” said Hal. “Wait.” He stood up. He went ': 'p118_ch11.jpg',
    'Someone was walking along the road toward the': 'p119_ch11.jpg',
}

for _k, _v in place.items():
    _n = sum(1 for x in blocks if x.startswith(_k))
    if _n != 1 or not os.path.exists(os.path.join(P, _v)):
        print("ANCHOR PROBLEM", _n, _v, repr(_k[:50]))


def img_bytes(path, w=640, q=68):
    im = Image.open(path).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "JPEG", quality=q, optimize=True)
    b.seek(0)
    return b


def make_cover():
    src = Image.open(os.path.join(B, "Cover_Front_1600x2560.jpg")).convert("RGB")
    out = os.path.join(P, "cover_1000x1600.jpg")
    src.resize((1000, 1600), Image.LANCZOS).save(out, quality=88)
    return out


COVER = make_cover()
d = Document()
sec = d.sections[0]
sec.page_width = Inches(6)
sec.page_height = Inches(9)
for a in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
    setattr(sec, a, Inches(0.8))
st = d.styles["Normal"]
st.font.name = "Georgia"
st.font.size = Pt(13)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Georgia")
st.paragraph_format.space_after = Pt(10)
st.paragraph_format.line_spacing = 1.3
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
RUST = RGBColor(0xA8, 0x4B, 0x2A)
for n, sz in (("Heading 1", 24), ("Heading 2", 19)):
    h = d.styles[n]
    h.font.name = "Georgia"
    h.font.size = Pt(sz)
    h.font.bold = True
    h.font.color.rgb = NAVY
    h.element.rPr.rFonts.set(qn("w:eastAsia"), "Georgia")
    h.paragraph_format.keep_with_next = True
    h.paragraph_format.space_before = Pt(14)

bid = [0]


def bookmark(par, name):
    bid[0] += 1
    s = OxmlElement("w:bookmarkStart")
    s.set(qn("w:id"), str(bid[0]))
    s.set(qn("w:name"), name)
    e = OxmlElement("w:bookmarkEnd")
    e.set(qn("w:id"), str(bid[0]))
    par._p.insert(0, s)
    par._p.append(e)


def link(par, text, anchor):
    h = OxmlElement("w:hyperlink")
    h.set(qn("w:anchor"), anchor)
    r = OxmlElement("w:r")
    rp = OxmlElement("w:rPr")
    c = OxmlElement("w:color")
    c.set(qn("w:val"), "1F3A5F")
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rp.append(c)
    rp.append(u)
    r.append(rp)
    t = OxmlElement("w:t")
    t.text = text
    r.append(t)
    h.append(r)
    par._p.append(h)


def pagebreak():
    d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def centered(text, size=13, bold=False, italic=False, after=10, color=None):
    p = d.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = color
    return p


def pic(name, w_in=4.4):
    p = d.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(img_bytes(os.path.join(P, name)), width=Inches(w_in))


def heading(text, level, anchor=None, center=True):
    h = d.add_paragraph(text, style="Heading %d" % level)
    if center:
        h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if anchor:
        bookmark(h, anchor)
    return h


def toc_link():
    p = d.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    link(p, "↑ Contents", "toc")


def para(t, lead=None):
    p = d.add_paragraph()
    if lead:
        r = p.add_run(lead + " ")
        r.bold = True
    p.add_run(t)


def lead_bold(par, text):
    m = re.match(r"^(\d+\. [^.]+\.)(.*)$", text, re.S)
    if m:
        r = par.add_run(m.group(1))
        r.bold = True
        par.add_run(m.group(2))
    else:
        par.add_run(text)


chapters = [b.split("\n")[0] for b in blocks if b.startswith("Chapter ")]
TOC = [("Meet the Characters", "cast")] + [(c, "ch%d" % (i + 1)) for i, c in enumerate(chapters)] + [
    ("Hal" + A + "s Slate: What We Found Out", "slate"), ("For Parents and Teachers", "guide"),
    ("About the Author", "about"), ("Also by Anneliese Tauber", "alsoby")]

# cover
sec.top_margin = sec.bottom_margin = Inches(0.2)
sec.left_margin = sec.right_margin = Inches(0.2)
p = d.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_after = Pt(0)
p.add_run().add_picture(COVER, height=Inches(8.5))
sec2 = d.add_section()
for a in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
    setattr(sec2, a, Inches(0.8))

for _ in range(5):
    d.add_paragraph()
centered(TITLE1, 34, True, color=NAVY)
centered(TITLE2, 34, True, color=RUST)
centered("Book 3 of " + SERIES, 15, italic=True, after=30)
centered(AUTHOR, 18)
pagebreak()
heading("Contents", 1, "toc")
for t, a in TOC:
    p = d.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(4)
    link(p, t, a)
pagebreak()

heading("Meet the Characters", 1, "cast")
cast = [
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
]
for n, t in cast:
    p = d.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(9)
    r = p.add_run(n)
    r.bold = True
    p.add_run("\n" + t)
centered("Ages 7–10. Younger children can follow the whole story from the pictures alone.", 12, italic=True)
pagebreak()

ci = 0
in_slate = False
first = True
for b in blocks:
    if b == "---":
        continue
    if b.startswith("Chapter "):
        ci += 1
        if not first:
            toc_link()
            pagebreak()
        first = False
        heading(b, 2, "ch%d" % ci)
        continue
    if b == "The End":
        centered("The End", 18, True).paragraph_format.space_before = Pt(18)
        toc_link()
        pagebreak()
        continue
    if b.startswith("Hal" + A + "s Slate: What We Found Out"):
        heading("Hal" + A + "s Slate: What We Found Out", 1, "slate")
        in_slate = True
        continue
    if len(b) < 60 and "\n" not in b and not re.search(r"[a-z]", b):
        centered(b, 16, True, after=12)
        continue
    if len(b.split("\n")) in (2, 3) and all(l.isupper() or not re.search(r"[a-z]", l) for l in b.split("\n")):
        p = d.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        lines = b.split("\n")
        for i, l in enumerate(lines):
            r = p.add_run(l)
            r.bold = True
            if i < len(lines) - 1:
                r.add_break()
        continue
    p = d.add_paragraph()
    if in_slate:
        lead_bold(p, b.replace("\n", " "))
    else:
        p.add_run(b.replace("\n", " "))
    for k, v in place.items():
        if b.startswith(k):
            pic(v)
            break

toc_link()
pagebreak()
heading("For Parents and Teachers", 1, "guide")
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
    ("Ice on the Pond:", "how thick ice must be to hold you, why white ice is weaker, why ice floats, and reach or throw."),
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
    ("Ice.", "Ice must be at least four inches thick to walk on, and clear ice is stronger than white ice. Ice over moving water is thinnest. Never go on ice alone, and never trust a claim that it is safe unless someone checked. If someone falls in, reach or throw; do not go out after them. If the ice cracks under you, lie flat and crawl back. Please check your local guidance."),
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
    "Wen was afraid of the dark and went into the cave anyway. What did he do to feel braver?",
    "Hopsi says " + Q + "I was wrong" + R + " more than once. Is that easy or hard to do? How did people react?",
    "What do you think a new baby in a family feels like for a big brother or sister? What do you think Pip and Hal feel?",
    "What would you do if you were lost in the snow, or if someone said ice was safe and you were not sure?",
]:
    para(q)
heading("Words to grow", 2, center=False)
para("echo, ultrasound, hibernate, estimate, insurance, friction, scan, heartbeat, pitch, expand.")
heading("A note for adults", 2, center=False)
para("The science is simplified for ages 7 to 10. Bats make very high calls, listen for the echoes, and build a sound picture of the space around them; they can also see. Hibernating bats live on stored fat, and each time one wakes it uses some of it. A medical ultrasound scan uses the same kind of echo to make a picture, and doctors use it to look at an unborn baby; the baby " + A + "s heart beats about twice as fast as an adult" + A + "s. Water expands by roughly one eleventh when it freezes. The book mentions pregnancy lightly and without detail, and a new baby in the family can be a good moment to talk about feelings of being left out. Bats are protected in many places; please never disturb a roost.")
toc_link()
pagebreak()
heading("About the Author", 1, "about")
para("Anneliese Tauber is a mother of four. When her children were small she read them a great many fairy tales, and she noticed that the best ones answered the questions children ask, and never needed to bend the truth. The Step Stories are for curious children and the grown-ups who read to them.")
centered("If your child enjoyed this book, a short, kind review on Amazon helps other curious families find it. Thank you.", 13, italic=True)
toc_link()
pagebreak()
heading("Also by Anneliese Tauber", 1, "alsoby")
centered("The Wee Scallywag and the Gentle Elf", 15, True, after=4)
centered("The Step Stories, Book 1. Where Scally first met Hal, Hopsi and a ghost in a mill.", 12, italic=True, after=14)
centered("Scally and the Sleepless Stream", 15, True, after=4)
centered("The Step Stories, Book 2. Hal, Scally and Hopsi follow the stream to find where the water goes.", 12, italic=True, after=14)
centered("Book 4 of The Step Stories is coming soon.", 12, italic=True, after=14)
centered("Bavarian Cooking Made Simple", 15, True, after=4)
centered("Classic dishes from a Bavarian kitchen, written so that any cook can enjoy a taste of Bavaria.", 12, italic=True)
toc_link()
centered("Typeface in the e-book edition: Comic Neue, © The Comic Neue Project Authors, used under the SIL Open Font License 1.1.", 10, italic=True)
d.core_properties.title = FULL
d.core_properties.author = AUTHOR
now = datetime.datetime.now(datetime.timezone.utc)
d.core_properties.created = now
d.core_properties.modified = now
d.core_properties.last_modified_by = AUTHOR
dst = os.environ.get("OUTDOCX") or os.path.join(B, "Scally_and_the_Hill_with_the_Hanging_Socks_Book3_%s.docx" % VERSION)
d.save(dst)
print(dst, os.path.getsize(dst) // 1024, "KB")
