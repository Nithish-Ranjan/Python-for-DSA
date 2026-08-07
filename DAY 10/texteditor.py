stack = []
text = ""

while True:
    print("\n----- Text Editor -----")
    print("1. Add Text")
    print("2. Display Text")
    print("3. Undo")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        stack.append(text)          # Save current state
        new_text = input("Enter text: ")
        text = text + new_text
        print("Text added successfully.")

    elif choice == 2:
        if text == "":
            print("Editor is empty.")
        else:
            print("Current Text:", text)

    elif choice == 3:
        if len(stack) == 0:
            print("Nothing to undo.")
        else:
            text = stack.pop()
            print("Undo successful.")

    elif choice == 4:
        print("Exiting Text Editor...")
        break

    else:
        print("Invalid Choice") 