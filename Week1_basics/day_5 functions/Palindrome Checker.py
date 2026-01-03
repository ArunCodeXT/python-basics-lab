def is_palindrome(value):
    s = str(value)
    return s == s[::-1]

print(is_palindrome(121))   # True
print(is_palindrome("madam"))  # True
print(is_palindrome("python")) # False
 