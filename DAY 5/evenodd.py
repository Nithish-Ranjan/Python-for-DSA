lst = []
e , o =0,0
n = int(input())
for i in range(n):
    lst.append(int(input()))
    
for i in range(n):
    if n%2 == 0:
        e+=1
    else:
        o+=1
        
print(o,e)