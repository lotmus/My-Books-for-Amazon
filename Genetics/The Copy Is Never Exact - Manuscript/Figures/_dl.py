"""Resolve exact Commons titles and save figNN.jpg."""
import io, json, os, time, urllib.parse, urllib.request
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "CopyIsNeverExactFigureCredits/1.0 (book figure research; educational)"}

# exact titles to try, in preference order, per figure
WANTED = {
    0: ["File:Home DNA Testing Kit Tube (47400098641).jpg"],
    4: [
        "File:CSIRO ScienceImage 3567 Examining an agar dish for bacterial colonies as part of the bioremediation research.jpg",
        "File:CSIRO ScienceImage 3619 Examining an agar dish for bacterial colonies as part of the bioremediation research.jpg",
    ],
    17: ["File:StThomasAbbeyBrno.jpg"],
    29: ["File:A ewe and her lamb at Reed Ranch (40871239920).jpg"],
    33: ["File:Fresh tomatoes stacked at market stall.jpg"],
    30: ["File:Havanese Litter.png"],
}

def api(params, tries=5):
    url = API + "?" + urllib.parse.urlencode(dict(params, format="json"))
    for i in range(tries):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(" retry", e)
            time.sleep(4 * (i + 1))
    raise SystemExit("api failed")

def info(title):
    data = api({
        "action": "query", "titles": title,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size|mime",
    })
    pages = data.get("query", {}).get("pages", {})
    for p in pages.values():
        if "missing" in p:
            return None
        ii = (p.get("imageinfo") or [None])[0]
        return p.get("title"), ii
    return None

records = []
for n, titles in WANTED.items():
    got = None
    for t in titles:
        print("lookup", n, t[:70])
        r = info(t)
        time.sleep(1.2)
        if r and r[1]:
            got = r
            break
        print("  miss")
    if not got:
        print("FAILED", n)
        continue
    title, ii = got
    meta = ii.get("extmetadata") or {}
    url = ii["url"]
    print("  get", ii.get("width"), (meta.get("LicenseShortName") or {}).get("value"))
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read()
    im = Image.open(io.BytesIO(raw))
    im = im.convert("RGB")
    im.thumbnail((3000, 3000), Image.Resampling.LANCZOS)
    dest = os.path.join(FIGS, f"fig{n:02d}.jpg")
    im.save(dest, "JPEG", quality=88, optimize=True)
    print("  saved", dest, im.size)
    records.append({
        "n": n,
        "title": title,
        "lic": (meta.get("LicenseShortName") or {}).get("value"),
        "artist": (meta.get("Artist") or {}).get("value"),
        "licurl": (meta.get("LicenseUrl") or {}).get("value"),
        "page": "https://commons.wikimedia.org/wiki/" + title.replace(" ", "_"),
        "w": ii.get("width"),
        "h": ii.get("height"),
    })
    time.sleep(1)

open(os.path.join(HERE, "_got.json"), "w", encoding="utf-8").write(json.dumps(records, indent=2))
print("done", len(records))
