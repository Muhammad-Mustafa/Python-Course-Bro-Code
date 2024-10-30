# for loop is a loop which iterate the block of code with a limited number of time

import time

for i in range(10):
    print(i)

for i in range(12, 20 + 1):
    print(i)

for i in range(2, 20 + 1, 2):
    print(i)

for i in "Muhammad Mustafa":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("happy New year")
