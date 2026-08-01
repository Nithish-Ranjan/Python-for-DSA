li = []
n = int(input("Enter the number of elements: "))
for i in range(1, n):
    element = int(input("Enter element: "))
    li.append(element)
    if li[i-1] % 2 == 0:
        print(f"{li[i-1]} is even")
    else:
        print(f"{li[i-1]} is odd")
        