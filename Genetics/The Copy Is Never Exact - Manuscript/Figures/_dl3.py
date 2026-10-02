"""Print candidate Commons titles, then download an explicit allow-list."""
import io, json, os, time, urllib.parse, urllib.request
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "CopyIsNeverExactFigureCredits/1.0 (book figure research; educational)"}

QUERIES = [
    "filing cabinet",
    "vacutainer",
    "blood collection tubes",
    "infusion bag hospital",
    "broiler chickens barn",
    "poultry house interior",
    "Illumina sequencer",
    "DNA sequencer laboratory",
    "saliva DNA kit",
    "server room racks",
    "data center servers",
    "Whippet",
]

def api(params):
    url = API + "?" + urllib.parse.urlencode(dict(params, format="json"))
    for i in range(5):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(" api", e)
            time.sleep(6 * (i + 1))
    return {}

out = []
for q in QUERIES:
    print("\n##", q)
    data = api({"action": "query", "list": "search", "srnamespace": 6,
                "srsearch": "filetype:bitmap " + q, "srlimit": 6})
    time.sleep(2.5)
    titles = [h["title"] for h in data.get("query", {}).get("search", [])]
    if not titles:
        print("  none")
        continue
    info = api({"action": "query", "titles": "|".join(titles),
                "prop": "imageinfo", "iiprop": "url|extmetadata|size"})
    time.sleep(2.5)
    for p in info.get("query", {}).get("pages", {}).values():
        ii = (p.get("imageinfo") or [None])[0]
        if not ii:
            continue
        meta = ii.get("extmetadata") or {}
        lic = (meta.get("LicenseShortName") or {}).get("value", "")
        line = f"{ii.get('width')} | {lic} | {p.get('title')}"
        print(" ", line[:140])
        out.append(q + " :: " + line)

open(os.path.join(HERE, "_cands.txt"), "w", encoding="utf-8").write("\n".join(out))
print("\nwrote", len(out))
