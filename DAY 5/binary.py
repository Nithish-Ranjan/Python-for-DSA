lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
lst = sorted(lst)
key = int(input())
st = 0
end = n-1
while st<=end:
    mid = (end + st)//2
    if key == lst[mid]:
        print("Element found at loc ",mid)
        break
    elif key<lst[mid]:
        mid = end -1
    else:
        mid = st+1
    
