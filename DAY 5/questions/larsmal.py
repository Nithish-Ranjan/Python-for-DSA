lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
    
mini = lst[0]
maxi = lst[0]
for i in range(n):
    if mini > lst[i]:
        mini = lst[i]
    if maxi < lst[i]:
        maxi = lst[i]
        
print("max = ",maxi," min = ",mini)