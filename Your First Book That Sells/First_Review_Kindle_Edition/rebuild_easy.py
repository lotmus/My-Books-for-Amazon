"""Plain-language rebuild of the Kindle manuscript. Uses the pictures already in this folder."""
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor

root = Path(__file__).parent
out = root / "Your_First_Book_That_Sells_Updated.docx"

d = Document()
s = d.sections[0]
s.page_width = Inches(7)
s.page_height = Inches(10)
s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Inches(0.7)
for name in ["Normal", "Title", "Subtitle", "Heading 1", "Heading 2"]:
    d.styles[name].font.name = "Calibri"
    d.styles[name].font.color.rgb = RGBColor(0, 0, 0)
d.styles["Normal"].font.size = Pt(12)
d.styles["Normal"].paragraph_format.space_after = Pt(8)
d.styles["Normal"].paragraph_format.line_spacing = 1.15
d.styles["Title"].font.size = Pt(32)
d.styles["Heading 1"].font.size = Pt(22)
d.styles["Heading 1"].paragraph_format.page_break_before = True
d.styles["Heading 2"].font.size = Pt(16)


def pic(name, alt):
    p = d.add_paragraph()
    r = p.add_run()
    r.add_picture(str(root / name), width=Inches(5.4))
    r._r.xpath(".//wp:docPr")[0].set("descr", alt)


def add(text):
    for line in text.strip().splitlines():
        if line.startswith("# "):
            d.add_paragraph(line[2:], "Heading 1")
        elif line.startswith("## "):
            d.add_paragraph(line[3:], "Heading 2")
        elif line.strip():
            d.add_paragraph(line.strip())


d.add_paragraph("Your First Book\nThat Sells", "Title")
d.add_paragraph(
    "How to Self Publish on Kindle, Attract Honest Reviews, and Build a Profitable Book Catalog",
    "Subtitle",
)
pic("readers.png", "An author and a diverse group of readers sharing an open book.")
d.add_paragraph("A short, plain guide to getting paid for a book you wrote.")
d.add_paragraph("Updated 30 September 2026")

add("""
# Start here

You do not need a fancy launch.
You need a book a stranger can finish, a page that tells the truth, and a price that pays you something.

Read this book in order if you have not published yet.
If the book is already live and quiet, jump to the money list in chapter 7. Then fix the page. Then look at reviews.

Every dollar figure in here is a teaching example, or a platform rule you should recheck.
None of it is a promise that you will earn that amount.
The Kindle rules were checked on 27 September 2026. Look again before you click publish. [3] [4]

If the manuscript is not written yet, do chapter 15 first.
A price cannot fix a book that has no shape.

# Contents

1 Name the reader
2 Make the page easy to trust
3 Ask for an honest review
4 Find people who already want this book
5 Send the copy and stop nagging
6 Price so a sale pays you
7 Twenty-four ways a book can pay you
8 Spend less than a sale brings back
9 Let the next book earn too
10 Six calm weeks
11 When the book is quiet
12 Words you can copy
13 One money sheet
14 Look at the Kindle file
15 Write one kind of book
Official sources

# 1 Name the reader

Do not write for “people who like books.”
That is everyone. It helps no one.

Name one reader.
A cozy-mystery reader who wants a small town and a kind heroine.
Or a first-time author who wants a simple plan and a price that is not a guess.

Finish this sentence.
This book helps or entertains [this reader] by giving them [this experience].

Then write the opposite.
This book is a poor fit for people who want [something else].
That second sentence keeps you from begging the wrong people to buy.

## Money idea

The reader sentence is a sales tool.
It becomes the first two lines of your description, the words on the cover, and the reason someone pays.

## Your action

Write the two sentences.
If you cannot, stop buying ads.

# 2 Make the page easy to trust

The cover, the description, the sample, and the book must promise the same thing.
A good review cannot save a sample that is hard to read.

Look at the cover as a tiny picture.
Can you read the title?
Can you tell what kind of book it is?

Read the first two sentences of the description out loud.
They should say who it is for and what they get.
Cut praise you cannot prove.
Cut any line that says the reader will get rich.

Open the sample on your phone.
A reader should reach something useful before a pile of front matter.

## Money idea

A clear page sells while you sleep.
A muddy page makes you pay for clicks that do not become sales.

## Your action

Ask one person who does not know the book what they think it is.
If their answer is wrong, fix the page before you look for readers.

# 3 Ask for an honest review

A new book has little proof.
An honest review is one piece of proof.
It is not a bill you can send a reader.

You may give a free advance copy.
Say that a review is welcome and optional.
Do not ask for a star rating.
Do not offer a gift card.
Do not pay for praise.
Amazon’s review rules say a free copy is allowed only when you do not require or steer the review. Recheck that page. [1] [2]

Some people will not finish.
Some will finish and say nothing.
That is allowed.

If a service promises a stack of five-star reviews, do not buy it.

## Money idea

Reviews do not deposit money.
They help the next stranger decide to pay.
Ten honest lines beat a bought pile that can get the book in trouble.

## Your action

Read your invitation.
Delete any sentence that sounds like a debt.

# 4 Find people who already want this book

The best reader already likes this kind of book and has time to read it.
Someone who “supports authors” but hates your subject will not buy the next one.

Start with people who asked to hear from you.
Then try communities that allow a polite invitation.
Follow their rules.
Do not scrape email addresses.

Tell them the subject, the length, the format, and the dates.
Give them an easy way to say no.

## Money idea

A small list of the right people is worth more than a big list of strangers.
The right people buy book two.

## Your action

Pick two places to invite readers.
Set a limit on how many free copies you can handle.
Stop when you hit the limit.

# 5 Send the copy and stop nagging

Make the file easy to open.
Test the link yourself.
Use a file name with the title and the date.

Send a short note when you send the file.
Send the store link when the book is live and reviews are open.
Send one gentle reminder later.
Then stop.

If the file was broken, fix it and give them more time.
Do not send another “please review” note to someone who could not open the book.

If you plan to join KDP Select, read the exclusivity rules before you hand out the ebook anywhere else. [5]

## Money idea

A calm campaign costs little.
A messy one eats the week you could have spent on the next book, which is where repeat money comes from.

## Your action

Send the file to one friend first.
If they get stuck, fix the instructions before you mail the group.

# 6 Price so a sale pays you

A low price can sell more copies and still pay you less.
Write down what you keep, not just the sticker.

On Amazon.com, as checked in September 2026, the usual 70 percent ebook band is $2.99 to $12.99.
Other rules apply. Look at the price page and at the estimate in your KDP account. [3]

A simple picture, with no tax and a small file:
At $0.99 you are often in the 35 percent band. You might keep about $0.35.
At $2.99 in the 70 percent band, after a small delivery fee, you might keep about $1.88.
At $4.99 you might keep about $3.28.
At $7.99 you might keep about $5.38.

These are rounded examples for a 2 MB file.
Delivery on Amazon.com was listed at $0.15 per megabyte. [4]
An illustrated book can cost more to deliver.
Use KDP’s own estimate for your file.

Thirty copies at about $1.88 is about $56.
Twenty-five copies at about $2.58 is about $65.
Fewer sales can pay you more.
Do not change the price, the cover, and the ads on the same day. You will not know what worked.

A paperback is a different sum.
You take a royalty rate times the list price, then subtract the print cost. [7]
A sample only: a $14.99 paperback is not “$14.99 for you.”
The print cost comes off.
Use the calculator. Do not guess.

## Money idea

Put a debut ebook at $2.99 or $3.99 if similar books in your corner live there.
$0.99 feels friendly and often pays you about a third of a dollar.
Save $0.99 for a short extra, not for the book you spent months on.

## Your action

Write your price and what you expect to keep.
Write what would make you change it.

# 7 Twenty-four ways a book can pay you

Pick a few. Do not try all of them in week one.
None of these is a guarantee. Each one is a door.

1. Charge a real ebook price. Stay in the 70 percent band when you can. A handful of $4.99 sales can beat a pile of $0.99 sales.

2. Make book one easy to buy and book two full price. The first book is the handshake. The second book is the payment.

3. Write the next book before you forget the reader. A second book is the most ordinary way a catalog starts to pay.

4. Link the books on a series page. One sale should show the rest.

5. After three books, sell a box set at a small discount. Some readers would rather buy the set once.

6. Add a paperback. Many readers will pay more for paper. Subtract the print cost before you celebrate.

7. Add large print if your readers are older or tired. It is the same book, another price.

8. Join Kindle Unlimited for 90 days if ebook reads are your market. You are paid for pages read, and you agree not to sell that ebook elsewhere during the term. Read the current terms. [5]

9. Run a short countdown, then go back to the normal price. A sale is a visit. The regular price is the business. Check countdown rules before you schedule one. [6]

10. Make the first book free for a few days only if book two is ready and linked. A free book with nothing to buy next is a gift, not a business.

11. Sell a workbook as its own short book. Checklists, prompts, and templates can be a $2.99 or $4.99 extra.

12. Sell a one-hour companion. A “field guide,” a recipe card set, or a troubleshooting list. Small, clear, and priced so you keep more than a few cents.

13. Turn the best chapter into a talk, a class, or a newsletter lesson, and point people back to the book. You get paid for the hour and for the book.

14. For a how-to book, offer a paid template pack on your own site. The book still has to stand alone. Do not hide the ending behind a paywall.

15. Translate one book that already sells. One language you can check is enough. A bad translation does not pay you twice. It refunds.

16. Record the audiobook after the ebook has real readers. Audio is a second product. It is a poor first bet if nobody wants the book yet.

17. Use a preorder so people can buy before launch day. You still have to finish on time.

18. Pick two categories where a reader like yours actually looks. The biggest category hides you. A true smaller shelf can be where the sale happens.

19. Put the promise in the first two lines of the description. Shoppers do not read paragraph four.

20. Keep every older book for sale and linked. Old books are how a catalog pays you in a quiet month.

21. Write a seasonal short and price it low, with a link to the main book. A holiday story, a new-year checklist, a summer guide.

22. Ask a library-friendly paperback price you can live with after print cost. One library sale will not make a career. A backlist of them can be a small, steady drip.

23. Teach the book to a group once, for a fee, if you like teaching. Ten people in a room can pay more than ten ebook sales. Do not promise the room will fill.

24. Spend on ads only after you know what one sale pays you. If a click costs more than you keep, the ad is a donation. Chapter 8 shows the sum.

Skip these if you are on book one: mugs, a paid fan club, and a course with nothing behind it.
They add work. They rarely add money until strangers already want the book.

## Your action

Circle three ideas you can do in the next month.
One should be a price.
One should be the next book, even if it is only a sentence today.
One should be a format: paper, a short extra, or a page-read test.

# 8 Spend less than a sale brings back

A promotion needs a job.
“Get the book moving” is not a job.
“See if this newsletter can pay for itself” is a job.

Here is the sum in plain words.
If you keep about $1.88 a sale, a $60 ad has to bring about 32 extra sales before the ad is paid back.
Extra means sales you would not have had anyway.
The ad does not pay for your editor or your cover. Those are separate bills.

Free downloads are not sales.
Do not spend as if every free reader will buy book two.

Kindle Unlimited page-read money is real money. Count it in its own column.
Do not pretend an ad caused it just because both happened in the same week.

## Money idea

Write the most you can lose on a piece of paper before you pay.
When you hit that number, stop.
Curiosity is expensive.

## Your action

Cost of the test, money you keep per sale, sales needed to cover the test.
If the number of sales looks silly, do not buy the test.

# 9 Let the next book earn too

One book can pay you a little.
A row of related books can pay you again from the same happy reader.

Do not spend next month’s dream to excuse a loss today.
If book one loses money, book two is not a magic fix.
It is a second chance for a reader who liked book one.

A plain example.
Suppose 100 people buy book one.
30 of them later buy book two.
That is 30 percent, and it is only an example.
If book one keeps $0.35 and book two keeps $2.58, those 100 people bring you about $112, not 100 times the big number.
Do not count a third book unless you have a reason to think people will buy it.

Say the next book’s real title.
Link it when the link works.
Do not promise a date you cannot keep.

## Money idea

The cheapest sale you will ever make is the next book to someone who just finished this one.
Put that link where they can see it. At the end. In the description. On the series page.
""")

pic("catalog.png", "A small stack of related books on a shelf, suggesting a catalog a reader can continue.")

add("""
## Your action

Write one sentence: why a happy reader wants book two.
If you do not have that sentence, do not discount book one to “build a brand.”

# 10 Six calm weeks

Move the dates if the book is not ready.
A late, good book beats an on-time mess.

Four weeks out. Finish the edit. Write the reader sentence. Fix the page. Choose the price and the budget. Start inviting readers only if the book is actually readable.

Three weeks out. Send the advance file. Fix anything people cannot open.

Two weeks out. Read the ebook on your phone. Check the price rules again.

Publication week. Check the live page. Tell the people who asked. Send the link to advance readers when reviews can be posted. Write down what you spent and what you kept.

One week later. Send one gentle note, if you said you would. Change one thing at most.

Two weeks later. Look at the sheet. Pick one next step. A better page, a small test, a pause, or the first page of book two.

## Money idea

A calm launch protects the budget.
You can always spend more later. You cannot un-spend a bad week.

# 11 When the book is quiet

Do not blame “the algorithm” first.
Find the first broken step.

Nobody asked for the advance copy. The invitation is unclear, or the people are the wrong people. Fix the note before you pay to show it to more of them.

People cannot open the file. That is on you. Fix it.

People read and do not review. That happens. Check the link. Send the one reminder you planned. Then let it go.

Several readers name the same problem. Fix the book or the description. Do not argue with a review.

Sales lose money. More copies of a losing price are still a loss.
Pause the spend. Look at what you keep per sale.

## Money idea

A quiet book is information.
The fix is usually the page, the price, or the promise. It is rarely another $100.

## Your action

Change the earliest broken step.
Give that one change two weeks.

# 12 Words you can copy

Fill in the brackets.
These are your notes to readers.
Do not write their review for them.

## Public invitation

I am inviting readers who enjoy [subject] to get a free advance copy of [Title].
It is [one sentence and about how long], due out on [date].
If it fits you and you have time during [dates], ask for a copy here: [link].
An honest review later is welcome and optional.
No star rating is requested.
You can stop or say nothing. That is fine.

## Confirmation

Thank you for asking about [Title].
I plan to send the file on [date].
The book should be on sale on [date].
You can opt out any time at [how].
The free copy does not require a review.

## Delivery

Your copy of [Title] is here: [link].
To open it, [the steps you tested].
If it fails, reply and I will help.
I will send the store page when the book is live.
A review is optional.
Please do not pass the file around.

## Publication

[Title] is here: [link].
If you read it and want to leave an honest review, use the review button on that page.
It is optional.
If you do review, please say you received a free advance copy.
Thank you for your time.

## One gentle follow-up

A last note about [Title].
If you finished and want to leave an honest review, the page is [link].
If you already did, thank you.
If you would rather not, that is fine.
I will not ask again about this book.

## Inside the book

Thank you for reading.
If you want to help another reader decide, you can leave an honest review where you bought the book.
It is optional.
Your own experience is the useful part.

# 13 One money sheet

Keep this on one page.
You will forget the numbers if they live in five apps.

Price.
What you expect to keep per sale.
What you spent to get those sales.
Sales you think you would have had anyway.
What is left.
What you still owe the editor, the cover, and the tools.
The one change you will test next, and the date you will look again.

A useful line looks like this.
“Moved the ebook from $2.99 to $3.99. No new ads. Royalties went up. Traffic may have changed. I will wait four more weeks.”

Do not write “higher prices work.”
That sentence will fool you later.

## Your action

Fill the sheet for this month, even if the numbers are small.
Small and true is useful. Blank is not.

# 14 Look at the Kindle file

Your Word file is not the book the reader sees.
Open the preview.
Read it on a phone.

Use real headings.
Do not put the only copy of a warning inside a picture.
Do not depend on color alone.
If a table turns into mush on a small screen, use short lines instead.

Check the name, the title, the description, the cover, the categories, the price, and the countries.
Look at the file size and the royalty estimate KDP shows you.

If you used AI to draft text or pictures, say so where KDP asks.
Light editing help is not the same thing as a generated book.
Answer for the book you are actually uploading. [8]

## Money idea

A file that is hard to read gets returned.
A return takes the money back.
Previewing is part of getting paid.

## Your action

Have someone open the ebook, jump to a chapter, and follow one example.
Fix the place they get stuck.

# 15 Write one kind of book

Chapter 1 assumes the book exists.
If it does not, write it before you shop for a cover.

Pick one form.
A textbook teaches a next step. Use one meaning per word. Give the reader practice. Keep a familiar order unless a new order teaches better.
A popular book has to be easy to stay with. Voice, pictures, and the path matter more than worksheets.

Write one page of the words you will use.
Write one page of the path: what the reader can do, or what they understand, at the end.
Then fill the pages inside that path.

If you remember an example from someone else’s book, it is still theirs.
Write a new one.
Check any number a reader could look up.
Invented prices in your story should be labeled as examples.

## Money idea

A clear book in one form is easier to price, easier to describe, and easier to follow with a second book.
A mix of textbook and chatty essay is hard to sell because the reader does not know what they bought.

## Your action

One sentence for the form.
One page of words.
One page for the path.
Then go back to chapter 1.

# Official sources

These links are for the platform rules named above.
The money ideas and the sample sums are teaching tools, not Amazon rules.
Checked 27 September 2026. Look again before you publish.

[1] Amazon KDP Customer Reviews
https://kdp.amazon.com/en_US/help/topic/G202101910

[2] Amazon Community Guidelines. Use the link for your marketplace on the Customer Reviews page above.

[3] Amazon KDP eBook List Price Requirements
https://kdp.amazon.com/en_US/help/topic/G200634560

[4] Amazon KDP Digital Book Pricing Page
https://kdp.amazon.com/en_US/help/topic/G200634500

[5] Amazon KDP Select
https://kdp.amazon.com/en_US/select

[6] Amazon KDP Kindle Countdown Deals
https://kdp.amazon.com/en_US/help/topic/G201293780

[7] Amazon KDP Paperback Royalty
https://kdp.amazon.com/en_US/help/topic/G201834330

[8] Amazon KDP Content Guidelines
https://kdp.amazon.com/en_US/help/topic/G200672390

[9] Amazon KDP Kindle Publishing Guidelines
https://kdp.amazon.com/en_US/help/topic/GU72M65VRFPH43L6

Independent guide. Not affiliated with or endorsed by Amazon.
""")

d.save(out)
words = 0
for p in d.paragraphs:
    words += len(p.text.split())
print("saved", out.name, "words", words)
