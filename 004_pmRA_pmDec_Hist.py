from numpy import *
from matplotlib.pyplot import *
import pandas as pd

df = pd.read_csv('RA_Dec_plx_2.csv')
pmRA_list=[float(a) for a in df['pmRA'].tolist()]
pmDE_list=[float(a) for a in df['pmDE'].tolist()]



counts,bins=histogram(pmRA_list, bins=15, range=(min(pmRA_list), max(pmRA_list)))
hist(pmRA_list, bins=15,  edgecolor='white', facecolor='black')
plot(bins[:-1]+0.5, counts)
xlabel('pmRA')
savefig('pmRA_hist.png')

clf()

counts,bins=histogram(pmDE_list, bins=15, range=(min(pmDE_list), max(pmDE_list)))
hist(pmDE_list, bins=15,  edgecolor='white', facecolor='black')
plot(bins[:-1]+0.5, counts)
xlabel('pmDE')
savefig('pmDE_hist.png')
