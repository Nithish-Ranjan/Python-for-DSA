lst = [int(x) for x in input().split()]
n = len(lst)
for i in range(n-1):
    max = i
    for j in range(i+1,n):
        if lst[j]>lst[max]:
            max = j
    lst[i],lst[max]=lst[max],lst[i]
print(lst)