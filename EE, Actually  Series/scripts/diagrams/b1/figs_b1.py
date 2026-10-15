import sys; sys.path.insert(0,'../common')
from eestyle import *
import numpy as np, schemdraw, schemdraw.elements as elm
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle, FancyBboxPatch
O='fig/'
# 1.1 conductor vs insulator
f,ax=fig(8,3.8); ax.axis('off'); ax.set_xlim(0,16); ax.set_ylim(0,7.6); ax.grid(False)
rng=np.random.default_rng(3)
for x0,title,free in ((0.3,'Metal (conductor)',True),(8.3,'Plastic or glass (insulator)',False)):
    ax.add_patch(Rectangle((x0,0.6),7.4,5.6,fc='#f6f6f6',ec=INK,lw=1))
    ax.text(x0+3.7,6.8,title,ha='center',fontsize=12,weight='bold')
    for i in range(4):
        for j in range(3):
            cx,cy=x0+1.0+i*1.8,1.6+j*1.8
            ax.add_patch(Circle((cx,cy),0.42,fc='#e8c9a0',ec=INK,lw=0.8)); ax.text(cx,cy,'+',ha='center',va='center',fontsize=11)
            if free:
                ex,ey=cx+0.9+rng.uniform(-0.3,0.3),cy+0.9+rng.uniform(-0.3,0.3)
                ax.add_patch(Circle((ex,ey),0.16,fc=BLUE,ec='none'))
                a=rng.uniform(0,2*np.pi); ax.annotate('',xy=(ex+0.45*np.cos(a),ey+0.45*np.sin(a)),xytext=(ex,ey),arrowprops=dict(arrowstyle='->',color=BLUE,lw=0.9))
            else:
                ax.add_patch(Circle((cx,cy),0.72,fc='none',ec=BLUE,lw=0.8,ls='--'))
                ax.add_patch(Circle((cx+0.72,cy),0.16,fc=BLUE,ec='none'))
ax.text(4.0,0.15,'outer electrons wander freely between ions',ha='center',color=BLUE,fontsize=10)
ax.text(12.0,0.15,'each electron stays tied to its own atom',ha='center',color=BLUE,fontsize=10)
save(f,O+'b1_conductor_insulator.png')

# 7.2 resistor colour code 4.7 kohm 5%
f,ax=fig(8,3.4); ax.axis('off'); ax.set_xlim(0,16); ax.set_ylim(0,6.8); ax.grid(False)
ax.plot([0.6,4],[4,4],color=GRAY,lw=3); ax.plot([12,15.4],[4,4],color=GRAY,lw=3)
ax.add_patch(FancyBboxPatch((4,3.0),8,2,boxstyle='round,pad=0.05,rounding_size=0.8',fc='#e9d8b4',ec=INK,lw=1.2))
bands=[(5.0,'#f1c40f','yellow','1st digit 4'),(6.2,'#7d3c98','violet','2nd digit 7'),(7.4,'#c0392b','red','multiplier ×100'),(10.6,'#c9a227','gold','tolerance ±5%')]
for x,c,n,lab in bands:
    ax.add_patch(Rectangle((x,3.0),0.6,2,fc=c,ec='none'))
    tx={5.0:2.2,6.2:5.6,7.4:9.2,10.6:13.2}[x]; ax.annotate(lab+'\n('+n+')',xy=(x+0.3,3.0),xytext=(tx,0.7),ha='center',fontsize=10,arrowprops=dict(arrowstyle='-',color=GRAY,lw=0.8))
ax.text(8,6.1,'4 7 × 100 = 4 700 Ω = 4.7 kΩ, ±5% (anything from 4.465 kΩ to 4.935 kΩ passes)',ha='center',fontsize=11)
save(f,O+'b1_color_code.png')

# 8.2 LED with series resistor
def led(d):
    V=d.add(elm.SourceV().up().label('5.0 V',loc='top'))
    d.add(elm.Line().right(1.5))
    d.add(elm.Resistor().right().label('R = 330 Ω',loc='top').label('drops 3.0 V',loc='bottom'))
    d.add(elm.LED().down().label('red LED\nV$_F$ ≈ 2.0 V',loc='bottom'))
    d.add(elm.Line().left().to(V.start))
    d.add(elm.Label().at((2.25,-0.8)).label('I = (5.0 V − 2.0 V) / 330 Ω ≈ 9 mA'))
    d.add(elm.Arrow().at((0.25,V.end[1]+0.25)).right(1.0).color('#2f6db0').label('I',loc='top',color='#2f6db0'))
schem(O+'b1_led.png',led,unit=3.0,fontsize=15,pad=1.0)

# 9.1 charge circling in B out of page
f,ax=fig(8,4.6); ax.set_aspect('equal'); ax.axis('off'); ax.grid(False); ax.set_xlim(-4.2,6.4); ax.set_ylim(-3.0,3.0)
for x in np.arange(-3.6,3.7,0.9):
    for y in np.arange(-2.6,2.7,0.9):
        ax.add_patch(Circle((x,y),0.13,fc='none',ec=GRAY,lw=0.8)); ax.plot(x,y,'.',color=GRAY,ms=2)
th=np.linspace(0,2*np.pi,200); R=1.9; ax.plot(R*np.cos(th),R*np.sin(th),color=BLUE,lw=1.4,ls='--')
ax.add_patch(Circle((0,R),0.25,fc=RED,ec=INK)); ax.text(0,R,'+',ha='center',va='center',color='white',weight='bold')
ax.annotate('',xy=(1.6,R),xytext=(0.28,R),arrowprops=dict(arrowstyle='-|>',color=INK,lw=1.8)); ax.text(1.65,R+0.25,'velocity v',fontsize=11)
ax.annotate('',xy=(0,R-1.3),xytext=(0,R-0.28),arrowprops=dict(arrowstyle='-|>',color=RED,lw=1.8)); ax.text(0.15,R-1.0,'force F = qv × B',color=RED,fontsize=11,bbox=dict(fc='white',ec='none',pad=1))
ax.annotate('',xy=(R*np.cos(-0.5),R*np.sin(-0.5)),xytext=(R*np.cos(-0.3),R*np.sin(-0.3)),arrowprops=dict(arrowstyle='-|>',color=BLUE,lw=1.5))
ax.text(4.2,1.6,'B points out of the page\n(dots: arrow tips coming\ntoward you)',fontsize=10.5,ha='left',va='top')
ax.text(4.2,-0.4,'Positive charge: clockwise.\nNegative charge: counter-\nclockwise.\nRadius r = mv / (qB)',fontsize=10.5,ha='left',va='top')
save(f,O+'b1_charge_in_B.png')

# 12.1 EM plane wave
f=plt.figure(figsize=(8,4.4),dpi=100); ax=f.add_subplot(projection='3d')
x=np.linspace(0,4*np.pi,300); ax.plot(x,np.zeros_like(x),0,color=INK,lw=1)
ax.plot(x,np.zeros_like(x),np.sin(x),color=RED,lw=2,label='electric field E (vertical)')
ax.plot(x,-np.sin(x),np.zeros_like(x),color=BLUE,lw=2,label='magnetic field B (horizontal, in phase with E)')
for xi in x[::12]:
    ax.plot([xi,xi],[0,0],[0,np.sin(xi)],color=RED,lw=0.6); ax.plot([xi,xi],[0,-np.sin(xi)],[0,0],color=BLUE,lw=0.6)
ax.quiver(4*np.pi,0,0,1.6,0,0,color=INK,arrow_length_ratio=0.3); ax.text(4*np.pi+0.6,0,-0.45,'travels at c',fontsize=10)
ax.set_xlim(0,4*np.pi+2.4); ax.set_ylim(-1.2,1.2); ax.set_zlim(-1.2,1.3); ax.set_axis_off(); ax.view_init(elev=20,azim=-60); ax.set_box_aspect((3,1,1),zoom=1.35); ax.legend(loc='upper left',fontsize=10)
ax.plot([np.pi/2,5*np.pi/2],[0,0],[1.15,1.15],color=INK,lw=1); ax.text(np.pi*1.2,0,1.3,'one wavelength λ = c / f',fontsize=10)
f.subplots_adjust(0,0,1,1); f.savefig(O+'b1_em_wave.png',dpi=100); plt.close(f)
from PIL import Image; Image.open(O+'b1_em_wave.png').convert('P',palette=Image.ADAPTIVE,colors=64).save(O+'b1_em_wave.png',optimize=True)

# 19.2 decibel ladder
f,ax=fig(8,3.6); ax.axis('off'); ax.grid(False); ax.set_xlim(-1.6,11.4); ax.set_ylim(-3,3.4)
pts=((-30,'1/1000','0.032'),(-20,'1/100','0.1'),(-10,'1/10','0.32'),(-6,'1/4','0.5'),(-3,'1/2','0.71'),(0,'1','1'),(3,'2','1.41'),(6,'4','2'),(10,'10','3.16'),(20,'100','10'),(30,'1000','31.6'))
ax.plot([0,10],[0,0],color=INK,lw=1.5)
for k,(db,pw,vt) in enumerate(pts):
    ax.plot([k,k],[-0.2,0.2],color=INK); ax.text(k,0.45,('%+d dB'%db) if db else '0 dB',ha='center',fontsize=9.5,weight='bold')
    ax.text(k,1.3,'×'+pw,ha='center',color=BLUE,fontsize=9.5); ax.text(k,-0.9,'×'+vt,ha='center',color=RED,fontsize=9.5)
ax.text(-1.5,1.3,'power',color=BLUE,ha='left',fontsize=10,va='center'); ax.text(-1.5,-0.9,'voltage',color=RED,ha='left',fontsize=10,va='center')
ax.text(5,2.6,'dB = 10 log₁₀(P₂/P₁) = 20 log₁₀(V₂/V₁)   (ticks not to scale)',ha='center',fontsize=11.5)
ax.text(5,-2.2,'Every +10 dB multiplies power by 10; +3 dB roughly doubles it; +6 dB doubles voltage.',ha='center',fontsize=10,color=GRAY)
save(f,O+'b1_db_ladder.png')

# 31.2 Thevenin source line
f,ax=fig(8,4.4); I=np.linspace(0,5,100); Voc,Rth=10.0,2.0
ax.plot(I,Voc-Rth*I,color=BLUE,lw=2,label='source: V = V$_{Th}$ − I·R$_{Th}$')
RL=2.0; ax.plot(I,RL*I,color=GRAY,lw=1.3,ls='--',label='2 kΩ load line: V = I·R$_L$')
ax.plot([2.5],[5],'o',color=RED); ax.annotate('operating point\n2.5 mA, 5 V\n(R$_L$ = R$_{Th}$: maximum power, 12.5 mW)',xy=(2.5,5),xytext=(3.0,7.2),fontsize=10,arrowprops=dict(arrowstyle='->',color=RED))
ax.text(0.08,10.15,'V$_{Th}$ = 10 V (open circuit)',fontsize=10); ax.text(4.15,0.4,'I$_N$ = 5 mA\n(short circuit)',fontsize=10)
ax.set_xlim(0,5.6); ax.set_ylim(0,11.5); ax.set_xlabel('load current I (mA)'); ax.set_ylabel('terminal voltage V (V)'); ax.legend(loc='upper right')
save(f,O+'b1_thevenin_line.png')

# 35.2 RL phase lag
f,ax=fig(8,4.0); t=np.linspace(0,2,400); ph=np.deg2rad(60)
ax.plot(t,np.sin(2*np.pi*t),color=BLUE,lw=2,label='source voltage v(t)')
ax.plot(t,0.6*np.sin(2*np.pi*t-ph),color=RED,lw=2,label='current i(t), lags by 60°')
ax.annotate('',xy=(0.25+60/360,0.6),xytext=(0.25,0.6),arrowprops=dict(arrowstyle='<->',color=INK)); ax.text(0.27,0.67,'60° = 1/6 period',fontsize=10)
ax.set_xlabel('time (periods)'); ax.set_ylabel('normalized amplitude'); ax.set_ylim(-1.25,1.35); ax.legend(loc='lower left',ncol=2)
ax.text(1.05,1.12,'series RL with ωL = √3·R: tan φ = ωL/R, φ = 60°',fontsize=10)
save(f,O+'b1_rl_phase.png')

# 36.2 instantaneous power
f,(a1,a2)=plt.subplots(1,2,figsize=(8,3.6),dpi=100,sharey=True); t=np.linspace(0,2,400)
for a,phd,tt in ((a1,0,'PF = 1 (resistor)'),(a2,60,'PF = 0.5 (current lags 60°)')):
    v=np.sin(2*np.pi*t); i=np.sin(2*np.pi*t-np.deg2rad(phd)); p=v*i
    a.plot(t,v,color=BLUE,lw=1.2,label='v'); a.plot(t,i,color=RED,lw=1.2,label='i'); a.fill_between(t,p,0,color=ORANGE,alpha=0.35,label='p = v·i')
    a.axhline(np.cos(np.deg2rad(phd))/2,color=INK,ls='--',lw=1); a.text(1.02,np.cos(np.deg2rad(phd))/2+0.06,'average P',fontsize=9)
    a.set_title(tt); a.set_xlabel('time (periods)')
a1.set_ylabel('normalized'); a1.legend(loc='lower left',fontsize=9,ncol=3)
a2.text(0.03,-0.95,'orange below zero: energy\nflowing back to the source',fontsize=9)
save(f,O+'b1_inst_power.png')
print('ok')

# 38.1 diode small-signal tangent
import numpy as np
VT=0.02585; Is=1e-14
V=np.linspace(0.55,0.72,400); I=Is*(np.exp(V/VT)-1)*1e3
VQ=VT*np.log(1e-3/Is+1); rd=VT/1e-3
f,ax=fig(8,4.6)
ax.plot(V,I,color=BLUE,lw=2,label='diode: I = I$_S$(e$^{V/V_T}$ − 1)')
Vt=np.linspace(VQ-0.03,VQ+0.03,10); ax.plot(Vt,1+(Vt-VQ)/rd*1e3,color=RED,lw=2,ls='--',label='tangent at the bias point: slope = 1/r$_d$')
ax.plot([VQ],[1],'o',color=INK); ax.annotate('bias point\nI$_D$ = 1 mA, V ≈ %.2f V'%VQ,xy=(VQ,1),xytext=(0.575,2.2),fontsize=10,arrowprops=dict(arrowstyle='->',color=GRAY))
ax.text(0.672,0.25,'r$_d$ = V$_T$ / I$_D$ ≈ 26 mV / 1 mA = 26 Ω',fontsize=10.5,color=RED)
ax.set_xlim(0.55,0.72); ax.set_ylim(0,4); ax.set_xlabel('diode voltage V (V)'); ax.set_ylabel('diode current I (mA)')
ax.legend(loc='upper left',fontsize=10)
save(f,O+'b1_diode_tangent.png'); print('ok')
