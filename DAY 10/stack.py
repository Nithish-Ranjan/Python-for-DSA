class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print(self.stack.pop(), "popped from stack")

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack is not empty")

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i])

s = Stack()

while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Is Empty")
    print("6.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        x = int(input("Enter element: "))
        s.push(x)
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.peek()
    elif ch == 4:
        s.display()
    elif ch == 5:
        s.isEmpty()
    elif ch == 6:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
