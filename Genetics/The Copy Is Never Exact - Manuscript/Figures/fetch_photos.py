"""Fetch real, rights-clear photographs for the 'photo' figure slots via the
Wikimedia Commons search + imageinfo API (never guessed filenames). Downloads
only files with a usable licence (public domain or CC BY / CC BY-SA), writes
CREDITS.md with the real author/licence/source URL for each figure, and
leaves a figNN_slot.png placeholder (handled by build_docx.py) for anything
that could not be confidently matched, so the author can drop in his own
photo later exactly as with the Cosmology books.
Run: python fetch_photos.py
"""
import json
import os
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
os.makedirs(FIGS, exist_ok=True)

HEADERS = {"User-Agent": "GeneticsBookFigureResearch/1.0 (contact: unexpectedmotionpictures@gmail.com)"}
API = "https://commons.wikimedia.org/w/api.php"

# n -> (search query, caption for credits, minimum width preferred)
QUERIES = {
    1: ('"The Eagle" pub Cambridge Bene\'t Street', "The Eagle, Bene't Street, Cambridge"),
    4: ("bacteria colony petri dish culture plate", "Bacterial colonies on a plate"),
    14: ("winter field snow bare trees rural", "A bare winter field"),
    17: ("Brno city view Czech Republic historic", "Brno, where Mendel's abbey stands"),
    26: ("laboratory pipette blood sample tubes rack", "Samples prepared in a laboratory"),
    29: ("sheep lamb field pasture farm", "A ewe with her lamb"),
    30: ("two puppies same litter siblings", "Two dogs of the same litter"),
    31: ("laboratory microscope researcher biology", "A biology research laboratory"),
    34: ("chicken farm barn interior poultry", "A poultry barn"),
    36: ("genomics laboratory scientist pipette DNA research", "A genetics research laboratory"),
    39: ("plastic test tube laboratory sample vial", "A sample collection tube"),
    42: ("server room data center computer racks", "A server room"),
    45: ("whippet dog racing track running", "A whippet at full stretch"),
    46: ("newborn baby hand parent finger", "A newborn's hand"),
}

GOOD_LICENCE_KEYWORDS = (
    "public domain", "pd-", "cc-zero", "cc0",
    "cc-by-sa", "cc-by ", "cc-by-2", "cc-by-3", "cc-by-4",
    "attribution", "share alike", "creative commons",
)


def api_get(params, tries=4):
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(tries):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(3 * (attempt + 1))
                continue
            raise
    return {}


def find_candidate(query):
    data = api_get({
        "action": "query", "list": "search", "srnamespace": 6,
        "srsearch": f"filetype:bitmap {query}", "srlimit": 8,
    })
    hits = data.get("query", {}).get("search", [])
    titles = [h["title"] for h in hits]
    if not titles:
        return None
    data2 = api_get({
        "action": "query", "titles": "|".join(titles[:8]),
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size",
    })
    pages = data2.get("query", {}).get("pages", {})
    best = None
    for p in pages.values():
        infos = p.get("imageinfo")
        if not infos:
            continue
        info = infos[0]
        width = info.get("width", 0)
        url_path = urllib.parse.urlparse(info.get("url", "")).path
        url_ext = os.path.splitext(url_path)[1].lower()
        if url_ext not in (".jpg", ".jpeg", ".png"):
            continue
        if width < 800:
            continue
        if info.get("size", 0) > 15_000_000:
            continue
        meta = info.get("extmetadata", {})
        licence_short = (meta.get("LicenseShortName", {}) or {}).get("value", "")
        usage_terms = (meta.get("UsageTerms", {}) or {}).get("value", "")
        combined = (licence_short + " " + usage_terms).lower()
        if not any(k in combined for k in GOOD_LICENCE_KEYWORDS):
            continue
        artist = (meta.get("Artist", {}) or {}).get("value", "")
        artist = artist.replace("<a", " <a")
        import re as _re
        artist_plain = _re.sub("<[^>]+>", "", artist).strip() or "unknown"
        candidate = {
            "title": p.get("title"),
            "url": info["url"],
            "width": width,
            "licence": licence_short or usage_terms or "unspecified",
            "artist": artist_plain,
            "descr_url": f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(p.get('title'))}",
        }
        if best is None or width > best["width"]:
            best = candidate
    return best


def download(n, candidate):
    ext = os.path.splitext(urllib.parse.urlparse(candidate["url"]).path)[1].lower()
    if ext not in (".jpg", ".jpeg", ".png"):
        ext = ".jpg"
    dest = os.path.join(FIGS, f"fig{n:02d}{ext}")
    req = urllib.request.Request(candidate["url"], headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    with open(dest, "wb") as f:
        f.write(data)
    return dest, len(data)


def main():
    lines = ["# Photo credits\n", "\nFetched automatically from Wikimedia Commons search + imageinfo API on 2026-09-15.\n",
             "All entries below were selected for a public-domain or Creative Commons licence at fetch time;\n",
             "spot-check the description-page link before publication, since licence tags can be mis-applied.\n\n"]
    ok, missing = 0, []
    for n, (query, caption) in sorted(QUERIES.items()):
        try:
            cand = find_candidate(query)
        except Exception as e:
            cand = None
            print(f"fig{n:02d}: search error {e}")
        if cand is None:
            print(f"fig{n:02d}: NO SUITABLE MATCH for '{query}' -> leaving as slot placeholder")
            lines.append(f"- Figure {n:02d}: NOT FOUND automatically ({caption}). Needs manual photo.\n")
            missing.append(n)
        else:
            dest, size = download(n, cand)
            safe_title = cand['title'].encode("ascii", "replace").decode("ascii")
            print(f"fig{n:02d}: {safe_title} ({cand['width']}px, {size} bytes) -> {dest}")
            lines.append(
                f"- Figure {n:02d} ({caption}): \"{cand['title'].replace('File:', '')}\", "
                f"by {cand['artist']}, licence: {cand['licence']}. Source: {cand['descr_url']}\n"
            )
            ok += 1
        time.sleep(1.5)
    with open(os.path.join(HERE, "CREDITS.md"), "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"\nDone. {ok} fetched, {len(missing)} left as placeholders: {missing}")


if __name__ == "__main__":
    main()
