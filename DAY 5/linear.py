n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
    
key = int(input())
    
for i in range(n):
    if key == lst[i]:
        print("Ele found")
        break