def samogloski(string):
    for x in string:
        if x in ["a","ą","e","ę","i","o","ó","u","y","A","Ą","E","Ę","I","O","Ó","U","Y"]:
            yield x

samo1=samogloski("A Wyraz6E")

for x in samo1:
    print(x)