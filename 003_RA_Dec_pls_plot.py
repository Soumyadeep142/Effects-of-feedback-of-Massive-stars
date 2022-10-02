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
#dist_list_updated=[]

#print(max(plx_list), max(dist_list), max(pmRA_list), max(pmDE_list), max(Gmag_list), max(BPmag_list), max(RPmag_list))
i_range=[RA_list, Dec_list, dist_list, plx_list, pmRA_list, pmDE_list, Gmag_list, BPmag_list, RPmag_list]
i_range_label=['RA', 'Dec', 'dist', 'plx', 'pmRA', 'pmDE', 'Gmag', 'BPmag', 'RPmag']
for i in range(len(i_range)-1):
	for j in range(i+1, len(i_range)):
		clf()
		#print(i,j)
		#print(i_range[i], i_range[j])
		scatter(i_range[i], i_range[j])
		#print(type(i_range[i]))
		xlabel(f'{i_range_label[i]}')
		ylabel(f'{i_range_label[j]}')
		savefig(f'{i_range_label[i]}_{i_range_label[j]}.png')
		#show()
		

#scatter(BPmag_list, RPmag_list)
#show()
