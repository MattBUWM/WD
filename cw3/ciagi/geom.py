#geom.py
def wyraz(a1,r,n):
    return a1*(r**(n-1))

def suma(a1,r,n):
    wynik=0
    for x in range(n):
        wynik+=a1*(r**x)
    return wynik