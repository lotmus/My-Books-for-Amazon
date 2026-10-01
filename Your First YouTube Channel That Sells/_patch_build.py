from pathlib import Path

p = Path("build_docx.py")
t = p.read_text(encoding="utf-8")

t = t.replace("line_spacing = 1.08", "line_spacing = 1.15", 1)
t = t.replace(
    'doc.styles["Normal"].paragraph_format.space_after = Pt(7)',
    'doc.styles["Normal"].paragraph_format.space_after = Pt(8)',
    1,
)
old_h2 = 'doc.styles["Heading 2"].font.size = Pt(14)\n'
new_h2 = (
    'doc.styles["Heading 2"].font.size = Pt(14)\n'
    '    doc.styles["Heading 2"].paragraph_format.space_before = Pt(12)\n'
    '    doc.styles["Heading 2"].paragraph_format.space_after = Pt(6)\n'
)
if old_h2 not in t:
    raise SystemExit("heading 2 line missing")
t = t.replace(old_h2, new_h2, 1)
t = t.replace("run.font.size = Pt(10)\n", "run.font.size = Pt(10.5)\n", 1)

old_ch5 = (
    "Affiliate-link placement is creator consensus plus a disclosure habit, not a promise of income.*"
)
new_ch5 = (
    "Affiliate-link placement is creator consensus plus a disclosure habit, not a promise of income. "
    "Using one offer on every site is editorial. Instagram’s link sticker and TikTok’s profile-website page are cited in the chapter. "
    "Confirm each tap on a phone.*"
)
if old_ch5 not in t:
    raise SystemExit("chapter 5 source line missing")
t = t.replace(old_ch5, new_ch5, 1)

old_interviews = (
    "[Ali Abdaal, Mixergy](https://mixergy.com/interviews/youtubes-most-popular-productivity-creator/).\","
)
new_interviews = (
    "[Ali Abdaal, Mixergy](https://mixergy.com/interviews/youtubes-most-popular-productivity-creator/). "
    "[Hannah Hart, The Verge, 19 October 2016](https://www.theverge.com/2016/10/19/13315924/hannah-hart-interview-youtube-buffering-my-drunk-kitchen).\","
)
if old_interviews not in t:
    raise SystemExit("interview line missing")
t = t.replace(old_interviews, new_interviews, 1)

extra_sources = '''    "[Instagram, editing your profile](https://help.instagram.com/936495066470190/) — lists adding a website to the profile. [Instagram link sticker](https://help.instagram.com/192168966243613) — a sticker on an organic Story can send a tap to a website.",
    "[TikTok, adding a website to your profile](https://support.tiktok.com/en/getting-started/setting-up-your-profile/adding-a-website-to-your-profile) — whether the control appears is on that page.",
'''
needle = '    "[FTC Endorsement Guides'
if needle not in t:
    raise SystemExit("ftc line missing")
t = t.replace(needle, extra_sources + needle, 1)

glossary_extra = '''    ("Closed captions", "A text track the viewer can turn on or off. The words can be searched. They are not burned into the picture."),
    ("Burned-in captions", "Words that are part of the picture. They stay on. They are a different choice from closed captions."),
    ("Series playlist", "A playlist YouTube can feature as the next video while someone is watching one of yours. The account has to be verified, the videos have to be yours, and a video can sit in only one series playlist."),
    ("Fader", "The volume slider in an editor. A music fader at about a tenth to a fifth of the way up is a position on that slider, not a measurement of loudness."),
    ("Text-to-speech", "A tool that reads a script aloud. Usable when the voice is not a clone of someone else. Cloning someone else’s voice is a consent question the tool does not answer for you."),
    ("Stock license", "The terms on one clip or track. “Free” and “free to use commercially” are different sentences. Read the line on that file before you publish it, including on a second site."),
    ("Offer page", "The page where a stranger sees the price and pays or books. The video is not that page unless the platform gives you a product shelf you are allowed to use."),
    ("Short", "A vertical video, 1080 by 1920. On YouTube, an address in a Short’s description or comments is not clickable. A Short can point at a long video. It cannot be the checkout."),
    ("Qualified Shorts views", "Public views of Shorts in the Shorts feed that YouTube counts toward the Shorts bars: 3 million in 90 days for the expanded program, or 10 million in 90 days for the Partner Program. They do not fill the long-form hour bars."),
'''
aff = '    ("Affiliate link", "A link that pays you if the viewer buys. Say so next to the link. The FTC pages in the sources list are the U.S. disclosure guidance this book points at."),\n'
if aff not in t:
    raise SystemExit("affiliate glossary missing")
t = t.replace(aff, aff + glossary_extra, 1)

p.write_text(t, encoding="utf-8", newline="\n")
print("patched", p.stat().st_size)
