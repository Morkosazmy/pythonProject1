#Date And Time

import datetime
from time import strftime

date = datetime.date(2025, 1, 7)
day = datetime.date.today()

time = datetime.time(22, 12, 00)
now = datetime.datetime.now()

now2 = now.strftime("%H:%M:%S / %d-%m-%Y")

target_datetime = datetime.datetime(2025, 1, 7, 00, 00, 1)

current_datetime = datetime.datetime.now()

print(date)
print(day)
print(time)
print(now)
print(now2)

if target_datetime < current_datetime:
    print("Target date time has passed")
else:
    print("Target date time has NOT passed")
