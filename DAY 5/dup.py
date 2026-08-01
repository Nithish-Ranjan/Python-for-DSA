lst = []
n = int(input())
for i in range(n):
    c = int(input())
    lst.append(c)
a= []
for i in range(n):
    for j in range(1,n):
        if lst[i] == lst[j]:
            a.append(lst[i])
            
print(a)