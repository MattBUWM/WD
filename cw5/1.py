class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    
    def wyswietl_nazwe(self):
        print(self.rodzaj)

class Ubrania(Material):
    rozmiar="XL"
    kolor="Czerwony"
    dla_kogo="Marian Bezowski"

    def wyswietl_dane(self):
        print("Rozmiar: "+self.rozmiar)
        print("Rodzaj materiału: "+self.rodzaj)
        print("Kolor: "+self.kolor)
        print("Dla: "+self.dla_kogo)

class Sweter(Ubrania):
    rodzaj_swetra="Rozpinany"

    def wyswietl_dane(self):
        print("Rodzaj swetra: "+self.rodzaj_swetra)
        print("Rozmiar: "+self.rozmiar)
        print("Rodzaj materiału: "+self.rodzaj)
        print("Kolor: "+self.kolor)
        print("Dla: "+self.dla_kogo)

sweterek=Sweter("Wełna",3,3)
sweterek.wyswietl_dane()