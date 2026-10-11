# Rev9 diagrams: surveyors (book sign convention, label on the distance line),
# embedding (label clear of the rings), Kruskal (labels clear of curves), wormhole slice (replaces the AI flask).
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
O='/workspace/grav9/img/'
BLUE='#1f4e79'; ORANGE='#d9822b'; GREY='#666666'; RED='#c0392b'; GREEN='#2e7d32'
def save(fig,name):
    fig.savefig(O+name,dpi=200,bbox_inches='tight',facecolor='white',pad_inches=0.15); plt.close(fig)

# 1 surveyors
fig,(a1,a2)=plt.subplots(1,2,figsize=(10,4.8))
for a in (a1,a2): a.set_aspect('equal'); a.axis('off')
a1.set_xlim(-1.2,6.2); a1.set_ylim(-2.6,6.0)
th=np.radians(20.6)
def ax_pair(a,ang,col,l1,l2,L=5.2):
    c,s=np.cos(ang),np.sin(ang)
    a.annotate('',xy=(L*c,L*s),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=col,lw=1.6))
    a.annotate('',xy=(-L*s,L*c),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=col,lw=1.6))
    a.text(L*c+0.05,L*s-0.35,l1,color=col,fontsize=9.5); a.text(-L*s-0.2,L*c+0.15,l2,color=col,fontsize=9.5,ha='center')
ax_pair(a1,0,BLUE,'east (day)','north (day)')
ax_pair(a1,-th,ORANGE,'east (night)','north (night)')
a1.plot([0,3],[0,4],color='k',lw=2.2); a1.plot(3,4,'ko')
a1.text(3.1,4.15,'corner stake',fontsize=9.5)
a1.plot([3,3],[0,4],color=BLUE,ls=':',lw=1.2); a1.text(3.12,1.6,'day: 3 east, 4 north',color=BLUE,fontsize=9)
a1.text(-1.1,-2.5,'night: 1.4 east, 4.8 north',color=ORANGE,fontsize=9)
a1.text(1.75,1.85,'5 km',fontsize=11,fontweight='bold',rotation=53,ha='center',va='center',
        bbox=dict(fc='white',ec='none',pad=0.5))
a1.set_title('Two surveyors: different parts, same distance\n3² + 4² = 1.4² + 4.8² = 25',fontsize=10.5)
a2.set_xlim(-1.2,6.2); a2.set_ylim(-2.6,6.0)
a2.annotate('',xy=(5.2,0),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=BLUE,lw=1.6)); a2.text(4.6,-0.45,'space (ground)',color=BLUE,fontsize=9.5)
a2.annotate('',xy=(0,5.6),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=BLUE,lw=1.6)); a2.text(-0.15,5.75,'time (ground)',color=BLUE,fontsize=9.5,ha='center')
v=0.6
a2.annotate('',xy=(5.4*v/np.hypot(1,v),5.4/np.hypot(1,v)),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=ORANGE,lw=1.6))
a2.text(2.15,3.3,'time (ship)',color=ORANGE,fontsize=9.5)
a2.annotate('',xy=(5.4/np.hypot(1,v),5.4*v/np.hypot(1,v)),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=ORANGE,lw=1.6))
a2.text(4.7,2.55,'space (ship)',color=ORANGE,fontsize=9.5)
a2.plot([0,5.4],[0,5.4],color=GREY,ls='--',lw=1); a2.text(5.0,5.45,'light',color=GREY,fontsize=9)
a2.plot([0,3],[0,5],color='k',lw=2.2); a2.plot(3,5,'ko'); a2.text(3.15,5.05,'event',fontsize=9.5)
a2.text(-1.1,-2.3,'ground: 5 s of time, 3 light-s of space\nship (0.6c): 4 s of time, 0 of space',fontsize=9)
a2.set_title('Two observers: different parts, same interval\n−5² + 3² = −4² + 0² = −16',fontsize=10.5)
save(fig,'diag_surveyors.png')

# 2 embedding
fig=plt.figure(figsize=(7,5.0)); ax=fig.add_subplot(111,projection='3d')
rs=1.0; r=np.linspace(rs,6,60); ph=np.linspace(0,2*np.pi,72)
R,P=np.meshgrid(r,ph); Z=2*np.sqrt(rs*(R-rs))
ax.plot_wireframe(R*np.cos(P),R*np.sin(P),Z,rstride=3,cstride=3,color=BLUE,lw=0.5)
t=np.linspace(0,2*np.pi,200)
ax.plot(rs*np.cos(t),rs*np.sin(t),0*t,color=RED,lw=2.5)
for rr in (2.0,3.0):
    ax.plot(rr*np.cos(t),rr*np.sin(t),2*np.sqrt(rs*(rr-rs))+0*t,color=ORANGE,lw=2)
ax.text(0,0,-0.9,'horizon (r = rₛ)',color=RED,fontsize=10,ha='center')
ax.set_axis_off(); ax.view_init(elev=24,azim=-60); ax.set_box_aspect((1,1,0.6),zoom=1.35)
fig.text(0.80,0.42,'orange rings:\nshells at\nr = 2rₛ and 3rₛ',color=ORANGE,fontsize=10,ha='left')
ax.set_title('A slice of space around a black hole, drawn as a surface.\nDistances along the surface are what rulers on the shells measure.',fontsize=10)
save(fig,'diag_embedding.png')

# 3 Kruskal
fig,ax=plt.subplots(figsize=(7.2,7.4)); ax.set_xlim(-3.0,3.0); ax.set_ylim(-3.75,3.75); ax.set_aspect('equal'); ax.axis('off')
L=2.9; X=np.linspace(-L,L,600); Ts=np.sqrt(1+X**2); top=np.sqrt(1+L**2)
ax.fill_between(X,Ts,top,color='#eeeeee'); ax.fill_between(X,-top,-Ts,color='#eeeeee')
ax.plot(X,Ts,color='k',lw=2.5); ax.plot(X,-Ts,color='k',lw=2.5)
ax.plot([-L,L],[-L,L],color=RED,lw=2); ax.plot([-L,L],[L,-L],color=RED,lw=2)
ax.text(0,3.3,'black curve at top: the singularity, r = 0,\na moment ahead, not a place',ha='center',fontsize=9.5)
ax.text(0,-3.55,'black curve at bottom: a past singularity (white hole),\nin the eternal mathematical solution only',ha='center',fontsize=8.5,color=GREY)
ax.text(2.2,2.75,'horizon',color=RED,fontsize=9.5,ha='right',va='center',bbox=dict(fc='white',ec='none',pad=1))
for rr in (1.2,1.5,1.8):
    k=(rr-1)*np.exp(rr); Tl=np.linspace(-2.2,2.2,200); Xl=np.sqrt(k+Tl**2); mm=Xl<=L
    ax.plot(Xl[mm],Tl[mm],color=BLUE,lw=1,ls='--'); ax.plot(-Xl[mm],Tl[mm],color='#9db7d3',lw=1,ls='--')
ax.annotate('shells held in place\n(r = 1.2, 1.5, 1.8 rₛ)',xy=(2.45,1.2),xytext=(1.2,2.05),color=BLUE,fontsize=8.5,
            arrowprops=dict(arrowstyle='->',color=BLUE,lw=0.8),bbox=dict(fc='white',ec='none',pad=1))
s=np.linspace(0,1,100); xa=2.0-0.75*s-0.55*s**2; ta=-0.6+1.9*s+0.25*s**2
m=ta<np.sqrt(1+xa**2); ax.plot(xa[m],ta[m],color=ORANGE,lw=2.5)
ax.annotate('falling astronaut',xy=(1.95,-0.5),xytext=(1.45,-1.9),color=ORANGE,fontsize=9,
            arrowprops=dict(arrowstyle='->',color=ORANGE,lw=0.8),bbox=dict(fc='white',ec='none',pad=1))
def cone(x,y,h=0.2):
    ax.add_patch(Polygon([[x,y],[x-h,y+h],[x+h,y+h]],closed=True,fc=ORANGE,alpha=0.3,ec=ORANGE))
for (x,y) in ((2.7,-1.2),(-0.3,1.1),(-2.2,-1.1)): cone(x,y)
ax.text(2.25,-0.15,'I  our\noutside',fontsize=9.5,fontweight='bold')
ax.text(-0.75,0.45,'II  inside\nthe hole',fontsize=9.5,fontweight='bold')
ax.text(-0.15,-0.85,'III',fontsize=11,fontweight='bold',color=GREY)
ax.text(-2.95,-0.15,'IV  a second\noutside (eternal\nsolution only)',fontsize=8.5,color=GREY)
fig.text(0.5,0.035,'Light runs at 45° everywhere on this map. Time goes up. The small orange cones show where light can go.',ha='center',fontsize=9)
save(fig,'diag_kruskal.png')

# 4 wormhole slice (replaces the AI flask painting)
fig=plt.figure(figsize=(7.0,5.2)); ax=fig.add_axes([0.0,0.0,1.0,0.86],projection='3d')
b=1.0; r=np.linspace(b,5.5,70); ph=np.linspace(0,2*np.pi,72); R,P=np.meshgrid(r,ph)
Z=b*np.arccosh(R/b)
for sgn,col in ((1,BLUE),(-1,'#5b7fa6')):
    ax.plot_wireframe(R*np.cos(P),R*np.sin(P),sgn*Z,rstride=4,cstride=4,color=col,lw=0.5)
t=np.linspace(0,2*np.pi,200); ax.plot(b*np.cos(t),b*np.sin(t),0*t,color=RED,lw=3)
rr=np.linspace(5.0,b,60); ax.plot(rr*0,-rr,b*np.arccosh(rr/b),color=GREEN,lw=3.2)
ax.plot(rr*0,-rr[::-1],-b*np.arccosh(rr[::-1]/b),color=GREEN,lw=3.2)
ax.scatter([0],[-5.0],[b*np.arccosh(5.0)],color='k',s=30); ax.scatter([0],[-5.0],[-b*np.arccosh(5.0)],color='k',s=30)
ax.text(0.3,-5.6,b*np.arccosh(5.0)+0.35,'A',fontsize=14,fontweight='bold')
ax.text(0.3,-5.6,-b*np.arccosh(5.0)-0.8,'B',fontsize=14,fontweight='bold')
ax.set_axis_off(); ax.view_init(elev=12,azim=-35); ax.set_box_aspect((1,1,0.8),zoom=1.55)
fig.text(0.70,0.45,'throat',color=RED,fontsize=14)
fig.text(0.02,0.47,'green: the short\nroad from A to B,\nthrough the throat',color=GREEN,fontsize=12.5)
fig.text(0.5,0.93,'A slice through a wormhole at one moment:\ntwo regions joined by a throat',fontsize=13,ha='center',va='center')
save(fig,'diag_wormhole.png')
print('ok')
