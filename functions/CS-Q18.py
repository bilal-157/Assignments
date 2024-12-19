def func(str):
    count = {}
    for char in str:
        count[char] = count.get(char,0)+1
    return count
string = "bilal"
value = func(string)
print(value)