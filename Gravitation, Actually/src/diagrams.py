import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Polygon
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
O='/workspace/grav/img/'
BLUE='#1f4e79'; ORANGE='#d9822b'; GREY='#666666'
def save(fig,name):
    fig.savefig(O+name,dpi=300,bbox_inches='tight',facecolor='white'); plt.close(fig)

# 1 light clock
fig,ax=plt.subplots(figsize=(7,3.6))
ax.set_xlim(-0.5,10.5);ax.set_ylim(-0.8,4.2);ax.axis('off')
# rest clock
for y in (0,3): ax.plot([0.2,1.8],[y,y],color=BLUE,lw=4)
ax.annotate('',xy=(1,2.95),xytext=(1,0.05),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=2))
ax.text(1,3.5,'clock at rest',ha='center',fontsize=10)
# moving clock
xs=[3.5,6.5,9.5]
for x in xs:
    for y in (0,3): ax.plot([x-0.8,x+0.8],[y,y],color=BLUE,lw=4,alpha=0.35 if x!=xs[1] else 1)
ax.plot([xs[0],xs[1]],[0,3],color=ORANGE,lw=2); ax.plot([xs[1],xs[2]],[3,0],color=ORANGE,lw=2)
ax.annotate('',xy=(9.3,3.7),xytext=(3.7,3.7),arrowprops=dict(arrowstyle='->',color=GREY,lw=1.5))
ax.text(6.5,3.85,'clock moves at speed v',ha='center',color=GREY,fontsize=10)
ax.text(4.6,1.5,'c·t',color=ORANGE,fontsize=11,ha='right'); ax.text(6.6,1.3,'c·t₀',color=BLUE,fontsize=11)
ax.plot([xs[1],xs[1]],[0,3],color=BLUE,ls=':',lw=1.5)
ax.plot([xs[0],xs[1]],[0,0],color=GREY,ls='--',lw=1); ax.text(5,-0.25,'v·t',ha='center',color=GREY,fontsize=10)
ax.text(5.2,-0.6,'Seen from the platform: a zigzag, a longer path at the same speed c.\nPythagoras: (ct)² = (ct₀)² + (vt)², so t = t₀ / √(1 − v²/c²)',ha='center',va='top',fontsize=10)
save(fig,'diag_light_clock.png')

# 2 light cone / spacetime diagram
fig,ax=plt.subplots(figsize=(6,5.2))
ax.set_xlim(-3.2,3.2);ax.set_ylim(-3.2,3.4);ax.set_aspect('equal');ax.axis('off')
ax.fill_between([-3,0,3],[3,0,3],[3.2,3.2,3.2],color='#dbe8f5'); ax.fill_between([-3,0,3],[-3,0,-3],[-3.2,-3.2,-3.2],color='#f7e3cf')
ax.plot([-3,3],[-3,3],color=ORANGE,lw=2);ax.plot([-3,3],[3,-3],color=ORANGE,lw=2)
ax.annotate('',xy=(0,3.3),xytext=(0,-3.2),arrowprops=dict(arrowstyle='->',color='k'));ax.annotate('',xy=(3.2,0),xytext=(-3.2,0),arrowprops=dict(arrowstyle='->',color='k'))
ax.text(0.1,3.25,'time (c·t)',fontsize=10);ax.text(2.4,-0.35,'space',fontsize=10)
ax.text(-1.25,2.45,'future light cone\n(timelike: you can\nget there)',ha='center',fontsize=10,color=BLUE)
ax.text(1.25,-2.75,'past light cone\n(timelike: it can\nreach you)',ha='center',fontsize=10,color='#8a4b12')
ax.text(-2.1,0.5,'elsewhere\n(spacelike)',ha='center',fontsize=10,color=GREY);ax.text(2.1,0.5,'elsewhere\n(spacelike)',ha='center',fontsize=10,color=GREY)
ax.plot(0,0,'ko');ax.text(0.15,-0.3,'here, now',fontsize=10)
t=np.linspace(-3,3,50); ax.plot(0.3*t+0.05*t**2,t,color=BLUE,lw=1.5,ls='--'); ax.text(0.88,1.95,'a traveler’s\nworldline',fontsize=9,color=BLUE)
ax.text(2.25,2.7,'light',color=ORANGE,fontsize=10,rotation=45)
save(fig,'diag_light_cone.png')

# 3 tidal stretching
fig,ax=plt.subplots(figsize=(7,4))
ax.set_xlim(-1,11);ax.set_ylim(-3,3);ax.set_aspect('equal');ax.axis('off')
ax.add_patch(Circle((0,0),1.2,color='#4a7fb5'));ax.text(0,0,'Earth',ha='center',va='center',color='white',fontsize=10)
cx=6
th=np.linspace(0,2*np.pi,200)
ax.plot(cx+1.6*np.cos(th),1.6*np.sin(th),color=GREY,ls=':',lw=1)
ax.plot(cx+2.1*np.cos(th),1.25*np.sin(th),color=ORANGE,lw=2)
pts=[(cx-1.6,0,-1,0),(cx+1.6,0,1,0),(cx,1.6,0,-1),(cx,-1.6,0,1)]
for x,y,dx,dy in pts:
    ax.annotate('',xy=(x+0.9*dx,y+0.55*dy),xytext=(x,y),arrowprops=dict(arrowstyle='->',color=BLUE,lw=2))
    ax.plot(x,y,'o',color=BLUE)
ax.text(cx,2.55,'A ring of free balls, falling together, seen from its own center',ha='center',fontsize=10)
ax.text(cx,-2.6,'Near and far balls drift apart; side balls drift together.\nThe ring becomes an egg pointing at the Earth. That stretch is the tide.',ha='center',fontsize=10)
ax.annotate('',xy=(1.5,0),xytext=(3.8,0),arrowprops=dict(arrowstyle='->',color=GREY,lw=1,ls='--'));ax.text(2.6,0.25,'toward\nthe center',ha='center',fontsize=9,color=GREY)
save(fig,'diag_tides.png')

# 4 GPS budget
fig,ax=plt.subplots(figsize=(6.5,3.8))
vals=[45.7,-7.2,38.5];labs=['Height\n(gentler bend in time)','Speed\n(3.9 km/s orbit)','Net offset\nper day']
cols=[BLUE,ORANGE,'#3a7d44']
b=ax.bar(labs,vals,color=cols,width=0.55)
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v+(1.5 if v>0 else -4.5),f'{v:+.1f} µs',ha='center',fontsize=11)
ax.axhline(0,color='k',lw=0.8);ax.set_ylabel('microseconds per day\n(satellite clock vs ground clock)');ax.set_ylim(-14,55)
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.set_title('38.5 µs × c ≈ 11.5 km of range error per day, if left uncorrected',fontsize=10,color=GREY)
save(fig,'diag_gps.png')

# 5 L-shaped LIGO
fig,ax=plt.subplots(figsize=(6,5.4))
ax.set_xlim(-1,11);ax.set_ylim(-1.8,10.5);ax.set_aspect('equal');ax.axis('off')
ax.plot([0,9.5],[0,0],color=GREY,lw=6,solid_capstyle='butt');ax.plot([0,0],[0,9.5],color=GREY,lw=6,solid_capstyle='butt')
ax.add_patch(Rectangle((9.5,-0.5),0.6,1,color=BLUE));ax.add_patch(Rectangle((-0.5,9.5),1,0.6,color=BLUE))
ax.text(10.4,0.0,'mirror',va='center',fontsize=9);ax.text(0.7,10.1,'mirror',fontsize=9)
ax.add_patch(Polygon([[-0.45,-0.45],[0.45,0.45],[0.55,0.35],[-0.35,-0.55]],color=ORANGE))
ax.text(0.7,-0.75,'beam splitter',fontsize=9)
ax.add_patch(Rectangle((-1.0,-1.6),0.9,0.7,color='#c0392b'));ax.text(-0.55,-1.85,'laser',ha='center',va='top',fontsize=9)
ax.plot([-0.55,0],[-0.9,0],color='#c0392b',lw=1.5)
ax.add_patch(Circle((1.2,-1.25),0.3,color='k'));ax.plot([0,1.2],[0,-1.25],color='#c0392b',lw=1.2,ls='--');ax.text(1.65,-1.35,'detector',fontsize=9)
ax.plot([0,9.5],[0.15,0.15],color='#c0392b',lw=1.2);ax.plot([0.15,0.15],[0,9.5],color='#c0392b',lw=1.2)
ax.text(5,0.6,'arm 1: 4 km',fontsize=10,ha='center');ax.text(-0.6,5,'arm 2: 4 km',fontsize=10,rotation=90,va='center')
ax.text(5.5,6.2,'A passing wave stretches one arm\nwhile it squeezes the other,\nthen they swap.\nChange in length: about\n4 × 10⁻¹⁸ m, a few thousandths\nof a proton’s width.',fontsize=10,ha='center')
ax.annotate('',xy=(9.9,1.2),xytext=(8.9,1.2),arrowprops=dict(arrowstyle='<->',color=BLUE));ax.annotate('',xy=(1.2,9.9),xytext=(1.2,8.9),arrowprops=dict(arrowstyle='<->',color=BLUE))
save(fig,'diag_ligo.png')

# 6 lensing
fig,ax=plt.subplots(figsize=(7.5,3.6))
ax.set_xlim(-0.8,10.5);ax.set_ylim(-3.1,3.1);ax.axis('off')
ax.add_patch(Circle((0,0),0.18,color='#f1c40f'));ax.text(0,-0.5,'distant\nquasar',ha='center',va='top',fontsize=9)
ax.add_patch(Circle((5,0),0.55,color='#7f8c8d',alpha=0.8));ax.text(5,-0.75,'galaxy or cluster\n(visible + dark mass)',ha='center',va='top',fontsize=9)
ax.add_patch(Circle((10,0),0.15,color=BLUE));ax.text(10,-0.4,'Earth',ha='center',va='top',fontsize=9)
for s in (1,-1):
    ax.plot([0,5,10],[0,1.3*s,0],color=ORANGE,lw=1.8)
    ax.plot([10,0],[0,2.6*s],color=ORANGE,lw=1,ls='--')
    ax.add_patch(Circle((0,2.6*s),0.15,color='#f1c40f',alpha=0.6))
ax.text(0.3,2.6,'where Earth sees image 1',fontsize=9,va='center');ax.text(0.3,-2.6,'where Earth sees image 2',fontsize=9,va='center')
ax.text(7.6,1.3,'paths bent by the\nmass in between',fontsize=9,color=ORANGE)
ax.text(7.2,-2.3,'The bend weighs the lens. More bend than\nthe visible stars allow = extra, dark mass.',fontsize=9,ha='center',color=GREY)
save(fig,'diag_lensing.png')
print('ok')
