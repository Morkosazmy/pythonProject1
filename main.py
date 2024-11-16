#CREDIT CARD VALIDATOR :
#1. Remove any '-' or ' '
#2. Add all digits in the odd places from right to left
#3. Double every second digit from right to left
#           (If result is a two-digit number,
#            add the twi-digit numbers together to get a single digit)
#4. Sum the totals of step 2 & 3
#5. If sum is divisible by 10, the credit card number is valid
#from curses.ascii import isdigit
#from idlelib.replace import replace

#organized version
credit_card_number = input("Enter the credit card's number : ")
credit_card_number = credit_card_number.replace("-", "")
credit_card_number = credit_card_number.replace(" ", "")
credit_card_number = credit_card_number[::-1]

total = 0

for num in credit_card_number[::2]: # odd numberss
    #print(num)
    total += int(num)

for num in credit_card_number[1::2]:
    x = int(num) * 2
    if x >= 10:
        two_digit = str(x)
        total +=  int(two_digit[0]) + int(two_digit[1])
    else:
        total += x

if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")









"""
credit_card = input("Enter the credit card number : ")

credit_card = credit_card.replace("-","")
credit_card = credit_card.replace(" ","")

print(credit_card)
odd_places = []
even_places = []
print(len(credit_card)) # length is the literal amount of characters !

if len(credit_card) % 2 == 0:
    for x in range(1, len(credit_card), 2):  # we can run through the credit card in reverse !
        #print(credit_card[x],end="")
        odd_places.append(credit_card[x])
    for x in range(0, len(credit_card), 2):
        #print(credit_card[x],end="")
        even_places.append(credit_card[x])
else:
    for x in range(0, len(credit_card), 2):
        #print(credit_card[x],end="")
        odd_places.append(credit_card[x])
    for x in range(1, len(credit_card), 2):  # we can run through the credit card in reverse !
        #print(credit_card[x],end="")
        even_places.append(credit_card[x])



def sum_of_double_digit(x):
    x = str(x)
    total_two_digits = 0
    for index in range(len(x)):
        total_two_digits += int(x[index])
    return str(total_two_digits)



print(f"odd_places : {odd_places}")
print(f"even_places : {even_places}")
int_even_nums_doubled = []

for num in range(0,len(even_places)):
    if int(even_places[num]) * 2 < 10:
        int_even_nums_doubled.append(int(even_places[num]) * 2)
    else:
        #x = sum_of_double_digit(str(int(even_places[num]) * 2))
        int_even_nums_doubled.append((int(even_places[num]) * 2))

int_even_nums_after_double = []
for num in range(0,len(even_places)):
    if int(even_places[num]) * 2 < 10:
        int_even_nums_after_double.append(int(even_places[num]) * 2)
    else:
        #x = sum_of_double_digit(str(int(even_places[num]) * 2))
        int_even_nums_after_double.append(sum_of_double_digit(str(int(even_places[num]) * 2)))
print(f"int_even_nums_doubled : {int_even_nums_doubled}")
print(f"int_even_nums_after_double : {int_even_nums_after_double}")
odd_places_reversed = []

for num in range(len(odd_places)-1, -1, -1):
    odd_places_reversed.append(odd_places[num])

print(f"odd_places_reversed : {odd_places_reversed}")
total_odd_numbers = 0
for num in odd_places_reversed:
    total_odd_numbers += int(num)
print(f"total_odd_numbers : {total_odd_numbers}")
# so the problem here is that it gets the index of the first integer of that value (example 111 will only get index 0
# cause the first 1 is at index 0

total_even_numbers = 0

for num in int_even_nums_after_double:
    print(num,end=" ")
    total_even_numbers += int(num)
print()
print(f"total_even_numbers : {total_even_numbers}")
#two_digits = input("Enter a double digit: ")
#print(sum_of_double_digit(two_digits))

# we need to sum the even numbers and the odd numbers now !
grand_total = total_even_numbers + total_odd_numbers

print(f"grand_total = {grand_total}")

if grand_total % 10 == 0:
    print("Valid")
else:
    print("Invalid card ! ")

# I can't believe I actually did that lol ( messy as hell but still it works, gotta make functions
# and organize it later )
"""