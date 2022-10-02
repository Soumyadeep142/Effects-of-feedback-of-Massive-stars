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
	if (i==A) or (l==B) or (m==C) or (o==E) or (p==F):
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

for count in range(3):
	mean_plx=mean(plx_updated)
	mean_pmRA=mean(pmRA_updated)
	mean_pmDE=mean(pmDE_updated)
	mean_Gmag=mean(Gmag_updated)
	mean_BPmag=mean(BPmag_updated)
	mean_RPmag=mean(RPmag_updated)
	mean_dist=mean(dist)
	
	sd_plx=std(plx_updated)
	sd_pmRA=std(pmRA_updated)
	sd_pmDE=std(pmDE_updated)
	sd_Gmag=std(Gmag_updated)
	sd_BPmag=std(BPmag_updated)
	sd_RPmag=std(RPmag_updated)
	sd_dist=std(dist)
	
	RA_updated_new=[]
	Dec_updated_new=[]
	plx_updated_new=[]
	pmRA_updated_new=[]
	pmDE_updated_new=[]
	Gmag_updated_new=[]
	BPmag_updated_new=[]
	RPmag_updated_new=[]
	dist_new=[]
	
	for (i,l,m,n,o,p,j,k,q) in zip(plx_updated, pmRA_updated, pmDE_updated, Gmag_updated, BPmag_updated, RPmag_updated, RA_updated, Dec_updated, dist):
		if (i<(mean_plx-3*sd_plx)) or (i>(mean_plx+3*sd_plx)) or (l<(mean_pmRA-3*sd_pmRA)) or (l>(mean_pmRA+3*sd_pmRA)) or (m<(mean_pmDE-3*sd_pmDE)) or (m>(mean_pmDE+3*sd_pmDE)) or (n<(mean_Gmag-3*sd_Gmag)) or (n>(mean_Gmag+3*sd_Gmag)) or (o<(mean_BPmag-3*sd_BPmag)) or (o>(mean_BPmag+3*sd_BPmag)) or (p<(mean_RPmag-3*sd_RPmag)) or (p>(mean_RPmag+3*sd_RPmag)) or (q<(mean_dist-3*sd_dist)) or (q>(mean_dist+3*sd_dist)):
			pass
		else:
			plx_updated_new.append(float(i))
			RA_updated_new.append(float(j))
			Dec_updated_new.append(float(k))
			pmRA_updated_new.append(float(l))
			pmDE_updated_new.append(float(m))
			Gmag_updated_new.append(float(n))
			BPmag_updated_new.append(float(o))
			RPmag_updated_new.append(float(p))
			dist_new.append(float(q))
		
	RA_updated=RA_updated_new
	Dec_updated=Dec_updated_new
	plx_updated=plx_updated_new
	pmRA_updated=pmRA_updated_new
	pmDE_updated=pmDE_updated_new
	Gmag_updated=Gmag_updated_new
	BPmag_updated=BPmag_updated_new
	RPmag_updated=RPmag_updated_new
	dist=dist_new


dict = {'RA': RA_updated, 'Dec': Dec_updated, 'plx': plx_updated, 'dist': dist, 'pmRA': pmRA_updated, 'pmDE': pmDE_updated, 'Gmag': Gmag_updated, 'BPMag': BPmag_updated, 'RPmag': RPmag_updated}  
       
df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('RA_Dec_plx_2.csv')

