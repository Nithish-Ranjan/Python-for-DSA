n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
b = 0
for i in range(n-1):
    for j in range(i+1,n):
        if k==a[i]+a[j]:
            print(a[i],a[j])
            
