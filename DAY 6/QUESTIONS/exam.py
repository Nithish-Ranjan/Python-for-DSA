lst = [int(x) for x in input().split()]
maxi = lst[0]
for i in lst:
    if i>maxi:
        maxi = i
    
print(maxi)