
def func(num):
    if num<=1:
        return False
    for i in range(2,(num//2)+1):
        if num%i==0:
            return False
    return True
    
for x in range(2,51):
    if func(x):
        print(f"{x} is prime")

