def anagrams(str1,str2):
    if len(str1) != len(str2):
        return False
    for char in str1:
        if char not in str2:
            return False
    return True
ans = anagrams("bilal","alabi")
print(ans)