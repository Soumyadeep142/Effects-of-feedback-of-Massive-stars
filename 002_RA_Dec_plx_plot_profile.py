from numpy import *
from matplotlib.pyplot import *
import pandas as pd
RA, Dec=loadtxt('RA_Dec_Plx.txt', unpack='true', usecols=(0,1), skiprows=1)
#plx=loadtxt('RA_Dec_Plx.txt', unpack='true', usecols=(2), skiprows=1, dtype=str)
df = pd.read_csv('RA_Dec_plx.csv')
plx_list=(df['plx'].tolist())
A=(plx_list[4])

RA_updated=[]
Dec_updated=[]
plx_updated=[]
for (i,j,k) in zip(plx_list, RA, Dec):
	if i==A:
		pass
	else:
		plx_updated.append(float(i))
		RA_updated.append(float(j))
		Dec_updated.append(float(k))
		
dist=[1000/a for a in plx_updated]

dict = {'RA': RA_updated, 'Dec': Dec_updated, 'plx': plx_updated, 'dist': dist}  
       
df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('RA_Dec_plx_2.csv')


