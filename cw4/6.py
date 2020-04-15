class slowa:
    def __init__(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    
    def czy_palindrom(self):
        for x in range(len(self.slowo1)):
            if self.slowo1[x]!=self.slowo1[len(self.slowo1)-(x+1)]:
                return False
        return True
    
    def czy_metagramy(self):
        temp=0
        for x in range(len(self.slowo1)):
            if self.slowo1[x]!=self.slowo2[x]:
                temp+=1
                if temp > 1: return False
        return True if temp==1 else False

    def czy_anagramy(self):
        temp=self.slowo2
        for x in self.slowo1:
            temp2=temp.replace(x,"",1)
            if temp==temp2:
                return False
            temp=temp2
        return True

    def wyswietl_wyrazy(self):
        print("Wyraz 1: "+self.slowo1)
        print("Wyraz 2: "+self.slowo2)



test=slowa("zakaz","nakaz")
print(test.czy_palindrom())
print(test.czy_metagramy())
print(test.czy_anagramy())
test.wyswietl_wyrazy()