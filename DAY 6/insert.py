#Insertion Sort
lst = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter an element: "))
    lst.append(element)

for i in range(1, n):
    key = lst[i]
    j = i - 1
    while j >= 0 and key < lst[j]:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key

print("Sorted list:", lst)