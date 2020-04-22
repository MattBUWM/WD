class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]



kol1=Wspak([1,2,3,4,5,6])
kol2=Wspak(["Kota","Ma","Ala"])

for x in kol1:
    print(x)

for x in kol2:
    print(x)