a = (input().split())
b = (input().split())
c = []
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in c:
        c.append(i)
        
print(" ".join(c))