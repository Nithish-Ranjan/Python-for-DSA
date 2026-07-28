a = int(input("enter number 1:")) 
b = int(input("enter number 2:"))
op = input("enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")