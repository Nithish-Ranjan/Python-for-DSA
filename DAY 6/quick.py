#Qucik Sort
lst = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter an element: "))
    lst.append(element)
    
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

sorted_list = quick_sort(lst)
print("Sorted list:", sorted_list)


