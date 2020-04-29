import numpy as np

s1=np.array(list("slowo"))
s2=np.array(list("wyraz"))
s3=np.array(list("string"))

wykresl=np.empty((10,10),dtype="U1")

for x in range(s1.size):
    wykresl[3][x+1]=s1[x]

for x in range(s2.size):
    wykresl[x+1][0]=s2[x]

for x in range(s3.size):
    wykresl[9-x][9-x]=s3[x]

print(wykresl)