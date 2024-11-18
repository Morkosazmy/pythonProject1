# SLOTS GAME
import random


def spin_row(symbols):
    row = []
    for x in range(3):
        row.append(random.choice(symbols))
    print_row(row)
    multiplier = 0
    if row[0] == row[1] == row[2]:
        if row[0] == "💕":
            multiplier = 2
            return get_payout(multiplier)
        elif row[0] == "😘":
            multiplier = 3
            return get_payout(multiplier)
        elif row[0] == "👌":
            multiplier = 4
            return get_payout(multiplier)
        elif row[0] == "💖":
            multiplier = 5
            return get_payout(multiplier)
        else:
            print("JACKPOT")
            multiplier = 10
            return get_payout(multiplier)
    else:
        multiplier = 0
        return get_payout(multiplier)


def print_row(row):
    for symbol in row:
        print(symbol, end=" ")
    print()

def get_payout(multiplier):
    return multiplier

def main():
    balance = 100
    playing = True
    print("**********************")
    print("*****SLOT MACHINE*****")
    print("   💕  😘  👌  💖  🤩")
    print("**********************")
    symbols = ["💕", "😘", "👌", "💖", "🤩"]
    while playing:
        bet = int(input("Place your bet : "))
        if bet > balance:
            print("INSUFFICIENT FUNDS !")
        elif bet < 0:
            print("INVALID INPUT")
        elif balance == 0:
            playing = False
        else:
            balance -= bet
            bet *= spin_row(symbols)
            balance += bet
            print(f"Your balance is ${balance}")
            if balance == 0:
                print("You don't have any money left GAME OVER !")
                break
            continue
    print("Thank You For Playing !")


if __name__ == '__main__':
    main()