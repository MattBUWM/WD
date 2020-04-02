A=[1/i for i in range(10) if i>0]
B=[2**i for i in range(10)]
C=[i for i in B if i%4==0]
print(A)
print(B)
print(C)