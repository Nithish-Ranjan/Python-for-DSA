'''check whether a string is a palindrome using recursion'''
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

print( is_palindrome("racecar"))
print( is_palindrome("hello"))