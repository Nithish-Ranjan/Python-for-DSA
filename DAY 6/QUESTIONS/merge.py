list1 = [int(x) for x in input().split()]
list2 = [int(y) for y in input().split()]
optimal = []
i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        optimal.append(list1[i])
        i += 1
    else:
        optimal.append(list2[j])
        j += 1

while i < len(list1):
    optimal.append(list1[i])
    i += 1

while j < len(list2):
    optimal.append(list2[j])
    j += 1

print(optimal)