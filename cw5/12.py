def miesiace():
    miesiace=["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
    for x in miesiace:
        yield x

mie=miesiace()

for x in mie:
    print(x)