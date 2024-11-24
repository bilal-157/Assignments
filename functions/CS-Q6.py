def count(str):
    str = str.lower()
    numbers = 0
    for x in str:
        vowels = ['a','e','i','o','u']
        for y in vowels:
            if x==y:
                numbers = numbers +1
    return numbers
value = input("Enter the String")
ans = count(value)
print(ans)
