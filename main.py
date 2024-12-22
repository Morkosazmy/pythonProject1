#COMPOSITION

class Engine:
    def __init__(self,hp):
        self.hp = hp

class Wheel:
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self, make, model, year, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
    def display_car(self):
        return f"{self.year} {self.make} {self.model} : {self.engine.hp}(hp) - {self.wheels[0].size}in"
car1 = Car(make="Ford", model="Mustang",year="2024",horse_power=455, wheel_size=18)
car2 = Car(make="Mercedes_Benz", model="S class", year="2025", horse_power=500, wheel_size=20)
print(car1.display_car())
print(car2.display_car())