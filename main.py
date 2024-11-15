#List comprehension

doubles = [ x * 2 for x in range(1,11)]
triples = [ x * 3 for x in range(1,11)]
halves =  [ x / 2 for x in range(1,11)]
squares = [ pow(x,2) for x in range(1,11)]
#squares =[ (x ** 2 or x * x) for x in range(1,11)]
foods = ["apple", "banana", "mango", "pineapple", "Orange"]
print(foods)
foods = [food.upper() for food in foods]
# or
fruits = [fruit.upper() for fruit in ["apple", "banana", "mango", "pineapple", "Orange"]]
print(doubles)
print(triples)
print(halves)
print(squares)
print(foods)
print(fruits)

numbers = [1,2,3,4,5,6,-7,-8,-9,10,11,12,-13,14,-15,-16,17,18,19,20]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(numbers)
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)
grades = [86, 45, 32, 68, 48, 98, 90, 2, 32, 100, 59, 60]
print(grades)
passing_grades = [num for num in grades if num >= 60]
failing_grades = [num for num in grades if num <  60]
print(passing_grades)
print(failing_grades)