lst = [int(x) for x in input().split()]
n = len(lst)
count = 0
for i in range(1,n-1):
    j = i-1
    k = lst[i]
    while j>=0 and lst[j] > k:
        lst[j+1]=lst[j]
        j-=1
        count+=1
    lst[j+1]=k
print(lst)
print(count)