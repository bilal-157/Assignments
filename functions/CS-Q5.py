def check_prime(num):
    if num<=1:
        return True
    for x in range(2,(num//2)+1,1):
        if num%x==0:
            return False
    return True
    
value = int(input("Enter the number"))
ans = check_prime(value)
if not ans:
    print("Not Prime")
else:
    print("Prime")
