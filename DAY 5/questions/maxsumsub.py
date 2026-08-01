n = int(input())
lst = list(map(int,input().split()))
max_sum = lst[0]
cur_sum = lst[0]
for i in range(1,n):
    cur_sum = max(lst[i],lst[i]+cur_sum)
    if cur_sum > max_sum:
        max_sum = cur_sum
print("MAX SUBARRAY SUM :",max_sum)