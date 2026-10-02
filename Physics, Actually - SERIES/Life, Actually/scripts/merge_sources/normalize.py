"""House-style normalization so the whole book reads as one text:
American spelling (as in the Physics, Actually volumes) and typographic (curly) quotes."""
import re
# lowercase-initial stems; capitalised forms are converted too unless part of a proper name list
# (british_stem, american_stem, allowed_suffix_regex)
SUF_OUR = r'(s|ed|ing|ful|fully|less|able|ably|ite|ites|er|ers|ist|ists|ism)?'
PAIRS = [(w+'our', w+'or', SUF_OUR) for w in ['col','fav','flav','behavi','lab','hon','neighb','hum','rum','od','vap','harb','tum','arm','sav','endeav','rig','vig','splend','clam','ferv']]
PAIRS += [('neighbourhood','neighborhood','(s)?'),('favourite','favorite','(s)?'),('honourable','honorable','')]
PAIRS += [(p+'metre',p+'meter','(s)?') for p in ['kilo','centi','milli','micro','nano','pico','deci']]
PAIRS += [(p+'litre',p+'liter','(s)?') for p in ['milli','micro','nano','pico','deci','centi']]
PAIRS += [('prising','prying',''),('detasselling','detasseling',''),('resynthesising','resynthesizing',''),('resynthesise','resynthesize','(d|s)?')]
PAIRS += [('centre','center','(s)?'),('centred','centered',''),('centring','centering',''),('metre','meter','(s)?'),
 ('litre','liter','(s)?'),('fibre','fiber','(s)?'),('theatre','theater','(s)?'),('calibre','caliber',''),('sombre','somber',''),
 ('grey','gray','(s|er|est|ed|ing|ish|ness)?'),('mould','mold','(s|ed|ing|y)?'),('plough','plow','(s|ed|ing)?'),
 ('aluminium','aluminum',''),('sulphur','sulfur',''),('sulphate','sulfate','(s)?'),('sulphide','sulfide','(s)?'),
 ('haemoglobin','hemoglobin',''),('haemophilia','hemophilia',''),('haemophiliac','hemophiliac','(s)?'),('anaemia','anemia',''),
 ('leukaemia','leukemia','(s)?'),('oestrogen','estrogen','(s)?'),('foetus','fetus','(es)?'),('foetal','fetal',''),
 ('paediatric','pediatric','(s|ian|ians)?'),('oesophagus','esophagus',''),('diarrhoea','diarrhea',''),('caesarean','cesarean',''),
 ('manoeuvre','maneuver','(s|d)?'),('programme','program','(s)?'),('catalogue','catalog','(s)?'),('catalogued','cataloged',''),
 ('analogue','analog','(s)?'),('defence','defense','(s|less)?'),('offence','offense','(s)?'),('licence','license','(s)?'),
 ('pretence','pretense',''),('cheque','check','(s)?'),('tyre','tire','(s)?'),('storey','story',''),('storeys','stories',''),
 ('jewellery','jewelry',''),('artefact','artifact','(s)?'),('sceptic','skeptic','(s|al|ally|ism)?'),('judgement','judgment','(s|al)?'),
 ('ageing','aging',''),('acknowledgement','acknowledgment','(s)?'),('enrol','enroll','(s)?'),('enrolment','enrollment','(s)?'),
 ('fulfil','fulfill','(s)?'),('fulfilment','fulfillment',''),('skilful','skillful','(ly)?'),('wilful','willful','(ly)?'),
 ('instalment','installment','(s)?'),('learnt','learned',''),('spelt','spelled',''),('whilst','while',''),('amongst','among',''),
 ('towards','toward',''),('afterwards','afterward',''),('practise','practice','(s)?'),('practised','practiced',''),('practising','practicing',''),
 ('kerb','curb','(s)?'),('pyjamas','pajamas',''),('draught','draft','(s)?'),('gaol','jail',''),
 ('travelled','traveled',''),('travelling','traveling',''),('traveller','traveler','(s)?'),('labelled','labeled',''),('labelling','labeling',''),
 ('modelled','modeled',''),('modelling','modeling',''),('cancelled','canceled',''),('cancelling','canceling',''),
 ('signalled','signaled',''),('signalling','signaling',''),('fuelled','fueled',''),('fuelling','fueling',''),
 ('counselled','counseled',''),('counselling','counseling',''),('counsellor','counselor','(s)?'),('channelled','channeled',''),
 ('tunnelled','tunneled',''),('tunnelling','tunneling',''),('levelled','leveled',''),('totalled','totaled',''),('dialled','dialed',''),
 ('marvellous','marvelous',''),('jewelled','jeweled',''),('quarrelled','quarreled',''),('equalled','equaled',''),('rivalled','rivaled',''),
 ('analyse','analyze','(d)?'),('analysing','analyzing',''),('catalyse','catalyze','(d|s)?'),('catalysing','catalyzing',''),
 ('paralyse','paralyze','(d|s)?'),('hydrolyse','hydrolyze','(d|s)?'),('dialyse','dialyze','(d|s)?'),
 ('emphasise','emphasize','(d|s)?'),('emphasising','emphasizing',''),('synthesise','synthesize','(d|s|r|rs)?'),('synthesising','synthesizing',''),
 ('photosynthesise','photosynthesize','(d|s)?'),('photosynthesising','photosynthesizing',''),('fossilise','fossilize','(d|s)?'),('fossilised','fossilized',''),
]
ISE = ['realis','recognis','organis','characteris','summaris','criticis','apologis','specialis','standardis',
 'minimis','maximis','hybridis','colonis','sterilis','fertilis','ionis','metabolis','memoris','prioritis',
 'patronis','legalis','modernis','mobilis','immunis','neutralis','visualis','optimis','utilis','stabilis','authoris',
 'capitalis','commercialis','industrialis','popularis','publicis','scrutinis','sympathis','theoris','harmonis',
 'categoris','civilis','crystallis','digitis','energis','familiaris','finalis','formalis','generalis','globalis',
 'hospitalis','internalis','italicis','jeopardis','localis','marginalis','monopolis','normalis','penalis','personalis',
 'polaris','privatis','randomis','rationalis','revolutionis','sanitis','satiris','socialis','stigmatis','symbolis',
 'trivialis','urbanis','vaporis','vandalis','westernis','dramatis','agonis','antagonis','galvanis','pasteuris',
 'homogenis','methylis','mineralis','oxidis','polymeris','solubilis','sensitis','desensitis','computeris','customis',
 'idealis','immobilis','naturalis','nationalis','plagiaris','miniaturis','proselytis','terroris','tantalis','sterilis','mesmeris',
 'apologis','vernalis','improvis','motoris','weaponis','cannibalis','emphasis_','fictionalis','sexualis','glamoris','romanticis','victimis']
PROTECT = ['Centre for','Centre,','Wellcome','Sanger Centre','Medical Research Council','Labour Party','Programme for',
 'Defence Research','Ministry of Defence','Human Fertilisation','Fertilisation and Embryology','World Health Organization']

def _case(src, rep):
    if src.isupper(): return rep.upper()
    if src[0].isupper(): return rep[0].upper()+rep[1:]
    return rep

def americanize(text):
    # protect proper names
    keep={}
    for i,p in enumerate(PROTECT):
        tok=f'\x00P{i}\x00'
        if p in text: text=text.replace(p,tok); keep[tok]=p
    # protect URLs/paths and image links
    urls={}
    def _u(m):
        k=f'\x00U{len(urls)}\x00'; urls[k]=m.group(0); return k
    text=re.sub(r'\]\([^)]*\)|https?://\S+',_u,text)
    for brit,am,suf in PAIRS:
        text=re.sub(r'\b'+brit+suf+r'\b', lambda m,b=brit,a=am: _case(m.group(0), a+m.group(0)[len(b):].lower()), text, flags=re.I)
    for stem in set(ISE):
        if stem.endswith('_'): continue
        text=re.sub(r'\b((?:un|re|de|non|over|under|mis|pre|self-)?)'+stem+r'(e|ed|es|ing|ation|ations|er|ers|able|ational)\b',
                    lambda m: m.group(1)+m.group(0)[len(m.group(1)):len(m.group(1))+len(stem)-1]+'z'+m.group(0)[len(m.group(1))+len(stem):], text, flags=re.I)
    for k,v in urls.items(): text=text.replace(k,v)
    for k,v in keep.items(): text=text.replace(k,v)
    return text

def smart_quotes(text):
    urls={}
    def _u(m):
        k=f'\x00U{len(urls)}\x00'; urls[k]=m.group(0); return k
    text=re.sub(r'\]\([^)]*\)|https?://\S+',_u,text)
    text=re.sub(r'(^|[\s(\[\u2014\u2013/*_-])"', lambda m:m.group(1)+'\u201c', text, flags=re.M)
    text=text.replace('"','\u201d')
    text=re.sub(r"(^|[\s(\[\u2014\u2013/*_\u201c-])'(?=\w)", lambda m:m.group(1)+'\u2018', text, flags=re.M)
    text=text.replace("'",'\u2019')
    # restore years/abbrev: ‘90s → ’90s
    text=re.sub('\u2018(\\d\\d)s\\b','\u2019'+r'\1s',text)
    for k,v in urls.items(): text=text.replace(k,v)
    return text
