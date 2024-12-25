#filter(function, collection) will return every element that pass a condition
def is_passing(grade):
    if grade >= 60:
        return True
    else:
        return False
grades = [56, 21, 48, 65, 98, 62, 28, 75, 41, 36, 22, 0, 8, 99, 100, 50, 51, 49, 86, 55, 67, 69]

passing_grades = list(filter(is_passing, grades))
passing_grades2 = list(filter(lambda grade: grade >= 60, grades))

print(passing_grades)
print(passing_grades2)