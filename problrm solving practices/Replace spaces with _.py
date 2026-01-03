def space(s,i):
    if i==len(s):
        return ""
    if s[i] == ' ':
        return '_' + space(s,i+1)
    else:
        return s[i]+ space(s,i+1)
s="i love ptythin yhu"
print(space(s,0))