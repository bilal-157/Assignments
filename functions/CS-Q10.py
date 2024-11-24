def sum(num):
    sum = 0
    for x in num:
        if x%2==0:
            sum = sum + x
    return sum

question = [1,2,3,4]
ans = sum(question)
print(ans)
