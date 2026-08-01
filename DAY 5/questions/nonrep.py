str = input()

lst = list(str)
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
    else:
        lst1.remove(i)
        
print(lst1[0])