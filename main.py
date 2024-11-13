import random
print("Dice roller game ! ")

print("\u25CF \u250C \u2510 \u2500 \u2502 \u2514 \u2518 ")
# ● ┌ ┐ ─ │ └ ┘
dice_art = {1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│ ●       │",
                "│         │",
                "│       ● │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│ ●       │",
                "│    ●    │",
                "│       ● │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│ ●     ● │",
                "│         │",
                "│ ●     ● │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│ ●     ● │",
                "│    ●    │",
                "│ ●     ● │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│ ●     ● │",
                "│ ●     ● │",
                "│ ●     ● │",
                "└─────────┘"),
                }


dice = []
total = 0

num_dice = int(input("How many dice would u like to throw ?"))

for x in range(num_dice):
    dice_roll = random.randint(1,6)
    #print(dice_roll)
    dice.append(dice_roll)
    total += dice_roll

#print(total)
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="  ")
    print()

print(f"your total is {total}")
    #print(dice_art.get(1)[line])