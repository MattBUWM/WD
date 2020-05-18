import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,30,0.1)

plt.plot(x,np.sin(x),label='sin(x)')
plt.plot(x,np.cos(x),label='cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('sinus i cosinus')
plt.legend()
plt.show()