text='the the the'
m=''
for ch in text:
    if ch.isspace():
        m+='-'
    else:
        m+=ch
print(m)
