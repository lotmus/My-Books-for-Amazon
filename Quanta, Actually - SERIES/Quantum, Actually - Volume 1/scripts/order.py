from docx.oxml.ns import qn
PPR = ['pStyle','keepNext','keepLines','pageBreakBefore','framePr','widowControl','numPr','suppressLineNumbers','pBdr','shd','tabs','suppressAutoHyphens','kinsoku','wordWrap','overflowPunct','topLinePunct','autoSpaceDE','autoSpaceDN','bidi','adjustRightInd','snapToGrid','spacing','ind','contextualSpacing','mirrorIndents','suppressOverlap','jc','textDirection','textAlignment','textboxTightWrap','outlineLvl','divId','cnfStyle','rPr','sectPr','pPrChange']
RPR = ['rStyle','rFonts','b','bCs','i','iCs','caps','smallCaps','strike','dstrike','outline','shadow','emboss','imprint','noProof','snapToGrid','vanish','webHidden','color','spacing','w','kern','position','sz','szCs','highlight','u','effect','bdr','shd','fitText','vertAlign','rtl','cs','em','lang','eastAsianLayout','specVanish','oMath']
def _sort(el, order):
    W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    kids=list(el)
    def key(c):
        t=c.tag.replace(W,'') if isinstance(c.tag,str) else ''
        return order.index(t) if c.tag.startswith(W) and t in order else len(order)
    s=sorted(kids,key=key)
    if s!=kids:
        for c in kids: el.remove(c)
        for c in s: el.append(c)
        return 1
    return 0
def fix_order(p_el):
    n=0
    for pPr in p_el.iter(qn('w:pPr')):
        n+=_sort(pPr,PPR)
    for rPr in p_el.iter(qn('w:rPr')):
        n+=_sort(rPr,RPR)
    return n
