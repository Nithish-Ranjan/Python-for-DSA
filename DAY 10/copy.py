stack1 = []
n = int(input("Enter number of elements: "))
print("Enter elements:")
for i in range(n):
    stack1.append(int(input()))

stack2 = stack1.copy()
print("Stack 1:", stack1)
print("Stack 2:", stack2)
