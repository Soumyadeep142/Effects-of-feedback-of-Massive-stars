from numpy import *
from matplotlib.pyplot import *
import pandas as pd
#RA, Dec=loadtxt('RA_Dec_Plx.txt', unpack='true', usecols=(0,1), skiprows=1)
#plx=loadtxt('RA_Dec_Plx.txt', unpack='true', usecols=(2), skiprows=1, dtype=str)
df = pd.read_csv('RA_Dec_plx.csv')
RA=(df['RA'].tolist())
Dec=(df['Dec'].tolist())
plx_list=(df['plx'].tolist())
pmRA_list=df['pmRA'].tolist()
pmDE_list=df['pmDE'].tolist()
Gmag_list=df['Gmag'].tolist()
BPmag_list=df['BPMag'].tolist()
RPmag_list=df['RPmag'].tolist()



RA_updated=[]
Dec_updated=[]
plx_updated=[]
pmRA_updated=[]
pmDE_updated=[]
Gmag_updated=[]
BPmag_updated=[]
RPmag_updated=[]

i_range=[plx_list, pmRA_list, pmDE_list, Gmag_list, BPmag_list, RPmag_list]
k_up_range=[plx_updated, pmRA_updated, pmDE_updated, Gmag_updated, BPmag_updated, RPmag_updated]
csv_header=['plx', 'pmRA', 'pmDE', 'Gmag', 'BPmag', 'RPmag']
l=0
A=(plx_list[4])
B=pmRA_list[4]
C=pmDE_list[4]
E=BPmag_list[4]
F=RPmag_list[4]

for (i,l,m,n,o,p,j,k) in zip(plx_list, pmRA_list, pmDE_list, Gmag_list, BPmag_list, RPmag_list, RA, Dec):
	if (i==A) or (l==B) or (m==C) or (o==E) or (o==F):
		pass
	else:
		plx_updated.append(float(i))
		RA_updated.append(float(j))
		Dec_updated.append(float(k))
		pmRA_updated.append(float(l))
		pmDE_updated.append(float(m))
		Gmag_updated.append(float(n))
		BPmag_updated.append(float(o))
		RPmag_updated.append(float(p))
	
dist=[1000/a for a in plx_updated]
dict = {'RA': RA_updated, 'Dec': Dec_updated, 'plx': plx_updated, 'dist': dist, 'pmRA': pmRA_updated, 'pmDE': pmDE_updated, 'Gmag': Gmag_updated, 'BPMag': BPmag_updated, 'RPmag': RPmag_updated}  
       
df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('RA_Dec_plx_2.csv')

