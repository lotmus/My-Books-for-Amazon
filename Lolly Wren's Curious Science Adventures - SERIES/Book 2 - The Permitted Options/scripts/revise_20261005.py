from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib, json, re, copy, sys

BOOK = Path(__file__).resolve().parents[1]
SRC = BOOK / 'The_Permitted_Options_BOOK_2_DRAFT.docx'
OUT = BOOK / 'The_Permitted_Options_BOOK_2_REVISION_20261005.docx'
EXPECTED = '145b46ab4ce619863d51eb532f9b75d5810abe53c1e1c6a50eb7aa3830cf333b'
NS = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W = '{'+NS['w']+'}'
EDITS = [
 (42, 'Miss Adaeze Pike put her head round the door at nine forty on a Thursday morning in the third week of March, and Lolly knew from her face that Thursday was not going to be routine, because Miss Pike had spent sixteen months becoming the best analyst in the building and had entirely lost the brittle brightness she had arrived with and had acquired instead a level way of delivering bad news.', 'Miss Adaeze Pike put her head round the door at nine forty on a Thursday morning in the third week of March. In sixteen months she had become the best analyst in the building and exchanged her brittle brightness for a level delivery of bad news. Lolly recognised the delivery before Miss Pike spoke.'),
 (62, 'Miss Pike had been waiting for that, and Lolly saw that she had been waiting for it, and understood that the morning was about to get worse.', 'Miss Pike had been waiting for that objection. Lolly could see the answer in the papers still in her hand.'),
 (78, 'They had put them all up: fourteen coherence traces, pinned in a row along the plasterboard of the third-floor briefing room, and every one of them did the same thing.', 'Fourteen coherence traces were pinned along the plasterboard of the third-floor briefing room. Each showed the same event.'),
 (109, 'Then she put it down on the briefing room table with considerable care, in the manner of someone setting down something that might still be live.', 'She laid it on the briefing room table as carefully as a live circuit.'),
 (133, 'Inside, she took them to a room in which four men and a woman were conducting, with great courtesy, the sort of argument that has been going on so long that everybody has memorised everybody else’s position and is now arguing chiefly out of loyalty to their earlier selves.', 'Inside, four men and a woman were conducting an argument with great courtesy. They had memorised one another’s positions and were now defending their own chiefly out of loyalty to the time already spent.'),
 (209, 'They were in the car park at half past four when Miss Pike rang, and Lolly put it on speaker on the roof of the car so that Fainrose, on the other side of it, could hear.', 'Miss Pike rang at half past four, while they were in the car park. Lolly set the phone on the roof, on speaker, between herself and Fainrose.'),
 (281, 'with the patience of a man who had sat for Holbein and been disappointed.', 'with the patience he had inherited from a disappointing sitting for Holbein.'),
 (285, 'in a hand that had learned its letters before printing,', 'in a hand shaped by memories older than printing,'),
 (286, 'They put him in the third-floor briefing room, where the traces were still pinned along the plasterboard, and Fainrose came in from a dinner she did not explain and Miss Pike came in from her desk, where she had been since seven in the morning, and Beatrix Sloan arrived at ten past ten from a chambers in Gray’s Inn looking like someone who had cancelled something she had been looking forward to.', 'They took him to the third-floor briefing room, where the traces were still pinned up. Fainrose came from a dinner she did not explain; Miss Pike came from the desk she had occupied since seven that morning. Beatrix Sloan arrived from chambers in Gray’s Inn at ten past ten, looking as if she had cancelled something she had been looking forward to.'),
 (331, 'Then she got up, went out, and came back four minutes later with a lever-arch file and put it on the briefing table and opened it.', 'Four minutes later she was back, opening a lever-arch file on the briefing table.'),
 (346, 'At least one live option in all of them,', 'At least one live option in every file I’ve checked,'),
 (349, 'Fainrose had gone to the blackboard and was standing in front of it without writing anything, which Lolly had learned meant that she was doing something enormous in her head and should not be spoken to.', 'Fainrose stood at the blackboard with the chalk unused. Lolly had learned to leave her alone at that stage.'),
 (491, 'the one with the postgraduate place and the shop and the two years of not deciding', 'the one with the postgraduate place and the shop and the sixteen months of not deciding'),
 (520, 'She had known. She had not let herself put it in those words. Once it was in words it would go in the notebook, and once it was in the notebook she would have to do something about it.', 'She had kept that knowledge out of the notebook. Written down, it would require something of her.'),
 (524, 'I’m only saying one of them’s yours.', 'I’m saying your dad needs the same.'),
 (537, 'On the Tuesday, Mrs Susie Kind opened the shop', 'On the Friday, Mrs Susie Kind opened the shop'),
 (541, 'She came in most Tuesdays now.', 'She came in most Fridays now.'),
 (541, 'her sister was being buried in Inverness on Friday,', 'her sister was being buried in Inverness the following Friday,'),
 (547, 'at eleven on Friday and then sleep', 'at eleven next Friday and then sleep'),
 (737, 'Then she went out of the room and did not come back for fifty minutes, and when she did she had her sleeves up.', 'She left for fifty minutes. When she returned, her sleeves were up.'),
 (783, 'Stadthof put both hands flat on the table.', 'Stadthof leaned across the table, palms down.'),
 (1124, 'He spelled it properly, and initialled it, and crossed the High Road against the lights like a man who has lived on it for forty years, and posted the letter at five twenty-six with the postscript facing up.', 'He spelled it properly and initialled it. At five twenty-six he crossed the High Road against the lights, with forty years’ confidence, and posted the letter with the postscript facing up.'),
 (1157, 'answer:if', 'answer: if'),
 (1157, 'invitation?He', 'invitation? He'),
 (1159, 'seven weeks early', 'five weeks early'),
 (1509, 'Albrecht Eilstein has had a horizon for a hundred centuries.', 'Albrecht Eilstein has inherited a horizon with a hundred centuries behind it.'),
 (1524, 'I have carried the far end of such a bridge on my back since before the pyramids and did not know it,', 'What I inherited has carried the far end of such a bridge since before the pyramids, and I did not know it,'),
 (1526, 'for a hundred and nine years', 'for more than a century'),
 (1545, 'Nobody had looked at the booking. In the department’s mind there had not been one.', 'The department had treated the booking as a metaphor. It had not asked to see the order.'),
 (1604, 'it was the most continuously he had been addressed since the Council of Constance.', 'not even the memory he carried of the Council of Constance contained so much continuous speech.'),
 (1790, 'A week later a letter came to the department', 'On the Friday a letter came to the department'),
 (1809, 'Sandra let her in. Sandra did not ask why. Sandra had worked nights for nineteen years and had stopped asking people why they turned up at night some time in the first.', 'Sandra let her in without asking why. Nineteen years on nights had taught her that people generally brought the answer with them.'),
 (1818, 'And everybody who was waiting for something heard a door.', 'You heard a door. I can’t tell you what anyone outside our records heard.'),
 (1836, 'Two hundred and nine of two hundred and nine dipped and returned.', 'All two hundred and nine monitored states dipped: fourteen left their permitted options, and the other hundred and ninety-five returned to where they had been.'),
 (1839, 'with a paper bag and the expression of someone who had negotiated a peace with the frame and lost on points.', 'with a paper bag held in the hand whose knuckle had healed badly.'),
 (1850, 'larger name.Dad', 'larger name. Dad'),
]

def text(p): return ''.join(p.xpath('.//w:t/text()',namespaces=NS))
def stripped(root):
    r = copy.deepcopy(root)
    for n in r.xpath('//w:t',namespaces=NS): n.text = ''
    return etree.tostring(r,method='c14n')

assert hashlib.sha256(SRC.read_bytes()).hexdigest() == EXPECTED, 'Source changed; review again.'
assert not OUT.exists(), 'Never overwrite a revision.'
with ZipFile(SRC) as src:
    data = src.read('word/document.xml')
    root = etree.fromstring(data)
    before = copy.deepcopy(root)
    paras = root.xpath('//w:body//w:p',namespaces=NS)
    changes = []
    for idx,old,new in EDITS:
        p = paras[idx]
        original = text(p)
        assert original.count(old) == 1, (idx,old)
        start = original.index(old); end = start+len(old)
        nodes = p.xpath('.//w:t',namespaces=NS)
        offset = 0; affected = []
        for node in nodes:
            t = node.text or ''
            if offset < end and offset+len(t) > start:
                affected.append((node,offset,t))
            offset += len(t)
        assert affected
        # Keep every run, property, bookmark and hyperlink node in place.
        first = affected[0][0]
        for node,pos,t in affected:
            left = t[:max(0,start-pos)]
            right = t[max(0,end-pos):]
            node.text = left + (new if node is first else '') + right
        assert text(p) == original.replace(old,new,1)
        changes.append({'paragraph':idx,'before':old,'after':new})
    assert stripped(root) == stripped(before), 'Non-text OOXML changed.'
    revised = etree.tostring(root,encoding='UTF-8',xml_declaration=True,standalone=True)
    with ZipFile(OUT,'x') as out:
        out.comment = src.comment
        for member in src.infolist():
            out.writestr(member,revised if member.filename=='word/document.xml' else src.read(member.filename))

with ZipFile(SRC) as a, ZipFile(OUT) as b:
    assert b.testzip() is None
    assert a.namelist() == b.namelist()
    unchanged = [n for n in a.namelist() if n!='word/document.xml']
    assert all(a.read(n)==b.read(n) for n in unchanged)
    for n in b.namelist():
        if n.endswith(('.xml','.rels')): etree.fromstring(b.read(n))
bookmarks = root.xpath('//w:bookmarkStart/@w:name',namespaces=NS)
anchors = root.xpath('//w:hyperlink/@w:anchor',namespaces=NS)
assert all(x in bookmarks for x in anchors)
assert hashlib.sha256(SRC.read_bytes()).hexdigest() == EXPECTED
report = {
 'source_sha256':EXPECTED,'revision_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),
 'replacement_count':len(changes),'changed_paragraphs':len(set(x['paragraph'] for x in changes)),
 'paragraphs':len(paras),'bookmarks':len(bookmarks),
 'hyperlinks':len(root.xpath('//w:hyperlink',namespaces=NS)), 'broken_internal_links':0,
 'unchanged_package_parts':len(unchanged),'all_nontext_document_xml_identical':True,
 'source_unchanged':True,'changes':changes,
}
(BOOK/'bak/review-20261005/verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='changes'},indent=2))
