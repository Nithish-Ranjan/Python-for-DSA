'''to implement a customer servic queue 
1.add customer
2.servie customer 
3.waiting customer
4.display front customer
5.total customers'''
# Customer Service Queue

queue = []

while True:

    print("\n----- Customer Service Queue -----")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Display Waiting Customers")
    print("4. Display Front Customer")
    print("5. Display Total Customers")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Customer
    if choice == 1:

        customer = input("Enter Customer Name: ")
        queue.append(customer)
        print(customer, "added to the queue.")

    # Serve Customer
    elif choice == 2:

        if len(queue) == 0:
            print("No customers to serve.")

        else:
            print(queue[0], "has been served.")

            # Shift elements to the left
            for i in range(len(queue) - 1):
                queue[i] = queue[i + 1]

            queue.pop()

    # Display Waiting Customers
    elif choice == 3:

        if len(queue) == 0:
            print("No waiting customers.")

        else:
            print("Waiting Customers:")

            for i in range(len(queue)):
                print(queue[i])

    # Display Front Customer
    elif choice == 4:

        if len(queue) == 0:
            print("Queue is Empty")

        else:
            print("Front Customer:", queue[0])

    # Display Total Customers
    elif choice == 5:

        print("Total Customers:", len(queue))

    # Exit
    elif choice == 6:

        print("Thank You!")
        break

    else:
        print("Invalid Choice")