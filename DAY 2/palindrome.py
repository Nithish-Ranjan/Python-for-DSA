#palindrome

# n = int(input("Enter n "))
# temp = n
# rev = 0
# while n>0:
#     i = n%10
#     rev = rev * 10 + i
#     n = n//10
    
# if(temp==rev):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#armstrong number
n = int(input("Enter n "))
temp = n
sum = 0
while n>0:
    i = n%10
    sum = sum + (i**3)
    n = n//10

if(temp==sum):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")