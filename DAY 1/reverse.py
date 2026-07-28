#reverse a number

a = int(input())
num = 0
while a>0:
    i=a%10
    num = num * 10 + i
    a = a//10
    
print(num)