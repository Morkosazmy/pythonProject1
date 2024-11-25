#P.O.O.P 4.
#Multi level inheritance
#multiple inheritance
import Animal
#from Animal import rabbit

dog1 = Animal.Dog("Roy")
dog2 = Animal.Dog("Lulu")
cat1 = Animal.Cat("Johara")
cat2 = Animal.Cat("Cheetos")
mouse1 = Animal.Mouse("Minnie")

#dog3 = Dog("gog", True)

print(cat1.name)
print(cat1.is_alive)
cat1.eat()
cat1.sleep()
cat1.meow()
cat2.talk()

print()
print(cat2.name)
print(cat2.is_alive)

cat2.eat()
cat2.sleep()
cat2.meow()
cat2.talk()

print()
print(dog1.name)
print(dog1.is_alive)

dog1.eat()
dog1.sleep()
dog1.bark()
dog1.talk()

print()
print(mouse1.name)
print(mouse1.is_alive)

mouse1.eat()
mouse1.sleep()
mouse1.squeak()
mouse1.talk()




rabbit1 = Animal.Rabbit("bugs")
rabbit1.flee()

hawk1 = Animal.Hawk("Tony")
hawk1.hunt()

fish1 = Animal.Fish("Neemo")
fish1.hunt()
fish1.flee()

fish1.eat()

hawk1.hunt()

















"""
class Student:
    graduation_year = 2026
    num_students = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1
print(Student.num_students)
student1 = Student("Spongebob", 31)
print(Student.num_students)
student2 = Student("Patrick", 32)
student3 = Student("Squidward", 36)
student4 = Student("Sandy", 18)
print(student1.name, end=" ")
print(student1.age)
print(student2.name, end=" ")
print(student2.age)

print(student1.graduation_year)
print(student2.graduation_year)
print(Student.graduation_year) # it is better to access this type of variable with the class's name itself instead of accessing it through instances like student1 or student2 as they are global!

print(Student.num_students)
print(f"My Graduation class {Student.graduation_year} has {Student.num_students} students : ")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
"""