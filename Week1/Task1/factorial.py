# python program to calculate factorial of given number
def factorial(num):   
   if num == 1 or num ==0:
    return 1
   return num * factorial(num-1) 
num = int(input("Enter number:"))  
res = factorial(num)
print(f"Factorial of {num} is = {res}")