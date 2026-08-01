lst = [int(x) for x in input().split()]
n = int(input())
dict = {}
for i in lst:
    dict[i] = dict.get(i,0)+1
    
print(dict.get(n,0))