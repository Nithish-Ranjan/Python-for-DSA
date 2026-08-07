stack = []

n = int(input("Enter number of elements: "))

print("Enter elements:")
for i in range(n):
    stack.append(int(input()))

print("Original Stack:", stack)

temp = []
while len(stack) > 0:
    temp.append(stack.pop())
stack = temp
print("Reversed Stack:", stack)