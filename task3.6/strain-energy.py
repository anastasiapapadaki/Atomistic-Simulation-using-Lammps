import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

x = np.loadtxt('boxsize0.txt', usecols=(1))
y = np.loadtxt('pressure0.txt', usecols=(1))


# define the true objective function
def objective(x, a, b):
	return a * x + b
# curve fit
popt, _ = curve_fit(objective, (x[:10]-x[0])/x[0], -y[:10])
# summarize the parameter values
a,b = popt
print('y =%.1f * x + %.1f' % (a*100000,b))


plt.plot((x-x[0])/x[0],(-y[:len(x)])*100000, 'r--')
plt.plot((x-x[0])/x[0],(a*(x-x[0])/x[0] + b)*100000, 'b-')
plt.xlabel("Strain ",fontsize=22,)
plt.ylabel("Stress",fontsize=22)

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 4))
plt.tight_layout()
plt.title('Strain Energy for t=0K',fontweight="bold")
plt.legend(['Strain Energy for t=0K'])
plt.show()
