class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    
    def __add__(self, other):
        return Kwadrat(self.x+other.x)

kwad1=Kwadrat(5)
kwad2=Kwadrat(3)
kwad3=kwad1+kwad2
print(str(kwad3.x))