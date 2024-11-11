import math
import time
from itertools import count

'''vid 21: List, set, tuple'''
#List = []
#Set = {}
#Tuple = ()

"""LISTS: Ordered and changeable ! (Can have duplicates) """
games = ["God of war", "Uncharted", "The last of us", "Ghost of Tsushima"] #List
print(games)

games.append("Ratchet and Clank")
games.append("Ratchet and Clank")
games.append("Ratchet and Clank")
games.append("Ratchet and Clank")
games.insert(4,"Elden ring")
for game in games:
    print(f"-{game}")
games.sort()
print()
for game in games:
    print(f"-{game}")
print(games.count("Ratchet and Clank"))


"""SETS: Unordered and immutable(cant change), (Can't have duplicates) , We can add or remove though ! """
shapes = {"Circle", "Rectangle", "Square", "Cylinder","Circle"} # duplicates won't count when printing
print(shapes)
print("Circle" in shapes)


"""TUPLES: Ordered but unchangeable Faster than a List, Duplicates are ok"""
fruits = ("Mango", "Banana", "Orange", "Apple", "Strawberry", "Mango")
print(fruits)
print(fruits.index("Mango",1))
print(fruits)
for fruit in fruits:
    print(f"-{fruit}")
print(fruits.count("Mango"))
print(fruits.count("Apple"))
