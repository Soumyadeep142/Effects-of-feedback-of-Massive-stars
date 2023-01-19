from numpy import *
from matplotlib.pyplot import *
import pandas as pd

#'Full', 'WISE', 'RAJ2000\ndeg', 'DEJ2000\ndeg', 'eeMaj\narcsec','eeMin\narcsec', 'Im', 'W1mag\nmag', 'e_\nmag', 'W2mag\nmag','e_\nmag.1', 'W3mag\nmag', 'e_\nmag.2', 'W4mag\nmag', 'e_\nmag.3', 'Jmag\nmag', 'Hmag\nmag', 'Kmag\nmag', 'ccf', 'ex', 'var', 'd2M\narcsec', '2M'
       
df=pd.read_excel('Data 1.xlsx')
Full = df['Full'].tolist()
Wise = df['WISE'].tolist()
RA = df['RAJ2000\ndeg'].tolist()
DE = df['DEJ2000\ndeg'].tolist()
eeMaj=df['eeMaj\narcsec'].tolist()
eeMin=df['eeMin\narcsec'].tolist()
Im=df['Im'].tolist()
W1mag=df['W1mag\nmag'].tolist()
e=df['e_\nmag'].tolist()
W2mag=df['W2mag\nmag'].tolist()
e_1=df['e_\nmag.1'].tolist()
W3mag=df['W3mag\nmag'].tolist()
e_2=df['e_\nmag.2'].tolist()
W4mag=df['W4mag\nmag'].tolist()
e_3=df['e_\nmag.3'].tolist()
Jmag=df['Jmag\nmag'].tolist()
Hmag=df['Hmag\nmag'].tolist()
Kmag=df['Kmag\nmag'].tolist()
ccf=df['ccf'].tolist()
ex=df['ex'].tolist()
var=df['var'].tolist()
d2M=df['d2M\narcsec'].tolist()
M=df['2M'].tolist()

x_axis_1=[]
y_axis_1=[]

x_axis_2=[]
y_axis_2=[]

for (i,j,k,l) in zip(W1mag, W2mag, W3mag, W4mag):
	x_axis_1.append(j-k)
	y_axis_1.append(i-j)
	
	x_axis_2.append(i-k)
	y_axis_2.append(i)
	
scatter(x_axis_1, y_axis_1)
xlabel('w2-w3')
ylabel('w1-w2')
savefig('Plot1.png')
clf()
scatter(x_axis_2, y_axis_2)
xlabel('w1-w3')
ylabel('w1')
savefig('Plot2.png')
