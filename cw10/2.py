import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,19,19,)

plt.plot(x,1/x,'g>:',label='f(x)=1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('wykres funkcji f(x) dla x [1, 20]')
plt.legend()
plt.axis([0,20,0,1])
plt.show()