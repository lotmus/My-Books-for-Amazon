"""Search remaining photo slots and download the first honest match."""
import io, json, os, re, time, urllib.parse, urllib.request
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "CopyIsNeverExactFigureCredits/1.0 (book figure research; educational)"}

# n, query, function(title, description)->bool
def has(blob, *words):
    return all(w in blob for w in words)

SLOTS = [
    (4, "bacterial colonies agar plate petri",
     lambda b: ("colon" in b or "agar" in b or "petri" in b) and "algorithm" not in b and "dog" not in b and "diagnostic" not in b),
    (19, "filing cabinets archive",
     lambda b: ("cabinet" in b or "catalogue" in b or "catalog" in b) and "kitchen" not in b and "oil house" not in b),
    (26, "blood collection tubes laboratory rack",
     lambda b: ("tube" in b and ("blood" in b or "sample" in b or "vacutainer" in b))),
    (31, "intracytoplasmic sperm injection microscope",
     lambda b: ("icsi" in b or "sperm injection" in b or "micromanipul" in b or "microinjection" in b)),
    (34, "broiler chickens poultry barn interior",
     lambda b: ("chicken" in b or "broiler" in b or "poultry" in b) and "garden" not in b),
    (36, "DNA sequencing machine laboratory",
     lambda b: ("sequenc" in b or "genom" in b or "pipette" in b)),
    (39, "saliva DNA collection kit",
     lambda b: ("saliva" in b or "spit" in b or "oragene" in b or "dna test" in b) and "47400098641" not in b),
    (42, "server room racks data center",
     lambda b: ("server" in b or "datacenter" in b or "data center" in b) and ("rack" in b or "room" in b)),
    (45, "whippet dog running race",
     lambda b: "whippet" in b),
    (46, "newborn baby hand",
     lambda b: ("newborn" in b or "baby" in b or "infant" in b) and ("hand" in b or "feet" in b or "foot" in b) and "bat" not in b),
]

def api(params):
    url = API + "?" + urllib.parse.urlencode(dict(params, format="json"))
    for i in range(6):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print("  api", e)
            time.sleep(5 * (i + 1))
    return {}

def licence_ok(name):
    n = (name or "").lower()
    if any(x in n for x in ("nc", "noncommercial", "non-commercial", "nd", "noderiv")):
        return False
    return any(x in n for x in ("cc0", "cc by", "cc-by", "public domain"))

def strip(html):
    return re.sub("<[^>]+>", "", html or "")

records = []
for n, q, pred in SLOTS:
    print("\n==", n)
    data = api({"action": "query", "list": "search", "srnamespace": 6,
                "srsearch": "filetype:bitmap " + q, "srlimit": 10})
    time.sleep(2)
    titles = [h["title"] for h in data.get("query", {}).get("search", [])]
    if not titles:
        print("  none")
        continue
    info = api({"action": "query", "titles": "|".join(titles[:8]),
                "prop": "imageinfo", "iiprop": "url|extmetadata|size|mime"})
    time.sleep(2)
    chosen = None
    for p in info.get("query", {}).get("pages", {}).values():
        ii = (p.get("imageinfo") or [None])[0]
        if not ii:
            continue
        meta = ii.get("extmetadata") or {}
        lic = (meta.get("LicenseShortName") or {}).get("value", "")
        title = p.get("title", "")
        desc = strip((meta.get("ImageDescription") or {}).get("value", ""))
        blob = (title + " " + desc).lower()
        w = ii.get("width") or 0
        ok = licence_ok(lic) and pred(blob) and w >= 900
        print(("  OK " if ok else "  -- "), w, lic, title[:90])
        if ok and chosen is None:
            chosen = (title, ii, meta, lic)
    if not chosen:
        print("  NO PICK")
        continue
    title, ii, meta, lic = chosen
    print("  DOWNLOAD", title[:80])
    req = urllib.request.Request(ii["url"], headers=HEADERS)
    with urllib.request.urlopen(req, timeout=90) as resp:
        raw = resp.read()
    im = Image.open(io.BytesIO(raw)).convert("RGB")
    im.thumbnail((3000, 3000), Image.Resampling.LANCZOS)
    dest = os.path.join(FIGS, f"fig{n:02d}.jpg")
    im.save(dest, "JPEG", quality=88, optimize=True)
    print("  saved", im.size)
    records.append({
        "n": n, "title": title, "lic": lic,
        "artist": strip((meta.get("Artist") or {}).get("value", "")),
        "licurl": (meta.get("LicenseUrl") or {}).get("value", ""),
        "page": "https://commons.wikimedia.org/wiki/" + title.replace(" ", "_"),
    })
    time.sleep(2)

open(os.path.join(HERE, "_got2.json"), "w", encoding="utf-8").write(json.dumps(records, indent=2))
print("saved", len(records))
