'''to find sum of digits of a number using recursion'''
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

print("Sum of digits in 12345:", sum_of_digits(12345))