# mini calculator

import math
import time
from asyncio import wait_for

'''vid 19 : nested loops'''

credit_card = "1234-5678-9012-3456"

for y in range (3):
    print()
    for x in range (1,10):
        print(x, end="")
    print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")

for y in range(rows):
    for x in range(columns):
        print(symbol, end="")
    print()



for i in range(4): # equivalent of range(0,4)
    print(i)