"""Download an explicit list of Commons files."""
import io, json, os, re, time, urllib.parse, urllib.request
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
REV = os.path.join(HERE, "_review")
os.makedirs(REV, exist_ok=True)
API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "CopyIsNeverExactFigureCredits/1.0 (book figure research; educational)"}

# dest name -> commons title
JOBS = {
    "fig19.jpg": "File:Card Filing Cabinet.jpg",
    "fig36.jpg": "File:Illumina Hiseq 2000 sequencers, BGI Hong Kong sequencing room.JPG",
    "fig42.jpg": "File:NOIRLab HQ Server Racks (6V6A0395-CC).jpg",
    "rev26.jpg": "File:Vacutainer with blood collection tube.jpg",
    "rev34a.jpg": "File:Red chicken barn Canada.jpg",
    "rev34b.jpg": "File:The Bethlehem Poultry Farm. (Esan Safieh). Chicken house interior LOC matpc.18456.jpg",
    "rev45a.jpg": "File:Whippet 2018 6.jpg",
    "rev45b.jpg": "File:Fireworks Whippets.jpg",
    "rev39.jpg": "File:Wonder Who I Am - Flickr - Lisa Zins.jpg",
    "rev26b.jpg": "File:Blood collection renal function test tube.jpg",
}

def api(params):
    url = API + "?" + urllib.parse.urlencode(dict(params, format="json"))
    for i in range(5):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(" api", e)
            time.sleep(8 * (i + 1))
    return {}

def strip(html):
    return re.sub("<[^>]+>", "", html or "").replace("&amp;", "&").strip()

records = []
# batch imageinfo in groups of 4
titles = list(JOBS.values())
pages = {}
for i in range(0, len(titles), 4):
    chunk = titles[i:i+4]
    data = api({"action": "query", "titles": "|".join(chunk),
                "prop": "imageinfo", "iiprop": "url|extmetadata|size"})
    for p in data.get("query", {}).get("pages", {}).values():
        pages[p.get("title")] = p
    time.sleep(2)

for dest, title in JOBS.items():
    p = pages.get(title) or {}
    ii = (p.get("imageinfo") or [None])[0]
    if not ii:
        print("MISSING", title)
        continue
    meta = ii.get("extmetadata") or {}
    lic = (meta.get("LicenseShortName") or {}).get("value", "")
    print("GET", dest, ii.get("width"), lic, title[:70])
    req = urllib.request.Request(ii["url"], headers=HEADERS)
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read()
    im = Image.open(io.BytesIO(raw)).convert("RGB")
    im.thumbnail((3000, 3000), Image.Resampling.LANCZOS)
    folder = FIGS if dest.startswith("fig") else REV
    path = os.path.join(folder, dest)
    im.save(path, "JPEG", quality=88, optimize=True)
    print("  ", im.size)
    records.append({
        "dest": dest, "title": title, "lic": lic,
        "artist": strip((meta.get("Artist") or {}).get("value", "")),
        "credit": strip((meta.get("Credit") or {}).get("value", "")),
        "licurl": (meta.get("LicenseUrl") or {}).get("value", ""),
        "page": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"), safe="/:()"),
    })
    time.sleep(1.5)

open(os.path.join(HERE, "_got3.json"), "w", encoding="utf-8").write(json.dumps(records, indent=2))
print("done", len(records))
