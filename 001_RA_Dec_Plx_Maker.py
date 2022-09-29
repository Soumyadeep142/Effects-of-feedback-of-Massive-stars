import pandas as pd
from numpy import *
from matplotlib.pyplot import *

#RA_ICRS;DE_ICRS;Plx;e_Plx;pmRA;e_pmRA;pmDE;e_pmDE;Gmag;e_Gmag;BPmag;e_BPmag;RPmag;e_RPmag

df = pd.read_csv('Gaia_SFO38.tsv', skiprows=64, skipfooter=50, sep=';')
RA_list = df['RA_ICRS'].tolist()
Dec_list=df['DE_ICRS'].tolist()
plx_list=df['Plx'].tolist()
error_plx_list=df['e_Plx'].tolist()
pmRA_list=df['pmRA'].tolist()
error_pmRA_list=df['e_pmRA'].tolist()
pmDE_list=df['pmDE'].tolist()
error_pmDE_list=df['e_pmDE'].tolist()
Gmag_list=df['Gmag'].tolist()
error_Gmag_list=df['e_Gmag'].tolist()
BPmag_list=df['BPmag'].tolist()
error_BPmag_list=df['e_BPmag'].tolist()
RPmag_list=df['RPmag'].tolist()
error_RPmag_list=df['e_RPmag'].tolist()

for i in range(2):
	RA_list.pop(0)
	Dec_list.pop(0)
	plx_list.pop(0)
	error_plx_list.pop(0)
	pmRA_list.pop(0)
	error_pmRA_list.pop(0)
	pmDE_list.pop(0)
	error_pmDE_list.pop(0)
	Gmag_list.pop(0)
	error_Gmag_list.pop(0)
	BPmag_list.pop(0)
	error_BPmag_list.pop(0)
	RPmag_list.pop(0)
	error_RPmag_list.pop(0)

#RA_list.insert(0, "RA")
#Dec_list.insert(0, 'Dec')
#plx_list.insert(0, 'Plx')

#col =column_stack((RA_list, Dec_list, plx_list))
#savetxt('RA_Dec_Plx.txt', col,  fmt='%s')
dict = {'RA': RA_list, 'Dec': Dec_list, 'plx': plx_list, 'pmRA': pmRA_list, 'pmDE': pmDE_list, 'Gmag': Gmag_list, 'BPMag': BPmag_list, 'RPmag': RPmag_list}  
       
df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('RA_Dec_plx.csv')
