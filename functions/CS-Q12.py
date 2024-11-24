person = {
    "first" : 2,
    "second" : 10,
    "third" : 90,
    "fourth" : 73
    
}
result = 0
for x in person:
    if person[x]>result:
        result = person[x]
print(result)