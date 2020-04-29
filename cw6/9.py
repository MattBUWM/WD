import numpy as np
fib=np.array([np.arange(5) for x in np.arange(5)])
a=0
b=1
for x in np.arange(5):
    for y in np.arange(5):
        if y==0:
            fib[x][0]=a
        elif y==1:
            fib[x][1]=b
        else:
            fib[x][y]=fib[x][y-1]+fib[x][y-2]
        a=fib[x][3]+fib[x][4]
        b=fib[x][4]+a
        
print (fib)