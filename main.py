#P.O.O.P 1.
# import Car from car (car class)

class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def move_car(self):
        print(f"You move the {self.color} {self.year} {self.model}")
    def stop_car(self):
        print(f"You stop the {self.color} {self.year} {self.model}")
    def set_for_sale(self,for_sale_new):
        self.for_sale = for_sale_new
        print(f"For sale status : {self.for_sale}")
    def describe_car(self):
        print(f"{self.color} {self.year} {self.model}")

car1 = Car("Honda Civic", "2016", "Red", True)
car2 = Car("Mustang","2020","Yellow",False)
car3 = Car("Hellcat","2021","Black", True)
car4 = Car("Mercedes benz", "2024", "Black", True)



"""
print(car4.model)
print(car4.year)
print(car4.color)
print(car4.for_sale)

car4.set_for_sale(False)
print()

car4.describe_car()
"""