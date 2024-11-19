#Hangman game

import random

words = ("banana", "orange", "apple", "pineapple", "kiwi", "pear", "watermelon", "passion"
         ,"world","affair","beneath","inspire","beautiful","butterfly","insect","coconut","peanut",
         "stomach","wizard","gigantic","satisfy","admire","earth","perfect","ambition","success") # should import more words !

hangman_art = {0:("   ",
                  "   ",
                  "   ",),
             1:(  " o ",
                  "   ",
                  "   "),
             2:(  " o ",
                  " | ",
                  "   "),
             3:(  " o ",
                  "/| ",
                  "   "),
             4:(  " o ",
                  "/|\\",
                  "   "),
             5:(  " o ",
                  "/|\\",
                  "/  "),
             6:(  " o ",
                  "/|\\",
                  "/ \\")}


def display_hangman(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    is_running = True
    guessed_letters = set()

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("INVALID INPUT")
            continue

        if guess in guessed_letters:
            print(f"your guess {guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range (len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("YOU WIN !")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE")
            is_running = False

if __name__ == '__main__':
    main()