'''merge 2 queue into single queue while preserving the order of elements'''

queue1 = []
queue2 = []
merged_queue = []

# Input for Queue 1
n1 = int(input("Enter the number of elements in Queue 1: "))

print("Enter Queue 1 elements:")
for i in range(n1):
    element = int(input())
    queue1.append(element)

# Input for Queue 2
n2 = int(input("\nEnter the number of elements in Queue 2: "))

print("Enter Queue 2 elements:")
for i in range(n2):
    element = int(input())
    queue2.append(element)

# Copy Queue 1 into merged_queue
for i in range(n1):
    merged_queue.append(queue1[i])

# Copy Queue 2 into merged_queue
for i in range(n2):
    merged_queue.append(queue2[i])

# Display Queue 1
print("\nQueue 1:")
for i in range(n1):
    print(queue1[i], end=" ")

# Display Queue 2
print("\nQueue 2:")
for i in range(n2):
    print(queue2[i], end=" ")

# Display Merged Queue
print("\nMerged Queue:")
for i in range(len(merged_queue)):
    print(merged_queue[i], end=" ")