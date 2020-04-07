def ilosc(**zakupy):
    suma=0
    for x in zakupy:
        suma+=zakupy[x]
    return suma

print (ilosc(a=4,b=8))