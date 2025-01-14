#Multithreading

import threading
import time


def take_out_trash():
    print("You are taking out the trash")
    time.sleep(10)
    print("You took out the trash")

def do_laundry():
    print("You are doing the laundry")
    time.sleep(10)
    print("You did the laundry")

def wash_dishes():
    print("You are washing the dishes")
    time.sleep(4)
    print("You washed the dishes")

def get_mail():
    print("You are getting the mail")
    time.sleep(6)
    print("You got the mail")

def walk_dog(first_name, last_name):
    print(f"You are walking the dog {first_name} {last_name}")
    time.sleep(1)
    print(f"You walked the dog {first_name} {last_name}")

chore1 = threading.Thread(target=take_out_trash)
chore1.start()

chore2 = threading.Thread(target=do_laundry)
chore2.start()

chore3 = threading.Thread(target=wash_dishes)
chore3.start()

chore4 = threading.Thread(target=get_mail)
chore4.start()

chore5 = threading.Thread(target=walk_dog, args=("scooby","doo"))
chore5.start()

chore1.join()
chore2.join()
chore3.join()
chore4.join()
chore5.join()

print("All chores are finished")