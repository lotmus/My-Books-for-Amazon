"""Add selected front-cover images as the first page of the two DOCX masters.

The edit updates only the OOXML image part, document relationship, and opening
paragraphs. It leaves the existing title pages, story content, and final
back-cover pages in place. Running twice skips files already containing the
selected image relationship.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import re
import tempfile
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BOOKS = [
    (Path('Book 1 - Schrodingers Paperwork'),
     'Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx',
     'KINDLE_FRONT_COVER_LIGHT.jpg'),
    (Path('Book 2 - The Permitted Options'),
     'The_Permitted_Options_BOOK_2_REVISION_20261005.docx',
     'KINDLE_COVER_FINAL_2560.jpg'),
]
EMU_PER_INCH = 914400
TWIPS_PER_INCH = 1440


def insert_cover(docx: Path, cover: Path) -> bool:
    with ZipFile(docx, 'r') as src:
        files = {item.filename: src.read(item.filename) for item in src.infolist()}
        infos = {item.filename: item for item in src.infolist()}

    xml = files['word/document.xml'].decode('utf-8')
    rels = files['word/_rels/document.xml.rels'].decode('utf-8')
    media_names = [name for name in files if name.startswith('word/media/')]
    cover_bytes = cover.read_bytes()
    if any(files[name] == cover_bytes for name in media_names):
        return False

    # Book 1 already opens with an earlier front-cover rendering. Replace that
    # picture in place so the selected cover is authoritative and appears once.
    opening = re.search(r'<wp:inline\b.*?</wp:inline>', xml, flags=re.DOTALL)
    if opening and re.search(r'<wp:docPr\b[^>]*descr="[^"]*front cover', opening.group(), flags=re.IGNORECASE):
        drawing = opening.group()
        embed = re.search(r'<a:blip\b[^>]*r:embed="([^"]+)"', drawing)
        if not embed:
            raise ValueError(f'Opening front-cover picture has no image relationship in {docx}')
        relationship = re.search(r'<Relationship\b[^>]*Id="' + re.escape(embed.group(1)) + r'"[^>]*Target="([^"]+)"', rels)
        if not relationship:
            raise ValueError(f'Could not resolve opening cover image in {docx}')
        part = 'word/' + relationship.group(1)

        sect = re.search(r'<w:sectPr\b[^>]*>.*?</w:sectPr>', xml)
        page = re.search(r'<w:pgSz\b[^>]*w:w="(\d+)"[^>]*w:h="(\d+)"', sect.group())
        margins = re.search(r'<w:pgMar\b[^>]*w:top="(\d+)"[^>]*w:right="(\d+)"[^>]*w:bottom="(\d+)"[^>]*w:left="(\d+)"', sect.group())
        page_w, page_h = map(int, page.groups())
        top, right, bottom, left = map(int, margins.groups())
        max_w = page_w - left - right
        max_h = page_h - top - bottom
        with Image.open(cover) as im:
            ratio = im.width / im.height
        width = min(max_w, round(max_h * ratio))
        height = round(width / ratio)
        cx = round(width * EMU_PER_INCH / TWIPS_PER_INCH)
        cy = round(height * EMU_PER_INCH / TWIPS_PER_INCH)
        drawing = re.sub(r'<wp:extent\b[^>]*/>', f'<wp:extent cx="{cx}" cy="{cy}"/>', drawing, count=1)
        drawing = re.sub(r'<a:ext\b[^>]*/>', f'<a:ext cx="{cx}" cy="{cy}"/>', drawing, count=1)
        drawing = re.sub(r'(<wp:docPr\b[^>]*descr=")[^"]*(")', r'\1Front cover: selected Kindle cover artwork.\2', drawing, count=1)
        drawing = re.sub(r'(<pic:cNvPr\b[^>]*descr=")[^"]*(")', r'\1Front cover: selected Kindle cover artwork.\2', drawing, count=1)
        xml = xml[:opening.start()] + drawing + xml[opening.end():]
        files['word/document.xml'] = xml.encode('utf-8')
        files[part] = cover_bytes
        with tempfile.NamedTemporaryFile(dir=docx.parent, suffix='.docx', delete=False) as tmp:
            tmp_path = Path(tmp.name)
        try:
            with ZipFile(tmp_path, 'w', ZIP_DEFLATED) as dst:
                for name, data in files.items():
                    info = infos.get(name)
                    dst.writestr(info, data) if info else dst.writestr(name, data)
            tmp_path.replace(docx)
        finally:
            tmp_path.unlink(missing_ok=True)
        return True

    if cover.name in rels and 'frontCover' in xml:
        return False

    sect = re.search(r'<w:sectPr\b[^>]*>.*?</w:sectPr>', xml)
    if not sect:
        raise ValueError(f'Could not find page layout in {docx}')
    page = re.search(r'<w:pgSz\b[^>]*w:w="(\d+)"[^>]*w:h="(\d+)"', sect.group())
    margins = re.search(r'<w:pgMar\b[^>]*w:top="(\d+)"[^>]*w:right="(\d+)"[^>]*w:bottom="(\d+)"[^>]*w:left="(\d+)"', sect.group())
    if not page or not margins:
        raise ValueError(f'Could not read page dimensions/margins in {docx}')
    page_w, page_h = map(int, page.groups())
    top, right, bottom, left = map(int, margins.groups())
    max_w = page_w - left - right
    max_h = page_h - top - bottom
    with Image.open(cover) as im:
        ratio = im.width / im.height
    width = min(max_w, round(max_h * ratio))
    height = round(width / ratio)
    cx = round(width * EMU_PER_INCH / TWIPS_PER_INCH)
    cy = round(height * EMU_PER_INCH / TWIPS_PER_INCH)

    rid_nums = [int(n) for n in re.findall(r'\bId="rId(\d+)"', rels)]
    rid = f'rId{max(rid_nums, default=0) + 1}'
    drawing_ids = [int(n) for n in re.findall(r'<wp:docPr\b[^>]*\bid="(\d+)"', xml)]
    drawing_id = max(drawing_ids, default=0) + 1
    escaped_name = cover.name.replace('&', '&amp;').replace('"', '&quot;')
    alt = ('Front cover: ' + cover.stem.replace('_', ' ')).replace('&', '&amp;')
    image_rel = f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{escaped_name}"/>'
    rels = rels.replace('</Relationships>', image_rel + '</Relationships>')

    picture = (
        f'<w:p><w:pPr><w:spacing w:before="0" w:after="0"/><w:ind w:left="0" w:right="0" w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
        f'<w:r><w:drawing><wp:inline xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" distT="0" distB="0" distL="0" distR="0">'
        f'<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
        f'<wp:docPr id="{drawing_id}" name="frontCover" descr="{alt}"/>'
        f'<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>'
        f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        f'<pic:pic><pic:nvPicPr><pic:cNvPr id="{drawing_id}" name="{escaped_name}" descr="{alt}"/><pic:cNvPicPr><a:picLocks noChangeAspect="1"/></pic:cNvPicPr></pic:nvPicPr>'
        f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
        f'</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
        '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
    )
    body_open = re.search(r'<w:body\b[^>]*>', xml)
    if not body_open:
        raise ValueError(f'Could not find document body in {docx}')
    point = body_open.end()
    xml = xml[:point] + picture + xml[point:]
    files['word/document.xml'] = xml.encode('utf-8')
    files['word/_rels/document.xml.rels'] = rels.encode('utf-8')

    types = files['[Content_Types].xml'].decode('utf-8')
    if not re.search(r'<Default\b[^>]*Extension="jpg"', types):
        types = types.replace('</Types>', '<Default Extension="jpg" ContentType="image/jpeg"/></Types>')
    files['[Content_Types].xml'] = types.encode('utf-8')
    files['word/media/' + cover.name] = cover_bytes

    with tempfile.NamedTemporaryFile(dir=docx.parent, suffix='.docx', delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        with ZipFile(tmp_path, 'w', ZIP_DEFLATED) as dst:
            for name, data in files.items():
                info = infos.get(name)
                if info:
                    dst.writestr(info, data)
                else:
                    dst.writestr(name, data)
        tmp_path.replace(docx)
    finally:
        tmp_path.unlink(missing_ok=True)
    return True


if __name__ == '__main__':
    for folder, master, cover_name in BOOKS:
        book = ROOT / folder
        changed = insert_cover(book / master, book / cover_name)
        print(('Added' if changed else 'Already present:'), cover_name, '->', master)
