from numpy import *
from matplotlib.pyplot import *

L_bol=3*10**4*4*10**33
c=3*10**10

M_w=1.9*10**20
V_w=2900*10**5
pc=3*10**18

m2=0.678
mh=9.1*10**-27
c2=11*10**5
sly=10**48
b2=2.6*10**-13
Ds=[x*pc for x in arange(0.000001,20,0.001)]
P_wind=[]
P_rad=[]
P_h2=[]
for i in Ds:
	P_wind.append(M_w*V_w/(4*pi*i**2))
	P_rad.append(L_bol/(4*pi*c*i**2))
	P_h2.append(m2*mh*c2**2*sqrt(sly/(4*pi*b2*i**3)))
plot(Ds, log10(P_wind))
plot(Ds, log10(P_rad))
plot(Ds, log10(P_h2))
show()

