str = input()
lst = list(str)
count =0
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
        count+=1
    else:
        break
    
print(count)