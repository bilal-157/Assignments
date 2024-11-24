def GCD(n1, n2):
    if not n1 or not n2: 
        return False
    
    result = 1
    for i in range(1, min(n1, n2) + 1):  
        if n1 % i == 0 and n2 % i == 0:
            result = i  
    return result

value1 = int(input("Enter the first number: "))
value2 = int(input("Enter the second number: "))
ans = GCD(value1, value2)
print(ans)
