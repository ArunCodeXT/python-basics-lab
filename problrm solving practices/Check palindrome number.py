def reverse(n,rev):
    if n==0:
        return rev
    last=n%10
    return reverse(n//10,rev*10+last)
def palindrome(n):
    reversednum=reverse(n,0)
    if n==reversednum:
        return f"{n} is palindrome"
    else:
        return f"{n} is not a palindrome"
print(palindrome(121))