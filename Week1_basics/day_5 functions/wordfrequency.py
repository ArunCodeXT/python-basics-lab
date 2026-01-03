def word_freq(sentence):
    word=sentence.lower().split()
    freq={}
    for s in word:
        if s in freq:
            freq[s]+=1
        else:
            freq[s]=1
    return freq
print(word_freq("python is fun and python is easy"))
