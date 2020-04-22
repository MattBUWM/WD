class Samogloski:
    def __init__(self, data):
        if isinstance(data,str):
            self.data = data
        else:
            self.data = str(data)
        self.index = -1
        self.temp=[]

    def __iter__(self):
        self.temp=[]
        samogloski=["a","ą","e","ę","i","o","ó","u","y","A","Ą","E","Ę","I","O","Ó","U","Y"]
        for x in self.data:
            if x in samogloski:
                self.temp+=x
        return self
    
    def __next__(self):
        self.index = self.index + 1
        if self.index >=len(self.temp):
            self.index = -1
            raise StopIteration
        return self.temp[self.index]     
    
kol1=Samogloski("A Wyraz6E")

for x in kol1:
    print(x)

for x in kol1:
    print(x)