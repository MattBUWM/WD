def ciag(*liczby):
    if len(liczby)==0:
        return 0.0
    else:
        suma=0.0
        for i in liczby:
            if suma==0.0:
                suma=i
            else:
                if i==0.0:
                    return 0.0
                else:
                    suma*=i
        return suma

print(ciag())
print(ciag(1,2,3,4,5,6,7,8))