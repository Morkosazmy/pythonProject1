import math
import time

'''-----vid 25: Quiz program ! -----'''

#name = input("Enter your name please : ")
question_number = 0
questions = ("How many elements are in the periodic table ?",
             "How many bones are in the human body ?",
             "Which of the following animals lays the biggest eggs ?",
             "Which of the following planets is the hottest in the solar system ?",
             "What is the most abundant gaz in the atmosphere ?")


options = (("A.115","B.116","C.117","D.118"),
           ("A.206","B.207","C.208","D.209"),
           ("A.Elephant","B.Crocodile","C.Whale","D.Ostrich"),
           ("A.Earth","B.Venus","C.Mars","D.Mercury"),
           ("A.Nitrogen","B.Carbon-Dioxide","C.Hydrogen","D.Oxygen"))

answers = ("D","A","D","B","C")
score = 0
guesses = []
print("Choose from (A, B, C or D)")
for question in questions:
    print(f"{question}")
    for option in options[question_number]:
        print(option)

    guess = input("Enter an answer (A, B, C, D)\n").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("Correct !")
    else:
        print("Incorrect !")
        print(f"The correct answer is : ({answers[question_number]})")
    question_number += 1

# now we gathered all the answers and can compare each to the correct answers !
fscore = 0
for x in range (0,5):
    if guesses[x] == answers[x]:
        print(f"Answer number {x+1} is correct ! ")
        fscore += 1
    else:
        print(f"Answer number {x+1} is incorrect !")

print(f"Your score is {score}/{len(questions)}")

if score == 5:
    print("PERFECT SCORE")
score = score / len(guesses) * 100

print(f"Your score is : {score}%")