'''rotate a queue by k position '''
# Rotate Queue by K Positions

queue = []

n = int(input("Enter the number of elements: "))

print("Enter queue elements:")
for i in range(n):
    element = int(input())
    queue.append(element)

k = int(input("Enter K value: "))

# If K is greater than queue size
k = k % n

# Rotate the queue
for i in range(k):

    first = queue[0]

    # Shift elements to the left
    for j in range(n - 1):
        queue[j] = queue[j + 1]

    # Place first element at the end
    queue[n - 1] = first

print("\nQueue after rotation:")

for i in range(n):
    print(queue[i], end=" ")