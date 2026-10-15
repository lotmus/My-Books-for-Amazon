from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Inches
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph
import shutil

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / 'Book 2 - The Permitted Options'
MASTER = BOOK / 'The_Permitted_Options_BOOK_2_REVISION_20261005.docx'
OUT = BOOK / 'diagrams'
OUT.mkdir(exist_ok=True)

# Three-part schematics make the core idea legible without turning the lecture
# into a textbook plate. Labels deliberately distinguish measured science from
# the novel's conjecture.
FIGURES = [
 ('01_tunnelling', 'TUNNELLING: AMPLITUDE THROUGH A BARRIER', ['APPROACHING STATE', 'FINITE BARRIER', 'TRANSMITTED AMPLITUDE'], 'Quantum: amplitude decays inside; it does not stop at the classical edge.', 'Story: the proposed cosmic barrier change is invented.'),
 ('02_vacuum', 'VACUUM ENERGY & CASIMIR BOUNDARIES', ['PLATES SET BOUNDARIES', 'ALLOWED FIELD MODES', 'MEASURABLE FORCE'], 'Measured: changing boundary conditions changes the force.', 'Not measured: absolute vacuum energy or a cosmic-scale Casimir cavity.'),
 ('03_inference', 'OUTCOME, RECORD, INFERENCE', ['QUANTUM OUTCOME', 'APPARATUS + RECORD', 'CLAIM ABOUT CAUSE'], 'Landauer bound: erasing a bit has a minimum heat cost under stated conditions.', 'A record’s cost does not prove that its outcome was predetermined.'),
 ('04_holography', 'BLACK HOLE ENTROPY SCALES WITH AREA', ['ENCLOSED REGION', 'BOUNDARY AREA', 'MAXIMUM INFORMATION'], 'Black-hole entropy is proportional to horizon area, motivating holographic bounds.', 'The holographic principle is a deep theoretical idea; this is not a literal projected picture.'),
 ('05_complementarity', 'COMPLEMENTARITY & THE FIREWALL PUZZLE', ['OUTSIDE DESCRIPTION', 'HORIZON CROSSING', 'INFALLING DESCRIPTION'], 'Complementarity and the firewall argument are competing theoretical responses to the black-hole information puzzle.', 'No firewall has been observed. The lecture also connects tunnelling to stellar fusion and core-collapse supernovae.'),
 ('07_godel', 'GÖDEL: FORMAL SYSTEMS HAVE LIMITS', ['FORMAL RULES', 'ARITHMETIC STATEMENTS', 'TRUE ≠ PROVABLE HERE'], 'Incompleteness applies to consistent, effectively axiomatized systems able to express arithmetic; undecidability also appears in some physics questions.', 'A bureaucracy is an analogy, not a mathematical instance of the theorem.'),
 ('08_games', 'STRATEGY, CORRELATION & UNDECIDABILITY', ['PLAYERS + PAYOFFS', 'ALLOWED CORRELATIONS', 'VALUE OF THE GAME'], 'Nash equilibrium concerns unilateral strategy changes; Bell-type nonlocal games test correlations.', 'An undecidable game value is a result about specified mathematical games, not every real-world decision.'),
 ('09_records', 'UNCERTAINTY, DECOHERENCE & REDUNDANT RECORDS', ['QUANTUM STATE', 'ENVIRONMENT COUPLING', 'STABLE, SHARED RECORDS'], 'Conjugate quantities obey uncertainty relations; environmental interactions can spread redundant records.', 'Decoherence explains loss of observable interference, not by itself why one outcome is experienced.'),
 ('10_decoherence', 'DECOHERENCE SELECTS STABLE POINTER STATES', ['SUPERPOSITION', 'ENVIRONMENT COUPLING', 'ROBUST POINTER STATES'], 'Interactions suppress interference between alternatives and help explain why some states leave stable records.', 'Decoherence is not a standalone solution to every interpretation of measurement.'),
 ('11_observer', 'OBSERVATION SELECTION EFFECT', ['MANY POSSIBLE CONDITIONS', 'OBSERVER EXISTS', 'OBSERVED CONDITIONS'], 'Our existence filters which environments we can observe.', 'That selection effect alone does not explain why the universe has its laws.'),
 ('12_entropy', 'ENTROPY COUNTS MICROSCOPIC POSSIBILITIES', ['MACROSTATE', 'MANY MICROSTATES', 'S = k ln Ω'], 'Boltzmann entropy links a macrostate to the number of microstates that realise it.', 'Maxwell’s demon does not evade thermodynamics: information handling and erasure have physical costs.'),
 ('13_contextuality', 'MEASUREMENT CONTEXT MATTERS', ['CHOOSE COMPATIBLE TESTS', 'MEASURE IN CONTEXT', 'NO FIXED VALUE FOR ALL'], 'The Kochen–Specker theorem rules out noncontextual value assignments for the relevant quantum observables.', 'Contextuality does not mean observers can choose outcomes or send faster-than-light messages.'),
 ('14_wormhole', 'EINSTEIN–ROSEN BRIDGE: CONNECTED, NOT TRAVERSABLE', ['REGION I', 'PINCHING THROAT', 'REGION II'], 'The maximally extended Schwarzschild solution has a bridge that closes too quickly to cross.', 'A stable, traversable wormhole needs conditions not shown by this solution.'),
 ('15_controls', 'A NULL RESULT NEEDS A KNOWN SENSITIVITY', ['CALIBRATE + CONTROL', 'ALTERNATE ON / OFF', 'REPORT LIMIT + RESULT'], 'Controls, drift checks, and stated sensitivity turn a null reading into evidence.', 'No detected signal is not proof of absolute absence.'),
 ('16_evidence', 'A SHARP CUTOFF CAN REVEAL A DECISION', ['CONTINUOUS MARGINS', 'EXACT CUT AT FOURTEEN', 'COMPARE EXPLANATIONS'], 'A smooth physical process and a rank-based human choice predict different patterns near a cutoff.', 'A likelihood ratio compares explanations; it is not itself the probability either explanation is true.'),
]

FONT = Path('C:/Windows/Fonts/arial.ttf')
FONT_BOLD = Path('C:/Windows/Fonts/arialbd.ttf')
def font(size, bold=False):
    p = FONT_BOLD if bold else FONT
    return ImageFont.truetype(str(p), size)

def wrap(draw, text, fnt, max_width):
    words, lines, line = text.split(), [], ''
    for word in words:
        test = (line + ' ' + word).strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= max_width:
            line = test
        else:
            if line: lines.append(line)
            line = word
    if line: lines.append(line)
    return lines

def make_figure(spec, dest):
    name, title, nodes, science, boundary = spec
    im = Image.new('RGB', (800, 440), '#f7f4ed')
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((12, 12, 788, 428), radius=18, fill='#fffdf8', outline='#173c60', width=3)
    d.text((34, 30), title, font=font(21, True), fill='#173c60')
    x0, y0, w, h, gap = 34, 93, 218, 100, 27
    for i, label in enumerate(nodes):
        x = x0 + i * (w + gap)
        d.rounded_rectangle((x, y0, x+w, y0+h), radius=12,
                            fill=('#e9f0f5' if i != 1 else '#f3ead8'),
                            outline=('#315f82' if i != 1 else '#9a7433'), width=2)
        lines = wrap(d, label, font(16, True), w-24)
        line_h = 22
        yy = y0 + (h - len(lines)*line_h)//2
        for line in lines:
            bb = d.textbbox((0,0), line, font=font(16,True))
            d.text((x+(w-(bb[2]-bb[0]))/2, yy), line, font=font(16,True), fill='#1d2b36')
            yy += line_h
        if i < 2:
            ax = x + w + 3
            d.line((ax, y0+h//2, ax+gap-9, y0+h//2), fill='#9a7433', width=4)
            d.polygon([(ax+gap-9,y0+h//2),(ax+gap-18,y0+h//2-7),(ax+gap-18,y0+h//2+7)], fill='#9a7433')
    d.text((36, 220), 'ESTABLISHED SCIENCE', font=font(14, True), fill='#315f82')
    yy=244
    for line in wrap(d, science, font(15), 724):
        d.text((36, yy), line, font=font(15), fill='#263746'); yy += 21
    d.text((36, 305), 'BOUNDARY / CAVEAT', font=font(14, True), fill='#8a5b22')
    yy=329
    for line in wrap(d, boundary, font(15), 724):
        d.text((36, yy), line, font=font(15), fill='#463b2c'); yy += 21
    im.save(dest, 'JPEG', quality=88, optimize=True, progressive=True)

for spec in FIGURES:
    make_figure(spec, OUT / (spec[0] + '.jpg'))

doc = Document(MASTER)
headings = {p.text: p for p in doc.paragraphs if p.style.name == 'Heading 2' and p.text.startswith('Lecture.')}
if len(headings) != 15:
    raise RuntimeError(f'Expected 15 lecture headings; found {len(headings)}')
for heading in headings.values():
    nxt = heading._p.getnext()
    if nxt is not None and nxt.xpath('.//w:drawing'):
        raise RuntimeError(f'An image already follows {heading.text}; refusing duplicate insertion')

for spec, heading in zip(FIGURES, headings.values()):
    image_path = OUT / (spec[0] + '.jpg')
    # Place the image after the lecture's short opening frame, so its labels
    # are interpreted in context and appear at the first relevant discussion.
    intro = next((p for p in heading._parent.paragraphs if p._p.getprevious() is heading._p), None)
    if intro is None:
        p_xml = OxmlElement('w:p')
        heading._p.addnext(p_xml)
        p = Paragraph(p_xml, heading._parent)
    else:
        p_xml = OxmlElement('w:p')
        intro._p.addnext(p_xml)
        p = Paragraph(p_xml, heading._parent)
    p.alignment = 1
    r = p.add_run()
    pic = r.add_picture(str(image_path), width=Inches(6.0))
    # Screen readers and Pandoc use this description; keep the image in-reading.
    docpr = pic._inline.docPr
    docpr.set('descr', spec[1].title() + '. ' + spec[3] + ' ' + spec[4])
    p.paragraph_format.space_after = Inches(0.08)

doc.save(MASTER)
print(f'Inserted {len(FIGURES)} 800 x 440 lecture diagrams into {MASTER}')
