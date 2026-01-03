def string(s,left,right):
    if left>=right:
        return 0
    s[left],s[right]=s[right],s[left]
    return string(s,left+1,right-1)
s="helloworld"
slist=list(s)
string(slist,0,len(s)-1)
sttr="".join(slist)
print(sttr)
