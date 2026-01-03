a=[1,2,4,6]
ch=len(a)+2
lst=[]
for num in range(1,ch+1):
    found=False
    for i in range(len(a)):
        if a[i]==num:
            found=True
            break
    if not found:
        lst.append(num)
print(lst)

