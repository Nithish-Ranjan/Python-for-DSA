'''to compare 2 queue and determine they contain same element in same order'''
# Compare Two Queues

queue1 = []
queue2 = []

# Input for Queue 1
n1 = int(input("Enter the number of elements in Queue 1: "))

print("Enter Queue 1 elements:")
for i in range(n1):
    element = int(input())
    queue1.append(element)

# Input for Queue 2
n2 = int(input("\nEnter the number of elements in Queue 2: "))

print("Enter Queue 2 elements:")
for i in range(n2):
    element = int(input())
    queue2.append(element)

# Compare sizes
if n1 != n2:
    print("\nQueues are Not Equal")
else:
    equal = True

    # Compare each element
    for i in range(n1):
        if queue1[i] != queue2[i]:
            equal = False
            break

    if equal:
        print("\nQueues are Equal")
    else:
        print("\nQueues are Not Equal")