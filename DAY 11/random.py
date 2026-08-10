import random

size = 5
queue = [None] * size

front = -1
rear = -1

# Enqueue
def enqueue():
    global front, rear

    if (rear + 1) % size == front:
        print("Queue is Full")
        return

    value = random.randint(1, 100)

    if front == -1:
        front = 0

    rear = (rear + 1) % size
    queue[rear] = value

    print("Inserted:", value)


# Dequeue
def dequeue():
    global front, rear

    if front == -1:
        print("Queue is Empty")
        return

    value = queue[front]
    print("Deleted:", value)

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size


# Display
def display():
    if front == -1:
        print("Queue is Empty")
        return

    print("Queue:", end=" ")

    i = front

    while True:
        print(queue[i], end=" ")

        if i == rear:
            break

        i = (i + 1) % size

    print()


# Main program
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid choice")