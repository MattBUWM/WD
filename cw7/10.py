import numpy as np

a=np.array([np.arange(9) for b in np.arange(9)])
print(a.reshape(3,27))

"""
możliwe przekształcenia:
1x81
3x27
9x9
27x3
81x1
"""