from numpy import *
from matplotlib.pyplot import *
import pandas as pd

df = pd.read_csv('RA_Dec_plx_2.csv')
plx_list=[float(a) for a in (df['plx'].tolist())]
RA_list=[float(a) for a in (df['RA'].tolist())]
Dec_list=[float(a) for a in (df['Dec'].tolist())]
dist_list=[float(a) for a in (df['dist'].tolist())]
i=1
x=[300,500,700,900]
for j in x:
	scatter(dist_list, RA_list)
	xlim(100,j)
	xlabel('dist')
	ylabel('RA')
	savefig('RA_dist_{0}.png'.format(i))
	i+=1
	
i=0	
for j in x:
	scatter(dist_list, Dec_list)
	xlim(100,j)
	xlabel('dist')
	ylabel('Dec')
	savefig('Dec_dist_{0}.png'.format(i))
	i+=1
	
