#Execution Time

import time

start_time = time.perf_counter()

for i in range(100000000):
    pass

end_time = time.perf_counter()

elapsed_time = end_time - start_time #the difference in time is the time it took to execute

print(f"elapsed time is :{elapsed_time:.3f} seconds")
