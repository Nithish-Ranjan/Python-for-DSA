lst = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter an element: "))
    lst.append(element)
    
for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print("Sorted list:", lst)