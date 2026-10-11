import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
O='/workspace/grav/img/'
BLUE='#1f4e79'; ORANGE='#d9822b'; GREY='#666666'; RED='#c0392b'; GREEN='#2e7d32'
def save(fig,name):
    fig.savefig(O+name,dpi=300,bbox_inches='tight',facecolor='white'); plt.close(fig)

# 1 ants: flat table vs curved skin
fig=plt.figure(figsize=(9,4.4))
a=fig.add_subplot(1,2,1); a.set_xlim(0,6); a.set_ylim(0,6); a.set_aspect('equal'); a.axis('off')
a.add_patch(plt.Rectangle((0.3,0.3),5.4,5.4,fc='#f3efe6',ec=GREY))
for x,c in ((2.4,RED),(3.6,BLUE)):
    a.annotate('',xy=(x,5.4),xytext=(x,0.7),arrowprops=dict(arrowstyle='-|>',color=c,lw=2.4))
    a.plot(x,0.7,'o',color=c,ms=7)
a.text(3,0.05,'start: side by side, parallel',ha='center',fontsize=9.5)
a.text(3,5.75,'still the same distance apart',ha='center',fontsize=9.5)
a.set_title('On a flat table',fontsize=11)
b=fig.add_subplot(1,2,2,projection='3d')
u=np.linspace(0,2*np.pi,60); v=np.linspace(0,np.pi,30)
X=np.outer(np.cos(u),np.sin(v)); Y=np.outer(np.sin(u),np.sin(v)); Z=np.outer(np.ones_like(u),np.cos(v))
b.plot_surface(X,Y,Z,color='#f3d9cf',alpha=0.15,linewidth=0,shade=True)
b.plot_wireframe(X,Y,Z,rstride=5,cstride=5,color='#c9a99c',lw=0.4)
t=np.linspace(0,2*np.pi,200); b.plot(np.cos(t),np.sin(t),0*t,color=GREY,lw=1,ls='--')
th=np.linspace(np.pi/2,0.02,100)
for ph,c in ((-0.35,RED),(0.35,BLUE)):
    b.plot(np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th),color=c,lw=3.4)
    b.scatter([np.cos(ph)],[np.sin(ph)],[0],color=c,s=30)
b.scatter([0],[0],[1],color='k',s=25)
b.text(0,0,1.18,'they meet',ha='center',fontsize=9.5)
b.text(1.05,0,-0.35,'start: parallel',fontsize=9.5)
b.view_init(elev=18,azim=8); b.set_box_aspect((1,1,1),zoom=1.25); b.set_axis_off()
b.set_title('On a curved skin',fontsize=11)
fig.text(0.5,0.02,'Each path is as straight as the surface allows. No force acts. The surface makes the paths meet.',ha='center',fontsize=9.5,color=GREY)
save(fig,'diag_ants.png')

# 2 the funnel and its limit: sheet picture vs clock-rate curve
fig=plt.figure(figsize=(10,4.3))
a=fig.add_subplot(1,2,1,projection='3d')
x=np.linspace(-6,6,61); y=np.linspace(-4,4,41); Xg,Yg=np.meshgrid(x,y)
def well(x0,y0,d,w): return -d/np.sqrt(((Xg-x0)**2+(Yg-y0)**2)/w**2+1)
Zs=well(-2,0,2.2,0.9)+well(3.2,0,0.6,0.5)
a.plot_wireframe(Xg,Yg,Zs,rstride=2,cstride=2,color=BLUE,lw=0.45)
a.scatter([-2],[0],[-2.05],color='#3b7dd8',s=260,depthshade=False); a.scatter([3.2],[0],[-0.55],color='#aaaaaa',s=70,depthshade=False)
a.text(-2,0,0.45,'Earth',ha='center',fontsize=9.5); a.text(3.2,0,0.4,'Moon',ha='center',fontsize=9.5)
a.view_init(elev=28,azim=-62); a.set_axis_off(); a.set_box_aspect((1.5,1,0.45),zoom=1.3)
a.set_title('The familiar sheet: a dent in space only.\nIt needs a hidden "downhill" to work.',fontsize=10)
b=fig.add_subplot(1,2,2)
GMc2=4.435e-3; R=6.371e6
h=np.linspace(0,36000e3,400); rate=(GMc2/R-GMc2/(R+h))*1e9
b.plot(h/1e3,rate,color=ORANGE,lw=2.6)
hg=26571e3-R; rg=(GMc2/R-GMc2/26571e3)*1e9
b.plot([hg/1e3],[rg],'o',color=RED); b.annotate('GPS orbit, 20,200 km:\n+0.53 parts per billion\n= +45.7 µs a day',xy=(hg/1e3,rg),xytext=(9000,0.22),fontsize=9,arrowprops=dict(arrowstyle='->',color=RED))
b.set_xlabel('height above the ground (km)'); b.set_ylabel('how much faster a clock runs\nthan one on the ground (parts per billion)',fontsize=9.5)
b.set_xlim(0,36000); b.set_ylim(0,0.65); b.grid(alpha=0.3)
b.set_title('What does most of the work for a falling apple:\nclocks run faster higher up',fontsize=10)
save(fig,'diag_funnel_time.png')
print('ok')
