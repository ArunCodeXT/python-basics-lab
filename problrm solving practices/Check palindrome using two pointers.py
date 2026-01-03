s="tene"
lst=[]
for ch in s:
    lst.append(ch)
left=0
right=len(s)-1
is_palindrome=True
while left<right:
    if lst[left]!=lst[right]:
        is_palindrome=False
        break
    left+=1
    right-=1
if is_palindrome:
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")
