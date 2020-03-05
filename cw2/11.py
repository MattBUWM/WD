wysokosc = int(input("podaj wysokosc"))
if 3 <= wysokosc <=9 : 
    for x in (i for j in (range(1,wysokosc,2), range((((wysokosc+1)//2)*2-1),0,-2)) for i in j): 
        print(f'{"o"*x:^{wysokosc}}')