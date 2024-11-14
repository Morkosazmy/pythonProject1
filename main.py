import time


def count(end, start = 0): #put start at the end because it has a default and a non default variable must be addressed before the defaulted one
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE !")



#count(10,5)
#count(7)

def hello( greeting, title, firstname, lastname):
    print(f"{greeting} {title}{firstname} {lastname} !")

hello("Hello", lastname= "Squarepants",firstname="Spongebob", title= "Mr.")
hello("Hello", "Mr.", "Spongebob", lastname="Squarepants")

def net_price(list_price,discount = 0,tva = 20): # insert the discount & TVA in percentage without typing the % symbol
    final_price = list_price * (1 - (discount/100)) * (1 + (tva/100))
    return final_price

#goofy code where i separate the number in 2s instead of just typing them
def get_number(country, carrier, rest_of_number):
    rest_of_number = list(rest_of_number)
    rest_of_number = rest_of_number[0] , rest_of_number[1] , rest_of_number[2] , rest_of_number[3] , rest_of_number[4] , rest_of_number[5] , rest_of_number[6] , rest_of_number[7]
    rest_of_number = f"{rest_of_number[0]}{rest_of_number[1]} {rest_of_number[2]}{rest_of_number[3]} {rest_of_number[4]}{rest_of_number[5]} {rest_of_number[6]}{rest_of_number[7]}"
    return f"{country} {carrier} {rest_of_number}"

print(get_number("+33", carrier= "1",rest_of_number= "23456789"))

print(net_price(500))
print(net_price(500,20))
print(net_price(500,20,0))
print(net_price(500,0,0))
