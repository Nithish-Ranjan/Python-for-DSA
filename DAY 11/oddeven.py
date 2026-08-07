'''separate a elements of queue into even and odd'''

queue = []
even_queue = []
odd_queue = []

n = int(input("Enter the number of elements: "))

print("Enter queue elements:")

for i in range(n):
    element = int(input())
    queue.append(element)

# Separate elements
for i in range(n):
    if queue[i] % 2 == 0:
        even_queue.append(queue[i])
    else:
        odd_queue.append(queue[i])

# Display Original Queue
print("\nOriginal Queue:")
for i in range(n):
    print(queue[i], end=" ")

# Display Even Queue
print("\n\nEven Queue:")
for i in range(len(even_queue)):
    print(even_queue[i], end=" ")

# Display Odd Queue
print("\n\nOdd Queue:")
for i in range(len(odd_queue)):
    print(odd_queue[i], end=" ")