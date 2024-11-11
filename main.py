# mini calculator

import math
import time
from asyncio import wait_for

'''vid 18 : for loops'''

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    if credit_card[4] == x or credit_card[9] == x or credit_card[14] == x:
        continue
    else:
        print(x)

for x in range(1,11):
    print(x)

#equivalent of
for x in range(0,10):
    print(x+1)