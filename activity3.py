def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

num1=int(input("Enter your first number: "))
num2=int(input("Enter your Second number: "))
print(f"\nThe addition of {num1} and {num2} is: ", addition(num1, num2))
print(f"\n The subtraction of {num1} and {num2} is: ", subtraction(num1, num2))
print(f"\n The multiplication of {num1} and {num2} is: ", multiplication(num1, num2))
print(f"\n The division of {num1} and {num2} is: ", division(num1, num2))