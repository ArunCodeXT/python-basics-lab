"""
n=int(input("enter number:"))
for i in range(1,n+1):
    print(i)
"""
"""
n=int(input("enter num:"))
i=1
while i<=n:
    print(i)
    i+=1
"""
def number(i,n):
    if i>n:
        return
    print(i)
    number(i+1,n)
number(1,10)