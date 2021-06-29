
import time

for i in range(10):
    print(i+1)

for i in range(50,60+1,2): #range(start, stop, step)
    print(i)

for i in "Samuel Mrazik":
    print(i)

for seconds in range(10, 0, -1): #counting from 10 to 0 due to -1 step
    print(seconds)
    time.sleep(1)
print("Happy New Year!")