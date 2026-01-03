def reverse(n,rev):
    if n==0:
        return rev
    last=n%10
    return reverse(n//10,rev*10+last)
result=reverse(123,0)
print(result)