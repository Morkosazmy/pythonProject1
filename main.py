import math
import time
from functools import total_ordering
from time import process_time_ns

'''-----vid 26: Dictionaries (MAPS) -----'''
menu = {"popcorn":5.99,
        "hotdog":1.99,
        "pretzel":2.99,
        "nachos":3,
        "soda":3.50,
        "bottled water":1.99}

print("------------- MENU -------------")
for key, value in menu.items():
    print(f"{key:13} ............ ${value:.2f}")
print("--------------------------------")
cart = []
total = 0


while True:
    food = input("Select an item (q to quit) ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------------- YOUR ORDER -------------")

for food in cart:
    total += menu.get(food)
    print(f"You added a {food}\t\t",end="")

print(f"Your total is : ${total:.2f}")



"""
while True:
    food = input("Select an item (q to quit) : ")
    if food == "q":
        break
    elif food == "popcorn":
        cart.append(food)
        print(f"You added a {food}")
        #total += 5.99
    elif food == "hot dog":
        cart.append(food)
        print(f"You added a {food}")
        #total += 1.99
    elif food == "giant pretzel":
        cart.append(food)
        print(f"You added a {food}")
        #total += 2.99
    elif food == "nachos":
        cart.append(food)
        print(f"You added a {food}")
        #total += 3
    elif food == "soda":
        cart.append(food)
        print(f"You added a {food}")
        #total += 3.5
    elif food == "Bottled Water":
        cart.append(food)
        print(f"You added a {food}")
        #total += 1.99
    else:
        print("That item is not on the menu, please re-enter the item's name !")
print(f"You ordered : {cart}")
print(f"Your total is : ${total}")
num_popcorn = cart.count("popcorn")
num_giant_pretzel = cart.count("giant pretzel")
num_soda = cart.count("soda")
num_hot_dog = cart.count("hot dog")
num_nachos = cart.count("nachos")
num_bottled_water = cart.count("bottled water")

print(f"{num_popcorn}, {num_giant_pretzel}, {num_soda}, {num_hot_dog}, {num_nachos}, {num_bottled_water}")


for item in cart:
    if item == "popcorn":
        print("You ")
    elif item == "hot dog":
        cart.append(item)
        total += 1.99
    elif item == "giant pretzel":
        cart.append(item)
        total += 2.99
    elif item == "nachos":
        cart.append(item)
        total += 3
    elif item == "soda":
        cart.append(item)
        total += 3.5
    elif item == "Bottled Water":
        cart.append(item)
        total += 1.99



items = menu.keys()
prices = menu.values()

print("------------CONCESSIONS------------")
itemsxprices = menu.items()
num_menu=0
for item, price in itemsxprices:
    print(f"{num_menu+1}. Item: {item:<13} ,price: ${price:<10}")
    num_menu += 1
order = int(input("What would you like to order ? (Choose from 1 to 6) (0 to quit)"))
order_total = 0
if order == 0:
    print("Order cancelled !")
    exit()
elif order == 1 or order == 4 or order == 5 or order == 6:
    order_total += 1
elif order == 2 or order == 3:
    order_total += 2
order = int

while True:
    order = int(input("Would you like anything else ? (Choose from 1 to 6) (0 to quit)"))
    if order == 0:
        break
    elif order == 1 or order == 4 or order == 5 or order == 6:
        order_total += 1
    else:
        order_total += 2

print(f"Your total is ${order_total}")
"""
#i can get the total but i cant get the item itself tho ! 
