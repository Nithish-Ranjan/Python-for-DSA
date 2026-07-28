
a = int(input())
num = 0
while a>0:
    i=a%10
    num = num + i
    a = a//10
    
print(num)