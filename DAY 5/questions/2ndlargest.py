lst = []
n = int(input("Enter number of elements: "))
for i in range(n):
    lst.append(int(input()))
max1 = lst[0]
max2 = lst[0]

for i in range(1, n):
    if lst[i] > max1:
        max2 = max1
        max1 = lst[i]
    elif lst[i] > max2:
        max2 = lst[i]

print("Second largest:", max2)