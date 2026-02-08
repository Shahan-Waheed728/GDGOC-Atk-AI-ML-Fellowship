# python program to create reusable utility function
def average():
    return (a + b) / 2   
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
result = average()
print(f"Average of {a} and {b} is = {result}")