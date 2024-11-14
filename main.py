#membership operators
from itertools import count

word = "APPLE"

letter = input("Guess the letter in the secret word : ")

if letter in word:
    amount = word.count(letter)
    print(f"The letter {letter} exists in the secret message {amount} times !")
else:
    print(f"The letter {letter} does NOT exist in the secret message !")

grades = {"sandy" : "C",
          "spongebob" : "B",
          "squidward" : "A",
          "patrick" : "D",
          "plankton" : "F"}

name = input("Enter the name for which the grade is desired : ")
if name not in grades:
    print("There was no student with that name ! ")
else:
    print(f"the student {name} got the grade {grades[name]}")

email = input("Insert an email : ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")