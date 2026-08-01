lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
    
r = []
for i in range(n):
    if lst[i] not in r:
        r.append(lst[i])
print(r)