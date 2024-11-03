
year = int(input("enter the year"))

if year%4==0:
    if year%100!=0:
        print("it is not a century year")
    else:
        if year%400==0:
            print("it is not a century year")
else:
    print("it is a century year")
            # TODO: write code...
        
