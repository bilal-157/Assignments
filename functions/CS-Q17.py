def not_duplicate(li):
    result = []
    for item in li:
        if item not in result:
            result.append(item)
    return result
ans = [1,2,3,3,4,4]
sol = not_duplicate(ans)
print(sol)