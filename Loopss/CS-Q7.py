
value = input("enter the number")
value = int(value)

ans = 1
if value==0 or value==1:
    print(1)
else:
    while value>1:
      ans = ans * value
      value = value-1
    print(ans)
