"""One-off: replace invented first names in the 24 cases with generic roles (Lothar's no-names rule)."""
import re,sys
FILES=['md/02_part2a.md','md/03_part2b.md','md/04_part2c.md','md/05_part2d.md']
# per case: list of (exact phrase, replacement) applied first, then name -> role
PRE={
1:[("At thirty-nine he married Ruth.","At thirty-nine he married again.")],
3:[("Her daughter Ellen lived","Her daughter lived"),("Her son Robert lived","One son lived"),("Her other son, Philip, lived","The other son lived")],
4:[("he named his younger brother, Josef, because","he named his younger brother, because"),("Years later Helmut met Lena, a retired pharmacist,","Years later he met a retired pharmacist,")],
5:[("a twelve-year-old son, Mateo, who","a twelve-year-old son who"),("Rosa's sister, Carmen, lived nearby","Her sister lived nearby"),("she wrote \"Mateo,\" with his date of birth","she wrote her son's name, with his date of birth")],
6:[("Paul, the eldest, lived","The eldest son lived"),("Susan lived in Seattle","The daughter lived in Seattle"),("Mark lived in Phoenix","The younger son lived in Phoenix")],
7:[("Her only son, Mark, was","Her only son was")],
8:[("Anna, Ben, and Clara grew up","Three siblings, an elder sister, a brother, and a younger sister, grew up"),("Ben also had a son, Tyler, from","He also had a son from")],
9:[("George had two children, Lisa and Andrew, from","The husband had two children from"),("she had a niece, Hannah, her late sister's daughter,","she had a niece, her late sister's daughter,"),("Lisa and Andrew","his two children"),("Lisa's and Andrew's","his children's")],
10:[("His son Jonas, a quiet man","His son, a quiet man"),("His sister Sophie lived in Hamburg","His sister lived in Hamburg")],
11:[("with Birgit, a former bookseller,","with a former bookseller, his partner,"),("his niece Katrin, the daughter of his late brother,","his niece, the daughter of his late brother,"),("his surviving sister, Monika, and","his surviving sister and"),("Katrin and her brother","his niece and nephew"),("Monika and Katrin's brother","His sister and his nephew"),("Katrin's brother","his nephew")],
12:[("two adult children, Marcus and Joy, and a stepson, Derek,","two adult children, a son and a daughter, and a stepson"),("\"Marcus, Joy, and Derek.\"","the three children's names."),("Marcus, Joy, and Derek","the three children"),("Marcus and Joy","her son and daughter")],
13:[("two daughters, Diane and Maria, and","two daughters and"),("with Diane's husband, Kevin.","with his elder daughter's husband."),("his next-door neighbour, Harold, and Kevin,","his next-door neighbour and the son-in-law,"),("Maria, who lived in Sacramento","The younger daughter, who lived in Sacramento"),("Diane and Maria","the two daughters")],
14:[("a granddaughter, Lea, who","a granddaughter who"),("during a hard time in Lea's own life","during a hard time in her own life")],
15:[("a daughter, Natalie, from","a daughter from"),("a second wife, Sharon, and a son with her, Jake.","a second wife and a son with her."),("Sharon and Jake","the second wife and her son")],
16:[("Her son, Eric, lived","Her son lived")],
17:[("with Denise, a dental receptionist,","with his partner, a dental receptionist,"),("Robert's brother, Gary, who","His brother, who")],
18:[("Robert's case","Case 17")],
19:[("her daughter, Joan, as","her daughter as"),("Her son, Tim, lived","Her son lived")],
20:[("two children, Claudia and Peter, in","two children, a daughter and a son, in"),("our children Claudia and Peter shall","our children shall"),("he met Monika, a widow from Lübeck","he met a widow from Lübeck"),("Claudia and Peter","the two children"),("Hans and Ingrid married","The husband and his first wife married")],
21:[("He married an American, Lisa; they had a son, Ben, and","He married an American; they had a son and"),("He met Helga, a widow.","He met a widow, who became his partner."),("naming his son Ben as","naming his son as"),("\"Everything I own in Germany goes to Helga.\"","\"Everything I own in Germany goes to\" his partner, by name.")],
22:[("her sister, Nina, and naming Nina as","her sister and naming her as")],
23:[("at sixty, to Carla, who brought into the marriage a grown daughter, Alicia.","at sixty, to a widow who brought a grown daughter into the marriage."),("two sons of his own, Daniel and Luis,","two sons of his own"),("Daniel and Luis","the two sons"),("Carla died","His wife died")],
24:[("married to Priya,","married,"),("When Oliver and Priya saw","When he and his wife saw"),("\"That way Priya will have them,\"","\"That way my wife will have them,\"")],
}
ROLE={
1:{'Daniel':'the husband','Ruth':'his second wife'},
2:{'Karin':'the wife','Thomas':'the husband'},
3:{'Margaret':'the mother','Ellen':'the daughter','Robert':'the son in Oregon','Philip':'the son in Texas'},
4:{'Helmut':'the engineer','Josef':'his brother','Lena':'his partner'},
5:{'Rosa':'the mother','Mateo':'the boy','Carmen':'the aunt'},
6:{'Walter':'the father','Paul':'the eldest son','Susan':'the daughter','Mark':'the younger son'},
7:{'Gisela':'the mother','Mark':'the son'},
8:{'Anna':'the elder sister','Ben':'the brother','Clara':'the younger sister','Tyler':'the brother\'s son'},
9:{'Patricia':'the wife','George':'the husband','Lisa':'his daughter','Andrew':'his son','Hannah':'the niece'},
10:{'Friedrich':'the father','Jonas':'the son','Sophie':'the daughter'},
11:{'Uwe':'the engineer','Birgit':'his partner','Katrin':'the niece','Monika':'his sister'},
12:{'Linda':'the mother','Marcus':'her son','Joy':'her daughter','Derek':'the stepson'},
13:{'Frank':'the father','Diane':'the elder daughter','Maria':'the younger daughter','Kevin':'the son-in-law','Harold':'the neighbour'},
14:{'Elisabeth':'the grandmother','Lea':'the granddaughter'},
15:{'Victor':'the father','Natalie':'the daughter','Sharon':'the second wife','Jake':'the younger son'},
16:{'Carol':'the mother','Eric':'the son'},
17:{'Robert':'the electrician','Denise':'his partner','Gary':'his brother'},
18:{'Martin':'the husband','Petra':'the wife'},
19:{'Edith':'the mother','Joan':'the daughter','Tim':'the son'},
20:{'Hans':'the husband','Ingrid':'his first wife','Monika':'the second wife','Claudia':'the daughter','Peter':'the son'},
21:{'Stefan':'the emigrant','Lisa':'his former wife','Ben':'the son','Helga':'his partner'},
22:{'Claire':'the designer','Nina':'the sister'},
23:{'Raymond':'the father','Carla':'his wife','Alicia':'the stepdaughter','Daniel':'the elder son','Luis':'the younger son'},
24:{'Oliver':'the developer','Priya':'his wife'},
}
def cap_fix(s):
    # capitalise roles at sentence starts
    s=re.sub(r'(^|[.!?]\s+|\*\*\s+|^\s*[-*]\s+|^\s*\d+\.\s+|[.!?]["\u201d]\s+|\n\n)(the|his|her) ',lambda m:m.group(1)+m.group(2).capitalize()+' ',s,flags=re.M)
    s=re.sub(r'(^|\n)(the|his|her) ',lambda m:m.group(1)+m.group(2).capitalize()+' ',s)
    return s
def run():
    left=[]
    for f in FILES:
        s=open(f).read(); parts=re.split(r'(?m)(?=^### Case )',s); out=[]
        for p in parts:
            m=re.match(r'### Case (\d+):',p)
            if m:
                n=int(m.group(1))
                for a,b in PRE.get(n,[]):
                    if a not in p: print('PRE miss',n,a); 
                    p=p.replace(a,b)
                for name,role in ROLE[n].items():
                    p=re.sub(r'\b'+name+r'\b',role,p)
                p=cap_fix(p)
                # Title line: keep heading capitalisation intact
            out.append(p)
        open(f,'w').write(''.join(out))
run()
