'''
a=input("enter string:").strip()
count=0
for ch in a:
    if ch in "aeiouAEIOU":
        count+=1
print(count)
'''
def string1(s,i):
    if i==len(s):
        return 0
    if s[i] in "aeiouAEIOU":
        return 1 + string1(s,i+1)
    else:
        return string1(s,i+1)
s='helloworld'
print(string1(s,0))