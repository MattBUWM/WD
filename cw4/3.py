with open("zadanie3.txt","w") as plik:
    plik.write("ala\n")
    plik.write("ma\n")
    plik.write("kota\n")
    
with open("zadanie3.txt","r") as plik:
    for linia in plik:
        print(linia,end="")
