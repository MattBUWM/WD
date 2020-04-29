import numpy as np

def mat_w(n):
    wynik=np.diag([2 for x in np.arange(n)])
    for x in range(2,n+1):
        wynik+= np.diag([2*x for y in np.arange(n-x+1)],-(x-1))
        wynik+= np.diag([2*x for y in np.arange(n-x+1)],(x-1))
    return wynik

print(mat_w(8))