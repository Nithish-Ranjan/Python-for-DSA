lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
    
for i in range(n):
    if lst[i] == 0:
        lst.remove(lst[i])
        lst.append(0)
        
print(lst)