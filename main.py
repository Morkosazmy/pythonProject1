import random

dice = random.randint(1,6)
print(dice)

options = ["rock","paper","scissors"]

option = random.choice(options)
print(option)

# we can shuffle as well !

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] #in order to shuffle it has to be a List
# a Tuple won't work with the shuffle method


random.shuffle(cards)
print(cards)

#mini guessing game !

guesses = 0

low = 1
high = 100

random_number = random.randint(low, high)

while True:
    guess = int(input("Guess a number between 1 & 100: "))
    guesses += 1
    if guess > random_number:
        print(f"your guess ( {guess} ) is too high")
    elif guess < random_number:
        print(f"your guess ( {guess} ) is too low")
    else:
        print(f"({guess}) is the correct answer !")
        break
print(f"This round took you {guesses} guesses !")