import numpy as np
import matplotlib.pylab as plt


data = np.loadtxt('pe.txt')
x=data[:,0]
p= data[:,1]
plt.figure(figsize=(9,6))

plt.plot(x,p, 'r--' , LineWidth = 2)
plt.xlabel("Time Step",fontsize=22,) 
plt.ylabel("Potential Energy",fontsize=22)

plt.xticks(fontsize=16);  plt.yticks(fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 4))

plt.tight_layout()



plt.title('Potential Energy T=0K',fontweight="bold")
plt.legend(['Potential Energy T=0K'])
plt.show()
