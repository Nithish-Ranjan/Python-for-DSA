n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
rot = int(input("Enter number of rotations:"))
a = rot%n
for i in range(a):
    b = lst[n-1]
    lst.remove(lst[n-1])
    lst.insert(0,b)
    
print(lst)