def fibonacci():
    first=True
    temp1=0
    temp2=0
    while True:
        if first:
            first=False
            temp1=1
            yield 1
        else:
            temp3=temp1+temp2
            temp2=temp1
            temp1=temp3
            yield temp3

fib=fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))