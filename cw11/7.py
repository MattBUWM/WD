import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig=plt.figure()
ax=fig.gca(projection='3d')
x=randrange(20,0,50)
y=randrange(20,0,50)
ax.scatter(x,y,color='red', marker='o')
x=[0,20,20,40,60]
y=[40,40,60,60,60]
ax.plot(x,y,color='green')
ax.set_zlim(0)
plt.show()