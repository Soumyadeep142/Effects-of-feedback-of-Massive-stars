from numpy import *
from matplotlib.pyplot import *
import pandas as pd

#'Full', 'WISE', 'RAJ2000\ndeg', 'DEJ2000\ndeg', 'eeMaj\narcsec','eeMin\narcsec', 'Im', 'W1mag\nmag', 'e_\nmag', 'W2mag\nmag','e_\nmag.1', 'W3mag\nmag', 'e_\nmag.2', 'W4mag\nmag', 'e_\nmag.3', 'Jmag\nmag', 'Hmag\nmag', 'Kmag\nmag', 'ccf', 'ex', 'var', 'd2M\narcsec', '2M'

#New- ['Full', 'AllWISE', 'RAJ2000\ndeg', 'DEJ2000\ndeg', 'Im', 'W1mag\nmag', 'e_\nmag', 'W2mag\nmag', 'e_\nmag.1', 'W3mag\nmag', 'e_\nmag.2','W4mag\nmag', 'e_\nmag.3', 'Jmag\nmag', 'e_\nmag.4', 'Hmag\nmag', 'e_\nmag.5', 'Kmag\nmag', 'e_\nmag.6', 'ccf', 'ex', 'var',pmRA\nmas/yr', 'e_\n(...)', 'pmDE\nmas/yr', 'e_\n(...).1', 'qph', 'd2M\narcsec', '2M'],
       
df=pd.read_csv('YSO_Selection_with_color_correction_2.csv')
Full = df['Full'].tolist()
Wise = df['AllWISE'].tolist()
RA = df['RAJ2000(deg)'].tolist()
DE = df['DEJ2000(deg)'].tolist()
#eeMaj=df['eeMaj\narcsec'].tolist()
#eeMin=df['eeMin\narcsec'].tolist()
Im=df['Im'].tolist()
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
ccf=df['ccf'].tolist()
ex=df['ex'].tolist()
var=df['var'].tolist()
d2M=df['d2M(arcsec)'].tolist()
M=df['2M'].tolist()
Cl=df['Class'].tolist()

Full_New=[]
Wise_New=[]
RA_New=[]
DE_New=[]
#eeMaj_New=[]
#eeMin_New=[]
IM_New=[]
W1Mag_New=[]
e_New=[]
W2Mag_New=[]
e_1_New=[]
W3Mag_New=[]
e_2_New=[]
W4Mag_New=[]
e_3_New=[]
Jmag_New=[]
Hmag_New=[]
Kmag_New=[]
ccf_New=[]
ex_New=[]
var_New=[]
d2M_New=[]
M_New=[]
Class=[]
Type=(type(W1mag[0]))
#print(Cl[0])
for (i,j,k,l,m,o,p,q,t,u,v,w,x,y,z,a,b,c,d,e,f,g) in zip(Full, W1mag, W2mag, W3mag, W4mag, Wise, RA, DE, Im,e, e_1, e_2, e_3, Jmag, Hmag, Kmag, ccf, ex, var, d2M, M, Cl):
	if g=='AGN'or g=='SFG':
		pass
	else:
		if ((k-l)>1.5) and ((j-k)>0.15) and ((j-k)<0.8) and ((j-k)>0.46*(k-l)-0.9) and (j<=13.0):
			Full_New.append(i)
			Wise_New.append(o)
			RA_New.append(p)
			DE_New.append(q)
			#eeMaj_New.append(r)
			#eeMin_New.append(s)
			IM_New.append(t)
			W1Mag_New.append(j)
			e_New.append(u)
			W2Mag_New.append(k)
			e_1_New.append(v)
			W3Mag_New.append(l)
			e_2_New.append(w)
			W4Mag_New.append(m)
			e_3_New.append(x)
			Jmag_New.append(y)
			Hmag_New.append(z)
			Kmag_New.append(a)
			ccf_New.append(b)
			ex_New.append(c)
			var_New.append(d)
			d2M_New.append(e)
			M_New.append(f)
			Class.append('I')
		elif (m<5.0) and ((k-m)>4.5) and ((k-m)<8.0) and ((j-k)>1.0) and ((l-m)>2.0):
			Full_New.append(i)
			Wise_New.append(o)
			RA_New.append(p)
			DE_New.append(q)
			#eeMaj_New.append(r)
			#eeMin_New.append(s)
			IM_New.append(t)
			W1Mag_New.append(j)
			e_New.append(u)
			W2Mag_New.append(k)
			e_1_New.append(v)
			W3Mag_New.append(l)
			e_2_New.append(w)
			W4Mag_New.append(m)
			e_3_New.append(x)
			Jmag_New.append(y)
			Hmag_New.append(z)
			Kmag_New.append(a)
			ccf_New.append(b)
			ex_New.append(c)
			var_New.append(d)
			d2M_New.append(e)
			M_New.append(f)
			Class.append('II')
		else:
			Full_New.append(i)
			Wise_New.append(o)
			RA_New.append(p)
			DE_New.append(q)
			#eeMaj_New.append(r)
			#eeMin_New.append(s)
			IM_New.append(t)
			W1Mag_New.append(j)
			e_New.append(u)
			W2Mag_New.append(k)
			e_1_New.append(v)
			W3Mag_New.append(l)
			e_2_New.append(w)
			W4Mag_New.append(m)
			e_3_New.append(x)
			Jmag_New.append(y)
			Hmag_New.append(z)
			Kmag_New.append(a)
			ccf_New.append(b)
			ex_New.append(c)
			var_New.append(d)
			d2M_New.append(e)
			M_New.append(f)
			Class.append('NA')

dict = {'Full': Full_New, 'AllWISE': Wise_New, 'RAJ2000(deg)': RA_New, 'DEJ2000(deg)': DE_New, 'Im': IM_New, 'W1mag(mag)': W1Mag_New, 'e(mag)': e_New, 'W2mag(mag)': W2Mag_New,'e(mag).1': e_1_New, 'W3mag(mag)': W3Mag_New, 'e(mag).2': e_2_New, 'W4mag(mag)': W4Mag_New, 'e(mag).3': e_3_New, 'Jmag(mag)': Jmag_New, 'Hmag(mag)': Hmag_New, 'Kmag(mag)': Kmag_New, 'ccf': ccf_New, 'ex': ex_New, 'var': var_New, 'd2M(arcsec)': d2M_New, '2M': M_New, 'Class': Class}  
       
df1 = pd.DataFrame(dict) 
    
# saving the dataframe 
df1.to_csv('YSO_Selection_with_color_correction_N.csv')
