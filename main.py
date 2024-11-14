#Creating functions !
from typing import override


def happy_birthday():
    print("Happiest of birthdays QUEER.")
    print("Oh my bad i meant QUEEN hehe !")
    for x in range(3):
        print("CELEBRATION MOVES")
def Dr_Han():
    for x in range(3):
        print("I AM A SURGEON !")
    print("I AM A SURGEON DR HAN !")
    print("I AM A SURGEON !")

def add(num1,num2):
    x = num1 + num2
    return x
def subtract(x,y):
    z = x - y
    return z
def multiply(x,y):
    z = x * y
    return z
def divide(x,y):
    z = x / y
    return z
a = add(2,3)
b = subtract(2,3)
c = multiply(2,3)
d = divide(2,3)

print(f"a = {a}\n"
      f"b = {b}\n"
      f"c = {c}\n"
      f"d = {d:.2f}\n")

def create_name(prenom, nom):
    firstname = prenom.capitalize()
    lastname = nom.upper()
    return lastname + " " + firstname
my_name = create_name("prénom","nom")
#cant use my_name.create_name cause that's for methods not functions and we created a function.

print(my_name)
#print(add(3,5))