def find_power(value,power):
    result = 1
    for x in range(abs(power)):
        result = value * result
    if power<0:
        result = 1/result
    return result
ans = find_power(2,-3)
print(ans)