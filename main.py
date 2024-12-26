# .sort() or sorted() (Sorting lists, tuples, dictionaries and objects)

#list

fruits = ["banana", "orange", "apple", "coconut", "pineapple"]

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

#tuple
fruits2 = ("banana", "orange", "apple", "coconut", "pineapple")

fruits2 = sorted(fruits2)

print(fruits2)

fruits2 = list(fruits2)

print(fruits2)
fruits2.sort(reverse=True)
print(fruits2)

print()
print()
#dictionary
fruit_cal = {"banana" : 120, "apple" : 160, "pineapple" : 250, "coconut" : 340, "orange" : 80}
#1
#sort by name and don't show values of calories.
print()
fruit_cal = sorted(fruit_cal)
print(fruit_cal)

#2
#sort by name in reverse and don't show values of calories.
print()
fruit_cal = sorted(fruit_cal, reverse=True)
print(fruit_cal)

#3
# Sorted by names while showing the whole item (name, value "calories" )
print()
fruit_cal = {"banana" : 120, "apple" : 160, "pineapple" : 250, "coconut" : 340, "orange" : 80}
fruit_cal = dict(sorted(fruit_cal.items()))
print(fruit_cal)

#4
# Sorted by names while showing the whole item (name, value "calories" ) in reverse order of names
print()
fruit_cal = {"banana" : 120, "apple" : 160, "pineapple" : 250, "coconut" : 340, "orange" : 80}
fruit_cal = dict(sorted(fruit_cal.items(), reverse= True))
print(fruit_cal)

#5
#Sort by calories ( value ) in ascending order
print()
fruit_cal = {"banana" : 120, "apple" : 160, "pineapple" : 250, "coconut" : 340, "orange" : 80}
fruit_cal = dict(sorted(fruit_cal.items(),key= lambda item: item[1]))
print(fruit_cal)

#6
#Sort by calories ( value ) in descending order
print()
fruit_cal = {"banana" : 120, "apple" : 160, "pineapple" : 250, "coconut" : 340, "orange" : 80}
fruit_cal = dict(sorted(fruit_cal.items(),key= lambda item: item[1], reverse= True))
print(fruit_cal)
print()
print()
# sorting objects !
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name} : {self.calories}"

print()
fruit_objs = [Fruit("banana", 105),
              Fruit("orange", 73),
              Fruit("apple", 72),
              Fruit("coconut", 354)]

fruit_objs = sorted(fruit_objs, key = lambda fruit: fruit.name)
print(fruit_objs)


print()
fruit_objs = [Fruit("banana", 105),
              Fruit("orange", 73),
              Fruit("apple", 72),
              Fruit("coconut", 354)]

fruit_objs = sorted(fruit_objs, key = lambda fruit: fruit.name, reverse= True)
print(fruit_objs)


print()
fruit_objs = [Fruit("banana", 105),
              Fruit("orange", 73),
              Fruit("apple", 72),
              Fruit("coconut", 354)]

fruit_objs = sorted(fruit_objs, key = lambda fruit: fruit.calories)
print(fruit_objs)


print()
fruit_objs = [Fruit("banana", 105),
              Fruit("orange", 73),
              Fruit("apple", 72),
              Fruit("coconut", 354)]

fruit_objs = sorted(fruit_objs, key = lambda fruit: fruit.calories, reverse= True)
print(fruit_objs)