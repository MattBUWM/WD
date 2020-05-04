import numpy as np

a=np.arange(12)
a3x4=a.reshape(3,4)
a4x3=a.reshape(4,3)
a2x6=a.reshape(2,6)
print(a3x4.ravel())
print(a4x3.ravel())
print(a2x6.ravel())