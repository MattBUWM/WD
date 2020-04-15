class NaZakupy:
    def __init__(self,nazwa,ilosc,jednostka,cena):
        self.nazwa_produktu=nazwa
        self.ilosc=ilosc
        self.jednostka_miary=jednostka
        self.cena_jed=cena
    
    def wyswietl_produkt(self):
        print("Nazwa: "+self.nazwa_produktu)
        print("Ilość: "+str(self.ilosc))
        print("Jednostka: "+self.jednostka_miary)
        print("Cena: "+str(self.cena_jed)+"zł")
    
    def ile_produktu(self):
        print(str(self.ilosc)+self.jednostka_miary)
    
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed

obiekt=NaZakupy("cos",7,"kg",2.59)
obiekt.wyswietl_produkt()
obiekt.ile_produktu()
print(obiekt.ile_kosztuje())