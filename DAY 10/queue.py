queue = []

n = int(input("Enter number of elements to insert: "))

for i in range(n):
    x = int(input("Enter element: "))
    queue.append(x)      # Enqueue

print("Queue after enqueue:", queue)