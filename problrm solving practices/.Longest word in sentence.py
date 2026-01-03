s="i love competitve programming"
mx_len=0
mx_word=""
cur_len=0
cur_word=""
for ch in s:
    if ch !=' ':
        cur_word+=ch
        cur_len+=1
    else:
        if cur_len > mx_len:
            mx_len=cur_len
            mx_word=cur_word
        cur_word=""
        cur_len=0
if cur_len>mx_len:
    mx_word=cur_word
print(mx_word)
