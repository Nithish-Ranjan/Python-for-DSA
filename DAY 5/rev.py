lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
  
st = 0
end = n-1  
while st <= end:
    temp = lst[st]
    lst[st] = lst[end]
    lst[end] = temp
    st +=1
    end -=1
print(lst)