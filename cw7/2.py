import numpy as np

m3x3=np.array(
    [[4,7,2],
    [7,1,10],
    [9,7,13]]
)

m4x4=np.array(
    [[4,7,8,2],
    [7,3,1,10],
    [9,7,13,1],
    [0,8,5,3]]
)

print(m3x3.min(axis=0))
print(m3x3.min(axis=1))
print(m4x4.min(axis=0))
print(m4x4.min(axis=1))