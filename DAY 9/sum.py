'''find sum of first N natural numbers using recursion'''
def sum_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n - 1)

print("Sum of first 5 natural numbers:", sum_natural_numbers(5))