"""Search Commons and print the best licence-clean candidates. Does not download."""
import json, urllib.parse, urllib.request

API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "CopyIsNeverExactFigureCredits/1.0 (book research; contact: unexpectedmotionpictures@gmail.com)"}

QUERIES = {
    0: "saliva DNA collection tube kit",
    4: "bacterial colonies agar petri dish",
    17: "Augustinian abbey Brno basilica",
    19: "archive filing cabinets shelves",
    26: "blood collection tubes laboratory rack",
    29: "ewe lamb sheep barn",
    30: "puppies litter two dogs",
    31: "intracytoplasmic sperm injection micromanipulator IVF",
    33: "tomatoes market stall",
    34: "broiler chickens poultry house interior",
    36: "DNA sequencing laboratory Illumina",
    39: "saliva collection kit box tube",
    42: "server room data center racks",
    45: "whippet dog running race",
    46: "newborn baby hand",
}

def api_get(params):
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=40) as resp:
        return json.loads(resp.read().decode("utf-8"))

def ok_licence(name):
    n = (name or "").lower()
    if any(x in n for x in ("nc", "noncommercial", "non-commercial", "nd", "noderiv")):
        return False
    return any(x in n for x in ("cc0", "cc by", "cc-by", "public domain", "pd"))

for n, q in QUERIES.items():
    print("\n==== FIG", n, q)
    data = api_get({
        "action": "query", "list": "search", "srnamespace": 6,
        "srsearch": "filetype:bitmap " + q, "srlimit": 6,
    })
    hits = data.get("query", {}).get("search", [])
    titles = [h["title"] for h in hits]
    if not titles:
        print("  NONE")
        continue
    data2 = api_get({
        "action": "query", "titles": "|".join(titles),
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size|mime",
    })
    pages = data2.get("query", {}).get("pages", {})
    for p in pages.values():
        ii = (p.get("imageinfo") or [None])[0]
        if not ii:
            continue
        meta = ii.get("extmetadata") or {}
        lic = (meta.get("LicenseShortName") or {}).get("value", "")
        artist = (meta.get("Artist") or {}).get("value", "")
        # strip tags roughly
        import re
        artist = re.sub("<[^>]+>", "", artist)[:80]
        w, h = ii.get("width"), ii.get("height")
        flag = "OK" if ok_licence(lic) else "NO"
        print(f"  {flag} {w}x{h} {lic} | {p.get('title','')[:90]}")
        print(f"     {artist}")
        print(f"     {ii.get('url','')[:140]}")
