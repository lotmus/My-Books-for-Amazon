import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
O='/workspace/grav/img/'
BLUE='#1f4e79'; ORANGE='#d9822b'; GREY='#666666'; RED='#c0392b'; GREEN='#2e7d32'
def save(fig,name):
    fig.savefig(O+name,dpi=300,bbox_inches='tight',facecolor='white'); plt.close(fig)

# 1 surveyors: two maps, two spacetime frames
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
a1.plot([3,3],[0,4],color=BLUE,ls=':',lw=1.2); a1.text(3.05,1.6,'day: 3 east, 4 north',color=BLUE,fontsize=9)
a1.text(-1.1,-2.5,'night: 1.4 east, 4.8 north',color=ORANGE,fontsize=9)
a1.text(0.9,2.6,'5',fontsize=12,fontweight='bold')
a1.set_title('Two surveyors: different parts, same distance\n3² + 4² = 1.4² + 4.8² = 25',fontsize=10.5)
# spacetime
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
a2.set_title('Two observers: different parts, same interval\n5² − 3² = 4² − 0² = 16',fontsize=10.5)
save(fig,'diag_surveyors.png')

# 2 one-form as a stack of surfaces
fig,ax=plt.subplots(figsize=(7,4.4)); ax.set_xlim(-0.5,10); ax.set_ylim(-0.6,6.4); ax.axis('off')
for k in range(7):
    y=0.4+0.85*k
    ax.add_patch(Polygon([[1,y],[7.5,y],[8.7,y+0.55],[2.2,y+0.55]],closed=True,fc='#dce7f3',ec=BLUE,lw=1,alpha=0.9))
    ax.text(8.9,y+0.2,'+%d' % k if k else '0',color=BLUE,fontsize=9)
ax.text(9.4,6.1,'surfaces of\nequal clock rate',color=BLUE,fontsize=9,ha='center')
ax.annotate('',xy=(4.2,3.15),xytext=(4.2,0.6),arrowprops=dict(arrowstyle='-|>',color=RED,lw=2.4))
ax.text(3.95,1.85,'lift A:\ncrosses 3',color=RED,fontsize=9.5,ha='right')
ax.annotate('',xy=(6.6,1.6),xytext=(5.6,0.75),arrowprops=dict(arrowstyle='-|>',color=GREEN,lw=2.4))
ax.text(6.7,1.0,'slanted move B:\ncrosses 1',color=GREEN,fontsize=9.5)
ax.text(0.0,5.9,'Each surface = one more part in 10¹⁶ of clock rate.\nSpacing on Earth ≈ 0.92 m (c² × 10⁻¹⁶ / g).',fontsize=9.5)
ax.text(5.0,-0.5,'The arrow is the move. The stack is the gradient. The count of surfaces crossed is the change.',fontsize=9.3,ha='center',color=GREY)
save(fig,'diag_oneform.png')

# 3 Flamm embedding of the Schwarzschild space slice
from mpl_toolkits.mplot3d import Axes3D  # noqa
fig=plt.figure(figsize=(7,4.8)); ax=fig.add_subplot(111,projection='3d')
rs=1.0; r=np.linspace(rs,6,60); ph=np.linspace(0,2*np.pi,72)
R,P=np.meshgrid(r,ph); Z=2*np.sqrt(rs*(R-rs))
ax.plot_wireframe(R*np.cos(P),R*np.sin(P),Z,rstride=3,cstride=3,color=BLUE,lw=0.5)
t=np.linspace(0,2*np.pi,200)
ax.plot(rs*np.cos(t),rs*np.sin(t),0*t,color=RED,lw=2.5)
for rr,col in ((2.0,ORANGE),(3.0,ORANGE)):
    ax.plot(rr*np.cos(t),rr*np.sin(t),2*np.sqrt(rs*(rr-rs))+0*t,color=col,lw=2)
ax.text(0,0,-0.7,'horizon (r = rₛ)',color=RED,fontsize=9.5,ha='center')
ax.text(4.5,-4.5,3.6,'shells at r = 2rₛ and 3rₛ',color=ORANGE,fontsize=9.5)
ax.set_axis_off(); ax.view_init(elev=24,azim=-60); ax.set_box_aspect((1,1,0.6),zoom=1.45)
ax.set_title('A slice of space around a black hole, drawn as a surface.\nDistances along the surface are what rulers on the shells measure.',fontsize=10)
save(fig,'diag_embedding.png')

# 4 Kruskal–Szekeres diagram
fig,ax=plt.subplots(figsize=(6.6,6.2)); ax.set_xlim(-3,3); ax.set_ylim(-2.35,2.35); ax.set_aspect('equal'); ax.axis('off')
X=np.linspace(-3,3,600)
Ts=np.sqrt(1+X**2)
ax.fill_between(X,Ts,2.4,color='#eeeeee'); ax.fill_between(X,-2.4,-Ts,color='#eeeeee')
ax.plot(X,Ts,color='k',lw=2.5); ax.plot(X,-Ts,color='k',lw=2.5,ls='-')
ax.text(0,2.05,'singularity, r = 0: a moment ahead, not a place',ha='center',fontsize=9.5)
ax.text(0,-2.1,'past singularity (white hole), in the eternal solution only',ha='center',fontsize=8.5,color=GREY)
ax.plot([-3,3],[-3,3],color=RED,lw=2); ax.plot([-3,3],[3,-3],color=RED,lw=2)
ax.text(1.95,1.62,'horizon',color=RED,fontsize=9.5,rotation=45)
for rr in (1.2,1.5,1.8):
    k=(rr-1)*np.exp(rr); Tl=np.linspace(-1.9,1.9,200); Xl=np.sqrt(k+Tl**2)
    ax.plot(Xl,Tl,color=BLUE,lw=1,ls='--'); ax.plot(-Xl,Tl,color='#9db7d3',lw=1,ls='--')
ax.text(2.0,-0.05,'r = 1.2, 1.5, 1.8 rₛ\n(shells held in place)',color=BLUE,fontsize=8.5)
# falling astronaut
s=np.linspace(0,1,100); xa=2.0-0.75*s-0.55*s**2; ta=-0.6+1.9*s+0.25*s**2
m=ta<np.sqrt(1+xa**2); ax.plot(xa[m],ta[m],color=ORANGE,lw=2.5)
ax.text(2.1,-0.95,'falling\nastronaut',color=ORANGE,fontsize=9)
# light cones
def cone(x,y,h=0.22):
    ax.add_patch(Polygon([[x,y],[x-h,y+h],[x+h,y+h]],closed=True,fc=ORANGE,alpha=0.25,ec=ORANGE))
for (x,y) in ((2.6,-1.2),(-0.3,1.05),(-1.9,-0.6)): cone(x,y)
ax.text(1.6,0.6,'I  our outside',fontsize=10,fontweight='bold')
ax.text(-0.85,0.6,'II  inside the hole',fontsize=10,fontweight='bold')
ax.text(-0.75,-0.95,'III',fontsize=10,fontweight='bold',color=GREY)
ax.text(-2.75,0.25,'IV  a second outside\n(eternal solution only)',fontsize=8.5,color=GREY)
ax.text(0,-2.33,'Light runs at 45° everywhere on this map. Time goes up.',ha='center',fontsize=9)
save(fig,'diag_kruskal.png')
print('ok')
