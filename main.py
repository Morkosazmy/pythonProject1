import random
from time import process_time_ns

#ROCK PAPER SCISSOR

print("Welcome to the rock paper scissor game ! ")

options = ["rock","paper","scissor"]
playing = True
while playing:
    computer = random.choice(options)
    player = input("Choose (rock, paper, scissor): ").lower()
    if player not in options:
        print("Invalid choice please chose again ! ")
    elif player == computer:
        print("Tie")
    elif player == "rock" and computer == "scissor" or player == "paper" and computer == "rock" or player == "scissor" and computer == "paper":
        print("You win ! ")
    else:
        print("You lose ! ")
    print(f"you choose : {player}")
    print(f"computer picked : {computer}")
    if not input("Would you like to play again ? (y/n) ").lower() == "y":
        playing = False
        break
    # elif player == "rock" and computer == "scissor":
    # elif player == "rock" and computer == "scissor":
print("Game Over ! ")
print("Thanks for playing ! ")