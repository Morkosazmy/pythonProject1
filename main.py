# mini calculator

import math

'''vid 17 : interest rate over the years'''
total = float
rate = float
time = float
initial = float

while True:
    initial = float(input("Enter the initial amount of money : "))
    if initial < 0:
        print("The initial value cant be a negative number !")
        initial = float(input("Enter the initial amount of money again : "))
    else:
        break

while True:
    rate = float(input("Enter the rate of interest in percentage (numbers only) : "))
    if rate < 0:
        print("The rate of interest cant be a negative number !")
        rate = float(input("Re-enter the rate of interest : "))
    else:
        break

while True:
    time = int(input("Enter the number of years for this investement : "))
    if time < 0:
        print("The time cant be a negative value !")
        time = int(input("Re-enter the time of years : "))
    else:
        break
total = initial * pow((1 + ( rate / 100 )),time)
print(f"Your initial total was : ${initial}")
print(f"The rate of interest is : {rate}%")
print(f"The number of years is : {time} year(s).")

print(f"Your balance after {time} year(s) is : ${total:.2f}")
