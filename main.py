#P.O.O.P 2.

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