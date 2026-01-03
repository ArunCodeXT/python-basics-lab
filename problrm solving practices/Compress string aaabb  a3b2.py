def compress(s,i,count):
    if i == len(s):
        return ""
    if i==len(s)-1 or s[i]!=s[i+1]:
        return s[i]+chr(ord('0')+count)+compress(s,i+1,1)
    else:
        return compress(s,i+1,count+1)
s="aaabb"
print(compress(s,0,1))