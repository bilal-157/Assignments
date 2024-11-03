
side01 = input("enter the first side of triangle")
side02 = input("enter the second side of triangle")
side03 = input("enter the thirdside of triangle")

side01 = int(side01)
side02 = int(side02)
side03 = int(side03)

if side01==side02==side03:
    print("the triangle is equilateral")
elif side01==side02 or side01==side03 or side02==side03:
    print("the triangle is isoscles")
else:
    print("the triangle is scalene")
