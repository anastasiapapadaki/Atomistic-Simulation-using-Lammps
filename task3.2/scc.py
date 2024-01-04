import matplotlib.pyplot as plt
import numpy as np


lattice=np.array([1.467,1.967,2.067,2.227,2.367,2.467,2.567])
W=np.array([13841.844,-1246.248,-2255.2312, -2989.8638,-3153.6773,-3138.5226,-3035.1401])

plt.plot(lattice,W,'ro',label='Lattice-Energy')

p = np.polyfit(lattice, W,2)

lattice2=np.arange(1.0,5.0,0.1)
plt.plot(lattice2,np.polyval(p, lattice2),color='blue',label='Best Fit')

plt.title('Energy-lattice constant plot of scc',fontweight="bold")
plt.legend()
plt.xlim(0.5,4.0)
plt.show()
