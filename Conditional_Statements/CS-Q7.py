
value01 = input("enter the first vlaue")
value02 = input("enter the second vlaue")
value03 = input("enter the third vlaue")
value01 = int(value01)
value02 = int(value02)
value03 = int(value03)

if value01>value02 and value01>value03:
    print("the first value is greatest")
elif value02>value01 and value02>value03:
    print("the second value is greatest")
elif value03>value01 and value03>value02:
    print("the third value is greatest")
elif value01==value02==value03:
    print("all values are equal")
