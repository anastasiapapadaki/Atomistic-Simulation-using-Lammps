import numpy as np
import matplotlib.pylab as plt



def W(p0,p1,p2,l):
    return (p0+p1*l+p2*(l**2))

l = [3.597,2.956,2.56]
W = [14153, 6926, 6452]

plt.figure(figsize=(9,6))
plt.plot(l,W, 'r--' , LineWidth = 2)
plt.xlabel("Lattice ($\AA$)",fontsize=22,) 
plt.ylabel("W(Ev)",fontsize=22)

plt.xticks(fontsize=16);  plt.yticks(fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 4))

plt.tight_layout()



plt.title('Energy-lattice constant plot',fontweight="bold")
plt.legend(['Energy-lattice constant plot'])
plt.show()
