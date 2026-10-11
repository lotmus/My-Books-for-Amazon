import numpy as np
def cr(pts,n=24):
    pts=np.array(pts,float); out=[]
    P=np.vstack([pts[0],pts,pts[-1]])
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        for t in np.linspace(0,1,n,endpoint=False):
            t2,t3=t*t,t*t*t
            out.append(0.5*((2*p1)+(-p0+p2)*t+(2*p0-5*p1+4*p2-p3)*t2+(-p0+3*p1-3*p2+p3)*t3))
    out.append(pts[-1]); return np.array(out)
# segments split at sharp corners (fin tips, fluke tips, notch, snout)
SEG=[
 [(1.0,0.0),(0.95,0.018),(0.915,0.03),(0.885,0.065),(0.84,0.098),(0.76,0.13),(0.62,0.152),(0.55,0.15)],   # snout->melon->back to fin front
 [(0.55,0.15),(0.51,0.215),(0.455,0.275),(0.40,0.305)],      # fin leading edge
 [(0.40,0.305),(0.425,0.25),(0.425,0.18),(0.395,0.13)],      # fin trailing edge
 [(0.395,0.13),(0.30,0.10),(0.18,0.06),(0.09,0.025)],      # back to peduncle
 [(0.09,0.025),(0.04,0.06),(-0.02,0.105),(-0.065,0.12)],   # fluke upper lead
 [(-0.065,0.12),(-0.04,0.07),(-0.015,0.02),(0.0,0.0)],     # fluke upper trail to notch
 [(0.0,0.0),(-0.015,-0.02),(-0.04,-0.07),(-0.065,-0.12)],
 [(-0.065,-0.12),(-0.02,-0.105),(0.04,-0.06),(0.09,-0.025)],
 [(0.09,-0.025),(0.20,-0.05),(0.35,-0.07),(0.60,-0.075)],  # belly to pectoral
 [(0.60,-0.075),(0.585,-0.12),(0.56,-0.17)],               # pectoral lead
 [(0.56,-0.17),(0.62,-0.13),(0.66,-0.085)],                # pectoral trail
 [(0.66,-0.085),(0.78,-0.07),(0.88,-0.04),(0.95,-0.015),(1.0,0.0)],
]
def outline():
    pts=[cr(s)[:-1] for s in SEG]; return np.vstack(pts)
def arched(bend=0.55):
    o=outline(); x,y=o[:,0]-0.5,o[:,1]
    R=1/bend; th=x/R
    X=(R+y)*np.sin(th); Y=(R+y)*np.cos(th)-R
    return np.c_[X,Y]
if __name__=='__main__':
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    fig,ax=plt.subplots(1,2,figsize=(12,4))
    for a,o in zip(ax,[outline(),arched()]): a.fill(o[:,0],o[:,1],'k'); a.set_aspect('equal'); a.axis('off')
    plt.savefig('dolphin_test.png',dpi=80)
