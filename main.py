#Lambda functions

double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y
is_even = lambda x: x % 2 == 0
full_name = lambda first_name, last_name: first_name + " " + last_name
#age_check = lambda x: f"{x} is over 18" if x >= 18 else "under age, ACCESS DENIED"
age_check = lambda x: True if x >= 18 else False

print(double(3))
print(double(4))
print()

print(add(3,2))
print(max_value(1,85))
print(min_value(1,85))
print(is_even(5))
print(is_even(100))
print(full_name("Mark", "Zuckerberg"))
print(age_check(5))
print(age_check(23))
