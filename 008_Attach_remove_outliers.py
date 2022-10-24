from numpy import *
from matplotlib.pyplot import *
import pandas as pd

df = pd.read_csv('Attach_cut_Gaia.csv')
'''
'Source_ID': Source_ID_new, 'RA': RA_new, 'Dec': Dec_new, 'plx': plx_list_new, 'dist': dist_list_new, 'pmRA': pmRA_list_new, 'pmDE': pmDE_list_new, 'Gmag': Gmag_list_new, 'BPMag': BPmag_list_new, 'RPmag': RPmag_list_new, 'parallax_new': plx_new, 'plx_error': plx_error_new, 'ra_error': ra_error_new, 'dec_error': dec_error_new, 'pmRA_error': pmra_error_new, 'pmDE_error': pmde_error_new, 'Ang_dist': Ang_dist_new
'''

Source_ID=df['Source_ID'].tolist()
RA=(df['RA'].tolist())
Dec=(df['Dec'].tolist())
dist=df['dist'].tolist()
plx_list=(df['plx'].tolist())
pmRA_list=df['pmRA'].tolist()
pmDE_list=df['pmDE'].tolist()
Gmag_list=df['Gmag'].tolist()
BPmag_list=df['BPMag'].tolist()
RPmag_list=df['RPmag'].tolist()
plx_new=df['parallax_new'].tolist()
plx_error=df['plx_error'].tolist()
ra_error=df['ra_error'].tolist()
dec_error=df['dec_error'].tolist()
pmRA_error=df['pmRA_error'].tolist()
pmDE_error=df['pmDE_error'].tolist()
Ang_dist=df['Ang_dist'].tolist()


for count in range(3):
	mean_plx=mean(plx_list)
	mean_pmRA=mean(pmRA_list)
	mean_pmDE=mean(pmDE_list)
	mean_Gmag=mean(Gmag_list)
	mean_BPmag=mean(BPmag_list)
	mean_RPmag=mean(RPmag_list)
	mean_dist=mean(dist)
	mean_plx_new=mean(plx_new)
	mean_Ang_dist=mean(Ang_dist)
	
	sd_plx=std(plx_list)
	sd_pmRA=std(pmRA_list)
	sd_pmDE=std(pmDE_list)
	sd_Gmag=std(Gmag_list)
	sd_BPmag=std(BPmag_list)
	sd_RPmag=std(RPmag_list)
	sd_dist=std(dist)
	sd_plx_new=std(plx_new)
	sd_Ang_dist=std(Ang_dist)
	
	Source_new=[]
	RA_updated_new=[]
	Dec_updated_new=[]
	plx_updated_new=[]
	pmRA_updated_new=[]
	pmDE_updated_new=[]
	Gmag_updated_new=[]
	BPmag_updated_new=[]
	RPmag_updated_new=[]
	dist_new=[]
	plx2_updated=[]
	plx_error_updated=[]
	ra_error_updated=[]
	dec_error_updated=[]
	pmRA_error_updated=[]
	pmDE_error_updated=[]
	Ang_dist_updated=[]
	
	for (i,l,m,n,o,p,j,k,q,r,s,t,u,v,w,x,y) in zip(plx_list, pmRA_list, pmDE_list, Gmag_list, BPmag_list, RPmag_list, RA, Dec, dist, Source_ID, plx_new, plx_error, ra_error, dec_error, pmRA_error, pmDE_error, Ang_dist):
		if (i<(mean_plx-3*sd_plx)) or (i>(mean_plx+3*sd_plx)) or (l<(mean_pmRA-3*sd_pmRA)) or (l>(mean_pmRA+3*sd_pmRA)) or (m<(mean_pmDE-3*sd_pmDE)) or (m>(mean_pmDE+3*sd_pmDE)) or (n<(mean_Gmag-3*sd_Gmag)) or (n>(mean_Gmag+3*sd_Gmag)) or (o<(mean_BPmag-3*sd_BPmag)) or (o>(mean_BPmag+3*sd_BPmag)) or (p<(mean_RPmag-3*sd_RPmag)) or (p>(mean_RPmag+3*sd_RPmag)) or (q<(mean_dist-3*sd_dist)) or (q>(mean_dist+3*sd_dist)) or (s>(mean_plx_new+3*sd_plx_new)) or (s<(mean_plx_new-3*sd_plx_new)) or (y>(mean_Ang_dist+3*sd_Ang_dist)) or (y<(mean_Ang_dist-3*sd_Ang_dist)):
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
			Source_new.append(float(r))
			plx2_updated.append(float(s))
			plx_error_updated.append(float(t))
			ra_error_updated.append(float(u))
			dec_error_updated.append(float(v))
			pmRA_error_updated.append(float(w))
			pmDE_error_updated.append(float(x))
			Ang_dist_updated.append(float(y))
		
	RA_updated=RA_updated_new
	Dec_updated=Dec_updated_new
	plx_updated=plx_updated_new
	pmRA_updated=pmRA_updated_new
	pmDE_updated=pmDE_updated_new
	Gmag_updated=Gmag_updated_new
	BPmag_updated=BPmag_updated_new
	RPmag_updated=RPmag_updated_new
	dist=dist_new
	Source_ID=Source_new
	plx_new=plx2_updated
	plx_error=plx_error_updated
	ra_error=ra_error_updated
	dec_error=dec_error_updated
	pmRA_error=pmRA_error_updated
	pmDE_error=pmDE_error_updated
	Ang_dist=Ang_dist_updated
	
dict = {'Source_ID': Source_new, 'RA': RA_updated, 'Dec': Dec_updated, 'plx': plx_updated, 'dist': dist_new, 'pmRA': pmRA_updated, 'pmDE': pmDE_updated, 'Gmag': Gmag_updated, 'BPMag': BPmag_updated, 'RPmag': RPmag_updated, 'parallax_new': plx_new, 'plx_error': plx_error, 'ra_error': ra_error, 'dec_error': dec_error, 'pmRA_error': pmRA_error, 'pmDE_error': pmDE_error, 'Ang_dist': Ang_dist}  
       
df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('Attach_cut_Gaia_w_o.csv')
