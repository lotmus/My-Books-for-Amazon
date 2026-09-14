# Fetch 14 real public-domain / NASA-ESA-style space photographs.
# Never invent Hubble / Planck / EHT / rover / Cassini frames.
# Writes figs/figNN.jpg at 1800x1350. Placeholders stay as figs/figNN_slot.png.
import io
import os
import ssl
import sys
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figs")
os.makedirs(OUT, exist_ok=True)
UA = "UniverseHasNoNow/1.0 (manuscript figure assembly; educational; contact: author)"

# Each entry: (figure number, credit key, process tag, url list)
# process: sun, disk, field, cmb, spiral, web, bullet, rim, eht, host, rover, europa, earth, tracks
PHOTOS = [
    (3, "sun", "sun", [
        "https://sdo.gsfc.nasa.gov/assets/img/browse/2015/10/27/20151027_000000_4096_HMIIF.jpg",
        "https://sdo.gsfc.nasa.gov/assets/img/browse/2017/09/06/20170906_000000_4096_HMIIF.jpg",
        "https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e001861/GSFC_20171208_Archive_e001861~large.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg?width=2048",
    ]),
    (4, "andromeda", "disk", [
        "https://cdn.spacetelescope.org/archives/images/large/heic1502a.jpg",
        "https://esahubble.org/media/archives/images/large/heic1502a.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Andromeda_Galaxy_560mm_FL.jpg?width=2048",
        "https://images-assets.nasa.gov/image/PIA04921/PIA04921~large.jpg",
    ]),
    (8, "hudf", "field", [
        "https://cdn.spacetelescope.org/archives/images/large/heic0611b.jpg",
        "https://esahubble.org/media/archives/images/large/heic0611b.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Hubble_ultra_deep_field_high_rez_edit1.jpg?width=2048",
        "https://images-assets.nasa.gov/image/hubble-ultra-deep-field/hubble-ultra-deep-field~large.jpg",
    ]),
    (9, "planck", "cmb", [
        "https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2013/03/planck_cmb/12583932-4-eng-GB/Planck_CMB.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Planck_CMB.jpg?width=2048",
        "https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2018/07/planck_s_view_of_the_cosmic_microwave_background/17552332-1-eng-GB/Planck_s_view_of_the_cosmic_microwave_background.jpg",
    ]),
    (14, "spiral", "spiral", [
        "https://cdn.spacetelescope.org/archives/images/large/opo9941a.jpg",
        "https://esahubble.org/media/archives/images/large/opo9941a.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/NGC_4414_(NASA-med).jpg?width=2048",
        "https://cdn.spacetelescope.org/archives/images/large/heic0506a.jpg",
    ]),
    (16, "sdss", "web", [
        "https://www.sdss.org/wp-content/uploads/2014/11/LSS_3Dslice.png",
        "https://www.sdss.org/wp-content/uploads/2014/10/sdss_pie2.jpg",
        "https://www.sdss4.org/wp-content/uploads/2014/11/LSS_3Dslice.png",
        "https://commons.wikimedia.org/wiki/Special:FilePath/2MASS_LSS_chart-NEW_Nasa.jpg?width=2048",
        "https://photojournal.jpl.nasa.gov/jpeg/PIA04248.jpg",
    ]),
    (17, "bullet", "bullet", [
        "https://chandra.harvard.edu/photo/2006/1e0657/1e0657.jpg",
        "https://chandra.si.edu/photo/2006/1e0657/1e0657.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Bulletcluster.jpg?width=2048",
        "https://chandra.harvard.edu/photo/2006/1e0657/1e0657_scale.jpg",
    ]),
    (18, "snr", "rim", [
        "https://cdn.spacetelescope.org/archives/images/large/heic0515a.jpg",
        "https://esahubble.org/media/archives/images/large/heic0515a.jpg",
        "https://chandra.harvard.edu/photo/2004/kepler/kepler.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Kepler%27s_Supernova_Remnant.jpg?width=2048",
        "https://cdn.spacetelescope.org/archives/images/large/heic0609a.jpg",
    ]),
    (20, "eht", "eht", [
        "https://cdn.eso.org/images/large/eso1907a.jpg",
        "https://eventhorizontelescope.org/files/eht/files/20190410-78m-4000x2330.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Black_hole_-_Messier_87_crop_max_res.jpg?width=2048",
        "https://cdn.eso.org/images/screen/eso1907a.jpg",
    ]),
    (24, "host", "host", [
        "https://cdn.spacetelescope.org/archives/images/large/heic0815a.jpg",
        "https://esahubble.org/media/archives/images/large/heic0815a.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Messier_87_Hubble_WikiSky.jpg?width=2048",
        "https://cdn.spacetelescope.org/archives/images/large/heic0814a.jpg",
    ]),
    (25, "rover", "rover", [
        "https://photojournal.jpl.nasa.gov/jpeg/PIA23764.jpg",
        "https://mars.nasa.gov/system/resources/detail_files/25058_PIA23764-web.jpg",
        "https://images-assets.nasa.gov/image/PIA23764/PIA23764~large.jpg",
        "https://photojournal.jpl.nasa.gov/jpeg/PIA24924.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/PIA24924-MarsPerseveranceRover-FirstDrive-20210304.jpg?width=2048",
    ]),
    (29, "europa", "europa", [
        "https://photojournal.jpl.nasa.gov/jpeg/PIA19048.jpg",
        "https://photojournal.jpl.nasa.gov/jpeg/PIA01299.jpg",
        "https://images-assets.nasa.gov/image/PIA19048/PIA19048~large.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Europa-moon.jpg?width=2048",
    ]),
    (41, "earth", "earth", [
        "https://images-assets.nasa.gov/image/as08-14-2383/as08-14-2383~large.jpg",
        "https://images-assets.nasa.gov/image/as08-14-2383/as08-14-2383~orig.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/NASA-Apollo8-Dec24-Earthrise.jpg?width=2048",
        "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a410/AS8-14-2383HR.jpg",
    ]),
    (45, "tracks", "tracks", [
        "https://photojournal.jpl.nasa.gov/jpeg/PIA16052.jpg",
        "https://images-assets.nasa.gov/image/PIA16052/PIA16052~large.jpg",
        "https://photojournal.jpl.nasa.gov/jpeg/PIA16142.jpg",
        "https://mars.nasa.gov/system/resources/detail_files/4454_pia16052-full.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/PIA16052-MarsCuriosityRover-Tracks-20120822.jpg?width=2048",
    ]),
]


def fetch(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "image/*,*/*"})
    with urllib.request.urlopen(req, timeout=90, context=ctx) as r:
        data = r.read()
        ctype = r.headers.get("Content-Type", "")
    if len(data) < 8000:
        raise ValueError("too small (%d bytes) %s" % (len(data), ctype))
    if data[:9].lstrip().lower().startswith(b"<!doctype") or data[:6].lower().startswith(b"<html"):
        raise ValueError("html, not an image")
    return data


def open_rgb(data):
    im = Image.open(io.BytesIO(data))
    if im.mode in ("P", "RGBA", "LA"):
        bg = Image.new("RGB", im.size, (255, 255, 255))
        im = im.convert("RGBA")
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")


def crop_43(im, cx=0.5, cy=0.5, zoom=1.0):
    w, h = im.size
    if zoom > 1.0:
        nw, nh = int(w / zoom), int(h / zoom)
        x0 = max(0, int((w - nw) * cx))
        y0 = max(0, int((h - nh) * cy))
        im = im.crop((x0, y0, x0 + nw, y0 + nh))
        w, h = im.size
    target = 4 / 3
    if w / h > target:
        nw = int(h * target)
        x = int((w - nw) * cx)
        im = im.crop((x, 0, x + nw, h))
    elif w / h < target:
        nh = int(w / target)
        y = int((h - nh) * cy)
        im = im.crop((0, y, w, y + nh))
    return im.resize((1800, 1350), Image.Resampling.LANCZOS)


def punch(im, contrast=1.18, sharpness=1.08):
    im = ImageEnhance.Contrast(im).enhance(contrast)
    im = ImageEnhance.Sharpness(im).enhance(sharpness)
    return ImageOps.autocontrast(im, cutoff=1)


def label(im, items, fill=(255, 255, 255), stroke=(0, 0, 0)):
    d = ImageDraw.Draw(im)
    try:
        fnt = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 78)
    except OSError:
        fnt = ImageFont.load_default()
    for xy, text in items:
        d.text(xy, text, font=fnt, fill=fill, anchor="mm", stroke_width=4, stroke_fill=stroke)
    return im


def process(im, tag):
    if tag == "sun":
        return punch(crop_43(im, 0.5, 0.5, 1.15), 1.12, 1.0)
    if tag == "disk":
        return punch(crop_43(im, 0.48, 0.50, 1.55), 1.22)
    if tag == "field":
        return punch(crop_43(im, 0.42, 0.38, 1.8), 1.25, 1.2)
    if tag == "cmb":
        g = ImageOps.grayscale(im)
        g = ImageOps.autocontrast(g, cutoff=0.5)
        rgb = Image.merge("RGB", (g, g, g))
        rgb = crop_43(rgb, 0.5, 0.48, 1.05)
        return label(rgb, [((450, 200), "warmer"), ((1350, 200), "cooler")],
                     fill=(230, 230, 230), stroke=(20, 20, 20))
    if tag == "spiral":
        return punch(crop_43(im, 0.5, 0.5, 1.25), 1.2)
    if tag == "web":
        rgb = punch(crop_43(im, 0.55, 0.5, 1.1), 1.35, 1.15)
        # threshold so filaments read as dark-on-light if the map is already high-key
        return rgb
    if tag == "bullet":
        return punch(crop_43(im, 0.5, 0.45, 1.05), 1.2)
    if tag == "rim":
        return punch(crop_43(im, 0.5, 0.5, 1.2), 1.22)
    if tag == "eht":
        im = crop_43(im, 0.5, 0.5, 1.35)
        im = ImageEnhance.Contrast(im).enhance(1.45)
        im = ImageEnhance.Brightness(im).enhance(1.08)
        return ImageOps.autocontrast(im, cutoff=2)
    if tag == "host":
        return punch(crop_43(im, 0.5, 0.5, 1.2), 1.25)
    if tag == "rover":
        return punch(crop_43(im, 0.5, 0.45, 1.15), 1.15)
    if tag == "europa":
        return punch(crop_43(im, 0.5, 0.5, 1.2), 1.2)
    if tag == "earth":
        return punch(crop_43(im, 0.55, 0.42, 1.05), 1.15)
    if tag == "tracks":
        return punch(crop_43(im, 0.5, 0.55, 1.1), 1.18)
    return punch(crop_43(im))


def one(n, key, tag, urls):
    dest = os.path.join(OUT, "fig%02d.jpg" % n)
    last = None
    for url in urls:
        try:
            print("try fig%02d %s" % (n, url[:88]))
            data = fetch(url)
            im = open_rgb(data)
            if min(im.size) < 400:
                raise ValueError("tiny image %s" % (im.size,))
            out = process(im, tag)
            out.save(dest, "JPEG", quality=90, optimize=True)
            print("wrote", dest, out.size)
            return dest
        except Exception as e:
            last = e
            print("  fail:", e)
    raise RuntimeError("fig%02d (%s) failed: %s" % (n, key, last))


if __name__ == "__main__":
    wanted = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else None
    bad = []
    for n, key, tag, urls in PHOTOS:
        if wanted and n not in wanted:
            continue
        try:
            one(n, key, tag, urls)
        except Exception as e:
            print("MISSING", n, e)
            bad.append(n)
    print("done. missing:", bad)
    sys.exit(1 if bad else 0)
