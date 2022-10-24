from numpy import *
from matplotlib.pyplot import *
import pandas as pd
import os


os.makedirs('Attach')

df = pd.read_csv('Attach_cut_Gaia_w_o.csv')

Ang_dist_list=[float(a) for a in (df['Ang_dist'].tolist())]
pmRA_list=[float(a) for a in df['pmRA'].tolist()]
pmDE_list=[float(a) for a in df['pmDE'].tolist()]

i_range=[Ang_dist_list, pmRA_list, pmDE_list]
i_range_label=['Ang_dist', 'pmRA', 'pmDE']
for i in range(len(i_range)-1):
	for j in range(i+1, len(i_range)):
		clf()
		#print(i,j)
		#print(i_range[i], i_range[j])
		scatter(i_range[i], i_range[j])
		#print(type(i_range[i]))
		xlabel(f'{i_range_label[i]}')
		ylabel(f'{i_range_label[j]}')
		savefig(f'/home/user/Desktop/Samrat/Attach/attach_{i_range_label[i]}_{i_range_label[j]}.png')
