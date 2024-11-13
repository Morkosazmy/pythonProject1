import math
import time

'''-----vid 26: Dictionaries (MAPS) -----'''
capitals = {"USA":"Washington D.C", "China":"Beijing","Russia":"Moscow","France":"Paris","United Kingdom":"London"}

print(capitals)

capitals.update({"Egypt":"Cairo","Russia":"Mos"})

print(capitals)

capitals.update({"Russia":"Moscow"})

print(capitals)

print()

if capitals.get("Egypt"):
    print(capitals.get("Egypt"))

keys = capitals.keys()
values = capitals.values()
capitals.pop("Russia")
print(keys)
print(values)

capitals.pop("China")
print(capitals)
capitals.popitem()
print(capitals)
capitals.update({"Egypt":"Cairo"})
print(capitals)

keys = capitals.keys()
values = capitals.values()
print(keys)
print(values)

items = capitals.items()

for key, value in items:
    print(f"{key} : {value}")