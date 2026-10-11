"""Build kindle_links rules for an EE book: Further Reading / sources -> Open Library search, Also-by -> Amazon search."""
import sys, re, json, docx
from urllib.parse import quote_plus
sys.path.insert(0, '.')
from eedoc import *
LABELS = {'Physics, Actually','More Actually Books','Math, Actually','Quantum, Actually','Science Sparks','Look First','Electrical Engineering Series','History','Fiction','In German'}
def rules_for(docx_path, reading_heading_prefix, out_json):
    d = docx.Document(docx_path); ps = body_ps(d); T = [ptext(p) for p in ps]
    H1 = [i for i, p in enumerate(ps) if sty(p) == 'Heading1']
    rules = []
    # reading list: last Heading1 starting with prefix, up to next Heading1 / review line
    a = max(i for i in H1 if T[i].startswith(reading_heading_prefix))
    b = next(i for i in H1 if i > a)
    for i in range(a+1, b):
        t = T[i]
        if sty(ps[i]).startswith('Heading') or ' — ' not in t: continue
        pre = t.split(' — ')[0]
        if ', ' not in pre or len(pre) > 160: continue
        segs = [x for x in pre.split(', ') if not re.match(r'(?i)^(\d+(st|nd|rd|th) edition|\w+ edition|\d{4}|vol\.? ?\d+)$', x.strip())]
        if len(segs) < 2: continue
        title = segs[-1].strip(); auth = segs[0]
        last = re.sub(r'\(.*?\)', '', auth).split(' and ')[0].strip().split()[-1]
        url = 'https://openlibrary.org/search?q=' + quote_plus(title + ' ' + last)
        rules.append({'find': title, 'to': '[%s](%s)' % (title, url), 'in': t[:60], 'max': 1})
    # also-by
    ab = max(i for i in H1 if T[i].startswith('Also by'))
    for i in range(ab+1, len(ps)):
        t = T[i].strip()
        if not t or t in LABELS: continue
        title = re.sub(r'\s*\((?:Book \d+)\)$', '', t)
        pen = re.search(r'writing as ([^(]+?)(?: \(|$)', t)
        title = re.split(r' \((?:The |Lolly|Book)', title)[0]
        title = title.split(', Lothar J. Musiol writing as')[0]
        who = pen.group(1).strip() if pen else 'Lothar J. Musiol'
        url = 'https://www.amazon.com/s?k=' + quote_plus(title + ' ' + who) + '&i=digital-text'
        rules.append({'find': title, 'to': '[%s](%s)' % (title, url), 'in': t[:60], 'max': 1})
    json.dump({'note': 'EE series link rules (11 Oct 2026): Further Reading titles -> Open Library search, Also-by titles -> Amazon Kindle search; keyword links, hidden URLs.', 'rules': rules}, open(out_json, 'w'), indent=1, ensure_ascii=False)
    return rules
def alsoby_rules(docx_path):
    """Also-by titles -> Amazon Kindle search (the Also-by half of rules_for, for books whose sources are not 'Author, Title — note' lines)."""
    d = docx.Document(docx_path); ps = body_ps(d); T = [ptext(p) for p in ps]
    H1 = [i for i, p in enumerate(ps) if sty(p) == 'Heading1']; rules = []
    ab = max(i for i in H1 if T[i].startswith('Also by'))
    for i in range(ab+1, len(ps)):
        t = T[i].strip()
        if not t or t in LABELS: continue
        title = re.sub(r'\s*\((?:Book \d+)\)$', '', t)
        pen = re.search(r'writing as ([^(]+?)(?: \(|$)', t)
        title = re.split(r' \((?:The |Lolly|Book)', title)[0]
        title = title.split(', Lothar J. Musiol writing as')[0]
        who = pen.group(1).strip() if pen else 'Lothar J. Musiol'
        url = 'https://www.amazon.com/s?k=' + quote_plus(title + ' ' + who) + '&i=digital-text'
        rules.append({'find': title, 'to': '[%s](%s)' % (title, url), 'in': t[:60], 'max': 1})
    return rules
if __name__ == '__main__':
    r = rules_for(sys.argv[1], sys.argv[2], sys.argv[3]); print(len(r))
    for x in r: print(x['find'][:70], '|', x['to'][-70:])
