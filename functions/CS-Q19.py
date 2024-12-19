def func(salaries):
    lenght = len(salaries)
    sum = 0
    for x in range(lenght):
        sum += salaries[x]
    return (sum/lenght)
value = [1232,123,3123,1231,1231]
ans = func(value)
print(ans)