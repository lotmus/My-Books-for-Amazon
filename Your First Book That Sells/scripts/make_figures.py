#!/usr/bin/env python3
"""Draw every figure used in Your First Book That Sells, in one visual style.

One palette (navy on cream, grayscale-safe: every colour also carries a word),
one font, one size (1600 x 900 px unless a tall diagram needs more).
Run from anywhere:  python scripts/make_figures.py
Writes PNG files into figures/. Docx only: nothing here builds PDF or EPUB.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent.parent / "figures"
NAVY, INK, PAPER = "#0C2D5A", "#1A1A1A", "#FFFCF6"
MUTED, PALE, LIGHT = "#5A5A5A", "#DCE4EF", "#F2F5FA"
GO, STOP, WARN = "#2E6B47", "#9E3B1E", "#B5832A"
CHECKED = "Amazon.com rules checked 3 October 2026"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK, "text.parse_math": False})


def fig(w=16, h=9):
    f = plt.figure(figsize=(w, h), dpi=100, facecolor=PAPER)
    return f


def head(f, title, sub=None):
    f.text(0.04, 0.93, title, fontsize=30, color=NAVY, weight="bold", va="center")
    if sub:
        f.text(0.04, 0.875, sub, fontsize=16, color=MUTED, va="center")


def canvas(f, rect=(0.03, 0.04, 0.94, 0.80)):
    ax = f.add_axes(rect)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    return ax


def box(ax, x, y, w, h, text, fill="white", edge=NAVY, color=INK, size=16, bold=False, lw=2.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.2",
                                fc=fill, ec=edge, lw=lw))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, color=color,
            weight="bold" if bold else "normal", linespacing=1.35, wrap=True)


def arrow(ax, x1, y1, x2, y2, label=None, lx=0, ly=0, color=NAVY):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=22,
                                 lw=2.2, color=color, shrinkA=2, shrinkB=2))
    if label:
        ax.text((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, label, fontsize=15, color=color,
                weight="bold", ha="center", va="center",
                bbox=dict(fc=PAPER, ec="none", pad=1.5))


def save(f, name):
    f.savefig(OUT / name, facecolor=PAPER)
    plt.close(f)


# 1 -- Part I: the keep test --------------------------------------------------
def keep_test():
    f = fig(); head(f, "The keep test: three lines, or you do not spend",
                    "Write all three before you pay for an ad, a promotion, or a stack of free copies.")
    ax = canvas(f)
    rows = [("1  The keep", "Dollars left on one sale, from your KDP royalty estimate (Chapter 3)."),
            ("2  The reader", "Who the book is for. Who it is not for (Chapter 2)."),
            ("3  The date", "The one change you will make, and the day you will look at the result.")]
    for i, (a, b) in enumerate(rows):
        y = 70 - i * 31
        box(ax, 2, y, 96, 24, "", fill="white")
        ax.text(5, y + 15.5, a, fontsize=24, color=NAVY, weight="bold", va="center")
        ax.text(5, y + 6.5, b, fontsize=18, color=INK, va="center")
    save(f, "keep_test.png")


# 2 -- Part I: keep by price --------------------------------------------------
def keep_by_price():
    f = fig(); head(f, "What you keep on one ebook sale",
                    "Worked example: 2 MB file, no VAT, 70% option selected where the price allows it. " + CHECKED + ".")
    ax = f.add_axes([0.20, 0.13, 0.70, 0.68], facecolor=PAPER)
    rows = [("$0.99", "35%", 0.35), ("$2.99", "70%", 1.88), ("$3.99", "70%", 2.58),
            ("$4.99", "70%", 3.28), ("$7.99", "70%", 5.38)]
    ys = list(range(len(rows)))[::-1]
    for y, (p, band, k) in zip(ys, rows):
        ax.barh(y, k, color=NAVY if band == "70%" else STOP, height=0.55)
        ax.text(k + 0.08, y, f"${k:.2f}", va="center", fontsize=20, color=INK)
        ax.text(-0.15, y, f"{p}  ({band})", va="center", ha="right", fontsize=20, color=INK)
    ax.set_xlim(0, 6.3); ax.set_yticks([]); ax.set_xlabel("Royalty kept per sale (USD)", fontsize=16)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    f.text(0.04, 0.04, "70%: 0.70 × (price − $0.30 delivery).  35%: 0.35 × price, no delivery charge.  "
           "Your own KDP estimate replaces these numbers.", fontsize=15, color=MUTED)
    save(f, "keep_by_price.png")


# 3 -- Part I: break-even cost per click -------------------------------------
def break_even_cpc():
    f = fig(); head(f, "The most a click can cost before the ad loses money",
                    "Worked example: keep $2.58 per sale ($3.99 ebook). Maximum cost per click = keep × conversion rate.")
    ax = f.add_axes([0.09, 0.13, 0.86, 0.68], facecolor=PAPER)
    conv = [i / 1000 for i in range(5, 151)]
    ax.plot([c * 100 for c in conv], [2.58 * c for c in conv], color=NAVY, lw=4)
    ax.fill_between([c * 100 for c in conv], [2.58 * c for c in conv], 0.45, color=STOP, alpha=0.10)
    ax.fill_between([c * 100 for c in conv], 0, [2.58 * c for c in conv], color=GO, alpha=0.10)
    ax.text(1.0, 0.41, "ABOVE THE LINE: each sale costs more than it keeps", color=STOP, fontsize=16, weight="bold")
    ax.text(9, 0.04, "BELOW THE LINE: the ad pays for itself", color=GO, fontsize=16, weight="bold")
    for c, lab in ((0.05, "5% converts: ceiling $0.13"), (0.10, "10% converts: ceiling $0.26")):
        ax.plot(c * 100, 2.58 * c, "o", color=NAVY, ms=11)
        ax.text(c * 100 + 0.3, 2.58 * c - 0.03, lab, fontsize=16, color=INK)
    ax.plot(10, 0.30, "s", color=STOP, ms=12)
    ax.text(5.2, 0.315, "$0.30 click at 10%: $3.00 of ads per $2.58 kept", fontsize=16, color=STOP)
    ax.set_xlim(0.5, 15); ax.set_ylim(0, 0.45)
    ax.set_xlabel("Sales per 100 clicks (conversion rate, %)", fontsize=16)
    ax.set_ylabel("Break-even cost per click (USD)", fontsize=16)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(alpha=0.25)
    save(f, "break_even_cpc.png")


# 4 -- Part I: six calm weeks -------------------------------------------------
def six_weeks():
    f = fig(); head(f, "Six calm weeks around publication",
                    "Move the dates if the book is not ready. One job per week.")
    ax = canvas(f)
    cols = [("4 weeks before", "Finish the edit.\nWrite the two\nreader sentences.\nWrite the keep.\nInvite readers."),
            ("3 weeks before", "Send the advance\nfile. Fix what\nreaders cannot\nopen."),
            ("2 weeks before", "Read the ebook\non a phone.\nCreate KDP\nentries early\n(2 per format\nper week)."),
            ("Publication\nweek", "Check the live\npage. Tell people\nwho asked. Send\nthe review link\nwhen reviews\nopen."),
            ("1 week after", "One optional\nfollow-up note.\nChange at most\none thing."),
            ("2 weeks after", "Read the money\nsheet. Pick one\nnext step.")]
    w = 14.6
    for i, (h, b) in enumerate(cols):
        x = 1 + i * 16.5
        box(ax, x, 74, w, 14, h, fill=NAVY, color="white", size=16, bold=True)
        box(ax, x, 6, w, 62, b, fill="white", size=15)
        if i < 5:
            arrow(ax, x + w + 0.4, 81, x + 16.3, 81)
    save(f, "six_weeks.png")


# 5 -- Ch 16: workflow --------------------------------------------------------
def workflow():
    f = fig(16, 10); head(f, "The self-publishing pipeline in this book",
                          "Each stage is one chapter of the full guide. Part I walks the same path faster.")
    ax = canvas(f, (0.03, 0.03, 0.94, 0.82))
    steps = [("Choose and write", "Ch. 19–20"), ("Format", "Ch. 21"), ("Cover", "Ch. 22"),
             ("Metadata,\npage", "Ch. 23"), ("Price", "Ch. 24"), ("Launch", "Ch. 25"),
             ("Ads (optional)", "Ch. 26"), ("Get paid", "Ch. 27"), ("Select or wide", "Ch. 28"),
             ("Next book", "Ch. 30")]
    for i, (a, b) in enumerate(steps):
        r, c = divmod(i, 5)
        x = 1 + c * 20; y = 58 - r * 44
        box(ax, x, y, 16, 22, f"{a}\n{b}", fill=NAVY if r == 0 else "white",
            color="white" if r == 0 else NAVY, size=17, bold=True)
        if c < 4:
            arrow(ax, x + 16.6, y + 11, x + 19.6, y + 11)
    arrow(ax, 89, 57.5, 9, 36.5)
    ax.text(50, 47, "then on to launch", ha="center", fontsize=15, color=MUTED)
    save(f, "workflow.png")


# 6 -- Ch 17: royalty cliff ---------------------------------------------------
def royalty_cliff():
    f = fig(); head(f, "The royalty cliff: 35% against 70%",
                    "Worked example: 2 MB file, no VAT. " + CHECKED + " (70% band $2.99–$12.99).")
    ax = f.add_axes([0.08, 0.12, 0.88, 0.70], facecolor=PAPER)
    p35 = [x / 100 for x in range(99, 2001)]
    ax.plot(p35, [0.35 * p for p in p35], color=STOP, lw=3.5, label="35% option: 0.35 × price")
    p70 = [x / 100 for x in range(299, 1300)]
    ax.plot(p70, [0.70 * (p - 0.30) for p in p70], color=NAVY, lw=4.5, label="70% option: 0.70 × (price − $0.30)")
    ax.axvspan(2.99, 12.99, color=PALE, alpha=0.6)
    ax.text(8.0, 9.4, "70% band on Amazon.com", ha="center", color=NAVY, fontsize=16, weight="bold")
    for p, k, t, dx, dy in ((2.49, 0.87, "$2.49 → $0.87", -1.9, 1.2), (2.99, 1.88, "$2.99 → $1.88", -2.6, 2.6),
                            (4.99, 3.28, "$4.99 → $3.28", 0.3, 0.9), (12.99, 8.88, "$12.99 → $8.88", 0.4, -0.2),
                            (13.99, 4.90, "$13.99 → $4.90", 0.4, -1.4)):
        ax.plot(p, k, "o", color=INK, ms=9)
        ax.text(p + dx, k + dy, t, fontsize=16, color=INK)
    ax.set_xlim(0, 20); ax.set_ylim(0, 10)
    ax.set_xlabel("Ebook list price (USD)", fontsize=16); ax.set_ylabel("Royalty kept per sale (USD)", fontsize=16)
    ax.legend(loc="lower right", fontsize=15, frameon=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(alpha=0.25)
    save(f, "royalty_cliff.png")


# 7 -- Ch 22: product page flow ----------------------------------------------
def product_page():
    f = fig(16, 10); head(f, "How a shopper reads a product page",
                          "Each step must answer the shopper's question before they move on.")
    ax = canvas(f, (0.03, 0.03, 0.94, 0.82))
    steps = [("Thumbnail", "Can I read the title?\nWhat kind of book?", "Ch. 5, 22"),
             ("Title and subtitle", "Is the promise\nfor me?", "Ch. 23"),
             ("First two lines", "Who is it for?\nWhat do I get?", "Ch. 4"),
             ("Bullets and fit", "What exactly is\ninside? Who is it\nnot for?", "Ch. 23"),
             ("Sample", "Do I reach what\nI came for fast?", "Ch. 4"),
             ("Price and reviews", "Is it worth the\nprice? Do others\nagree?", "Ch. 3, 6")]
    for i, (a, b, c) in enumerate(steps):
        x = 1 + i * 16.5
        box(ax, x, 62, 14.6, 16, a.replace(" and ", "\nand "), fill=NAVY, color="white", size=15, bold=True)
        box(ax, x, 22, 14.6, 34, b, fill="white", size=15)
        ax.text(x + 7.3, 15, c, ha="center", fontsize=14, color=MUTED)
        if i < 5:
            arrow(ax, x + 15, 70, x + 16.3, 70)
    ax.text(50, 4, "Not allowed in the KDP description: review quotes, requests for reviews, prices, "
            "time-sensitive offers, URLs [17].", ha="center", fontsize=15, color=STOP)
    save(f, "product_page_flow.png")


# 8 -- Ch 23: pricing paths ---------------------------------------------------
def pricing_paths():
    f = fig(); head(f, "Which pricing path are you on?",
                    "Recommendation, not a platform rule. Prices are Amazon.com examples inside the 70% band.")
    ax = canvas(f)
    box(ax, 32, 78, 36, 13, "Does a paid book two already exist\nfor the same reader?", fill=NAVY, color="white",
        size=17, bold=True)
    arrow(ax, 40, 77, 24, 66, "No", -3, 1, STOP)
    arrow(ax, 60, 77, 76, 66, "Yes", 3, 1, GO)
    box(ax, 4, 46, 40, 18, "Debut or standalone\nBook one must earn on its own.", fill=LIGHT, size=17, bold=True)
    box(ax, 56, 46, 40, 18, "Series or catalog\nBook one can carry the introduction.", fill=LIGHT, size=17, bold=True)
    box(ax, 4, 6, 40, 34, "Launch inside the 70% band\n($2.99–$4.99 for most first books).\n"
        "Hold through the first weeks.\nRaise by $1 only when reviews exist\nand sales hold. No $0.99 week:\n"
        "there is nothing to recover it.", size=15)
    box(ax, 56, 6, 40, 34, "Book one: a short discount, a\nCountdown Deal, or free days (Select),\n"
        "or permanently free (wide only).\nBooks two onward stay in the 70%\nband and carry the margin.\n"
        "Check read-through before you cut.", size=15)
    arrow(ax, 24, 45.5, 24, 40.5); arrow(ax, 76, 45.5, 76, 40.5)
    save(f, "pricing_paths.png")


# 9 -- Ch 25: break-even ACOS -------------------------------------------------
def break_even_acos():
    f = fig(); head(f, "Break-even ACOS: when an ad pays for itself",
                    "Worked example: $4.99 ebook keeping $3.28. Break-even ACOS = 3.28 ÷ 4.99 ≈ 66%.")
    ax = f.add_axes([0.09, 0.12, 0.86, 0.70], facecolor=PAPER)
    ac = [x / 10 for x in range(150, 1401)]
    prof = [10 * (3.28 / 4.99) / (a / 100) - 10 for a in ac]
    ax.plot(ac, prof, color=NAVY, lw=4)
    ax.axhline(0, color=MUTED, lw=1.2); ax.axvline(65.7, color=MUTED, ls="--", lw=1.5)
    ax.axvspan(15, 65.7, color=GO, alpha=0.08); ax.axvspan(65.7, 140, color=STOP, alpha=0.08)
    ax.text(20, 26, "PAYS FOR ITSELF", color=GO, fontsize=18, weight="bold")
    ax.text(95, 26, "LOSES MONEY", color=STOP, fontsize=18, weight="bold")
    ax.text(67, -8.5, "break-even ≈ 66%", fontsize=16, color=INK)
    for a, p, t, dx, dy in ((40.1, 6.40, "$10 → 5 sales: ACOS 40%, about +$6.40", 2, 2),
                            (100.2, -3.44, "$10 → 2 sales: ACOS 100%, about −$3.44", -12, -4.5)):
        ax.plot(a, p, "o", color=INK, ms=10); ax.text(a + dx, p + dy, t, fontsize=16, color=INK)
    ax.set_xlim(15, 140); ax.set_ylim(-10, 30)
    ax.set_xlabel("ACOS (%) = ad spend ÷ ad-attributed sales", fontsize=16)
    ax.set_ylabel("Royalty minus ad spend, per $10 spent (USD)", fontsize=16)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(alpha=0.25)
    save(f, "break_even_acos.png")


# 10 -- Ch 27: Select or wide -------------------------------------------------
def select_vs_wide():
    f = fig(); head(f, "KDP Select or wide: one 90-day test",
                    "Platform rules from KDP Select pages [5]; the decision itself is yours to test.")
    ax = canvas(f)
    box(ax, 4, 52, 42, 36, "KDP Select (90 days, auto-renews)\n\nEbook sold only through Amazon\n"
        "Paid for Kindle Unlimited page reads\nFree days OR one Countdown Deal\n70% in Brazil, Japan, Mexico, India\n"
        "Print and audio may be sold anywhere", fill=LIGHT, size=15)
    box(ax, 54, 52, 42, 36, "Wide\n\nEbook in other stores and libraries\nNo page-read income\n"
        "Each store's own royalty and tools\nPermanently free book one possible\nMore uploads to manage",
        fill="white", size=15)
    box(ax, 25, 24, 50, 16, "Run one term. Write down: sales, page reads,\nand what the same readers would have paid elsewhere.",
        fill=NAVY, color="white", size=16, bold=True)
    arrow(ax, 25, 51.5, 40, 40.5); arrow(ax, 75, 51.5, 60, 40.5)
    arrow(ax, 38, 23.5, 22, 14.5, "page reads carry\nreal weight", -13, 2)
    arrow(ax, 62, 23.5, 78, 14.5, "other stores or\nlibraries matter more", 15, 2)
    box(ax, 6, 2, 30, 11, "Renew Select", fill="white", size=17, bold=True)
    box(ax, 64, 2, 30, 11, "Untick renewal, go wide", fill="white", size=17, bold=True)
    save(f, "select_vs_wide.png")


# 11 -- Ch 31: review eligibility --------------------------------------------
def review_eligibility():
    f = fig(16, 10); head(f, "Can this advance reader post a review?",
                          "Platform rules: Amazon Community Guidelines and KDP Customer Reviews [1] [2]; Goodreads guidelines [16].")
    ax = canvas(f, (0.03, 0.03, 0.94, 0.82))
    box(ax, 34, 86, 32, 10, "Reader has your free copy", fill=NAVY, color="white", size=17, bold=True)
    arrow(ax, 42, 85.5, 24, 78, "Amazon", -4, 1); arrow(ax, 58, 85.5, 78, 78, "Goodreads", 5, 1)
    qs = ["Friend, relative, colleague,\nbusiness partner, or anyone\nwith a financial interest?",
          "Was a review required, a rating\nrequested, or anything beyond the\nbook offered (gift card, refund)?",
          "Spent $50 on Amazon.com with a\ncredit or debit card in the past\n12 months (promo discounts excluded)?"]
    ans = [("Yes: may not\nreview", STOP), ("Yes: the review\nbreaks the rules", STOP), ("No: cannot\npost yet", STOP)]
    for i, q in enumerate(qs):
        y = 60 - i * 22
        box(ax, 3, y, 36, 16, q, fill="white", size=14)
        box(ax, 42.5, y + 2, 17.5, 12, ans[i][0], fill=LIGHT, edge=ans[i][1], color=ans[i][1], size=13, bold=True)
        arrow(ax, 39.5, y + 8, 42.5, y + 8)
        if i < 2:
            arrow(ax, 21, y - 0.5, 21, y - 5.5, "No", 3, 0, GO)
    arrow(ax, 21, 15.5, 21, 9.5, "Yes", 3, 0, GO)
    box(ax, 3, 0.5, 36, 8, "Can post an honest review after the\npage is live (no Verified Purchase badge)",
        fill="white", edge=GO, color=GO, size=13, bold=True)
    box(ax, 64, 56, 32, 20, "No spend minimum.\nMust shelve the book as Read,\nCurrently Reading, or Did Not\nFinish to rate it.",
        fill="white", size=14)
    arrow(ax, 80, 55.5, 80, 49.5)
    box(ax, 64, 30, 32, 19, "Pre-publication: confirms reading\nand names the source of the copy\n(author, publisher, giveaway, other).",
        fill="white", size=14)
    arrow(ax, 80, 29.5, 80, 23.5)
    box(ax, 64, 12, 32, 11, "Can rate before publication.\nNot an Amazon review.", fill="white", edge=GO, color=GO,
        size=14, bold=True)
    save(f, "review_eligibility.png")


# 12 -- Ch 32: AI disclosure --------------------------------------------------
def ai_disclosure():
    f = fig(16, 10); head(f, "Do I declare this to KDP as AI-generated?",
                          "Platform rule: KDP Content Guidelines, AI content [8]. Ask once for text, once for images, once for translation.")
    ax = canvas(f, (0.03, 0.03, 0.94, 0.82))
    box(ax, 30, 84, 40, 12, "For this piece of text, image (cover or\ninterior), or translation:", fill=NAVY,
        color="white", size=17, bold=True)
    arrow(ax, 50, 83.5, 50, 75.5)
    box(ax, 26, 58, 48, 17, "Did an AI tool create the actual content,\neven if you edited it heavily afterwards?",
        fill="white", size=16, bold=True)
    arrow(ax, 30, 57.5, 18, 46.5, "Yes", -3, 1, STOP)
    arrow(ax, 70, 57.5, 82, 46.5, "No", 3, 1, GO)
    box(ax, 2, 24, 34, 22, "AI-GENERATED\nDeclare it when you publish\nor republish the book.", fill=LIGHT,
        edge=STOP, color=STOP, size=16, bold=True)
    box(ax, 62, 24, 36, 22, "You created it; a tool only edited,\nrefined, error-checked, or helped\nyou brainstorm?",
        fill="white", size=15)
    arrow(ax, 80, 23.5, 80, 15.5, "Yes", 3, 0, GO)
    box(ax, 62, 1, 36, 14, "AI-ASSISTED\nNo declaration required.", fill=LIGHT, edge=GO, color=GO, size=16, bold=True)
    box(ax, 2, 1, 54, 17, "Either way: you are responsible for the content, its accuracy,\nand its rights. "
        "In the U.S., machine-written expression\nhas no copyright owner (Chapter 33).", fill="white", size=14)
    save(f, "ai_disclosure.png")


ALL = [keep_test, keep_by_price, break_even_cpc, six_weeks, workflow, royalty_cliff, product_page,
       pricing_paths, break_even_acos, select_vs_wide, review_eligibility, ai_disclosure]

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for fn in ALL:
        fn()
    print(f"drew {len(ALL)} figures into {OUT}")
