
import mymath

total = 0
calculating = True
while calculating:
    minutes = int(input("Add minutes : "))
    total += minutes * 60
    print(total)
    stop = input("Stop ? (y/n)")
    if stop == "y" or stop == "Y":
        calculating = False
calculating = True
while calculating:
    seconds = int(input("Add seconds : "))
    total += seconds
    print(total)
    stop = input("Stop ? (y/n)")
    if stop == "y" or stop == "Y":
        calculating = False

time_sec = total % 60
time_minute = int(total / 60) % 60
time_hour = int(total / 3600)

print(f"time : {time_hour}:{time_minute}:{time_sec}")