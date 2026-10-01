import json, urllib.parse, urllib.request
from pathlib import Path
UA = "CopyIsNeverExactManuscript/1.0 (figure credits; educational)"
title = "File:Basilica of the Assumption of Our Lady, Abbatial church, Brno.jpg"
q = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
    "action": "query", "titles": title, "prop": "imageinfo",
    "iiprop": "url|size|mime|extmetadata", "format": "json",
})
req = urllib.request.Request(q, headers={"User-Agent": UA})
data = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))
page = next(iter(data["query"]["pages"].values()))
ii = page["imageinfo"][0]
meta = ii.get("extmetadata") or {}
def val(k):
    v = meta.get(k, {})
    return (v.get("value") if isinstance(v, dict) else "") or ""
Path("_fig17_meta.txt").write_text(
    f"{ii['width']}x{ii['height']} {ii['mime']}\n{ii['url']}\nLIC {val('LicenseShortName')}\nART {val('Artist')[:400]}\nCRED {val('Credit')[:400]}\n",
    encoding="utf-8",
)
print("meta written", ii["width"], val("LicenseShortName"))
