import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,30,0.1)

plt.plot(x,2+np.sin(x),label='sin(x)')
plt.plot(x,-np.sin(x),label='sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('wykres sin(x), sin(x)')
plt.legend()
plt.show()