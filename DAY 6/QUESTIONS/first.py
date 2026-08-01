lst = [int(x) for x in input().split()]
n = int(input())
for i in range(len(lst)):
    if lst[i] == n:
        print(i)
        break