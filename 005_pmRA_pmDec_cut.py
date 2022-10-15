from numpy import *
from matplotlib.pyplot import *
import pandas as pd

df = pd.read_csv('RA_Dec_plx_2.csv')
plx_list=[float(a) for a in (df['plx'].tolist())]
RA_list=[float(a) for a in (df['RA'].tolist())]
Dec_list=[float(a) for a in (df['Dec'].tolist())]
dist_list=[float(a) for a in (df['dist'].tolist())]
pmRA_list=[float(a) for a in df['pmRA'].tolist()]
pmDE_list=[float(a) for a in df['pmDE'].tolist()]
Gmag_list=[float(a) for a in df['Gmag'].tolist()]
BPmag_list=[float(a) for a in df['BPMag'].tolist()]
RPmag_list=[float(a) for a in df['RPmag'].tolist()]


RA_updated=[]
Dec_updated=[]
plx_updated=[]
pmRA_updated=[]
pmDE_updated=[]
Gmag_updated=[]
BPmag_updated=[]
RPmag_updated=[]
dist_updated=[]
for (i,l,m,n,o,p,j,k,r) in zip(plx_list, pmRA_list, pmDE_list, Gmag_list, BPmag_list, RPmag_list, RA_list, Dec_list,dist_list):
	if (l<-4) or (l>0) or (m<-4) or (m>0):
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
		dist_updated.append(float(r))

dict = {'RA': RA_updated, 'Dec': Dec_updated, 'plx': plx_updated, 'dist': dist_updated, 'pmRA': pmRA_updated, 'pmDE': pmDE_updated, 'Gmag': Gmag_updated, 'BPMag': BPmag_updated, 'RPmag': RPmag_updated}  
       
df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('RA_Dec_plx_3.csv')
