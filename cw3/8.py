def suma(a1=1,r=1,n=10):
    wynik=0
    for x in range(n):
        wynik+=a1+r*x
    return wynik

print(suma())
