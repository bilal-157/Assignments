def find(temp,unit):
    if unit=="c" or unit=="C":
        result = (9.0/5.0) * temp  + 32
        return result
    elif unit=="f" or unit=="F":
        result = (5.0/9.0) * (temp - 32)
        return result
    else:
        return "Something Went Wrong..."
ans = find(96.7,"f")
print(ans)
    