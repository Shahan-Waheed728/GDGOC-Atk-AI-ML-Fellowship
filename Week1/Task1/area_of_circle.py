# python program to calculate the area of circle
def area():
    radius = int(input("Enter radius of circle:"))
    res = 3.14 * radius * radius
    return res
res = area()
print(f"Area of circle is ={res}")
