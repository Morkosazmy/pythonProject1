import math
import time

'''-----vid 23: 2D Collections ! -----'''

fruits = ["Mango", "Pineapple", "Banana", "Apple", "Watermelon"]
vegetables = ["Cucumber", "Tomato", "Onion", "Cabbage", "Eggplant"]
meats = ["Beef", "Chicken", "Pork", "Fish"]

groceries = [fruits, vegetables, meats]

# OR

groceries2 = [["Mango", "Pineapple", "Banana", "Apple", "Watermelon"],
              ["Cucumber", "Tomato", "Onion", "Cabbage", "Eggplant"],
              ["Beef", "Chicken", "Pork", "Fish"]]

# grocerie2 is the same as groceries.

for row in groceries:
    for column in row:
        print(column, end=" ")
    print()

print()

for line in groceries2:
    for food in line:
        print(food, end=" ")
    print()

#The 2 for loops are identical.


"""----- 2D KEYPAD -----"""
"""
num_pad = (( 1 , 2 , 3 ),
          ( 4 , 5 , 6 ),
          ( 7 , 8 , 9 ),
          ("#", 0 ,"*"))
#num_pad is a Tuple of Tuples
#Print the numpad.

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()
"""
