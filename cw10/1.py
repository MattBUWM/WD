import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,20,100)

plt.plot(x,1/x,label='f(x)=1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('wykres funkcji f(x) dla x [1, 20]')
plt.legend()
plt.axis([1,20,0,1])
plt.show()