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

if head is not None and head.next is not None:
    secondLast = None
    last = head

    while last.next:
        secondLast = last
        last = last.next

    secondLast.next = None
    last.next = head
    head = last

print("Linked List:")
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")