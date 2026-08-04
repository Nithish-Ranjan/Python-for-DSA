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

slow = head
fast = head

while fast.next is not None and fast.next.next is not None:
    slow = slow.next
    fast = fast.next.next

head1 = head
head2 = slow.next
slow.next = None

print("First Half:")
temp = head1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

print("Second Half:")
temp = head2
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")