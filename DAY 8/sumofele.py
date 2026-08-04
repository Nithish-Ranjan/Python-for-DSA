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
        while temp.next:
            temp = temp.next
        temp.next = new

sum = 0
temp = head

while temp:
    sum += temp.data
    temp = temp.next

print("Sum =", sum)


