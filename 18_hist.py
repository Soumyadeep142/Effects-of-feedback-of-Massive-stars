from numpy import *
from matplotlib.pyplot import *

ID, d, th_pm, th_ip=loadtxt('data_18.txt', unpack='true')
for (k, i,j) in zip(ID, th_pm, th_ip):
	scatter(j,i,label=f'{int(k)}')
legend(loc='best')
show()

diff=[abs(i-j) for (i,j) in zip(th_pm, th_ip)]
hist(diff,6)
xlabel(r'|$\theta_{ip}-\theta_{pm}|$')
ylabel("Number of BRCs")
savefig('Hist')
show()
