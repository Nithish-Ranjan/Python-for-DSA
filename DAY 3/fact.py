def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
n = int(input("Enter a number to find its factorial: "))
result = fact(n)
print(f"The factorial of {n} is: {result}")