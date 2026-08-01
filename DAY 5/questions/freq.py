str = input()
lst = list(str)
key = input()
count =0
n = len(lst)
for i in range(n):
    if key == lst[i]:
        count+=1
        
print(count)