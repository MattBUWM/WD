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

    def __ge__(self,other):
        return self.x>=other.x

    def __gt__(self,other):
        return self.x>other.x

    def __le__(self,other):
        return self.x<=other.x

    def __lt__(self,other):
        return self.x<other.x

kwad1=Kwadrat(5)
kwad2=Kwadrat(3)
kwad3=Kwadrat(3)

print(str(kwad1>=kwad2)+" "+str(kwad2>=kwad3))
print(str(kwad1>kwad2)+" "+str(kwad2>kwad3))
print(str(kwad1<=kwad2)+" "+str(kwad2<=kwad3))
print(str(kwad1<kwad2)+" "+str(kwad2<kwad3))