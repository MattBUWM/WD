plik=open("przez4.txt","w")
lista=[]
for x in range(100):
    if (x%4==0):
        lista+=[x]
plik.writelines(str(lista))
plik.close