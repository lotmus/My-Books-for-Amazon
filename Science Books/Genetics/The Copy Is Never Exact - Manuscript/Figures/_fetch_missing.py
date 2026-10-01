"""Download specific Commons files for missing or mismatched photo slots."""
import json, os, re, time, urllib.parse, urllib.request
from PIL import Image
import io

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "CopyIsNeverExactFigureCredits/1.0 (book figure research)"}

# figure number -> preferred search, required words in title (lowercase)
SLOTS = [
    (0, "saliva collection tube OR Oragene OR spit kit DNA", ["saliva", "tube", "spit", "oragene", "buccal"]),
    (4, "bacterial colonies petri dish agar", ["colon", "agar", "petri", "bacteria"]),
    (17, "St Thomas Abbey Brno basilica Augustinian", ["abbey", "thomas", "brno", "bazilika", "august"]),
    (19, "archive shelves filing cabinets library stacks", ["cabinet", "archive", "shelf", "stacks", "catalog"]),
    (26, "blood collection tubes rack laboratory", ["blood", "tube", "vacutainer", "vial", "sample"]),
    (29, "ewe and lamb", ["ewe", "lamb"]),
    (30, "puppies same litter", ["pupp", "litter", "dog"]),
    (31, "ICSI micromanipulator IVF microscope injection", ["icsi", "ivf", "micro", "inject", "embryo"]),
    (33, "tomatoes market stall", ["tomato"]),
    (34, "broiler chickens poultry house barn interior", ["chicken", "broiler", "poultry", "hen"]),
    (36, "DNA sequencer laboratory Illumina", ["sequenc", "genom", "laborator", "pipette"]),
    (39, "saliva DNA collection kit box", ["saliva", "kit", "tube", "collection"]),
    (42, "server room data center racks", ["server", "rack", "datacenter", "data center"]),
    (45, "whippet dog running", ["whippet"]),
    (46, "newborn baby hand", ["newborn", "baby", "hand", "infant"]),
]

def api(params):
    url = API + "?" + urllib.parse.urlencode(dict(params, format="json"))
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=40) as resp:
        return json.loads(resp.read().decode("utf-8"))

def licence_ok(name):
    n = (name or "").lower()
    if any(x in n for x in ("nc", "noncommercial", "non-commercial", "nd", "noderiv")):
        return False
    return any(x in n for x in ("cc0", "cc by", "cc-by", "public domain"))

def strip(html):
    return re.sub("<[^>]+>", "", html or "").replace("\n", " ").strip()

out = []
for n, q, keys in SLOTS:
    print("\n==", n, q)
    data = api({"action": "query", "list": "search", "srnamespace": 6,
                "srsearch": "filetype:bitmap " + q, "srlimit": 8})
    titles = [h["title"] for h in data.get("query", {}).get("search", [])]
    if not titles:
        print("  no hits")
        continue
    info = api({"action": "query", "titles": "|".join(titles[:8]),
                "prop": "imageinfo", "iiprop": "url|extmetadata|size|mime"})
    cands = []
    for p in info.get("query", {}).get("pages", {}).values():
        ii = (p.get("imageinfo") or [None])[0]
        if not ii:
            continue
        meta = ii.get("extmetadata") or {}
        lic = (meta.get("LicenseShortName") or {}).get("value", "")
        title = p.get("title", "")
        blob = (title + " " + (meta.get("ImageDescription") or {}).get("value", "")).lower()
        if not licence_ok(lic):
            continue
        if not any(k in blob for k in keys):
            continue
        w = ii.get("width") or 0
        if w < 800:
            continue
        cands.append((w, title, lic, strip((meta.get("Artist") or {}).get("value", ""))[:100],
                      ii.get("url"), ii.get("mime"),
                      (meta.get("LicenseUrl") or {}).get("value", "")))
    cands.sort(reverse=True)
    for c in cands[:3]:
        print(" ", c[0], c[2], c[1][:100])
        print("   ", c[3][:80])
    if cands:
        out.append((n, cands[0]))
    time.sleep(0.4)

print("\n\nCHOSEN")
for n, c in out:
    print(n, c[1][:90], "|", c[2])
open(os.path.join(HERE, "_chosen.json"), "w", encoding="utf-8").write(
    json.dumps([{"n": n, "title": c[1], "lic": c[2], "artist": c[3], "url": c[4], "mime": c[5], "licurl": c[6], "w": c[0]}
                for n, c in out], indent=2))
