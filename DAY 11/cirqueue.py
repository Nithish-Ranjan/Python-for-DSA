'''circular queue using list and operations of enqueue and dequeue'''
size = int(input("Enter size of circular queue: "))

queue = [None] * size
front = -1
rear = -1

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        if (front == 0 and rear == size - 1) or (front == rear + 1):
            print("Queue Overflow")

        else:
            x = int(input("Enter element: "))

            if front == -1:
                front = rear = 0
            elif rear == size - 1:
                rear = 0
            else:
                rear += 1

            queue[rear] = x
            print("Inserted:", x)

    elif ch == 2:
        if front == -1:
            print("Queue Underflow")

        else:
            print("Deleted:", queue[front])

            if front == rear:
                front = rear = -1
            elif front == size - 1:
                front = 0
            else:
                front += 1
    elif ch == 3:
        if front == -1:
            print("Queue is Empty")
        else:
            print("Queue Elements:", end=" ")
            if front <= rear:
                for i in range(front, rear + 1):
                    print(queue[i], end=" ")
            else:
                for i in range(front, size):
                    print(queue[i], end=" ")
                for i in range(0, rear + 1):
                    print(queue[i], end=" ")
            print()
    elif ch == 4:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")