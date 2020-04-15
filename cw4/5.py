class ciag:
    def __init__(self, ciag):
        self.ciag=ciag
        self.n=len(ciag)
        self.a1=ciag[0]
        self.r=ciag[1]-ciag[0]
    
    def wyswietl_dane(self):
        print("Ciąg: "+str(self.ciag))
        print("Pierwszy element: "+str(self.a1))
        print("Różnica: "+str(self.r))
        print("Ilość elementów: "+str(self.n))
    
    def pobierz_elementy(self,ciag):
        self.ciag=ciag
        self.n=len(ciag)
        self.a1=ciag[0]
        self.r=ciag[1]-ciag[0]
    
    def pobierz_dane(self, a1, r, n):
        self.a1=a1
        self.r=r
        self.n=n
    
    def policz_sume(self):
        suma=0
        for x in self.ciag:
            suma+=x
        return suma

    def policz_elementy(self):
        for x in range(self.n):
            self.ciag[x]=self.a1+(self.r*x)


test=ciag([1,3,5,7,9])
test.wyswietl_dane()
test.pobierz_elementy([2,6,10,14,18])
test.pobierz_dane(3,10,5)
print(test.policz_sume())
test.policz_elementy()
test.wyswietl_dane()
