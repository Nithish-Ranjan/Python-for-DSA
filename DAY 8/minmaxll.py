class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    x = int(input("Enter data: "))
    new = Node(x)

    if head is None:
        head = new
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new

# Find minimum and maximum
temp = head
minimum = temp.data
maximum = temp.data

while temp is not None:
    if temp.data < minimum:
        minimum = temp.data

    if temp.data > maximum:
        maximum = temp.data

    temp = temp.next

print("Minimum =", minimum)
print("Maximum =", maximum)