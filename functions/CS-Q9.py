def palindrome(str):
    reverse_string = str[::-1]
    if str==reverse_string:
        return True
    return False

value = input("Enter the string")
ans = palindrome(value)
print(ans)
