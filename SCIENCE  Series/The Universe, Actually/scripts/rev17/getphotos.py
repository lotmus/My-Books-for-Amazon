"""Download the NASA public-domain photos used in REV18 (NASA Image and Video Library API). Writes photos/<key>.jpg and photos/meta.json."""
import urllib.request, urllib.parse, json, os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); os.makedirs(HERE+'/photos',exist_ok=True)
IDS={'p01_aurora':'iss029e012564','p02_jupiter':'PIA21376','p03_saturn':'PIA14934','p04_pluto':'PIA19966','p05_sun':'PIA26681',
 'p06_cliffs':'carina_nebula','p07_pillars':'GSFC_20171208_Archive_e000842','p08_crab':'PIA03606','p09_ring':'southern_ring_nebula',
 'p10_xdf':'GSFC_20171208_Archive_e001651','p11_andromeda':'PIA04921','p12_lens':'GSFC_20171208_Archive_e000791',
 'p13_bluemarble':'GSFC_20171208_Archive_e001386','p14_enceladus':'PIA07760','p15_europa':'PIA19048','p16_perseverance':'PIA24542',
'p18_apollo11':'as11-37-5545','p19_milkyway':'PIA03653'}
meta={}
for key,nid in IDS.items():
    j=json.load(urllib.request.urlopen('https://images-api.nasa.gov/asset/'+urllib.parse.quote(nid),timeout=30))
    urls=[i['href'] for i in j['collection']['items']]
    pick=None
    for tag in ('~large.jpg','~medium.jpg','~orig.jpg'):
        pick=next((u for u in urls if u.lower().endswith(tag)),None)
        if pick: break
    if not pick: pick=next(u for u in urls if u.lower().endswith('.jpg'))
    s=json.load(urllib.request.urlopen('https://images-api.nasa.gov/search?nasa_id='+urllib.parse.quote(nid),timeout=30))
    d=s['collection']['items'][0]['data'][0]
    fn=HERE+'/photos/'+key+'.jpg'
    urllib.request.urlretrieve(pick.replace(' ','%20'),fn)
    meta[key]={'nasa_id':nid,'url':pick,'title':d.get('title'),'center':d.get('center'),'credit':d.get('photographer') or d.get('secondary_creator') or '', 'description':(d.get('description') or '')[:400]}
    print(key,os.path.getsize(fn)//1024,'KB',pick.rsplit('/',1)[-1])
json.dump(meta,open(HERE+'/photos/meta.json','w',encoding='utf-8'),indent=1,ensure_ascii=False)
