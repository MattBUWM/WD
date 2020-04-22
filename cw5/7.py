class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 2
        if self.index >=len(self.data):
            self.index = -2
            raise StopIteration
        return self.data[self.index]

kol1=Parzyste([1,0,1,0,1,0,1,0,1,0])

for x in kol1:
    print(x)

for x in kol1:
    print(x)