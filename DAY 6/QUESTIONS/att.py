lst = [int(x) for x in input().split()]
n = int(input())
count = 0
for i in lst:
    if n == i:
        count+=1
        
print(count)
