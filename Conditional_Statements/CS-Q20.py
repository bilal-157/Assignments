
value = int(input("enter the number"))

def func(num):
    if num <=1:
        return False
    else:
        for x in range(2,(num//2)+1):
            if num%x==0:
                return False
        return True
if func(value):
    print("number is prime")
else:
    print("not prime")