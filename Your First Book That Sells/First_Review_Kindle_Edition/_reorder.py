"""Apply the review fixes to easy_book.md: order, methods, June, glossary, money, links."""
from pathlib import Path

path = Path(__file__).with_name("easy_book.md")
text = path.read_text(encoding="utf-8")

# Split off the front matter through the contents, then the chapters.
start, rest = text.split("\n# Contents\n", 1)
contents_and_body = rest
# contents ends at the next H1
body = contents_and_body.split("\n# ", 1)[1]
body = "# " + body
parts = body.split("\n# ")
parts = [parts[0]] + ["# " + p for p in parts[1:]]

def title_of(part):
    return part.split("\n", 1)[0]

by_title = {}
for part in parts:
    by_title[title_of(part)] = part

order = [
    "# 15 Write one kind of book",
    "# 1 Name the reader",
    "# 2 The number you keep",
    "# 3 A page a stranger can trust",
    "# 4 Cover, keywords, and categories",
    "# 5 Ask for an honest review",
    "# 6 Find readers and send the copy",
    "# 7 Thirty-two ways a book can pay you",
    "# 8 A small ad test",
    "# 9 The next book",
    "# 10 Six calm weeks",
    "# 11 When the book is already live",
    "# 12 Words you can copy",
    "# 13 A filled money sheet",
    "# 14 The Kindle file",
]
missing = [t for t in order if t not in by_title]
if missing:
    raise SystemExit("missing " + str(missing))

renamed = []
for i, old in enumerate(order, start=1):
    part = by_title[old]
    first, _, tail = part.partition("\n")
    # first is like "# 15 Write one kind of book"
    name = first.split(" ", 2)[2]
    renamed.append(f"# {i} {name}\n{tail}")

new_contents = """# Contents

1 Write one kind of book
2 Name the reader
3 The number you keep
4 A page a stranger can trust
5 Cover, keywords, and categories
6 Ask for an honest review
7 Find readers and send the copy
8 Thirty-two ways a book can pay you
9 A small ad test
10 The next book
11 Six calm weeks
12 When the book is already live
13 Words you can copy
14 A filled money sheet
15 The Kindle file
Glossary
Official sources
"""

opening = """# Start here

June has a finished mystery and a price of $0.99 in her head. She has not asked what one sale would leave her. This book is the month she finds out.

Read it in this order. Write the book. Name the reader. Learn the number you keep. Then fix the page, the reviews, and the money. If the book is already on sale, still read in this order. The chapter about a quiet book will be there when you reach it.

There is one method, the keep test. Three lines. What one sale leaves you. Who the reader is, and who the reader is not. The one change you will make, and the day you will look. The four steps in the money chapter are only how you fill those three lines for a single idea. The calendars are dates on a wall. They are not a second method.

Every dollar figure is marked. A teaching example is a made-up sum so you can practice the arithmetic. A platform rule is something Amazon published, checked here on 27 September 2026. Recheck the linked page before you rely on it. Nothing in this book is a promise that you will earn a stated amount.

## The keep test

Write the three lines before you spend money or a week.

The keep. What one sale leaves you, from the estimate in your KDP account. If you have no file yet, use a practice number from chapter 3 and write the word “practice” beside it.

The reader. The two sentences from chapter 2. Who it is for. Who it is not for.

The date. The one change, and the day you will look.

If a line is blank, do not pay for an ad, a promotion, or a stack of free copies. At each later decision the book fills the three lines with June’s numbers, so you can see the test instead of only the instruction.

{{img:keep_test.png|Three boxes: the keep, the reader, and the date. If a line is blank, do not spend.}}

"""

body_text = "\n".join(renamed)

# Old chapter numbers -> new. Replace high numbers first via tokens.
text = body_text
repls = [
    ("chapter 15", "@@15@@"),
    ("Chapter 15", "@@15@@"),
    ("chapter 14", "@@14@@"),
    ("chapter 13", "@@13@@"),
    ("chapter 12", "@@12@@"),
    ("chapter 11", "@@11@@"),
    ("chapter 10", "@@10@@"),
    ("chapter 9", "@@9@@"),
    ("chapter 8", "@@8@@"),
    ("chapter 7", "@@7@@"),
    ("chapter 6", "@@6@@"),
    ("chapter 5", "@@5@@"),
    ("chapter 4", "@@4@@"),
    ("chapter 3", "@@3@@"),
    ("chapter 2", "@@2@@"),
    ("chapter 1", "@@1@@"),
    ("Chapter 1", "@@1@@"),
]
for a, b in repls:
    text = text.replace(a, b)
new_of = {
    15: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8,
    8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15,
}
for old, new in new_of.items():
    text = text.replace(f"@@{old}@@", f"chapter {new}")

text = opening + "\n" + new_contents + "\n" + text

# June in the reader chapter, which is now chapter 2.
text = text.replace(
    "# 2 Name the reader\n\nDo not write for",
    "# 2 Name the reader\n\nJune is the author in the examples that follow. She begins the month at $0.99. She has two sentences to write before she is allowed to talk about price.\n\nDo not write for",
    1,
)
text = text.replace(
    "Story A, the price. June’s only book",
    "Story A, the price. This is June, later in the same month. Her only book",
    1,
)

# Filled keep test instead of the slogan.
old_slogan = "Before you spend, write the three lines. The keep. The reader. The date. If one is blank, do not pay yet."
filled = (
    "Before you spend, fill June’s three lines with your own.\n\n"
    "Keep: about $2.58 on a $3.99 ebook in the chapter 3 example, or the estimate KDP shows for your file.\n\n"
    "Reader: the two sentences from chapter 2.\n\n"
    "Date: the one change, and the day you will look.\n\n"
    "If one line is still blank, do not pay yet."
)
text = text.replace(old_slogan, filled)

# VAT and returns, once, in the keep chapter.
text = text.replace(
    "Whenever this book says “about $2.58,” it means that $3.99 line. It does not mean a mystery fee.",
    "Whenever this book says “about $2.58,” it means that $3.99 line. It does not mean a mystery fee.\n\n"
    "These examples have no VAT. A price that already includes VAT is a smaller base, so the keep is smaller than the line above. A return takes the keep back.",
    1,
)

# Box set sum.
text = text.replace(
    "Three related books can also be one purchase at a small discount off the sum of the three keeps. Some readers would rather pay once. Do the arithmetic. Three books at $2.58 kept is about $7.74 if bought separately. A set should still leave you a keep you can accept. Skip a set of one finished book and two promises.",
    "Three related books can also be one purchase. Three sales at the $3.99 keep of about $2.58 are about $7.74 if the reader buys them one by one. A set priced at $7.99, same 2 MB example, no tax, keeps 0.70 × ($7.99 − $0.30), about $5.38. The reader pays less. You keep less than three separate sales. Take the set only if you want that $5.38. Skip a set made of one finished book and two promises.",
    1,
)

# Library / expanded distribution.
text = text.replace(
    "Some paperbacks are ordered one at a time for a long while. The keep is still list price times rate, minus print. One library order will not pay your rent. A row of books can be a small drip. Skip a price so low that print cost eats it.",
    "Some paperbacks are ordered one at a time for a long while. A sale on Amazon’s own store often uses a higher rate than expanded distribution, which is the path many library sales use. In the chapter 3 illustration, $14.99 at 60 percent, after a $4 print cost, keeps about $5. The same book at a 40 percent expanded-distribution rate keeps (0.40 × $14.99) − $4, about $2. Those rates are the usual ones to check, not a promise. The calculator wins. One library order will not pay your rent. Skip a price so low that print cost eats it.",
    1,
)

# KU cannot be compared to a sale from this book.
text = text.replace(
    "Enrollment is not a promise of reads. [5]",
    "Enrollment is not a promise of reads. You cannot lay a page-read next to a $2.58 sale using this book. Amazon’s per-page rate changes, and it is in your reports, not here. Until you have read that rate, Select is a choice about where the ebook is sold, not a second keep. [5]",
    1,
)

# Cite the publishing guidelines.
text = text.replace(
    "Use real headings so the contents links work.",
    "The file has to meet the Kindle Publishing Guidelines. [9] Use real headings so the contents links work.",
    1,
)

# Direct link for community guidelines. Amazon's current help node.
text = text.replace(
    "[2] Amazon Community Guidelines. Use the marketplace link on the Customer Reviews page.",
    "[2] Amazon Community Guidelines\nhttps://www.amazon.com/gp/help/customer/display.html?nodeId=GLHXEX85MENUE4XF",
    1,
)

glossary = """
# Glossary

One line each. The chapter that teaches the word is named.

Advance copy. A free book you send before publication. A review is optional. Chapter 6.

Backlist. The books you already published and left on sale. Chapter 8.

Countdown. A short, scheduled price cut that may keep the 70 percent rate below $2.99 if you qualify. Chapter 8. [6]

Delivery. A per-megabyte charge taken off before the 70 percent cut. Not taken off in the 35 percent band. Chapter 3.

Expanded distribution. The wider paperback channel. Its rate is lower than a sale on Amazon’s own store. Chapter 3 and chapter 8.

Keep. What one sale leaves you after the percentage and, when it applies, delivery. Chapter 3.

KDP Select. A 90-day enrollment. Page reads may pay you. The ebook stays exclusive to Kindle for the term. Chapter 8. [5]

Seventy percent band. On Amazon.com, as checked on 27 September 2026, the usual ebook prices from $2.99 to $12.99 where a 70 percent royalty can apply. Chapter 3. [3]

Thumbnail test. Whether the title can be read when the cover is tiny. Chapter 5.

"""
text = text.replace("\n# Official sources\n", glossary + "\n# Official sources\n", 1)

# Decorative pictures the words already cover.
for tag in (
    "{{img:readers.png|An author and a diverse group of readers sharing an open book.}}\n\n",
    "{{img:three_ways.png|Three panels labeled Price, Next book, and Another format, each with a teaching-example figure.}}\n\n",
    "{{img:catalog.png|A small stack of related books, suggesting a catalog a reader can continue.}}\n\n",
):
    text = text.replace(tag, "")

path.write_text(text, encoding="utf-8")
print("chapters", text.count("\n# "))
print("june", text.count("June"))
print("glossary", "Glossary" in text)
print("twenty-four leftover", "twenty-four" in text.lower())
