import time

value = int(input("enter the value"))

for x in range(value-1,-1,-1):
    print(x)
    time.sleep(1)
print("END")