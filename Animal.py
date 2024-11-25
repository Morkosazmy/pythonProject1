class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def sleep(self):
        print(f"{self.name} is sleeping ! ")

    def eat(self):
        print(f"{self.name} is eating !")


#class Creature:
#    def __init__(self, is_big):
#        self.is_big = is_big




class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")
    def talk(self):
        print("WOOF !!!")
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")
    def talk(self):
        print("MEOW !!!")
class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} is squeaking")
    def talk(self):
        print("SQUEAK !!!")

