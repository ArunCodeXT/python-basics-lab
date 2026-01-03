text=input("Eneter string:")
string=text.split()
count=0
for ch in string:
    if ch == 'the':
        count+=1
print(count)