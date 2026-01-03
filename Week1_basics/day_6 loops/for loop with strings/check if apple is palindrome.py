text='apple'
palindrome=''
for ch in range(len(text)-1,-1,-1):
    palindrome+=text[ch]
if ch==palindrome:
    print('palindrome',text)
else:
    print('not palindrome',text)
