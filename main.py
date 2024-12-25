#reduce
from functools import reduce

def add(x,y):
    return x + y

prices = [10.99, 18.99, 25.45, 29.99, 60, 70, 32 , 80]

total1 = reduce(add, prices)
total2 = reduce(lambda x, y: x + y, prices)

print(f"${total1:.2f}")

print(f"${total2:.2f}")