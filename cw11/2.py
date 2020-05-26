import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

n=50
fig=plt.figure()
ax=fig.gca(projection='3d')
symbols=['.',',','o','v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','X','D','d','|','_']
colors=['r','g','b','c','m','k',]
rsymbols=random.sample(symbols,5)
rcolors=random.sample(colors,5)
for a in range(5):
    x=randrange(n,0,100)
    y=randrange(n,0,100)
    z=randrange(n,10*a,10*a+10)
    ax.scatter(x,y,z,marker=rsymbols[a],c=rcolors[a])

plt.show()