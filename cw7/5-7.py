import numpy as np

m1=np.array([
    [40,80,0,20],
    [180,90,45,0]
])

a=np.sin(m1)
print(a)

m2=np.array([
    [np.pi/2,np.pi/3,0,np.pi/20],
    [np.pi/6,np.pi,np.pi*2,0]
])
b=np.cos(m2)
print(b)

print(np.add(a,b))