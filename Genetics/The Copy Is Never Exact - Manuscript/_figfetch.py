# scratch: fetch figure 19 and look for a wider abbey photo
import json
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UA = "CopyIsNeverExactManuscript/1.0 (figure credits; educational)"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read(), r.geturl()

def api(params):
    q = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    raw, _ = get(q)
    return json.loads(raw.decode("utf-8"))

title = "File:First Annual Field Workers' Conference, Eugenics Record Office, Cold Spring Harbor, Long Island, New York, June 20 and 21,1912.jpg"
info = api({
    "action": "query",
    "titles": title,
    "prop": "imageinfo",
    "iiprop": "url|size|mime",
    "format": "json",
})
pages = info["query"]["pages"]
page = next(iter(pages.values()))
ii = page["imageinfo"][0]
print("ERO", ii["width"], ii["height"], ii["mime"], ii["url"][:120])
data, final = get(ii["url"])
dest = ROOT / "Figures" / "figs" / "fig19.jpg"
dest.write_bytes(data)
print("wrote", dest, "bytes", len(data), "final", final[:80])

# abbey candidates
searches = [
    "Augustinian abbey St Thomas Brno",
    "Starobrno klaster",
    "Mendel abbey Brno",
    "Stare Brno bazilika",
]
out = []
for term in searches:
    data = api({
        "action": "query",
        "generator": "search",
        "gsrsearch": term,
        "gsrnamespace": "6",
        "gsrlimit": "8",
        "prop": "imageinfo",
        "iiprop": "url|size|mime",
        "format": "json",
    })
    out.append("SEARCH " + term)
    for p in data.get("query", {}).get("pages", {}).values():
        ii = (p.get("imageinfo") or [{}])[0]
        out.append(
            f"{p.get('title')} | {ii.get('width')}x{ii.get('height')} | {ii.get('mime')} | {ii.get('url','')}"
        )
    out.append("---")

(ROOT / "_abbey_hits.txt").write_text("\n".join(out), encoding="utf-8")
print("abbey hits written")
