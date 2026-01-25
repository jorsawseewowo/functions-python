def mathematics(n):
    if n==1:
        return n
    else:
        return n*mathematics(n-1)
    
num = int(input("Enter a number: "))
if num<0:
    print("Sorry, we do not accept negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", mathematics(num))