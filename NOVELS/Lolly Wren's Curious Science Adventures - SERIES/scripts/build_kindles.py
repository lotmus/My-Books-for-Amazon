"""Build the series EPUBs from DOCX masters without a duplicate spine cover.

The DOCX masters include a front-cover page for review/print use. For Kindle,
the front cover is supplied as the EPUB cover resource; KDP advises against
adding a second HTML cover page. This script removes only that front page from
a temporary DOCX copy, then converts the remaining content. The back-cover
page remains at the end of the reading order.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_DEFLATED
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CSS = ROOT / 'scripts' / 'kindle.css'
BOOKS = [
    {
        'folder': 'Book 1 - Schrodingers Paperwork',
        'docx': 'Schrodingers_Paperwork_BOOK_1_KINDLE_FINAL.docx',
        'epub': 'Schrodingers_Paperwork_KINDLE.epub',
        'cover': 'KINDLE_FRONT_COVER_LIGHT.jpg',
        'title': "Schrödinger's Paperwork",
    },
    {
        'folder': 'Book 2 - The Permitted Options',
        'docx': 'The_Permitted_Options_BOOK_2_REVISION_20261005.docx',
        'epub': 'The_Permitted_Options_KINDLE.epub',
        'cover': 'KINDLE_COVER_FINAL_2560.jpg',
        'title': 'The Permitted Options',
    },
]


def make_epub_source(source: Path, target: Path) -> None:
    with ZipFile(source) as zin:
        files = {item.filename: zin.read(item.filename) for item in zin.infolist()}
    xml = files['word/document.xml'].decode('utf-8')
    # Locate the first image paragraph described as the front cover. The
    # marker is alt text in Book 1 and the picture name in Book 2.
    pattern = re.compile(
        r'<w:p\b[^>]*>(?:(?!</w:p>).)*?(?:<wp:docPr\b[^>]*(?:descr="Front cover[^\"]*"|name="frontCover")[^>]*/>).*?</w:p>',
        re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(xml)
    if not match:
        raise ValueError(f'Could not find the front-cover page in {source}')
    start, end = match.span()
    # The DOCX cover page is followed by a dedicated page-break paragraph.
    following = re.match(
        r'<w:p\b[^>]*>(?:(?!</w:p>).)*(?:<w:br\b[^>]*w:type="page"[^>]*/>)(?:(?!</w:p>).)*?</w:p>',
        xml[end:],
        re.DOTALL,
    )
    if following:
        end += following.end()
    files['word/document.xml'] = (xml[:start] + xml[end:]).encode('utf-8')
    with ZipFile(target, 'w', ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)


def build(book: dict) -> None:
    folder = ROOT / book['folder']
    source = folder / book['docx']
    output = folder / book['epub']
    cover = folder / book['cover']
    with TemporaryDirectory(prefix='kindle-source-') as temp:
        temp_docx = Path(temp) / source.name
        make_epub_source(source, temp_docx)
        command = [
            'pandoc', str(temp_docx), '--from=docx', '--to=epub3', '--standalone',
            '--toc', '--toc-depth=3', '--split-level=2',
            f'--metadata=title={book["title"]}',
            '--metadata=author=Quentin Edmund Darling',
            '--metadata=language=en-GB',
            f'--epub-cover-image={cover}', f'--css={CSS}', f'--output={output}',
        ]
        subprocess.run(command, cwd=ROOT, check=True)
    print(f'Built {output}')


if __name__ == '__main__':
    for config in BOOKS:
        build(config)
