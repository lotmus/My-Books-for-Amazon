"""Imageinfo only, for credit lines. One title at a time."""
import json, os, re, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "CopyIsNeverExactFigureCredits/1.0 (book figure research; educational)"}
TITLES = [
    "File:Card Filing Cabinet.jpg",
    "File:Vacutainer with blood collection tube.jpg",
    "File:Red chicken barn Canada.jpg",
    "File:Illumina Hiseq 2000 sequencers, BGI Hong Kong sequencing room.JPG",
    "File:NOIRLab HQ Server Racks (6V6A0395-CC).jpg",
    "File:Agarplate redbloodcells edit.jpg",
]

def api(params):
    url = API + "?" + urllib.parse.urlencode(dict(params, format="json"))
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))

def strip(html):
    return re.sub("<[^>]+>", "", html or "").replace("&amp;", "&").strip()

out = []
for title in TITLES:
    data = api({"action": "query", "titles": title, "prop": "imageinfo", "iiprop": "extmetadata"})
    page = next(iter(data["query"]["pages"].values()))
    meta = page["imageinfo"][0]["extmetadata"]
    out.append({
        "title": title,
        "lic": (meta.get("LicenseShortName") or {}).get("value", ""),
        "artist": strip((meta.get("Artist") or {}).get("value", "")),
        "licurl": (meta.get("LicenseUrl") or {}).get("value", ""),
        "credit": strip((meta.get("Credit") or {}).get("value", ""))[:240],
    })
    print(out[-1]["lic"], "|", out[-1]["artist"][:80], "|", title[:60])
    time.sleep(4)

open(os.path.join(HERE, "_meta.json"), "w", encoding="utf-8").write(json.dumps(out, indent=2))
print("ok")
