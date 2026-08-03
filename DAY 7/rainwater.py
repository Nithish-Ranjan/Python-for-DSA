
n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

left = 0
right = n - 1

leftmax = 0
rightmax = 0
water = 0

while left < right:
    if a[left] < a[right]:
        if a[left] >= leftmax:
            leftmax = a[left]
        else:
            water += leftmax - a[left]
        left += 1
    else:
        if a[right] >= rightmax:
            rightmax = a[right]
        else:
            water += rightmax - a[right]
        right -= 1

print(water)