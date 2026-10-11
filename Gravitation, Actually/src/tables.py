# Rev9: the three number tables of Appendix B, drawn at 1600 px wide so they stay readable on a phone.
from PIL import Image, ImageDraw, ImageFont
O='/workspace/grav9/img/'
FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; FR='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
T1=[['Speed (fraction of c)','Time factor','Same speed added twice','Interval² for 1 s of travel']]+[r.split('|') for r in '''0.1|1.005|0.198|−0.99
0.2|1.021|0.385|−0.96
0.3|1.048|0.550|−0.91
0.4|1.091|0.690|−0.84
0.5|1.155|0.800|−0.75
0.6|1.250|0.882|−0.64
0.7|1.400|0.940|−0.51
0.8|1.667|0.976|−0.36
0.9|2.294|0.994|−0.19
0.95|3.203|0.9987|−0.0975
0.99|7.089|0.99995|−0.0199
0.998 (cosmic-ray muons)|15.82|0.999998|−0.0040'''.split('\n')]
T2=[['Mass (Suns)','Horizon radius (if not spinning)','Example']]+[r.split('|') for r in '''1|2.95 km|the Sun, as a comparison
3|8.9 km|just past the heaviest neutron stars
10|29.5 km|a typical stellar black hole
36|106 km|the heavier hole in GW150914
62|183 km|the hole GW150914 left behind
100|295 km|
1,000|2,950 km|
4.3 million|12.7 million km (0.085 AU)|Sgr A*, the center of the Milky Way
6.5 billion|19.2 billion km (128 AU)|M87*'''.split('\n')]
T3=[['Place (height)','Height term, µs/day','Speed term, µs/day','Net vs ground, µs/day']]+[r.split('|') for r in '''Harvard tower (22.5 m)|+0.000212|0|+0.000212
Mount Everest (8.8 km)|+0.083|0|+0.083
Space station (400 km)|+3.6|−28.3|−24.7
GPS satellite (20,200 km)|+45.7|−7.2|+38.5
Geostationary (35,786 km)|+51.1|−4.5|+46.5'''.split('\n')]
def wrap(d,text,font,w):
    words=text.split(); lines=[]; cur=''
    for wd in words:
        t=(cur+' '+wd).strip()
        if d.textlength(t,font=font)<=w: cur=t
        else: lines.append(cur); cur=wd
    lines.append(cur); return lines or ['']
def table(rows,widths,name,W=1600,fs=40):
    fb=ImageFont.truetype(FB,fs); fr=ImageFont.truetype(FR,fs)
    tmp=ImageDraw.Draw(Image.new('RGB',(10,10))); pad=18; lh=int(fs*1.25)
    cw=[int(W*w) for w in widths]; cw[-1]=W-sum(cw[:-1])
    hts=[]
    for i,r in enumerate(rows):
        f=fb if i==0 else fr
        hts.append(max(len(wrap(tmp,c,f,cw[j]-2*pad)) for j,c in enumerate(r))*lh+2*pad)
    img=Image.new('RGB',(W,sum(hts)+4),'white'); d=ImageDraw.Draw(img); y=0
    for i,r in enumerate(rows):
        f=fb if i==0 else fr; x=0
        if i==0: d.rectangle([0,0,W-1,hts[0]],fill='#dde7f2')
        elif i%2==0: d.rectangle([0,y+2,W-1,y+hts[i]-1],fill='#f6f8fb')
        for j,c in enumerate(r):
            for k,ln in enumerate(wrap(d,c,f,cw[j]-2*pad)): d.text((x+pad,y+pad+k*lh),ln,font=f,fill='black')
            x+=cw[j]
        y+=hts[i]; d.line([0,y,W,y],fill='#999999',width=2)
    x=0
    for w in cw[:-1]: x+=w; d.line([x,0,x,y],fill='#999999',width=2)
    d.rectangle([0,0,W-1,y],outline='#666666',width=3)
    img=img.crop((0,0,W,y+2)); img.save(O+name,optimize=True); print(name,img.size)
table(T1,[0.30,0.20,0.25,0.25],'table_speed.png')
table(T2,[0.20,0.36,0.44],'table_horizon.png')
table(T3,[0.34,0.22,0.22,0.22],'table_height.png')
