year = int(input("enter the year"))

if year%4==0:
    if year%100!=0:
        print("it is a leap year")
    else:
        if year%400==0:
            print("it is a leap year")
else:
    print("not a leap year")
            # TODO: write code...
