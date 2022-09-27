from numpy import *
from matplotlib.pyplot import *
import pandas as pd

df = pd.read_csv('RA_Dec_plx_2.csv')
plx_list=[float(a) for a in (df['plx'].tolist())]
RA_list=[float(a) for a in (df['RA'].tolist())]
Dec_list=[float(a) for a in (df['Dec'].tolist())]
dist_list=[float(a) for a in (df['dist'].tolist())]

dist_list_updated=[]


xlim(100,1500)
#dist_list_updated=[a/1000 for a in dist_list]
scatter(dist_list, Dec_list)
xlabel('dist')
ylabel('Dec')
savefig('Dec_dist.png')

clf()
xlim(100,1500)
scatter(dist_list, RA_list)
xlabel('dist')
ylabel('RA')
savefig('RA_dist.png')
