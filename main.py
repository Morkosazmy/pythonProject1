# mini calculator

#import math
import time

Timer = int(input("Enter time again "))

seconds = Timer % 60
minutes = int(Timer / 60) % 60
hours = round(Timer / 3600)

print(f"Your countdown starts at : {hours:02}:{minutes:02}:{seconds:02}")
#time.sleep(1)

for x in range (Timer,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = round(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!")