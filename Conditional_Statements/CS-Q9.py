
side01 = input("enter first side of triangle ")
side02 = input("enter second side of triangle ")
side03 = input("enter third side of triangle ")

side01 = int(side01)
side02 = int(side02)
side03 = int(side03)

if side01 + side02 > side03 and side02 + side03 > side01 and side03 + side01 > side02:
    print("the given three side proves that the triangle is valid")
else:
    print("the triangle is not valid")
    # TODO: write code...
