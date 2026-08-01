str = input()
lst = str.split()
lent = 0
a = ""
for i in lst:
    if len(i)>lent:
        lent = len(i)
        a = i
print(a)
