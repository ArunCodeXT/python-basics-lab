def freqq(s,i,freq,result):
    if i==len(s):
        return result
    ch=s[i]
    if ch not in freq:
        freq[ch]=True
        result=result+ch
    return freqq(s,i+1,freq,result)
s="swiss"
f=freqq(s,0,{},"")
print(f)