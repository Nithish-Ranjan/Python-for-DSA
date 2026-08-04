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

prev = None
current = head

while current is not None:
    nxt = current.next
    current.next = prev
    prev = current
    current = nxt

head = prev

print("Reversed Linked List:")
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
