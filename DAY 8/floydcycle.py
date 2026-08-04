class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def detectLoop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

# Creating a loop
ll.head.next.next.next.next = ll.head.next

if ll.detectLoop():
    print("Loop Found")
else:
    print("No Loop")