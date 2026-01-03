def freque(s,i,freq):
    if i==len(s):
        return freq
    ch=s[i]
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
    return freque(s,i+1,freq)
s="aajjeuei hhh si f i i ggg h"
print(freque(s,0,{}))