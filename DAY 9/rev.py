'''to reverse a given number using recursion'''
def reverse_number(n):
    if n < 10:
        return n
    else:
        return (n % 10) * (10 ** (len(str(n)) - 1)) + reverse_number(n // 10)

print("Reverse of 12345:", reverse_number(12345))