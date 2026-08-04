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

key = int(input("Enter node to delete: "))

if head is not None and head.data == key:
    head = head.next
else:
    prev = None
    temp = head

    while temp is not None and temp.data != key:
        prev = temp
        temp = temp.next

    if temp is None:
        print("Node not found")
    else:
        prev.next = temp.next

print("Linked List:")
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")