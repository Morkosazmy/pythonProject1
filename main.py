#Nested Classes

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} : {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)


    def list_employees(self):
        return [employee.get_details() for employee in self.employees]



class None_profit:
    class Employee:
        pass
    pass


company1 = Company("Goodman and co.")
company1.add_employee("Mark", "CEO")
company1.add_employee("Mars", "Manager")
company1.add_employee("Spongebob","Cook")
company1.add_employee("Squidward","Cashier")
print(company1.list_employees())


company2 = Company("Chumbucket")
company2.add_employee("Sheldon", "Manager")
company2.add_employee("Computer", "Assistant")


#1
for employee in company1.list_employees():
    print(employee)

print()
#2
for employee in company2.employees:
    print(employee.get_details())

# Both 1 and 2 will do the same thing !