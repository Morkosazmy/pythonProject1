#Class Methods

class Student:

    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} : {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"The total number of students is : {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        return f"Average Gpa : {(cls.total_gpa / cls.count):.2f}"
#print(Student.get_count())

student1 = Student("Mark",3.9)
student2 = Student("Marco",3.227)
student3 = Student("Nick",3.23334)
student4 = Student("pete",4.0)

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(student4.get_info())

print(Student.get_count())


print(Student.total_gpa)
print(Student.get_count())
print(Student.get_average_gpa())