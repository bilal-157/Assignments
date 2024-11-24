def calculate_radius(r):
    pi = 3.14
    return 2*pi*(r**r)
radius = float(input("enter the radius of the cirle : "))
ans = calculate_radius(radius)
print(ans)