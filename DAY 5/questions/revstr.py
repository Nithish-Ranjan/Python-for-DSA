s = input("Enter a string: ")
# chars = list(s)
# st = 0
# end = len(chars) - 1

# while st < end:
#     chars[st], chars[end] = chars[end], chars[st]
#     st += 1
#     end -= 1

# print("Reversed string:", "".join(chars))
s = s[::-1]
print(s)