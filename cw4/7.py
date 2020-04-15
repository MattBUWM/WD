class robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok

    def idz_w_gore(self,kroki):
        self.x+=kroki*self.krok

    def idz_w_dol(self,kroki):
        self.x-=kroki*self.krok

    def idz_w_lewo(self,kroki):
        self.y-=kroki*self.krok

    def idz_w_prawo(self,kroki):
        self.y+=kroki*self.krok

    def pokaz_gdzie_jestes(self):
        print("x="+str(self.x))
        print("y="+str(self.y)+"\n")

    def __del__(self):
        print("Robaczek znudził się chodzeniem")


test=robaczek(0,0,5)
test.idz_w_dol(2)
test.pokaz_gdzie_jestes()
test.idz_w_lewo(1)
test.pokaz_gdzie_jestes()
test.idz_w_gore(12)
test.pokaz_gdzie_jestes()
test.idz_w_prawo(4)
test.pokaz_gdzie_jestes()