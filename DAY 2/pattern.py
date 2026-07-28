#pattern to print right angle triangle

# n=int(input("Enter n "))
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print('*',end=" ")
#     print( )

#pattern to print reverse right angle triangle
# n = int(input("Enter n "))
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print('*', end=" ")
#     print()
    
    
# n = int(input("Enter n "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


n = int(input("Enter n "))
for i in range(n,):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()