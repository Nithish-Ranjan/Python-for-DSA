'''to calculate x power n using recursion'''
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print("5 raised to the power of 3:", power(5, 3))