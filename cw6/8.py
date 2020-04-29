import numpy as np

def podzial(mat,kierunek):
    a,b=mat.shape
    if kierunek==0:
        if a%2==0:
            return mat[:int(a/2),:],mat[int(a/2):,:]
        else:
            print("Podział niemożliwy")
            return 0,0
    elif kierunek==1:
        if b%2==0:
            return mat[:,:int(b/2)],mat[:,int(b/2):]
        else:
            print("Podział niemożliwy")
            return 0,0
    

a=np.array([
    [2, 3, 5, 6],
    [4, 4, 1, 4],
    [8, 3, 5, 6],
    [34, 4, 1, 4]])
b,c=podzial(a,0)

print(c)
print(b)

b,c=podzial(a,1)

print(c)
print(b)