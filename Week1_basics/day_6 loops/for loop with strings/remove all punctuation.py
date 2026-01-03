text=input("Enter string:")
word=''
for ch in text:
    if ch.isalnum() or ch==' ':
        word+=ch
    else:
        continue
print(word)