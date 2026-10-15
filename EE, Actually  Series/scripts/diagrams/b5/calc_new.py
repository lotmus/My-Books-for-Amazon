from math import *
c=2.998e8
def db(x): return 10*log10(x)
# 8.9 duplexer
fl=-174+4; dl=db(10**0.05-1); print('8.9 floor',fl,'allowed',fl+dl,'iso',-128-(fl+dl),'txrej',26-(-30))
fl=-174+5; dl=db(10**0.1-1); print('P8.10 allowed',fl+dl,'iso',-130-(fl+dl))
# FMCW
B=4e9;Tr=40e-6;S=B/Tr;print('dR',c/2/B,'Rmax',10e6*c/2/S,'fb6m',2*6*S/c)
lam=c/62e9;Tc=50e-6;N=128;print('lam',lam,'vmax',lam/4/Tc,'dv',lam/(2*N*Tc),'frame',N*Tc)
print('bytes/frame',4*128*512*4)
print('breath phase deg',degrees(4*pi*1e-3/lam))
# CFAR
print('thr1e-6',db(-log(1e-6)));T=16*(1e-6**(-1/16)-1);print('CA',T,db(T),db(T)-db(-log(1e-6)))
print('virt res deg',degrees(2/12),'theta',degrees(asin(60/180)))
lb=c/2.44e9;print('ble lam',lb,'d/l',0.04/lb,'aoa',degrees(asin((60/360)/(0.04/lb))))
print('mic',343/8000/2,'delay',0.04*3/343,0.04*3/343*48000)
print('tof 1mm ps',2e-3/c*1e12,'4m ns',8/c*1e9,'N',(200/6.67)**2)
print('fuse',1/sqrt(1/9+1/4),4/13,'alpha',0.5/(0.5+0.01))
# ch22
mf=2*32*40e6;fft=192*4/4e-6;eq=52*4/4e-6;print('ch22 mults',mf,fft,eq,mf+fft+eq,(mf+fft+eq)/2e8,'acs',64*54e6)
print('energy',(mf+fft+eq)*3e-12,(mf+fft+eq)*70e-12)
print('B bits',(30+10-1.76+9)/6.02)
K=1
for i in range(40): K*=sqrt(1+2**(-2*i))
print('cordic K',K,1/K,'atan2^-15',atan(2**-15),'lat ns',16/245.76e6*1e9)
print('fir slices',32*245.76e6/491.52e6)
print('breakeven',3e6/72)
print('uxga raw',1600*1200*2*15*8/1e6,'1080p',1920*1080*1.5*30*8/1e6)
# ch24
print('C band THz',196.1-191.3,48*400)
lam=1550e-9;D=17e-6
for Bd in [10e9,25e9,53.125e9,59.84375e9]:
    dl=lam**2*Bd/c; print(Bd/1e9,'dlam nm',dl*1e9,'L(1sym) km',(1/Bd)/(D*dl)/1e3)
dl=lam**2*59.84375e9/c;dt=D*80e3*dl;print('400ZR 80km ps',dt*1e12,'symbols',dt*59.84375e9)
print('link',0-3.5-1-0.4, 'margin',-14-(-4.9))
print('pam4 opt',db(3),'line',4*53.125*2,'zr',59.84375*8)
print('nec',9+4.5+16*1.125+16*2.25,32/67.5e-3,562.5e-6*38e3)
# ch25
Ts=2**11/250e3;pl=50;ps=8+max(ceil((8*pl-4*11+28+16)/(4*11))*5,0);toa=(12.25+ps)*Ts;print('LF Tsym',Ts,'sym',ps,'toa',toa)
sens=-174+db(250e3)+6-17.5;print('sens',sens,'budget',22-sens)
print('fspl d km',10**((22-sens-20*log10(915)-32.45)/20))
print('horizon',4.12*2*sqrt(500),'fresnel',17.32*sqrt(50/(4*0.915)))
G=30*4*toa/900;print('util',G,'succ',exp(-2*G))
print('rssi d',10**(11/22),10**(4/22),10**(11/22)/10**(4/22),10**(11/22)*10**(4/22))
print('rssi err',10**(4/25))
print('wifi',0.18/600*1e3,'mA', 3000/(0.18/600*1e3)/8760)
def toaf(sf,bw,pl,de=0):
    Ts=2**sf/bw; ps=8+max(ceil((8*pl-4*sf+28+16)/(4*(sf-2*de)))*5,0); return (12.25+ps)*Ts
print('sf7 250 20B',toaf(7,250e3,20))
print('can',111/1e6)
