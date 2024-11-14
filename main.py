#ITERABLES

numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d", "e"]
extra_numbers = (1, 2, 3, 4, 5)
fruits = {"Apple", "Orange", "Banana", "Pineapple", "Coconut"}
name = "full name"
my_dictionary = {"Morkos": 1, "Mark": 2, "Michael": 3, "Momo": 4}


for number in numbers:
    print(number)
print()

for letter in letters:
    print(letter)
print()
for extra_number in extra_numbers:
    print(extra_number)
print()

for fruit in fruits:
    print(fruit)
print()
for letter in name:
    print(letter, end="")
print()
print()

for key in my_dictionary.keys():
    print(key)
for value in my_dictionary.values():
    print(value)
for key, value in my_dictionary.items():
    print(f"{key} : {value}")
    print(key,value)