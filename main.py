# mini calculator

import math

# 1. less than 12 characters ! (DONE)
# 2. no spaces ! (DONE)
# 3. no digits ! (only contains letters)


# while loops !
"""

'''vid 16'''
name = input("Enter your name\n")

while name == "":
    print("You didn't enter your name !")
    name = input("Enter your name\n")
print(f"Hello {name}")

age = str(input("Enter your age: "))

while age ==  "":
    print("You didn't enter your age !")
    age = str(input("Enter your age: "))
age = int(age)
while age < 0:
    print("Your age cant be a negative number !")
    age = int(input("Enter your age in numbers only ! "))

if age == 1:
    print(f"You are a {age} year old !")
else:
    print(f"You are {age} year(s) old !")

food = input("Enter your favorite food (PRESS Q to quit !) \n")

if food == "Q":
    print("BYE BYE")
    exit()

while food == "":
    print("You didn't enter your favorite food !")
    food = input("Enter your favorite food\n")
print(f"Your favorite food is {food}")

"""



'''
''''''vid 15''''''
price1 = 684.584684
price2 = -874.21
price3 = 6.3

print(f"Price 1 is {price1:.2f}")
print(f"Price 2 is {price2:.1f}")
print(f"Price 3 is {price3:.0f}")
'''





""" 
loyer = float(input("Entrez la loyer: "))
charge = float(input("Entrez la charge: "))
aide = float(input("Entrez l'aide au logement: "))
resources_mensuelles = 3760.0

total = (((loyer + charge - aide) / resources_mensuelles) * 100 )

print(f"Le total est = {total}")
"""



"""
email = "bro@gmail.com"

stop = email.index("@")
print(stop)

username = email[0:stop]
print(username)
"""


"""
username = input("Enter your username :\n")
username_length = len(username)
print(username_length)

if not username.isalpha():
    print("Error")
    exit()
else:
    print(f"welcome {username}")
"""
"""
if username_length >= 12 or username_length == 0:
    print("Error")
    exit()
else:
    print(f"The username is less than 12 characters, it contains ({username_length}) characters. ")

number_of_spaces = username.count(" ")

print(number_of_spaces)

spaces = username.find(" ")
if spaces == -1:
    print("no spaces found")
else:
    print("delete the spaces please")




print(f"There is {number_of_spaces} space(s) in the username" if number_of_spaces > 0 else "The username contains no spaces at all")

if number_of_spaces > 0:
    exit()

only_alpha_username = username.isalpha()

if only_alpha_username:
    print(f"your username : ( {username} ) IS VALID")
"""


















"""
name = input("Enter your full name : \n")


name_length = len(name)
print(name_length)

result = name.isalpha()

name = name.capitalize()
print(name)
print(result)


phone_number = input("Enter your phone number : ")

num_of_spaces = phone_number.count(" ")

phone_number = phone_number.replace(" ", "-")

print(num_of_spaces)
print(phone_number)

"""









"""
user = "limited"

site = "Allowed" if user == "full" else "Limited"

print(site)
"""















"""
Temperature = float(input("Enter the temperature's value :"))
Unit = input("Enter the unit : (C / F) ")

if  Unit == "C":
    Temperature = (Temperature * 9/5) + 32
    Unit = "°F"
elif Unit == "F":
    Temperature = (Temperature -32) * 5/9
    Unit = "°C"
else:
    print(f"{Unit} is invalid please rerun the program ")
    exit()

print(f"The temperature is : {round(Temperature,1)}{Unit}")
"""



"""
x = 96

print("Positive" if x>0 else "Negative")

if x > 0:
    print("Positive")
else:
    print("Negative")

result = "Even" if x%2 == 0 else "Odd"

print(result)


a = -8
b = -57


max_num = a if a >= b else b
min_num = a if a <= b else b

print(max(a,b))

print(max_num)
print(min_num)


user_role = "normal usqef^qf"

full_access = True if user_role == "admin" else False


print("full access" if full_access == True else "Limited access")

"""



"""
num1 = float(input("Enter the first value\n"))
num2 = float(input("Enter the second value\n"))
print("The first value will be used first then the second ")
operator = input("Choose between the following operators ( + , - , * , / , **)\n")
result1 = int
if operator == "+":
    result1 = (num1 + num2)
    #print(result1)
elif operator == "-":
    result1 = num1 - num2
    #print(result1)
elif operator == "*":
    result1 = num1 * num2
    #print(result1)
elif operator == "/":
    result1 = round(num1 / num2)
    #print(result1)
elif operator == "**":
    result1 = pow(num1 , num2)
    #print(result1)
else:
    print(f"ERROR : {operator} is not a valid operator ! ")
    exit()

print(f"{num1} {operator} {num2} = {result1}")
"""