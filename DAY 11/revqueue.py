'''reverse a queue'''
queue = []
n = int(input("Enter the number of elements: "))
print("Enter queue elements:")
for i in range(n):
    element = int(input())
    queue.append(element)
print("Original Queue:")
for i in range(n):
    print(queue[i], end=" ")
reverse_queue = []
for i in range(n - 1, -1, -1):
    reverse_queue.append(queue[i])
print("\nReversed Queue:")
for i in range(n):
    print(reverse_queue[i], end=" ")