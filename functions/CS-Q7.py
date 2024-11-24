def greatest(num):
    num.sort()
    return num[-1]
value = [1,23,4,3,52,32]
ans = greatest(value)
print(ans)
