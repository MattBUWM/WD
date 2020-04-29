import numpy as np

def generuj(l,p):
    return np.logspace(1,p,num=p,base=l)

print(generuj(2,4))