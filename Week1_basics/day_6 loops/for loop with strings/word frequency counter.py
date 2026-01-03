text='HELLO WORLD HELLO'
word=""
words=[]
for ch in text:
    if ch !=' ':
        word+=ch
    else:
        words.append(word)
        word=""
words.append(word)
counted=[]
for w in words:
    if w not in counted:
        count=0
        for w2 in words:
            if w==w2:
                count+=1
        print(w,"-",count)
        counted.append(w)

