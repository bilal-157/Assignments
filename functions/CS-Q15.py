def flatten_list(li):
    result = []
    for item in li:
        if isinstance(item,list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
question = [1,[2,3,4]]
ans = flatten_list(question)
print(ans)