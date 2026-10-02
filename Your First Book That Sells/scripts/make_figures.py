"""Teaching diagrams for the plain-language Kindle guide. Grayscale-safe."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

out = Path(__file__).resolve().parent.parent / "figures"
W, H = 1600, 900
NAVY = (12, 45, 90)
INK = (20, 20, 20)
PAPER = (255, 252, 246)
BAR = (30, 70, 120)
MUTED = (90, 90, 90)
LINE = (180, 180, 180)


def font(size):
    for name in ("calibri.ttf", "arial.ttf", "segoeui.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def canvas():
    im = Image.new("RGB", (W, H), PAPER)
    return im, ImageDraw.Draw(im)


def title(draw, text):
    draw.text((60, 36), text, fill=NAVY, font=font(42))


def keep_chart():
    im, d = canvas()
    title(d, "What you keep on one ebook sale")
    d.text((60, 100), "Teaching example. 2 MB file. No tax. Amazon.com rules as checked 27 September 2026.", fill=MUTED, font=font(24))
    rows = [
        ("$0.99", "35% band", "$0.35", 0.12),
        ("$2.99", "70% band", "$1.88", 0.40),
        ("$3.99", "70% band", "$2.58", 0.55),
        ("$4.99", "70% band", "$3.28", 0.70),
        ("$7.99", "70% band", "$5.38", 0.95),
    ]
    y = 180
    for price, band, keep, frac in rows:
        d.text((60, y), price, fill=INK, font=font(32))
        d.text((220, y), band, fill=MUTED, font=font(28))
        d.rectangle((520, y + 8, 520 + int(900 * frac), y + 48), fill=BAR)
        d.text((540 + int(900 * frac), y + 6), keep, fill=INK, font=font(32))
        y += 120
    d.text((60, 820), "Delivery of $0.30 is taken off before the 70% cut. It is not taken off in the 35% band.", fill=INK, font=font(26))
    im.save(out / "keep_by_price.png")


def weeks():
    im, d = canvas()
    title(d, "Six calm weeks")
    labels = [
        ("Week 4", "Edit. Promise.\nPrice. Invite."),
        ("Week 3", "Send the file.\nFix what breaks."),
        ("Week 2", "Read it\non a phone."),
        ("Live", "Check the page.\nTell people."),
        ("+1 week", "One note.\nOne change."),
        ("+2 weeks", "Read the sheet.\nPick one next step."),
    ]
    x = 40
    for i, (name, body) in enumerate(labels):
        d.rounded_rectangle((x, 220, x + 240, 700), radius=16, outline=NAVY, width=4, fill=(255, 255, 255))
        d.rectangle((x, 220, x + 240, 300), fill=NAVY)
        d.text((x + 24, 240), name, fill=(255, 255, 255), font=font(28))
        d.multiline_text((x + 24, 360), body, fill=INK, font=font(28), spacing=8)
        if i < 5:
            d.polygon([(x + 248, 450), (x + 268, 470), (x + 248, 490)], fill=NAVY)
        x += 260
    im.save(out / "six_weeks.png")


def ad_math():
    im, d = canvas()
    title(d, "When an ad cannot pay for itself")
    d.text((60, 140), "Teaching example. Not a bid you should copy.", fill=MUTED, font=font(26))
    lines = [
        "The example author keeps about $2.58 on a $3.99 sale.",
        "A click costs $0.30.",
        "1 sale from every 10 clicks means the ad costs $3.00 to make that $2.58.",
        "The click would need to cost about $0.26 or less to break even.",
        "If it costs more, fix the page before you raise the budget.",
    ]
    y = 230
    for line in lines:
        d.text((80, y), line, fill=INK, font=font(32))
        y += 100
    im.save(out / "ad_math.png")


def three():
    im, d = canvas()
    title(d, "Three ways the same reader pays you again")
    boxes = [
        ("Price", "A $3.99 sale can\nkeep about $2.58.\nA $0.99 sale keeps\nabout $0.35."),
        ("Next book", "30 of 100 buyers\nget book two.\nThat is a teaching\nexample, not a rate."),
        ("Another format", "Paperback, large print,\nor pages read.\nSubtract the real cost\nbefore you count it."),
    ]
    x = 50
    for name, body in boxes:
        d.rounded_rectangle((x, 200, x + 480, 780), radius=18, outline=NAVY, width=4, fill=(255, 255, 255))
        d.text((x + 36, 240), name, fill=NAVY, font=font(40))
        d.multiline_text((x + 36, 340), body, fill=INK, font=font(30), spacing=10)
        x += 520
    im.save(out / "three_ways.png")


def keep_test():
    im, d = canvas()
    title(d, "The keep test. Three lines, or you do not spend.")
    rows = [
        ("1. The keep", "Dollars left on one sale, from your KDP estimate."),
        ("2. The reader", "Who it is for. Who it is not for."),
        ("3. The date", "One change. The day you will judge it."),
    ]
    y = 200
    for name, body in rows:
        d.rounded_rectangle((80, y, 1520, y + 180), radius=16, outline=NAVY, width=4, fill=(255, 255, 255))
        d.text((120, y + 30), name, fill=NAVY, font=font(40))
        d.text((120, y + 100), body, fill=INK, font=font(32))
        y += 210
    im.save(out / "keep_test.png")


if __name__ == "__main__":
    keep_chart()
    weeks()
    ad_math()
    three()
    keep_test()
    print("figures ok")
