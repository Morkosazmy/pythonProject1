# writing files ( a, x, r, w )



# w to write or create a new one    ( it will override the file )
# x to create a new one and if it exists it'll give an error and won't create a second one

"""
txt_data = "I love you !"

file_path = "C:/Users/morko/OneDrive/Bureau/python_test.txt"

try:
    with open(file_path, "w" ) as file:
        file.write(txt_data)
        print(f"The file '{file_path}' was created")
except FileExistsError:
    print("The file exists already")

# a to append data to an existing file


try:
    with open(file_path, "a" ) as file:
        file.write("\n" + txt_data)
        print(f"The file '{file_path}' was created")
except FileExistsError:
    print("The file exists already")

"""
import json


"""
# Collections
employees = ["Patrick", "Spongebob", "Eugene", "Squidward", "Sally"]

file_path = "C:/Users/morko/OneDrive/Bureau/python_test.txt"

try:
    with open(file_path, "w" ) as file:
        for employee in employees:
            file.write(" " + employee)
        print(f"The file '{file_path}' was created ")
except FileExistsError:
    print("The file exists already ")
"""

"""
#json
employee = {
    "name" : "Spongebob",
    "age" : 30,
    "position" : "chef"
}


file_path = "C:/Users/morko/OneDrive/Bureau/python_test.json"

try:
    with open(file_path, "w" ) as file:
        json.dump(employee, file, indent = 4)
        #for employee in employees:
        #    file.write(" " + employee)
        print(f"The json file '{file_path}' was created ")
except FileExistsError:
    print("The file exists already ")

"""

import csv

file_path = "C:/Users/morko/OneDrive/Bureau/ING INFO/python_tesst.csv"
employees = [["name", "age", "job"],
             ["Spongebob", 30, "cook"],
             ["Patrick", 38, "unemployed"],
             ["Eugene", 56, "manager"],
             ["Squidward", 40, "cashier"]]
try:
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"The CSV file '{file_path}' was created ")
except FileExistsError:
    print("The file exists already ")
