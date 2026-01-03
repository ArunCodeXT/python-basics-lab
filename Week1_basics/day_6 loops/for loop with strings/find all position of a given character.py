text=input("enter string:")
string=input("enter to charcter to find:")
text1=[]
for i in range(len(text)):
    if string==text[i]:
        text1.append(i)
print(f"character{string} at position {text1}")