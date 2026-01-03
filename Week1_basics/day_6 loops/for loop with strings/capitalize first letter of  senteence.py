txt=input("Enter sentence:")
text=txt.split()
for i in range(len(text)):
    chh=text[i][0].upper() + text[i][1:]
    print(chh,end=' ')