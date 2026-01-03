text=input("Enter string:")
word=text.split()
words={}
for ch in word:
    if ch in words:
        words[ch]+=1
    else:
        words[ch]=1
print(words)
    