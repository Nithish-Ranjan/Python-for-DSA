lst = [int(x) for x in input().split()]
lst = lst[::-1]
n = int(input())
for i in range(len(lst)):
    if n == lst[i]:
        print(len(lst)-1-i)
        break
    