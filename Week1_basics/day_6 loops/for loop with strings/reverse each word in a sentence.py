text="python rocks"
word=text.split()
words=''
for ch in word:
    reversed_word=''    
    for i in range(len(reversed_word)-1,-1,-1):
        reversed_word += ch[i]
    words +=reversed_word + ' '
print(reversed_word.strip())