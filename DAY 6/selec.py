#Selection Sort
lst = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter an element: "))
    lst.append(element)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]

print("Sorted list:", lst)