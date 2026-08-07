stack = []

n = int(input("Enter number of elements: "))

print("Enter elements:")
for i in range(n):
    stack.append(int(input()))

print("Original Stack:", stack)

while len(stack) > 0:
    stack.pop()

print("Stack after deleting all elements:", stack)