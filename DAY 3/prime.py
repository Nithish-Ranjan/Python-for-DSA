import math
n = int(input("Enter the number: "))
for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")