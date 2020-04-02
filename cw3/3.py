Produkty={"Ziemniaki" : "Kg", "Mydło" : "Sztuki", "Woda" : "Litry", "Kubki" : "Sztuki"}
Produkty_sztuki=[x for x,y in Produkty.items() if y=="Sztuki"]
print(Produkty_sztuki)