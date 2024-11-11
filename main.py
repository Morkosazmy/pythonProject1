import math
import time
from itertools import count

'''vid 22: Shopping cart ! '''

total = 0
prices = []
items = []

while True:
    item = input("Enter the name of the item that you would like to purchase please (q to quit) : ")
    if item.lower() == "q":
        break
    else:
        items.append(item)
        price = float(input(f"Enter the price of a {item} please: $"))
        prices.append(price)

print("----- YOUR SHOPPING CART -----")
for item in range(0,len(items)-1):
    print(items[item],end=", ")
for item in range(len(items)-1,len(items)):
    print(items[item],end=".\n")
print()
for price in prices:
    total += price

print(f"Your total is : ${total}")