def swap(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b
a = int(input())
b = int(input())
print(swap(a,b))