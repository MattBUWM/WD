import random
Matryca=[[random.randrange(0,10) for x in range(4)] for x in range(4)]
print(Matryca)
Lista=[Matryca[x][x] for x in range(4)]
print(Lista)