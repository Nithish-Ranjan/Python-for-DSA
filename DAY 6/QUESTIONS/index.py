lst = [int(x) for x in input().split()]
target = int(input())
for i in range(len(lst)):
    if lst[i] == target:
        print("Element found at index : ", i)
        break
else:
    print("Element not found")