"""Create Book 6 figures from published reference-design measurements.

The charts are original redraws of numerical claims in the cited primary sources.
They do not reproduce source artwork or present new measurements.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "chapters" / "Book6" / "fig"
FONT_DIR = Path(r"C:\Windows\Fonts")


def font(name, size):
    path = FONT_DIR / name
    return ImageFont.truetype(str(path), size)


def line(draw, xy, fill="#222222", width=2):
    draw.line(xy, fill=fill, width=width)


def figure_current_slope():
    w, h = 1200, 680
    im = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(im)
    title = font("arialbd.ttf", 31)
    label = font("arial.ttf", 23)
    small = font("arial.ttf", 18)
    d.text((w/2, 28), "A measured inductor-current slope is below the ideal slope", font=title, fill="#172b4d", anchor="ma")
    left, top, right, bottom = 150, 125, 1090, 535
    d.text((left, 86), "Current rise ΔI (A)", font=label, fill="#222222", anchor="ls")
    # Published test: 50 kHz, 8% duty gives a 1.6 us on-pulse.
    # Ideal slope 3.0 A/us; measured slope 2.8 A/us. Plot delta current only.
    xmax, ymax = 1.6, 5.0
    for y in range(0, 6):
        py = bottom - y / ymax * (bottom-top)
        line(d, (left, py, right, py), "#d9dee7", 1)
        d.text((left-18, py), str(y), font=small, fill="#333333", anchor="rm")
    for x in (0.0, 0.4, 0.8, 1.2, 1.6):
        px = left + x / xmax * (right-left)
        line(d, (px, top, px, bottom), "#e7eaf0", 1)
        d.text((px, bottom+14), f"{x:.1f}", font=small, fill="#333333", anchor="ma")
    line(d, (left, top, left, bottom), "#222222", 3)
    line(d, (left, bottom, right, bottom), "#222222", 3)
    d.text((w/2, 610), "Time since start of PWM pulse (µs)", font=label, fill="#222222", anchor="mm")
    # Map data points to image coordinates.
    def pt(t, di):
        return (left + t/xmax*(right-left), bottom - di/ymax*(bottom-top))
    ideal = [pt(0,0), pt(1.6,4.8)]
    measured = [pt(0,0), pt(1.6,4.48)]
    line(d, (*ideal[0], *ideal[1]), "#c43c30", 6)
    line(d, (*measured[0], *measured[1]), "#2367a8", 6)
    d.ellipse((ideal[1][0]-7, ideal[1][1]-7, ideal[1][0]+7, ideal[1][1]+7), fill="#c43c30")
    d.ellipse((measured[1][0]-7, measured[1][1]-7, measured[1][0]+7, measured[1][1]+7), fill="#2367a8")
    d.text((ideal[1][0]-32, ideal[1][1]-36), "4.80 A", font=small, fill="#c43c30", anchor="rm")
    # Keep the endpoint label well clear of the sloping measured line.
    d.text((measured[1][0]-70, measured[1][1]+92), "4.48 A", font=small, fill="#2367a8", anchor="rm")
    d.rectangle((left+24, top+16, left+48, top+40), fill="#c43c30")
    d.text((left+60, top+28), "Ideal: 3.0 A/µs", font=small, fill="#222222", anchor="lm")
    d.rectangle((left+285, top+16, left+309, top+40), fill="#2367a8")
    d.text((left+321, top+28), "Published measured slope: 2.8 A/µs", font=small, fill="#222222", anchor="lm")
    d.text((w/2, 662), "Reconstructed from Analog Devices CN0196 data; ΔI is relative to pulse start, not an absolute current trace.", font=small, fill="#555555", anchor="ms")
    im.save(OUT / "fig3_2.png", dpi=(220,220), optimize=True)


def figure_published_efficiency():
    w, h = 1200, 680
    im = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(im)
    title = font("arialbd.ttf", 31)
    label = font("arial.ttf", 23)
    small = font("arial.ttf", 18)
    d.text((w/2, 28), "Ideal energy balance and one published test point", font=title, fill="#172b4d", anchor="ma")
    left, top, right, bottom = 150, 120, 1080, 535
    d.text((left, 86), "Input power (W)", font=label, fill="#222222", anchor="ls")
    ymax = 16.0
    for y in range(0, 17, 2):
        py = bottom - y/ymax*(bottom-top)
        line(d, (left,py,right,py), "#d9dee7", 1)
        d.text((left-18,py), str(y), font=small, fill="#333333", anchor="rm")
    line(d,(left,top,left,bottom),"#222222",3)
    line(d,(left,bottom,right,bottom),"#222222",3)
    d.text((w/2, 610), "Case at 12.6 W delivered output", font=label, fill="#222222", anchor="mm")
    # Both cases deliver 12.6 W; the reported board has 1.8 W of losses.
    scale=(bottom-top)/ymax
    bars=[(390,12.6,0.0,"Ideal, lossless"),(790,12.6,1.8,"TI reference board")]
    for cx,useful,loss,name in bars:
        bw=180
        x0=cx-bw/2; x1=cx+bw/2
        yout=bottom-useful*scale
        d.rectangle((x0,yout,x1,bottom),fill="#3478b9")
        if loss:
            yloss=yout-loss*scale
            d.rectangle((x0,yloss,x1,yout),fill="#d9782d")
            d.text((cx,yloss-15),"14.4 W in",font=small,fill="#222222",anchor="ms")
            d.text((cx,(yloss+yout)/2),"1.8 W loss",font=small,fill="white",anchor="mm")
        else:
            d.text((cx,yout-15),"12.6 W in",font=small,fill="#222222",anchor="ms")
        d.text((cx,(yout+bottom)/2),"12.6 W\noutput",font=small,fill="white",anchor="mm",spacing=6,align="center")
        d.text((cx,bottom+20),name,font=small,fill="#222222",anchor="ma")
    # Legend
    d.rectangle((245, top+15, 270, top+40), fill="#3478b9")
    d.text((280,top+27),"Useful output",font=small,fill="#222222",anchor="lm")
    d.rectangle((470, top+15, 495, top+40), fill="#d9782d")
    d.text((505,top+27),"Reported converter loss",font=small,fill="#222222",anchor="lm")
    d.text((w/2, 662), "TI TIDU926; 12 V input, 1.05 V output, 12 A, 650 kHz, 25 °C. Efficiency derived from rounded reported powers.", font=small, fill="#555555", anchor="ms")
    im.save(OUT / "fig9_2.png", dpi=(220,220), optimize=True)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    figure_current_slope()
    figure_published_efficiency()
    print(OUT / "fig3_2.png")
    print(OUT / "fig9_2.png")
