import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig=plt.figure()
ax1=fig.add_subplot(121, projection='3d')
x=randrange(20,0,50)
y=randrange(20,0,50)
ax1.scatter(x,y)
ax2=fig.add_subplot(122, projection='3d')
x=[0,20,20,40,60]
y=[40,40,60,60,60]
ax2.plot(x,y)
plt.show()