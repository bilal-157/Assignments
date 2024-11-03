
value = int(input("enter the number"))
ans = 0
while value!=0:
    x=value%10
    value = value//10
    ans = ans + x
print(ans)
