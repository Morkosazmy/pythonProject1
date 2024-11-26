from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("GO !")
    def stop(self):
        print("STOP !")

class Motorcycle(Vehicle):
    def go(self):
        print("The bike moves")
    def stop(self):
        print("The bike stops")

class Boat(Vehicle):
    def go(self):
        print("You sail the boat")
    def stop(self):
        print("You drop the anchor to stop the boat")