def fib(limit):
    if limit<0:
        return False
    first,second = 0,1
    result = [first]
    while second<limit:
        result.append(second)
        first,second = second,first+second
    return result
value = int(input("Enter the number"))
ans = fib(value)
print(ans)
