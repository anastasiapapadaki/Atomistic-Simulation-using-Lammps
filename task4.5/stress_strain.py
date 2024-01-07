import numpy as np
import matplotlib.pylab as plt


x = np.loadtxt('stress.txt', usecols=(1))
y = np.loadtxt('forcetube.txt', usecols=(1))


plt.figure(figsize=(9,6))


plt.plot(x,y[:len(x)], 'r--')
plt.xlabel("Stress ",fontsize=22,)
plt.ylabel("Strain",fontsize=22)

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 4))
plt.tight_layout()
plt.title('Stress-Strain',fontweight="bold")
plt.legend(['Stress-Strain'])
plt.show()
