class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def swap(self, x, y):
        if x == y:
            return

        prevX = None
        currX = self.head
        while currX and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX is None or currY is None:
            print("One or both elements not found")
            return

        if prevX:
            prevX.next = currY
        else:
            self.head = currY

        if prevY:
            prevY.next = currX
        else:
            self.head = currX

        currX.next, currY.next = currY.next, currX.next


ll = LinkedList()

n = int(input("Enter number of nodes: "))

for _ in range(n):
    ll.insert(int(input()))

print("Original Linked List:")
ll.display()

x = int(input("Enter first value to swap: "))
y = int(input("Enter second value to swap: "))

ll.swap(x, y)

print("Linked List after swapping:")
ll.display()