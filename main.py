#Banking program !
# withdraw, deposit, show balance !
from re import match


def show_balance(balance):
    print(f"${balance:.2f}")

def deposit(balance):
    amount = float(input("Insert the amount to be deposited : "))
    if amount <= 0:
        print("INVALID AMOUNT !")
        return 0
    else:
        #balance += amount
        print(f"${amount:.2f} have been successfully added to your bank account ! ")
        return amount

def withdraw(balance):
    amount = float(input("Insert the amount to be withdrawn : "))
    if amount < 0:
        print("INVALID AMOUNT !")
        return 0
    elif amount == 0:
        print("You cannot withdraw $0 please try again !")
        return 0
    elif amount > balance:
        print("Insufficient funds !")
        return 0
    else:
        return amount


def main():
    # we gotta have several options (withdraw, deposit, show balance)
    balance = 0
    print("******************************")
    print("******* BAKING PROGRAM *******")
    print("******************************")
    banking = True
    while banking:
        choice = input("1.Show balance \n2.Deposit \n3.Withdraw \n4.EXIT \n")
        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit(balance)
            case "3":
                balance -= withdraw(balance)
            case "4":
                print("Thank you for using the banking program. Good Bye !")
                banking = False
            case _:
                print("INVALID CHOICE")




if __name__ == '__main__':
    main()