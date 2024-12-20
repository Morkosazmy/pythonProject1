class Animal:
        alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Duck(Animal):
    def speak(self):
        print("QUACK!")

class Car:
    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(),Cat(),Duck(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive, end="\n\n")