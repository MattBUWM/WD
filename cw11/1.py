import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.gca(projection='3d')
z=np.linspace(0,2*np.pi,100)

ax.plot(np.sin(z),2*np.cos(z),z)
plt.show()