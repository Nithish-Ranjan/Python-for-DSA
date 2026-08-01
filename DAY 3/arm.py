n = int(input("Enter the number: "))
a = len(str(n))
sum = 0
for i in range(a):
    digit = n % 10
    n = n // 10
    arm = digit ** a
    sum += arm
if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")