import matplotlib.pyplot as plt
import numpy as np


lattice=np.array([2.367,2.997,3.125,3.597,3.988,4.367,4.997])
W=np.array([72639.632,-4412.381,-8870.7905, -14154.68,-12815.233,-10408.056,-6144.0533])

plt.plot(lattice,W,'ro',label='Lattice-Energy')

p = np.polyfit(lattice, W,2)

lattice2=np.arange(2.3,10.0,0.1)
plt.plot(lattice2,np.polyval(p, lattice2),color='blue',label='Best Fit')

plt.title('Energy-lattice constant plot of fcc',fontweight="bold")
plt.legend()
plt.show()
