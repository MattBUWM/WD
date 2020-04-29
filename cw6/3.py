import numpy as np

def ciag(n):
    return np.array([np.arange(x*n+1,x*n+n+1) for x in np.arange(0,n)])


print(ciag(5))