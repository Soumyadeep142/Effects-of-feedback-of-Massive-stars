from numpy import *
from matplotlib.pyplot import *
import pandas as pd

#'Unnamed: 0', 'RAJ2000(deg)', 'DEJ2000(deg)', 'W1mag(mag)', 'e(mag)', 'W2mag(mag)', 'e(mag).1', 'W3mag(mag)', 'e(mag).2', 'W4mag(mag)', 'e(mag).3', 'Jmag(mag)', 'Hmag(mag)', 'Kmag(mag)', 'Class'
df=pd.read_csv('YSO_Selection_with_color_correction_N.csv')

#print(df.keys())

#Full = df['Full'].tolist()
#Wise = df['WISE'].tolist()
RA = df['RAJ2000(deg)'].tolist()
DE = df['DEJ2000(deg)'].tolist()
#eeMaj=df['eeMaj\narcsec'].tolist()
#eeMin=df['eeMin\narcsec'].tolist()
#Im=df['Im'].tolist()
W1mag=df['W1mag(mag)'].tolist()
e=df['e(mag)'].tolist()
W2mag=df['W2mag(mag)'].tolist()
e_1=df['e(mag).1'].tolist()
W3mag=df['W3mag(mag)'].tolist()
e_2=df['e(mag).2'].tolist()
W4mag=df['W4mag(mag)'].tolist()
e_3=df['e(mag).3'].tolist()
Jmag=df['Jmag(mag)'].tolist()
Hmag=df['Hmag(mag)'].tolist()
Kmag=df['Kmag(mag)'].tolist()
#ccf=df['ccf'].tolist()
#ex=df['ex'].tolist()
#var=df['var'].tolist()
#d2M=df['d2M\narcsec'].tolist()
#M=df['2M'].tolist()
Class=df['Class'].tolist()

#print(len(Class))

x_axis_1_C1=[]
y_axis_1_C1=[]

x_axis_1_C2=[]
y_axis_1_C2=[]

x_axis_1_C3=[]
y_axis_1_C3=[]

x_axis_2_C1=[]
y_axis_2_C1=[]

x_axis_2_C2=[]
y_axis_2_C2=[]

x_axis_2_C3=[]
y_axis_2_C3=[]

for (i,j,k,l,m) in zip(W1mag, W2mag, W3mag, W4mag, Class):		
	if m=='I':
		print(m)
		x_axis_1_C1.append(j-k)
		y_axis_1_C1.append(i-j)
		
		x_axis_2_C1.append(i-k)
		y_axis_2_C1.append(i)
		
		
	elif m=='II':
		x_axis_1_C2.append(j-k)
		y_axis_1_C2.append(i-j)
		
		x_axis_2_C2.append(i-k)
		y_axis_2_C2.append(i)
		
	else:
		x_axis_1_C3.append(j-k)
		y_axis_1_C3.append(i-j)
		
		x_axis_2_C3.append(i-k)
		y_axis_2_C3.append(i)
		
scatter(x_axis_1_C1, y_axis_1_C1, label='Class I', s=10, marker='x')
scatter(x_axis_1_C2, y_axis_1_C2, label='Class II', s=10, marker='+')
scatter(x_axis_1_C3, y_axis_1_C3,s=1, label='No class')
legend(loc='best')
xlabel('w2-w3')
ylabel('w1-w2')
savefig('Plot1_new_I_II.png')
clf()
scatter(x_axis_2_C1, y_axis_2_C1, label='Class I', s=1)
scatter(x_axis_2_C2, y_axis_2_C2, label='Class II', s=1)
scatter(x_axis_2_C3, y_axis_2_C3, s=1, label='No Class')
legend(loc='best')
xlabel('w1-w3')
ylabel('w1')
savefig('Plot2_new_I_II.png')

