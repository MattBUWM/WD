import numpy as np

def macierz(n):
    a=np.arange(n,0,-1)
    return np.diag(a)

print(macierz(5))