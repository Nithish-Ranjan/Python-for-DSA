lst = [int(x) for x in input().split()]
n = len(lst)
for i in range(n-1):
    min = i
    for j in range(i+1,n):
        if lst[j]<lst[min]:
            min = j
    lst[i],lst[min]=lst[min],lst[i]
print(lst)