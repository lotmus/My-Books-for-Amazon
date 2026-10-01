"""Finish remaining downloads and collect credit metadata. Sleeps hard to avoid 429."""
import io, json, os, re, time, urllib.parse, urllib.request
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
REV = os.path.join(HERE, "_review")
os.makedirs(REV, exist_ok=True)
API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "CopyIsNeverExactFigureCredits/1.0 (book figure research; educational)"}

JOBS = {
    "rev34b.jpg": "File:The Bethlehem Poultry Farm. (Esan Safieh). Chicken house interior LOC matpc.18456.jpg",
    "rev45a.jpg": "File:Whippet 2018 6.jpg",
    "rev45b.jpg": "File:Fireworks Whippets.jpg",
    "rev39.jpg": "File:Wonder Who I Am - Flickr - Lisa Zins.jpg",
}

def api(params):
    url = API + "?" + urllib.parse.urlencode(dict(params, format="json"))
    for i in range(6):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(" api", type(e).__name__, e)
            time.sleep(12 * (i + 1))
    return {}

def strip(html):
    return re.sub("<[^>]+>", "", html or "").replace("&amp;", "&").strip()

print("pause before first request")
time.sleep(15)
records = []
for dest, title in JOBS.items():
    data = api({"action": "query", "titles": title, "prop": "imageinfo", "iiprop": "url|extmetadata|size"})
    page = next(iter((data.get("query") or {}).get("pages", {}).values()), {})
    ii = (page.get("imageinfo") or [None])[0]
    if not ii:
        print("MISSING", title)
        time.sleep(8)
        continue
    meta = ii.get("extmetadata") or {}
    lic = (meta.get("LicenseShortName") or {}).get("value", "")
    print("GET", dest, ii.get("width"), lic)
    time.sleep(3)
    req = urllib.request.Request(ii["url"], headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read()
    except Exception as e:
        print("  download failed", e)
        time.sleep(20)
        continue
    im = Image.open(io.BytesIO(raw)).convert("RGB")
    im.thumbnail((3000, 3000), Image.Resampling.LANCZOS)
    im.save(os.path.join(REV, dest), "JPEG", quality=88, optimize=True)
    print("  saved", im.size)
    records.append({
        "dest": dest, "title": title, "lic": lic,
        "artist": strip((meta.get("Artist") or {}).get("value", "")),
        "licurl": (meta.get("LicenseUrl") or {}).get("value", ""),
        "page": "https://commons.wikimedia.org/wiki/" + title.replace(" ", "_"),
    })
    time.sleep(8)

open(os.path.join(HERE, "_got4.json"), "w", encoding="utf-8").write(json.dumps(records, indent=2))
print("done", len(records))
