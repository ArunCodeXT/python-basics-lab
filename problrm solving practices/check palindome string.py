def palindrome(s,i):
    if i<0 :
        return ""
    return s[i] + palindrome(s,i-1)
def compare(s):
    rev=palindrome(s,len(s)-1)
    if s==rev :
        return f"{s} is a palindrome"
    else:
        return f"{s} is not a aplaindrome"
s="malayalam"
print(compare(s))    

    