text='code'
result=''
for i in range(len(text)):
    result+=text[i]
    if i!=len(text)-1:
        result+='.'
print(result)