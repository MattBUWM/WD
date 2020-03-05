print("hello world!")

tekst = "hello world!"
tekst = 'hello world!'
tekst = """Hello
 world!"""
tekst = 0
print(tekst)
print(type(tekst))
print(type("ala"))
print(type(5))
print(type(5.5))
print(type(True))
print(type(None))

print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)
print(5 // 5) # dzielenie bez reszty
print(5 % 5) # modulo
print(5 ** 5) # potęgowanie

print("Ala "+"ma kota.") # konkatenacja
print("Ala " + "ma "+ str(5) + " lat")

liczba = int("100")

print ("Ala " * 10)

#listy
lista = []
print(type(lista))
lista2 = [1, 2, 3]
print(lista2[0])
lista2[0] = 5
imie = "Magdalena"
print(imie)
print(imie[0])
imie = imie.swapcase()
print(imie)

lista3 = [1, "ala", 4.5, None, True, [1,2]]
lista3[5][1]

macierz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
macierz[1][1] # 5
nowa = lista2 + macierz

#słownik
slownik = {}
slownik['imie'] = 'Adam'
slownik[0] = 'Adam'
print(slownik)

slownik2 = {'imie': 'Adam', 0: 'Adam'}
print(slownik2.keys())
print(slownik2.values())

def pow():
    pass

from math import *
from math import pi as mpi
import math as m

print(mpi)
#m.pow()
