#map(function, collection)

def c_to_f(temp):
    return (temp * 9/5) + 32

celsius_temps = [0.0, 32.0, 18.0, 55.0, 45.0, -8.0, -60.0, 100.0]

fahrenheit_temps = list(map(c_to_f, celsius_temps))

fahrenheit_temps2 = list(map(lambda temp: (temp * 9/5) + 32, celsius_temps))

print(celsius_temps) # Prints a list of temps in Celsius

print(fahrenheit_temps) # Prints a list of temps in fahrenheit

for temp in fahrenheit_temps2:
    print(temp)
#Prints a temperature for each line