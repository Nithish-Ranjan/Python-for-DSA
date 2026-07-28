# a = int(input())

# if a>0:
#     print("positive")
# elif a<0:
#     print("negative")
# else:
#     print("zero")
    
    
    
# a = int(input())
# if a%5==0:
#     print("divisible by 5")

# a = int(input())
# b = int(input())
# c = int(input())

# if a>b:
#     if a>c:
#         print("a is greatest")
#     else:
#         print("c is largest")
        
# else:
#     if b>c:
#         print("b is greatest")
#     else:
#         print("c is greatest")


#leap year or not
a = int(input("enter year"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("leap year")
        else:
            print("not leap year")