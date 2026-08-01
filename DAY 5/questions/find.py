n = int(input())
lst = list(map(int, input().split()))

i = 1

while i < n:
    if i != lst[i - 1]:
        print(i)
        break
    i += 1