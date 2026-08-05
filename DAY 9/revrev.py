
'''to print numbers from N to 1 using recursion'''
def print_numbers_reverse(n):
    if n > 0:
        print(n, end=" ")
        print_numbers_reverse(n - 1)
print_numbers_reverse(5)
